import os
from os.path import join
import sys
from datetime import datetime
from random import choice as rchoice

os.chdir(join(os.environ["SKYSPACE"], "posts"))


IMAGES = ["images/rat.png", "images/blob.png", "images/cat.png"]

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
      this_entry += f"<a href='posts/{dir}/{file}'>{title}</a>\n"
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
    f.write(topics[dir])
    # future: this is just part of what we write, this needs to be injected into something else

os.chdir("..")
with open("topic-elts.html", "w") as f:
  for dir in topics:
    f.write(f"<h1>{dir}</h1>")
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

