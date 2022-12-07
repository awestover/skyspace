\newcommand{\R}{\mathbb{R}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\K}{\mathbb{K}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\set}[1]{\{#1\}}
\newcommand{\setof}[2]{\{#1 \mid #2\}}
\newcommand{\im}{\mathrm{im}}

\DeclareMathOperator{\polylog}{\text{polylog}}
\DeclareMathOperator{\poly}{\text{poly}}
\DeclareMathOperator{\E}{\mathbb{E}}
\DeclareMathOperator{\Var}{\text{Var}}

Showing that BPP can do some surprising problems.
read-once Branching program evaluation

trick:
"arithmetize" the boolean circuit.
This means extend it to be a function over the integers.

"while two boolean functions might only disagree in a single
place, if you arithmetize different boolean functions they are
gonna disagree in a lot of places. That's because Polynomials
aren't too bouncy."


