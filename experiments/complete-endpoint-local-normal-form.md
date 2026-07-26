# Complete endpoint local-normal-form diagnostic

Run

```text
python scripts/check_complete_endpoint_local_normal_form.py \
  experiments/complete-endpoint-local-normal-form-example.json
```

The stored strictly alternating cycle has ten marked indices and ten ordinary helpers,
so it selects twenty endpoint cells.  The checker exhaustively enumerates every
one-, two-, and three-cell pattern:

```text
20 unary patterns,
190 binary patterns,
1,140 ternary patterns.
```

Every selected cell contains exactly one helper.  Consequently every enumerated
positive pattern has nonempty helper support, with minimum rank one and maximum rank
three.  The directed selected cells also form one permutation cycle.

The extremal controller model declares all twenty selected marked/helper indices to
be active controllers.  Puncturing them costs `20=0.002R` values.  A domain lower
bound of `6,000` falls only to `5,980`, still above the `5,000` half-margin
threshold.

The exact output is

```text
marked size 10
selected cycle cells 20
one-cell patterns 20
two-cell patterns 190
three-cell patterns 1140
minimum helper support rank 1
maximum helper support rank 3
selected controller punctures 20
puncture to R ratio 0.002
initial domain lower bound 6000.000000000001
post-puncture lower bound 5980.000000000001
half-margin threshold 5000.0
outcome complete_endpoint_rank_three_local_normal_form
```

This verifies the exhaustive support and margin claims behind PP3atv--PP3aty in a
finite model.
