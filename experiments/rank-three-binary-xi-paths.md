# Rank-three binary Xi path diagnostic

This finite check accompanies
`docs/177-fixed-centre-rank-three-binary-xi-path-localization.md` and verifies the
weighted path bookkeeping behind PP3abn--PP3abu.

Run:

```bash
python scripts/check_rank_three_binary_xi_paths.py \
  experiments/rank-three-binary-xi-paths-example.json
```

The stored example has six noncentre indices. Every source path is allowed, every
predecessor and successor path has cost `1`, and every middle path has cost `10`.
The local budget is `12`. Thus every five-index chain has deterministic cost
exactly `12`, so no chain is strictly cheap.

All six predecessor middles and all six successors have at least three low-cost
outer choices. The checker therefore finds a `6 by 6` high-choice product, removes
the six diagonal pairs, and reports a heavy middle rectangle on thirty ordered
pairs with total weight `300`.

For a cheap-chain test, change one middle cost through
`middle_cost_overrides`, for example:

```json
[[1, 2, 2]]
```

Then a chain through the middle pair `(1,2)` has total cost `4`. For `n=7`, the
checker also verifies that the selected four-arc chain occurs in exactly

```text
(7-5)!=2
```

directed Hamilton cycles.

The diagnostic checks the finite weighted-choice theorem. It does not prove the
asymptotic divisor bound for the source-invalid middle relation and does not pay
the heavy middle rectangle or outer-role family.
