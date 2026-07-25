# Recursive coarse resets have an exact fine-token return profile

CMR378--CMR381 give a general vacated-row budget for one laminar prefix sweep.
This chapter sharpens that accounting when the sweep remains in the recursive
prefix geometry of CMR93--CMR94. A coarse block has one complete row fibre, so
its return to a fixed finer token is either zero or exactly flat. After a
depth-`b` token is exposed, only `2b` compatible ancestor depth-layer slots can
return its endpoint edges.

Work in one normalized inherited parent block of side

\[
t=p^h
\]

with `p` odd. At depth `r`, the recursive row fibre in layer `ell` is

\[
R_{r,a,\ell}
=
\{y:y\equiv\rho_{r,\ell}(a)\pmod {p^r}\},
\]

where `a -> rho_{r,ell}(a)` is a permutation of the residues modulo `p^r`.
CMR93--CMR94 preserve these fibres while finer blocks are processed.

Fix a row-prefix direction token

\[
\tau=(b,c,\theta),
\qquad
1\le b<h,
\qquad
c\in\mathbb Z/p^b\mathbb Z,
\]

and put

\[
U_\tau=\{(x,y)\in[t]^2:y\equiv c\pmod {p^b}\}.
\]

The direction `theta` labels certificates but does not alter this endpoint
stock.

## 1. Exact host churn and the flat recursive-fibre profile

Let `B` be a set of `q` columns and `R` a set of `q` rows. Put

\[
K=B\times R.
\]

Let `M` be the current matching of the moving layer and let `L` be the partial
matching formed by opposite-layer cells in `K`. Suppose `M'` is an
old-cell-clean replacement, so

\[
M\cap L=M'\cap(M\cup L)=\varnothing.
\]

Define the allowed hosts

\[
H=K\setminus(M\cup L),
\qquad
H'=K\setminus(M'\cup L).
\]

### Theorem CMR382 — PROVED

The host churn is exact:

