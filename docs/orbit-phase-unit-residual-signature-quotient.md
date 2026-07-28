# OP unit-sensitive residual signature quotient

This note compresses the zero-drift residual transportation problem while retaining the finite unit field. It does not prove OP5 or the no-three-in-line conjecture.

## Complete residual state

After valuation drift, unit clocks, and holonomy have returned, every exact physical residual state `x` carries:

- a retained unit class `u(x)` in a finite set `U`;
- a nonnegative integer demand `d_x`; and
- a complete compatible source neighbourhood `N(x)`.

## Unit-sensitive signature

Define

`sig(x) = (u(x), N(x))`.

Aggregate demands within each signature. If there are `S` source classes, the quotient has at most

`|U| 2^S`

states.

## Exact transport preservation

The signature quotient preserves:

1. maximum integral residual payment;
2. total unpaid residual mass;
3. every maximum capacitated Hall deficit;
4. the existence of a full payment.

The proof is the same exact flow aggregation used for terminal RI profiles: all members of a signature class have identical outgoing payment arcs and the same retained unit-sensitive legality.

## Why the unit field is necessary

Two residuals with the same unlabelled source neighbourhood but different unit classes may have different legal physical continuations. Merging them after forgetting `u(x)` is therefore not licensed.

Whenever one neighbourhood occurs in more than one retained unit class, omission of the unit field returns a unit-sensitive reset rather than a smaller quotient.

## Routing

A full quotient flow pays the complete zero-drift residual state. Failure returns a least deficient unit-signature/source cut. A changed source dictionary, unit class, physical owner, blocker fibre, or action kernel is an explicit reset.

## Outside the contract

The quotient does not cover infinite unit groups, dynamic source dictionaries, nonintegral hidden capacities, or genuinely wide interactions whose legality is not determined by the retained unit signature and pairwise source arcs.
