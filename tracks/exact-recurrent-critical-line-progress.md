# Exact recurrent critical-line progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This addendum records the completed two-point analysis on the two critical
pair-through-response lines for first host `s4-75b04c45c1c8eac2`.

The classical no-three-in-line conjecture remains open. None of the affine
background families below has been proved physically realizable in the installed
global construction.

## Critical pair-through-response lines

Exactly two response-union pair lines have contribution vector

```text
(3012,3210,2031,2310,3201)=(0,0,1,1,1):
```

```text
x+y=2, through response-union points 02 and 20
x+y=4, through response-union points 13 and 31.
```

Neither line is a secant of any one candidate response.

## Generic integer pairs

After removing the finite response-union and response-secant intersection set,
each critical line contains infinitely many integer points with zero singleton
increment. Any two distinct such points produce

```text
3012=1, 3210=4, 2031=1, 2310=1, 3201=1.
```

Thus generic pairs restore the original response `3012` to the minimizer face

```text
{3012,2031,2310,3201}.
```

This is the infinite original-face family checked by

```text
scripts/check_exact_recurrent_first_host_two_point_original_face_family.py
```

## Exceptional integer points

Each critical line has exactly four admissible integer intersections with the
twenty response-secant lines.

```text
x+y=2: (-3,5), (-1,3), (3,-1), (5,-3)
x+y=4: (-2,6), (0,4), (4,0), (6,-2).
```

Every strict reversal must use two exceptional points. All six unordered pairs
on each line have been checked by direct triple enumeration.

## Complete strict reversal list on the critical lines

```text
x+y=2:
  {(-3,5),(5,-3)}
  {(-1,3),(5,-3)}

x+y=4:
  {(-2,6),(4,0)}
  {(-2,6),(6,-2)}.
```

Every one has complete score vector

```text
3012=1, 3210=4, 2031=2, 2310=2, 3201=2,
```

so `3012` is the unique minimizer.

```text
radius 5: 2 strict pairs
radius 6: 2 strict pairs.
```

No other integer pair on either critical line is a strict reversal.

## Exact scope boundary

The classification is complete on `x+y=2` and `x+y=4`. It is not yet a theorem
that no strict reversal exists on a pair line with another contribution vector.
It also does not determine physical provenance, deletion causes, legal
operations, child rows, positive weights or termination.

## Mandatory next step

The physical compiler must do one of the following for both critical line
classes:

1. prove they cannot occur in a realizable `{02,20}` fibre;
2. route every occurrence through another installed legal operation;
3. pay the resulting row with a strict parent budget;
4. retain the tie and strict-reversal signatures as labelled recurrent states.

All global proof flags, including `all_n_proved_by_checker`, remain zero.
