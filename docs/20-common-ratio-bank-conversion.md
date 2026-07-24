# Common-ratio bank conversion

This chapter converts a same-ratio rectangle bank into either an improving switch or an explicit algebraic concentration certificate. The theorem is deliberately one-switch local: this avoids uncontrolled interactions among several simultaneously flipped rectangles while still producing a rigorous decoder-or-structure dichotomy.

Throughout, let `p` be an odd prime and

\[
H_c=\{(x,\langle c/x\rangle_p):x\in\mathbb F_p^*\}
\]

be a modular hyperbola represented in the integer square. Let the current saturated configuration `S` be contained in a union of `q` distinct hyperbola channels

\[
S\subseteq\bigcup_{b\in\mathcal B}H_b,
\qquad |\mathcal B|=q.
\]

Fix `a in B` and `g ne 1`. Suppose one permutation layer contains pairwise row- and column-disjoint current pairs

\[
C_i=\left\{\left(x_i,\frac a{x_i}\right),
\left(gx_i,\frac a{gx_i}\right)\right\},
\qquad 1\le i\le m.
\]

Their rectangle-switched states are

\[
W_i=\left\{u_i,v_i\right\}
=\left\{\left(x_i,\frac a{gx_i}\right),
\left(gx_i,\frac a{x_i}\right)\right\}.
\]

All displayed finite-field coordinates are interpreted by their nonzero integer representatives. Assume each switch is admissible: neither inserted cell is already selected outside `C_i`.

Let

\[
\Phi(T)=\sum_L\binom{|T\cap L|}{3}
\]

be the real collinear-triple certificate potential.

## 1. Exact one-switch collateral

For a point `z notin Y`, define its weighted secant load against `Y` by

\[
A_Y(z)=\sum_{L\ni z}\binom{|Y\cap L|}{2}.
\]

Equivalently, `A_Y(z)` is the number of unordered pairs of points of `Y` collinear with `z`.

For block `i`, put

\[
Y_i=S\setminus C_i,
\]

\[
d_i=\Phi(S)-\Phi(Y_i),
\]

and let `ell_i` be the real line through `u_i,v_i`. Define

\[
\sigma_i=A_{Y_i}(u_i)+A_{Y_i}(v_i),
\qquad
r_i=|Y_i\cap\ell_i|.
\]

### Theorem CR1 — PROVED

The exact collateral created by switching block `i` is

\[
\boxed{
\Phi(Y_i\cup W_i)-\Phi(Y_i)=\sigma_i+r_i.
}
\]

Consequently the potential change is

\[
\boxed{
\Delta_i=\sigma_i+r_i-d_i.
}
\]

### Proof

Triples created using exactly one inserted point are counted by `A_{Y_i}(u_i)` and `A_{Y_i}(v_i)`. Triples using both inserted points are exactly

\[
\{u_i,v_i,y\},\qquad y\in Y_i\cap\ell_i,
\]

and contribute `r_i`. These classes are disjoint and exhaustive. `square`

The formula remains correct when `ell_i` already contains several outside points. If it contains `k` outside points, its total contribution is

\[
2\binom{k}{2}+k=k^2
=\binom{k+2}{3}-\binom{k}{3}.
\]

## 2. Radial anchor equation

The switched cells satisfy

\[
v_i\equiv g u_i\pmod p
\]

coordinatewise. Thus they lie on one modular radial line.

Let

\[
w=(z,b/z)\in H_b.
\]

### Lemma CR2 — PROVED

If `u_i,v_i,w` are collinear as real grid points, then

\[
\boxed{a z^2=b g x_i^2\pmod p.}
\]

Equivalently,

\[
\boxed{z=\lambda x_i,
\qquad \lambda^2=bg/a.}
\]

### Proof

Reducing the real determinant modulo `p` gives

\[
\det(u_i,v_i,w)
=
\frac{g-1}{g x_i z}\left(bg x_i^2-a z^2\right).
\]

The prefactor is nonzero, so real collinearity implies the displayed quadratic relation. `square`

For each outside channel `b`, there are at most two possible values of `lambda`. Hence

\[
\boxed{r_i\le 2q.}
\]

More importantly, all paired-anchor incidences belong to at most `2q` signatures `(b,lambda)`. For one signature, the possible anchors form the aligned multiplicative set

\[
\mathcal O_{b,\lambda}
=
\left\{
\left(\lambda x_i,\frac b{\lambda x_i}\right):1\le i\le m
\right\}\subseteq H_b.
\]

These sets lie on torus orbits of the action

\[
T_g(x,y)=(gx,y/g),
\]

because `T_g` preserves every channel `H_b`.

## 3. Decoder-or-structure theorem

Put

\[
D=\sum_{i=1}^m d_i,
\qquad
\Sigma=\sum_{i=1}^m\sigma_i,
\qquad
R=\sum_{i=1}^m r_i.
\]

### Theorem CR3 — PROVED

At least one of the following holds.

1. **Improving rectangle.** Some `i` satisfies
   \[
   \Phi(Y_i\cup W_i)<\Phi(S).
   \]

