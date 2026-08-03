# Exact recurrent alternating-core import progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track records only interfaces imported from the main-focus branch
`research/alternating-core-chain`. It does not identify the alternating-core
construction with the prime-power side-four construction.

## ERL1w — cross-branch contract audit

Four alternating-core interfaces were audited:

```text
occurrence-lineage gates
physical-signature lineage quotient
physical arithmetic-profile bound
cross-branch event interfaces
```

They provide conditional rules for exact owner continuation, finite physical
signature quotients, shared alias capacities, polynomial arithmetic labels and
physical event costs. They do not supply first-host occurrence records or values
for any of the sixteen required physical fields.

## ERL1x — exact safe score quotient

Under chart confinement and response disjointness, the 32 possible first-host
backgrounds have exactly three complete-score classes:

```text
offset 0: 20 backgrounds
offset 1:  8 backgrounds
offset 2:  4 backgrounds
```

For offset `c`, the score vector in response order
`3012,3210,2031,2310,3201` is

```text
(1+c,4+c,c,c,c).
```

Every class has minimizer face `{2031,2310,3201}`. Thus selector score and the
Boolean original-response-currentness predicate factor through a three-state
alphabet.

## ERL1y — exact side-four arithmetic-profile import

For side four, the normalized primitive direction universe has exactly 15
elements. The 225 ordered direction pairs contain 210 nonzero determinants, and
the nonzero determinant magnitudes are exactly

```text
1,2,...,13.
```

Therefore every reduced determinant-ratio denominator is at most 13, improving
the generic alternating-core safe bound 18. The exact conditional arithmetic
profile stock is

```text
15^2 * sum(q, q=2..13) = 20,250,
```

rather than 38,250. With 16 board anchors, the exact non-scalar address
coefficient is `324,000 * L_ext` rather than `612,000 * L_ext`.

This does not populate `provenance.crt`: no physical source proves determinant
realization for the first host, and the external role dictionary bound `L_ext`
remains absent.

## ERL1z — exact safe 31-signature quotient

The three complete-score classes are not the exact geometric state alphabet.
Recomputing all 31 signature coordinates on the 32 safe backgrounds gives four
classes:

```text
no active target pair: 20 backgrounds
active pair {00,01}:    4 backgrounds
active pair {01,11}:    4 backgrounds
both active pairs:      4 backgrounds
```

All 20 secant line-load coordinates vanish. The two offset-one classes have the
same score vector `(2,5,1,1,1)` but different pair-through coordinates:

```text
{00,01} -> response points 02 and 03
{01,11} -> response points 21 and 31.
```

Thus present score equality does not imply exact 31-signature equality, and the
three-state score quotient is formally non-injective on retained geometry.
The four-state signature quotient is exact for current complete-score geometry,
but transition congruence and payment completeness remain unproved.

## Import boundary

Current source coverage still has zero of sixteen physical fields populated.
There is no proof that legal operations, intermediate states, child rows,
weights, budgets, continuation identity or shared capacities factor through the
four exact signature classes.

The arithmetic import supplies a finite conditional CRT alphabet but not the
actual CRT profile or continuation/payment data.

Therefore:

```text
alternating_core_recurrence_closure_import_allowed = 0
promotion_to_recurrent_row_allowed = 0
all_n_proved_by_checker = 0
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_alternating_lineage_import.py
data/exact_recurrent_first_host_alternating_lineage_import.json
docs/exact-recurrent-first-host-alternating-lineage-import.md

scripts/check_exact_recurrent_first_host_side_four_arithmetic_profile_import.py
data/exact_recurrent_first_host_side_four_arithmetic_profile_import.json
docs/exact-recurrent-first-host-side-four-arithmetic-profile-import.md

scripts/check_exact_recurrent_first_host_safe_signature_quotient.py
data/exact_recurrent_first_host_safe_signature_quotient.json
docs/exact-recurrent-first-host-safe-signature-quotient.md

.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```

The next admissible cross-branch result must populate a payment-complete physical
signature map and registered continuation edges, prove operations and child rows
congruent on the four exact signature classes, or attach a physically
determinant-realized CRT profile and finite external role address.
