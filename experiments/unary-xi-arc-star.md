# Unary Xi arc-star diagnostic

This finite check accompanies `docs/176-fixed-centre-unary-xi-arc-star-localization.md`.
It verifies the exact local bookkeeping behind PP3abf--PP3abm.

Run:

```bash
python scripts/check_unary_xi_arc_star.py \
  experiments/unary-xi-arc-star-example.json
```

The stored example has no locally clean incoming/outgoing pair of total cost
strictly below the budget. The checker therefore identifies the incoming side as
a heavy arc star. All five unary-admissible incoming arcs have weight at least
half the local budget.

The checker logic was independently reproduced and executed against the committed
fixture on 25 July 2026. The exact finite output has:

```text
compatible pairs: 20
cheap pairs: 0
low incoming arcs: 0
low outgoing arcs: 2
heavy side: incoming
exceptional low arcs on that side: 0.
```

For an instance with a cheap pair, the checker also enumerates directed Hamilton
cycles when `n<=9` and verifies that a prescribed segment

```text
r -> c -> s
```

belongs to exactly

```text
(n-3)!
```

single-cycle states.

The script checks a finite directed-cost instance. It does not establish the
asymptotic divisor bound on the middle-transition relation and does not convert
the resulting fixed-axis heavy star.
