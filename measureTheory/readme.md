# Measure Theory

---

> Alek: You know what's trash?

> Rand: What?

> Alek: The Reiman integral.

> Rand: How so? 

> Alek: It's just so $\mathbb{R}^n$-y yah know? And it can't even handle integrating really basic functions like the indicator function for $\mathbb{Q}\cap [0,1]$. Ugh, if only there was a better way.

> Rand: Well what could you do besides partitioning the domain, and summing over function values on each element of the partition?

> Alek: What if you instead *partition the codomain*, and then see how much of the domain fits into the codomain bins?

> Rand: How do you measure how much of the domain falls into the codomain bins?

> Alek: ***Measure Theory!!!***

--- 

# A Measure Space

OK, before defining a measure space in full generality, I'll give some super nice motivating examples that are very relatable and stuff to ease you into the topic.

So one really useful type of measure is a "probability measure" on a space.
For simplicity, let's say that we are trying to assing probabilities to subsets of $[0,1]$ "occuring". Maybe we are chosing a random number at uniform from $[0,1]$ and an event $E_S$ corresponding to a set $S\subset [0,1]$ is said to occur if the randomly chosen point lies in $S$. 
It would kinda seem like we want to define a function $\mu: \mathcal{P}([0,1]) \to [0,1] $ that maps any subset of $[0,1]$ (the powerset is denoted by $\mathcal{P}$, and is the collection of all subsets of the set) to a probability (which is by convention a number in $[0,1]$. *It turns out that this actually* **doesn't work!!!!** (As I will show shortly by constructing a subset of $[0,1]$ which isn't measurable). You need some "$\sigma$-Algebra" of subsets that the measure is going to be defined on which is not all subsets, just the subsets that we actually care about :).

---

> Rand: so let me get this straight, the first thing you are gonna do once you define a measure is show that it's broken?

> Alek: Well, I don't know if the existence of non-lesbegue-measurable sets means "measure theory is broken"

> Rand: lolllll

> Alek: idk bro, just trust me, the construction is pretty epic

> Rand: whatever you say dude...

---

Anyways, back to defining a measure on this space.
Beause the point on $[0,1]$ is being chosen uniformly at random, we probably want our probability measure function thing to have 
$\mu((a,b)) = b-a$ for any $(a,b) \subset [0,1]$. Actually we definitely want this, it is saying e.g. that the probability of chosing a number less than $1/2$ is well $1/2$ which is pretty good.
We would also like to satisfy some basic probability axioms like 

- $\mu(\emptyset) = 0$
- $\mu(A) \ge 0 \quad \forall \text{ (measurable...) } A\subset[0,1] $
- $\mu([0,1]) = 1$
- For a countable number of disjoint sets $A_1, A_2, \ldots$ we have countable additivity, i.e. $$\mu\left( \bigcup_{i\ge 1} A_i \right) = \sum_{i\ge 1} \mu(A_i)$$

It turns out that we can get all this, and the property $\mu((a,b)) = b-a$ with the following definition:

begin defn
$$\mu(E) = \inf \Big\{ \sum_{n\ge 1} l(I_n) : E \subset \bigcup_{n \ge 1} I_n \text{ where } \{\exists a_n,b_n, \text{ such that } I_n = (a_n, b_n)\}_{n\ge 1}\Big\}$$
end defn

begin rmk
In words, this says *very very very roughly (this is not a good way to describe an infimum, sorry :( )*
"the measure of a set $E$ is the limit of the sum of the lengths of the intervals in smaller and smaller interval *covers* of the set"
end rmk

begin rmk

Ok, you'll notice that this is really asymmetric, "why did we do an infimum over covers instead of a supremum over stuff contained in the set?"

Well, because its a tiny bit nicer.

The definition of measure that I gave is called "outer measure".
You can also define "inner measure" as the supremum over compact sets contained in a set.

It turns out that "inner measure = outer measure" for any measurable set.

Also countable additivity is actually only countable subaditivity if you don't restrict to measurable sets. :(

Basically "let all your sets be measurable" except if you are interested in seeing some really weird stuff.

end rmk

begin rmk
One should note that this definition of measure has all the nice properties that we wanted!

Namely, 

* $\mu(\emptyset) = 0$ because $l(\emptyset) = 0$ $\emptyset = (0,0)$ or just say that $l(\emptyset) = 0$. 
* $\mu((a,b)) = b-a $ because $(a,b)\cup \emptyset \cup \emptyset \cup \cdots$ covers $(a,b)$ 
* $\mu([0,1]) = 1$ (above)
* countable (sub?)-additivity (ok, so we unfortunately don't have countable additivity yet... this is beacause of those dang non-measurable sets and stuff. don't worry, we get this once we define our sigma algebra)
* measure is non-negative : well length is so yup, we're good

end rmk

begin rmk
Measure has a lot of really nice properties:

- translation invariant: $\mu(x+E) = \mu(E)$
- monotone: $A\subset B \implies \mu(A) \le \mu(B)$

end rmk

begin rmk

We really want countable additivity, so we introduce the "splitting condition" which says for a set $A$ that 

$$\mu(X)  = \mu(X \cap A) + \mu(X \setminus A) \quad \forall X \subset \mathbb{R}$$

If $A$ satisfies this, then $A$ satisfies this, then $A$ satisfies this, then $A$ satisfies this, then $A$ is said to be Lesbegue measurable, and we get countable additivity, not lame subaditivity. yay!

end rmk


# An unmeasurable set!!!

OK, I just defined measure like half a minute ago. Now seems like a good time to show that defining it as a function on all subsets of $[0,1]$ is not a great idea. More specifically, there are subsets of $[0,1]$ that aren't measurable!! (with the axiom of choice... (Just for fun, a quote from a stackoverflow article "The sentence 'outermeasure is not finitely additive' is independent from ZF+DC") luckily we aren't crazy set theorists and accept ZFC :) (set theory sounds pretty interesting, but I really like choice. Trust me $\exists$ weird stuff with choice))