\[
\boxed{H'\setminus H=M},
\qquad
\boxed{H\setminus H'=M'}.
\]

Now let `B` be one recursive depth-`r` prefix block with `0<=r<b`, so
`q=t/p^r`, and let its row set be `R_{r,a,ell}`. Call it
**tau-compatible** when

\[
\rho_{r,\ell}(a)\equiv c\pmod {p^r}.
\]

At the full-host level, an old-cell-clean rematching of this block reintroduces
exactly

\[
\boxed{
\frac{q}{p^{b-r}}=\frac{t}{p^b}
}
\]

old matching edges in `U_tau` when the block is tau-compatible, and none when
it is not. With a persistent residual deletion mask, the actual returned
available-edge count is at most `t/p^b`.

### Proof

An edge is in `H'\H` exactly when it is excluded by `M union L` but not by
`M' union L`; pairwise disjointness makes this set exactly `M`. The reverse
difference is symmetric.

For the prefix statement, the old matching is a bijection onto the complete row
fibre. An incompatible fibre contains no row congruent to `c modulo p^b`. A
compatible fibre contains exactly

\[
\frac{t/p^r}{p^{b-r}}=\frac{t}{p^b}
\]

such rows, each used by exactly one old matching edge. A retained deletion mask
can only suppress returned edges. ∎

The return count is independent of the coarse depth. This is stronger than the
general CMR378 row-stock inequality because the recursive fibre is exactly
balanced over every finer residue.

## 2. Ancestor-slot factorization and the one-pass sum

Once a depth-`b` token is exposed in a descending schedule, only later depths
`r<b` are coarser than it. For every such depth and moving layer, the quotient
row-prefix permutation gives one unique tau-compatible block.

Let `A_{tau,r,ell}` count rematchings of that block after the token is exposed,
and put

\[
A_\tau
=
\sum_{r=0}^{b-1}\sum_{\ell=0}^1A_{\tau,r,\ell}.
\]

### Theorem CMR383 — PROVED UNDER THE DESCENDING RECURSIVE SCHEDULE

The coarse-prefix part of the CMR347 return mass satisfies

\[
\boxed{
I_\tau^{\rm coarse}
\le
\frac{t}{p^b}A_\tau.
}
\]

In a one-pass schedule, every depth-`r` block in each layer is rematched at most
once, so

\[
\boxed{A_\tau\le2b},
\qquad
\boxed{
I_\tau^{\rm coarse}
\le
\frac{2bt}{p^b}.
}
\]

Consequently the endpoint visits paid by CMR347 obey

\[
\boxed{
D_\tau
\le
\frac{t^2}{p^b}
+
\frac{2bt}{p^b}.
}
\]

Summing the labelled return mass over all nonroot row-prefix tokens gives

\[
\boxed{
\sum_{\theta\in\mathbb P^1(\mathbb F_p)}
\sum_{b=1}^{h-1}
\sum_{c\bmod p^b}
I_{(b,c,\theta)}^{\rm coarse}
\le
(p+1)t\,h(h-1).
}
\]

For fixed prime base this is `O_p(t log^2 t)`.

### Proof

CMR382 contributes at most `t/p^b` for each compatible reset, giving the first
inequality. There are `b` coarser depths and at most two moving layers, proving
`A_tau<=2b`. Apply CMR347 for the endpoint bound.

At depth `b` there are `p^b` row residues and `p+1` directions. Multiplying by
`2bt/p^b` gives `2(p+1)bt`; summing `b=1,...,h-1` gives the displayed total. ∎

Compared with the general laminar bound `2ht/p^b` from CMR380, the recursive
post-exposure bound replaces `h` by the actual number `b` of compatible coarser
ancestor levels.

## 3. Reset multiplicity and witness execution

### Theorem CMR384 — PROVED

Fix `m>=0`. If every tau-compatible ancestor depth-layer slot is rematched at
most `m` times after the token is exposed, then

\[
\boxed{
I_\tau^{\rm coarse}
\le
\frac{2bmt}{p^b}
}
\]

and

\[
\boxed{
D_\tau
\le
\frac{t^2}{p^b}
+
\frac{2bmt}{p^b}.
}
\]

Conversely, if either bound fails, one of the at most `2b` compatible ancestor
slots has been rematched more than `m` times.

Moreover, the witness-escape case in CMR349 is already executable. Every such
certificate opens a CMR75 prefix continuation:

1. an external witness exits at a strict earlier depth and leaves the Hall pair
   as the unique closest pair;
2. an internal non-equilateral witness transfers ownership to a strictly deeper
   closest pair; or
3. an equilateral witness lies wholly in one common prefix block.

A chain using only the deeper internal alternative has length at most
`h-1-b`.

### Proof

The multiplicity assumption gives `A_tau<=2bm`; apply CMR383 and CMR347. Its
converse is the contrapositive.

For witnesses, apply the primitive-parameter trichotomy CMR315--CMR317 and the
executable continuations CMR340--CMR343. Those results apply to each compatible
triple individually and do not require a heavy population. ∎

Thus unrestricted coarse return has one precise source: repeated use of a fixed
compatible ancestor slot. Witness visits are no longer a separate local
classification problem. The remaining fixed-envelope terms are:

- a monotone payment for repeated ancestor-slot resets;
- the width of fully forced CMR217 exchange ancestry;
- and, at full-token resolution, the two-dimensional return mass of
  CMR394--CMR402.

Joint-parent resets still require a separate descendant-token profile because
they preserve envelope row sets but need not preserve all recursive descendant
fibres.

No all-`n` theorem is claimed here. Exact host churn, flat p-adic returns,
one-pass sums, reset multiplicity, and witness routing are checked in
[`scripts/verify_prime_power_coarse_reset_profile.py`](../scripts/verify_prime_power_coarse_reset_profile.py).
