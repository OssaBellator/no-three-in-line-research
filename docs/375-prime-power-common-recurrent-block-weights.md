# Common positive weights for recurrent blocks

A row may be strict under one positive child-weight vector without extending to a common
Lyapunov vector for a recurrent block. This chapter imposes one shared state-weight
registry on a collection of witness-bound row certificates and separates common-weight
consistency, graph closure, strong connectivity and strictness.

## Theorem CMR2174 — PROVED AS AN INTERFACE

All embedded row sources are merged into one exact state registry. If the same state ID
appears in two rows, its role, stratum and owner must agree exactly.

Every state appearing in the shared row sources receives one positive integer global
weight. The weight records are canonically ordered and normalized by

\[
\boxed{\gcd\{w_s:s\in S\}=1.}
\]

## Theorem CMR2175 — PROVED

For a row with parent state `p` and child set `C`, common-weight consistency requires

\[
\boxed{W_p=w_p,\qquad w^{\mathrm{row}}_c=w_c\quad(c\in C).}
\]

Here `W_p` is the row's parent budget and `w^row` is the exact child-weight vector used by
the labelled row-margin certificate. No row may rescale, reorder or replace the common
weights locally.

## Theorem CMR2176 — PROVED

Each declared recurrent-block state must be recurrent and must occur as the parent of
exactly one supplied row. Duplicate parent rows and missing block-parent rows are
rejected. Thus row coverage is exact relative to the declared block state list.

## Theorem CMR2177 — PROVED

For one row, a support edge `p -> c` is present when some response has a positive child
coefficient in coordinate `c`.

The checker partitions these edges into recurrent edges internal to the declared block,
recurrent exits to states outside the block, and nonrecurrent exits to offdiagonal,
auxiliary or sink states. The support graph is reconstructed from the complete
response-vector table, not from a selected response only.

## Theorem CMR2178 — PROVED

The declared block is **closed** exactly when it has no recurrent exits. Its internal
recurrent support graph is tested for strong connectivity by exact forward and reverse
reachability.

A singleton state is strongly connected by the length-zero path convention, but it is
not closed when it has a positive recurrent edge to an external state.

## Theorem CMR2179 — PROVED

Every embedded row retains its exact maximum margin

\[
\mu_p=w_p-
\min_Q\left(a_p+\sum_cw_cv_{p,c}(Q)-\sum_cw_cr_{p,c}(Q)\right).
\]

The common-weight certificate publishes the minimum and total margins and the exact
strict/critical/excess row partition.

## Theorem CMR2180 — PROVED

A collection is recognized as a **complete strict SCC certificate** exactly when

\[
\boxed{
\text{strongly connected}\land\text{closed}\land\min_p\mu_p>0.
}
\]

Common weights alone do not imply closure; closure alone does not imply strictness; and
rowwise strictness under unrelated weights does not imply a common SCC certificate.

## Corollary CMR2181 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_common_recurrent_block_weights.py` validates shared state
records, primitive integer weights, exact row restrictions, recurrent support edges,
closure, strong connectivity and strict margins. It includes deterministic strict
open-block regressions, three exact graph regressions and twelve corruption tests.

The publication environment syntax-compiled the checker. A genuine complete strict SCC
still requires the actual closed row population; the synthetic suite is not such a
population.
