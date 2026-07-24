# Affine-orbit spread from one strong complete mapping

PX100 develops switching flows in the full strong-complete state space.  There
is a complementary route: the affine similarity orbit of one sufficiently
nonlinear seed already has three independent field parameters.  Its low-rank
cylinder probabilities are governed by exact secant and affine-triangle
multiplicities of the seed graph.

Throughout, let \(p\) be an odd prime and let

\[
f:\mathbb F_p\longrightarrow\mathbb F_p
\]

be strong complete, so

\[
f,
\qquad x\mapsto x-f(x),
\qquad x\mapsto x+f(x)
\]

are permutations.

For

\[
\lambda\in\mathbb F_p^\ast,
\qquad
a,b\in\mathbb F_p,
\]

define

\[
T_{\lambda,a,b}f(x)
=
\lambda f\!\left(\lambda^{-1}(x-a)\right)+b.
\]

Choose the three parameters independently and uniformly.  Repetitions caused
by affine stabilizers are retained; this is a probability distribution, not
necessarily the uniform measure on the distinct orbit.

## 1. Secant and triangle multiplicities

For a nonzero slope \(r\), put

\[
\mu_f(r)
=
\#\left\{
(u,v):u\ne v,
\frac{f(v)-f(u)}{v-u}=r
\right\}.
\]

For

\[
r\in\mathbb F_p^\ast,
\qquad
t,s\in\mathbb F_p\setminus\{0,1\},
\]

put

\[
\tau_f(r,t,s)
=
\#\left\{
(u,v):u\ne v,
\begin{array}{l}
\displaystyle\frac{f(v)-f(u)}{v-u}=r,\\[2mm]
\displaystyle
\frac{f(u+t(v-u))-f(u)}{f(v)-f(u)}=s
\end{array}
\right\}.
\]

The second denominator is nonzero because \(f\) is a permutation.

Write

\[
\mu(f)=\max_r\mu_f(r),
\qquad
\tau(f)=\max_{r,t,s}\tau_f(r,t,s).
\]

## Theorem PX129 -- PROVED

Every map \(T_{\lambda,a,b}f\) is strong complete.  Under the uniform parameter
measure, every compatible matching cylinder has the following exact
probability.

### Rank one

For one row-image edge,

\[
\boxed{
\Pr(g(x)=y)=\frac1p.
}
\]

### Rank two

For distinct rows and distinct images, put

\[
r=\frac{y_2-y_1}{x_2-x_1}.
\]

Then

\[
\boxed{
\Pr(g(x_1)=y_1,\ g(x_2)=y_2)
=
\frac{\mu_f(r)}{p^2(p-1)}.
}
\]

### Rank three

For three distinct rows and images, put

\[
r=\frac{y_2-y_1}{x_2-x_1},
\qquad
 t=\frac{x_3-x_1}{x_2-x_1},
\qquad
 s=\frac{y_3-y_1}{y_2-y_1}.
\]

Then

\[
\boxed{
\Pr(g(x_j)=y_j\ (j=1,2,3))
=
\frac{\tau_f(r,t,s)}{p^2(p-1)}.
}
\]

Consequently the affine-orbit measure is rank-three spread with normalized
constants

\[
\boxed{
K_1=1,
\qquad
K_2=\frac{\mu(f)}p,
\qquad
K_3=\frac{p-2}{p}\tau(f).
}
\]

### Proof

Write

\[
u=\lambda^{-1}(x-a).
\]

Then

\[
x-g(x)
=a-b+\lambda(u-f(u)),
\]

and

\[
x+g(x)
=a+b+\lambda(u+f(u)).
\]

Thus the three required maps remain permutations.

For one prescribed edge, choose \(\lambda,a\) arbitrarily; there is one value
of \(b\).  This gives \(p(p-1)\) successful parameter triples out of
\(p^2(p-1)\).

For two edges, a successful parameter triple determines an ordered seed pair
\((u,v)\).  Conversely, if its secant slope is \(r\), then

\[
\lambda=\frac{x_2-x_1}{v-u},
\qquad
 a=x_1-\lambda u,
\qquad
 b=y_1-\lambda f(u)
\]

are uniquely determined and realize the cylinder.  The number of choices is
therefore \(\mu_f(r)\).

For three edges, the row equations additionally force

\[
u_3=u+t(v-u).
\]

