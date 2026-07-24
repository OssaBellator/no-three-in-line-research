# The four-endpoint alternating core

CMR133--CMR137 reduce every globally nonimproving alternating closure to a
four-endpoint board destroying one specified triple. This chapter gives the
exact finite spread profile of every four-endpoint board and records the
finite-cycle certificate which any genuine positive global minimum must
contain.

## 1. Correction to naive two-layer rematching

CMR129 correctly converts a vertex-disjoint triple family to a same-layer bank
with at least half the target load. A proposed strengthening, formerly labeled
CMR138, claimed that moving selected points in the two layers sequentially
preserves the complete target load. That statement is false without an
old-cell-clean condition.

### Claim CMR138 — REFUTED AS STATED

Moving a labeled point out of its old cell does not ensure that the old
**geometric** cell disappears from the final union: the other layer may occupy
it at the second stage.

An explicit normalized four-column example is

```text
old layer 0 = (0,1,2,3)
old layer 1 = (1,0,3,2)
new layer 0 = (2,3,0,1)
new layer 1 = (0,1,2,3).
```

The first move avoids both old matchings. The second avoids its own old matching
and the new first layer. Nevertheless the final second layer reoccupies every
old cell of layer zero.

Therefore the original proof's sentence “every selected target point is moved,
so every target triple loses a cell” was invalid for unlabeled point sets.

Correct full-load two-layer conversions require one of the following:

1. disjoint inherited row fibres, as in CMR162--CMR165;
2. an explicitly old-cell-clean ordered bank, as in CMR154--CMR156;
3. an exact finite escape certificate, as in CMR147 or CMR151.

None of CMR133--CMR137 uses the refuted strengthening; their target-load
contraction relies only on the valid one-layer conversion CMR129.

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
For a fixed grid triple, follow its indicator around the cycle. Every
zero-to-one change is a creation and every one-to-zero change is a removal. The
indicator returns to its initial value, so the two counts agree. Sum over
triples. ∎

## 5. Limitation of the abstract cycle reduction

CMR143--CMR144 exhibit a potential-one two-cycle at `N=4` with no decreasing
four-endpoint move, while a separate potential-zero saturated state exists.
Therefore balanced four-core cycles cannot be ruled out abstractly, and no
monotone invariant depending only on normalized board type and current triple
potential can prove the full theorem.

The correct remaining target is **inherited escape**: a terminal core arising
from the prime-power construction retains a closure envelope, protected row
sets, quotient state, and carry signatures. One must use that ancestry either
to find a larger old-cell-clean escape move or to prove that the trapped
component cannot arise from the recursive closure.

See [`docs/79-four-endpoint-trap-counterexample.md`](79-four-endpoint-trap-counterexample.md)
for the exact trap and corrected open lemma.

No all-`n` theorem is claimed here. The exact four-board enumeration, cycle
balance, and trap checks are in
[`scripts/verify_prime_power_four_endpoint_core.py`](../scripts/verify_prime_power_four_endpoint_core.py).
