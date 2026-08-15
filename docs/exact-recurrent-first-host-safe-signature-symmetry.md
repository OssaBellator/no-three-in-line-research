# First-host safe-signature symmetry obstruction

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact finite automorphism audit. It does not prove physical chart confinement or transition congruence.

## Ordered Boolean signature

On the chart-safe background class, define

```text
left bit  a(B)=1[{00,01} subset B]
right bit b(B)=1[{01,11} subset B].
```

The exact 31-coordinate signature is determined by the ordered pair `(a,b)`:

```text
(0,0): no active pair
(1,0): pair {00,01}
(0,1): pair {01,11}
(1,1): both pairs.
```

The complete score vector depends only on the sum `a+b`:

```text
(3012,3210,2031,2310,3201)
  = (1+a+b,4+a+b,a+b,a+b,a+b).
```

Thus score offset one merges `(1,0)` and `(0,1)`. The previous exact signature audit proved that these states retain different pair-through-response coordinates.

## Ambient coordinate group

The checker enumerates all

```text
4! * 4! * 2 = 1152
```

row relabelings, column relabelings and optional axis swaps. Exactly eight preserve every collinear triple of the standard `4 x 4` grid. They are the ordinary square symmetries obtained from identity or coordinate reversal on each axis, with optional transposition.

## First-host stabilizers

The exact stabilizer census is

```text
ambient collinearity automorphisms        8
lineage-host stabilizer                   2
lineage-host plus deletion stabilizer     2
plus five-response-menu stabilizer        1
exact target-preserving stabilizer        1
```

The same identity-only result holds even when the collinearity requirement is removed and all 1152 row/column/axis relabelings are tested only against the first-host structural data.

Therefore the exact first-host automorphism group is trivial.

## Why transposition fails

The only nonidentity symmetry preserving the lineage host and deletion set is transposition.

It fails in three independent ways relevant to the quotient:

```text
target 01 maps to 10
left pair {00,01} maps to {00,10}, not {01,11}
the five-response menu is not preserved.
```

For example, transposition sends `3012` to the matching

```text
{01,12,23,30},
```

which is outside the five-response menu, while it exchanges `2310` and `3201` and fixes `3210`.

Hence even the relaxed lineage/deletion stabilizer does not exchange the two offset-one activation classes.

## Exact consequence

```text
score equality                         does not imply signature equality
signature collision resolved by symmetry                    no
four exact signature classes reduce to three by symmetry    no
```

The safe signature must retain the ordered two-bit state `(a,b)`. Replacing it by the scalar offset `a+b` loses geometric information and is not justified by any first-host automorphism.

## Remaining recurrence obligation

The ordered two-bit signature is exact for current complete-score geometry. A valid alternating-core physical quotient must still prove that legal operations, intermediate states, child rows, weights, budgets, continuation edges and shared capacities are congruent inside each of the four exact classes.

No such transition or payment congruence is populated.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_safe_signature_symmetry.py \
  --check data/exact_recurrent_first_host_safe_signature_symmetry.json
```

The checker verifies the complete 1152-map census and rejects eleven deliberate corruptions.

Physical chart confinement, occurrence coverage, transition congruence, payment congruence, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
