# Iterated heavy-atom cores for oriented legality menus

**Branch:** `research/sparse-algebraic-spread`

SAS5hs--SAS5hw handle one heavy common atom and then either return a second heavy residual atom or an executable residual-independent fan.  This note iterates that reduction.  Since every candidate uses at most `r` exact constraint atoms, a nested common heavy core has depth at most `r`.

## Common-core family

Let `V` be the retained oriented candidates, partitioned by operation square.  Candidate `v` has square weight `w_v=w_Q` and exact atom support `S(v)` with `|S(v)|<=r`.

For a common atom set `C`, define

\[
V_C=\{v:C\subseteq S(v)\},
\qquad
R_C(v)=S(v)\setminus C.
\]

Let `m_Q(C)` be the number of candidates of square `Q` in `V_C`.  For a residual atom `a`, define its current weighted load

\[
L_C(a)=\sum_{v\in V_C:\ a\in R_C(v)}w_v.
\]

The common-core execution contract says that all atoms in `C` may be counted once across the selected fan.  Failure of that contract returns the exact core `C` as a capacity obstruction.

## SAS5hx -- heavy-core extension -- PROVED

If some residual atom has `L_C(a)>tau`, choose the least such atom and put `C'=C union {a}`.  Then

\[
\sum_{v\in V_{C'}}w_v=L_C(a)>\tau,
\]

so the restricted family is nonempty and the core depth increases by one.

### Proof

`V_{C'}` consists exactly of candidates in `V_C` containing `a`; their total vertex weight is the displayed load. QED.

## SAS5hy -- heavy depth is at most support rank -- PROVED

Every nested sequence

\[
\varnothing=C_0\subset C_1\subset\cdots\subset C_k
\]

obtained by SAS5hx has `k<=r`.

### Proof

Every candidate in `V_{C_k}` contains all `k` distinct core atoms, while every support has size at most `r`. QED.

## SAS5hz -- light-residual weighted fan -- PROVED

Suppose `|C|=k`, the common core is shareable, and every residual atom has load at most `tau`.  Then there is a set of candidates using distinct squares and pairwise disjoint residual supports whose weight is at least

\[
\boxed{
\sum_Q
\frac{m_Q(C)w_Q^2}
{m_Q(C)w_Q+(r-k)\tau}.
}
\]

### Proof

Form the residual conflict graph: same-square candidates are adjacent, and candidates from different squares are adjacent when their residual supports intersect.  For candidate `v` from square `Q`, the total closed-neighbourhood weight is at most

\[
m_Q(C)w_Q+\sum_{a\in R_C(v)}L_C(a)
\le m_Q(C)w_Q+(r-k)\tau.
\]

The weighted local-minimum/Caro--Wei bound gives an independent set of weight at least the sum of `w_v^2` divided by these denominators.  Group by square. QED.

## SAS5ia -- depth-r exact fan -- PROVED

If `|C|=r`, every candidate in `V_C` has empty residual support.  Under the common-core execution contract, one may select one candidate from every represented square, with total weight

\[
\boxed{\sum_{Q:m_Q(C)>0}w_Q.}
\]

This equals the bound in SAS5hz with `r-k=0`.

### Proof

A support of size at most `r` containing the `r` core atoms equals `C`; hence residual supports are empty.  Only same-square conflicts remain. QED.

## SAS5ib -- iterated heavy-core router -- PROVED UNDER THE SHARED-CORE CONTRACT

Starting from `C=empty`, repeatedly apply the following deterministic procedure:

1. if the current common core is not jointly shareable, return that exact capacity overload;
2. if a residual atom has load above `tau`, extend by the least such atom;
3. otherwise output the compatible fan of SAS5hz.

The process stops after at most `r` heavy extensions.  Its final output is therefore one of:

- an exact nonshareable core of size at most `r`;
- a compatible residual-independent fan with the SAS5hz weight bound;
- or a depth-`r` fan representing every square surviving the nested heavy-core restriction.

Thus repeated heavy-atom concentration cannot continue indefinitely without producing a bounded exact obstruction or an executable batch.

### Proof

SAS5hx preserves a nonempty family and increases depth; SAS5hy bounds the number of extensions.  If no extension applies, use SAS5hz, and at maximal depth use SAS5ia. QED.

## Updated SAS frontier

The remaining arithmetic task is to prove shareability or payment for the bounded exact core returned by SAS5ib and to connect the resulting fan margin to the global barrier, neutral-output and compression ledgers.

## Finite check

`scripts/verify_sas_iterated_heavy_atom_core.py` generates finite weighted candidate systems, runs the nested heavy-core procedure, checks the depth bound and verifies the light-residual lower bound against the exact maximum-weight independent set.