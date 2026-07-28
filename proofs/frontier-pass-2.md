# Bounded-denominator frontier pass 2

This compact addendum records the cycle-local restoration results proved after the current branch theorem index. It does not change the status of BDA6 or the global conjecture.

| ID | Statement | Status | Location |
|---|---|---|---|
| BDA5bl--BDA5bp | Every nonconstant simple same-denominator profile cycle has a canonical least-field leave/restore excursion; monotone fields forbid recurrence, while exact restoration edges admit payment, descent, impossibility, outer-reset or capacity-one ticket routing | PROVED UNDER THE COMPLETE-PROFILE AND RESTORATION-TICKET CONTRACTS | `docs/bounded-denominator-least-field-restoration-gates.md` |
| BDA5bq--BDA5bu | A recurrent bounded-jump floor coordinate has a canonical minimum-floor restoration edge; that edge is a negative wall crossing with overshoot at most `B-1`, has a finite address stock under the finite numerator-range contract, and routes to payment, descent, impossibility, tickets or reset | PROVED UNDER THE COMPLETE-WALL AND FINITE-NUMERATOR-RANGE CONTRACTS | `docs/bounded-denominator-balanced-floor-wall-restoration.md` |
| BDA5bv--BDA5bz | Every unbounded negative floor-restoration jump in a closed numerator cycle has a canonical positive source edge of size at least the jump divided by `P-1`; the dyadic scale gap is bounded by `ceil(log_2(P-1))`, reducing large-jump recurrence to one exact source/restoration pair | PROVED UNDER THE COMPLETE-EDGE AND BOUNDED-CYCLE-LENGTH CONTRACTS | `docs/bounded-denominator-large-jump-compensation.md` |

## Updated frontier

The recurrent non-scalar cycle is now localized in four complementary ways:

1. BDA5bc--BDA5bf expose one cycle-space chord from a stock of size `E-V+c`;
2. BDA5bl--BDA5bp expose one exact restoration of the least changing physical field;
3. BDA5bq--BDA5bu identify bounded-jump balanced-floor restoration as one downward wall crossing `(field,level,overshoot,jump,edge)`;
4. BDA5bv--BDA5bz pair every unbounded restoration jump with a comparable positive physical source edge.

The remaining BDA6 work is edge-pair specific: pay, descend, ticket or exclude the reachable wall/source classes for rank-two/rank-three and unresolved ordinary-role profiles. Unbounded jump magnitude is no longer by itself an unstructured recurrence regime; genuinely unbounded cycle length, changing physical edge dictionaries and replenishable sources remain outside the contract.

No statement here proves BDA6 or the no-three-in-line conjecture.