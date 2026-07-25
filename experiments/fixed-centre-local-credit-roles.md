# Fixed-centre local-credit role diagnostic

This check accompanies
`docs/187-fixed-centre-local-credit-role-splitting.md`.

Run:

```bash
python scripts/check_fixed_centre_local_credit_roles.py \
  experiments/fixed-centre-local-credit-roles-example.json
```

The stored instance has seven endpoint indices, captive centre `0`, and no
source-invalid five-chains. Hence there are

```text
6*5*4*3=360
```

ordered source-clean chains through the centre.

All deterministic local cost is placed in the middle rank-three role with
weight seven, equal to `lambda`. Every chain is therefore expensive and is
assigned to the same role. The middle object is the path

```text
p -> 0 -> s.
```

There are exactly

```text
6*5=30
```

distinct such paths. Each extends to

```text
(7-3)(7-4)=12
```

ordered five-chains, attaining the extension-multiplicity cap exactly. The
checker returns `heavy_rank3_middle_grid`.

Moving the weight seven to `unary_in` exercises the heavy incoming arc family;
moving it to `rank3_left` exercises the heavy outer path family; moving it to
`rank4_in_cross` exercises the fixed-centre rank-four partner family. Setting
all seven role weights below one while keeping `lambda=7` exercises the cheap
local-chain branch.

The diagnostic verifies the seven-role and extension-multiplicity bookkeeping.
It does not pay the extracted heavy family; that handoff uses the existing
arc-petal, paid-grid, outer-path, or rank-four partner chains.
