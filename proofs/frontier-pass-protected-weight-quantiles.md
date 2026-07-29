# Geometric-cleaning frontier pass: protected-event weight quantiles

**Branch:** `research/geometric-cleaning`

| ID | Statement | Status | Location |
|---|---|---|---|
| GC4ah | An address with incidence cap `d_p` has exact extremal capacity equal to the sum of its `d_p` largest eligible operation weights | PROVED | `docs/geometric-cleaning-protected-event-weight-quantiles.md` |
| GC4ai | Aggregate protected capacity is bounded by the sum of address-specific top-weight capacities, with a global quantile fallback | PROVED | `docs/geometric-cleaning-protected-event-weight-quantiles.md` |
| GC4aj | Small aggregate top-weight capacity gives clean-height-safe payment or Hall deficiency; failure is an exact incidence or record obstruction | PROVED | `docs/geometric-cleaning-protected-event-weight-quantiles.md` |
| GC4ak | Protected-height work reduces to concrete incidence caps and eligible top-weight sums | PROVED | `docs/geometric-cleaning-protected-event-weight-quantiles.md` |

## Updated GC5 frontier

Uniform maximum operation weight is no longer needed. The protected-height branch now asks for physical address-incidence bounds and control of the largest eligible operation weights, followed by payment of any exact overloaded address.

No statement here proves GC5 or the global conjecture.