The second image difference is correct exactly when the seed triangle has
output ratio \(s\).  Thus the number of parameter triples is
\(\tau_f(r,t,s)\).  Dividing by \(p^2(p-1)\) gives the exact formulas.
Multiplication by \((p)_k\) gives the normalized constants. \(\square\)

The theorem reduces affine-orbit spread to one deterministic pseudorandomness
problem on a seed graph: bound every secant slope by \(O(p)\) and every full
affine triangle shape by \(O(1)\).

## 2. Exact order-thirteen seed

Take

\[
f_{13}
=
(0,2,4,9,7,12,3,11,6,1,5,10,8).
\]

It is a nonlinear strong complete mapping.

## Theorem PX130 -- PROVED FINITE

The exact multiplicities of this seed satisfy

\[
\boxed{
\mu(f_{13})=28,
\qquad
\tau(f_{13})=8.
}
\]

Hence its affine-parameter measure has

\[
K_1=1,
\qquad
K_2=\frac{28}{13}<3,
\qquad
K_3=\frac{88}{13}<7.
\]

Among the \(13^2\cdot12=2028\) parameter triples there are \(1014\) distinct
maps.  The maximum parameter multiplicities of prescribed cylinders of ranks
one, two, and three are exactly

\[
\boxed{156,\qquad28,\qquad8.}
\]

### Proof

Direct exact enumeration gives the displayed secant and triangle tables.  The
parameter count then follows from PX129. \(\square\)

The complete order-thirteen census has a sharp class decomposition:

| Number of seeds | \(\mu(f)\) | \(\tau(f)\) |
|---:|---:|---:|
| 2,028 | 28 | 8 |
| 1,352 | 42 | 24 |
| 1,014 | 72 | 48 |
| 130 | 156 | 156 |

The final row is exactly the affine strong-complete family.  The best 2,028
seeds are the degree-two class in the PX99 switching graph.

## 3. Conditional second rainbow stage

For the two normalized protected directions, a first-stage permutation
\(\Phi\) is admissible exactly when it is strong complete.  After fixing
\(\Phi\), put

\[
P(x)=h(\Phi(x)),
\]

where \(h\) is another strong complete mapping.  Then

\[
P(x)-\Phi(x)
=h(u)-u,
\qquad
P(x)+\Phi(x)
=h(u)+u,
\qquad u=\Phi(x),
\]

are permutations.  Thus this is precisely the conditional second-stage
rainbow problem from PX96.

## Theorem PX131 -- PROVED

Normalize two protected linear colourings to the sum and difference
colourings.  Choose \(\Phi\) from the affine-parameter distribution generated
by \(f_{13}\).  Conditionally on every realized \(\Phi\), independently choose
\(h\) from the same distribution and put

\[
P=h\circ\Phi.
\]

Then \((P,\Phi)\) is protected, and for every joint prescribed cylinder of rank
\(k\le3\),

\[
\boxed{
\Pr\bigl(
\Phi(x_j)=y_j,
P(x_j)=w_j
\text{ for }j\in[k]
\bigr)
\le
\frac{49}{(13)_k^2}.
}
\]

Thus the conditional spread hypothesis PX97 is unconditionally true at local
order thirteen for two protected directions.

### Proof

PX130 gives the one-stage cylinder bound

\[
\frac7{(13)_k}
\]

for every \(k\le3\).  After conditioning on \(\Phi\), the inputs
\(\Phi(x_j)\) are distinct, and the prescribed values of \(P\) become a
matching cylinder for \(h\).  Its conditional probability is again at most
\(7/(13)_k\).  Multiply and average over \(\Phi\).  Protection follows from
the displayed sum and difference identities. \(\square\)

## 4. Revised asymptotic target

PX129 changes the infinite protected-spread problem.  It is enough to construct,
for infinitely many primes \(p\), one strong complete seed satisfying

\[
\mu(f)=O(p),
\qquad
\tau(f)=O(1),
\]

or a sufficiently mild polylogarithmic variant compatible with the downstream
local-load estimates.

This deterministic triangle-multiplicity problem may be more tractable than
rapid mixing of the complete PX98 switching graph.  The switching machinery
remains relevant as a way to construct or sample candidate low-multiplicity
seeds.

## 5. Verification

Run

```bash
python scripts/verify_product_affine_orbit_spread.py
```

The verifier enumerates all 4,524 order-thirteen strong complete mappings,
computes every secant and affine-triangle multiplicity, reproduces the four
classes above, and checks every affine-orbit cylinder formula and the
conditional composition theorem.
