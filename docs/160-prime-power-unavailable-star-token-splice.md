# Heavy unavailable row-column stars splice directly into full-prefix token alternatives

CMR507--CMR511 adapt the line-clean forbidden matching until the remaining
unavailable inventory is either freely absorbed or concentrated in one residual
source row or target column.  This chapter feeds that heavy star into the exact
full-prefix token system already used by CMR390--CMR417.

A row star has one fixed source prefix at every depth.  Partitioning its target
columns by residue modulo `p^b` therefore gives an exact heavy-cell versus
dispersed-token alternative.  The same statement holds with rows and columns
interchanged.

Let

\[
t=p^h,
\qquad h\ge2,
\]

and let

\[
S_x
=
\{(x,y):y\in Y\}
\]

be a set of `d=|Y|` distinct unavailable edges in one source row.  For a
nonroot depth `1\le b<h`, put

\[
a=x\bmod p^b,
\qquad
Y_c=\{y\in Y:y\equiv c\pmod{p^b}\}.
\]

For every direction label `\theta\in\mathbb P^1(\mathbb F_p)`, the full token

\[
\tau=(b,a,c,\theta)
\]

has edge universe

\[
U_\tau^{(2)}
=
\{(u,v):u\equiv a\pmod{p^b},\ v\equiv c\pmod{p^b}\}.
\]

## 1. Exact star-prefix occupancy

### Theorem CMR512 — PROVED

At every nonroot depth `b`,

\[
\boxed{
|S_x\cap U_{(b,a,c,\theta)}^{(2)}|
=|Y_c|
}
\]

for every direction label `\theta`, and

\[
\boxed{
\sum_{c\bmod p^b}|Y_c|=d.
}
\]

Each occupied target prefix satisfies the capacity bound

\[
\boxed{|Y_c|\le t/p^b.}
\]

### Proof

Every edge of the row star has source coordinate congruent to `a`.  Membership
in the full-prefix universe is therefore equivalent to the target congruence
`y\equiv c\pmod{p^b}`.  The classes partition `Y`.  Each residue class modulo
`p^b` has exactly `t/p^b` representatives in the parent coordinate set. ∎

The direction label repeats the same two-dimensional edge universe, as in
CMR391 and CMR413.

## 2. Tunable heavy-or-dispersed alternative

### Theorem CMR513 — PROVED

Fix an integer threshold `H\ge2`.  At every nonroot depth `b`, at least one of
the following holds.

1. **Heavy unavailable token.** Some target prefix `c` satisfies
   \[
   \boxed{|Y_c|\ge H.}
   \]
   Consequently every direction-labelled token `(b,a,c,\theta)` contains at
   least `H` unavailable star edges.
2. **Dispersed unavailable tokens.** At least
   \[
   \boxed{
   \left\lceil\frac d{H-1}\right\rceil
   }
   \]
   distinct target prefixes are occupied.

### Proof

If no class has size at least `H`, every occupied class has size at most
`H-1`.  Since their sizes sum to `d`, at least `\lceil d/(H-1)\rceil` classes
are needed. ∎

This is exact for every chosen scale and threshold.

## 3. Dispersed token packing

### Corollary CMR514 — PROVED

In the dispersed branch of CMR513, fix one direction label `\theta` and choose
one unavailable edge from each occupied target prefix.  The chosen edges belong
to pairwise distinct full tokens

\[
(b,a,c,\theta),
\]

and those token edge universes are pairwise disjoint.

Thus the row star supplies at least

\[
\boxed{
\left\lceil\frac d{H-1}\right\rceil
}
\]

distinct unavailable full-token witnesses at depth `b`.

### Proof

Different target residues `c` define disjoint edge universes at the same depth,
source prefix, and direction label.  Choose one star edge in each occupied
class. ∎

The selected token witnesses can therefore enter the existing fresh-token,
return, and ancestry ledgers without token collisions at that scale.

## 4. Square-root endpoint and column symmetry

### Theorem CMR515 — PROVED

Let

\[
H=\lceil\sqrt d\rceil.
\]

For every nonroot depth `b`, the unavailable row star gives either

\[
\boxed{
\text{one full token containing at least }\lceil\sqrt d\rceil
\text{ unavailable edges},
}
\]

or at least

\[
\boxed{
\left\lceil
\frac d{\lceil\sqrt d\rceil-1}
\right\rceil
\ge
\lfloor\sqrt d\rfloor
}
\]

pairwise disjoint unavailable token witnesses.

The same conclusions hold for a target-column star

\[
S_y=\{(x,y):x\in X\}
\]

by interchanging the source and target coordinates.

### Proof

Apply CMR513--CMR514 with the displayed threshold.  For `d\ge2`, the elementary
inequality gives the stated lower bound.  For `d=1`, the unique edge is already
one token witness and the heavy/dispersed conclusion is interpreted directly.
Column symmetry is coordinate interchange. ∎

## 5. Adaptive line-clean token endpoint

### Corollary CMR516 — PROVED

Apply CMR510 to a rooted-arm or bottleneck line-clean cylinder in a parent of
side `t=p^h`, with `h\ge2`.  If the heavy unavailable row/column branch has
degree

\[
D
\ge
\left\lceil
\frac{\alpha q(n-1)}{2\ell_L+s-1}
\right\rceil,
\]

then at every chosen nonroot depth the branch yields one of:

1. a full-prefix token containing at least `\lceil\sqrt D\rceil` unavailable
   edges;
2. at least `\lfloor\sqrt D\rfloor` pairwise disjoint unavailable full-token
   witnesses.

Consequently the complete adaptive line-clean endpoint reaches at least one of:

- a cheap clean completion;
- anchored continuation;
- strict forced-core factorization;
- frozen CMR334 collateral mass;
- free absorption of a large unavailable matching;
- a heavy unavailable full-prefix token;
- a dispersed unavailable-token bank.

### Proof

CMR510 supplies the unavailable row or column star.  Apply CMR515.  All other
branches are unchanged from CMR511. ∎

The repeated unavailable-cell obstruction has therefore been converted to the
same heavy-prefix versus dispersed-token language already used in the sharp
Hall-blocker and line-energy endpoints.  What remains is temporal accounting:
show that free absorption and dispersed unavailable tokens cannot be reused
indefinitely across compatible parent epochs without paying reserve depletion,
ancestor-return incidence, or envelope expansion.

No all-`n` theorem is claimed.  Prefix occupancies, threshold arithmetic,
square-root bounds, disjoint token cells, and row-column symmetry are checked in
[`scripts/verify_prime_power_unavailable_star_tokens.py`](../scripts/verify_prime_power_unavailable_star_tokens.py).
