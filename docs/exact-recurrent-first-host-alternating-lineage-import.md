# First-host alternating-core lineage import gate

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact conditional score quotient and cross-branch import audit. It does not populate a physical occurrence or prove recurrent closure.

## Imported alternating-core contracts

The audit binds four contracts from `research/alternating-core-chain`:

```text
occurrence-lineage gates
physical-signature lineage quotient
physical arithmetic-profile bound
cross-branch event interfaces
```

Those contracts are deliberately conditional.

- Same-owner continuation requires a registered exact occurrence edge.
- Symbolic aliases may be quotiented only through a finite payment-complete physical signature.
- All aliases sharing one signature gate must share its capacity.
- Arithmetic and event-cost imports retain their physical realization hypotheses.

They do not supply a physical `{02,20}` occurrence, continuation graph, operation trace, child row, or payment value.

## Exact safe score quotient

Under the previously declared chart-confinement and response-disjointness predicates, the first-host background lies in

```text
{00,01,11,22,33}.
```

The 32 subsets have exactly three complete-score vectors. Writing `c` for the common offset:

```text
c=0: 20 backgrounds, scores (1,4,0,0,0)
c=1:  8 backgrounds, scores (2,5,1,1,1)
c=2:  4 backgrounds, scores (3,6,2,2,2)
```

The coordinate order is

```text
3012,3210,2031,2310,3201.
```

Every class has minimizer face

```text
{2031,2310,3201}.
```

Thus the safe selector layer admits an exact three-state quotient, and the Boolean predicate

```text
an original residual response belongs to the minimizer face
```

factors through that quotient with constant value false.

## Why three score states are not a physical signature quotient

Alternating-core's physical-signature theorem requires every payment-relevant field to factor through the quotient. That condition is not met.

The exact source-coverage census remains

```text
required physical fields       16
source-backed populated fields  0
```

In particular, no source proves that two backgrounds with the same score offset have identical:

```text
physical owner and continuation identity
legal operation menu
intermediate-state trace
labelled child multiplicities
positive child weights
parent budget
capacity consumption
realization status.
```

The full background may affect future operations even when its present complete score agrees. Therefore the three-class quotient is exact for selector scores, but not known to be payment-complete or transition-congruent.

## Exact import result

```text
finite selector-score alphabet                         yes
original-response currentness factors through it       yes
payment-complete physical signature proved             no
legal operations factor through score class            no
child rows factor through score class                   no
registered occurrence continuation graph populated     no
shared quotient capacities populated                   no
alternating-core recurrent closure import allowed       no
```

A future import may be enabled only after every physical occurrence is mapped to a payment-complete signature, every legal continuation is registered, and shared capacities or another alternating-core closing route are populated.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_alternating_lineage_import.py \
  --check data/exact_recurrent_first_host_alternating_lineage_import.json
```

The checker reconstructs the three score classes from all 32 safe backgrounds, joins the sixteen-field source census, validates the four alternating-core source contracts, and rejects eleven deliberate corruptions.

Physical chart confinement, occurrence coverage, recurrent child rows, strict Lyapunov slack, global termination, and `all_n_proved_by_checker` remain zero.
