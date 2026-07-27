# Superregular Resampling Research Track

**Branch:** `research/superregular-resampling`

This branch studies exact resampling for one or two perfect-matching layers in dense and superregular bipartite hosts. Branch proofs are stored in `docs/`, and finite state-space checks are stored in `scripts/`.

> **Status:** Exact stationary resampling is proved for complete hosts and several dense or sparse-hole models, together with deterministic locality and uniform fixed-rank spread. SRR2c--SRR2e now give the exact post-resampling cylinder law: every remote-cylinder bias is precisely the average reverse flaw-entry column load of the feasible switching flow. The central open step is therefore to construct a bounded-cycle fractional Hall flow whose reverse column loads are nearly balanced on all relevant remote partial-matching cylinders in arbitrary superregular hosts; spread alone does not supply it.

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
- [`docs/superregular-first-moment-endpoint.md`](docs/superregular-first-moment-endpoint.md): direct conflict-free endpoint from the dense-host cylinder bound.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): branch theorem ledger.

## Highest-value frontier

1. Construct a feasible bounded-cycle switching flow whose reverse column load is nearly constant on every relevant remote partial-matching cylinder.
2. Control the loss of forward switches caused by a bounded remote partial matching in a way that implies the SRR2d average column-load bound, rather than a crude global hole count.
3. Upgrade the first-moment endpoint to local conflict families whose global mass is too large but whose dependency neighbourhoods are sparse.

## Checks

The branch verification programs are in `scripts/`. They are finite checks, not arbitrary-size proofs.
