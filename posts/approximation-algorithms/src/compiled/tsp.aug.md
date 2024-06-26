\newcommand{\one}{\mathbbm{1}}
\newcommand{\bigO}{\mathcal{O}}
\DeclareMathOperator{\E}{\mathbb{E}}
\DeclareMathOperator{\Var}{\text{Var}}
\DeclareMathOperator{\Hom}{Hom}
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\sgn}{sgn}
\DeclareMathOperator{\Id}{Id}
\DeclareMathOperator{\img}{Img}
\DeclareMathOperator{\polylog}{\text{polylog}}
\DeclareMathOperator{\poly}{\text{poly}}
\newcommand{\st}{\text{ such that }}
\newcommand{\norm}[1]{\left\lVert#1\right\rVert}
\newcommand{\interior}[1]{ {\kern0pt#1}^{\mathrm{o}} }
\newcommand{\mb}{\mathbf}
\newcommand{\partition}{\vdash}
\newcommand{\x}{\mathbf{x}}
\newcommand{\y}{\mathbf{y}}
\newcommand{\z}{\mathbf{z}}
\newcommand{\eps}{\varepsilon}
\renewcommand{\d}{\mathrm{d}}
\renewcommand{\Re}{\mathrm{Re}}
\renewcommand{\Im}{\mathrm{Im}}

\newcommand{\setof}[2]{\left\{ #1\; : \;#2 \right\}}
\newcommand{\set}[1]{\left\{ #1\right\}}

\newcommand{\R}{\mathbb{R}}
\newcommand{\Q}{\mathbb{Q}}
\newcommand{\C}{\mathbb{C}}
\newcommand{\Z}{\mathbb{Z}}
\newcommand{\F}{\mathbb{F}}
\newcommand{\K}{\mathbb{K}}
\newcommand{\N}{\mathbb{N}}
\newcommand{\contr}{\[ \Rightarrow\!\Leftarrow \]}
\newcommand{\defeq}{\vcentcolon=}
\newcommand{\eqdef}{=\vcentcolon}

\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}
\newcommand{\paren}[1]{\left( #1 \right)}
\newcommand{\ang}[1]{\langle #1 \rangle}
\newcommand{\abs}[1]{\left| #1 \right|}


# the problem

ok so TSP on an arbitrary graph is actually just too hard: 
there might not even be a hamiltonian cycle in the graph, and
checking this is already NP-complete.
So as a simplification we are just going to consider some nice
graphs.

In particualr, we consider graphs that define metric spaces:
i.e. all edges are defined, and the edge-costs satisfy the
triangle inequality.
$$w_{a\to b} + w_{b\to c} \geq w_{a\to c}.$$
This is a fairly reasonable set of graphs, and it has the nice
property that by virtue of being complete there will always be a
hamiltonian cycle. Nice.

OK but TSP is still NP-hard on these nicer graphs.
What to do? Well let's just approximate it.

# approximation algorithm

Consider the following relaxation of TSP: 
Find a minimal-cost connected sub-graph spanning the graph. Now
of course, the TSP tour is a connected sub-graph spanning the
graph. 
But actually the minimal-cost connected sub-graph spanning the
graph is just the Minimum spanning tree (MST).

of course the MST is not really path-y. But actually we can turn
it into a path not too hard.

<div class="prop envbox">**Proposition.**
If you just do a DFS traversal of the MST you get a 2-approx for
TSP.
</div>
<div class="pf envbox">**Proof.**
clearly $2MST \leq 2TSP$, so its cost is $2$-competitive. On the
other hand, it is a tour! yay.
</div>

So that was easy, and computing MSTs is easy. epic.
On the other hand, we can actually do better!

<div class="thm envbox">**Theorem.**
we can do a 1.5 approx to TSP pretty dang fast
</div>
<div class="pf envbox">**Proof.**
take the vertices in the MST with odd degree and form a min-cost
matching on them.
This turns the MST into an eulerian graph, so it defines a path.
on the other hand, one possible matching is taking less than
every other edge in the TSP tour. So we are 1.5 compettive.

</div>

finally, apparently some dudes got like 1.4999 or something.



