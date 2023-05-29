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
\newcommand{\floor}[1]{\left\lfloor #1 \right\rfloor}
\newcommand{\ceil}[1]{\left\lceil #1 \right\rceil}




# the marriage problem

Bob has a pool of $n$ people that he is willing to date. Each of
these $n$ people has some **"goodness-score"** that Bob is able to
discover after dating them for a week. Bob writes the people's
names down on a list in a random permutation, and plans to go
down the list dating people, until he stops and chooses someone
to marry. After dating someone for a
week Bob must either decide whether to reject the person or marry
them. This decision cannot be reversed once made. 
**The Question:** What is the optimal dating strategy for Bob,
where by optimal we mean the strategy that maximizes Bob's
probability of ending up married to the person with the highest
goodness-score?

This problem is both theoretically interesting as a neat
combinatorial puzzle, and practically interesting; the
applications of an optimal dating strategy are clear.

<div class="lem envbox">**Lemma.**
The optimal strategy must be of the form 
"date $k$ people without considering them, and then marry the
first person after the $k$-th person who has a higher
goodness-score then any of the first $k$ people that you dated."
</div>
<div class="pf envbox">**Proof.**
Obviously the optimal strategy never consists of choosing someone
worse than the people that you've already seen; doing so is never
productive towards achieving the best person.

Every time Bob finishes dating someone and they have a
goodness-score higher than all previously seen goodness-scores,
Bob has two choices: he can marry them, or not.

Bob may as well write down on his list a $0$ or a $1$ next to
people's names based on which of these situations he will choose. 
That is, if next to name $i$ Bob writes a $0$, then Bob is not
going to marry person $i$ no matter what, and if next to name $i$
Bob writes a $1$ then Bob is going to marry person $i$ if and
only if Bob has not married some person $j < i$ and person $i$
had goodness-score higher than all people $j < i$.

We claim that in the optimal strategy all the $1$'s on Bob's list
are at the bottom of the list, and all the $0$'s are at the top.

Consider a list where this is not the case. In particular, say
that for people $i, j$ with $i < j$ there is a $1$ on person
$i$'s name and a $0$ on person $j$'s name.
We claim that by swapping the $0$ and the $1$ we get a better
strategy (in terms of probability). We prove this by considering
when it is better to swap.

- If the best person is some $k < i$ then it doesn't matter at all whether or not we swap
- If $i$ is the best person, then it is obviously better to not swap 
- If $k > i$ is the best person, then actually swapping is a
really good idea. Having an extra baseline measurement is pretty
helpful for declining future people. 

We leave computing the exact probabilities as an exercise for the interested reader.

</div>

Now that we know essentially what Bob's strategy should look
like, we optimize the parameter $k$.
<div class="thm envbox">**Theorem.**
The optimal number of people to use as a baseline is
approximately $n/e$ for large $n$. By setting $k \approx n/e$ Bob
gets an approximately $1/e$ chance of marrying the person with
the highest goodness-score.
</div>
<div class="pf envbox">**Proof.**
Say that Bob is using the strategy "marry the first person better
than all of the first $k$ people". We now compute the probability
that Bob marries the best person by using this strategy.

Of course there is a $k/n$ chance that the best person is one of
the first $k$ people Bob dates. In this case Bob just loses. :(

Now we condition on the best person not being one of the first
$k$ people that Bob dates; this happens with probability
$(n-k)/n$.

In this case the probability that Bob wins can be computed by
summing over values of who the best person is, and for each of
these values determining what the probability is that Bob wasn't
tricked in to marrying someone earlier.

If person $i$ is the best, then Bob wins if and only if the
second best person, from among the first $i$ people, is among the
first $k$ people. This happens with probability $\frac{k}{i-1}$.
Hence the probability of Bob winning is 

$$\frac{n-k}{n} \sum_{i=k+1}^n \frac{1}{n-k} \cdot \frac{k}{i-1}
\approx \frac{k}{n}\ln (n/k),$$
where we have used the fact that $\sum_{i=1}^n 1/i \approx \ln n$
which can be seen by considering the integral of the function
$x\mapsto 1/x$ and Reiman approximations to this integral, using
rectangles of width $1$.

Now we optimize $-x\ln x$; the optimal value of $k/n$ will be
adjacent to $x$ by monotonicity. 

$$\frac{d}{dx} x\ln x = 1+\ln x.$$
Clearly the derivative of our function is $0$ at $x=1/e$.

Hence setting $k \approx n/e$ is the optimal setting for $n$
large enough that our estimates have been resonable.

Another interesting fact is that the optima of $-x\ln x$ is
$1/e$, meaning that Bob's optimal strategy has about a $36%$
chance of succeeding, which all things considered is not bad.

</div>

This result will undoubedly prove incredibly useful for any
reading this. The assumptions made in our model of dating are
completly legitamite. One word of caution however, is that we
have not considered the possibility that modifying Bob's dating
strategy could affect the distribution of people available for
him to date. This minor concern is alleviated by Bob simply not
advertising that he is following this strategy.

**Future work**:
It would be quite interesting to empirically evaluate the
effectiveness of this strategy. Please contact the author if you
are able to produce any such data.

