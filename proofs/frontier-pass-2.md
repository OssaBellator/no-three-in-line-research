# Geometric-cleaning frontier pass 2

This addendum records the bounded small-reservoir results proved after the current branch theorem index. It does not change the status of GC5 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| GC2gj--GC2gn | A donor reservoir of size at most `D` over `K` exact physical donor addresses has `Q sum_{i<=D} binom(K,i)` complete states; recurrent donor churn exposes one canonical membership-restoration gate and closes by monotone depletion, payment, source debit, capacity-one tickets, impossibility or reset | PROVED UNDER THE COMPLETE-LINEAGE AND RESTORATION CONTRACTS | `docs/geometric-cleaning-bounded-small-reservoir-quotient.md` |
| GC2go--GC2gs | A failed canonical maximum donor matching produces one alternating Hall core `(X,Y)` with `N(X)=Y` and exact deficit equal to the unmatched-target count; all unmatched weight is retained and one exact blocker/cause class carries at least a `1/L_cause` share | PROVED UNDER THE EXACT-DONOR-GRAPH CONTRACT | `docs/geometric-cleaning-weighted-alternating-hall-core.md` |
| GC2gt--GC2gx | A Hall core is either a pure global donor-count overload or exposes the complete missing rectangle `X x (A\Y)`; its weighted blocked mass concentrates on one exact cause or spreads over at least `|X|(|A|-|Y|)/Gamma` distinct causes | PROVED UNDER THE LEAST-CAUSE CONTRACT | `docs/geometric-cleaning-hall-core-missing-rectangle.md` |

## Updated frontier

The `p<=D_phys` branch now has:

1. an exact finite reservoir quotient;
2. a weighted canonical Hall core when assignment fails;
3. either a pure global donor-count overload or the complete outside-donor missing rectangle;
4. one heavy exact blocker/cause or many distinct exact causes.

Remaining GC5 work is concentrated on payment or neutralization of the returned target-common/global causes, genuinely fresh or unbounded donor dictionaries, untagged feedback lacking occurrence-faithful lineage, block-tuple/global-context recursion, clean-height preservation and local superregular resampling.

No statement here proves GC5 or the no-three-in-line conjecture.