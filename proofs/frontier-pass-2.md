# Sparse-algebraic-spread frontier pass 2

This addendum records the mixed-orientation legality results proved after the current branch theorem index. It does not change the status of SAS6 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SAS5hi--SAS5hm | Creator/opposite-destroyer orientations form finite menus with canonical base/cross failure reasons; if each square has `m` legal alternatives, candidate atom support at most `r` and atom incidence at most `Lambda`, a compatible oriented subbatch retains weight at least `mW/[m+r(Lambda-1)]` | PROVED UNDER THE ADDITIVE-EXECUTION AND CONSTRAINT-ATOM CONTRACTS | `docs/sparse-orientation-legality-batching.md` |
| SAS5hn--SAS5hr | Weighted atom loads give a second legality route: either one exact physical constraint atom has load above `tau`, or a compatible oriented batch has weight at least `sum_Q m w_Q^2/(m w_Q+r tau)` | PROVED UNDER THE ADDITIVE-EXECUTION AND EXACT-CONSTRAINT-ATOM CONTRACTS | `docs/sparse-weighted-constraint-load-batching.md` |
| SAS5hs--SAS5hw | Candidates sharing one heavy exact atom form a common-atom fan; either a residual atom is also heavy, or after counting the common atom once a residual-independent fan has weight at least `sum_Q m_Q w_Q^2/(m_Q w_Q+r_circ tau)` | PROVED UNDER THE SHARED-ATOM AND COMMON-ATOM EXECUTION CONTRACTS | `docs/sparse-heavy-common-atom-fan.md` |

## Updated frontier

Mixed-orientation legality now has a complete three-level quantitative route:

1. bounded cardinality incidence `Lambda` gives a compatible batch;
2. bounded weighted atom load `tau` gives a compatible batch;
3. a heavy exact atom is reduced to a one-time common debit, a second heavy atom, or a compatible residual-independent fan.

Remaining SAS6 work is payment or exclusion of exact one-atom capacity overloads and two-atom heavy obstructions, verification of common-atom execution for each arithmetic word family, global barrier and neutral outputs, boundary profiles and exact balanced standard-grid compression.

No statement here proves SAS6 or the no-three-in-line conjecture.