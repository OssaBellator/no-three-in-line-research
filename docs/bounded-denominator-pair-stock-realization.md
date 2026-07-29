# Realization classes for disjoint BDA pair stocks

**Branch:** `research/bounded-denominator-absorbers`

BDA5cc--BDA5cf turn every heavy connector, resonant or radial line into either a high-incidence context-cell star or a vertex-disjoint weighted pair stock. This note resolves the disjoint stock into one finite owner/payment class.

Let `M` be the returned matching of pair addresses on a fixed line, with weights `w(e)`. Fix an ordered finite realization dictionary

\[
\mathcal R=\{r_1,\ldots,r_K\}
\]

whose records may encode owner, absorber type, payment channel, protected-cell ticket, occurrence class or context orientation. Assign every matched pair its least valid realization class.

## BDA5cg -- exact realization partition -- PROVED

For `1<=j<=K`, let

\[
M_j=\{e\in M:\text{least realization}(e)=r_j\}.
\]

Then the `M_j` partition `M` and

\[
\boxed{
 w(M)=\sum_{j=1}^K w(M_j).
}
\]

Every `M_j` remains a matching and therefore remains context-cell-disjoint.

### Proof

Every matched address has exactly one least valid realization class. Subfamilies of a matching are matchings. Summing weights over the partition proves the identity. QED.

## BDA5ch -- one heavy realization class -- PROVED

One class satisfies

\[
\boxed{
 w(M_j)\ge \frac{w(M)}K.
}
\]

Combining with BDA5cc, if the original line weight is `W_L` and the positive-address degree is at most `d`, then one realization class supports a disjoint pair stock of weight at least

\[
\boxed{
 \frac{W_L}{K(2d-1)}.
}
\]

### Proof

Pigeonhole BDA5cg and use `w(M)>=W_L/(2d-1)`. QED.

## BDA5ci -- realized payment and ticket capacity -- PROVED UNDER THE CLASS CONTRACT

Suppose class `r_j` realizes payment at least `rho_j w(e)` from each pair `e in M_j`, with `rho_j>=0`. Then total realized payment is at least

\[
\boxed{
 \rho_j w(M_j)
 \ge
 \frac{\rho_j W_L}{K(2d-1)}.
}
\]

Alternatively, if class `r_j` consumes one capacity-one resource attached to one context cell of each pair, the complete class stock is valid because its pairs are vertex-disjoint.

### Proof

Sum the per-pair payment over `M_j` and use BDA5ch. Context-cell disjointness prevents reuse of a cell-local capacity. QED.

## BDA5cj -- complete realized-line router -- PROVED

For every weighted connector, resonant or radial line family and every threshold `d`, one exact continuation holds:

1. one context cell lies in more than `d` positive pair addresses;
2. one owner/payment/ticket realization class contains a disjoint pair stock of weight at least `W_L/(K(2d-1))`;
3. that class realizes payment according to BDA5ci;
4. or one pair lacks a fixed owner, realization, occurrence, orientation or context-cell record.

Thus the disjoint BDA pair branch is reduced to finitely many owner/payment classes with an explicit retained fraction. Remaining line work is to prove the per-class payment efficiency or pay the returned high-incidence context star.

## Corrected BDA6 frontier

Off-diagonal geometry, weighted overlap, disjoint pair extraction and finite realization concentration are closed. Remaining work is class-specific payment, high-incidence star payment and higher-rank event imports.

## Finite check

`scripts/verify_bda_pair_stock_realization.py` enumerates small weighted matchings, verifies realization partitions, the `1/K` class bound and the inherited line-weight payment estimate.