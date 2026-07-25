# Cycle-free terminal cores force trajectory saturation

PX287 shows that every diagonal-forbidden block with `m>Delta` has an allowed
principal cycle trade. The only genuinely cycle-free terminal blocks therefore
satisfy `m<=Delta`. Their structure is exact: the allowed digraph is acyclic
and consequently has a sink and a source, giving one completely forbidden row
and one completely forbidden column.

When the forbidden graph is the union of a bounded base graph and historical
position matchings, a completely forbidden row certifies that one endpoint has
visited almost every column during the ancestor chain.

## 1. Full forbidden boundary vertices

Use the loopless allowed digraph `A_F` from PX287.

### Theorem PX291 -- PROVED

If `A_F` has no directed cycle, then there are labels `u,v` such that

\[
\boxed{\{v\}\times[m]\subseteq F}
\]

and

\[
\boxed{[m]\times\{u\}\subseteq F.}
\]

Thus one row and one column are completely forbidden. In particular

\[
\boxed{m\le\Delta.}
\]

### Proof

A finite directed graph without a directed cycle is acyclic and has a sink and
a source. A sink `v` has no allowed outgoing arc. Since the diagonal is also
forbidden, every cell in row `v` lies in `F`. A source gives the column
statement. The maximum-degree bound implies `m<=Delta`. \(\square\)

This is the exact converse obstruction to the elementary cycle argument of
PX287.

## 2. Historical trajectory saturation

Suppose

\[
F=F_0\cup H_1\cup\cdots\cup H_d,
\]

where `F_0` has maximum row and column degree at most `Delta_0` and every `H_j`
is a partial matching of historical endpoint positions.

### Theorem PX292 -- PROVED

For a fully forbidden row `v`, at least

\[
\boxed{m-\Delta_0}
\]

distinct historical matchings `H_j` contain an edge in row `v`. These edges
occupy distinct columns. Therefore the endpoint in row `v` has visited at
least `m-Delta_0` distinct historical columns.

The symmetric statement holds for a fully forbidden column.

### Proof

The base graph contributes at most `Delta_0` cells to row `v`. The other
`m-Delta_0` forbidden cells must be supplied by historical partial matchings.
Each `H_j` contributes at most one cell in the row, and different cells have
different columns. \(\square\)

Consequently a cycle-free terminal core cannot occur early in the recursion:

\[
\boxed{d\ge m-\Delta_0.}
\]

## 3. Final terminal dichotomy

### Corollary PX293 -- PROVED

Every terminal diagonal-forbidden block has one of two forms.

1. **Cycle-executable:** `m>Delta` or the allowed digraph otherwise contains a
   directed cycle. PX287--PX290 give a principal cycle trade and exact
   subpower optimization.
2. **Trajectory-saturated:** the allowed digraph is acyclic, `m<=Delta`, and
   there is a row endpoint and a column endpoint with at least `m-Delta_0`
   distinct historical positions.

Along the nested chain `Delta<=Delta_0+d`, the second case has

\[
\boxed{m\le\Delta_0+d=O(\log\log N).}
\]

and supplies an explicit trajectory-saturation certificate to the terminal
optimizer PX273--PX276.

### Proof

Combine PX291--PX292 with the degree growth and depth bound of PX265. \(\square\)

The remaining terminal-core frontier is no longer arbitrary: it is the
classification or absorption of trajectory-saturated rows and columns whose
historical positions cover a linear fraction of the terminal label set.

## 4. Verification

Run

```bash
python scripts/verify_product_trajectory_saturated_core.py
```

The verifier exhausts diagonal-forbidden digraphs through order five, confirms
the cycle-or-full-row/full-column dichotomy, and checks the historical matching
count needed to cover a saturated row.
