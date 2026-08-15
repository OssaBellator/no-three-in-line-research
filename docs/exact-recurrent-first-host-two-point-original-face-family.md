# First-host two-point original-face family

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact affine schema-completion theorem; physical realization remains open.

## Setup

For first residual host `s4-75b04c45c1c8eac2`, use the five-response menu

```text
3012, 3210, 2031, 2310, 3201.
```

Their intrinsic score vector is

```text
(1,4,0,0,0).
```

For a two-point background `{p,q}`, the complete score vector decomposes as

```text
intrinsic
+ singleton secant increment at p
+ singleton secant increment at q
+ pair-through-response contribution of line pq.
```

The final term is the first contribution not present for singleton backgrounds.

## Exact critical lines

Enumerate every line determined by two points in the eleven-point response union.
Exactly two lines have pair-through-response vector

```text
(0,0,1,1,1):
```

```text
x+y=2, containing response-union points 02 and 20;
x+y=4, containing response-union points 13 and 31.
```

No other response-union line contributes one point to each reopening response
while contributing zero points to both original responses.

## Infinite generic family

Neither critical line is a secant of any one candidate response. Each is a
primitive integer line and therefore contains infinitely many integer points.
Only finitely many points must be removed:

1. the eleven response-union points;
2. intersections with the twenty response-secant lines.

Every remaining point has zero singleton increment. Consequently, any two
distinct remaining integer points on either critical line have complete score
vector

```text
(1,4,1,1,1).
```

The minimizer face is therefore

```text
{3012,2031,2310,3201}.
```

Thus a two-point background can promote the original intrinsically bad response
`3012` back into the complete-score minimizer face, even while all three local
reopening responses remain available only at the same positive score.

## Interpretation

This is a direct obstruction to any repair rule that assumes the three
intrinsically zero reopening responses stay strictly preferable after arbitrary
background completion. A complete state must distinguish these pair-line
incidences.

It is not a geometric counterexample to the no-three-in-line conjecture. The
relative affine completions have not been shown to occur in the installed global
construction, and no deletion cause, owner, legal transition, child row or
Lyapunov weight has been attached.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_two_point_original_face_family.py \
  --check data/exact_recurrent_first_host_two_point_original_face_family.json
```

The checker:

- reconstructs all eleven response-union points and twenty response secants;
- enumerates all response-union pair lines;
- proves the two-line classification;
- verifies generic integer witnesses by direct triple counting;
- checks score vector `(1,4,1,1,1)`;
- rejects eight deliberate corruptions.

All physical, recurrent, strict-Lyapunov and all-`n` flags remain zero.

## Next exact target

Determine whether either critical pair-line class can occur in a physically
realizable `{02,20}` fibre. A positive realization must include the full
31-coordinate background signature, deletion causes, physical owner/provenance
labels and installed legal operations. A negative result must prove that the
global construction excludes both critical line classes.
