# Sparse-algebraic-spread frontier pass 2

This addendum records the mixed-orientation legality results proved after the current branch theorem index. It does not change the status of SAS6 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SAS5hi--SAS5hm | Creator/opposite-destroyer orientations form finite menus with canonical base/cross failure reasons; if each square has `m` legal alternatives, candidate atom support at most `r` and atom incidence at most `Lambda`, a compatible oriented subbatch retains weight at least `mW/[m+r(Lambda-1)]` | PROVED UNDER THE ADDITIVE-EXECUTION AND CONSTRAINT-ATOM CONTRACTS | `docs/sparse-orientation-legality-batching.md` |
| SAS5hn--SAS5hr | Weighted atom loads give a second legality route: either one exact physical constraint atom has load above `tau`, or a compatible oriented batch has weight at least `sum_Q m w_Q^2/(m w_Q+r tau)` | PROVED UNDER THE ADDITIVE-EXECUTION AND EXACT-CONSTRAINT-ATOM CONTRACTS | `docs/sparse-weighted-constraint-load-batching.md` |
| SAS5hs--SAS5hw | A heavy common atom is either a nonshareable capacity overload, extends to a second heavy residual atom, or yields a compatible common-atom fan with an explicit weighted bound | PROVED UNDER THE SHARED-ATOM EXECUTION CONTRACT | `docs/sparse-heavy-common-atom-fan.md` |
| SAS5hx--SAS5ib | Heavy residual atoms may be iterated into a nested common core of depth at most `r`; the process ends in a bounded exact nonshareable core or a residual-independent fan satisfying the weighted local-minimum bound | PROVED UNDER THE SHARED-CORE EXECUTION CONTRACT | `docs/sparse-iterated-heavy-atom-core.md` |
| SAS5ic--SAS5ig | A shareable exact heavy core has a finite capacity bank: every execution debits every core atom, so total execution weight is at most the least initial-plus-replenished core capacity; failure returns one least exhausted atom or a shareability reset | PROVED UNDER THE COMPLETE CORE-LINEAGE AND CAPACITY CONTRACTS | `docs/sparse-exact-core-capacity-bank.md` |

## Updated frontier

Mixed-orientation legality now has cardinality, weighted-load, one-heavy-atom, iterated heavy-core and exact core-capacity routes. Repeated concentration cannot continue beyond support rank `r`, and a shareable terminal core executes only up to its least capacity. Remaining SAS6 work is arithmetic proof of shareability/payment for the finite exact core, connection of compatible fan margin to global barrier and neutral ledgers, boundary profiles and exact balanced compression.

No statement here proves SAS6 or the no-three-in-line conjecture.