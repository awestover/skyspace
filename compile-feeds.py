import os
from os.path import join
import sys

os.chdir(join(os.environ["SKYSPACE"], "posts"))

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
      description = "".join(f_rows[1:])

      this_entry += f"<a href='posts/{dir}/{file}'>{title}</a>\n"
      this_entry += f"<p>[{file.replace('.html', '')}]</p>\n"
      this_entry += f"<p>{description}</p>"

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

all_feeds.sort(key=lambda x: x[0], reverse=True)
concat_feeds = "".join([x[1] for x in all_feeds])

with open("compile-feeds.html", "w") as f:
  f.write(concat_feeds)

