# The four-endpoint alternating core

CMR133--CMR137 reduce every globally nonimproving alternating closure to a
four-endpoint board destroying one specified triple. This chapter strengthens
the disjoint-defect conversion, gives the exact finite spread profile of every
four-endpoint board, and records the finite-cycle certificate which any genuine
positive global minimum must contain.

## 1. Full-load conversion of disjoint defects

CMR129 used one fixed layer and retained at least half of a vertex-disjoint
triple family. By moving the two layers in sequence, the complete family can be
retained.

### Theorem CMR138 — PROVED

Let `Q_1,...,Q_q` be vertex-disjoint real collinear triples in a saturated state
on an `N` by `N` grid, with `N>=4`. Then there is an ordered two-layer endpoint
bank which preserves saturation and layer disjointness and destroys all `q`
triples in every final state.

Choose one point from each `Q_i` and partition the chosen points by permutation
layer. In each nonempty layer, pad the chosen set to at least four endpoints.
First rematch layer zero while avoiding the current layer-one cells. Then
rematch layer one while avoiding the new layer-zero cells.

### Proof

The chosen points are distinct because the triples are vertex-disjoint. Within
each permutation layer they have distinct rows and columns. Pad a nonempty
layer set of size below four by arbitrary further points from that layer.

For the first layer, forbid the old endpoint cells and all cells occupied by the
current second layer. The forbidden board has row and column degree at most two,
so CMR128 gives a perfect matching. This move preserves the first-layer row and
column sets and remains disjoint from the unchanged second layer.

For the second layer, use its original selected rows and columns, but now forbid
its old cells and all cells occupied by the new first layer. Again CMR128 gives
a perfect matching. Every selected target point is moved at its layer's stage,
so every `Q_i` loses at least one cell. ∎

Thus the disjoint-defect alternative of CMR124 can preserve its full target
load if an ordered two-layer bank is permitted.

## 2. Exact four-board state profile

Normalize a four-endpoint board so that the old endpoint matching is the
identity. The opposite layer contributes a partial injective off-diagonal
matching `f`. An allowed state is a permutation `pi` satisfying

\[
\pi(i)\ne i
\]

for every row and

\[
\pi(i)\ne f(i)
\]

whenever `f(i)` is defined.

### Theorem CMR139 — PROVED BY EXHAUSTIVE FINITE CHECK

Every such four-endpoint board has at least two allowed perfect matchings.
Under the uniform law on its allowed states,

\[
\Pr(\text{one prescribed cell})\le\frac34,
\]

\[
\Pr(\text{two prescribed cells})\le\frac23,
\]

and

\[
\Pr(\text{three prescribed cells})\le\frac12.
\]

All three constants are attained. The possible numbers of allowed states are

\[
2,3,4,5,6,9.
\]

Among the `108` normalized partial off-diagonal matchings, the state-count
distribution is

\[
6,32,45,12,12,1
\]

in that order.

### Proof

The checker enumerates every partial injective off-diagonal map, every
permutation, and every compatible rank-one, rank-two, and rank-three
prescription. ∎

The lower bound of two also follows structurally. After choosing one allowed
perfect matching, contract its edges. Every contracted vertex has a further
allowed incoming and outgoing edge because the allowed graph has minimum degree
at least two. A directed cycle of further edges lifts to an alternating cycle,
whose flip gives a second matching.

### Corollary CMR140 — PROVED

Let `T_r` count real-collinear candidate certificates containing exactly `r`
compatible four-board cells and `3-r` fixed outside points. For a uniformly
random allowed state,

\[
\mathbb E[\text{new triples touching the board}]
\le
\frac34T_1+
\frac23T_2+
\frac12T_3.
\]

### Proof

Apply CMR139 to every candidate certificate and sum by linearity of expectation.
∎

## 3. Finite-cycle certificate for a positive global minimum

For fixed `N`, the family of saturated two-permutation states is finite. Fix a
deterministic rule which, given a saturated state with a real triple,

1. chooses one real triple;
2. chooses one of its points;
3. pads that point's layer to four endpoints;
4. chooses one allowed four-board state.

### Theorem CMR141 — PROVED

Suppose the minimum triple potential among all saturated states at side length
`N>=4` is positive. Then the deterministic four-endpoint closure contains a
finite directed cycle

\[
S_0,S_1,\ldots,S_{r-1},S_r=S_0
\]

such that every transition is an allowed four-endpoint rematching, preserves
saturation and layer disjointness, destroys the selected source triple, and
never visits a state below the global minimum potential.

### Proof

Start from a saturated state attaining the global minimum. Its potential is
positive, so the deterministic rule is defined. Every allowed move produces
another saturated state, and global minimality prevents a lower-potential
state. Continue indefinitely. There are finitely many state/selected-triple
pairs, so one repeats and yields the cycle. ∎

Thus failure of the no-three conclusion cannot hide in an infinite or
scale-growing closure. It must produce a finite cycle of four-point trades.

## 4. Exact defect-flow balance on a core cycle

For a transition `S_j -> S_{j+1}`, let

\[
R_j=\mathcal T(S_j)\setminus\mathcal T(S_{j+1}),
\qquad
C_j=\mathcal T(S_{j+1})\setminus\mathcal T(S_j),
\]

where `T(S)` is the set of real collinear triples selected by `S`.

### Theorem CMR142 — PROVED

On every cycle from CMR141:

1. the selected source triple belongs to `R_j`;
2. every triple in `R_j union C_j` touches an old or new moved endpoint cell;
3. every fixed grid triple is created and removed equally often;
4. consequently
   \[
   \sum_j|C_j|=\sum_j|R_j|.
   \]

### Proof

A triple using only cells common to consecutive states has unchanged presence.
For a fixed grid triple, follow its indicator around the cycle. Every zero-to-one
change is a creation and every one-to-zero change is a removal. The indicator
returns to its initial value, so the two counts agree. Sum over triples. ∎

## 5. Limitation of the abstract cycle reduction

CMR143--CMR144 exhibit a potential-one two-cycle at `N=4` with no decreasing
four-endpoint move, while a separate potential-zero saturated state exists.
Therefore balanced four-core cycles cannot be ruled out abstractly, and no
monotone invariant depending only on normalized board type and current triple
potential can prove the full theorem.

The correct remaining target is **inherited escape**: a terminal core arising
from the prime-power construction retains a prefix owner, recursive parent,
protected quotient state, opposite-layer ancestry, and carry signatures. One
must use that ancestry either to find a larger escape move or to prove that the
trapped component cannot arise from the recursive closure.

See [`docs/79-four-endpoint-trap-counterexample.md`](79-four-endpoint-trap-counterexample.md)
for the exact trap and corrected open lemma.

No all-`n` theorem is claimed here. The exact four-board enumeration, cycle
balance, and trap checks are in
[`scripts/verify_prime_power_four_endpoint_core.py`](../scripts/verify_prime_power_four_endpoint_core.py).
