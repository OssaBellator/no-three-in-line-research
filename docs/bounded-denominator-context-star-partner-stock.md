# Partner-stock routing for BDA context stars

**Branch:** `research/bounded-denominator-absorbers`

BDA5cc--BDA5cj route a weighted line family to either a context-disjoint matching or a high-incidence context-cell star. This note gives an independent payment stock inside the star branch when payment is attached to the partner cell rather than the common center.

Let `G_L` be the simple weighted pair-address graph on the `n` available context cells of one connector, resonant or radial line. Write

\[
W_L=\sum_{e\in E(G_L)}w(e)
\]

and, for a cell `x`,

\[
S_x=\sum_{e\ni x}w(e).
\]

## BDA5ck -- exact weighted star identity -- PROVED

\[
\boxed{
\sum_x S_x=2W_L.
}
\]

Consequently some context cell `x` satisfies

\[
\boxed{S_x\ge 2W_L/n.}
\]

### Proof

Every pair address has exactly two context-cell endpoints and contributes its weight once to each endpoint star. Pigeonhole over the `n` cells. QED.

## BDA5cl -- distinct-partner stock at one center -- PROVED

Fix a center `x`. Because pair addresses are simple unordered pairs, the incident addresses

\[
\{x,y\}
\]

have pairwise distinct partner cells `y`. Thus the complete star at `x` is automatically disjoint on its partner side.

### Proof

Two different simple pair addresses with common center `x` cannot have the same second endpoint. QED.

## BDA5cm -- one heavy partner-realization class -- PROVED

Fix a finite ordered partner-payment dictionary

\[
\mathcal R=\{r_1,\ldots,r_K\}.
\]

Assign every edge of the star at `x` its least realization class. One class has star weight at least

\[
\boxed{S_x/K.}
\]

For a center supplied by BDA5ck, this is at least

\[
\boxed{2W_L/(nK).}
\]

The selected edges still have pairwise distinct partner cells. If class `r_j` realizes at least `rho_j w(e)` through a capacity attached only to the partner cell, total realized payment is at least

\[
\boxed{2\rho_j W_L/(nK).}
\]

### Proof

The least realization classes partition the star, so pigeonhole gives `S_x/K`. BDA5cl gives distinct partners. Sum the declared partner-local payments. QED.

## BDA5cn -- complete matching-or-partner-star router -- PROVED UNDER THE PAYMENT CONTRACT

For every weighted BDA line family, one exact continuation holds:

1. bounded context-cell incidence gives a context-disjoint matching and one realization class of weight at least `W_L/(K(2d-1))` by BDA5ch;
2. one weighted context star has weight at least `2W_L/n`, and one partner-payment class inside it has weight at least `2W_L/(nK)`;
3. branch 2 realizes partner-local payment according to BDA5cm;
4. or one pair lacks a fixed line, partner, realization, owner, orientation, occurrence or payment record.

The matching branch is disjoint at both endpoints. The star branch reuses one center but is disjoint at every partner, so it is valid whenever the consumed resource is partner-local.

### Proof

Apply either the earlier bounded-incidence matching router or BDA5ck--BDA5cm. The two payment contracts record exactly which endpoint-local capacities are reused. QED.

## Corrected BDA6 frontier

Both outputs of the heavy-line router now contain a quantitatively large realization class: a fully context-disjoint matching, or a common-center stock disjoint on the partner side. Remaining work is to verify the appropriate endpoint-local payment contract for each owner/absorber class and to import higher-rank events.

## Finite check

`scripts/verify_bda_context_star_partner_stock.py` enumerates finite weighted pair graphs, verifies the weighted star identity, partner distinctness and realization-class bounds.