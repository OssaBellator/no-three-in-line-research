# First-host exact safe-signature quotient

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact 31-coordinate classification on the chart-safe background class. It does not prove physical chart confinement or transition congruence.

## Score quotient versus geometric signature quotient

Under chart confinement and response disjointness, the background is a subset of

```text
{00,01,11,22,33}.
```

The 32 subsets have only three complete-score vectors, indexed by the common offset `c=0,1,2`. However, the lossless 31-coordinate background signature has four distinct values.

The difference occurs inside score offset one.

## Exact four classes

### No active target pair

```text
backgrounds: 20
score vector: (1,4,0,0,0)
nonzero signature coordinates: none
```

### Active pair `{00,01}`

```text
backgrounds: 4
score vector: (2,5,1,1,1)
pair-through coordinates:
  response point 02: 1
  response point 03: 1
```

### Active pair `{01,11}`

```text
backgrounds: 4
score vector: (2,5,1,1,1)
pair-through coordinates:
  response point 21: 1
  response point 31: 1
```

### Both target pairs active

```text
backgrounds: 4
score vector: (3,6,2,2,2)
pair-through coordinates:
  response points 02,03,21,31: 1 each
```

The response order for score vectors is

```text
3012,3210,2031,2310,3201.
```

All twenty response-secant line-load coordinates vanish throughout the safe class. Points `22` and `33` are invisible to the current 31-coordinate signature, so they only multiply the members inside each class.

## Exact non-injectivity result

The two offset-one classes have equal current complete scores but different exact pair-through-response coordinates. Therefore

```text
present score equality does not imply 31-signature equality.
```

Consequently the earlier three-state score quotient is not injective on the known geometric signature and cannot be used as a recurrence-state quotient without an additional congruence theorem.

This is stronger than saying payment completeness is unproved: a concrete piece of retained geometric state is already lost by score-only compression.

## Remaining quotient obligation

The four-class signature is an exact candidate state alphabet for the current complete-score geometry, but it is not yet a physical alternating-core signature. A valid recurrence quotient must still prove that every physical occurrence in one class has identical or honestly dominated:

```text
owner and continuation identity
legal operation menu
intermediate-state trace
child labels and multiplicities
positive weights and parent budget
capacity consumption and realization status.
```

No such transition or payment congruence is populated.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_safe_signature_quotient.py \
  --check data/exact_recurrent_first_host_safe_signature_quotient.json
```

The checker recomputes all 32 signatures from the exact 20-line and 11-point coordinate system, verifies the `20,4,4,4` class census, proves the offset-one collision, and rejects eleven deliberate corruptions.

Physical chart confinement, occurrence coverage, legal operations, recurrent child rows, strict Lyapunov slack, global termination, and `all_n_proved_by_checker` remain zero.
