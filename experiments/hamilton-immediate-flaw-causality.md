# Immediate Hamilton flaw causality

Run:

```bash
python scripts/check_hamilton_immediate_flaw_causality.py \
  experiments/hamilton-immediate-flaw-causality-audit.json
```

For each atomic flaw `A`, the diagnostic enumerates every state containing `A`,
every labelled support-one or support-three deletion outcome, and every atomic
flaw newly present after the deletion.  Their union is the immediate causal
out-neighborhood of `A`.

| `m` | atomic flaws | deletion transitions | maximum new flaws in one transition | maximum causal outdegree | total causal edges |
|---:|---:|---:|---:|---:|---:|
| 4 | 224 | 3,456 | 12 | 48 | 7,296 |
| 5 | 2,032 | 65,024 | 40 | 176 | 172,352 |
| 6 | 8,160 | 1,060,864 | 76 | 704 | 2,196,736 |

Separated by owner count, the maximum immediate causal outdegrees are

```text
m=4: two-owner 24,  three-owner 48
m=5: two-owner 152, three-owner 176
m=6: two-owner 364, three-owner 704.
```

The finite results support the deterministic locality theorem in `docs/311`:
an immediate deletion can create a flaw only if that flaw contains one of the
at most three newly inserted orbit blocks.  A fixed orbit block belongs to only
`O(n^2 log n)` atomic collinear-triple flaws.
