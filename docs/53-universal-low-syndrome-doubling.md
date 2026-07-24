# Universal low-syndrome product doubling

The exact side-six closure PX60 finishes the finite relative-cycle classes at
base six, but it does not yet give an infinite closure theorem. This chapter
replaces the next factorial host search by an all-side structural endpoint.

For every saturated no-three side-`n` factor, arbitrary block maps produce a
saturated side-`2n` product state with only `O(n log n)` bad triples. The state
is not asserted to be no-three. Its purpose is to reduce exact doubling to a
sparse repair problem.

Throughout, permutations are composed from right to left and

\[
H_k=\sum_{d=1}^k\frac1d
\]

denotes the harmonic number.

## 1. Three-labeling full-host normal form

PX50 writes every normalized full host as

\[
g_{ijs}=Q^jTH^sP^i.
\]

Put

\[
R=P^{-1},\qquad A=T,\qquad B=QT.
\]

The three permutations `R,A,B` are independent.

### Theorem PX61 -- PROVED

Fix a derangement `H` on `[n]` and an orientation `theta`. Every normalized
arbitrary-block full host is obtained as follows.

Use one abstract fine-row index `u`. In coarse row block zero give it scalar
fine-row label `u`; in coarse row block one give it label `R(u)`. Its two
inner-layer neighbours in coarse column block zero have labels

\[
A(u),\qquad A(Hu),
\]

and in coarse column block one have labels

\[
B(u),\qquad B(Hu).
\]

Conversely every triple of permutations `(R,A,B)` gives a normalized full host,
and corresponds uniquely to

\[
P=R^{-1},\qquad T=A,\qquad Q=BA^{-1}.
\]

Thus, after fixing the relative cycle representative `H`, full-host geometry is
exactly the problem of independently labeling the second row copy and the two
column copies.

### Proof

Reindex the second coarse row block by

\[
w=P(u).
\]

Its scalar fine-row label is `u=P^{-1}(w)=R(w)`, while its block maps are

\[
Q^jTH^s(w).
\]

For `j=0` these are `A(w),A(Hw)`; for `j=1` they are `B(w),B(Hw)`. The first row
block already uses the abstract label directly. The converse substitutions
recover PX50 exactly. \(\square\)

This form absorbs the factorial parameter `P` into a row-pattern assignment and
replaces `(T,Q)` by two independent column labelings.

## 2. Primitive-direction grid-line count

Let `L(N)` be the number of unordered triples of distinct collinear points in
`[N]^2`.

### Lemma PX62 -- PROVED

For every `N>=2`,

\[
\boxed{L(N)\le 2N^4H_{N-1}.}
\]

Consequently the number of ordered collinear triples is at most

\[
12N^4H_{N-1}.
\]

### Proof

Represent every unoriented line direction by one primitive integer vector
`q=(a,b)` in a fixed half-plane and put

\[
d=\lVert q\rVert_\infty.
\]

There are at most `4d` such primitive directions with norm `d`. A triple in
this direction has a first point `z` and the form

\[
z,\qquad z+r q,\qquad z+s q,
\qquad 1\le r<s\le\frac{N-1}{d}.
\]

There are at most `N^2` choices for `z` and at most

\[
\frac12\left(\frac Nd\right)^2
\]

choices for `(r,s)`. Therefore

\[
L(N)
\le
\sum_{d=1}^{N-1}4dN^2\frac{N^2}{2d^2}
=
2N^4H_{N-1}.
\]

Multiplying by six gives the ordered bound. \(\square\)

## 3. Random rectangle state

Use the PX43 rectangle normal form in any fixed orientation. Choose three
independent uniform permutations

\[
p,t,r\in\operatorname{Sym}([n]).
\]

For each `u`, select the four corners of

\[
R_u=
\{X_0(u),X_1(p(u))\}
\times
\{Y_0(t(u)),Y_1(r(u))\}.
\]

This is always a saturated state of `4n` points in `[2n]^2`. By the
full-symmetric gauge theorem, every permutation layer of every saturated
side-`n` factor realizes every such normalized state after suitable block maps.

PX44 says that every bad triple is either diagonal, using two opposite corners
of one rectangle and one corner of another, or transversal, using one corner
from each of three rectangles.

