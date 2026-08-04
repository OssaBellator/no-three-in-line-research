# All-optimal prefix four-run compositions

`docs/690` audits every optimal route against the 56 ordered compositions of
eleven having at most three runs. This chapter identifies the exact route
redundancy across physical matchings and extends the complete all-route audit to
all compositions with at most four runs.

## PP3dfa — Exact route deduplication across physical matchings

For each deletion class, all 104 minimum-crossing matchings have exactly 144
optimal radius-four routes, giving 14,976 route occurrences. The coordinate
embedding depends only on deletion class, ordered route, and composition, not on
the matching that produced the route. Deduplication leaves exactly 3,624 distinct
routes in each deletion class.

## PP3dfb — Complete all-route audit through four runs

There are

```text
1+10+45+120 = 176
```

ordered compositions of eleven with at most four positive parts. The exact audit
checks all 7,248 distinct route states against all 176 compositions:

```text
7,248 * 176 = 1,275,648
```

distinct coordinate embeddings. Every embedding succeeds. Exact route
deduplication means these checks cover

```text
104 * 2 * 144 * 176 = 5,271,552
```

physical route/composition pairs. The new exactly-four-run layer accounts for
3,594,240 pairs.

## PP3dfc — Incremental no-three certificate and remaining frontier

The embedding kernel checks every inserted point against every existing point pair
and permits collinearity only when all three points carry one run label. Since the
initial 22-point source is no-three, this is equivalent to the final global
mixed-run audit. There are zero failures. Uniform maximum coordinates remain

```text
delete {0,2}: 120,
delete {3,5}: 154.
```

The complete composition set has 1,024 members, leaving 848 compositions with at
least five runs unaudited for all optimal routes. The fixed thirteen-pair source
also lacks a recurrence to larger source sizes.

The exact checker is
`scripts/check_prefix_all_optimal_four_run_compositions.py`.

## Evidence boundary

This is an exact finite coordinate lift for every optimal route and every
composition with at most four runs. It is not an all-composition theorem, an
all-size selector, or an all-length recurrence. The all-`n` theorem remains open,
and the next theorem identifier is `PP3dfd`.
