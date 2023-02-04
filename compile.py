import os
from os.path import join
import sys

BASEDIR=os.environ["SKYSPACE"]
os.chdir(BASEDIR)

with open ("formatting/tex_macros.tex", "r") as f:
  tex_macros = f.read()

long_name = {
  "thm": "Theorem",
  "rmk": "Remark",
  "prop": "Proposition",
  "ex": "Example",
  "cor": "Corollary",
  "clm": "Claim",
  "lem": "Lemma",
  "defn": "Definition",
  "pf": "Proof", 
  "quote": "Quote"
}
environment_types = list(long_name.keys())

IMAGES = [
  ("<rat>", "<img src='../../images/rat.png' width='25%'>"),
  ("<cat>", "<img src='../../images/cat.png' width='25%'>"),
  ("<blob>", "<img src='../../images/blob.png' width='25%'>")
]

def augment_md(body):
  looking_for_closure = False
  start_environment = ""

  out_text = ""
  for row in body:
    if "@importpdf:" in row:
      xxx = row.replace("@importpdf: ", "")
      out_text += f'<iframe src="src/{xxx}.pdf" width="100%" height="700px">\n'

    row_handled = False
    if not looking_for_closure:
      for env_type in environment_types:
        if row.strip() == f"begin {env_type}":
          looking_for_closure = True
          start_environment = env_type
          
          if start_environment == "quote":
            out_text += "---\n\n"
          else:
            out_text += f'<div class="{start_environment} envbox">**{long_name[start_environment]}.**\n'

          row_handled = True
          break
    elif looking_for_closure:
      if row.strip() == f"end {start_environment}":
        looking_for_closure = False
        if start_environment == "quote":
          out_text += "\n---\n"
        else:
          out_text += f"</div>\n"
        unclosed_stack = []
        start_environment = ""
        row_handled = True
    if not row_handled:
      if looking_for_closure and start_environment == "quote":
        out_text += "> " + row.strip() + "  \n"
      else:
        out_text += row

  if looking_for_closure:
    sys.exit("ERROR: no closure!")


  for img in IMAGES:
    out_text = out_text.replace(img[0], img[1])

  return tex_macros+out_text

def toc(contents):
  elts = []
  kill_chars = ["<br>", "?", ".", "!", "'", '"', ","]

  for label in contents:
    id_name = label.lower().replace(" ", "-")
    for char in kill_chars:
      id_name = id_name.replace(char, "")
    elts.append(f'<li> <a href="#{id_name}" class="js-scroll-trigger">{label}</a> </li>')

  return "\n".join(elts)

for folder in os.listdir(join(BASEDIR,"posts")):
  os.chdir(join(BASEDIR,"posts", folder, "src"))

  for fname in os.listdir():
    if ".md" in fname:
      real_name = fname.replace(".md", "")
      with open(fname, "r") as f: 
        all_rows = []
        for row in f:
          all_rows.append(row)

      title = ""
      contents = []
      description = ""
      body = []

      stages = ["{title}", "{contents}", "{description}", "{body}"]
      stage = 0
      for i in range(1,len(all_rows)):
        #  print(stages[stage])
        if stages[stage] == "{body}":
          body.append(all_rows[i])
        elif all_rows[i].strip() == stages[stage+1]:
          stage += 1
        elif stages[stage] == "{title}":
          title += all_rows[i]
        elif stages[stage] == "{contents}":
          contents.append(all_rows[i])
        elif stages[stage] == "{description}":
          description += all_rows[i]
    
      aug_loc = join("compiled", real_name+".aug.md")
      with open(aug_loc, "w") as f:
        f.write(augment_md(body))
      #  with open(join("compiled", real_name+".toc.html"), "w") as f:
      #    f.write(toc(contents))

      os.system(f"pandoc --mathjax {aug_loc} -o compiled/{real_name}.content.html")

      with open(f"compiled/{real_name}.content.html", "r") as f:
        compiled_body = f.read()

      with open(join(BASEDIR, 'formatting/template.html'), "r") as f:
        template = f.read()

      template = template.replace("***CONTENT REPLACE THING 3899259***", compiled_body)
      template = template.replace("***TOC REPLACE THING 322946***", toc(contents))
      
      with open(f"../{real_name}.html", "w") as f:
        f.write(template)
      with open(f"../{real_name}.metadata.txt", "w") as f:
        f.write(title)
        f.write(description)


