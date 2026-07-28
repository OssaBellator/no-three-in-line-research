# AC5 Hall-core obstruction bridge

This note composes the reverse-load transportation endpoint with the exact obstruction-capacity bank. It does not prove AC5, AC6, or the no-three-in-line conjecture.

## Setup

Fix one endpoint-cost threshold. Let `L` be the retained restricted-menu states and `R` the threshold-eligible endpoint states. Write `G` for the complete compatibility graph after all retained blockers and conditioning losses have been applied.

Assume every absent incidence `(x,y)` is assigned one exact class from a finite obstruction dictionary `C`. The assignment must be complete: no absent pair may be omitted, multiply charged, or relabelled during the epoch.

## Canonical Hall core

If the threshold graph has no full matching, choose the canonical Hall-deficient set `X subseteq L` supplied by the deterministic maximum-matching convention, and put `Y=N(X)`.

Then:

1. `|X|-|Y|>0` is an exact threshold deficiency;
2. every pair in `X x (R\Y)` is absent from `G`;
3. the complete missing rectangle has size

   `M_X = |X| (|R|-|Y|)`.

The reverse-load theorem therefore returns not only a deficient menu subset but a complete stock of exact missing incidences.

## Obstruction concentration

Let `m_c(X)` be the number of missing pairs in the rectangle assigned to class `c in C`. Then

`sum_c m_c(X)=M_X`.

Consequently some exact class satisfies

`m_c(X) >= ceil(M_X/|C|)`.

This is a retained physical obstruction witness, not an averaged or anonymous failure.

## Capacity routing

Give every class `c` an initial-plus-deposited capacity `K_c`. The rectangle decomposes exactly into

- paid incidence mass `min(m_c(X),K_c)`; and
- overload mass `(m_c(X)-K_c)_+`.

Thus every threshold Hall core is routed to one of the following:

- complete payment from the obstruction bank;
- one exact overloaded obstruction class;
- a dictionary, lineage, or deposit reset.

Summing over the endpoint-cost layer cake preserves this routing threshold by threshold. No reverse-load deficit can disappear between the transportation theorem and the obstruction ledger.

## Outside the contract

The bridge does not cover omitted missing pairs, dynamic obstruction dictionaries, signed cancellation between classes, nonadditive capacity reuse, or menu transitions that change the retained compatibility graph without a reset.
