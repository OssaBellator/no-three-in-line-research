# First-host raw-lineage promotion gap

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact schema-compatibility obstruction. It does not prove physical realization or physical exclusion of any background.

## Projected first-host convention

For host `s4-75b04c45c1c8eac2`, the side-four projection removes the diagonal, target `01`, and deletion edges `02,20` from the response host. The resulting nine response-eligible edges admit exactly

```text
3012: intrinsic triples 1
3210: intrinsic triples 4.
```

The target is deliberately not response-eligible.

## Installed raw-lineage convention

The installed raw-lineage validator requires

```text
target in host_edges
```

and then computes the response family from every edge in `host_edges`.

Copying the projected first-host edges directly therefore fails with

```text
target in host.
```

Adding target `01` satisfies that condition, but expands the matching family to

```text
1032: intrinsic triples 0
1230: intrinsic triples 1
3012: intrinsic triples 1
3210: intrinsic triples 4.
```

Reusing the projected response count two then fails with

```text
response linkage.
```

Thus the projected record cannot be promoted by copying fields into the installed schema. The schema has no separate fields for

1. edges present in the physical lineage host;
2. edges eligible for the response matching.

That distinction is compulsory here: allowing target `01` as a response edge introduces the zero-triple response `1032` and destroys the projected blocker classification.

## Background-coordinate audit

The installed validator bounds host-edge coordinates by `side`, but its only background check is uniqueness. It does not enforce

- integer coordinate type;
- a coordinate range determined by `side`;
- disjointness from host or response points;
- physical deletion causes or owner ancestry;
- declared batch completeness.

After adding target and using the expanded four-response count, the validator accepts an empty background and all four exterior strict-reversal backgrounds:

```text
{(-3,5),(5,-3)}
{(-1,3),(5,-3)}
{(-2,6),(4,0)}
{(-2,6),(6,-2)}.
```

This acceptance is a schema fact, not evidence that those backgrounds are physically realizable.

## Required bridge contract

A usable first-host physical fibre format must separate at least

```text
lineage host edges
response-eligible edges
target edge
coordinate domain
coordinate-labelled background
physical deletion causes
owner/fate/collision/line/interface/CRT ancestry
installed legal operations and intermediate states
labelled child rows, positive weights, and parent budget.
```

The response-eligible edge set must reconstruct exactly `3012,3210`, while the lineage record may still retain target `01` under its correct physical meaning.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_raw_lineage_promotion_gap.py \
  --check data/exact_recurrent_first_host_raw_lineage_promotion_gap.json
```

The checker reconstructs both edge conventions, validates the response-family expansion, tests the installed validator on five distinct backgrounds, verifies injective background-sensitive identifiers, and rejects twelve deliberate corruptions.

Physical background coverage, target-convention reconciliation, legal operations, recurrent child rows, strict Lyapunov weights, global termination, all-side transfer, and `all_n_proved_by_checker` remain zero.
