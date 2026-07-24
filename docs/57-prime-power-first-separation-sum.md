# Summing recursive first-separation certificates

The local conic-fibre estimate CMR46 can be iterated along the lower-digit
quotient tree. This chapter proves a general first-separation probability bound
and sums it over all column triples. For primes congruent to one modulo four, a
balanced reciprocal family gives the natural quadratic-logarithmic syndrome
scale.

Let

\[
N=p^k,
\qquad h=(p-1)/2,
\]

with `p` odd. For `b` modulo `p` and nonzero `c`, put

\[
F_{b,c}(0)=b,
\qquad
F_{b,c}(x)=[b+cx^{-1}]_p\quad(x\ne0).
\]

## 1. A balanced no-three fibre family when `p=1 mod 4`

Assume in this section that

\[
p\equiv1\pmod4.
\]

Let `C_p` be the set of nonzero quadratic nonsquares modulo `p`, and define

\[
\mathcal B_p
=
\{F_{b,c}:b\in\mathbb F_p,\ c\in C_p\}.
\]

Thus `|B_p|=ph`.

### Theorem CMR67 — PROVED

Every member of `B_p` is an integer no-three permutation. Under the uniform
measure on `B_p`:

1. every prescribed cell `(x,y)` has probability exactly `1/p`;
2. every compatible prescription on at least two distinct columns has
   probability at most
   \[
   \frac1{ph}.
   \]

There is also an exact saturated two-layer root law: choose `c` uniformly from
`C_p` and choose an ordered pair of distinct shifts `(b_0,b_1)` uniformly. Use
`F_{b_0,c}` and `F_{b_1,c}` as the two root permutations. The layers are
pointwise disjoint, and each individual layer still has the uniform `B_p`
marginal.

### Proof

First suppose `0<=b<=h`. The determinant calculation from CMR35 remains valid,
including the endpoint `b=0`. A modular triple must contain the exceptional
point `(0,b)` and the two conic points with columns `x,-x`. In the only range
where the standard integer determinant can vanish, equality forces

\[
c=x^2\pmod p,
\]

which is impossible for a nonsquare `c`.

Now suppose `b>h`. Reflect the graph in the horizontal midline of the integer
square. The reflected permutation is

\[
F_{p-1-b,-c}.
\]

Its new shift lies in `[0,h]`. Since `p=1 mod 4`, the element `-1` is a square,
so `-c` is again a nonsquare. The first case applies, and reflection preserves
real collinearity.

For the cylinder law, at column zero the equation `F(0)=y` fixes `b=y` and
leaves all `h` choices of `c`. At a nonzero column, each nonsquare `c` determines
exactly one shift

\[
b=y-cx^{-1}.
\]

Hence every cell occurs in exactly `h` of the `ph` states. Two prescribed cells
in distinct columns determine both parameters, so at most one state survives.

It remains to characterize disjoint root pairs. If `b_0=b_1`, the two maps
collide at column zero. If `b_0\ne b_1` and `c_0\ne c_1`, then the equation

\[
b_0+c_0x^{-1}=b_1+c_1x^{-1}
\]

has one nonzero solution `x`. Thus two maps from `B_p` are pointwise disjoint
exactly when they have one common `c` and distinct shifts. The stated root law
is therefore saturated. Its layer marginals are uniform because each shift and
each nonsquare parameter occur equally often. ∎

Starting from this saturated root pair, use an independent uniform member of
`B_p` at every layer-prefix node of depths `1,...,k-1`. The quotient row prefixes
of the two layers are already distinct, so independent child permutations map
into disjoint row fibres and preserve saturation.

The resulting balanced recursive bank contains

\[
hp(p-1)(ph)^{2(p+p^2+\cdots+p^{k-1})}
=
hp(p-1)(ph)^{2(N-p)/(p-1)}
\]

states. Every nonroot node has the exact one-cell atom `1/p` and rank-two atom
at most `1/(ph)`.

## 2. A multiscale first-separation probability

The next statement applies to any recursive digit bank whose nonroot local node
law has a one-cell bound. At depth `n`, the node key of a selected position is

\[
(\text{layer},x\bmod p^n).
\]

The local permutation at that node supplies the row digit of place value `p^n`.
Assume every prescribed output at a fixed input has conditional probability at
most `mu`, independently at distinct nonroot nodes.

