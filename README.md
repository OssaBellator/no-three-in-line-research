# Superregular Resampling Research Track

**Branch:** `research/superregular-resampling`

This branch studies exact resampling for one or two perfect-matching layers in dense and superregular bipartite hosts. Branch proofs are stored in `docs/`, and finite state-space checks are stored in `scripts/`.

> **Status:** Exact stationary resampling is proved for complete hosts and several dense or sparse-hole models, together with deterministic locality and uniform fixed-rank spread. SRR2c--SRR2e give the exact post-resampling cylinder law: every remote-cylinder bias is precisely the average reverse flaw-entry column load of the feasible switching flow. SRR2f--SRR2i turn flow design into exact finite optimization, and SRR2j--SRR2r identify exact endpoint-cost Hall deficiencies and their conditioning drift. SRR2s--SRR2u now show that a switching graph with left-hole degree at most `Delta` loses at most `Delta` units of sublevel rank and admits an endpoint flow bounded by the `Delta`-shifted cost quantiles. The central open step is to construct bounded-cycle switching graphs with a uniformly useful left-hole or threshold-intersection bound in arbitrary superregular hosts; spread and Hall feasibility alone do not supply it.

## Branch map

- [`docs/superregular-resampling.md`](docs/superregular-resampling.md): dependency chain and endpoint.
- [`docs/complete-host-resampling-oracle.md`](docs/complete-host-resampling-oracle.md)
- [`docs/complete-two-layer-resampling.md`](docs/complete-two-layer-resampling.md)
- [`docs/deleted-matching-locality.md`](docs/deleted-matching-locality.md)
- [`docs/dense-host-stationary-resampling.md`](docs/dense-host-stationary-resampling.md)
- [`docs/sparse-hole-locality.md`](docs/sparse-hole-locality.md)
- [`docs/two-layer-sparse-hole-locality.md`](docs/two-layer-sparse-hole-locality.md)
- [`docs/superregular-hall-resampling.md`](docs/superregular-hall-resampling.md)
- [`docs/superregular-switching-criterion.md`](docs/superregular-switching-criterion.md)
- [`docs/superregular-reverse-flow-cylinder-law.md`](docs/superregular-reverse-flow-cylinder-law.md): exact reverse-flow identity and cylinder-balance criterion.
- [`docs/superregular-cylinder-flow-minimax.md`](docs/superregular-cylinder-flow-minimax.md): minimax worst-cylinder design and aggregate min-cost event flows.
- [`docs/superregular-endpoint-cost-cuts.md`](docs/superregular-endpoint-cost-cuts.md): exact sublevel-rank and Hall-deficiency cost formula.
- [`docs/superregular-conditioned-endpoint-cost.md`](docs/superregular-conditioned-endpoint-cost.md): conditioning-local cost drift.
- [`docs/superregular-bounded-hole-endpoint-flow.md`](docs/superregular-bounded-hole-endpoint-flow.md): bounded left holes imply shifted-quantile event-flow cost.
- [`docs/superregular-first-moment-endpoint.md`](docs/superregular-first-moment-endpoint.md): direct conflict-free endpoint from the dense-host cylinder bound.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.

## Highest-value frontier

1. Construct a bounded-cycle switching graph with uniformly bounded left-hole degree, or prove the sharper threshold-local intersection bounds needed by SRR2s--SRR2u.
2. Evaluate the shifted endpoint-cost quantiles for the actual rank-two/rank-three event inventories after bounded remote conditioning.
3. Extend the flow design to two-layer and multistep resampling while retaining deterministic locality.
4. Upgrade the first-moment endpoint to local conflict families whose global mass is large but whose dependency neighbourhoods are sparse.

## Checks

The branch verification programs are in `scripts/`. They are finite checks, not arbitrary-size proofs.
