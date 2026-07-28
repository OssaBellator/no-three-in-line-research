# Clean-macro fibre width and adjacent-shell rigidity through `m=10`

`docs/350` expresses clean-macro distance by root-cube eligibility masks and
neighbouring cycle minima. This chapter records both the minimum and maximum
distance attained inside every clean orientation fibre. The result shows that,
away from cycles already containing a valid orientation, orientation dependence
is confined to two adjacent shells through `m=10`.

No asymptotic fibre-width or macro-horizon theorem is claimed.

## 1. Fibre distance interval

For a parity-clean Hamilton cycle `rho`, define

```text
d_min(rho) = min_(e in Omega(rho)) d(rho,e),
d_max(rho) = max_(e in Omega(rho)) d(rho,e),
w(rho)     = d_max(rho)-d_min(rho).
```

The root-cube reverse search from `docs/346` and `docs/350` assigns every fresh
orientation the first shell at which it is covered. Recording the first and
last occupied shell gives `d_min`, `d_max`, and the exact set of shell indices
inside each fibre.

### Proposition PP3brd -- PROVED / EXACT FIBRE-WIDTH EXTRACTION

The clean-macro root-cube search computes all fibre intervals without storing
explicit signed states. If a target cycle has minimum distance `j`, then every
fresh source root in the corresponding eligibility mask receives distance
`j+1`. Therefore the minimum and maximum nonempty first-coverage layers are
exactly `d_min(rho)` and `d_max(rho)`.

The same pass detects shell gaps by comparing the observed layer set with the
integer interval from `d_min` to `d_max`. ∎

## 2. Exact width census

### Theorem PP3bre -- VERIFIED FINITELY / NONVALID WIDTH AT MOST ONE

For every parity-clean Hamilton cycle without a valid orientation, through
`m=10`,

```text
w(rho) <= 1.
```

The complete census is

| `m` | clean cycles | valid-containing cycles | complete nonvalid fibres | mixed nonvalid fibres | nonvalid maximum width |
|---:|---:|---:|---:|---:|---:|
| 8 | 3,542 | 10 | 3,526 | 6 | 1 |
| 9 | 31,688 | 4 | 31,676 | 8 | 1 |
| 10 | 297,886 | 4 | 297,844 | 38 | 1 |

The mixed nonvalid cycle pairs `(d_min,d_max)` are

```text
m=8:  (1,2): 2 cycles,  (2,3): 4 cycles;
m=9:  (2,3): 8 cycles;
m=10: (2,3): 26 cycles, (3,4): 12 cycles.
```

Every other nonvalid clean fibre lies in one exact shell.

#### Verification

The checker reproduces the complete signed-state distance ledgers at
`m=8,9,10`, records the first and last first-coverage shell in each clean fibre,
and compares every cycle and state min--max distribution with hard-coded
regression data. ∎

At `m=10`, only 38 of the 297,882 nonvalid clean cycles retain any orientation
dependence in their macro distance.

## 3. Complete-shell distributions

### Theorem PP3brf -- VERIFIED FINITELY / COMPLETE-SHELL DOMINANCE

The numbers of complete nonvalid fibres in each exact shell are

| `m` | shell 1 | shell 2 | shell 3 | shell 4 | shell 5 |
|---:|---:|---:|---:|---:|---:|
| 8 | 446 | 2,644 | 436 | -- | -- |
| 9 | 282 | 6,080 | 23,016 | 2,298 | -- |
| 10 | 458 | 14,590 | 137,640 | 143,896 | 1,260 |

At `m=10` these complete fibres contribute respectively

```text
205,376,
5,512,128,
52,039,168,
57,266,364,
535,072
```

signed states. In particular, the entire maximum-distance layer remains the
complete fifth shell from `docs/348` and `docs/350`.

The only width-two fibres are cycles already containing valid orientations:

```text
m=8: 10 cycles with pair (0,2),
m=9:  4 cycles with pair (0,2),
m=10: 4 cycles with pair (0,2).
```

Those are also the only fibres with a missing intermediate shell. Every
nonvalid fibre has a contiguous one- or two-shell distance set. ∎

## 4. Cycle-coordinate consequence

### Corollary PP3brg -- PROVED / ONE-SHELL ORIENTATION CORRECTION

In the audited range, for every nonvalid clean cycle,

```text
d(rho,e) in {d_min(rho), d_min(rho)+1}
```

for every clean orientation `e` over `rho`.

Thus an upper bound on the cycle minimum immediately gives an upper bound only
one larger for every orientation in the fibre. Moreover, complete-shell cycles
require no orientation correction at all.

This does not yet bound `d_min(rho)` asymptotically. It changes the structural
target: prove a decreasing invariant for the cycle minimum, then control only a
single adjacent-shell boundary rather than an unrestricted orientation spread.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_clean_macro_fibre_width_through_m10.cpp \
  -o /tmp/check_clean_macro_fibre_width_through_m10

for m in 8 9 10; do
  OMP_NUM_THREADS=8 \
    /tmp/check_clean_macro_fibre_width_through_m10 "$m"
done
```

## 5. Revised horizon frontier

The finite horizon problem now separates into two parts.

1. **Cycle minimum.** Bound `d_min(rho)` by a geometric invariant that decreases
   under at least one eligible rotation.
2. **Boundary fibre.** Prove that the observed adjacent-shell rigidity persists,
   or replace it with a uniform width bound.

The exact `3,4,5` maxima are complete cycle shells, not orientation outliers.
The next theorem identifier after this chapter is `PP3brh`.
