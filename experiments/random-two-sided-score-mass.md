# Random two-sided score-mass diagnostic

Run

```text
python scripts/check_random_two_sided_score_mass.py \
  experiments/random-two-sided-score-mass-example.json
```

The stored instance uses

```text
W=100,
R=10,000,
T=1,000,
delta=0.20,
h=100.
```

The complementary scores are

```text
rho=620,
chi=310,
rho+chi=930>T-h=900.
```

The exact output is

```text
W 100
R 10000
T 1000
random Ore slack h 100.0
rho 620.0
chi 310.0
score sum 930.0
failure threshold 900.0
forced high-score threshold 450.0
stored movement numerator 1240000.0
delta R high-score bound 1240000.0
one-summand mass threshold 450000.0
outcome fixed_macro_refill_defect_conversion
```

The movement score is the larger score.  Its stored numerator

```text
B_i+U_i(A)=900,000+340,000=1,240,000
```

attains the exact lower bound `delta R rho`.  The macro refill-defect term alone
exceeds the one-summand threshold

```text
delta R(T-h)/4=450,000,
```

so the failed random two-sided Ore condition enters the fixed-macro resource
conversion PP3alo--PP3alq.

The checker also accepts the direct branch when `rho+chi<=T-h`, and verifies the
uniform-margin score-to-numerator and numerator-to-one-summand inequalities.
