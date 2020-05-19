
import sys
import os

## toc.txt --> toc.html

try:
    file = sys.argv[1]
except:
    sys.exit("ERROR: Please input a file to eat")

elts = []

with open(file, "r") as f:
    for line in f.readlines():
        real_name = line.strip()

        kill_chars = ["<br>", "?", ".", "!", "'", '"', ","]
        id_name = real_name.lower().replace(" ", "-")
        for char in kill_chars:
            id_name = id_name.replace(char, "")

        elts.append(f'<li> <a href="#{id_name}" class="js-scroll-trigger">{real_name}</a> </li>')

path_start, path_end = os.path.split(file.replace(".txt", ".html"))
out_path = os.path.join(path_start, "data", path_end)

out_text = "\n".join(elts)

with open(out_path, 'w') as f:
    f.write(out_text)

