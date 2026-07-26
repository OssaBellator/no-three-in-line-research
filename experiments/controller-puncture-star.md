# One-controller puncture star diagnostic

Run

```text
python scripts/check_controller_puncture_star.py \
  experiments/controller-puncture-star-example.json
```

The stored instance uses

```text
R=1,000,000,
gamma=0.35,
xi=0.20,
Q=1,000,000,
q=100,
C=100,000.
```

The exact output is

```text
original domain lower bound 550000
post-puncture lower bound  549999
half-margin threshold       450000
puncture/domain ratio       1e-06
marked self-recapture bound 9.800019600
paid potential upper bound  -98990.199980400
reserve cap per macro       100000
exhausted macros            [1]
outcome one_controller_puncture_frees_star
```

The marked star entries are explicitly declared not to be controlled by the
centre.  This is forced by the definition of a noncontroller blocker witness.
Consequently deleting entries controlled by the centre leaves all designated star
credit in the punctured candidate universe.

The example also illustrates the reserve endpoint: with `beta=0.10`, a macro that
has accumulated `100,000` punctures reaches its stored reserve cap, while isolated
punctures remain negligible at the domain scale.
