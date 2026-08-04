# All-optimal prefix lifts through four-run compositions

`docs/690` certifies every optimal radius-four route for all compositions of
eleven with at most three runs. This chapter extends the exact coordinate audit to
every composition with at most four runs and removes repeated physical route
occurrences before embedding.

## PP3dex — Exact route-orbit reduction

The fixed thirteen-pair source has 104 minimum-crossing matchings and two deletion
classes. Every physical matching/deletion case has exactly 144 optimal radius-four
routes, so the complete physical route multiset contains

```text
104 * 2 * 144 = 29,952
```

route occurrences.

For a fixed deletion class, the coordinate embedding depends only on the ordered
route and not on which minimum-crossing matching produced it. Deduplicating the
route occurrences therefore preserves the complete geometric audit. In each
deletion class there are exactly

```text
3,624
```

distinct optimal routes.

The source-distance census remains

```text
rerouting distance 4: 208 physical cases,
optimal routes 144:   208 physical cases.
```

## PP3dey — Every composition with at most four runs embeds

The number of ordered compositions of eleven with exactly `r` positive parts is
`binom(10,r-1)`. Hence the number with at most four runs is

```text
1 + 10 + 45 + 120 = 176.
```

For both deletion classes, embed every one of the 3,624 distinct optimal routes
with all 176 compositions. The exact distinct-geometry audit contains

```text
2 * 3,624 * 176 = 1,275,648
```

route/composition embeddings. Every embedding succeeds. There is no mixed-run
collinear triple, and the maximum absolute coordinate remains

```text
delete {0,2}: 120,
delete {3,5}: 154.
```

The incremental verifier checks each inserted point against every existing pair.
The only permitted collinearity is a triple wholly inside the inserted point's
labelled run. Since the fixed source is already no-three, this incremental test
covers every possible forbidden triple without a redundant final cubic scan.

## PP3dez — Exact physical coverage added by four-run compositions

There are exactly

```text
binom(10,3) = 120
```

compositions with four runs. Thus this chapter adds

```text
29,952 * 120 = 3,594,240
```

new physical route/composition pairs beyond the at-most-three-run theorem.
Together, the 176 audited compositions cover

```text
29,952 * 176 = 5,271,552
```

physical route/composition pairs. Repeated route occurrences are represented by
one identical coordinate audit within their deletion class, so this coverage is
exact rather than sampled.

The checker is
`scripts/check_prefix_all_optimal_four_run_compositions.py`.

## Evidence boundary

This is complete for all optimal routes of the fixed thirteen-pair source and all
compositions with at most four runs. Compositions with five or more runs and a
recurrence between source sizes remain open. The theorem is finite coordinate
evidence, not an all-length construction, and the all-`n` theorem remains open.
