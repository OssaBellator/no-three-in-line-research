# Critical-line strict reversal classification

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** complete on the two critical pair lines; physical realization and all-line classification remain open.

## Critical pair lines

The two lines

```text
x+y=2
x+y=4
```

have pair-through-response vector

```text
(3012,3210,2031,2310,3201)=(0,0,1,1,1).
```

Generic integer background points on either line have zero singleton increment,
so generic pairs produce score vector `(1,4,1,1,1)` and only tie `3012` with the
three reopening responses.

A strict reversal can therefore occur only when both background points are
integer intersections with one of the twenty response-secant lines.

## Complete exceptional sets

For `x+y=2`, the admissible exceptional points are exactly

```text
(-3,5), (-1,3), (3,-1), (5,-3).
```

For `x+y=4`, they are exactly

```text
(-2,6), (0,4), (4,0), (6,-2).
```

Each line has six unordered exceptional pairs. Direct triple enumeration of all
twelve pairs gives exactly four strict reversals.

## Complete strict reversal list on the critical lines

```text
x+y=2:
  {(-3,5),(5,-3)}
  {(-1,3),(5,-3)}

x+y=4:
  {(-2,6),(4,0)}
  {(-2,6),(6,-2)}
```

Every strict pair has complete score vector

```text
3012=1, 3210=4, 2031=2, 2310=2, 3201=2,
```

so `3012` is the unique minimizer.

The radius census is

```text
radius 5: 2 pairs
radius 6: 2 pairs.
```

This extends the minimal-radius theorem by adding the two symmetric radius-six
reversals and proving that no other integer pair on either critical line is
strict.

## Scope boundary

This theorem does not classify strict reversals on pair lines having a different
pair-through-response vector. It also does not prove that any of the four pairs
is a realizable background in the installed global construction.

If one of these signatures is physically realizable, the current local reopening
rule cannot choose a lower complete-score response. The state must instead be
excluded by provenance, routed by another legal operation, paid by a strict
budget, or retained in the recurrent offspring matrix.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_critical_line_strict_reversal.py \
  --check data/exact_recurrent_first_host_critical_line_strict_reversal.json
```

The checker reconstructs the two lines, enumerates all integer secant
intersections, audits all twelve exceptional pairs by direct triple counting and
rejects nine deliberate corruptions.

All physical, legal-operation, recurrent-row, strict-Lyapunov and all-`n` flags
remain zero.
