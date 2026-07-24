# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This track assumes saturated no-three configurations are eventually available at
all sufficiently large prime-minus-one side lengths and asks how to extend them
to every nearby side length. Increasing the side from `m` to `m+t` requires an
exact row-column-preserving absorber adding `2t` net points.

The focused theorem ledger is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).
Detailed chapters now run through `docs/96`.

## PP1 — Degree interface

### Status: PROVED

Boundary states, the exceptional one-strip state, and arbitrary-reservoir degree
deficits are classified. Deleting source points and restoring their old rows and
columns is separated cleanly from the geometric no-three condition.

## PP2 — Selection endpoints

### Status: PROVED AS IMPLICATIONS

The branch contains exact clone-space, matching, SAT, CSP, first-moment, and
local-lemma endpoints for selecting from a prepared patch bank. The unresolved
work is geometric preparation, not degree selection.

## PP3 — Robust seed preparation

### Status: OPEN, reduced to support-concentrated controller-shadow conversion

## 1. Permanent corrections

Two tempting shortcuts are refuted.

1. Independent old-column and old-row templates cannot retain constant
   matching-admissible density at sublinear width. Matching coordinates must be
   correlated through actual source edges.
2. Numerical candidate labels are final grid coordinates. Unused labels cannot
   be discarded and arbitrarily compressed while preserving saturation and
   collinearity.

A third correction is essential for active matching pools: fixed-core safety does
not test blocker pairs using unselected pool edges. The valid domains are
controller-aware.

## 2. Exponent-optimal slab macro architecture

Every saturated source decomposes into two perfect matching layers. Choose one
layer and split consecutive old-column slabs into matching pools. The product-LLL
macro theorem does not require endpoint order inside a pool.

The optimal disjoint square-root-macro balance is

```text
macro count M   = m^(1/20+o(1))   = m^0.05
pool size R     = m^(19/20+o(1))  = m^0.95
macro width W   = m^(19/40+o(1))  = m^0.475
total width T   = MW              = m^(21/40+o(1)) = m^0.525.
```

For constants `a,b,gamma>0` with `ab<1`, one may take

\[
M\sim am^{1/20},
\qquad
R\sim bm^{19/20},
\qquad
W\sim\frac{\gamma\sqrt R}{16}.
\]

Then

\[
MW=
\left(
\frac{a\gamma\sqrt b}{16}+o(1)
\right)m^{21/40}.
\]

This exponent balance is optimal among architectures with disjoint source pools
and local width `O(sqrt(R))`:

\[
M\ge\frac{T^2}{C^2m},
\qquad
R\le\frac{C^2m^2}{T^2}.
\]

Every pool supports an internally no-three macro with fixed-rank conditioned
spread `O(R^-r)`.

## 3. Saturation-compatible global labels

Use exactly the final

\[
T=MW
\]

new rows and columns. A balanced ownership assigns exactly `W` movement labels
to every macro. One global perfect matching assigns every refill label exactly
once through the compatibility graph of the owning macro.

For a fixed global graph, every nonedge `AB` may have irregular endpoint degrees;
it is enough that

\[
\deg(A)+\deg(B)\ge T.
\]

For random balanced ownership, define

\[
q_B=
\frac1M
\sum_i
|\{A:(A,B)\in J_i\}|.
\]

A sufficient condition is

\[
\boxed{
\deg_{J_i}(A)+q_B
\ge
T+8\sqrt{T\log T}
}
\]

for every incompatible triple `(i,A,B)`.

## 4. Controller-aware source safety

For source edge `e=(x,y)` and final labels `A,B`, define

\[
H_{A,B}^{\rm ctrl}
=
C_A^{\rm ctrl}
\cap
D_B^{\rm ctrl}
\setminus
U_{A,B}^{\rm ctrl}.
\]

Here every blocker pair through `(x,A)` or `(B,y)` must contain the controller
`e`, which is deleted when that value is selected. The last term removes a
retained anchor on the line through both inserted cells.

For macro `i`, put

\[
J_i^{\rm ctrl}(\gamma)
=
\{(A,B):|H_{i,A,B}^{\rm ctrl}|\ge\gamma R\}.
\]

If these graphs satisfy the global allocation theorem, all unary source
certificates disappear value by value.

## 5. External macro geometry is closed

After unary cleaning, witnesses producing the same forbidden slot-value pattern
are grouped into one rank-two or rank-three event. The weighted local lemma
charges total incident probability rather than raw geometric descriptions.

The internal events leave residual slot budget

\[
\frac1{48}-\frac{5}{8\gamma\sqrt R}.
\]

At the slab-optimal scale, the branch proves `o(1)` incident mass for:

- every patch-only cross-macro pair event;
- all-movement and all-refill triples by gcd sums;
- every mixed patch triple by divisor factorization;
- every ordinary two-slot source-anchor pair by congruence and divisor-square
  sums.

Thus controller-aware global allocation alone would produce the required
`Omega(m^0.525)` saturated patch.

