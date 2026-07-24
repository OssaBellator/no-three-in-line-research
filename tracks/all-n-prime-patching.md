# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This independent track assumes saturated no-three configurations are eventually
available on every sufficiently large `(p-1)x(p-1)` grid and asks how to extend
them to nearby side lengths. Prime gaps alone do not suffice: increasing the
side from `m` to `m+t` requires an exact row-column-preserving absorber adding
`2t` net points.

The focused theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).
Detailed chapters are `docs/27` through `docs/88`.

## PP1 — Degree interface

### Status: PROVED

The branch classifies the boundary degree states, including the exceptional
one-strip case, and separates exact saturation from geometric no-three
conditions. For general reservoirs, deleting source points creates prescribed
row and column deficits that are restored by movement, refill, corner, or
old-old replacement cells.

## PP2 — Selection endpoints

### Status: PROVED AS IMPLICATIONS; geometric preparation remains open

Available exact endpoints include:

- pair-aware and arbitrary-reservoir clone-space local lemmas;
- state-dependent deletion expectation PP2l--PP2o;
- internally clean spread-bank first moments;
- sequential and static permutation-layer local lemmas;
- binary and finite-state forbidden-box CSPs;
- exact SAT/backtracking solvers;
- product-distribution first-moment, occurrence, and weighted-probability-mass
  local-lemma criteria.

For active clone size `N>=200`, the sufficient arbitrary-reservoir bounds

```text
u_*   <= N/200
pi_*  <= N^2/1600
tau_* <= N^3/3200
```

remain available. The unresolved work is geometric preparation, not degree
selection.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to one controller-shadow conversion theorem

## 1. Earlier architectures and corrections

The branch contains complete positive and negative analyses for:

- one-strip and corner patches;
- deletion-aware row-lift banks;
- projection obstructions and forced-triple lower bounds;
- component-clean movement/refill banks;
- square-root parabolic matching reservoirs and sheared parameter families;
- cycle-reservoir 2-SAT;
- protected rectangle and tomographic trade banks;
- matching-first width-two rungs and full 36-state block banks.

Two important corrections are permanent.

1. Independent old-column and old-row templates cannot have positive constant
   matching-admissible density at sublinear width. Matching coordinates must be
   correlated through actual source edges.
2. Numerical candidate labels are actual final grid coordinates. Unused labels
   cannot be discarded and then compressed arbitrarily without risking loss of
   saturation and collinearity preservation.

## 2. Slab-optimal matching-pool supply

Every saturated source decomposes into two perfect matching layers. Choose one
layer and split consecutive old-column slabs into disjoint matching pools.
Unlike the earlier monotone-subsequence construction, the product-LLL macro
needs no endpoint order inside a pool.

The exponent-optimal square-root-macro balance is

```text
macro count M   = m^(1/20+o(1))  = m^0.05
pool size R     = m^(19/20+o(1)) = m^0.95
macro width W   = m^(19/40+o(1)) = m^0.475
total width T   = MW             = m^(21/40+o(1)) = m^0.525.
```

For constants `a,b,gamma>0` with `ab<1`, one may take

\[
M\sim a m^{1/20},
\qquad
R\sim b m^{19/20},
\qquad
W\sim \frac{\gamma\sqrt R}{16}.
\]

Then

\[
MW=
\left(
\frac{a\gamma\sqrt b}{16}+o(1)
\right)m^{21/40}.
\]

This balance is exponent-optimal among architectures with disjoint source pools
and local width `O(sqrt(R))`:

\[
M\ge \frac{T^2}{C^2m},
\qquad
R\le \frac{C^2m^2}{T^2}.
\]

Thus neither the `m^0.05` macro count nor the `m^0.95` pool size can be improved
by another power-law rebalance inside the current square-root framework.

## 3. Universal internal macro geometry

One macro has `2W` slots. A slot selects a source edge `(x,y)` and inserts

\[
(x,A),
\qquad
(B,y),
\]

for one movement-row label `A` and one refill-column label `B`. Balanced label
maps give exactly two points on every installed new coordinate.

The product-space local lemma proves that every `R`-edge matching pool supports
an internally no-three macro of width `Theta(sqrt(R))`. The conditioned
distribution has fixed-rank cylinder spread `O(R^-q)`.

Therefore matching supply, degree restoration, internal geometry, and internal
spread are universal at the required prime-gap width.

## 4. Saturation-compatible global label allocation

Use exactly the final

\[
T=MW
\]

