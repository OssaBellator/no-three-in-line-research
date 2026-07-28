# Sparse-algebraic-spread frontier pass 2

This addendum records the mixed-orientation legality results proved after the current branch theorem index. It does not change the status of SAS6 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SAS5hi--SAS5hm | Creator/opposite-destroyer orientations form finite menus with canonical base/cross failure reasons; if each square has `m` legal alternatives, candidate atom support at most `r` and atom incidence at most `Lambda`, a compatible oriented subbatch retains weight at least `mW/[m+r(Lambda-1)]` | PROVED UNDER THE ADDITIVE-EXECUTION AND CONSTRAINT-ATOM CONTRACTS | `docs/sparse-orientation-legality-batching.md` |
| SAS5hn--SAS5hr | Weighted atom loads give a second legality route: either one exact physical constraint atom has load above `tau`, or a compatible oriented batch has weight at least `sum_Q m w_Q^2/(m w_Q+r tau)` | PROVED UNDER THE ADDITIVE-EXECUTION AND EXACT-CONSTRAINT-ATOM CONTRACTS | `docs/sparse-weighted-constraint-load-batching.md` |

## Updated frontier

Mixed-orientation legality now has two quantitative routes: a cardinality-incidence bound `Lambda`, or a weighted atom-load cap `tau`. Failure of the weighted route is itself a heavy exact column, endpoint, record, constraint or boundary atom. Remaining SAS6 work is payment of those heavy atoms, global barrier and neutral high-incidence outputs, boundary profiles and exact balanced standard-grid compression.

No statement here proves SAS6 or the no-three-in-line conjecture.