2. **Secant-star concentration.** There are a switched candidate cell `z`, an unordered channel pair `{b,c}` from `B`, and at least
   \[
   \boxed{
   \frac{D}{4m\binom{q+1}{2}}
   =
   \frac{D}{2m q(q+1)}
   }
   \]
   outside pairs with one endpoint in `H_b`, the other in `H_c`, and whose real joining lines all pass through `z`.

3. **Aligned radial-anchor concentration.** There are a channel `b`, a root
   \[
   \lambda^2=bg/a,
   \]
   and at least
   \[
   \boxed{\frac{D}{4q}}
   \]
   distinct bank blocks whose switched pair is real-collinear with the aligned anchor
   \[
   \left(\lambda x_i,\frac b{\lambda x_i}\right)\in S.
   \]

In the secant-star alternative, the pairs may be chosen pairwise endpoint-disjoint after losing at most a factor two.

### Proof

If no rectangle improves, Theorem CR1 gives

\[
d_i\le\sigma_i+r_i
\]

for every `i`, and hence

\[
D\le\Sigma+R.
\]

Therefore either `Sigma>=D/2` or `R>=D/2`.

Assume first that `Sigma>=D/2`. There are `2m` switched candidate cells, so one of them, say `z`, has weighted secant load at least

\[
\frac{D}{4m}.
\]

Every outside point lies on one of the `q` disjoint hyperbola channels. Partition the pairs counted by `A_Y(z)` according to their unordered channel pair. There are `binom(q+1,2)` types, so one type contributes at least the quantity in alternative 2.

For a same-channel type, the pairs through `z` are already endpoint-disjoint: a point and `z` determine one line, and a line meets one modular hyperbola in at most two points. For two different channels, the resulting bipartite graph has maximum degree at most two on each side, since a line through `z` and one endpoint meets the other hyperbola in at most two points. Its edges split into two matchings, so at least half may be made endpoint-disjoint.

Assume instead that `R>=D/2`. Lemma CR2 partitions all paired-anchor incidences into at most `2q` signatures `(b,lambda)`. One signature therefore occurs at least

\[
\frac{R}{2q}\ge\frac{D}{4q}
\]

times. For fixed `(b,lambda)` and block `i`, the anchor parameter is uniquely `lambda x_i`; disjoint blocks have distinct `x_i`, so these are distinct aligned anchors. `square`

## 4. Uniform conversion criterion

Define

\[
\Theta
=
\max_{i,\ z\in W_i}A_{Y_i}(z)
\]

and let

\[
\Lambda
=
\max_{b,\lambda}
\#\left\{
 i:
 \lambda^2=bg/a,
 \left(\lambda x_i,b/(\lambda x_i)\right)\in Y_i\cap\ell_i
\right\}.
\]

### Corollary CR4 — PROVED

If

\[
\boxed{D>2m\Theta+2q\Lambda,}
\]

then some common-ratio rectangle switch strictly lowers `Phi`.

### Proof

The definitions give

\[
\Sigma\le2m\Theta,
\qquad
R\le2q\Lambda.
\]

If no switch improved, Theorem CR1 would imply

\[
D\le\Sigma+R\le2m\Theta+2q\Lambda,
\]

a contradiction. `square`

This is the desired conversion inequality. Failure is not anonymous: it means either a large secant load at one inserted cell or a large aligned multiplicative anchor class.

## 5. Paid-bank issue

The inverse-additive theorem that extracts a common-ratio bank from a small quotient set only guarantees many disjoint quotient pairs. It does **not** guarantee that those pairs carry current defect incidence.

The quantity needed by CR3 and CR4 is

\[
D=\sum_i d_i.
\]

A large algebraic bank with `D=0` is useless for decoding. Thus the next inverse statement must be weighted by the current syndrome.

### Target CR5 — OPEN: weighted quotient-bank extraction

Let `w(x,y)` be the amount of current triple incidence destroyed by switching the rectangle generated by a quotient pair `{x,y}`. Prove that a low-complexity frozen core contains a common ratio `g` and a disjoint family `{x_i,gx_i}` satisfying

\[
\sum_i w(x_i,gx_i)
\ge c\,W,
\]

where `W` is a fixed positive fraction of the total syndrome weight of the core.

Combined with CR4, such a theorem would give:

\[
\text{weighted inverse extraction}
\Longrightarrow
\text{improving switch or explicit opposite-colour structure}.
\]

## 6. Relation to alternating closure

The two obstruction outputs feed directly into the existing alternating red/blue framework.

- A secant-star concentration gives a high-load anchor cell and a large matching of outside secants through it. The anchor's opposite-colour block is the canonical next closure block.
- An aligned radial-anchor class lies in one of at most `2q` multiplicative signatures and has small quotient complexity inherited from the bank bases. It can be passed to the PFR anchor-propagation theorem.

Thus CR3 supplies an exact local transition:

\[
\boxed{
\text{paid common-ratio bank}
\Longrightarrow
\text{improvement, high-load anchor, or multiplicative structure propagation}.
}
\]
