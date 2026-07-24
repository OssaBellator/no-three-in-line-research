# Exact parent-bank escape from every prime-five four-core trap

CMR143--CMR144 show that four-endpoint local dynamics can be trapped above the
global minimum. The first prime case behaves differently once the complete
parent-layer bank is restored: every terminal potential-one component at side
length five has an ordered two-layer escape to a no-three state.

This is the first exact model of the inherited-escape mechanism required by the
prime-power programme.

## 1. Complete saturated-state census at side five

A labeled saturated state is an ordered pair of disjoint permutations of
`0,...,4`. There are

\[
5!\,D_5=120\cdot44=5280
\]

such states, where `D_5=44` is the number of derangements.

### Theorem CMR145 — PROVED BY EXHAUSTIVE FINITE CHECK

The exact triple-potential distribution over all `5280` labeled saturated
states is

| potential | number of states |
|---:|---:|
| 0 | 64 |
| 1 | 192 |
| 2 | 960 |
| 3 | 1200 |
| 4 | 904 |
| 5 | 616 |
| 6 | 560 |
| 7 | 336 |
| 8 | 96 |
| 9 | 64 |
| 10 | 32 |
| 11 | 104 |
| 12 | 80 |
| 13 | 32 |
| 14 | 24 |
| 15 | 16 |

Every count uses exact integer determinants over all

\[
\binom{10}{3}=120
\]

triples of each state.

### Proof

The checker enumerates all ordered pairs of permutations, retains the disjoint
pairs, and tests every point triple. ∎

## 2. Terminal components under four-endpoint moves

A **four-move** chooses one permutation layer, chooses four of its five
columns, and rematches their four existing rows while

1. moving every chosen point;
2. avoiding the unchanged opposite layer.

The move preserves saturation and layer disjointness.

### Theorem CMR146 — PROVED BY EXHAUSTIVE FINITE CHECK

Among the `192` potential-one states, the graph of potential-one four-moves has
component-size distribution

\[
80\cdot1,
\qquad
16\cdot2,
\qquad
16\cdot5.
\]

Exactly `88` of these components have no four-move to potential zero. They
consist of

\[
80
\]

isolated states and

\[
8
\]

two-cycles. Thus exactly `96` potential-one states belong to terminal
components for the nonincreasing four-move dynamics.

One explicit terminal two-cycle is

```text
P0 = (0,3,1,4,2)
P1 = (2,4,0,3,1)

Q0 = (0,2,4,1,3)
Q1 = (2,4,0,3,1).
```

The unique triples are

```text
P: (0,0,P0), (2,1,P0), (4,2,P0)
Q: (0,0,Q0), (1,2,Q0), (2,4,Q0).
```

Each state has exactly one potential-one four-move, namely the move to the
other state, and no potential-zero four-move.

### Proof

The checker constructs every legal four-move from every potential-one state,
forms the equal-potential components, and tests all outgoing moves for potential
zero. ∎

This proves that the `N=4` phenomenon is not merely a nonprime exception:
genuine terminal four-core components also occur at the first balanced prime
base.

## 3. Ordered full-parent escape

A **full-parent move** rematches all five points of one layer, moving every
point and avoiding the currently fixed opposite layer. An ordered two-layer
full-parent move performs such a move in one layer and then in the other,
avoiding the newly moved first layer at the second stage.

### Theorem CMR147 — PROVED BY EXHAUSTIVE FINITE CHECK

Every one of the `96` potential-one states in a terminal four-move component has
an ordered two-layer full-parent escape to potential zero.

More precisely, for each trapped state there is a zero-potential saturated
state `(G_0,G_1)` such that

- both `G_0` and `G_1` move every point of their source layers;
- either `G_0` avoids the old second layer, permitting the order `0` then `1`,
  or `G_1` avoids the old first layer, permitting the order `1` then `0`;
- the final layers are disjoint.

The numbers of ordered zero escapes per trapped state are distributed as

\[
1^{16},
\qquad
3^{32},
\qquad
4^{16},
\qquad
5^{32}.
\]

### Proof

The checker enumerates all `64` zero-potential saturated states. For each of the
`96` trapped states it tests pointwise movement of both layers, final
disjointness, and both possible sequential orders. Every trapped state has at
least one valid ordered escape. ∎

For the displayed two-cycle state `P`, one explicit escape is

```text
G0 = (1,0,3,2,4)
G1 = (3,1,4,0,2).
```

Move layer zero first. `G0` avoids the old layer `P1`; then move layer one to
`G1`, which is disjoint from `G0`. The final state has no real collinear triple.

## 4. Consequence for inherited four-core escape

### Corollary CMR148 — PROVED FOR THE EXACT `N=5` STATE SPACE

At side length five, no terminal component of the four-endpoint one-target
closure survives the complete recursive parent bank. Every such component is
an artefact of restricting the move support to four endpoints.

The correct general escape theorem should therefore compare two nested banks:

1. the terminal four-endpoint board;
2. the smallest inherited parent-prefix or opposite-layer bank containing it.

A terminal core should either improve internally or be absorbed by that parent
bank. The exact `N=5` census supports this statement for every locally trapped
potential-one component, not only for one selected example.

This does not prove the prime-power theorem. At larger powers the inherited
parent bank acts on a row fibre rather than on the complete grid, and its
collateral must be charged to protected quotient and carry data. The remaining
target is a parent-escape theorem with a scale-compatible collateral bound.

The complete census, component classification, and ordered escapes are checked
in
[`scripts/verify_prime_five_four_core_escape.py`](../scripts/verify_prime_five_four_core_escape.py).
