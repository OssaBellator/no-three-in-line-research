# Ambient unary positive-support diagnostic

Run

```text
python scripts/check_ambient_unary_positive_support.py \
  experiments/ambient-unary-positive-support-example.json
```

The stored instance uses

```text
Q=101,
q=4,
tau=0.30,
S_1=100.
```

The positive unary cells all share one typed ambient endpoint resource.  Their
chosen retained-source witness pairs form a 100-cycle.

The exact output is

```text
Q 101
q 4
tau 0.3
p1 0.010000000000
positive signatures 100
support expectation 1.000000000000
density threshold 30.000
witness maximum degree 2
sqrt threshold 10
greedy witness matching 50
matching lower bound 5.000
one-layer endpoint bank 25
q^3/Q 0.633663
outcome one_layer_credited_witness_bank
```

The exact conditioned probability is `p1=1/(Q-1)`.  Since the support expectation
exceeds `tau`, the stored instance lies in the dense positive-support branch.  The
witness graph has maximum degree below the square-root star threshold, so the
matching branch supplies 50 vertex-disjoint witness pairs.  Pigeonholing one
source-layer endpoint position retains a 25-point credited bank, much larger than
the selected state size `q=4`.

The checker also verifies the adaptive consistency inequality `q^3<Q` and the
star--matching lower bound `S_1/(2 ceil(sqrt(S_1)))`.
