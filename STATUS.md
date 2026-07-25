# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

A July 2026 result proves the corresponding eventual maximum `kn` for every
fixed `k>=3`; the saturated `k=2` case addressed here remains exceptional.

## Established platform

The notebook contains proved lemmas or exact conditional endpoints for:

- saturated two-per-row/column decomposition into two perfect-matching layers;
- clone-space, permutation, and superregular perfect-matching selection;
- protected rectangle, tomographic, cycle, subgroup, and endpoint trades;
- exact fixed- and variable-reservoir patch expectations;
- binary and multistate rank-at-most-three forbidden-box CSPs;
- weighted local-lemma and fixed-rank spread endpoints;
- modular-hyperbola, carry, quotient, gcd, divisor, Ramsey, and incidence
  structure;
- exact finite certificate verification and small exhaustive searches.

The principal non-prime-patching route still lacks its second-generation
alternating-bank concentration/termination theorem and final carry absorber.

## All-n prime-patching track

### Slab-optimal macro architecture

Every saturated source decomposes into two matching layers. Consecutive
column-slab pools give

```text
macro variables M = m^(1/20+o(1))   = m^0.05
pool size R       = m^(19/20+o(1))  = m^0.95
macro width W     = m^(19/40+o(1))  = m^0.475
total width MW    = m^(21/40+o(1))  = m^0.525.
```

The branch proves matching-pool supply, exact degree restoration, internally
no-three square-root macros, conditioned fixed-rank spread, and exponent
optimality within disjoint `O(sqrt(R))` macro architectures.

### Controller-aware domains and external geometry

Every final numerical row and column must be used. Fixed-core safety is
insufficient because unselected active-pool edges remain in the source.
Controller-aware safety tests every blocker pair against the full source and
permits a candidate value only when its controller deletion clears every unary
source obstruction.

At the slab-optimal scale, every patch-only cross-macro class and every ordinary
two-slot source-anchor class has `o(1)` incident probability mass. Thus any
saturation-compatible controller-aware allocation gives an
`Omega(m^0.525)` saturated patch.

### Dynamic excess-shadow potential

Positive controller shadow produces either:

1. a source-endpoint blocker star of size `Omega(m^0.475)`; or
2. `Omega(m^0.525)` resource-disjoint bad entries with distinct labels,
   controllers, and endpoint-disjoint blocker pairs.

Within-pool endpoint permutations preserve the pool coordinate sets and complete
candidate-cell universe. Every candidate has one automatic controller-containing
axis blocker. Therefore

\[
\Xi(S)=\sum_z\bigl(b_S(z)-1\bigr)
\]

is a nonnegative pairing-invariant excess-shadow potential. Every pool-compatible
trade satisfies an exact insertion-cost-minus-removal-credit identity for `Xi`.
Uniform improving trades terminate automatically.

## Four direct allocation interfaces

Let `rho_i(A)` and `chi_i(B)` be the movement-row and refill-column nondegree
upper bounds obtained from controller-cell defects and same-slot anchor counts.
Let `kappa(B)` be the average refill score.

The branch has four separate allocation mechanisms.

1. **One-sided bottleneck versus refill slack.** Direct allocation follows when
   ```text
   r_score <= min_B Lambda_score(B).
   ```
   Failure gives an exact capacitated movement-label Hall set paired with a refill
   label whose cumulative local slack is too small.
2. **Deterministic two-sided ownership.** Route exactly `W` movement labels and
   `W` refill labels to every macro. Local Ore matching succeeds when
   `r+s<=W`.
3. **Random two-sided ownership.** Hypergeometric sampling succeeds when every
   macro nonedge has
   ```text
   rho_i(A)+chi_i(B) <= T-m^(23/80+o(1)).
   ```
4. **Random one-sided ownership.** The average-refill complementary-degree
   criterion succeeds when
   ```text
   rho_i(A)+kappa(B) <= T-8*sqrt(T log T).
   ```

Sparse exceptional macro-label pairs are routable. A direct obstruction must
survive all four mechanisms.

### Anchor-energy localization

The complete same-slot anchor mass across all disjoint active pools satisfies

\[
\sum_{i,A,B}u_i(A,B)=O(m^{2+o(1)}).
\]

Combining this divisor-energy bound with the exact ownership Hall rectangle
shows that an anchor-driven ownership failure cannot have a middle-sized Hall
set. At the PP3of threshold it is either:

- a sublinear exceptional label cluster; or
- a macro rejecting all but a sublinear label set.

Diffuse or positive-density anchor Hall rectangles are therefore closed.

## Source-valid resource trades

A resource bank of size `Q=Omega(m^0.525)` may be thinned to a growing subbank.
Under sparse unary source shadow, endpoint-host pruning, a permutation local
lemma, transition divisor regularisation, and support-rank thinning produce a
saturation-preserving no-three endpoint trade.

The thinning may be chosen adaptively so that:

- the unary forbidden graph has `o(q)` edges;
- the anchored transition family has `o(q)` events;
- deleting all their incident indices costs only `o(q)` endpoints;
- the remaining fully source-valid derangement has one-cell probabilities
  `(1+o(1))/q`.

Source admissibility of the resource endpoint is therefore closed with a
near-uniform one-cell law.

## Zero-unary Hall and binary endpoints