## 6. Failure structure

A bad controller-aware entry consists of a typed final label, a controller edge,
and a noncontroller source blocker pair. Positive-density failure forces one of:

1. **blocker star:** one source point lies on `Omega(m^0.475)` distinct blocker
   pairs;
2. **resource matching:** `Omega(m^0.525)` bad entries have distinct labels and
   controllers and endpoint-disjoint blocker pairs, with no controller reused as
   a selected blocker endpoint.

The resource alternative contains a matching-layer endpoint bank. The blocker
star is aligned with the alternating neutralisation bank.

## 7. Endpoint trades and monotone termination

For endpoint set

\[
R_0=\{(x_i,y_i):i\in[q]\}
\]

in one permutation layer, replace it by

\[
R_\pi=\{(x_i,y_{\pi(i)}):i\in[q]\}.
\]

This preserves every old row and column count. For the fixed controller-entry
universe, the controller-shadow potential satisfies

\[
\Psi(S_\pi)-\Psi(S)
=
\mathcal I(\pi)-\mathcal C(R_0),
\]

where `C` is removal credit and `I` is inserted shadow. A resource bank of size
`q` guarantees

\[
\mathcal C(R_0)\ge q.
\]

Every successful trade strictly decreases a fixed nonnegative integer potential
while preserving all controller pools. Therefore any uniform improvement theorem
terminates automatically; a separate anti-cycling argument is unnecessary.

## 8. Resource-bank source validity is closed

The resource bank initially has size

\[
Q=\Omega(m^{21/40}).
\]

Assume its endpoint unary forbidden density is `o(1)`. Thin to

\[
q=m^\kappa,
\qquad
0<\kappa<\frac1{40}.
\]

The branch then constructs a saturation-preserving no-three endpoint permutation
using four ingredients.

1. **Endpoint-host regularisation.** Delete high forbidden-degree tied indices;
   the remaining source-safe host is superregular.
2. **Permutation local lemma.** Remove unary cells, transpositions, anchored
   directed transitions, and directed 3-cycles while retaining `O(q^-r)`
   conditioned spread.
3. **Transition factorization.** Anchored path `i->j->k` satisfies

   \[
   (u-x_i)(v-y_k)=(u-x_j)(v-y_j),
   \]

   so divisor counting and `o(q)` endpoint pruning make transition resource mass
   `o(1)`.
4. **Support-rank thinning.** Rank-four anchored pairs and support-rank `4,5,6`
   inserted triples have unique-completion bounds and total normalized mass
   `o(1)` at `kappa<1/40`.

Therefore source admissibility of the resource endpoint trade is no longer open.

## 9. Protecting credit and eliminating diffuse insertion shadow

For each selected resource entry, replacement cells that directly recreate its
designated blocker incidence lie on one nonaxis line and form a partial matching
in the endpoint rectangle. Let `d_rec` be the maximum row or column degree of the
simple union of these recapture cells.

After direct recapture is removed, let:

- `d_1` be the maximum endpoint-resource degree of cells with any positive
  residual unary insertion shadow;
- `d_2` be the maximum endpoint-resource degree of compatible cell pairs with
  any positive residual binary insertion shadow.

Each positive support is forbidden once, regardless of witness multiplicity. The
permutation local lemma gives a source-admissible endpoint trade with

\[
\mathcal I(\pi)=0
\]

whenever

\[
\boxed{
d_{\rm rec}+d_1=o(q),
\qquad
d_2=o(q^2).
}
\]

Because the removal credit is positive, this is a strict controller-shadow
improvement. Diffuse weighted collateral is therefore closed exactly, not merely
in expectation.

## 10. Current exact bottleneck

Only support-concentrated conversion remains.

### Direct route

Prove the controller-aware graphs `J_i^ctrl(gamma)` satisfy the complementary-
degree global allocation criterion.

### Blocker-star route

Convert the forced `m^0.475` blocker star by an alternating, endpoint, rectangle,
cycle, or tomographic trade with negative controller-shadow change.

### Resource route

If the zero-cost permutation endpoint fails, one of the following explicit
concentrations exists:

1. dense unary endpoint source shadow;
2. rich designated-credit recapture fibre;
3. unary insertion-shadow fibre;
4. binary insertion-shadow star.

A successful conversion either lowers the monotone potential or directly creates
the dense controller-aware allocation needed by the macro theorem.

The branch does not yet prove this final conversion theorem and therefore does
not prove the no-three-in-line conjecture.

## 11. Constant-width side analysis

The older width-two matching-block route remains diagnostic. It proves exact
36-state banks, clean-state packing criteria, deletion-aware profiles, and
rank-at-most-three blocker-demand CSPs. It also records that independent deletion
does not cover additional blockers at prime-gap scale and that all stored raw
two-block extensions at sides eight through ten fail before patch-patch
interactions.

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
```

These are diagnostics or exact finite checks, not asymptotic proofs without the
stated classification theorems.