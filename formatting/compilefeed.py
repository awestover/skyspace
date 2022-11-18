import os

HTML = ""

DIR = "/home/alek/Desktop/art/skyspace/"

for feed in os.listdir(DIR):
  if "-feed" in feed:
    HTML += f"<a href='{feed}'>{feed}</a>\n"
    with open(os.path.join(DIR,feed,"description.md"), "r") as f:
      describe = f.read()
    HTML += f"<p>{describe}</p>\n"

with open(os.path.join(DIR,"feed-elts.html"),"w") as f:
  f.write(HTML)

