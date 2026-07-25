# All-n product track: effective repair and side-seven structural stage

**Branch:** `research/all-n-product-construction`

PX397--PX492 give an effective rectangle-label doubling reduction above
`10^2900`.  PX493--PX498 begin the structural finite-range bridge at the first
unresolved base side, seven.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| PX63 entry | **AUDITED** | Every positive rectangle state re-enters through a label block or high source with explicit destruction and spread. |
| Rectangle invariants | **LIFTED** | Terminal, first-generation, packet, mixed-shadow, and recurrence moves are paired `t/r` label permutations. |
| Paired internal sign | **EFFECTIVE** | `A_3=320` and corrected thinning constants force internal rank-three creation below destruction. |
| Dependency DAG | **AUDITED** | PX492 is the effective closure root; every move-producing dependency is rectangle-label compatible. |
| Active cutoff | **EXPLICIT** | `N_3=10^2900`, using `d(N)<=10^59 N^(16/109)`. |
| Side-seven factor census | **COMPLETE** | PX493--PX495 give 132 saturated configurations, 488 ordered factors, and exactly four relative classes. |
| Direct side-six insertion recursion | **REFUTED** | PX497 rejects all 21,952 inherited one-label host extensions. |
| Auxiliary `(2,2,2)` affine route | **REFUTED** | PX498 rejects all 6,912 affine hosts for the missing predecessor class. |
| Universal side-seven doubling | **OPEN** | One full-selector template is needed for each of `(7)`, `(5,2)`, `(4,3)`, `(3,2,2)`. |
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

A saturated side-seven configuration is a degree-two bipartite graph.  A
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

## Insertion-recursion barrier

The elementary extension of a permutation either fixes the new label or inserts
it into one old arrow.  Applying this independently to `T,P,Q` and inserting the
new label into the relevant relative cycle gives the complete inherited
one-label neighbourhood of the side-six templates.

| Target class | Hosts | Selector nodes | Successes |
|---|---:|---:|---:|
| `(7)` | 8,232 | 34,170,644 | 0 |
| `(5,2)` | 5,488 | 13,077,659 | 0 |
| `(4,3)` | 8,232 | 34,754,272 | 0 |

The auxiliary `(2,2,2)` affine search adds 6,912 failed hosts and 14,345,445
nodes.  These are exact finite obstructions to the simplest recursive mechanism,
not evidence that side-seven closure itself is false.

## Immediate frontier

1. **Arbitrary side-seven full-selector hosts.** Search or construct one host for
   each of the four canonical relative classes, outside the inherited extension
   neighbourhood.
2. **Non-affine `(2,2,2)` predecessor.** Determine whether an arbitrary
   `(2,2,2)` host exists and whether it can seed `(3,2,2)` insertion.
3. **Single-cycle structural theorem.** Replace finite searches for `(L)` by a
   construction or obstruction valid for arbitrary cycle length.
4. **Cross-cycle gluing.** Enrich the PX54 transfer system with geometric data
   sufficient to combine cycle components without cross-component triples.
5. **Finite-range bridge.** Use the resulting structural theorem, rather than
   further divisor-constant tuning, to connect every base side to PX492.

## Verification

```bash
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_side_seven_relative_classes.py
g++ -O3 -std=c++17 scripts/verify_product_side_seven_insertion_barrier.cpp -o /tmp/side7_barrier
/tmp/side7_barrier cycle7
/tmp/side7_barrier cycle52
/tmp/side7_barrier cycle43
/tmp/side7_barrier affine222
```

The side-seven class census and every insertion-barrier case use exact integer
determinants.  Exact all-side product closure and the classical no-three-in-line
conjecture remain open.
