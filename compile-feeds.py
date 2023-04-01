import os
from os.path import join
import sys
from datetime import datetime
from random import choice as rchoice

os.chdir(join(os.environ["SKYSPACE"], "posts"))

with open("../formatting/template_minusdisquss.html", "r") as f:
  TEMPLATE = f.read()

#  IMAGES = ["images/rat.png", "images/blob.png", "images/cat.png"]
IMAGES = [join("images", img) for img in os.listdir("../images")]

all_feeds = []
topics = {}
for dir in os.listdir():
  topics[dir] = ""
  for file in os.listdir(dir):
    if ".html" in file and file != "index.html":
      this_entry = ""
      with open(join(dir, file.replace(".html",".metadata.txt")),"r") as f:
        f_rows = []
        for row in f:
          f_rows.append(row)
      title = f_rows[0]
      image = f_rows[1]
      description = "".join(f_rows[2:])

      this_entry += f"<div class='post-card'>\n"
      escaped_title = title.replace(" ", "-").strip()
      this_entry += f"<h5 id='{escaped_title}'><a href='posts/{dir}/{file}' class='blog-title'>{title}</a></h5>\n"
      if len(image) < 3:
        image = rchoice(IMAGES)
        this_entry += f"<img class='side-img' src='{image}'/>"
      else:
        this_entry += f"<img src='posts/{dir}/src/{image}'/>"
      this_entry += f"<p>[{file.replace('.html', '')}]</p>\n"
      this_entry += f"<p>{description}</p>"
      this_entry += f"</div>\n"

      topics[dir] += this_entry
      all_feeds.append((file.replace(".html", ""), this_entry))

  with open(join(dir, "index.html"), "w") as f:
    blob = TEMPLATE

    other_bad_images = "<img class='side-img' src='images/"
    fix_other_bad_images = "<img class='side-img' src='../../images/"

    dude = topics[dir]
    dude = dude.replace(other_bad_images, fix_other_bad_images)

    bad_image_thing  = f'posts/{dir}/'
    good_image_thing = ''
    fix_images = dude.replace(bad_image_thing, good_image_thing)

    blob = blob.replace( "***CONTENT REPLACE THING 3899259***", fix_images)
    #  blob = blob.replace("***TOC REPLACE THING 322946***", "")
    f.write(blob)

os.chdir("..")
with open("topic-elts.html", "w") as f:
  for dir in topics:
    f.write(f"<h1 class='topic-title'>{dir}</h1>")
    f.write(f"<a href='posts/{dir}'>zoom</a>")
    f.write(topics[dir])

def weird(x):
  if x[0][0] in ["0", "1"]:
    return datetime.strptime(x[0], "%m-%d-%y").strftime("%y-%m-%d")
  else:
    return "***"+x[0].lower().replace(" ", "")

all_feeds.sort(key=weird, reverse=True)
concat_feeds = "".join([x[1] for x in all_feeds])

with open("compile-feeds.html", "w") as f:
  f.write(concat_feeds)

