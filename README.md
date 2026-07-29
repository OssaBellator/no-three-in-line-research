# Superregular Resampling Research Track

**Branch:** `research/superregular-resampling`

This branch studies exact resampling for one or two perfect-matching layers in dense and superregular bipartite hosts. Branch proofs are stored in `docs/`, and finite state-space checks are stored in `scripts/`.

> **Status:** Exact stationary resampling is proved for complete hosts and several dense or sparse-hole models, together with deterministic locality and uniform fixed-rank spread. SRR2c--SRR2e give the exact post-resampling cylinder law: every remote-cylinder bias is precisely the average reverse flaw-entry column load of the feasible switching flow. SRR2f--SRR2i turn flow design into exact finite optimization, and SRR2j--SRR2r identify exact endpoint-cost Hall deficiencies and their conditioning drift. SRR2s--SRR2u show that left-hole degree at most `Delta` gives a `Delta`-shifted endpoint-quantile bound. SRR2v--SRR2x now show that deleting a compatible conditioned endpoint set of rank `k` preserves the same bound on the surviving graph and costs only an additive `k` positions in the original quantile order. The central open step is to prove Hall survival and useful `Delta+k` endpoint abundance for actual bounded-cycle switching graphs in arbitrary superregular hosts.

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
- [`docs/superregular-conditioned-shifted-quantiles.md`](docs/superregular-conditioned-shifted-quantiles.md): bounded-rank conditioning adds only an endpoint-order shift.
- [`docs/superregular-first-moment-endpoint.md`](docs/superregular-first-moment-endpoint.md): direct conflict-free endpoint from the dense-host cylinder bound.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.
- [`proofs/frontier-pass-conditioned-quantiles.md`](proofs/frontier-pass-conditioned-quantiles.md): conditioned-quantile frontier ledger.

## Highest-value frontier

1. Prove Hall survival after actual bounded remote assignments and a uniform left-hole or threshold-intersection bound for the resulting switching graph.
2. Evaluate the `Delta+k` shifted endpoint quantiles for the actual rank-two/rank-three event inventories.
3. Extend the flow design to two-layer and multistep resampling while retaining deterministic locality.
4. Upgrade the first-moment endpoint to local conflict families whose global mass is large but whose dependency neighbourhoods are sparse.

## Checks

The branch verification programs are in `scripts/`. They are finite checks, not arbitrary-size proofs.
