# All-n product track: second repair-stage update

**Branch:** `research/all-n-product-construction`

This addendum extends
[`tracks/all-n-product-repair-stage.md`](all-n-product-repair-stage.md).

## New finite theorem

**PX19 — PROVED.** In a successful crossed `3 x 3` factor-product host of side
nine, the complete degree-two repair graph has:

- `6,840` states;
- `1,359,432` unordered single-cycle adjacencies;
- `2` no-three states;
- `6,814` bad states with an improving one-cycle move;
- `24` one-cycle traps, all repairable within two toggles.

The optimal two-step profiles are

\[
20\text{ states with }3\longrightarrow3\longrightarrow0
\]

and

\[
4\text{ states with }3\longrightarrow4\longrightarrow0.
\]

Together with PX18, both successful finite hosts studied exhaustively have
repair radius two and maximum uphill barrier one.

## Updated PC6 boundary

The missing theorem is no longer monotone descent. A viable result must prove a
bounded-uphill batch or resampling rule across many projection fibres. It must
also distinguish feasible hosts from the exact infeasible `2 x 5` and `5 x 2`
families, or enlarge those hosts with offsets or non-global digit maps.

## Verification

```bash
python scripts/verify_product_batch_repair.py
```
