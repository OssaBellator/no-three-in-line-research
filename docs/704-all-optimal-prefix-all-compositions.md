# All optimal prefix routes for all compositions

This chapter completes the fixed thirteen-pair prefix composition frontier begun
in `docs/684`, `docs/690`, and `docs/698`.

## PP3dfs — Complete deduplicated route family

The 104 minimum-crossing physical matchings and two deletion classes give 208
physical cases. Every case has exact rerouting distance four and exactly 144
optimal routes.

Across physical cases, each deletion class has

```text
14,976 optimal-route occurrences,
3,624 distinct ordered routes.
```

Thus the complete deduplicated family contains 7,248 distinct deletion/route
pairs.

## PP3dft — Every composition succeeds

There are exactly

```text
2^10 = 1,024
```

ordered compositions of eleven. Every one of the 7,248 distinct optimal routes
passes the deterministic coordinate insertion verifier for every composition.

The exact deduplicated audit contains

```text
7,248 * 1,024 = 7,421,952
```

coordinate embeddings with zero failures. Accounting for repeated route
occurrences across physical matchings, this covers

```text
104 * 2 * 144 * 1,024 = 30,670,848
```

physical route/composition pairs.

The uniform maximum coordinates over the complete audit are

```text
delete {0,2}: 144,
delete {3,5}: 156.
```

The checker uses sixteen deterministic route shards and is
`scripts/check_prefix_all_optimal_all_compositions_704.py`.

## PP3dfu — Exact fixed-source closure

For the fixed thirteen-pair source, both canonical deletion classes, every
minimum-crossing physical matching, every optimal radius-four route, and every
ordered composition of eleven are now certified.

No composition-length frontier remains on this source. The only unresolved prefix
question is structural continuation: no theorem currently constructs a compatible
fourteen-pair reservoir or gives an insertion selector uniform across source
sizes.

## Evidence boundary

This is complete finite coordinate evidence for one source size. It is not an
all-size recurrence and does not promote an asymptotic evidence row. The all-`n`
theorem remains open.