### Theorem PX63 -- PROVED

For every `n>=3`, the expected number `D` of bad triples in the random rectangle
state satisfies

\[
\boxed{
\mathbb E D
\le
\frac{8n^2}{n-1}
+
12288\frac{n^3}{(n-1)(n-2)}H_{2n-1}.
}
\]

Consequently every saturated no-three side-`n` factor has a factor-compatible
saturated product state of `4n` points in `[2n]^2` with

\[
D=O(n\log n).
\]

### Proof

PX45a gives

\[
\mathbb E D_{\rm diag}\le\frac{8n^2}{n-1}.
\]

For the transversal contribution, fix an ordered choice of one of the four
corner types for each of three distinct rectangles and condition on `p`. The
three scalar row coordinates are distinct.

Suppose `k` chosen corners use `t` and `3-k` use `r` for their fine-column
labels. Every admissible ordered scalar-column assignment has probability

\[
\frac1{(n)_k(n)_{3-k}}
\le
\frac1{(n)_3}.
\]

By PX62, the number of possible ordered collinear scalar triples in `[2n]^2` is
at most

\[
12(2n)^4H_{2n-1}.
\]

There are `4^3=64` ordered corner patterns. Hence

\[
\mathbb E D_{\rm trans}
\le
64\frac{12(2n)^4H_{2n-1}}{n(n-1)(n-2)}
=
12288\frac{n^3}{(n-1)(n-2)}H_{2n-1}.
\]

Adding the contributions proves the bound. Since the expectation is an average
over finitely many states, one state attains it. Full-symmetric gauge transport
makes that scalar state available to every factor layer. \(\square\)

The constant is intentionally crude. Exact small averages and random samples
are much smaller; the theorem records the asymptotic order needed for repair.

## 4. Sparse-syndrome consequences

### Corollary PX64 -- PROVED

Every saturated no-three side-`n` factor has a factor-compatible saturated
side-`2n` product state with all of the following properties.

1. It has `O(n log n)` bad triples.
2. It has `O(n log n)` bad lines.
3. If a scalar line contains `k` selected points, then
   \[
   k\le 2+(6D)^{1/3}=O((n\log n)^{1/3}).
   \]
4. The average bad-triple incidence of one rectangle is `O(log n)`.
5. At least `n/2` of the `n` rectangles have bad-triple incidence `O(log n)`.

### Proof

The first assertion is PX63. Every bad line contributes at least one triple, so
the second follows.

A line containing `k>=3` selected points contributes

\[
\binom k3
\]

bad triples. Since

\[
\binom k3
=\frac{k(k-1)(k-2)}6
\ge\frac{(k-2)^3}{6},
\]

we have `k<=2+(6D)^(1/3)`, proving the third assertion.

A bad triple involves at most three rectangles, so the sum of rectangle defect
degrees is at most `3D=O(n log n)`. Averaging gives the fourth assertion, and
Markov's inequality gives the fifth. \(\square\)

Arbitrary blockwise digit permutations preserve the four-regular combinatorial
host and saturation, but they do not preserve the earlier global-radix line cap
PX6. The subcubic line-occupancy conclusion above is the valid consequence of
the low-syndrome theorem.

## 5. Revised general-proof target

The next theorem should operate on the rectangle matching directly:

> every saturated rectangle state with `O(n log n)` bad triples admits either an
> improving balanced trade or a structured one-point/two-point line-shadow
> certificate.

PX15 and PX21 give the exact collateral identity and composite-batch
compression. PX22 shows bounded-support improvement in all exact side-six and
side-nine traps examined. PX69 now supplies an all-side transposition
improvement-or-shadow theorem beginning from the PX63 seed.

A successful absorption theorem for the resulting logarithmic shadow
concentration would upgrade approximate doubling to exact multiplicative
closure.

## Verification

Run

```bash
python scripts/verify_product_low_syndrome_doubling.py
```

The verifier checks the three-labeling normal form on random exact hosts through
base seven, verifies PX62 by complete grid enumeration through side eight,
computes the exact rectangle-state averages through base four, and checks
saturation and the diagonal/transversal classification in random states through
base ten.
