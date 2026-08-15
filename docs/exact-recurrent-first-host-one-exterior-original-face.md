# First-host one-exterior original-face classification

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact over the full integer lattice for two-point backgrounds with exactly one chart point. Physical occurrence remains open.

## Scope

Consider backgrounds with two distinct integer points, disjoint from the
five-response union, such that exactly one point lies in the standard side-four
chart. The chart point must then lie in

```text
{00,01,11,22,33}.
```

The question is when an original residual response, `3012` or `3210`, enters the
complete-score minimizer face.

## Complete infinite families

There are exactly two infinite families.

### Critical line through `11`

```text
background = {11,(t,2-t)}
t in Z minus {0,1,2}
```

The exterior point lies on `x+y=2`. Generically the score vector is

```text
3012=1, 3210=4, 2031=1, 2310=1, 3201=1.
```

The four exceptional parameters are

```text
t=-3: (-3,5), scores (1,4,1,1,2)
t=-1: (-1,3), scores (1,4,1,1,2)
t= 3: ( 3,-1), scores (1,4,1,2,1)
t= 5: ( 5,-3), scores (1,4,2,2,1).
```

### Critical line through `22`

```text
background = {22,(t,4-t)}
t in Z minus {1,2,3}
```

The exterior point lies on `x+y=4`. Generically the score vector is again
`(1,4,1,1,1)`. The four exceptional parameters are

```text
t=-2: (-2,6), scores (1,4,2,1,2)
t= 0: ( 0,4), scores (1,4,1,1,2)
t= 4: ( 4,0), scores (1,4,1,2,1)
t= 6: ( 6,-2), scores (1,4,1,2,1).
```

In every case `3012` is tied with at least one reopening response. It is never
strictly minimal.

## Complete isolated list

Outside the two critical lines, exactly two one-exterior backgrounds put `3012`
in the minimizer face:

```text
{00,(-3,-1)}
{33,(6,4)}.
```

Both have score vector `(1,4,1,1,1)` and minimizer face

```text
{3012,2031,2310,3201}.
```

No background using chart point `01` has an original response in its minimizer
face.

## Exhaustive reduction

The checker uses the exact decomposition

```text
intrinsic score
+ singleton secant contribution of the exterior point
+ pair-through-response contribution of its line with the chart point.
```

If the pair line contains no response-union point, the pair term is zero and the
complete singleton atlas excludes an original minimizer. Therefore only the 36
lines joining one safe chart point to one response-union point need inspection.

On each line the singleton vector is constant away from intersections with the
20 response secants. The checker audits all 114 admissible integer intersection
candidates. Exactly the two infinite lines and two isolated pairs survive.

## Consequences

```text
one exterior point can create an original-response tie    yes
one exterior point can create a strict original reversal  no
strict two-point reversal requires two exterior points    yes
```

Thus a physical theorem bounding each two-point background to at most one
exterior point would exclude all four strict reversals, but it would not close
selector ties. Closing ties requires chart confinement or exclusion of the two
critical line families and the two isolated pairs.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_one_exterior_original_face.py \
  --check data/exact_recurrent_first_host_one_exterior_original_face.json
```

The checker also compares the exact classification against 18,525 bounded pairs
in `[-30,30]^2` and rejects eleven deliberate corruptions.

Physical one-exterior coverage, legal operations, recurrent child rows, strict
Lyapunov slack, and `all_n_proved_by_checker` remain zero.
