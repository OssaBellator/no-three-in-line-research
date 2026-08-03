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

## Import boundary

The three-state quotient is not payment-complete. Current source coverage still
has zero of sixteen physical fields populated, and there is no proof that legal
operations, intermediate states, child rows, weights, budgets or capacities
factor through score offset.

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
.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```

The next admissible cross-branch result must populate a payment-complete physical
signature map and registered continuation edges, or prove directly that every
operation and child row is congruent on the three score classes.
