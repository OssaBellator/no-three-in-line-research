# Two-scale capacity envelope for terminal descent through `m=10`

`docs/361` gives an explicit terminal-shell policy: a closing rotation to a
predecessor cycle `eta` is weighted proportionally to the clean-fibre size
`F(eta)`, and the target fibre is then regenerated uniformly.  Its exact column
load is

```text
kappa_F(eta) = sum_x m(x,eta)/Z(x),
Z(x) = sum_(T in G(x)) F(eta_T).
```

The exact values through `m=10` are below `3/5`, but the formula by itself does
not identify which part of the incoming family must be controlled
asymptotically.  This chapter separates a low-normalizer harmonic tail from a
high-normalizer counting term.

No asymptotic terminal-gate theorem is claimed.

## 1. Exact two-scale decomposition

Fix

```text
T_m = 2^(m+5).
```

For a predecessor-shell target cycle `eta`, split its incoming labelled terminal
sources according to whether their normalizer `Z(x)` is below `T_m`.  Define

```text
L_m(eta) = sum_(x,Z(x)<T_m) m(x,eta)/Z(x),
H_m(eta) = sum_(x,Z(x)>=T_m) m(x,eta).
```

### Proposition PP3bsh -- PROVED / TWO-SCALE CAPACITY ENVELOPE

For every predecessor-shell signed target column,

```text
kappa_F(eta) <= L_m(eta) + H_m(eta)/T_m.
```

#### Proof

The low-normalizer terms are retained exactly.  Every high-normalizer label has
`Z(x)>=T_m`, so its contribution `1/Z(x)` is at most `1/T_m`.  Summing the two
parts proves the bound. ∎

This is deliberately weaker than the exact harmonic sum, but it separates the
remaining asymptotic task into two concrete estimates: a low-capacity tail and a
bulk reverse-multiplicity count.

## 2. Exact finite envelope

### Theorem PP3bsi -- VERIFIED FINITELY / COMPLETE TWO-SCALE CENSUS

The exact maxima of

```text
E_m(eta) = L_m(eta) + H_m(eta)/T_m
```

are

| `m` | `T_m` | exact maximum envelope | decimal | low labels at maximizer | high labels at maximizer | target components |
|---:|---:|---:|---:|---:|---:|---:|
| 8 | 8,192 | `1468416446839930521721999/3789940340738886748063650` | `0.387451071737...` | 1,744 | 0 | 8 |
| 9 | 16,384 | `80380644898328654826210429323/137462767954375595411229359040` | `0.584744844691...` | 4,222 | 4,352 | 9 |
| 10 | 32,768 | `17257/63040` | `0.273746827411...` | 256 | 8,704 | 10 |

At each size the maximum is attained by exactly two target cycles.

#### Verification

The checker repeats the exact root-cube terminal-gate computation.  For every
incoming label it records the integer normalizer `Z(x)`.  Terms below `T_m` are
grouped by exact denominator and summed as a reduced rational.  Terms above the
threshold are counted and contribute the rational upper bound `H_m/T_m`.
Outward-rounded intervals retain every possible maximizer before the final exact
rational comparison.  All displayed values, label counts, component counts, and
tie counts are hard-coded regression data. ∎

## 3. A finite `3/5` certificate with separated obligations

### Corollary PP3bsj -- PROVED / TWO-SCALE ENVELOPE BELOW THREE FIFTHS

For `m=8,9,10`,

```text
sup_eta E_m(eta) < 3/5.
```

#### Proof

The largest envelope is the `m=9` value.  Direct cross multiplication gives

```text
5 * 80380644898328654826210429323
<
3 * 137462767954375595411229359040.
```

The other two exact maxima are smaller. ∎

The useful asymptotic target is therefore no longer the full harmonic sum in one
piece.  It is enough to prove, for a suitable growing threshold, that the
low-normalizer tail remains small and that the high-normalizer reverse
multiplicity is `o(T_m)` or has a fixed margin below it.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_gate_two_scale_capacity_envelope.cpp \
  -o /tmp/check_terminal_gate_two_scale_capacity_envelope

for m in 8 9 10; do
  OMP_NUM_THREADS=8 \
    /tmp/check_terminal_gate_two_scale_capacity_envelope "$m"
done
```

The next theorem identifier after this chapter is `PP3bsk`.
