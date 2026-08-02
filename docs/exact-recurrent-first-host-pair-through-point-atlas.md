# Exact first-host pair-through-response-point atlas

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** the non-additive pair-through-response-point component is classified exactly; the full two-point score atlas remains open.

## Why this term appears

For a two-point background `B={b1,b2}`, the lossless score identity is

```text
score(Q;B)
 = intrinsic(Q)
 + singleton secant contribution of b1
 + singleton secant contribution of b2
 + number of response points q in Q collinear with b1,b2.
```

The final term is the first part of the 31-coordinate signature that cannot be recovered by adding two singleton score vectors. It is determined by the line through the two background points.

## Exact affine classification

Let `U` be the union of the five candidate responses. It contains 11 integer points. A background-pair line has exactly one of three forms:

1. it avoids `U`, giving the zero vector;
2. it contains exactly one point of `U`, giving that point's response-membership vector;
3. it contains at least two points of `U`, hence is one of the finitely many lines through pairs of points of `U`.

The union-pair line census is

```text
36 distinct lines
28 lines containing 2 union points
 7 lines containing 3 union points
 1 line containing 4 union points.
```

The 11 union points have 11 distinct membership vectors. Combining the zero, one-point and multi-point cases, and identifying equal contribution vectors, yields exactly

```text
39 pair-through-response-point contribution classes.
```

Every stored class has an explicit integer background-pair witness disjoint from `U`. There are 48 stored witnesses because several distinct geometric sources produce the same contribution vector.

## Contribution census

Across the 39 distinct vectors, the sum of the five response contributions has census

```text
total 0   1 class
total 1   4 classes
total 2   8 classes
total 3  12 classes
total 4   8 classes
total 5   4 classes
total 6   1 class
total 10  1 class.
```

The componentwise maxima are

```text
3012: 3
3210: 4
2031: 2
2310: 2
3201: 2.
```

The largest vector is realized when the background pair is `(-1,4),(4,-1)`. Its line is `x+y-3=0`, and its contribution vector is

```text
3012=2, 3210=4, 2031=0, 2310=2, 3201=2.
```

This is only the pair-through-point term. The complete two-point score must also include both singleton secant-incidence vectors.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_pair_through_point_atlas.py \
  --check data/exact_recurrent_first_host_pair_through_point_atlas.json
```

The checker rebuilds the response union, all 36 union-pair lines, all 39 distinct vectors and every integer witness. It rejects twelve deliberate corruptions.

## Boundary

The full two-point signature is

```text
intrinsic + singleton(b1) + singleton(b2) + pair-through-point(b1,b2).
```

Although each of the three variable pieces now has a finite atlas, not every formal combination is geometrically realizable. The next theorem must classify compatible combinations or derive a construction-level restriction that avoids the dangerous combinations.

No physical-coverage, legal-operation, recurrent-row, Lyapunov, termination or all-`n` claim is made.
