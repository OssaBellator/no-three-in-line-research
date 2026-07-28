# Bounded-denominator frontier pass 2

This compact addendum records the cycle-local restoration results proved after the current branch theorem index. It does not change the status of BDA6 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| BDA5bl--BDA5bp | Every nonconstant simple same-denominator profile cycle has a canonical least-field leave/restore excursion; monotone fields forbid recurrence, while exact restoration edges admit payment, descent, impossibility, outer-reset or capacity-one ticket routing | PROVED UNDER THE COMPLETE-PROFILE AND RESTORATION-TICKET CONTRACTS | `docs/bounded-denominator-least-field-restoration-gates.md` |
| BDA5bq--BDA5bu | A recurrent bounded-jump floor coordinate has a canonical minimum-floor restoration edge; that edge is a negative wall crossing with overshoot at most `B-1`, has a finite address stock under the finite numerator-range contract, and routes to payment, descent, impossibility, tickets or reset | PROVED UNDER THE COMPLETE-WALL AND FINITE-NUMERATOR-RANGE CONTRACTS | `docs/bounded-denominator-balanced-floor-wall-restoration.md` |
| BDA5bv--BDA5bz | Every unbounded negative floor-restoration jump in a closed word has a canonical positive source edge of comparable size; the source/restoration dyadic scales differ by at most `ceil(log_2(P-1))` | PROVED UNDER THE COMPLETE CLOSED-WORD AND EDGE-ADDRESS CONTRACTS | `docs/bounded-denominator-large-jump-compensation.md` |
| BDA5ca--BDA5ce | If decorated positive sources have finite nonreplenishing numerator-mass capacities and word length is at most `L`, the number of restorations of size at least `J_0` is at most `floor((L-1)C_tot/J_0)`; failure is a replenishment or dictionary reset | PROVED UNDER THE COMPLETE SOURCE-MASS BANK CONTRACT | `docs/bounded-denominator-source-mass-bank.md` |
| BDA5cf--BDA5cj | Paid replenishment extends the source bank: cumulative restoration cost is at most initial mass plus exact deposits, giving thresholded and dyadic restoration bounds; free replenishment is returned as the remaining obstruction | PROVED UNDER THE PAID-DEPOSIT AND COMPLETE SOURCE-LINEAGE CONTRACTS | `docs/bounded-denominator-paid-replenishment-bank.md` |

## Updated frontier

The recurrent non-scalar cycle is localized by cycle-space chords, least-field restoration gates and exact balanced-floor wall/source pairs. Bounded initial source mass and externally paid replenishment now pay even unbounded jump magnitudes. Remaining BDA6 work is arithmetic payment or impossibility of the selected exact pairs in rank-two/rank-three and unresolved ordinary-role profiles, plus genuinely free or cyclically self-replenishing sources, unbounded word length or changing edge/source dictionaries.

No statement here proves BDA6 or the no-three-in-line conjecture.