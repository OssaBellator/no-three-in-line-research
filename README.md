# Superregular Resampling Research Track

**Branch:** `research/superregular-resampling`

This branch studies exact resampling for one or two perfect-matching layers in dense and superregular bipartite hosts. Branch proofs are stored in `docs/`, and finite state-space checks are stored in `scripts/`.

> **Status:** Exact stationary resampling is proved for complete hosts and several dense or sparse-hole models, together with deterministic locality and uniform fixed-rank spread. SRR2c--SRR2e give the exact post-resampling cylinder law: every remote-cylinder bias is precisely the average reverse flaw-entry column load of the feasible switching flow. SRR2f--SRR2i now turn flow design into exact finite optimization: worst-cylinder balance is a minimax transportation problem against an adversarial cylinder mixture, while a declared geometric event inventory is one min-cost fractional Hall flow. The central open step is to prove uniformly low transportation cost for bounded-cycle switching graphs in arbitrary superregular hosts; spread and Hall feasibility alone do not supply it.

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
- [`docs/superregular-first-moment-endpoint.md`](docs/superregular-first-moment-endpoint.md): direct conflict-free endpoint from the dense-host cylinder bound.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.

## Highest-value frontier

1. Construct a bounded-cycle switching graph whose Hall-flow polytope has uniformly small adversarial cylinder transportation cost.
2. Bound the min-cost endpoint objective for the actual rank-two/rank-three event inventories after conditioning on a bounded remote partial matching, rather than using a crude global hole count.
3. Extend the flow design to two-layer and multistep resampling while retaining deterministic locality.
4. Upgrade the first-moment endpoint to local conflict families whose global mass is large but whose dependency neighbourhoods are sparse.

## Checks

The branch verification programs are in `scripts/`. They are finite checks, not arbitrary-size proofs.
