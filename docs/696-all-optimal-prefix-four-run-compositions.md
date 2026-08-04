# All-optimal prefix four-run compositions

`docs/690` audits every optimal route against the 56 ordered compositions of
 eleven having at most three runs. This chapter identifies the exact route
redundancy across physical matchings and extends the complete all-route audit to
all compositions with at most four runs.

## PP3deu — Exact route deduplication across physical matchings

For each of the two deletion classes, every one of the 104 minimum-crossing
matchings has exactly 144 optimal radius-four routes. This gives

```text
104 * 144 = 14,976
```

route occurrences per deletion.

The coordinate embedding function depends only on

```text
deletion class,
ordered optimal route,
ordered composition,
```

and not on which minimum-crossing matching produced the route. Deduplicating the
14,976 occurrences leaves exactly

```text
3,624 distinct routes
```

in each deletion class. Thus all physical cases can be covered by auditing 7,248
labelled route states rather than 29,952 repeated route occurrences.

## PP3dev — Complete all-route audit through four runs

There are

```text
C(10,0)+C(10,1)+C(10,2)+C(10,3)
= 1+10+45+120
= 176
```

ordered compositions of eleven with at most four positive parts. The new exactly
four-run layer contains 120 compositions.

`scripts/check_prefix_all_optimal_four_run_compositions.py` audits every one of the
7,248 distinct route states against all 176 compositions:

```text
7,248 * 176 = 1,275,648
```

distinct coordinate embeddings. Every embedding succeeds. Because route
deduplication is exact, these checks cover

```text
104 * 2 * 144 * 176 = 5,271,552
```

physical route/composition pairs. The newly added exactly-four-run layer accounts
for

```text
104 * 2 * 144 * 120 = 3,594,240
```

of those pairs.

## PP3dew — Incremental no-three certificate and remaining frontier

The embedding kernel checks every inserted point against every existing point
pair. A collinear triple is accepted only when all three points carry the same run
label. Since the initial 22-point source is already no-three, this incremental
condition is equivalent to the final global mixed-run triple audit; the redundant
cubic rescan is removed in the deduplicated checker.

There are zero failures. The uniform maximum coordinates remain

```text
delete {0,2}: 120,
delete {3,5}: 154.
```

The complete ordered-composition set has 1,024 members, so

```text
1,024-176 = 848
```

compositions with at least five runs remain unaudited for all 144 optimal routes.
The fixed thirteen-pair source also still lacks a recurrence to larger source
sizes.

## Evidence boundary

This is an exact finite coordinate lift for every optimal route and every
composition with at most four runs. It is not an all-composition theorem, an
all-size insertion selector, or an all-length recurrence.

The all-`n` theorem remains open, and the next theorem identifier is `PP3dex`.
