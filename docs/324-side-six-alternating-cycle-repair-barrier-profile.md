# Side-six alternating-cycle repair barrier profile

PX13--PX17 establish exact projection-fibre concentration, the alternating-cycle
collateral identity, and finite traps for monotone triple-count and pair-energy
descent. This chapter computes the complete distance and minimax-defect profile
of the same canonical side-six repair graph.

The host is the crossed `cf` product of

\[
((0,1),(1,0))
\quad\text{and}\quad
((0,2,1),(1,0,2)).
\]

Its vertices are all spanning degree-two states and two vertices are adjacent
when their symmetric difference is one alternating cycle.

This is a finite repair-geometry theorem, not an all-side resampling theorem.

## 1. Complete graph profile

### Theorem PX1036 -- PROVED FINITE

The repair graph has exactly:

- `546` degree-two states;
- `20,944` unordered single-cycle adjacencies;
- `2` no-three states.

Every state is within two unweighted cycle toggles of a no-three state. The exact
distance distribution is:

| Shortest distance | States |
|---:|---:|
| 0 | 2 |
| 1 | 112 |
| 2 | 432 |

Thus the obstruction to monotone repair is not graph distance or disconnected
state space: solutions are uniformly close.

## 2. Exact minimax defect barrier

For a path, define its defect barrier as the largest number of bad triples on the
path. Minimize this barrier first and path length second.

### Theorem PX1037 -- PROVED FINITE

For `536` of the `546` states, a path to a no-three state exists whose barrier is
no larger than the starting triple count. Exactly ten states require an increase,
and every one requires an increase by exactly one:

| Minimum barrier excess | States |
|---:|---:|
| 0 | 536 |
| 1 | 10 |

The ten exceptional states are precisely the one-defect local minima already
identified by PX16. Each has minimax profile `(barrier,steps)=(2,2)`.

No state requires defect excess greater than one. This gives an exact finite
target for a repair theorem: controlled one-unit uphill moves suffice on the
canonical side-six host, while strict monotonicity is impossible.

## 3. Length/barrier tradeoff

### Theorem PX1038 -- PROVED FINITE

Among minimax-barrier paths, the exact optimal-length distribution is:

| Optimal minimax steps | States |
|---:|---:|
| 0 | 2 |
| 1 | 112 |
| 2 | 431 |
| 3 | 1 |

The unique three-step state has index `291` in the deterministic state
enumeration and begins with two bad triples. It has a barrier-preserving path

\[
291\to92\to124\to537
\]

with defect sequence

\[
2,2,2,0.
\]

Every two-step path from state `291` to a solution rises above the starting
defect: two such paths pass through defect `3` and four pass through defect `4`.
Therefore shortest-path repair and minimum-barrier repair are genuinely
different optimization problems even in this smallest exact graph.

## 4. Explicit permutation-layer certificate

### Theorem PX1039 -- PROVED FINITE

The barrier-preserving path in PX1038 has the following permutation-layer
decompositions:

1. `((1,0,2,3,5,4),(2,4,5,0,1,3))`;
2. `((0,4,2,1,5,3),(2,0,5,3,1,4))`;
3. `((0,4,3,1,5,2),(2,1,5,0,4,3))`;
4. `((2,1,5,0,4,3),(3,5,4,1,0,2))`.

Each consecutive pair differs by one alternating cycle. The final state is
no-three.

## 5. Consequence for the global repair frontier

The exact graph rules out two oversimplified strategies:

- insist that every move strictly lowers the triple count;
- insist that a shortest route also minimizes peak collateral.

A viable global theorem may instead target a bounded-barrier resampling rule:
permit a controlled defect increase, preserve a separate causal or historical
certificate, and guarantee escape before the temporary collateral accumulates.
The side-six census shows that barrier excess one and at most three moves are
sufficient here, but it does not prove uniform bounds for larger hosts.

## 6. Verification

```bash
python scripts/verify_product_side_six_repair_barrier_profile.py
```

The verifier reconstructs all states and adjacencies, checks the complete defect
and degree distributions, runs multi-source breadth-first and lexicographic
minimax searches, and verifies the explicit path and its two-step obstruction.
