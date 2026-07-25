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
- modular-hyperbola, carry, quotient, gcd, divisor, and incidence structure;
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

The branch now has four separate allocation mechanisms.

### 1. One-sided ownership bottleneck versus refill slack

For a balanced movement-label ownership, define the minimum possible maximum row
score

\[
r_{\rm score}
=
\min_\sigma\max_A\rho_{\sigma(A)}(A).
\]

For refill label `B`, define cumulative local slack

\[
\Lambda_{\rm score}(B)
=
\sum_i(W-\chi_i(B))_+.
\]

If

\[
\boxed{
r_{\rm score}
\le
\min_B\Lambda_{\rm score}(B),
}
\]

then a global label matching exists. This is threshold-free and deterministic.
A failure returns an exact capacitated ownership Hall set and a refill label whose
total local slack is below the ownership bottleneck.

Under a fixed refill-label margin,

\[
\Lambda_{\rm score}(B)
\ge
T-
\frac{
\sum_iA_i+\sum_iV_i(B)
}{\delta R}.
\]

Hence global rather than worst-macro excess-shadow and same-slot anchor mass
controls the refill side.

### 2. Deterministic two-sided ownership

Assign exactly `W` movement labels and exactly `W` refill labels to every macro.
If the two ownership score thresholds satisfy

\[
\boxed{r+s\le W,}
\]

then every induced `W by W` macro compatibility graph has a perfect matching by
the bipartite Ore theorem.

Both ownership hosts have exact capacitated Hall criteria. Sparse exceptional
macro-label pairs can therefore be routed around independently on the two label
sides.

### 3. Random two-sided ownership

Independent random balanced partitions sample every global nondegree down by the
factor `W/T`. If every macro nonedge satisfies

\[
\rho_i(A)+\chi_i(B)
\le
T-h,
\]

with

\[
h=2T\sqrt{\frac{\log(4MT)}W}
=m^{23/80+o(1)},
\]

then all induced macro graphs simultaneously satisfy local Ore and admit perfect
matchings.

### 4. Random one-sided ownership

The earlier complementary-degree theorem remains available. Global allocation
follows whenever every incompatible triple satisfies

\[
\rho_i(A)+\kappa(B)
\le
T-8\sqrt{T\log T}.
\]

Diffuse excess shadow is therefore sufficient, but uniform smallness is no
longer required. A direct obstruction must survive routing, cumulative slack,
two-sided local matching, per-macro complementary degree, and average refill
complementary degree simultaneously.

## Exact ownership failure objects

At threshold `r`, a balanced acceptable movement ownership exists exactly when

\[
W|N_M(X)|\ge|X|
\]

for every numerical-label set `X`. Failure gives an all-bad score rectangle

\[
X\times([M]\setminus N_M(X)).
\]

A middle-sized Hall set produces a positive-density label-by-macro rectangle;
a very large Hall set produces at least one nearly dead macro column; and a small
Hall set is an explicit exceptional-label cluster.

Thus isolated bad macro-label pairs are not terminal. The direct numerical
obstruction is a capacitated Hall/slack core or a score concentration surviving
all four allocation architectures.

## Source-valid resource trades

A resource bank of size `Q=Omega(m^0.525)` may be thinned to a growing subbank.
Under sparse unary source shadow, endpoint-host pruning, a permutation local
lemma, transition divisor regularisation, and support-rank thinning produce a
saturation-preserving no-three endpoint trade.

The thinning can be chosen adaptively so that:

- the unary forbidden graph has `o(q)` edges;
- the anchored transition family has `o(q)` events;
- deleting all their incident indices costs only `o(q)` endpoints;
- the remaining fully source-valid derangement has one-cell probabilities
  `(1+o(1))/q`.

Source admissibility of the resource endpoint is therefore closed with a
near-uniform, rather than merely constant-factor, one-cell law.

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
witness-line overlap is also absorbed. The remaining binary objects are a
linear-congestion fractional dual packing or a high-overlap witness-line pencil.

## Rich-line conversion endpoint

Naive one-survivor deletion cannot absorb a linear bank of linear-rich distinct
geometric lines: the survivor-cover volume forces linear resource congestion.
The owner lines must move.

For the Hall-derived target set, adaptive thinning preserves a fixed positive
quadratic density jointly with every source-validity diagnostic. Under the
near-uniform source-valid derangement, the owner-line potential either strictly
decreases or the assignment incidence system is near extremal:

\[
H_0=(1+o(1))|\mathcal A|,
\qquad
\mathcal W=(1-o(1))q|\mathcal A|.
\]

Applying Szemerédi--Trotter to the `q^2` typed owner/replacement lines converts
the near-extremal alternative into one nonaxis geometric line carrying

\[
\Omega(q^{1/3})
\]

pairwise resource-disjoint owner/replacement endpoint cells and their owner
candidate points.

The former second-generation grid-rich pencil is therefore reduced to one common
geometric carrier suitable for a protected line, rectangle, cycle, or
tomographic trade.

## What remains conditional

The remaining conversion theorem has the following structured forms.

1. Convert an ownership Hall/slack core, a two-sided threshold gap, or the
   simultaneous complementary-score concentration surviving all four direct
   allocation interfaces.
2. Convert a Hall rectangle or a matchable but non-superregular zero-unary host
   outside the recapture-line class.
3. Convert the common nonaxis line matching from PP3oc.
4. Convert a linear-congestion binary dual packing or witness-line pencil.
5. Build source-admissible pool-compatible trades with `Xi` insertion cost below
   their star/resource removal credit.

Diffuse weighted residuals, external completion energy, source validity of the
resource endpoint, sparse exceptional labels, isolated rich fibres, raw
binary-fan size, naive rich-line covering, dynamic controller relabelling, and
termination are no longer separate open problems.

## Important cautions

- Unused numerical labels cannot be discarded and compressed while preserving
  saturation.
- Fixed-core domains do not handle unselected active-pool edges.
- A source-endpoint blocker star is not automatically a common-candidate star.
- A single rich line has bounded cover congestion, but a linear bank of
  linear-rich distinct lines need not.
- Finite diagnostics validate identities and expose obstructions; they do not
  prove the asymptotic conversion theorem.

## Bottom line

There is no complete proof. The branch closes matching supply, exponent-optimal
macro width, saturation-compatible allocation interfaces, external weighted
geometry, source-valid near-uniform resource trades, low-congestion binary
covering, direct controller-defect routing, exact ownership Hall/slack cores, and
rich-line reduction to a common-line matching. The structured conversion cases
above remain open.
