# Parabolic parameter sweep

The script
[`scripts/search_parabolic_parameters.py`](../scripts/search_parabolic_parameters.py)
repeats the exact matching-reservoir search over several parabola scales and
branch gaps.

Run:

```bash
python scripts/search_parabolic_parameters.py \
  certificates/prime-patching-small.json \
  --widths 2,3 --max-scale 10
```

The scan covers

```text
2 <= t <= 3
2 <= L <= 10
1 <= d < L
```

with every feasible row and column translation in each stored certificate.

| Source `n` | Parameter/translation instances with a matching | Matching reservoirs | Minimum external triples | Clean patches |
|---:|---:|---:|---:|---:|
| 2 | 0 | 0 | -- | 0 |
| 3 | 0 | 0 | -- | 0 |
| 4 | 1 | 4 | 3 | 0 |
| 5 | 5 | 5 | 4 | 0 |
| 6 | 5 | 5 | 3 | 0 |
| 7 | 6 | 6 | 9 | 0 |
| 8 | 9 | 9 | 10 | 0 |
| 9 | 3 | 3 | 9 | 0 |
| 10 | 8 | 8 | 8 | 0 |

There are 40 matching reservoirs in total and no clean patch.

Every candidate has zero internal patch triples, as guaranteed by PP3ac--PP3ae.
The parameter sweep therefore reinforces rather than weakens the structural
conclusion: varying the parabola scale and branch gap does not reintroduce the
candidate-only obstruction, but it also does not automatically clear the
retained core.

The two best values remain three external triples:

- the `n=4`, `L=2`, `d=1` reservoir with zero retained-pair blockers and three
  retained-anchor triples;
- the `n=6`, `L=2`, `d=1` reservoir with two retained-pair blockers and one
  retained-anchor triple.

No width-three matching reservoir occurs in the stored sides through ten for
this parameter range.  This is a finite property of the current certificate
corpus, not an asymptotic nonexistence result.
