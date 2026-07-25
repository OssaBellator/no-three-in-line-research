# All-n product track: effective repair and side-seven structural stage

**Branch:** `research/all-n-product-construction`

PX397--PX492 give an effective rectangle-label doubling reduction above
`10^2900`. PX493--PX503 isolate the first unresolved finite base, reduce it to
four canonical relative classes, and rule out both direct side-six insertion and
the complete one-transposition neighbourhoods of the best certified side-seven
centres.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| PX63 entry | **AUDITED** | Every positive rectangle state re-enters through a label block or high source with explicit destruction and spread. |
| Rectangle invariants | **LIFTED** | Terminal, first-generation, packet, mixed-shadow, and recurrence moves are paired `t/r` label permutations. |
| Paired internal sign | **EFFECTIVE** | `A_3=320` and corrected thinning constants force internal rank-three creation below destruction. |
| Effective closure root | **AUDITED** | PX492 closes the asymptotic numerical ledger at `N_3=10^2900`. |
| Side-seven factor census | **COMPLETE** | PX493--PX495 give 132 saturated configurations, 488 ordered factors, and four relative classes. |
| Direct side-six insertion recursion | **REFUTED** | PX497 rejects all 21,952 inherited one-label host extensions. |
| Auxiliary `(2,2,2)` affine route | **REFUTED** | PX498 rejects all 6,912 affine hosts for the missing predecessor class. |
| Two-column selector normal form | **AVAILABLE** | PX499 writes every host uniquely as `g_ijs=A_j H^s P^i`; PX500 gives exact alternating-cycle selector moves. |
| Certified side-seven centre minima | **EXACT** | PX501 gives minimum triple counts `4,3,4,3` in the four best centre hosts. |
| Local transposition repair | **REFUTED** | PX502 rejects all 170,368 hosts in the four one-transposition product boxes. |
| Universal side-seven doubling | **OPEN** | A successful host must lie outside both the insertion and local-transposition neighbourhoods. |
| Exact all-side closure | **OPEN** | No structural bridge covers every base below the cutoff. |

## Effective asymptotic constants

\[
T(N)=\lceil N^{3/5}\rceil,
\qquad
A_3=320,
\]

\[
\mathfrak d(N)\le10^{59}N^{16/109},
\qquad
N_3=10^{2900}.
\]

The retained-order exponent is

\[
\frac65-1-\frac{16}{109}=\frac{29}{545}>0.
\]

For every `n>=N_3`, the indexed factor-compatible causal loop lowers the
integer bad-triple potential to zero while remaining inside the rectangle
product state space.

## Exact side-seven classes

A saturated side-seven configuration is a degree-two bipartite graph. A
component of length `2L` contributes an `L`-cycle to the relative permutation.
The exact census is:

| Relative type | Configurations | Ordered factors |
|---|---:|---:|
| `(7)` | 60 | 120 |
| `(5,2)` | 32 | 128 |
| `(4,3)` | 20 | 80 |
| `(3,2,2)` | 20 | 160 |
| **Total** | **132** | **488** |

PX50 therefore reduces universal `2 x 7 -> 14` closure to four canonical
full-selector host problems.

## Two-column selector decomposition

Put

\[
A_0=T,
\qquad
A_1=QT.
\]

Then

\[
\boxed{g_{ijs}=A_jH^sP^i},
\]

and arbitrary `A_0,A_1` are recovered by `T=A_0` and `Q=A_1A_0^{-1}`. The
abstract host has row vertices `(i,u)`, column vertices `(j,w)`, and edges

\[
(i,u)\to(j,H^sP^i(u)).
\]

A spanning abstract degree-two selector remains degree two after either
concatenated or interleaved scalar embedding. Alternating selected/unselected
cycles give exact selector moves without changing `P,A_0,A_1`.

This separates the next search into an abstract two-factor problem and two
independent geometric column-ordering problems.

## Exact local minima and product boxes

The current centre hosts have exact selector minima:

| Relative type | Minimum bad triples |
|---|---:|
| `(7)` | 4 |
| `(5,2)` | 3 |
| `(4,3)` | 4 |
| `(3,2,2)` | 3 |

For each centre, allow `T`, `P`, and `Q` independently to remain fixed or have
one pair of entries swapped, and allow all four orientations. Each box contains

\[
4\cdot22^3=42{,}592
\]

hosts. The exact zero-selector census is:

| Relative type | Hosts | Selector nodes | Successes |
|---|---:|---:|---:|
| `(7)` | 42,592 | 34,528,876 | 0 |
| `(5,2)` | 42,592 | 28,332,904 | 0 |
| `(4,3)` | 42,592 | 30,642,717 | 0 |
| `(3,2,2)` | 42,592 | 33,129,180 | 0 |
| **Total** | **170,368** | **126,633,677** | **0** |

These are exact finite obstructions to local repair, not evidence that the four
canonical host problems are globally unsatisfiable.

## Immediate frontier

1. **Larger permutation moves.** Search Cayley radius two or use nonlocal
   mutations of `P,A_0,A_1`; radius-one product boxes are exhausted.
2. **Global exact decision procedure.** Combine the PX54 transfer system with
   partial coordinate-order assignments and determinant pruning, rather than
   enumerating `7!^3` hosts.
3. **Single-cycle theorem.** Explain the persistent low-defect floor in the
   `(7)` class, or construct a host outside the local basin.
4. **Cross-cycle gluing.** Use the shorter `(5,2)` and `(3,2,2)` three-defect
   centres to identify a componentwise repair that does not create cross-cycle
   triples.
5. **Finite-range bridge.** Convert a successful side-seven or general cycle
   theorem into arithmetic coverage below PX492.

## Verification

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_side_seven_relative_classes.py
python scripts/verify_product_side_seven_two_column_normal_form.py
g++ -O3 -std=c++17 scripts/verify_product_side_seven_insertion_barrier.cpp -o /tmp/side7_barrier
/tmp/side7_barrier cycle7
/tmp/side7_barrier cycle52
/tmp/side7_barrier cycle43
/tmp/side7_barrier affine222
g++ -O3 -std=c++17 scripts/verify_product_side_seven_local_minimum_boxes.cpp -o /tmp/side7_boxes
/tmp/side7_boxes cycle7
/tmp/side7_boxes cycle52
/tmp/side7_boxes cycle43
/tmp/side7_boxes cycle322
```

Every recorded census and minimum uses exact integer determinants. Exact
all-side product closure and the classical no-three-in-line conjecture remain
open.
