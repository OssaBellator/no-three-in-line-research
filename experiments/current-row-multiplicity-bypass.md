# Current-row multiplicity-blind allocation diagnostic

Run:

```bash
python scripts/check_current_row_multiplicity_bypass.py \
  experiments/current-row-multiplicity-bypass-example.json
```

The stored input contains one fixed-cell fan state and one compatible two-cell
choice-grid state.  For each case the checker:

1. builds the distinct nonaxis lines joining fixed cells to the residual matching
   and, when present, the line between the two fixed cells;
2. verifies the bound `kn+binom(k,2)` on their number;
3. computes movement/refill controller-edge--label traces;
4. verifies that every one-sided trace degree is at most the line count;
5. verifies paired-domain loss at most twice the line count; and
6. checks that the supplied fixed margin still supports the allocation threshold.

Candidate multiplicities are deliberately absent from the schema: the regression
checks the simple-domain fact that repeating candidate incidences on one line does
not delete additional controller values.  This finite computation illustrates
PP3bbh--PP3bbn; it is not an asymptotic proof.
