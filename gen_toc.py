
import os
BASEDIR = os.environ["SKYSPACE"]
os.chdir(BASEDIR)

with open (".most_recent_feed.txt", "r") as f:
    FEED = f.read()
with open (".most_recent_feed_dir.txt", "r") as f:
    DIR = f.read()

fname = DIR + "/" + FEED
endl = "\n"

with open(fname, "r") as f:
    title = f.readline() +  f.readline() + f.readline() 

    toc = ""
    everything_else = ""
    started = False

    for line in f.readlines():
        if not started:
            if line.strip() == "{description}":
                started = True
        if started:
            for i in range(2, 5):
                if line[:i] == (i-1)*"#"+" ":
                    toc += line[i:]
            everything_else += line

    full = title + toc.strip() + endl + everything_else.strip()

with open(fname, "w") as f:
    f.write(full)

