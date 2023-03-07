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
    blob = """
    <head>
    <link href="../../formatting/pandoc.css" rel="stylesheet">
    <link href="../../formatting/envbox.css" rel="stylesheet">
    <link href="../../formatting/bars.css" rel="stylesheet">

    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.4.1/jquery.min.js" integrity="sha256-CSXorXvZcTkaix6Yvo6HppcZGetbYMGWSFlBw8HfCJo=" crossorigin="anonymous"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery-easing/1.4.1/jquery.easing.min.js" integrity="sha256-H3cjtrm/ztDeuhCN9I4yh4iN2Ybx/y1RM7rMmAesA0k=" crossorigin="anonymous"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
    <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/mathjax/2.7.2/MathJax.js?config=TeX-AMS_CHTML-full" type="text/javascript"></script>
    </head>
    <body>
    <div class="wrapper">
      <nav id="sidebar">
        <div id="sidebar-content">
          <div class="sidebar-header">
            <h4>SkySpace</h4>
          </div>
          <ul class="list-unstyled components">
            <img style="width:100%; max-width:250px;" src="../../images/cat.png" alt="cat"/>
            <li> <a href="https://awestover.github.io">awestover.github.io</a> </li>
            <li> <a href="../../index.html">Home</a> </li>
            <li> <a href="../../about.html">About</a> </li>
            <li> <a href="../../topics.html">Topics</a> </li>
          </ul>
          <div id="canvas-parent"> </div>
        </div>
      </nav>
      <div id="content">

    """
    f.write(blob)
    # TODO: this is just part of what we write, this needs to be injected into something else
    # UPDATE: This is trash, please just actually do it right.
    # we really should have a template, and then insert this into that.

    f.write(topics[dir])
    f.write("</div></body>")

os.chdir("..")
with open("topic-elts.html", "w") as f:
  for dir in topics:
    f.write(f"<h1>{dir}</h1>")
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

