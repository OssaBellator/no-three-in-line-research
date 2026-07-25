# Witness-line survivor-congestion regression

This experiment accompanies
[`docs/105-witness-line-survivor-congestion.md`](../docs/105-witness-line-survivor-congestion.md),
[`scripts/check_witness_line_survivors.py`](../scripts/check_witness_line_survivors.py),
and
[`witness-line-survivor-example.json`](witness-line-survivor-example.json).

Run

```bash
python scripts/check_witness_line_survivors.py \
  experiments/witness-line-survivor-example.json
```

The endpoint host has side `q=6`.  The four traces are the parallel nonaxis
lines

```text
y=x-1,
y=x,
y=x+1,
y=x+2
```

restricted to the `6 by 6` endpoint grid.  Their trace lengths are

```text
5, 6, 5, 4.
```

They are pairwise disjoint, so every survivor choice deletes exactly

```text
(5-1)+(6-1)+(5-1)+(4-1)=16
```

distinct endpoint cells.

The exact enumeration has

```text
5*6*5*4 = 600
```

survivor assignments.  Its optimum is

```text
minimum simple resource congestion       = 3,
minimum multiplicity congestion          = 3,
cover size                               = 16.
```

One optimal survivor choice is

```text
(1,0), (2,2), (3,4), (1,3).
```

The average resource-degree lower bound is

```text
ceil(16/6)=3,
```

so the exact optimum is forced by total cover volume.  This finite pencil
illustrates PP3lr--PP3lt: even though one line alone has a congestion-one cover,
a bank of several rich distinct lines can force larger congestion.  The
asymptotic theorem shows that a linear bank of linear-rich lines forces linear
congestion.

This is a regression for the survivor-cover barrier.  It does not rule out an
owner-line endpoint permutation that moves the lines themselves, which is the
separate PP3lg--PP3ll route.
