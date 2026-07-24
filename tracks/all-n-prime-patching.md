# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This independent track assumes saturated no-three configurations are eventually
available on every sufficiently large `(p-1)x(p-1)` grid and asks how to extend
them to nearby side lengths.  Prime gaps alone do not suffice: increasing the
side from `m` to `m+t` requires an exact row-column-preserving absorber adding
`2t` net points.

The focused theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).
Detailed chapters are `docs/27` through `docs/77`.

## PP1 — Degree interface

### Status: PROVED

The branch classifies the boundary degree states, including the exceptional
one-strip case, and separates exact saturation from geometric no-three
conditions.  For general reservoirs, deleting source points creates prescribed
row and column deficits that are restored by movement, refill, corner, or
old-old replacement cells.

## PP2 — Selection endpoints

### Status: PROVED AS IMPLICATIONS; geometric hypotheses remain open

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

remain available.  The unresolved work is geometric preparation, not degree
selection.

## PP3 — Robust seed preparation

### Status: OPEN, with prime-gap-scale internal macro geometry closed

## 1. Earlier local architectures

The branch contains complete positive and negative analyses for:

- one-strip and corner patches;
- deletion-aware row-lift banks;
- projection obstructions and forced-triple lower bounds;
- component-clean movement/refill banks;
- square-root parabolic matching reservoirs and sheared parameter families;
- cycle-reservoir 2-SAT;
- protected rectangle and tomographic trade banks;
- matching-first width-two rungs and full 36-state block banks.

A key correction is that independent old-column and old-row templates cannot
have positive constant matching-admissible density at sublinear width.  Matching
coordinates must be correlated through actual source edges.

## 2. Universal matching-pool supply

Every saturated source decomposes into two perfect matching layers.  Matching
availability is therefore exact and spread: a uniform `k`-edge subset of one
layer is always a matching reservoir and has hypergeometric cylinder
probabilities.

At the balanced prime-gap exponents, put

\[
 \rho=\frac{19}{40},
 \qquad
 \beta=\frac{19}{80},
 \qquad
 \mu=\frac{23}{80}.
\]

Then

```text
macro count M   = m^(23/80+o(1)) = m^0.2875
pool size R     = m^(19/40+o(1)) = m^0.475
macro width W   = Theta(sqrt R)  = m^0.2375
total width MW  = m^(21/40+o(1)) = m^0.525.
```

Every matching layer contains the required number of pairwise disjoint pools;
the total source-edge budget `MR=m^(61/80+o(1))` is sublinear.

## 3. Universal internal square-root macro

One macro has `2W` slots.  A slot selects a source edge `(x,y)` and inserts

\[
 (x,A),
 \qquad
 (B,y),
\]

for one movement-row label `A` and refill-column label `B`.  Balanced label maps
give exactly two points on every installed new coordinate.

The product-space local lemma PP3dl--PP3do proves that every `R`-edge matching
pool supports an internally no-three macro of width

\[
 W=\Theta(\sqrt R).
\]

The conditioned distribution has fixed-rank cylinder spread `O(R^-q)`.  Random
balanced movement/refill coupling further reduces a prescribed same-edge pair
to `O(1/(RW))`.

Thus matching supply, row-column restoration, internal geometry, and internal
spread are universal at the prime-gap width.

## 4. Fixed-pair and same-edge source cleaning

For each movement label `A` and refill label `B`, define the fixed-pair-safe edge
sets `C_A,D_B`.  The source-clean macro theorem applies when the compatibility
intersection has constant density.

A same-edge anchored triple has the exact factorization

\[
 (A-v)(B-u)=(x-u)(y-v).
\]

For a label pair `(A,B)`, delete from `C_A cap D_B` every source edge satisfying
this equation with a retained anchor.  The refined domain `H(A,B)` therefore
removes simultaneously:

- every fixed-fixed-patch triple;
- every fixed-anchor triple using the movement/refill pair controlled by one
  source edge.

The number of bad label incidences is controlled by an exact matrix

\[
 \mathcal U=\sum_{A,B}|U_{A,B}|
\]

and, more coarsely, by pool-anchor divisor energy.

## 5. Numerical-label coordinate correction

A numerical candidate label is an actual final grid coordinate.  Selecting only
`W<L` labels from `[m+1,m+L]` leaves the other coordinates unsaturated; arbitrary
compression of the selected labels does not preserve collinearity.  Therefore
unused labels are not free.

The valid replacement uses exactly

\[
 T=MW
\]

final new rows and exactly `T` final new columns.

A balanced ownership map assigns every movement label to one macro, exactly `W`
labels per macro.  One global perfect matching assigns every refill label exactly
once through the refined compatibility graph of the macro owning the movement
label.  PP3fw then applies the internal macro theorem independently in every
pool while saturating every final coordinate.

