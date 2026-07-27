# p=41 support-thirteen zero-permanent Hall witnesses

Run:

```bash
python scripts/check_p41_zero_permanent_hall_witnesses.py \
  experiments/p41-swapped-quarter-turn-near-example.json \
  experiments/p41-support13-residual-target-permanents.json
```

The checker reconstructs the residual target matrix for each of the eight
support-thirteen supports whose binary permanent is zero.  It independently
verifies:

1. direct residual line-capacity feasibility;
2. the equivalent support-signature inequalities;
3. zero permanent by subset dynamic programming; and
4. a smallest Hall-deficient source set.

Classification:

```text
7 supports: one zero source row
1 support:  one zero target column
0 supports: a higher-order Hall core with all row and column degrees positive
```

The zero source rows are:

```text
source 17: four supports
source 12: one support
source 18: two supports
```

The remaining support is

```text
{1,2,4,6,8,9,10,13,14,17,18,19,20}
```

and has zero target column `4`: none of its thirteen changed sources can
individually use the old target owned by source `4` after the other seven old
blocks are retained.

The result classifies the eight permanent-zero supports.  It does not decide
any positive-permanent support and does not prove support-thirteen
infeasibility.
