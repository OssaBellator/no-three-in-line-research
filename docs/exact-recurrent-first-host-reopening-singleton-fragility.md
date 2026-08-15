# First-host reopenings are not singleton-background robust

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** finite affine secant classification proved exactly.

This chapter studies the first residual host

```text
host       s4-75b04c45c1c8eac2
deletions  {02,20}
responses  3012,3210
```

The local host theorem gives three intrinsically triple-free responses after
reopening a blocked cell:

```text
restore 02 -> 2031 or 2310
restore 20 -> 3201
```

Intrinsic triple-freeness does not imply triple-freeness against an existing
background. This chapter classifies the smallest possible failure.

## ERL-S4.8 — exact common-secant classification

For a single background point `b`, an intrinsically triple-free four-point
response acquires a new triple exactly when `b` lies on one of its six response
secants.

Each of `2031`, `2310`, and `3201` has six distinct secant lines. The affine
points lying on a secant of all three responses are exactly

```text
(-1,4)
(2/3,7/3)
(3/2,3/2)
(7/3,2/3)
(4,-1)
```

Of these, exactly two are integer points:

```text
(-1,4), (4,-1).
```

There is no such integer point inside the original `4 x 4` coordinate square.
Both integer witnesses require exactly one unit of coordinate padding.

### Proof

Enumerate the six normalized primitive secant lines for each response. Intersect
each line from the first family with each line from the second and retain the
intersection exactly when it lies on a line from the third family. Rational
arithmetic gives the five displayed points. Filtering for integral coordinates
gives the two displayed witnesses. The checker independently verifies all
response triples. ∎

## ERL-S4.9 — simultaneous reopening failure

For either integer witness `b`, the complete triple scores are

```text
response  intrinsic  with singleton b
2031          0              1
2310          0              1
3201          0              1
3012          1              2
3210          4             10
```

Thus one background point simultaneously destroys the zero-triple property of
all three local reopening alternatives.

This does not say reopening is useless: each reopened response still has score
one, below the two unreopened response scores in this schema completion. It says
that the phrase “restore a blocked cell and take a zero response” is not a valid
physical operation unless background secant incidences are retained.

## Translation and realizability boundary

The witnesses are relative coordinates. After translating the local side-four
block, `(-1,4)` or `(4,-1)` becomes an ordinary nonnegative grid point whenever
the block has the corresponding one-cell margin. The checker does not prove that
such a translated point occurs in a legal construction state, nor that its owner
or deletion causes are compatible with the first host.

The result is therefore a schema-completion obstruction:

1. normalized host and selector data allow both empty and singleton background
   completions;
2. those completions disagree on whether the reopening responses are zero;
3. a legal transition compiler must retain the actual background secant profile.

## Consequence for the recurrent row

The first-host physical fibre must distinguish at least:

```text
background incidence with every secant of 2031
background incidence with every secant of 2310
background incidence with every secant of 3201
```

A single generic `background present` flag is insufficient. The exact child row
must also state whether a reopened response creates rank-two line children and
who owns those children.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_reopening_singleton_fragility.py \
  --check data/exact_recurrent_first_host_reopening_singleton_fragility.json
```

The checker rebuilds all secant families and rational intersections, verifies the
score table for both integer witnesses, and rejects ten corruption classes.

Global realizability, deletion causes, legal reopening, recurrent rows, strict
Lyapunov descent and the all-`n` conclusion remain unproved.