A deterministic sufficient condition is minimum degree `T/2` on both sides of
the resulting global graph.  PP3fy gives a random balanced-ownership endpoint:
uniform left degrees above `(1/2+zeta)T` and averaged right degrees above
`(1/2+2zeta)T` yield a valid allocation for large `T`.

## 6. Weighted global compatibility

After unary source cleaning, group all witnesses of the same forbidden slot
value pattern into one event.  For two slots use the relation

\[
 \Gamma_{s,t}\subseteq H_s\times H_t,
\]

and for three slots use

\[
 \Xi_{s,t,u}\subseteq H_s\times H_t\times H_u.
\]

Their exact probabilities are their domain densities.  For each slot define the
total additional incident probability mass `Lambda_ext(s)`.

The weighted asymmetric local lemma PP3fi--PP3fl proves completion when

\[
 \boxed{
 \Lambda_{\rm ext}(s)
 \le
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}
 \quad\text{for every slot }s.
 }
\]

This is strictly weaker than bounding the raw number of bad events by `O(R)`.
Many rank-three events are harmless when their individual probabilities are
small.

Writing `bar d_{s,t}` for average pair completion multiplicity and
`bar c_{s,t,u}` for average triple completion multiplicity, a sufficient form is

\[
 \sum_{t\ne s}\bar d_{s,t}
 +
 \sum_{\{t,u\}}\bar c_{s,t,u}
 \le
 \gamma R
 \left(
 \frac1{48}
 -
 \frac{5}{8\gamma\sqrt R}
 \right).
\]

Failure exposes one explicit high-energy slot star rather than an unstructured
global triple count.

## 7. Universal one-sided cross-macro cancellation

A perfect matching layer can be divided into `M` disjoint consecutive column
slabs of `R` edges because `MR=o(m)`.  Give those macros consecutive
movement-row intervals in the same order.

The movement/refill pair controlled by one slot lies on a negative-slope line.
Every movement point of a later macro is northeast of the movement endpoint, and
every movement point of an earlier macro is southwest.  Hence no movement point
of another macro lies on that line.

Therefore every cross-macro relation consisting of a same-slot pair plus a
movement point is empty.  The row-slab transpose eliminates the refill version.
One whole high-probability direction is removed from the weighted mass without
spending entropy.

## 8. Constant-width side analysis

The older width-two matching-block route remains useful diagnostically but is no
longer the principal asymptotic route.

It proves:

- exact 36-state local banks and clean-state packing criteria;
- random block and deletion-aware profile formulas;
- exact blocker-demand bad boxes of rank at most three.

It also records sharp barriers:

- random independent deletion covers an additional blocker only with probability
  `O(K/m)`;
- unary blocker-cover domains are empty on both stored matching layers from side
  seven through ten;
- every stored two-block width-two partition at sides eight through ten fails
  before patch-patch interactions are considered.

These failures motivate correlated deletion or protected trades rather than a
raw product measure.

## 9. Current exact bottleneck

The missing theorem now has two quantitative parts.

### A. Global refined label allocation

Construct a balanced ownership of all `T=MW` final movement labels and one global
refined perfect matching to all final refill labels.  Equivalently, prove the
left/right density conditions of PP3fy, or exploit failures through:

- boundary-shadow concentration;
- Hall obstructions;
- exact bad-label incidence concentration;
- divisor-energy concentration;
- protected rectangle, cycle, or tomographic trades.

### B. Residual grouped completion energy

After source cleaning and one-sided slab cancellation, prove for every slot

\[
 \Lambda_{\rm ordinary\ anchor}(s)
 +
 \Lambda_{\rm residual\ cross}(s)
 \le
 \frac1{48}-o(1).
\]

Equivalently, prove the PP3fp completion-energy inequality.  This is the exact
remaining cross-macro distribution theorem.

The branch does not prove the no-three-in-line conjecture.

## PP4 — Prime-gap transfer

### Status: PROVED UNDER PP2--PP3

If the extension width covers the backward gaps from solved prime-minus-one
sizes, then the solved sizes transfer to every sufficiently large side length.
The published exponent requires a fixed positive multiple of `m^0.525` (with the
usual constant and rounding slack).

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; STORED CERTIFICATES VERIFIED FOR `2<=n<=10`

The eventual finite threshold and complete exception list depend on the missing
asymptotic PP3 theorem.

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
- refined fixed-pair/same-edge label domains;
- exact versus divisor-energy oversampled graph bounds.

Key current commands include:

```bash
python scripts/check_weighted_slot_mass.py \
  experiments/weighted-slot-mass-example.json

python scripts/analyze_same_edge_anchor_domains.py \
  certificates/prime-patching-small.json \
  --labels 12 --gamma 1/3 --epsilon 1/6 \
  --output /tmp/refined-labels.json

python scripts/check_oversampled_label_matching.py \
  /tmp/refined-labels.json
```

These finite programs are diagnostics or exact finite checks; they are not an
asymptotic proof unless paired with a proved classification theorem.