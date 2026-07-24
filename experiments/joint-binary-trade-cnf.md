# Joint binary trade-bank CNF regression

This experiment checks the generic exact interface from
[`docs/45-joint-binary-trade-cnf.md`](../docs/45-joint-binary-trade-cnf.md).

The fixture
[`two-rectangle-binary-bank-n4.json`](two-rectangle-binary-bank-n4.json)
expresses the side-six two-rectangle repair as two arbitrary equal-margin binary
local variables rather than using rectangle-specific input.

Run:

```bash
python scripts/solve_binary_trade_bank.py \
  experiments/two-rectangle-binary-bank-n4.json
```

The exact output has:

- two binary variables;
- eight potentially selected collinear triples;
- four distinct clauses, two unary and two binary;
- maximum clause rank two;
- a satisfying assignment selecting state one for both variables.

The independently verified final configuration is

```text
(1,1), (1,3), (2,4), (2,5),
(3,2), (3,6), (4,1), (4,2),
(5,5), (5,6), (6,3), (6,4).
```

This regression confirms that the generic equal-margin theorem reproduces the
rectangle-specific SAT bank exactly.  Future fixtures may replace either
variable by a reservoir-cycle choice, a two-state parabolic rung, or a
binary tomographic trade without changing the solver or the clause semantics.
