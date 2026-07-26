# Final-universe credit telescoping diagnostic

Run

```text
python scripts/check_final_universe_credit_telescoping.py \
  experiments/final-universe-credit-telescoping-example.json
```

The first stored package has total designated credit `120`, loses `20` entries to
later controller punctures, and has final-universe insertion cost `80`.  Its
surviving credit is `100`, so the final-universe potential decreases by at least
`20`.

The boundary package has

```text
H=36,
W=6,
C=HW=216.
```

It loses `18` credits and has final-universe insertion cost `198`, exactly equal to
the surviving credit.  The strict paid conclusion therefore fails at equality and
the lost-credit dependency table becomes active.

One synthetic realization sends all 18 lost records to the same exact candidate
entry controlled by the later centre `p35`.  The other uses distinct earlier
centres, partners, later controllers, labels, and candidate entries.

The exact output is

```text
paid credit 120
paid lost credit 20
paid surviving credit 100
paid final insertion 80
paid strict gap 20
boundary total credit 216
boundary lost credit 18
boundary surviving credit 198
boundary final insertion 198
repeated lost candidate degree 18
diffuse maximum candidate degree 1
diffuse maximum future-controller degree 1
full forward dependency matching 18
outcome final_universe_payment_or_future_controller_dependency
```

Thus temporal blocker coexistence is irrelevant in the paid case.  At the exact
failure boundary, the lost credit is already an explicit future-controller
candidate stack or a full forward dependency matching.
