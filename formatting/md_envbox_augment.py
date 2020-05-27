import sys
import os

try:
    file = sys.argv[1]
except:
    sys.exit("ERROR: Please input a file to eat")

environment_types = ["thm", "rmk", "prop", "ex", "cor", "lem", "clm", "defn", "pf"]
long_name = {
    "thm": "Theorem",
    "rmk": "Remark",
    "prop": "Proposition",
    "ex": "Example",
    "cor": "Corollary",
    "clm": "Claim",
    "lem": "Lemma",
    "defn": "Definition",
    "pf": "Proof"
}

looking_for_closure = False
start_environment = ""

out_text = ""
with open(file, "r") as f:
    for row in f:
        row_handled = False
        if not looking_for_closure:
            for env_type in environment_types:
                if row.strip() == f"begin {env_type}":
                    looking_for_closure = True
                    start_environment = env_type
                    out_text += f'<div class="{start_environment} envbox">**{long_name[start_environment]}.**\n'
                    row_handled = True
                    break
        elif looking_for_closure:
            if row.strip() == f"end {start_environment}":
                looking_for_closure = False
                out_text += f"</div>\n"
                unclosed_stack = []
                start_environment = ""
                row_handled = True
        if not row_handled:
            out_text += row

if looking_for_closure:
    sys.exit("ERROR: no closure!")


path_start, path_end = os.path.split(file.replace(".md", ".aug.md"))
out_path = os.path.join(path_start, "data", path_end)

with open(out_path, 'w') as f:
    f.write(out_text)