Fix three distinct columns `x_1,x_2,x_3` and any layer choices. Put

\[
s=\max_{i<j}v_p(x_i-x_j).
\]

Since the columns are distinct, `0<=s<=k-1`.

### Theorem CMR68 — PROVED

In the recursive product bank,

\[
\Pr(\text{the three selected points are real collinear})
\le
\mu^{k-s-1}.
\]

The same bound holds for the event that their determinant is zero modulo
`p^k`.

### Proof

Write the determinant as

\[
\Delta=\kappa_1y_1+\kappa_2y_2+\kappa_3y_3,
\]

where

\[
\kappa_1=x_3-x_2,
\qquad
\kappa_2=x_1-x_3,
\qquad
\kappa_3=x_2-x_1.
\]

Let

\[
r=\min_i v_p(\kappa_i)
\]

and put `K_i=kappa_i/p^r`. At least two of the `K_i` are units modulo `p`.
Choose one unit coefficient, say `K_j`.

Expand the row coordinates in lower-first base-`p` digits,

\[
y_i=\sum_{n=0}^{k-1}p^n\eta_{i,n}.
\]

Divisibility of `Delta` by successive powers of `p`, after division by `p^r`,
gives at the next digit a congruence

\[
C_n+K_j\eta_{j,n}\equiv0\pmod p.
\]

After all other depth-`n` outputs are exposed, at most one value of
`eta_{j,n}` works.

For every depth `n>s`, the three column prefixes modulo `p^n` are pairwise
distinct. Therefore the chosen point's node key is used by no other point in the
triple. These depths are nonroot because `n>s>=0`, and their local choices are
independent. There are exactly `k-s-1` such depths. Multiplying the conditional
bounds proves both the modular-divisibility statement and, a fortiori, the
real-collinearity statement. ∎

The estimate deliberately ignores the separation depth `s` itself. At that
depth two or three points may use one local map, so a one-cell argument is not
universally available.

## 3. Global syndrome sums

Let `T_k` be the number of unordered real collinear triples in the two-layer
recursive state at modulus `N`.

For one `s`, the number of unordered column triples whose maximum pair valuation
is `s` is at most the number having some pair congruent modulo `p^s`. There are

\[
p^s\binom{N/p^s}{2}
<
\frac{N^2}{2p^s}
\]

such pairs and fewer than `N` choices for the third column. Each column triple
has eight layer assignments. Triples using two points in one actual column are
vertical with respect to every third point and never contribute to real
collinearity.

### Corollary CMR69 — PROVED

For the original restricted conic bank CMR43, whose nonroot one-cell atom is
`mu=1/h`,

\[
\mathbb E T_k
<
8h\,N^{3-\log_p h}.
\]

For every fixed odd `p>=5`, this is genuinely subcubic.

If `p=1 mod 4` and the corrected balanced saturated bank from CMR67 is used,
then `mu=1/p` at every nonroot node and

\[
\mathbb E T_k\le4pkN^2.
\]

Consequently the bank contains a saturated state with

\[
T_k=O_p(N^2\log N),
\]

while retaining exact product spread and deterministic exclusion of every
one-fibre triple.

### Proof

Insert CMR68 into the preceding count and sum over `s`. For the restricted bank,

\[
\begin{aligned}
\mathbb E T_k
&\le
8\sum_{s=0}^{k-1}
\frac{N^3}{2p^s}h^{-(k-s-1)}\\
&=
4N^3h^{-(k-1)}
\sum_{s=0}^{k-1}(h/p)^s
<8\frac{N^3}{h^{k-1}}.
\end{aligned}
\]

For the balanced bank,

\[
\begin{aligned}
\mathbb E T_k
&\le
8\sum_{s=0}^{k-1}
\frac{N^3}{2p^s}p^{-(k-s-1)}\\
&=4pkN^2.
\end{aligned}
\]

The root coupling does not enter CMR68, because all charged depths satisfy
`n>s>=0` and hence are nonroot. A state no worse than the expectation exists. ∎

This completes the first-separation summation at the quadratic-logarithmic
scale for the infinite prime-power class `p=1 mod 4`. It does not yet reach the
near-linear repair threshold.

The finite structural checker is
[`scripts/verify_prime_power_first_separation_sum.py`](../scripts/verify_prime_power_first_separation_sum.py).
