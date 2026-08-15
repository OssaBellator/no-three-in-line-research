# Exact first-host two-point reversal witness

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** minimal affine integer reversal proved; physical realizability remains open.

## Result

For a singleton integer background, an original residual response never enters the minimizer face. This fails at background size two.

The smallest coordinate radius at which an original response becomes strictly better than every reopening response is

```text
max(|x|,|y|)=5.
```

There are exactly two reversal backgrounds inside `[-5,5]^2`:

```text
{(-3,5),(5,-3)}
{(-1,3),(5,-3)}.
```

Both give the complete score vector

```text
3012 = 1
3210 = 4
2031 = 2
2310 = 2
3201 = 2.
```

Thus `3012` is the unique complete-score minimizer, despite being intrinsically bad and despite all three local reopening responses being intrinsically zero.

## Exact decomposition

For both backgrounds, the line through the two background points is

```text
x+y-2=0.
```

It contains response-union points `02` and `20`, producing pair-through-point contribution

```text
3012=0, 3210=0, 2031=1, 2310=1, 3201=1.
```

One background point contributes one singleton secant hit to `3201`; the other contributes one hit each to `2031` and `2310`. Adding the intrinsic vector

```text
(3012,3210,2031,2310,3201)=(1,4,0,0,0)
```

gives `(1,4,2,2,2)`.

## Minimality

The checker exhausts every unordered background pair disjoint from the response union in two boxes:

```text
radius 4: 70 points, 2,415 pairs, 0 strict original reversals
radius 5: 110 points, 5,995 pairs, 2 strict original reversals.
```

Therefore radius five is minimal for this affine integer phenomenon, and the two displayed pairs are the complete minimal witness set.

## Meaning

This disproves any background-independent rule asserting that one of the three local reopening responses always minimizes the complete geometric score. It does not disprove the no-three-in-line conjecture and does not prove that either background occurs in the installed global construction.

A successful proof architecture must now do at least one of the following:

1. exclude these pair-signature classes by physical provenance;
2. route them through a different legal operation;
3. pay the resulting original-response row with a strict parent budget;
4. retain them as explicit recurrent states.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_two_point_reversal_witness.py \
  --check data/exact_recurrent_first_host_two_point_reversal_witness.json
```

The checker reconstructs the score decomposition, proves radius minimality and rejects eleven corruptions. Every physical-realizability, legal-operation, recurrent-row, Lyapunov and all-`n` flag remains zero.
