
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
    "\\begin": "begin",
    "\\end": "end",
    "\\section": "#",
    "`": "\""
}

for rule in rules:
    content = content.replace(rule, rules[rule])

"""
with this scheme we would need to allow the following things in augmd:

begin {lemma}
end {lemma}

etc
which I'm fine with. just wanted to lyk

"""

