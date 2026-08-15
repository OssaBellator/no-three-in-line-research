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

Thus generic pairs restore the original response `3012` to minimizer face

```text
{3012,2031,2310,3201}.
```

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

## Global closure of the strict problem

The later global compatibility compiler audits all 15 singleton vectors, all 39
pair vectors, 43 abstract `3012`-strict triples, fourteen fixed response-union
lines and the single-response-point line cases. It proves that the four pairs
above are the complete strict original-response reversal set over the entire
integer lattice at background size two. No `3210`-strict background exists.

Thus the critical-line theorem is no longer merely a partial line-restricted
result. The unresolved two-point work concerns non-strict tie signatures and
physical provenance, not additional strict reversals.

## Exact scope boundary

The current side-four host/response projection does not carry coordinate-labelled
backgrounds, so it cannot physically exclude or realize these four signatures.
The physical compiler must either exclude them by complete provenance, route
them through another installed operation, pay them with a strict budget or
retain them as labelled recurrent states.

All global proof flags, including `all_n_proved_by_checker`, remain zero.
