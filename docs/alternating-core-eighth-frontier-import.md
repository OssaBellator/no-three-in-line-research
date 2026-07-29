# Eighth frontier import for AC5 resource capacity and local closure

**Branch:** `research/alternating-core-chain`

AC5ca--AC5cg import labeled RI conflicts, labeled source-hole stars, realized BDA pair stocks, signed sparse cycle defects, mixed-radix recurrence and degenerate rational charts. This note imports the next physical closures.

## AC5ch -- RI conflict-resource capacity import -- PROVED

Suppose a failed requested RI bank returns a conflict class of weight `Q`, and every conflict record has one least payment resource. For resource multiplicity threshold `mu`, one exact alternative holds:

1. one resource occurs in more than `mu` conflict records;
2. one resource-disjoint representative stock has weight at least
   \[
   \boxed{Q/\mu.}
   \]

After the conflict-label and sublabel reductions, the retained stock has weight at least

\[
\boxed{
\frac{W}{(q-1)(K+1)R\mu}.
}
\]

### Proof

Partition the class by least resource and choose one maximum-weight record from each fibre. A fibre of size at most `mu` has maximum weight at least its total divided by `mu`. QED.

## AC5ci -- source-star resource-capacity import -- PROVED

Let one labeled source-cause hole star have weight `Q_C`. For resource multiplicity threshold `mu`, either one payment resource occurs more than `mu` times or a distinct-resource endpoint stock has weight at least

\[
\boxed{Q_C/\mu.}
\]

Hence one threshold set with weighted hole mass `mathcal M_S` yields a stock of weight at least

\[
\boxed{
\frac{\mathcal M_S}{|A|K\mu}.
}
\]

### Proof

Apply the same maximum-representative argument to endpoint records in the labeled source star, then use AC5cb. QED.

## AC5cj -- BDA partner-star import -- PROVED

Let a weighted BDA line have `n` available context cells and total pair weight `W_L`. The weighted endpoint-star identity gives one center with star weight at least

\[
\boxed{2W_L/n.}
\]

All pair addresses in that star have distinct partner cells. With a partner-realization dictionary of size `K`, one class retains at least

\[
\boxed{2W_L/(nK).}
\]

If payment is attached only to the partner cell, this stock is capacity-one on the consumed resources even though it reuses the center.

### Proof

Every pair contributes its weight to two endpoint stars. Pigeonhole over centers and then over realization classes. Simplicity of pair addresses makes partners distinct. QED.

## AC5ck -- sparse Coxeter-local history import -- PROVED UNDER THE CHART CONTRACT

Order the `r` moved rows and use adjacent swaps `s_i`. On a Coxeter-closed legal-state chart, an antisymmetric transition charge is a state potential if and only if every commuting-square and braid-hexagon defect vanishes.

The local relation dictionary has at most

\[
\boxed{
\frac{(r-2)(r-1)}2
}
\]

defects per state. Failure returns one least square, braid, intermediate-legality or Coxeter-closure defect.

### Proof

Zero local defects make path charge invariant under commuting and braid moves; antisymmetry cancels backtracks. Coxeter closure connects any same-endpoint legal words, so integration from a base state defines a potential. QED.

## AC5cl -- exact physical stutter import -- PROVED UNDER THE TICKET CONTRACT

For an exact deterministic physical stutter `F(d)=d`, the score decomposition satisfies

\[
\boxed{G=P-D.}
\]

The transition therefore gives positive payment, physical debt, a balanced positive exchange, or a neutral stutter. A neutral stutter receives one capacity-one ticket keyed by the complete state identity. Ticket nonreuse forbids a second identical neutral stutter without payment, reset, changed state or a named hidden-field failure.

### Proof

The state potential cancels because the endpoints agree. Determinism reproduces the same fixed-point ticket key on repetition. QED.

## AC5cm -- rational fixed-ratio capacity import -- PROVED

For a rational line-following chart `lambda=f/g`, put `D=max(deg f,deg g)` and let at most `M` physical operations share one parameter. For every fixed finite ratio `alpha`, either

\[
\boxed{f-\alpha g\ne0}
\]

and the ratio address has incidence at most `DM`, or `f-alpha g=0` identically and `lambda` is the constant ratio `alpha`.

A finite dictionary of `J` ratios, together with denominator exceptions, has incidence at most

\[
\boxed{JDM+(\deg g)M.}
\]

### Proof

Clear the nonzero denominator. A nonzero degree-at-most-`D` polynomial has at most `D` roots; the denominator has at most `deg g` roots. Multiply by physical parameter multiplicity. QED.

## AC5cn -- strengthened resource/local continuation -- PROVED UNDER THE DECLARED CONTRACTS

An AC menu now has one exact continuation:

1. a physical RI bank, one overloaded conflict resource, or a resource-disjoint conflict stock with explicit retained weight;
2. trimmed low-event flow, one overloaded source-star resource, or a distinct-resource endpoint stock;
3. a fully disjoint BDA matching class, or a common-center stock disjoint on the partner-payment side;
4. a sparse endpoint potential certified by local square/braid tests, or one local Coxeter defect;
5. mixed-radix descent, a finite decoration cycle, positive/debt/balanced score, or one nonreusable neutral fixed-point ticket;
6. polynomial or nonconstant rational protected-event capacities, or one constant-ratio homothetic family;
7. or one existing AC4/AC5 payment, Hall-core, owner, reset, ticket or failed physical contract.

This does not yet prove the actual resource multiplicities, endpoint-local payment contracts, Coxeter closure, score identities or constant-ratio payment. It replaces those gaps by explicit overloaded resources, disjoint stocks, local relations, fixed-point identities and fixed-ratio profiles.

## Finite check

`scripts/verify_ac_eighth_frontier_import.py` checks resource-fibre representative bounds, weighted partner stars, local Coxeter relations, fixed-point ticket identity and rational fixed-ratio root bounds on finite abstractions.