new rows and exactly `T` new columns. A balanced ownership map assigns every
movement label to one macro, exactly `W` labels per macro. One global perfect
matching assigns every refill label exactly once through the compatibility graph
of the macro owning its movement label.

The original sufficient condition required minimum degree `T/2` on both sides.
The stronger complementary-degree theorem permits irregular graphs. For a fixed
ownership, it is enough that every nonedge `(A,B)` satisfy

\[
\deg(A)+\deg(B)\ge T.
\]

For random balanced ownership, define the average compatible ownership degree
of refill label `B` by

\[
q_B=
\frac1M
\sum_i
|\{A:(A,B)\in J_i\}|.
\]

A sufficient asymptotic condition is

\[
\boxed{
\deg_{J_i}(A)+q_B
\ge
T+8\sqrt{T\log T}
}
\]

for every incompatible triple `(i,A,B)`. This strictly weakens separate
`T/2+Omega(T)` bounds and localizes any failed Hall condition to one
complementary low-degree nonedge.

## 5. Controller-aware source safety

A fixed-core safety test is insufficient when a matching pool is active:
unselected pool edges remain in the source and may participate in blocker
pairs.

For source edge `e=(x,y)` and labels `A,B`, the correct unary domain is

\[
H_{A,B}^{\rm ctrl}
=
C_A^{\rm ctrl}
\cap
D_B^{\rm ctrl}
\setminus
U_{A,B}^{\rm ctrl}.
\]

Here:

- `e in C_A^ctrl` means every source blocker pair through `(x,A)` contains `e`;
- `e in D_B^ctrl` is the refill analogue;
- `U_AB^ctrl` removes values whose same-slot movement/refill pair has a retained
  source anchor.

Selecting a value deletes its controller edge, so every allowed blocker pair is
cleared deterministically. No unselected pool edge is silently treated as
fixed-deleted.

For macro `i`, define the controller-aware graph

\[
J_i^{\rm ctrl}(\gamma)
=
\{(A,B):|H_{i,A,B}^{\rm ctrl}|\ge\gamma R\}.
\]

All global allocation theorems apply unchanged to these graphs. If they admit a
balanced ownership and one global perfect matching, every unary retained-pair
and same-slot anchor certificate is absent value by value.

## 6. Weighted external geometry is closed

After unary controller-aware cleaning, all witnesses producing the same
forbidden slot-value pattern are grouped into one rank-two or rank-three event.
The weighted asymmetric local lemma charges the total incident event
probability, not the raw number of geometric descriptions.

The internal macro events leave the residual per-slot budget

\[
\frac1{48}-\frac{5}{8\gamma\sqrt R}.
\]

At the slab-optimal exponents, all remaining external geometry has total
incident mass `o(1)`.

### Patch-only events

- Cross-macro rank-two event mass is `O(T/R)=o(1)`.
- Pure movement and pure refill rank-three relations are bounded by an exact
  interval/gcd sum.
- Mixed rank-three relations satisfy divisor equations such as

  \[
  (x'-x)(y-A)=(A'-A)(B-x),
  \]

  and have total incident mass `o(1)` even under the elementary divisor bound.

Thus every patch-only cross-macro class is summable.

### Ordinary source-anchor pairs

- Movement-movement and refill-refill relations are bounded by congruence sums
  involving `gcd(h,d)/h`.
- Movement-refill relations satisfy

  \[
  (x-u)(y-v)=(A-v)(B-u)
  \]

  and are bounded using divisor-square sums and the fact that the source has
  exactly two points per old row and column.

Their complete incident mass is also `o(1)`.

Consequently, once the controller-aware global allocation exists, the weighted
local lemma gives a saturated no-three patch of width `Omega(m^0.525)`. Cross-
macro completion energy is no longer an independent bottleneck.

## 7. Structure forced by controller-shadow failure

A bad movement or refill entry consists of a typed new label, a controller edge,
and a noncontroller blocker pair.

A fixed source secant can witness at most one movement candidate per new row and
one refill candidate per new column. Therefore a positive fraction of bad
controller-aware entries forces linearly many distinct blocker pairs.

At the slab-optimal scale, one obtains one of two alternatives.

1. **Blocker star:** one source point lies on at least `m^0.475` distinct blocker
   pairs.
2. **Resource matching:** there are `Omega(m^0.525)` bad entries with pairwise
   distinct typed labels, distinct controller edges, and endpoint-disjoint
   blocker pairs; no selected controller is used as another selected blocker
   endpoint.

