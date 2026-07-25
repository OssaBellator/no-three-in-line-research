# Rich-line endpoint-energy regression

This experiment accompanies
[`docs/103-rich-line-endpoint-energy.md`](../docs/103-rich-line-endpoint-energy.md),
[`scripts/check_rich_line_energy.py`](../scripts/check_rich_line_energy.py),
and
[`rich-line-energy-example.json`](rich-line-energy-example.json).

Run

```bash
python scripts/check_rich_line_energy.py \
  experiments/rich-line-energy-example.json
```

The endpoint coordinate sets are both `{1,2,3,4}`.  Every owner candidate is the
origin, and the target-cell set is the complete `4 by 4` endpoint rectangle.  The
current diagonal owner lines each contain the other three diagonal target cells,
so

```text
current line load H_0 = 12.
```

Only off-diagonal endpoint assignments are permitted.  Their complete load matrix
is

```text
3 1 0 0
1 3 0 1
0 0 3 0
0 1 0 3
```

and the permitted off-diagonal energy is

```text
W_mu = 4.
```

With `K=1`, PP3lh gives

```text
E[H(pi)] <= W_mu/q = 1 < 12.
```

The exact minimum-cost derangement is

```text
pi = [3,2,1,0]
```

with line load zero.  The regression therefore checks both the first-moment
certificate and an exact improving endpoint assignment.

This fixture is deliberately elementary.  It verifies the owner-line matrix and
assignment calculation; it does not assert that every Hall-derived line bank has
small replacement energy.
