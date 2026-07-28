# Sparse-algebraic-spread frontier pass 2

This addendum records the mixed-orientation legality results proved after the current branch theorem index. It does not change the status of SAS6 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| SAS5hi--SAS5hm | Creator/opposite-destroyer orientations form finite menus with canonical base/cross failure reasons; if each square has `m` legal alternatives, candidate atom support at most `r` and atom incidence at most `Lambda`, a compatible oriented subbatch retains weight at least `mW/[m+r(Lambda-1)]` | PROVED UNDER THE ADDITIVE-EXECUTION AND CONSTRAINT-ATOM CONTRACTS | `docs/sparse-orientation-legality-batching.md` |
| SAS5hn--SAS5hr | Weighted atom loads give a second legality route: either one exact physical constraint atom has load above `tau`, or a compatible oriented batch has weight at least `sum_Q m w_Q^2/(m w_Q+r tau)` | PROVED UNDER THE ADDITIVE-EXECUTION AND EXACT-CONSTRAINT-ATOM CONTRACTS | `docs/sparse-weighted-constraint-load-batching.md` |
| SAS5hs--SAS5hw | A heavy common atom is either a nonshareable capacity overload, extends to a second heavy residual atom, or yields a compatible common-atom fan with an explicit weighted bound | PROVED UNDER THE SHARED-ATOM EXECUTION CONTRACT | `docs/sparse-heavy-common-atom-fan.md` |
| SAS5hx--SAS5ib | Heavy residual atoms may be iterated into a nested common core of depth at most `r`; the process ends in a bounded exact nonshareable core or a residual-independent fan satisfying the weighted local-minimum bound | PROVED UNDER THE SHARED-CORE EXECUTION CONTRACT | `docs/sparse-iterated-heavy-atom-core.md` |
| SAS5ic--SAS5ig | A shareable exact heavy core has a finite capacity bank: every execution debits every core atom, so total execution weight is at most the least initial-plus-replenished core capacity; failure returns one least exhausted atom or a shareability reset | PROVED UNDER THE COMPLETE CORE-LINEAGE AND CAPACITY CONTRACTS | `docs/sparse-exact-core-capacity-bank.md` |
| SAS5ih--SAS5il | An additive compatible fan with total output at least `gamma` times its weight concentrates at least a `gamma/L` share on one exact barrier/neutral ledger; finite capacities pay the fan or return one least overloaded output ledger | PROVED UNDER THE COMPLETE ADDITIVE OUTPUT-LEDGER CONTRACT | `docs/sparse-fan-output-ledger-concentration.md` |
| SAS5im--SAS5iq | Nonnegative additive fan output separates at any fixed threshold into a concentrated terminal-barrier ledger or a concentrated neutral ledger; neutral capacity pays the branch or returns one exact overload | PROVED UNDER THE COMPLETE BARRIER/NEUTRAL LEDGER CLASSIFICATION CONTRACT | `docs/sparse-barrier-neutral-ledger-separation.md` |
| SAS5ir--SAS5iv | Nonnegative bounded boundary profiles aggregate into at most `(B+1)^d` signatures; nonzero total output yields one heavy exact boundary coordinate, while zero total profile means every used ledger is boundary-neutral | PROVED UNDER THE COMPLETE NONNEGATIVE BOUNDARY-PROFILE CONTRACT | `docs/sparse-boundary-profile-quotient.md` |
| SAS5iw--SAS5ja | Signed bounded boundary profiles have exact coordinate cancellation `C=(V-||Z||_1)/2`; either one signed coordinate is heavy or a quantified fraction of variation pairs neutrally | PROVED UNDER THE COMPLETE SIGNED ADDITIVE BOUNDARY AND LEGAL-PAIRING CONTRACTS | `docs/sparse-signed-boundary-cancellation.md` |
| SAS5jb--SAS5jf | For each boundary coordinate, maximum legal opposite-sign cancellation is an exact bipartite matching; residual variation is unavoidable net boundary plus twice the sign-pair Hall deficiency | PROVED UNDER THE COMPLETE PHYSICAL SIGN-PAIR GRAPH CONTRACT | `docs/sparse-legal-cancellation-transport.md` |

## Updated frontier

Mixed-orientation legality now has heavy-core, capacity and output-ledger routes. Signed boundary output has both an algebraic cancellation identity and a physical matching criterion, with every extra residual unit localized to a sign-pair Hall cut. Remaining SAS6 work is proving concrete core shareability and output lower bounds, sign-pair Hall inequalities and exact balanced compression.

No statement here proves SAS6 or the no-three-in-line conjecture.