Direct recapture cells and residual unary-shadow cells are deleted from one
source-safe endpoint host `G_0`. Failure of a perfect matching is exactly a Hall
rectangle

\[
|X|+|Y|>q,
\qquad
X\times Y\subseteq E(\overline{G_0}).
\]

A macroscopic rectangle contains a quadratic core of one witness type.

Every binary conflict can be covered by deleting one of its endpoint cells. The
fractional minimum resource congestion has:

- factor-two threshold rounding;
- an exact LP dual weighted-conflict packing;
- Hall inheritance under low-congestion deletion.

One nonaxis witness line has a congestion-one cover. A family with `o(q)`
witness-line overlap is also absorbed. The remaining original binary-shadow
objects are a linear-congestion dual packing or a high-overlap witness-line
pencil.

## Recapture-line rectangle conversion

Naive one-survivor deletion cannot absorb a linear bank of linear-rich distinct
geometric lines. The owner lines must move.

Adaptive thinning preserves a positive-density Hall target core jointly with all
source-validity diagnostics. Failed owner-line improvement yields a
near-extremal typed incidence system. Szemerédi--Trotter and a multiplicity split
then produce a positive linear family of nonaxis lines with:

- at least `q^(1/3-delta)` resource-disjoint owner/replacement cells per line;
- at least `q^(1-delta)` Hall-target cells per line;
- total typed multiplicity `Omega(q^2)`.

Pairing the two matching traces on each line gives `Omega(q^3)` alternating
rectangle candidates. A resource-degree bound extracts `Omega(q)` pairwise
row/column-disjoint rectangle blocks.

Rectangle extraction is therefore closed.

## Superregular rectangle installation

For a small linear cross-safe rectangle bank in a superregular endpoint host:

- reserving its resources leaves a residual perfect matching;
- the residual matching may be chosen source-valid;
- the residual matching may also be chosen with low insertion-shadow base cost
  whenever its unary/binary expected shadow is small relative to rectangle
  credit;
- each rectangle is an exact two-state `2 by 2` permutation block;
- all remaining no-three constraints form a binary rank-at-most-three CNF;
- exact insertion shadow is a degree-at-most-two pseudo-Boolean cost.

Diffuse geometric clause mass and diffuse paid cost are closed by first moment,
variable local lemma, support cleaning, or weighted thinning.

## Signed binary rectangle endpoint

After unit preprocessing, ternary clauses have vanishing density and may be
removed on a growing subbank. Colouring each variable pair by its complete
sixteen-valued forbidden-state signature and applying fixed-colour Ramsey gives
a growing homogeneous subbank.

Its paid capacity is exact.

- If `(1,1)` is allowed, the all-cross state is geometrically valid and directly
  protects one designated credit unit per rectangle.
- If `(1,1)` is forbidden but `(0,0)` is allowed, every valid homogeneous
  assignment has at most one cross-oriented rectangle. This signature is
  explicitly credit-poor.
- If both diagonal state pairs are forbidden, three rectangles already form an
  unsatisfiable core.

A dense all-cross conflict graph is geometric. It yields a rich cross line, a
large pencil through one selected rectangle cell, or—after homogeneous Ramsey
refinement—a complete fixed-anchor secant design.

Sparse all-cross unary support and sparse all-cross binary support contain a
growing zero-cost subbank. Weighted unary `o(K)` and binary `o(K^2)` cost likewise
produce a growing `o(K)`-cost subbank. The residual matching base cost may be
selected simultaneously with source validity by a paid superregular first
moment.

Thus arbitrary dense Boolean satisfiability, common-line rectangle extraction,
residual matching, residual source validity, and diffuse paid collateral are no
longer separate open problems.

## What remains conditional

The remaining conversion theorem has the following structured forms.

1. Convert an ownership Hall/slack core, a two-sided threshold gap, or the
   simultaneous score concentration surviving all four allocation interfaces.
2. Convert a Hall rectangle or a matchable but non-superregular zero-unary host
   outside the superregular recapture branch.
3. Convert a credit-poor homogeneous rectangle signature, a rich cross line or
   pencil, a complete fixed-anchor secant design, or a constant-size signed
   contradiction.
4. Convert linear unary, quadratic binary, or residual weighted shadow
   concentration at the rectangle-credit scale.
5. Convert a linear-congestion original binary-shadow dual packing or
   witness-line pencil.
6. Build source-admissible pool-compatible trades with `Xi` insertion cost below
   their star/resource removal credit.

## Important cautions

- Unused numerical labels cannot be discarded and compressed while preserving
  saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- A source-endpoint blocker star is not automatically a common-candidate star.
- A single rich line has bounded cover congestion, but a linear bank of
  linear-rich distinct lines need not.
- The superregular rectangle theorems do not cover every matchable sparse host.
- Finite diagnostics validate identities and expose obstructions; they do not
  prove the asymptotic conversion theorem.

## Bottom line

There is no complete proof. The branch closes matching supply, exponent-optimal
macro width, saturation-compatible allocation interfaces, external weighted
geometry, source-valid near-uniform resource trades, low-congestion binary
covering, exact ownership Hall/slack cores, recapture-line rectangle extraction,
superregular residual installation, signed binary-CSP regularization, and
diffuse paid rectangle selection. The structured concentration cases above
remain open.