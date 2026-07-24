# Odd parent line-deletion resilience

The inherited parent blocks in the prime-power programme have odd size. The
rank-three candidate-only obstruction therefore has more matching resilience
than a general half-degree host: one may remove half a block's worth of entire
real-line matchings before an essential edge can appear.

Throughout,

\[
t=2h+1,
\qquad h\ge4,
\]

and

\[
G_t=K_{t,t}\setminus I
\]

is the normalized parent derangement graph. A nonaxis real line meets the
`t` by `t` board in a partial matching; write `E(L)` for its non-diagonal board
cells.

## 1. Rigidity of full affine transversals

### Theorem CMR227 — PROVED

Let `A,C` be finite subsets of the real line with

\[
|A|=|C|=n\ge2.
\]

There are at most two nonvertical, nonhorizontal real lines containing `n`
points of the Cartesian product

\[
A\times C.
\]

Equivalently, there are at most two affine bijections

\[
x\longmapsto \alpha x+\beta
\]

from `A` onto `C`.

### Proof

A nonvertical, nonhorizontal line containing `n` points of `A\times C` meets
each source coordinate of `A` and each target coordinate of `C` exactly once.
It is therefore the graph of an affine bijection from `A` to `C`.

Fix one such bijection `f_0`. For every other one, the composition

\[
f_0^{-1}\circ f
\]

is an affine automorphism of `A`. Order the elements of `A` increasingly. A
positive-slope affine automorphism is increasing and hence fixes every ordered
position, so it is the identity. A negative-slope affine automorphism is
decreasing and must send the `i`-th smallest element to the `i`-th largest;
there is at most one such map. Thus `A`, and consequently the pair `(A,C)`,
has at most two affine bijections. ∎

## 2. Half-block line deletions create no essential edge

### Theorem CMR228 — PROVED

Let

\[
L_1,\ldots,L_h
\]

be distinct nonaxis real lines, and let

\[
D\subseteq\bigcup_{i=1}^h E(L_i).
\]

If

\[
H=G_t-D
\]

has a perfect matching, then `H` has no essential edge.

### Proof

Each `E(L_i)` is a partial matching, so

\[
\delta(H)\ge (t-1)-h=h.
\]

Suppose that `e=uv` is essential. Apply CMR210 and write

\[
A\subseteq L,
\qquad
B=N_H(A)\subseteq R,
\qquad
|A|=|B|=a,
\]

with `uv` the unique edge from `A` to `v`. CMR211 gives

\[
h\le a\le h+2.
\]

Put

\[
C=(R\setminus B)\cup\{v\}.
\]

Then

\[
|C|=t-a+1,
\]

and every cell of `A\times C` except `uv` is absent from `H`: cells from `A`
to `R\setminus B` are absent because `N_H(A)=B`, while cells from
`A\setminus\{u\}` to `v` are absent by the unique-neighbour condition.

The old diagonal accounts for at most

\[
\min\{|A|,|C|\}
\]

of these missing cells. Hence `D` contains at least

\[
|A||C|-1-\min\{|A|,|C|\}
\]

cells of `A\times C`. For each of the three possibilities

\[
a=h,
\qquad a=h+1,
\qquad a=h+2,
\]

this lower bound is

\[
\boxed{h(h+1)-1}.
\]

If `a=h` or `a=h+2`, one has

\[
\min\{|A|,|C|\}=h.
\]

Each line contributes at most `h` cells to `A\times C`, so the `h` lines
contribute at most `h^2`, less than `h(h+1)-1`. These two cases are impossible.

It remains that

\[
|A|=|C|=h+1.
\]

Each of the `h` lines contributes at most `h+1` cells. Since their union must
contain at least `h(h+1)-1` cells, the total deficiency from the maximum
`h(h+1)` is at most one. Therefore at least `h-1` of the distinct lines contain
exactly `h+1` points of `A\times C`. They are full affine transversals from `A`
to `C`. CMR227 allows at most two, whereas

\[
h-1\ge3.
\]

This contradiction proves that no essential edge exists. ∎

The theorem applies to arbitrary subsets of the line matchings. This is
important when the cells of the final line are deleted one at a time.

## 3. Deleting half the rank-three line signatures

### Theorem CMR229 — PROVED

Let a globally nonimproving inherited parent state have block size

\[
t=2h+1\ge9.
\]

Starting from its one-layer derangement bank, at least one of the following
holds.

1. A residual parent state is covered by a rank-one or rank-two certificate;
   CMR201 supplies an executable anchored alternating continuation.
2. There are `h+1` distinct rank-three real-line signatures

   \[
   L_1,\ldots,L_{h+1},
   \]

   and a parent perfect matching which avoids every candidate cell on

   \[
   L_1,\ldots,L_h.
   \]

### Proof

Construct the lines inductively. Let `H_0=G_t`. At stage `j`, choose a perfect
matching of `H_{j-1}`. Every such parent state destroys the designated old
target, so global nonimprovement forces at least one new candidate certificate.
If a chosen certificate has rank one or two, CMR201 with a one-cell wall gives
the first alternative.

Otherwise choose a rank-three certificate and let `L_j` be its real line. The
line is nonaxis because its three cells are matching-compatible. It is distinct
from all earlier lines, since `H_{j-1}` contains no cell from an earlier line.

For

\[
1\le j\le h-1,
\]

delete all cells of `E(L_j)`. The resulting graph has minimum degree at least

\[
(t-1)-j=2h-j\ge h+1>t/2,
\]

and hence has a perfect matching by Hall's theorem.

For `j=h`, delete the cells of `E(L_h)` one at a time. Before each deletion the
current graph has a perfect matching and its deleted set is contained in the
union of the `h` distinct line matchings. CMR228 says that the next edge is not
essential, so deleting it preserves a perfect matching. Thus the complete
line matching `E(L_h)` can also be removed.

The final graph `H_h` has a perfect matching avoiding all cells on the first
`h` lines. Its covering certificate cannot use any of those lines. If it is
anchored, the first alternative holds; otherwise it supplies the distinct
rank-three line `L_{h+1}`. ∎

### Corollary CMR230 — PROVED

For every nonroot balanced reciprocal or prime-seven parent block of size at
least nine, a frozen parent cover either exposes an anchored alternating bank or
has more than half a block's worth of distinct candidate-only real-line
signatures. Moreover, one parent state simultaneously avoids all candidate
cells on `floor(t/2)` of those lines.

The block sizes `t=5,7` are explicit finite exceptions to CMR229. The general
small-block derangement banks remain available, but embedded blocks have
outside collateral and are not covered merely by the exact standalone
`N=5,7` root censuses.

## 4. Revised internal endpoint

The candidate-only obstruction can no longer be supported by only the minimum
Hall-wall population. At every genuine large odd prime-power parent it must
survive simultaneous deletion of

\[
\frac{t-1}{2}
\]

entire geometric line matchings.

The remaining fixed-envelope theorem is now a second-half line-avoidance or
signature-budget statement: either extend CMR229 beyond the half-block point,
or charge the forced additional line signatures to primitive-height, quotient,
or carry cells. At the exact half-block threshold there is no essential-edge
or forced-factor obstruction.

No all-`n` theorem is claimed here. The affine-transversal rigidity and the
three Hall-factor arithmetic cases are checked in
[`scripts/verify_prime_power_odd_line_resilience.py`](../scripts/verify_prime_power_odd_line_resilience.py).
