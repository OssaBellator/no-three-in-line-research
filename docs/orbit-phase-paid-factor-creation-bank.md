# OP paid factor-creation bank

The prime-support height theorem charges every first-seen prime to a source factor. This note allows the multiplicative height budget itself to grow, provided every growth is an exact paid deposit.

## Setup

Retain a multiplicative height account

`H = H_0 product_e d_e`,

where `H_0 >= 1` is initial source height and every deposit factor `d_e >= 1` is attached to one exact physical source operation. Let `S` be the current prime support and let `P(S)` be the product of its distinct primes.

For a proposed factor `f`, its novel part is the product of primes dividing `f` but not already in `S`. Old-support factors have novel part one and are handled by the existing valuation/unit routers.

## OP4bh — multiplicative payment invariant

Every accepted novel factor satisfies

`P(S_new) <= H`.

Equivalently, the product of all distinct first-introduction primes is bounded by initial height times recorded deposit factors.

## OP4bi — support-count bound

The number of distinct retained scale primes is at most

`floor(log_2 H)`.

Thus paid factor creation can enlarge the finite valuation dimension only logarithmically in the complete height account.

## OP4bj — exact unpaid-factor return

If the novel part would make `P(S)` exceed `H`, the branch returns the exact unpaid factor-creation witness: the source operation, factor and novel prime set. It is not folded into a generic dynamic-support reset.

## OP4bk — old-support closure

A factor with no novel prime changes only the existing valuation vector and unit class. It therefore routes immediately to valuation drift, finite unit order, holonomy and the bounded physical quotient.

## OP4bl — combined dynamic-support router

Repeated factor creation yields one of:

- finitely many paid novel-prime introductions;
- an exact unpaid factor-creation witness;
- old-support valuation/unit evolution;
- a changed source/deposit dictionary or omitted factor lineage reset.

The theorem does not prove that every physical factor source supplies the required deposit or that all legality data factor through the retained valuation/unit state.

No statement here proves OP5 or the no-three-in-line conjecture.