# Complete-grid extension decoder for Hall choices

`docs/568` identifies the quotient-choice pair `(s,c)` with one of the twelve
ordered distinct pairs of four labels.  This chapter realizes those labels as
actual cells of a complete bipartite choice grid and supplies a matching
extension witness for every decoded pair.

## 1. Explicit grid decoder

Fix the complete bipartite host `K_{4,4}` and two left resources `v=0,w=1`.
For syndrome `s in Z/3Z` and choice `c in Z/4Z`, define

```text
D(s,c)=((v,c),(w,c+s+1 mod 4)).
```

### Theorem PP3cqs -- PROVED / COMPLETE-GRID BIJECTION

The map `D` is a bijection from the twelve quotient-choice pairs to the twelve
compatible ordered cell pairs incident with `v,w`.

#### Proof

The second right endpoint differs from the first by one, two, or three modulo
four, so every decoded pair is compatible.  Conversely, every ordered distinct
pair has a unique nonzero difference and hence a unique syndrome. ∎

## 2. Exact matching extension

### Theorem PP3cqt -- PROVED / TWO-WITNESS RESIDUAL MATCHING

Every decoded pair extends to exactly two perfect matchings of `K_{4,4}`.
After fixing its two cells, the residual host is `K_{2,2}`.

#### Proof

The decoded cells use two left and two distinct right resources.  Deleting those
four endpoints leaves two vertices on each side with every edge present.  The
two bijections between the residual sides are exactly its perfect matchings. ∎

## 3. Microscopic witnesses

### Theorem PP3cqu -- PROVED / ORIENTATION-DOUBLED GRID DECODER

For each decoded quotient-choice pair, the cylinder microcensus of `docs/562`
has one witness in each orientation.  Hence all twelve grid pairs have two
microscopic witnesses per gadget, and each witness carries an explicit perfect
matching extension.

#### Proof

The quotient decoder depends only on syndrome and choice, not orientation.
The two orientation states therefore map to the same cell pair.  Apply
`PP3cqt` to either witness. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_hall_complete_grid_extensions.py
```

The audit checks all twelve decoded pairs, both residual matchings, and all
twenty-four orientation witnesses.

## 5. Prime-patching consequence

The Hall cylinder is now decoded into the complete-grid host type used by the
earlier two-resource choice-grid theory.  The remaining geometric gap is more
specific: identify the four choice labels with actual endpoint cells of one
prime-patching host, rather than with abstract `K_{4,4}` columns.
