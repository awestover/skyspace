import os
from os.path import join
import sys
from datetime import datetime

os.chdir(os.environ["SKYSPACE"])

print("WELCOME to SKYSPACE")
print("Thank you for posting today! I get bored when you neglect to post.")

options = []
for f in os.listdir("posts"):
    print(len(options), f)
    options.append(f)

category_type = options[int(input("category type idx?\n>> "))]

today = datetime.now().strftime("%m-%d-%y")+".md"
new_feed = join("posts", category_type, "src")

if os.path.exists(join(new_feed, today)):
    print(f"You already wrote a blog post about {category_type} today, take the day off!")
else:
    with open(join(new_feed, today), "w") as f:
        f.write("{title}\n\n")
        f.write("{contents}\n\n")
        f.write("{description}\n\n")
        f.write("{body}\n\n")

    with open(".most_recent_feed_dir.txt", "w") as f:
        f.write(join(os.environ["SKYSPACE"], new_feed))
        with open(".most_recent_feed.txt", "w") as f:
            f.write(today)

