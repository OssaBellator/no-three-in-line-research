# Geometric-cleaning frontier pass 2

This addendum records the bounded small-reservoir results proved after the current branch theorem index. It does not change the status of GC5 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| GC2gj--GC2gn | A donor reservoir of size at most `D` over `K` exact physical donor addresses has `Q sum_{i<=D} binom(K,i)` complete states; recurrent donor churn exposes one canonical membership-restoration gate and closes by monotone depletion, payment, source debit, capacity-one tickets, impossibility or reset | PROVED UNDER THE COMPLETE-LINEAGE AND RESTORATION CONTRACTS | `docs/geometric-cleaning-bounded-small-reservoir-quotient.md` |
| GC2go--GC2gs | A failed canonical maximum donor matching produces one alternating Hall core `(X,Y)` with `N(X)=Y` and exact deficit equal to the unmatched-target count; all unmatched weight is retained and one exact blocker/cause class carries at least a `1/L_cause` share | PROVED UNDER THE EXACT-DONOR-GRAPH CONTRACT | `docs/geometric-cleaning-weighted-alternating-hall-core.md` |
| GC2gt--GC2gx | Every non-global Hall core exposes the complete missing rectangle `X x (A\Y)`; its weighted incidence is partitioned into exact causes and either concentrates on one cause or spreads across many distinct causes | PROVED UNDER THE COMPLETE-MISSING-CAUSE CONTRACT | `docs/geometric-cleaning-hall-core-missing-rectangle.md` |
| GC2gy--GC2hc | Exact cause capacities either pay the complete missing rectangle or return one overloaded cause; across a nonreplenishing epoch cumulative paid failure mass is at most the total cause capacity | PROVED UNDER THE COMPLETE NONREPLENISHING CAUSE-BANK CONTRACT | `docs/geometric-cleaning-cause-capacity-bank.md` |
| GC2hd--GC2hh | The pure global Hall-shortage case has signed potential `|T|-|A|`; target removal and donor addition decrease it, while every closed count cycle requires equal paid target-recreation/donor-destruction mass | PROVED UNDER THE NONREPLENISHING ADVERSE-BANK AND COMPLETE COUNT-LINEAGE CONTRACTS | `docs/geometric-cleaning-global-shortage-bank.md` |
| GC2hi--GC2hm | Target recreation and donor destruction generated through a finite ranked acyclic dependency graph have cumulative adverse throughput at most `R(C_0+D_0)`; a backward dependency returns one exact directed source cycle | PROVED UNDER THE RANKED ADVERSE-SOURCE AND PREDECESSOR-LINEAGE CONTRACTS | `docs/geometric-cleaning-ranked-adverse-source-dependency.md` |
| GC2hn--GC2hr | One-for-one occurrence-faithful transitions conserve adverse-token mass inside every SCC; each token crosses at most `R-1` condensation boundaries, while splitting or source-less creation returns an exact adverse-amplification obstruction | PROVED UNDER THE CONSERVATIVE SCC ADVERSE-LINEAGE CONTRACT | `docs/geometric-cleaning-scc-adverse-conservation.md` |
| GC2hs--GC2hw | Exact cause demands and finite compatible remedy capacities form an integral transportation problem; full cause payment is equivalent to capacitated Hall inequalities, and failure returns one canonical deficient cause/remedy cut | PROVED UNDER THE COMPLETE CAUSE/REMEDY COMPATIBILITY CONTRACT | `docs/geometric-cleaning-cause-remedy-transport.md` |

## Updated frontier

The branch now has an exact reservoir quotient, Hall-core/missing-rectangle causes, finite cause and adverse-source accounts, and a complete physical cause-to-remedy transportation criterion. Remaining GC5 work is proving the concrete remedy graph and capacities, nonamplification for actual adverse cycles, clean-height preservation, untagged feedback and local resampling.

No statement here proves GC5 or the no-three-in-line conjecture.