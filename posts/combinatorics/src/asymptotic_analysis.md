{title}
asymptotic analysis
{contents}
{description}
what are functions look like
{body}

# asymptotic analysis

Now, I have mixed feelings about asymptotic analysis.

On the ond hand, estimating functions is pretty cool.
On the other hand, sometimes asymptotic analysis feels a little
bit too "computy" to me.
Like you have to do calculus, and there are often really nasty
expressions. 

I think the key to having a good expereience with asymptotic
analysis is to have a good understanding of functions.

Hence this little blog post in which I'm going to write down a
bunch of ineqaulities that are often rpetty useful. 

# general stuff

Bernouli's Identity:
For $x\ge -1, r \in \Z_{\ge 0}$
$$(1+x)^r \ge 1+rx$$

Also, 
for $x\ge -1, r\ge 1$ ($r\in\R$)
$$(1+x)^r \ge 1+rx$$

for $x\ge -1, r\in [0,1]$ ($r\in\R$)
$$(1+x)^r \le 1+rx$$

(equality at $r=1$)

For $p>0$
$$1-xp\le e^{-xp}$$
Here's another version of this one (you get it by taking the
$\ln$ of the above):
$$\ln \frac{1}{1-xp} \ge xp.$$

This one is super common! So I'll write it again, 
$$1-\delta \le e^{-\delta}$$ 
and
$$\ln \frac{1}{1-\delta} \ge \delta$$
these two are valid for all $\delta \in \R$, but they're really
tight (i.e. useful) when $0< \delta\ll 1/2$.

For $\delta\approx 0$
$$1-\delta \approx \frac{1}{1+\delta}$$ 

### series

$$\ln x \le \sum_{i=1}^x 1/i \le \ln x + 1$$

### quadratics:
$$x^2 \ge 0$$
$$a(x-h)^2+k \ge k$$


# calculus:
$f'(x_0) = 0$ and $f''(x_0) > 0$ then $x_0$ is a local minimum of
your function.

Taylor's Inequality:
For simplicity I take the domain of $f$ to be the region of
convergence of its taylor series. If $f$ used to have a bigger
domain, consider the restriction of $f$ to this domain.

Say we have some infinitely differentiable $f$; consider the
Taylor Series for $f$ about $x=a$.

Let 
$$P_k(x) = \sum_{i=0}^k \frac{f^{(i)}(a)}{i!}(x-a)^i$$
$$S_k(x) = \sum_{i=k}^\infty \frac{f^{(i)}(a)}{i!}(x-a)^i$$

Then $f(x) = P_k(x) + S_k(x).$
Say we are interested in bounding $f(x) - P_k(x)$. Of course this
can be accomplished by bounding $S_k(x)$.
That wasn't so scary now, was it!

The more typical way to write this is to observe that 
$$S_k(x) = \frac{f^{(k+1)}(x)}{(k+1)!}(x-a)^{k+1}$$
and then say

$$f(x) - P_k(x) = \frac{f^{(k+1)}(x)}{(k+1)!}(x-a)^{k+1}$$

But really we want an inequality. So we take any $M$ that is an
upper bound for $S_k(x)$ i.e. $M \ge S_k(x)$ for all $x$ (in the
    domain). Given such a choice of $M$ we have
$$f(x) - P_k(x) \le \frac{M}{(k+1)!}(x-a)^{k+1}$$

Another form of Taylor's Theorem is just that 
$$f(x) - P_k(x) \le o(|x-a|^k)$$
as $x\to a$ (this little-$o$ notation is a bit weird, but I'll live with it) which is nice.

# Binomial stuff

$$\binom{n}{k} \le 2^n$$
$$\binom{n}{k} \le \frac{n^k}{k!}$$
$$\left(\frac{n}{k}\right)^k \le \binom{n}{k} \le \left(\frac{ne}{k}\right)^k$$

[This nice little handout on binomial bounds](http://page.mi.fu-berlin.de/shagnik/notes/binomials.pdf) gives some more specific bounds:

If $k\le o(\sqrt{n})$
then $$\binom{n}{k} = (1+o(1))\frac{n^k}{k!},$$
which is tight up to a multiplicative $O(\sqrt{k})$ error.

If $k\le o(n)$
$$\log \binom{n}{k}  = (1+o(1)) k \log n/k$$

If $k\ge \Omega(n)$ then
$$\binom{n}{k} = 2^{\Omega(n)}$$
specifically $\binom{n}{k} \approx 2^{n\cdot H(k/n)}$ where $H$
is the binary entropy funcion $H(p) = -p\log p - (1-p) \log (1-p).$ 


# sums

AM-GM is a classic
$$\frac{1}{n}\sum_{i=1}^n a_i \ge \prod_{i=1}^n a_i^{1/n}$$

Who could stand to not have the triangle inequality
$$|\sum x_i | \le \sum |x_i|$$

Cauchy-shwarz, another classic
$$\Big|\sum a_i b_i \Big|^2 \le \sum a_i^2 \sum b_i^2$$

[aops has some generlaizations of AM-GM here](https://artofproblemsolving.com/wiki/index.php/Root-Mean_Square-Arithmetic_Mean-Geometric_Mean-Harmonic_mean_Inequality)
[power mean inequality](https://artofproblemsolving.com/wiki/index.php/Power_Mean_Inequality)

power mean inequality:
For any $a_1,\ldots, a_n \ge 0$ and $k_1, k_2 \in \R$ with $k_1\ge k_2$
$$\left(\frac{1}{n} \sum a_i^{k_1} \right)^{1/k_1} \ge
\left(\frac{1}{n} \sum a_i^{k_2} \right)^{1/k_2} $$

weighted AM-GM:
$$\sum \lambda_i a_i \ge \prod a_i^{\lambda_i}$$
for weights $\lambda_i\ge 0$ summing to $1$ ($\sum \lambda_i = 1$).

# probability inequalities

- Markov's Inequality
- Chebyshev's Inequality
- Chernoff Bound
- Hoeffding Bound
- Jensen's Inequality


# That's It so Far
Do you have an inequality that you really like that I don't have
written down? Please let me know!


