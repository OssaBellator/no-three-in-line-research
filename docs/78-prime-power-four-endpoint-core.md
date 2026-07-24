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

More precisely, choose one point from each `Q_i` and partition the chosen points
by permutation layer. In each nonempty layer, pad the chosen set to at least
four endpoints. First rematch the layer-zero board while avoiding the current
layer-one cells. Then rematch the layer-one board while avoiding the new
layer-zero cells. Both stages have an allowed perfect matching, and every
chosen triple loses its selected point.

### Proof

The chosen points are distinct because the triples are vertex-disjoint. Within
each permutation layer they have distinct rows and columns. Pad a nonempty
layer set of size below four by arbitrary further points from that layer.

For the first layer, forbid the old endpoint cells and all cells occupied by the
current second layer. The forbidden board has row and column degree at most two,
so CMR128 gives a perfect matching. This move preserves the first-layer row and
column sets and remains disjoint from the unchanged second layer.

For the second layer, use its original selected rows and columns, but now forbid
its old cells and all cells occupied by the new first layer. Again the forbidden
board has degree at most two, so CMR128 gives a perfect matching. The final two
layers are disjoint permutations.

Every selected target point is moved at its layer's stage. Hence every `Q_i`
loses at least one cell. ∎

Thus the disjoint-defect alternative of CMR124 can preserve target load `s`, not
merely `ceil(s/2)`, if an ordered two-layer bank is permitted.

## 2. Exact four-board state profile

Normalize a four-endpoint board so that the old endpoint matching is the
identity. The opposite layer contributes a partial injective matching `f`; an
entry `f(i)=i` is impossible because the two layers are disjoint. An allowed
state is a permutation `pi` satisfying

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
Under the uniform law on its allowed states, every compatible prescribed
partial matching satisfies

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

All three constants are attained by some partial opposite-layer matching.

The possible numbers of allowed states are exactly

\[
2,3,4,5,6,9.
\]

Among the `108` normalized partial off-diagonal matchings, the state-count
distribution is

\[
6,32,45,12,12,1
\]

in the displayed order.

### Proof

There are finitely many partial injective off-diagonal maps on four rows. The
checker enumerates all `108` maps, all `24` permutations, and every compatible
rank-one, rank-two, and rank-three prescription. ∎

The lower bound of two also has a short structural explanation. After choosing
one allowed perfect matching, contract its edges. Every contracted vertex has
at least one further allowed incoming and outgoing edge because the original
allowed graph has minimum degree at least two. A directed cycle of further
edges lifts to an alternating cycle, whose flip gives a second perfect
matching.

### Corollary CMR140 — PROVED

Let `B` be a four-endpoint board and let `T_r` count real-collinear candidate
certificates containing exactly `r` compatible board cells and `3-r` fixed
outside points. For a uniformly random allowed state,

\[
\mathbb E[\text{new triples touching the board}]
\le
\frac34T_1+
\frac23T_2+
\frac12T_3.
\]

### Proof

Apply the three atom bounds from CMR139 to every candidate certificate and sum
by linearity of expectation. ∎

This is the exact finite replacement for the `72/(t)_r` spread law at the
terminal board size.

## 3. Finite-cycle certificate for a positive global minimum

For fixed `N`, the family of saturated two-permutation states is finite. Fix a
deterministic rule which, given a saturated state with a real triple,

1. chooses one real triple;
2. chooses one of its points;
3. pads that point's layer to four endpoints;
4. chooses one allowed four-board state.

The rule may use lexicographic order throughout.

### Theorem CMR141 — PROVED

Suppose the minimum triple potential among all saturated states at side length
`N>=4` is positive. Then the deterministic four-endpoint closure contains a
finite directed cycle

\[
S_0,S_1,\ldots,S_{r-1},S_r=S_0
\]

such that every transition

- is an allowed four-endpoint rematching in one layer;
- preserves saturation and layer disjointness;
- destroys the triple selected at its source state;
- never visits a state below the global minimum potential.

### Proof

Start from any saturated state attaining the global minimum. Its potential is
positive, so the deterministic rule is defined. Every allowed four-board move
produces another saturated state. By global minimality, no resulting state has
smaller potential. A state of potential zero cannot occur.

Continue indefinitely. There are finitely many pairs consisting of a saturated
state and one of its selected triples. The deterministic rule therefore repeats
a pair, and the segment between two repetitions is the required directed
cycle. Each source triple is destroyed because the chosen endpoint is moved. ∎

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

1. the selected source triple belongs to `R_j` for every `j`;
2. every triple in `R_j union C_j` touches one of the old or new cells of the
   four moved endpoints;
3. for every fixed grid triple `Q`, the number of transitions on which `Q`
   belongs to `C_j` equals the number on which it belongs to `R_j`;
4. consequently
   \[
   \sum_j|C_j|=\sum_j|R_j|.
   \]

### Proof

The first assertion is the construction. A triple using only cells common to
`S_j` and `S_{j+1}` has the same presence in both states, proving the second.

For a fixed grid triple, follow its indicator around the directed cycle. Every
change from zero to one contributes one creation and every change from one to
zero contributes one removal. Since the indicator returns to its initial value,
the two counts agree. Summing over all grid triples proves the final identity. ∎

The remaining alternating theorem is therefore equivalent to ruling out these
balanced local defect-flow cycles, or showing that one contains a state below
its starting baseline. The natural next invariant is the multiset of p-adic
first-separation and carry signatures of the created and removed triples around
the cycle.

No all-`n` theorem is claimed here. The exact four-board enumeration and the
cycle-balance identities are checked in
[`scripts/verify_prime_power_four_endpoint_core.py`](../scripts/verify_prime_power_four_endpoint_core.py).
