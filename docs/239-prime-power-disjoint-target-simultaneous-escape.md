# Disjoint minimum targets admit one simultaneous degree-two Hall escape

CMR1070--CMR1077 use a vertex-disjoint target bank as a compatible contraction
prescription. For target-destruction arguments there is a stronger dynamic use.
Every target has at least two cells in one of the two permutation layers. At
least half of a disjoint target bank therefore have the same majority layer.
Choose one representative cell from each of those targets and rematch that
entire layer while forbidding its old permutation and the fixed opposite
permutation.

The forbidden board is the union of two perfect matchings and has maximum degree
two. The degree-two Hall theorem supplies a new permutation which moves every
representative and remains physically disjoint from the opposite layer. Thus one
bank state destroys a linear fraction of the disjoint targets simultaneously.

Let `S` be a saturated side-`n` state, and let

\[
T_1,\ldots,T_q
\]

be pairwise vertex-disjoint physical target triples of `S`.

## 1. Common majority layer

### Theorem CMR1078 -- PROVED

For every target `T_i`, choose a layer containing at least two of its three
selected cells. One layer `ell` is chosen by at least

\[
\boxed{
q_\ell
\ge
\left\lceil\frac q2\right\rceil
}
\]

targets.

### Proof

Every target has a majority layer. Partition the `q` targets by the chosen layer
and average. ∎

Ties, when all three cells do not lie in one layer, are resolved by a fixed rule.

## 2. Representative cells form a partial matching

For every target in the common-majority subbank, choose one of its cells in
layer `ell`; call the resulting set `R`.

### Theorem CMR1079 -- PROVED

\[
\boxed{|R|=q_\ell.}
\]

The labelled representatives form a compatible partial matching in layer `ell`.

### Proof

The targets are physically disjoint, so the representatives are distinct. They
are all selected in one permutation matching of `S`, so they use distinct source
and target vertices. ∎

## 3. Degree-two Hall rematching moves all representatives

Let `M_ell` be the old permutation in layer `ell`, and let `M_{1-ell}` be the
opposite permutation, kept fixed.

### Theorem CMR1080 -- PROVED

For side `n>=4`, there is a perfect matching `M_ell'` such that

\[
M_\ell'\cap M_\ell=\varnothing,
\qquad
M_\ell'\cap M_{1-\ell}=\varnothing.
\]

Consequently

\[
S'
=
M_\ell'\cup M_{1-\ell}
\]

is a saturated disjoint two-layer state and every representative cell of `R` is
absent from `S'`.

### Proof

The forbidden board is the union of the two old perfect matchings and has maximum
row and column degree at most two. Apply CMR128. Avoiding `M_ell` moves every old
cell in the rematched layer; avoiding the opposite matching preserves physical
layer disjointness. ∎

The construction rematches one layer only and therefore does not use the invalid
sequential-two-layer assumption.

## 4. Simultaneous target destruction

### Theorem CMR1081 -- PROVED

The state `S'` destroys every target assigned to layer `ell`. Hence it destroys
at least

\[
\boxed{
D\ge\left\lceil\frac q2\right\rceil
}
\]

pairwise disjoint designated targets of `S`.

### Proof

Each designated target contains its chosen representative in `R`, and every
representative is absent from `S'`. ∎

No claim is made that the other target cells move.

## 5. Minimum-potential trichotomy

Assume `S` is an actual minimum of the current finite feasible family, with value
`m`. Execute the full-parent bank state `S'` through the canonical host-transition
normalization.

### Theorem CMR1082 -- PROVED

At least one of the following occurs.

1. **Strict improvement:** a feasible normalized state has potential below `m`.
2. **Same-value target handoff:** a minimum state of value `m` destroys at least
   one designated target, so the physical two-label cell cut CMR983 preserves a
   minimum and permanently removes that target until restoration.
3. **Minimum-robust escape:** every target-destroying normalized bank state has
   potential `m+g` with `g>=1`; one such state destroys
   \[
   D\ge\left\lceil\frac q2\right\rceil
   \]
   targets and therefore creates at least `D+g` new triples by CMR991.
4. Exact rollback, added-edge minimum-core contraction, lost-minimum ancestry,
   structural owner/vertex-set exit, or envelope expansion.

### Proof

Use CMR926--CMR957 for execution of the full-parent response. Compare the
resulting target-destroying states with the minimum value and apply
CMR982--CMR997. ∎

## 6. Robust-surplus scale from a target matching

### Corollary CMR1083 -- PROVED

In the minimum-robust branch, the new-triple count satisfies

\[
\boxed{
N
\ge
\left\lceil\frac q2\right\rceil+g.
}
\]

Hence the entry-rank dichotomy CMR1006--CMR1013 and the direct protected
executions CMR1054--CMR1069 apply with destroyed load

\[
D\ge\left\lceil\frac q2\right\rceil.
\]

### Proof

Combine CMR1081--CMR1082 with CMR991. ∎

Thus a large disjoint target matching creates a proportionally large geometric
surplus or strict progress.

## 7. Small-side and restricted-host scope

### Theorem CMR1084 -- PROVED

If `n<4`, the state belongs to the finite base range outside CMR128. If the
current restricted host does not contain `M_ell'`, the missing bank edges are an
explicit added batch and are handled by rollback, added-core contraction,
minimum-loss ancestry, or strict improvement. The theorem does not assume those
edges were already available.

### Proof

This is the scope of CMR128 and the complete host-transition normalization. ∎

## 8. Disjoint-target escape endpoint

### Corollary CMR1085 -- PROVED

The disjoint-target branch of CMR1070 reaches at least one of:

1. simultaneous destruction of at least `ceil(q/2)` targets;
2. strict potential improvement;
3. same-value physical target handoff;
4. a robust-surplus episode of load at least `ceil(q/2)`, followed by direct
   common-layer star, cross-layer star, loaded-line, or large-core execution;
5. rollback, added-core contraction, loss ancestry, factor/wall descent, envelope
   expansion, or finite base handling.

Therefore a large target matching need not be converted immediately into a dirty
fixed core. It has a simultaneous saturated escape bank whose quantitative load
feeds the established robust-surplus machinery.

### Proof

Combine CMR1078--CMR1084 with CMR990--CMR1069. ∎

No all-`n` theorem is claimed. Majority-layer selection, representative
compatibility, degree-two Hall rematching, simultaneous destruction, and scale
arithmetic are checked in
[`scripts/verify_prime_power_disjoint_target_escape.py`](../scripts/verify_prime_power_disjoint_target_escape.py).
