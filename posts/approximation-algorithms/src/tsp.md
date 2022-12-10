{title}
approx tsp
{contents}
{description}
Travelling Salesman Problem (TSP) is one of the most famous
NP-hard problems. Today, we are going to solve it really fast!
(well, really just approximate it to within a factor of 1.5, but
 still).
{body}

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

Consider the following relaxation of TSP: 
Find a minimal-cost connected sub-graph spanning the graph. Now
of course, the TSP tour is a connected sub-graph spanning the
graph.  
But actually the minimal-cost connected sub-graph spanning the
graph is just the Minimum spanning tree (MST).

of course the MST is not really path-y. But actually we can turn
it into a path not too hard.

begin prop
If you just do a DFS traversal of the MST you get a 2-approx for
TSP.
end prop
begin pf
clearly $2MST \leq 2TSP$, so its cost is $2$-competitive. On the
other hand, it is a tour! yay.
end pf

So that was easy, and computing MSTs is easy. epic.
On the other hand, we can actually do better!

begin thm
we can do a 1.5 approx to TSP pretty dang fast
end thm
begin pf
take the vertices in the MST with odd degree and form a min-cost
matching on them.
This turns the MST into an eulerian graph, so it defines a path.
on the other hand, one possible matching is taking less than
every other edge in the TSP tour. So we are 1.5 compettive.

end pf

finally, apparently some dudes got like 1.4999 or something.



