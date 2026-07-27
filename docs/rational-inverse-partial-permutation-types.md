# Canonical partial-permutation types for blocker profiles

**Branch:** `research/rational-inverse-expansion`

RI5ap--RI5at show that a rank-at-most-three blocker prescription has an exact derangement probability determined by its column/row overlap. This note removes the remaining purely combinatorial ambiguity. Every prescription is one of nine path/cycle types, and only one overlap class splits into two types.

## Partial-permutation graph

Let

\[
\phi:C\longrightarrow R
\]

be an injective blocker prescription of rank `s<=3`, with `|C|=|R|=s` and `phi(c)\ne c` for every prescribed column. Draw the directed arcs

\[
c\longrightarrow\phi(c)
\]

on `C union R`. Every vertex has indegree and outdegree at most one, so every component is a directed path or a directed cycle.

Write `P_j` for a directed path with `j` arcs and `C_j` for a directed cycle with `j` arcs. Put

\[
q=|C\cap R|.
\]

For a path with `j` arcs, exactly `j-1` vertices lie in `C intersect R`; for a cycle with `j` arcs, all `j` vertices do.

## RI5au -- complete rank-at-most-three type dictionary -- PROVED

The possible canonical component types are exactly:

| rank `s` | overlap `q` | type |
|---:|---:|---|
| 1 | 0 | `P_1` |
| 2 | 0 | `P_1+P_1` |
| 2 | 1 | `P_2` |
| 2 | 2 | `C_2` |
| 3 | 0 | `P_1+P_1+P_1` |
| 3 | 1 | `P_2+P_1` |
| 3 | 2 | `P_3` or `C_2+P_1` |
| 3 | 3 | `C_3` |

Thus the numbers of types at ranks one, two and three are

\[
\boxed{\nu_1=1,\qquad \nu_2=3,\qquad \nu_3=5.}
\]

### Proof

Every component is a path or cycle and the total number of arcs is `s`. Partition `s` into component arc counts and impose the overlap contribution `j-1` for a path and `j` for a cycle.

For `s=1` only `P_1` is possible. For `s=2`, the partitions give two isolated arcs, one two-arc path or one two-cycle. For `s=3`, the possibilities are three isolated arcs, a two-arc path plus an isolated arc, a three-arc path, a two-cycle plus an isolated arc, or a three-cycle. Their overlaps are respectively `0,1,2,2,3`. QED.

## RI5av -- derangement probability is type-blind inside one overlap -- PROVED

For fixed `(t,s,q)`, every type in RI5au has the same extension count

\[
E(t,s,q)
=
\sum_{j=0}^{t-2s+q}
(-1)^j
\binom{t-2s+q}{j}(t-s-j)!,
\]

and hence the same probability `p_{t,s,q}=E(t,s,q)/D_t`.

The only type refinement not already determined by `(s,q)` is

\[
(s,q)=(3,2):
\qquad
P_3
\quad\hbox{or}\quad
C_2+P_1.
\]

### Proof

RI5ap proves that the extension count depends only on the number `t-2s+q` of still-available diagonal positions. The component arrangement does not enter that count. The table in RI5au shows that every `(s,q)` has one type except `(3,2)`. QED.

## Exact type amplification

Let `L` be the finite arithmetic/profile alphabet used after fixing `(t,s,q)`, excluding the path/cycle type bit. Define

\[
\tau_{s,q}
=
\begin{cases}
2,&(s,q)=(3,2),\\
1,&\text{otherwise}.
\end{cases}
\]

## RI5aw -- exact type-local large-profile output -- PROVED

In the large blocker alternative of RI5at, one exact path/cycle type and arithmetic profile has raw weight at least

\[
\boxed{
\frac{G}{36\,\tau_{s,q}\,p_{t,s}^{\rm sharp}L}
}
\]

for some `t>=7`, `s<=3` and feasible overlap `q`. Consequently,

\[
\boxed{
\frac{G}{36\,\tau_{s,q}\,p_{t,s}^{\rm sharp}L}
\ge
\frac{(t)_sG}{108\,\tau_{s,q}L}
\ge
\frac{(t)_sG}{216L}.
}
\]

### Proof

RI5at gives one exact overlap/arithmetic profile with raw weight at least `G/[36 p_sharp L]`. By RI5av that class contains at most `tau_{s,q}` canonical types, all with the same cylinder probability. Pigeonhole over that final type bit and apply `p_sharp<=3/(t)_s`. QED.

## RI5ax -- corrected exact blocker frontier -- PROVED

Every selected large blocker obstruction is now one of the nine explicit partial-permutation types together with:

- occupancy `t`;
- rank `s`;
- overlap `q`;
- quotient, scale, carry and physical arithmetic labels.

There is no further hidden combinatorial structure in the derangement prescription. The only unresolved work is arithmetic classification, payment or recurrence of one exact labelled path/cycle type.

## Finite check

`scripts/verify_ri_partial_permutation_types.py` enumerates all injective fixed-point-free prescriptions of rank at most three, verifies the nine-type dictionary and checks exhaustive derangement extension counts through size seven.
