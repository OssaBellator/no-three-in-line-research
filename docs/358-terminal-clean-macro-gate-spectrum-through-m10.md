# Terminal clean-macro gate spectrum through `m=10`

`docs/350` expresses clean-macro distance through eligibility masks on one
parity-clean root cube.  A complete shell at distance `h` has no eligible route
to a cycle of minimum distance at most `h-2`, while its neighbours of minimum
distance `h-1` cover the entire fibre.  This chapter audits the closing gate of
the outermost shell at `m=8,9,10`.

No asymptotic macro-horizon or gate-expansion theorem is claimed.

## 1. Terminal predecessor gate

For a parity-clean cycle `rho`, source-owner triple `T`, and its rotated target
cycle `rho^T`, retain the eligibility mask

```text
E_rho(T) subseteq Omega(rho)
```

from `docs/350`.  Let `H_m` be the maximum clean-macro distance at size `m`.
For a terminal cycle with cycle minimum `H_m`, call `T` a closing-gate triple
when

```text
d_min(rho^T)=H_m-1
```

and `E_rho(T)` is nonempty.

### Theorem PP3bru -- VERIFIED FINITELY / COMPLETE TERMINAL-GATE CENSUS

The exact terminal shells and closing gates are

| `m` | `H_m` | terminal cycles | terminal signed states | active closing triples per cycle | minimum per-root gate multiplicity |
|---:|---:|---:|---:|---:|---:|
| 8 | 3 | 436 | 33,624 | 13--47 | 13--47 |
| 9 | 4 | 2,298 | 478,040 | 29--75 | 29--75 |
| 10 | 5 | 1,260 | 535,072 | 70--118 | 70--118 |

For every terminal cycle in all three sizes,

```text
union_(T: d_min(rho^T)<=H_m-2) E_rho(T) = empty,
union_(T: d_min(rho^T)= H_m-1) E_rho(T) = Omega(rho).
```

Thus every terminal fibre is complete, has no two-layer shortcut, and is closed
exactly by its predecessor-shell neighbours.

The aggregate closing-gate totals are

| `m` | total active closing triples | sum of minimum root multiplicities |
|---:|---:|---:|
| 8 | 13,674 | 13,608 |
| 9 | 128,592 | 128,176 |
| 10 | 123,852 | 123,374 |

#### Verification

The checker repeats the exact root-cube reachability computation, records the
cycle minimum of every clean cycle, and examines only cycles in the maximum
cycle layer.  It constructs the lower-shortcut union and the predecessor-shell
closing union, then counts active triples and the number of closing triples
covering each root.  The complete `m=8`, `m=9`, and `m=10` ledgers are hard-coded
as regression values. ∎

## 2. The outer horizon is not a narrow gate

### Corollary PP3brv -- PROVED / VERIFIED FINITELY / DENSE TERMINAL DESCENT

Every signed state in the terminal shell has at least

```text
13 closing rotations at m=8,
29 closing rotations at m=9,
70 closing rotations at m=10
```

that enter a cycle whose minimum distance is one smaller.

#### Proof

The minimum per-root gate multiplicity in PP3bru counts distinct owner triples
whose eligibility mask contains that root and whose target cycle is in the
predecessor shell. ∎

Consequently, the finite `3,4,5` horizon is not produced by a unique or sparse
last move.  Terminal states have a broad forward gate, but all of those gates
land only one cycle shell lower.  The obstruction is therefore shell depth and
reverse concentration, not lack of forward alternatives at the outer boundary.

This supplies the forward-degree half of a possible `D/B` argument.  A future
charge theorem must bound how many terminal-gate labels can invert into one
predecessor-shell target, or construct balanced weights across these many
choices.  The census alone does not provide that reverse bound.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_shell_gate_spectrum.cpp \
  -o /tmp/check_terminal_shell_gate_spectrum

for m in 8 9 10; do
  OMP_NUM_THREADS=12 /tmp/check_terminal_shell_gate_spectrum "$m"
done
```

The next theorem identifier after this chapter is `PP3brw`.
