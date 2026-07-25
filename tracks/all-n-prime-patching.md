# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
prime-minus-one sizes and asks for an exact row-column-preserving patch from side
`m` to side `m+t`. Prime gaps alone are not enough: the patch must add `2t` net
points, preserve exactly two points in every old and new row and column, and
avoid every new collinear triple.

The detailed theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).

## PP1 — Degree interface

### Status: PROVED

The branch classifies the boundary and arbitrary-reservoir degree states. Deleting
source points creates exact row and column deficits; movement, refill, corner,
old-old, and equal-margin trade states restore those deficits.

The degree bookkeeping is no longer the bottleneck.

## PP2 — Selection endpoints

### Status: PROVED AS IMPLICATIONS

Available selection interfaces include:

- clone-space local lemmas for prescribed deficits;
- exact deletion-aware expectations;
- binary and finite-state forbidden-box CSPs;
- 2-SAT, CNF, and exact backtracking endpoints;
- first-moment, occurrence, and weighted local-lemma criteria;
- spread perfect-matching distributions in superregular hosts.

The unresolved work is geometric preparation of a sufficiently clean bank.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to structured controller-shadow conversion

## 1. Permanent corrections

Two earlier assumptions are refuted.

1. Independent old-column and old-row templates cannot retain constant
   matching-admissible density at sublinear width. Matching coordinates must be
   selected through actual source edges.
2. Numerical labels are actual final grid coordinates. Unused labels cannot be
   discarded and then compressed without risking loss of saturation and
   collinearity preservation.

A third correction is now explicit: the source-star alternative has a common
source endpoint, whereas the older alternating-star bank assumes a common
candidate point. Those two geometries are not interchangeable.

## 2. Slab-optimal matching-pool architecture

Every saturated source decomposes into two perfect matching layers. Consecutive
old-column slabs in one layer give disjoint pools with

```text
macro count M = m^(1/20+o(1)),
pool size   R = m^(19/20+o(1)),
macro width W = m^(19/40+o(1)),
total width T = MW = m^(21/40+o(1)).
```

For constants `a,b,gamma>0` with `ab<1`, one may take

\[
M\sim a m^{1/20},
\qquad
R\sim b m^{19/20},
\qquad
W\sim\frac{\gamma\sqrt R}{16}.
\]

This exponent balance is optimal among disjoint source pools with local width
`O(sqrt(R))`.

## 3. Internal macro geometry

A slot selecting source edge `(x,y)` and labels `(A,B)` deletes `(x,y)` and
inserts

\[
(x,A),
\qquad
(B,y).
\]

Balanced label maps restore exactly two points on every installed coordinate.
A product-space local lemma constructs internally no-three macros of width
`Theta(sqrt(R))`, and the conditioned distribution has fixed-rank spread
`O(R^-r)`.

Matching supply, saturation, internal geometry, and internal spread are closed.

## 4. Saturation-compatible global labels

Use exactly the final `T` new rows and `T` new columns. A balanced ownership map
assigns `W` movement labels to every macro, and one global perfect matching uses
every refill label exactly once.

For macro graph `J_i` and average refill degree `q_B`, the strongest current
direct endpoint is

\[
\deg_{J_i}(A)+q_B
\ge
T+8\sqrt{T\log T}
\]

for every incompatible triple `(i,A,B)`.

This complementary-degree condition is strictly weaker than separate `T/2`
minimum-degree requirements.

## 5. Controller-aware source safety

Unselected matching-pool edges remain in the source. A value is cell-safe only
when every blocker pair through its movement or refill cell contains its
controller edge. Its same-slot movement/refill pair must also avoid retained
source anchors.

After this unary cleaning, every remaining external pair/triple class has
`o(1)` incident probability mass at the slab-optimal exponents:

- patch-only cross-macro pairs;
- pure movement/refill triples;
- mixed patch triples;
- ordinary two-slot source-anchor pairs.

Thus global controller-aware allocation would complete the full
`Omega(m^0.525)` patch.

## 6. Failure structure

Positive-density controller-aware cell failure produces one of:

1. a source-endpoint star with `Omega(m^0.475)` distinct blocker rays;
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels,
   controllers, and endpoint-disjoint blocker pairs.

The resource branch contains a matching-layer endpoint bank. Endpoint
permutations preserve row and column degrees and satisfy exact
removal-credit-minus-insertion-cost identities.

## 7. Source-valid resource endpoint trade

For a resource endpoint bank of size

\[
Q=\Omega(m^{21/40}),
\]

sparse unary source shadow permits thinning to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40}.
\]

The branch removes every source-invalid class by:

- source-safe host pruning;
- a permutation local lemma for unary cells, transpositions, transitions, and
  directed 3-cycles;
- divisor regularisation of anchored transitions;
- support-sensitive thinning of rank-four anchored pairs and inserted triples.

The result is a saturation-preserving no-three endpoint trade. Source
admissibility is closed in this regime.

## 8. Zero-unary Hall endpoint

Delete from the source-safe endpoint host:

- designated-credit recapture cells;
- every cell with positive residual unary insertion shadow.

Call the resulting graph `G_0`. Every perfect matching of `G_0` has zero unary
insertion shadow and preserves the designated credit.

If `G_0` has no perfect matching, Hall gives exact sets

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

For every fixed `alpha>0`, failure is either:

- a macroscopic forbidden rectangle with both sides at least `alpha q`; or
- fewer than `alpha q` almost-completely forbidden fibres.

If `G_0` is superregular and its remaining pair/triple conflicts are summable, a
spread perfect matching produces a source-admissible trade with complete
insertion cost zero.

## 9. Support-core regularisation

Deleting `o(q)` exceptional endpoint indices preserves `(1-o(1))q` credit units
and decreases every support family. Therefore isolated rich fibres and binary
stars are not terminal.

Persistent failure forces either:

\[
\Omega(q^2)
\]

simple unary support in a linear fibre core, or

\[
\Omega(q^3)
\]

binary shadow support in a linear conflict core.

The Hall rectangle and binary core localise further.

- A recapture-dominated Hall rectangle contains `Omega(q)` designated lines,
  each meeting the endpoint rectangle in `Omega(q)` cells.
- A cubic binary core contains either one endpoint cell with `Omega(q)` shadow
  partners or `Omega(q)` resource-disjoint binary conflicts.
- The endpoint-cell fan gives either a common-candidate line with many endpoint
  intersections or many distinct controller candidates.

These are the exact rectangle, tomographic, and fan resources for the next
conversion.

## 10. Dynamic pool excess-shadow potential

Inside one controller pool, endpoint permutations preserve the pool's old-column
set `X_i` and old-row set `Y_i`. Hence they preserve the complete candidate-cell
universe even though the matching between `X_i` and `Y_i` changes.

Every movement/refill candidate cell has exactly one automatic axis blocker pair,
and that pair contains the current controller point. Every additional blocker is
nonaxis and controller-disjoint. Define

\[
\boxed{
\Xi(S)=\sum_{z\in\mathcal V_{\rm cell}}\bigl(b_S(z)-1\bigr).
}
\]

Then:

- `Xi` is a nonnegative integer;
- the number of bad cell entries is at most `Xi`;
- `Xi=0` exactly when every candidate cell is safe from retained-pair blockers;
- pool-compatible endpoint trades satisfy an exact
  `insertion cost - removal credit` identity.

A star centre inside a controller pool contributes its full blocker-star credit
to `Xi`. Moving it within the pool does not change the candidate-cell universe.
Thus the earlier dynamic-controller-identity obstruction is removed.

For any fixed density threshold `eta`, a uniform pool-compatible improving trade
terminates below `eta`. Uniform thresholds `eta_m=o(1)` yield `o(1)` bad cell
density; improvement whenever `Xi>0` terminates at `Xi=0`.

## 11. Current exact bottleneck

The missing theorem now has the following concrete forms.

### Direct allocation

Prove the controller-aware graphs satisfy the complementary-degree global
allocation condition.

### Hall/tomographic conversion

Convert a forbidden Hall rectangle, a matchable but non-superregular zero-unary
host, or the linear bank of rich designated recapture lines.

### Binary conversion

Convert the endpoint-cell fan or the linear resource-disjoint binary conflict
bank.

### Pool-compatible paid conversion

Construct source-admissible within-pool endpoint trades satisfying

\[
\mathcal I_\Xi<\mathcal C_\Xi
\]

for the source-star or resource structures.

A successful conversion strictly decreases the relevant integer potential or
directly creates the dense global allocation needed by the macro theorem.

The branch does not yet prove this final conversion theorem and therefore does
not prove the no-three-in-line conjecture.

## 12. Constant-width side analysis

The older width-two route remains diagnostic. It proves exact 36-state banks,
clean-state packing criteria, deletion-aware profiles, and blocker-demand CSPs.
It also records that independent deletion does not cover additional blockers and
that all stored raw two-block extensions at sides eight through ten fail before
patch-patch interactions.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

A patch of fixed positive width constant times `m^0.525` covers the published
backward prime-gap scale, with the usual constant and rounding slack.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES VERIFIED FOR `2<=n<=10`

The eventual threshold and finite exception list depend on the missing
asymptotic PP3 conversion theorem.

## Current computational checks

```bash
python scripts/verify_no_three_certificate.py \
  certificates/prime-patching-small.json

python scripts/check_global_label_ore.py \
  experiments/global-label-ore-example.json

python scripts/analyze_controller_aware_domains.py \
  certificates/prime-patching-small.json \
  --labels 12 --gamma 1/3

python scripts/analyze_endpoint_trade_hosts.py \
  certificates/prime-patching-small.json

python scripts/analyze_endpoint_hall_rectangles.py \
  certificates/prime-patching-small.json

python scripts/analyze_dynamic_cell_shadow.py \
  certificates/prime-patching-small.json \
  --labels 12
```

These are diagnostics or exact finite checks, not asymptotic proofs without the
stated classification theorems.
