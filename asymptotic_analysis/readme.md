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

For $\delta\approx 0$
$$1-\delta \approx \frac{1}{1+\delta}$$ 



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


