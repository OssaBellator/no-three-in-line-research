# Seventh frontier import for AC5 labeled payment and monotone recurrence

**Branch:** `research/alternating-core-chain`

AC5bt--AC5bz import heavy RI conflict neighborhoods, weighted endpoint stars, BDA line matchings, sparse fundamental defects, factorized decoration stocks and polynomial protected-event charts. This note imports the next physical refinements.

## AC5ca -- labeled RI conflict import -- PROVED

Fix a requested `q`-component RI bank, total component weight `W`, and a finite conflict-label dictionary of size `K`. If the bank does not exist, AC5bt returns one closed conflict neighborhood of weight at least `W/(q-1)`. Assign the center to one bucket and every neighbor to its least conflict label. Then one exact bucket has weight at least

\[
\boxed{
\frac{W}{(q-1)(K+1)}.
}
\]

Any finite sublabel dictionary of size `R` preserves weight at least `W/((q-1)(K+1)R)`.

### Proof

The center and least-label neighbor classes partition the heavy neighborhood. Pigeonhole over `K+1` buckets and then over any sublabels. QED.

## AC5cb -- labeled weighted hole-star import -- PROVED

Let a low-event threshold set have weighted hole mass

\[
\mathcal M_S=\sum_{a\in A}\sum_{b\in S\cap H(a)}\lambda_b.
\]

If every hole incidence has one least physical cause from a dictionary of size `K`, then one source-cause bucket carries weight at least

\[
\boxed{
\frac{\mathcal M_S}{|A|K}.
}
\]

If exceptional endpoint weight exceeds a proposed budget `Lambda` at multiplicity threshold `tau`, the returned bucket has weight greater than `(tau+1)Lambda/(|A|K)`.

### Proof

Partition the occurrence-faithful weighted hole incidences by source and least cause. Combine pigeonhole with AC5bu. QED.

## AC5cc -- realized BDA pair-stock import -- PROVED

Let a connector, resonant or radial line have weight `W_L`, context-cell incidence at most `d`, and a realization dictionary of size `K`. AC5bv gives a disjoint pair matching of weight at least `W_L/(2d-1)`. One realization class therefore contains a disjoint pair stock of weight at least

\[
\boxed{
\frac{W_L}{K(2d-1)}.
}
\]

If that class pays at efficiency `rho`, the realized payment is at least `rho W_L/(K(2d-1))`. Otherwise one pair lacks a fixed owner, realization, orientation or occurrence record.

### Proof

Partition the matching by least realization class and pigeonhole. Subclasses remain context-cell-disjoint. QED.

## AC5cd -- labeled sparse defect import -- PROVED

Let the finite sparse legal-state graph have total absolute fundamental defect mass `D`, and let its non-tree edges carry least physical labels from a dictionary of size `K`. One label carries defect mass at least

\[
\boxed{D/K,}
\]

and one sign within that label carries at least

\[
\boxed{D/(2K).}
\]

A least non-tree edge then returns the corresponding edge-level cycle witness.

### Proof

Partition absolute defect mass by label and then into positive and negative parts. Pigeonhole twice. QED.

## AC5ce -- mixed-radix decoration descent import -- PROVED

Suppose the nonreconstructible physical decoration coordinates have ordered alphabet sizes `K_1,...,K_r`. Their mixed-radix rank takes values in

\[
\{0,\ldots,\prod_iK_i-1\}.
\]

If every reset-free nonpaying transition is rank-nonincreasing and every nonstutter transition strictly decreases rank, then there are at most

\[
\boxed{
\prod_iK_i-1
}
\]

strict nonpaying transitions before payment, reset, exact stutter or one least rank-contract failure. No nontrivial balanced-cycle ticket is needed in this monotone case.

### Proof

Mixed-radix rank is an injective nonnegative integer stock. Every nonstutter transition decreases it by at least one; a closed nonincreasing cycle is rank-constant and hence consists only of stutters. QED.

## AC5cf -- degenerate protected-chart rational import -- PROVED

For a polynomial collinearity chart with

\[
A=X_2-X_1,
\qquad
B=X_3-X_1,
\qquad
\det(A,B)\equiv0,
\]

one exact alternative holds:

1. `A=0`, so two moving cells are identically coincident;
2. `A!=0`, and over `F(t)` one has
   \[
   \boxed{B=\lambda A}
   \]
   for a rational function `lambda=f/g` with `deg f<=deg B` and `deg g<=deg A`;
3. denominator-zero operations have incidence at most `(deg A)M` under physical parameter multiplicity `M`;
4. or one chart, field, fibre, alias, lineage or occurrence record fails.

Thus a coefficient-degenerate chart returns a bounded-degree rational line-following family plus a root-bounded exceptional set.

### Proof

Choose a nonzero coordinate `A_s` and set `lambda=B_s/A_s`. The determinant identity gives the other coordinate relation. The nonzero denominator has at most `deg A_s<=deg A` roots. QED.

## AC5cg -- strengthened labeled continuation -- PROVED UNDER THE DECLARED CONTRACTS

An AC menu now has one exact continuation:

1. a requested physical RI bank, or one quantitatively heavy conflict label/sublabel;
2. trimmed low-event flow, or one quantitatively heavy source-cause hole star;
3. a context-disjoint BDA pair stock in one owner/payment class, or one high-incidence line star;
4. a sparse endpoint potential, or one labeled and signed fundamental-cycle defect;
5. mixed-radix physical descent, payment, reset or exact stutter, with finite-cycle fallback only for genuinely circulating fields;
6. a nondegenerate polynomial protected capacity, or a degenerate rational line-following chart with bounded denominator exceptions;
7. or one existing AC4/AC5 payment, Hall-core, owner, reset, ticket or failed physical contract.

This does not yet prove the actual label dictionaries, per-class payment efficiencies, monotonicity orders or rational-line payment. It converts each remaining gap into one finite labeled physical class, one integer rank defect or one bounded-degree rational profile.

## Finite check

`scripts/verify_ac_seventh_frontier_import.py` checks the label partitions, source-cause concentration, pair-stock realization, signed defect concentration, mixed-radix descent and degenerate rational dependence on finite abstractions.