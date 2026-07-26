# Fixed-attempt allocation-or-direct-repair diagnostic

Run

```text
python scripts/check_fixed_attempt_allocation_or_repair.py \
  experiments/fixed-attempt-allocation-or-repair-example.json
```

The stored fixed attempt has `R=10,000`, `T=1,000`, `delta=0.2` and `h=100`.
Both individual unsafe-label counts lie below the margin threshold `delta R=2,000`,
so the attempt enters the uniform-denominator score branch.

The selected score pair has

```text
rho+chi=520+410=930>900=T-h.
```

The larger score forces numerator mass at least

```text
delta R max(rho,chi)=1,040,000.
```

The four stored numerator masses sum to exactly this value.  Their largest summand is
`510,000`, above the one-summand conversion threshold

```text
delta R(T-h)/4=450,000.
```

The converted credited structure is then spent by a zero-insertion direct trade with
credit `160`, giving fixed-universe potential change `-160`.

The exact output is

```text
R 10000
T 1000
delta 0.2
h 100
individual margin threshold 2000.0
movement unsafe 1500
refill unsafe 1000
rho 520
chi 410
score sum 930
Ore threshold 900
score numerator lower bound 1040000.0
numerator masses [120000, 280000, 510000, 130000]
one-mass conversion threshold 450000.0
largest numerator mass 510000
direct repair insertion 0
direct repair credit 160
direct repair change -160
outcome fixed_attempt_allocation_or_direct_repair
```

This verifies the numerical chain PP3aus--PP3auu in the Ore-failure branch.
