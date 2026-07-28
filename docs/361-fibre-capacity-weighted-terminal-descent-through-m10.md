# Fibre-capacity-weighted terminal descent through `m=10`

`docs/358` shows that every signed state in the outer clean-macro shell has many
closing rotations into the predecessor cycle shell.  `docs/359` shows that
choosing those rotations uniformly is nevertheless overloaded after target-fibre
regeneration.  The overload comes from concentrating too much label mass into
small clean fibres.  This chapter applies the simplest exact capacity correction:
weight each closing target cycle proportionally to its clean-fibre size.

No asymptotic terminal-gate theorem is claimed.

## 1. Exact fibre-capacity cancellation

Let `X_h` be the signed states in a complete terminal shell at cycle distance
`h`.  For `x in X_h`, let `G(x)` be its closing owner triples.  A label
`T in G(x)` rotates to a predecessor-shell clean cycle `eta_T`.  Write

```text
F(eta) = size of the clean orientation fibre over eta,
Z(x)   = sum_(T in G(x)) F(eta_T).
```

Choose `T` with probability

```text
P_x(T) = F(eta_T)/Z(x),
```

and then regenerate uniformly in the clean fibre over `eta_T`.

### Proposition PP3bsb -- PROVED / EXACT FIBRE-CAPACITY CANCELLATION

For every signed target state over a predecessor-shell cycle `eta`, the reverse
column load of this policy is

```text
kappa_F(eta) = sum_(x in X_h) m(x,eta)/Z(x),
```

where `m(x,eta)` is the number of closing labels from `x` whose rotated target
cycle is `eta`.

#### Proof

A label from `x` to `eta` is selected with probability `F(eta)/Z(x)`.  Uniform
regeneration assigns probability `1/F(eta)` to each signed state over `eta`.
The two factors cancel, so each such label contributes exactly `1/Z(x)` to each
signed target column.  Summing over the `m(x,eta)` labels and all terminal
sources gives the formula. ∎

Thus small target fibres no longer receive an explicit reciprocal-fibre penalty.
Only the capacity-normalised predecessor concentration remains.

## 2. Exact finite contraction

### Theorem PP3bsc -- VERIFIED FINITELY / CAPACITY-WEIGHTED TERMINAL CHARGE

The exact maximum regenerated column loads are

| `m` | exact maximum load | decimal | maximizing target components | maximizing cycles | overloaded signed columns |
|---:|---:|---:|---:|---:|---:|
| 8 | `1468416446839930521721999/3789940340738886748063650` | `0.387451071737...` | 8 | 2 | 0 |
| 9 | `406616023430754819367780545483294984597292560691/708943793924084504981546740829982708967717363200` | `0.573551848420...` | 8 | 2 | 0 |
| 10 | `5252950050653541320261353842660696885393101/33843848222070502440710524758866309866934400` | `0.155211370060...` | 9 | 2 | 0 |

The underlying raw incoming-label maxima remain `1,744`, `8,574`, and `8,960`,
respectively.  The improvement comes entirely from the source normalisers
`Z(x)`, not from deleting labels.

#### Verification

The checker repeats the exact root-cube reachability and terminal-gate census
from `docs/358`.  It accumulates outward-rounded lower and upper intervals for
every target-cycle sum.  A cycle is retained whenever its upper endpoint can
meet the largest lower endpoint.  Every retained cycle is then recomputed as an
exact rational by grouping equal integer denominators `Z(x)`.  The exact
maximizer, tie count, component count, raw incoming-label maximum, and absence of
overloaded columns are compared with hard-coded regression values. ∎

The two maximizing cycles at each size are related by the same global geometric
symmetry that repeatedly produces paired extremizers in the earlier audits.

## 3. Uniform finite margin

### Corollary PP3bsd -- PROVED / TERMINAL CHARGE BELOW THREE FIFTHS

For every terminal signed state at `m=8,9,10`, the fibre-capacity-weighted policy
has maximum reverse-column load strictly below

```text
3/5.
```

#### Proof

The largest of the three exact values in PP3bsc is the `m=9` value, and direct
cross-multiplication gives

```text
5 * 406616023430754819367780545483294984597292560691
<
3 * 708943793924084504981546740829982708967717363200.
```

The other two exact values are smaller. ∎

After this terminal descent, clean-fibre regeneration is already included in the
bound.  Any subsequent stochastic clean-cycle heat step can only contract the
inherited `L^infinity` density further.

This closes the finite terminal weighting problem through `m=10`: uniform label
weights amplify, while the explicit local formula `P_x(T) proportional to
F(eta_T)` contracts.  The asymptotic task is to bound

```text
sup_eta sum_x m(x,eta)/Z(x)
```

through a growing frustration window, or to combine this capacity correction
with a geometric Hall-balancing argument.

Compile and run the exact audit with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_terminal_gate_fibre_capacity_weighted_charge.cpp \
  -o /tmp/check_terminal_gate_fibre_capacity_weighted_charge

for m in 8 9 10; do
  OMP_NUM_THREADS=8 \
    /tmp/check_terminal_gate_fibre_capacity_weighted_charge "$m"
done
```

The next theorem identifier after this chapter is `PP3bse`.
