# Global integer two-point strict-reversal classification

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact over the full integer lattice for strict original-response minimizers. Physical realization and the full two-point score atlas remain open.

## Statement

For first residual host `s4-75b04c45c1c8eac2`, consider the response menu

```text
3012, 3210, 2031, 2310, 3201
```

and every two-point integer background disjoint from the eleven-point response union.

There are exactly four backgrounds for which an original residual response is the unique complete-score minimizer:

```text
{(-3,5),(5,-3)}
{(-1,3),(5,-3)}
{(-2,6),(4,0)}
{(-2,6),(6,-2)}.
```

Every one has score vector

```text
3012=1, 3210=4, 2031=2, 2310=2, 3201=2,
```

so `3012` is uniquely minimal. No integer two-point background makes `3210` uniquely minimal.

Thus the earlier four critical-line witnesses are not merely the complete list on `x+y=2` and `x+y=4`; they are the complete strict original-response reversal list over the entire integer lattice.

## Exact reduction

For a two-point background `{p,q}`, write

```text
score = intrinsic
      + singleton_increment(p)
      + singleton_increment(q)
      + pair_through_response(line(p,q)).
```

The exact alphabets contain

```text
15 singleton increment vectors
39 pair-through-response vectors.
```

Testing all abstract combinations gives

```text
43 vector triples making 3012 uniquely minimal
 0 vector triples making 3210 uniquely minimal.
```

Abstract compatibility is not sufficient, so the checker resolves the geometry in two cases.

### Pair line through at least two response-union points

Such a pair line is one of the finitely many fixed response-union lines. Only fourteen fixed lines occur among the 43 abstract strict triples.

For each line, the checker separates:

1. its generic integer singleton vector;
2. its finite set of admissible integer intersections with the twenty response secants.

No generic-generic or generic-exceptional combination is strict, so there is no infinite strict family. Auditing the 26 exceptional-pair candidates leaves exactly the four backgrounds above.

### Pair line through exactly one response-union point

Only two pair-vector types can contribute to an abstract strict triple in this case. Their singleton vectors are finite secant-intersection classes. The checker audits 24 candidate pairs and finds no geometrically compatible strict background.

## Consequences

The strict-reversal state space at background size two is finite and fully known. Any proof architecture need not search for additional strict original-response reversals at this background size.

However, infinitely many two-point backgrounds still place `3012` in a non-strict minimizer face, including the generic families on `x+y=2` and `x+y=4`. The full two-point score-signature atlas therefore remains open and is still relevant to recurrent-state closure.

This theorem does not show that any of the four strict backgrounds is physically realizable in the installed construction. Physical provenance must either exclude them, route them through another legal operation, pay their rows with a strict parent budget, or retain them as labelled recurrent states.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_global_integer_two_point_strict_reversal.py \
  --check data/exact_recurrent_first_host_global_integer_two_point_strict_reversal.json
```

The checker reconstructs all geometry from first principles, validates direct triple counts for every surviving pair, and rejects twelve deliberate corruptions.

Physical-background coverage, deletion causes, installed legal operations, recurrent child rows, strict Lyapunov weights, termination, all-side transfer and `all_n_proved_by_checker` remain zero.