Anyways, the following is true:

begin thm
$\exists V \subset [0,1]$ that isn't measurable
end thm

begin pf

Break $[0,1]$ up into equivalence classes based on the relation that 
$$x \sim y \iff x-y \in \mathbb{Q}$$
That is, consider $[0,1]/\mathbb{Q}$. WOW! WEIRD!

This means that for an equivalence class $\overline{x}$, any pair of elements in $\overline{x}$ differ from each other by some rational (a potentially different rational for each pair). 

So there are an uncountably infinite number of equivalence classes, things
like $\mathbb{Q}, \mathbb{Q} + \pi, \mathbb{Q}+e$ and stuff.

We then form a set $V_0$ by taking an element from each equivalence class. This is a lot of axiom of choice-ing!!! Like hard core axiom of choice. I digress.

Now we will consider sets $V_q$ for $q\in\mathbb{Q}\cap [-1,1]$ defined as $V_q = q+V_0$. That is, we consider translations of $V_0$ by all rationals on $[-1,1]$.

Note that $V_q \cap V_p \neq \emptyset \iff p = q$ because
imagine $x \in V_q \cap V_p$, this implies $x-q, x-p \in V_0$. Now consider $x-q - (x-p) = p-q$. This difference must be $0$, because we chose exactly one element from each equivalence class, so all distinct elements in $V_0$ differ by an irrational. Hence, $p=q$ and $V_p = V_q$.

OK but here's the problem. Yeah they're disjoint, but they still cover $[0,1]$.
Here's why, consider any $x \in [0,1]$. Well consider the element from the equivalence class that $x$ is in that is in $V_0$, which we'll call $y$. We know that $x-y \in \mathbb{Q}$ and more specifically $x-y \in \mathbb{Q} \cap [-1, 1]$. And we have access to all rational shifts of $y$ on $[-1,1]$. So we have $x$.
But also clearly $\cup_{q\in\mathbb{Q}} V_q \subset [-1,2]$ because $V_0 \subset [0,1]$ and the points are shifted by at most $\pm 1$. 

OK, now here's the killer blow as they say: countable additivity of disjoint sets measures!

$$ \mu\left(\bigcup_{q\in\mathbb{Q}} V_q\right) = \sum_{q\in\mathbb{Q}}\mu(V_q)  $$
Clearly measure is translation invariant so $\mu(V_q) = V_0 \forall q$.
Hence
$$ \mu\left(\bigcup_{q\in\mathbb{Q}} V_q\right) = \sum_{q\in\mathbb{Q}}\mu(V_0)  $$

Oh no.

$$[0,1] \subset \mu\left(\bigcup_{q\in\mathbb{Q}} V_q\right) \subset [-1,2]$$

Yeah that's right, so by monotonicity of measure
$$ 1 \le \mu\left(\bigcup_{q\in\mathbb{Q}} V_q\right) \le 3$$
But then, 
$$ 1 \le  \sum_{q\in\mathbb{Q}}\mu(V_0)  \le 3$$
Well $\mu(V_0)$ can't be $0$, or the sum would be 0, which is too small. And also $\mu(V_0)$ can't be $\epsilon > 0$ or the sum would be infinite which is too big.
Ahggg!! its' un unmeasurable subset of $\mathbb{R}$.



end pf

# Lesbegue Integration

Now we're going to talk about lesbegue integration.

recall that in reimann integration the idea is to partition the domain up, and take one funciton value per each part of the domain.

Here's Lesbegue integration:
Partition the codomain, and multiply function values by the measure of their preimages!!! 



# Lesbegue's dominated convergence theorem

Do you think that 

$$\lim_{n\to \infty} \int f_n = \int \lim_{n\to\infty} f_n$$
Well it turns out that this isn't true of all function sequences.

Lesbegue's dominated convergence theorem says that it is true of functions that are dominated (bounded in magnitude, maybe in support too).

Here's a counterexample if you don't have that constraint though

$$f_n(x) = 1_{[n,n+1]}$$
That is, $f_n$ is the indicator function for the interval $[n,n+1]$

We have 
$$\int f_n = 1 \forall n \implies \lim_{n\to\infty} \int f_n = 1$$
But, 

$$\lim_{n\to\infty} f_n \cong 0$$
so $$\int \lim f_n = 0$$





