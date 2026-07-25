# Geometric Cleaning Research Track

**Branch:** `research/geometric-cleaning`

This branch develops the scale-sensitive cleaning route from local candidate banks to a clean-host endpoint. It is an independent research branch: the branch-specific proofs live in `docs/`, executable finite checks live in `scripts/`, and `proofs/theorem-index.md` records exactly what is proved here.

> **Status:** The global no-three-in-line conjecture is not proved on this branch. The strongest completed chain is the exact partner-budget accounting, high-load peeling, anchor-link extraction, paid conflict localization, finite-support descent, and Hall-deficiency localization. The remaining geometric step is to convert the resulting same-token structural fan or conflict overload into a paid secant bank, an alternating-core transition, or a bounded-denominator delegation.

## Branch map

- [`docs/geometric-cleaning.md`](docs/geometric-cleaning.md): dependency chain and completion criterion.
- [`docs/geometric-cleaning-budget-and-wall.md`](docs/geometric-cleaning-budget-and-wall.md): protected-wall obstruction and exact partner budget.
- [`docs/geometric-cleaning-load-accounting.md`](docs/geometric-cleaning-load-accounting.md): blocker, latent-shadow, and exceptional-anchor accounting.
- [`docs/geometric-cleaning-conflict-peeling.md`](docs/geometric-cleaning-conflict-peeling.md): exact high-load peeling.
- [`docs/geometric-cleaning-anchor-link.md`](docs/geometric-cleaning-anchor-link.md): anchor-link, recursion, Hall, and labelled-fan lemmas.
- [`docs/geometric-cleaning-weighted-labelled-fan.md`](docs/geometric-cleaning-weighted-labelled-fan.md): weighted refinement of the deficient same-token fan.
- [`proofs/theorem-index.md`](proofs/theorem-index.md): theorem status ledger for this branch.

## Current frontier

1. Convert a broad same-token, same-role compatible fan into current paid secant incidence without counting the shared token repeatedly.
2. Classify the high installation-conflict alternative by anchor, line, carry, denominator, or quotient data.
3. Verify that the resulting transition preserves the active dyadic clean-height invariant.
4. Assemble the clean-host endpoint only after those interfaces are proved.

## Checks

```bash
python scripts/verify_conflict_peeling.py
python scripts/verify_gc_anchor_link.py
python scripts/verify_gc_weighted_labelled_fan.py
```

The scripts are finite sanity checks; the Markdown proofs carry the arbitrary-size claims.