After pigeonholing the matching-layer type of the blocker pairs, the resource
matching supplies a matching-layer endpoint set of the same order.

Thus positive-density failure cannot remain diffuse.

## 8. Endpoint-permutation conversion bank

Let

\[
R_0=\{(x_i,y_i):i\in[q]\}
\]

be the extracted endpoint set in one permutation layer. For a derangement
`sigma`, replace it by

\[
R_\sigma=\{(x_i,y_{\sigma(i)}):i\in[q]\}.
\]

This preserves every old row and column degree and removes every point of
`R_0`.

Define the controller-shadow incidence potential

\[
\Psi(S)=
\sum_{\{p,q\}\subseteq S}w(p,q),
\]

where `w(p,q)` counts the controller-aware candidate entries blocked by the
source pair `{p,q}`. The trade has the exact identity

\[
\Psi(S_\sigma)-\Psi(S)
=
\mathcal I(\sigma)-\mathcal C(R_0),
\]

where `C` is removal credit and `I` is inserted shadow. A resource matching of
size `q` guarantees

\[
\mathcal C(R_0)\ge q.
\]

Uniform derangements are fixed-rank `O(1/q)`-spread. If `C,P,Q` count forbidden
inserted cells, pairs, and triples, and `A,B` are unary and binary insertion-
shadow weights, then a strict improvement follows from

\[
\boxed{
24\left(
\frac Cq
+
\frac P{q^2}
+
\frac Q{q^3}
+
\frac A{q^2}
+
\frac B{q^3}
\right)<1.
}
\]

Failure localizes collateral to a dense rank-one, rank-two, or rank-three core
on the endpoint rectangle.

## 9. Current exact bottleneck

Only one conversion theorem remains.

### Direct form

Prove the controller-aware graphs `J_i^ctrl(gamma)` satisfy the complementary-
degree global allocation criterion.

### Structured form

When controller-aware density fails, use the forced blocker-star or resource-
matching alternative to construct a source-admissible endpoint, rectangle, or
tomographic trade whose inserted shadow is below its paid removal credit.

A successful conversion strictly decreases the controller-shadow potential or
directly creates the dense global allocation needed by PP3hq.

The branch does not yet prove this conversion theorem and therefore does not
prove the no-three-in-line conjecture.

## 10. Constant-width side analysis

The older width-two matching-block route remains useful diagnostically but is no
longer the principal asymptotic route. It proves exact 36-state local banks,
clean-state packing criteria, random-block/deletion-aware profile formulas, and
rank-at-most-three blocker-demand boxes.

It also records sharp barriers:

- independent deletion covers an additional blocker only with probability
  `O(K/m)`;
- unary blocker-cover domains are empty on both stored matching layers from side
  seven through ten;
- every stored two-block width-two partition at sides eight through ten fails
  before patch-patch interactions are considered.

These failures motivate controller-correlated domains and paid trades rather
than a raw product deletion measure.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

If the extension width covers the backward gaps from solved prime-minus-one
sizes, then the solved sizes transfer to every sufficiently large side length.
The published exponent requires a fixed positive multiple of `m^0.525`, with
the usual constant and rounding slack.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES VERIFIED FOR `2<=n<=10`

The eventual finite threshold and complete exception list depend on the missing
asymptotic PP3 conversion theorem.

## Computational tools

The branch includes exact analyzers and solvers for:

- finite certificates and prescribed-degree extension CSPs;
- row-lift banks, projections, static and sequential loads;
- parabolic matching reservoirs and parameter sweeps;
- variable-reservoir expectation and cycle-reservoir 2-SAT;
- rectangle repair to depth two;
- width-two block domains, packing, and blocker demands;
- multistate and binary trade CSPs;
- weighted slot-mass verification;
- refined fixed-pair and same-edge label domains;
- exact versus divisor-energy label-graph bounds;
- complementary-degree global allocation.

Key commands include:

```bash
python scripts/check_weighted_slot_mass.py \
  experiments/weighted-slot-mass-example.json

python scripts/analyze_same_edge_anchor_domains.py \
  certificates/prime-patching-small.json \
  --labels 12 --gamma 1/3 --epsilon 1/6 \
  --output /tmp/refined-labels.json

python scripts/check_oversampled_label_matching.py \
  /tmp/refined-labels.json

python scripts/check_global_label_ore.py \
  experiments/global-label-ore-example.json
```

These finite programs are diagnostics or exact finite checks; they are not an
asymptotic proof unless paired with a proved classification theorem.
