# Exact side-seven local minima and transposition-box barrier

PX499--PX500 separate a full-selector host into `P`, an abstract degree-two
selector, and two independent geometric column permutations.  Degree-preserving
search in this space finds one low-defect centre for each of the four canonical
side-seven relative classes from PX495.

This chapter certifies the centres exactly and exhausts their complete
one-transposition product neighbourhoods.  The result is a local obstruction,
not a nonexistence theorem for arbitrary side-seven hosts.

## 1. Four certified low-defect centres

All centres use orientation `cc`.  Permutations are written in one-line form.

| Relative type | `T` | `P` | `Q` | Exact minimum |
|---|---|---|---|---:|
| `(7)` | `(4,6,3,5,1,0,2)` | `(5,4,0,6,2,1,3)` | `(6,0,5,1,2,3,4)` | 4 |
| `(5,2)` | `(6,4,5,2,3,1,0)` | `(4,5,6,1,3,2,0)` | `(6,0,2,5,1,3,4)` | 3 |
| `(4,3)` | `(1,6,4,3,2,0,5)` | `(3,5,4,2,1,0,6)` | `(1,0,6,5,3,4,2)` | 4 |
| `(3,2,2)` | `(6,4,5,2,0,1,3)` | `(4,6,5,3,1,2,0)` | `(3,0,5,6,4,2,1)` | 3 |

Here the relative permutations are the canonical representatives

\[
(1,2,3,4,5,6,0),
\]

\[
(1,2,3,4,0,6,5),
\]

\[
(1,2,3,0,5,6,4),
\]

and

\[
(1,2,0,4,3,6,5),
\]

respectively.

### Theorem PX501 -- PROVED FINITE

The minimum number of real-collinear selected triples among all spanning
degree-two selectors in the four displayed hosts is exactly

\[
\boxed{4,\ 3,\ 4,\ 3.}
\]

The decisive strict-threshold searches visit, respectively,

\[
22{,}233,
\quad
8{,}465,
\quad
14{,}677,
\quad
7{,}983
\]

search nodes.

### Proof

The verifier contains one explicit selector attaining each displayed value.  It
then runs a dynamic minimum-remaining-row search which allows only partial
selectors whose current triple count is strictly below that value.  Column
completion is checked at every node, and all newly formed triples are evaluated
by exact integer determinants.  Every strict-threshold search is empty.
\(\square\)

## 2. One-transposition product boxes

For a permutation `sigma` on seven labels, let

\[
\mathcal B_1(\sigma)
\]

be the set consisting of `sigma` and the 21 permutations obtained by swapping
two entries in its one-line notation.  Thus

\[
|\mathcal B_1(\sigma)|=22.
\]

For one centre `(T,P,Q)`, its full local product box contains

\[
4\cdot22^3=42{,}592
\]

hosts after including all four radix orientations.

### Theorem PX502 -- PROVED FINITE

None of the four local product boxes contains a spanning no-three degree-two
selector.  The exact census is:

| Relative type | Hosts | Selector nodes | Maximum nodes in one host |
|---|---:|---:|---:|
| `(7)` | 42,592 | 34,528,876 | 3,574 |
| `(5,2)` | 42,592 | 28,332,904 | 3,217 |
| `(4,3)` | 42,592 | 30,642,717 | 2,881 |
| `(3,2,2)` | 42,592 | 33,129,180 | 2,792 |

In total,

\[
\boxed{170{,}368}
\]

hosts and

\[
\boxed{126{,}633{,}677}
\]

selector-search nodes are rejected exactly.

### Proof

For every host, the verifier branches on the unprocessed scalar row with the
fewest currently legal pairs.  It prunes if a scalar column can no longer reach
degree two and rejects a choice exactly when either new point completes a
collinear triple.  The search therefore exhausts every spanning degree-two
selector.  The recorded host, total-node, and maximum-node counts are asserted
for each class separately. \(\square\)

## 3. Consequence for the structural frontier

### Corollary PX503 -- PROVED REDUCTION

A successful canonical side-seven full-selector host, if one exists, must lie
outside all four displayed one-transposition product boxes.  In particular it
cannot be obtained from these best certified centres by independently leaving
`T`, `P`, and `Q` fixed or applying one one-line transposition to each.

Together with PX497--PX498, this rules out two distinct local mechanisms:

1. direct one-label insertion from the completed side-six hosts;
2. local transposition repair around the best currently certified side-seven
   centres.

The conclusion does **not** rule out arbitrary non-affine hosts, larger Cayley
moves, or a global selector theorem.  Exploratory random and annealing searches
are not part of PX501--PX503.

## Verification

Compile the exact verifier and run the four cases independently:

```bash
g++ -O3 -std=c++17 scripts/verify_product_side_seven_local_minimum_boxes.cpp -o /tmp/side7_boxes
/tmp/side7_boxes cycle7
/tmp/side7_boxes cycle52
/tmp/side7_boxes cycle43
/tmp/side7_boxes cycle322
```

Each case verifies its witness, exact centre minimum, box host count, complete
zero-selector rejection, total node count, and maximum per-host node count.