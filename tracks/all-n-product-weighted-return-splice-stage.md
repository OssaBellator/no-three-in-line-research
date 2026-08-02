# All-n product track: weighted return and splice stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`all-n-product-buffer-terminal-stage.md`](all-n-product-buffer-terminal-stage.md).
PX356--PX396 retain the full destruction multiplicity of nonimproving buffer
banks, compress blocker supports onto compatible endpoint blocks, cap the
path/mixed/generic sectors by incidence geometry, force rank-one returns into
large clean stars, and splice the bounded terminal return into the abstract
causal repair tree.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Weighted terminal cover | **EXACT** | PX356--PX357 scale the one-/two-variable blocker alternatives by the full parent destruction `D`. |
| Fixed-support return | **COMPRESSED** | PX371--PX375 assign the whole blocker family to one selected-point cover and one heavy layer/channel block. |
| Suppression under thinning | **CLOSED** | PX377--PX380 retain a constant fraction of assigned destruction unless one endpoint is already heavy. |
| Directed-path recurrence | **CAPPED** | PX364--PX366 give `O(n^(4/3))` total incidence and require `D=O(n^(1/3))`. |
| Mixed-shadow recurrence | **NONRECURRENT** | PX367--PX369 give at most `2n^2` blockers and exclude a second mixed return after the first linear-weight child. |
| Generic rank-one recurrence | **CAPPED** | PX381--PX385 give `O(K^2n^(8/3))` outside a loaded line and exclude it after a mixed return for `K=n^o(1)`. |
| Coordinate rank-one recurrence | **STAR/LINE** | PX370 and PX386 turn repeated support into a loaded line and average nondegenerate support into a clean star of order `D/(48K)`. |
| Two-variable rank-one return | **STAR** | PX387 forces clean-star order `D/(32K)`. |
| Actual asymptotic terminal branch | **RETURNS TO LARGE BLOCK** | PX389--PX392 give bounded causal return depth under subpower channel and line-occupancy hypotheses. |
| Large-block/terminal splice | **FORMALIZED** | PX393--PX395 prove conditional finite termination of the combined causal tree. |
| Original induction entry | **OPEN** | The exact source statement referred to as PX63 was not accessible through the connector; its entry hypotheses and invariant preservation must be checked directly. |
| Finite below-threshold orders | **OPEN** | Orders below the explicit buffer/divisor bounds still require exhaustive or symbolic verification. |
| Exact infinite closure | **OPEN** | No all-side product construction theorem follows yet. |

## 1. Weighted return hierarchy

If a terminal bank destroys `D` designated certificates and is nonimproving,
then one exact type carries at least

\[
\frac{Dn}{48}
\]

one-variable blockers or

\[
\frac{Dn^2}{32}
\]

two-variable blockers.

Every blocker has one or two fixed selected points.  A maximal disjoint-support
family gives a selected-point cover; one layer/channel type receives at least
`1/(2q_ch)` of the total assigned blocker weight.  Bernoulli thinning retains
at least `pW/4` of this suppression with probability at least `9/17`, unless
one endpoint already has weight above `pW/16`.

Thus each return produces either:

1. a large compatible endpoint block with explicit parent suppression credit;
2. a high-weight one-point buffer child;
3. a clean star or loaded line from rank-one averaging/incidence; or
4. an incidence sector whose total mass is too small to support the current
   destruction `D`.

## 2. Bounded actual terminal return

Under

\[
q_{\rm ch}=n^{o(1)},
\qquad
K=n^{o(1)},
\]

one-variable high-point returns amplify as

\[
D_j\ge
\left(\frac{n}{384q_{\rm ch}}\right)^{1-2^{-j}}.
\]

After two returns, `D=n^(3/4-o(1))`.  Directed paths are then excluded by
PX366, and coordinate rank one gives a clean star of the same scale by PX386.
A two-variable return creates `D_1>=Dn/64`; its next return cannot be mixed or
directed path and rank one gives a clean star of order `n^(1-o(1))`.

Hence every asymptotic actual order-one/two terminal core returns after bounded
causal depth to the large-block clean-star, endpoint-block, or loaded-line
interfaces.

## 3. Integration boundary

PX395 proves conditional repair termination once five interfaces are checked:

1. every induction obstruction enters a large-block, actual terminal, or finite
   base state;
2. large blocks satisfy PX334--PX335;
3. actual terminals satisfy PX391;
4. finite base states are absorbed or impossible;
5. every move preserves ancestor safety and the product invariants.

The unresolved theorem is therefore no longer a local geometric decoder.  It
is the exact verification that the original product induction supplies these
interfaces for every side length.

## Immediate frontier

1. **Locate and audit the PX63 entry statement.** Confirm its precise branch,
   hypotheses, and invariant list before editing it.
2. **Finite base-order census.** Enumerate every order below
   `4Delta+10+8 d(n)` and record explicit absorbers or obstruction certificates.
3. **Invariant-preservation table.** Check row/column saturation, layer
   disjointness, channel/factor protection, and historical-position constraints
   for each large-block and buffer-return move.
4. **Unified potential implementation.** Instantiate the PX394 vector using the
   exact coordinates already present in the product induction.
5. **Closure conversion.** Only after the preceding checks, state the final
   all-side induction theorem or identify the surviving finite obstruction.

## Verification

```bash
python scripts/verify_product_weighted_buffer_return.py
python scripts/verify_product_buffer_return_sector_caps.py
python scripts/verify_product_fixed_support_cover.py
python scripts/verify_product_weighted_suppression_thinning.py
python scripts/verify_product_generic_rank_one_cap.py
python scripts/verify_product_rank_one_return_star.py
python scripts/verify_product_splice_interface.py
```

All seven verifiers pass locally.  Exact infinite product closure and the
classical no-three-in-line conjecture remain open.