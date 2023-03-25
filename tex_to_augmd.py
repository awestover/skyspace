
"""
replace \begin \end with begin end

replace \section with #

replace `` with "
"""

import sys
import os

input_file = sys.argv[1]

with open(input_file, 'r') as f:
    content = f.read()

rules = {
    "\\begin": "beg ",
    "\\end": "end ",
    "\\section": "#",
    "`": "\""
}

for rule in rules:
    content = content.replace(rule, rules[rule])

output_file = input_file.replace(".tex", ".md")
with open(output_file, "w") as f:
    f.write(content)


