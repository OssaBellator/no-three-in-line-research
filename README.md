# Geometric Cleaning Research Track

**Branch:** `research/geometric-cleaning`

This branch develops the scale-sensitive cleaning route from local candidate banks to a clean-host endpoint. It is an independent research branch: branch-specific proofs live in `docs/`, executable finite checks live in `scripts/`, and `proofs/theorem-index.md` records exactly what is proved here.

> **Status:** The global no-three-in-line conjecture is not proved on this branch. The completed chain now includes exact partner and pair-shadow budgets, high-load peeling, Hall-deficiency localization, destruction-faithful source transfer, created-collateral lineage chargeback, compatible current-star product neutralization, donor-reservoir routing, and finite feedback dictionaries. GC4m--GC4p close the original same-token accounting gap under bounded noncommon-factor reuse: the shared token is counted once, all additional destroyed factors are union-paid, and failure is an exact noncommon demand/capacity overload. The remaining work is payment or neutralization of the resulting capacity overloads, bounded small reservoirs, recurrent untagged feedback, context/global causes, and clean-height preservation through the final transitions.

## Branch map

- [`docs/geometric-cleaning.md`](docs/geometric-cleaning.md): dependency chain and completion criterion.
- [`docs/geometric-cleaning-budget-and-wall.md`](docs/geometric-cleaning-budget-and-wall.md): protected-wall obstruction and exact partner budget.
- [`docs/geometric-cleaning-load-accounting.md`](docs/geometric-cleaning-load-accounting.md): blocker, latent-shadow, and exceptional-anchor accounting.
- [`docs/geometric-cleaning-conflict-peeling.md`](docs/geometric-cleaning-conflict-peeling.md): exact high-load peeling.
- [`docs/geometric-cleaning-anchor-link.md`](docs/geometric-cleaning-anchor-link.md): anchor-link, recursion, Hall, and labelled-fan lemmas.
- [`docs/geometric-cleaning-weighted-labelled-fan.md`](docs/geometric-cleaning-weighted-labelled-fan.md): weighted refinement of the deficient same-token fan.
- [`docs/geometric-cleaning-same-token-union-payment.md`](docs/geometric-cleaning-same-token-union-payment.md): union-safe payment of compatible same-token fans and exact overload return.
- [`docs/geometric-cleaning-shared-source-capacity.md`](docs/geometric-cleaning-shared-source-capacity.md): aggregate private and target-common source capacities.
- [`docs/geometric-cleaning-created-collateral-lineage-chargeback.md`](docs/geometric-cleaning-created-collateral-lineage-chargeback.md): occurrence-faithful lineage payment.
- [`docs/geometric-cleaning-compatible-star-product-neutralization.md`](docs/geometric-cleaning-compatible-star-product-neutralization.md): product neutralization of paid current stars.
- [`docs/geometric-cleaning-donor-reservoir-cause-router.md`](docs/geometric-cleaning-donor-reservoir-cause-router.md): explicit donor-reservoir cause budgets.
- [`docs/geometric-cleaning-donor-blocker-concentration.md`](docs/geometric-cleaning-donor-blocker-concentration.md): capacity-weighted least-blocker concentration.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): theorem status ledger.

## Current frontier

1. Route the GC4o noncommon-underweight fan and target-common/global blocker overloads into executable current payment, created-collateral descent, or a bounded-denominator/alternating-core delegation.
2. Resolve bounded-budget small donor reservoirs and failed incidence-cap alternatives without discarding their concentrated blocker or column witnesses.
3. Close repeated non-tagged feedback cycles, block-tuple overload recursion, unbounded context dictionaries, isolated prospective stars, and global-context causes.
4. Verify that every selected transition preserves the active dyadic clean-height invariant and then assemble the GC5 clean-host endpoint.

## Checks

```bash
python scripts/verify_conflict_peeling.py
python scripts/verify_gc_anchor_link.py
python scripts/verify_gc_weighted_labelled_fan.py
python scripts/verify_gc_same_token_union_payment.py
```

The scripts are finite sanity checks; the Markdown proofs carry the arbitrary-size claims.
