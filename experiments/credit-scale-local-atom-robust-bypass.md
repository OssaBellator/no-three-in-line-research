# Credit-scale local-atom robust-bypass diagnostic

Run

```text
python scripts/check_credit_scale_local_atom_robust_bypass.py \
  experiments/credit-scale-local-atom-robust-bypass-example.json
```

The stored state has

```text
R=1000,
xi=0.2,
s=8.
```

Its three binary atoms have total weighted multiplicity `225000`, but their
complete simple domain loss is only

```text
s(s-1)=56.
```

The local unary movement and refill degrees are `70` and `20`, so the exact
robust-domain calculation is

```text
70+20+56=146 <= xi R=200.
```

The expected output is

```text
R 1000
xi margin 200.000000
inserted state size 8
binary atom weighted multiplicity 225000
binary simple domain loss 56
local unary movement degree 70
local unary refill degree 20
combined robust domain loss 146
local atom count 10
marked removal credit 20
failed unary domain loss 260
source-star lower bound 12.500000
stored source-star fibre 20
outcome robust_atom_bypass_or_composite_source_star
```

Thus arbitrary binary multiplicity and the stored unary table fit inside the
robust margin.  The second stored branch loses `260>200` values to unary shadow.
PP3apd guarantees one inserted-cell/type fibre larger than

```text
xi R/(2s)=12.5,
```

and the example supplies a 20-partner post-trade source star.
