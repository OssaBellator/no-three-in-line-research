# Binary resource-star conditioning regression

This experiment accompanies:

- [`docs/157-conditional-binary-resource-star-completion.md`](../docs/157-conditional-binary-resource-star-completion.md);
- [`scripts/check_binary_resource_star_conditioning.py`](../scripts/check_binary_resource_star_conditioning.py);
- [`binary-resource-star-conditioning-example.json`](binary-resource-star-conditioning-example.json).

Run

```bash
python scripts/check_binary_resource_star_conditioning.py \
  experiments/binary-resource-star-conditioning-example.json
```

The endpoint host is the complete `4 by 4` bipartite graph. The binary conflicts
all touch left resource zero and split into the centre fibres

```text
centre (0,0): 3 partners
centre (0,1): 1 partner
centre (0,2): 0 partners
centre (0,3): 2 partners.
```

The exact conditional residual results are

```text
centre (0,0): 0 residual perfect matchings
centre (0,1): 4 residual perfect matchings
centre (0,2): 6 residual perfect matchings
centre (0,3): 3 residual perfect matchings.
```

For centre `(0,0)`, the three partner deletions remove every residual edge from
left vertex one. The exact Hall witness is

```text
X                 = {1}
N(X)              = empty
forbidden rights  = {1,2,3}
deficiency        = 1.
```

There are `24` perfect matchings of the full host, of which `13` avoid every
binary resource-star conflict. Exhaustive enumeration verifies for every one of
the 24 matchings that

```text
matching avoids the whole star
if and only if
its residual matching avoids the fibre of its selected centre cell.
```

The checker logic was independently reproduced and executed against this fixture
on 25 July 2026. The finite regression verifies PP3wv--PP3wx and the exact Hall
output; it does not establish the asymptotic superregular or paid hypotheses of
PP3wy--PP3xb.
