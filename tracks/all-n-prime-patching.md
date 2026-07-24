# All-n route A: prime-size patching

**Branch:** `research/all-n-prime-patching`

This branch is independent of the other all-`n` strategies. It assumes a
saturated no-three-in-line theorem is eventually proved on `(p-1)x(p-1)` grids
for all sufficiently large primes `p`, and asks how to extend such a
construction to nearby side lengths.

Prime-gap information alone is not sufficient: embedding a `2m`-point solution
in an `n x n` grid leaves `2(n-m)` missing points. The essential theorem is an
exact row-column-preserving extension absorber.

The focused recent theorem list is
[`proofs/prime-patching-recent-index.md`](../proofs/prime-patching-recent-index.md).
Detailed chapters for the current route are `docs/27` through `docs/55`.

## PP1 — Boundary extension interface

### Status: PROVED for saturation; geometry separated into PP2

The row-column bookkeeping is exact:

- for `t>=2`, two edge-disjoint permutation graphs on the new `t x t` corner add
  exactly `2t` points without changing the old core;
- for `t=1`, every boundary-only degree state is either a corner splice or a
  two-edge strip switch;
- the complete `t=1` list has only `2m^2-m` candidates;
- geometric validity is exactly the avoidance of retained-pair blockers,
  retained-anchor/new-pair triples, and internal patch triples.

## PP2 — Exact selection endpoints

### Status: OPEN geometrically; exact selection closed in several forms

The branch now contains:

- pair-aware and arbitrary-reservoir clone-space local lemmas;
- concrete cell, pair, and internal-triple load thresholds;
- internally clean spread-bank endpoints;
- exact state-dependent deletion expectations PP2l--PP2o;
- binary and finite-state bad-box CSP formulations;
- first-moment, bounded-dependency, and exact SAT/backtracking solvers.

For active clone size `N>=200`, the arbitrary-reservoir bounds

```text
u_* <= N/200,
pi_* <= N^2/1600,
tau_* <= N^3/3200
```

suffice. Failure forces one of those local loads to be large. The missing work is
geometric preparation, not row-column degree selection.

## PP3 — Robust seed preparation

### Status: OPEN, with matching availability and width-two internal geometry closed

### Earlier positive components

The branch proves:

- deletion-aware one-strip averaging and the finite one-strip obstruction;
- exact row-lift banks with sequential and static local-lemma endpoints;
- projection obstructions and quantitative forced-triple bounds;
- component-clean movement/refill factorization;
- internally no-three parabolic rungs of square-root width;
- sheared parabolic finite-state spread;
- cycle-reservoir 2-SAT and protected rectangle-trade CNF selection;
- multistate rank-at-most-three bad-box first-moment and LLL endpoints;
- reverse old/new ordering, eliminating repeated-component cross-rung triples.

### Matching-density correction

The hoped-for positive-density conditioning of independent sheared old-column
and old-row boxes is impossible in an arbitrary saturated source. If their
maximum coordinate marginals are `alpha,beta`, matching-admissible probability
is at most

\[
\frac{m\alpha\beta}{t}.
\]

For linear-size offset boxes at square-root width this is `O(m^-1/2)`, not a
positive constant. Matching admissibility must correlate row and column choices
through actual source edges.

### Matching-first bank

Every saturated source incidence graph decomposes into two perfect matchings.
Choosing one layer and a uniform `2t`-edge subset gives exactly

\[
2\binom m{2t}
\]

layer-labelled matching reservoirs with hypergeometric all-rank spread:

```text
source-edge deletion marginal       t/m
old-coordinate inclusion marginal   2t/m
rank-r coordinate cylinder          (2t)_r/(m)_r
```

Thus matching availability is closed for every saturated source.

### Universal endpoint-adapted width-two rung

Every four-edge matching reservoir supports a canonical internally no-three
width-two patch. Sort its four columns and rows; pair the two smaller coordinates
on the first new line and the two larger on the second. Internal nonaxis secants
have positive slope, while movement-refill secants have negative slope.

For the matching-first random canonical rung:

- every patch cell has probability at most `4/m`;
- every same-component pair has probability at most `12/[m(m-1)]`;
- source-edge-aligned retained-anchor events cancel through the deletion;
- anchored patch-pair defects are bounded by an absolute constant;
- only nonaxis retained-pair blockers can grow with `m`.

### Matching-block multistate variables

Let `E` be an `r`-edge matching block and reserve one width-two interval. A state
chooses four edges to delete and patches their endpoints. Retaining the unchosen
block edges makes every state have identical row and column margins.

The canonical family has `binom(r,4)` states. The full family retains all 36
width-two geometries for every deletion and has

\[
36\binom r4
\]

states. Before clean-domain conditioning, the full bank has bounds

```text
patch cell                         <= 2/r
ordinary same-block pair           <= 4/[r(r-1)]
same-edge movement/refill pair     <= 1/r
distinct-edge movement/refill pair <= 3/[r(r-1)].
```

If a clean fraction `delta` survives, these bounds lose only a factor `1/delta`.

### Local clean-domain endpoint

For the canonical block let `B` count retained-pair blocker signatures, `A_1`
same-edge anchored-pair signatures, and `A_2` ordinary anchored-pair signatures.
Put

\[
\Lambda(E)=
\frac{4|B|}{r}
+
\frac{4|A_1|}{r}
+
\frac{12|A_2|}{r(r-1)}.
\]

Then

\[
|\Omega_{\rm clean}(E)|
\ge
(1-\Lambda(E))\binom r4.
\]

Hence `|B|=o(r)`, `|A_1|=o(r)`, and `|A_2|=o(r^2)` preserve a `1-o(1)` clean
fraction. Failure forces a linear blocker core, linear same-edge anchor core, or
quadratic ordinary-anchor core.

### Clean-rung packing

Locally clean four-edge deletions form a 4-uniform hypergraph on the block edges.
If it has `h` hyperedges and maximum vertex degree `Delta`, it contains a matching
of size at least

\[
\left\lceil\frac{h}{4\Delta}\right\rceil.
\]

If a large matching does not exist, a small source-edge transversal hits every
clean state. That core is an explicit target for protected rectangle or
tomographic trades.

On the stored certificates, the canonical clean hypergraph always has matching
number one and transversal at most two. Retaining all 36 geometries breaks this
obstruction: stored sides eight, nine, and ten contain two disjoint locally clean
width-two reservoirs in each tested layer.

### Global seven-profile endpoint

For `K` disjoint `r`-edge blocks with clean-domain density at least `delta`, every
remaining triple has one of seven profiles:

- `N_1`: two fixed points and one patch cell;
- `N_h`: one fixed point and one same-edge patch pair;
- `N_2`: one fixed point and one ordinary patch pair;
- `N_11`: one fixed point and cells from two blocks;
- `N_h1`: a same-edge pair plus a cell from another block;
- `N_21`: an ordinary pair plus a cell from another block;
- `N_111`: cells from three distinct blocks.

A complete patch exists if

\[
\frac{2N_1+N_h}{\delta r}
+
\frac{8N_2}{\delta r^2}
+
\frac{4N_{11}+2N_{h1}}{\delta^2r^2}
+
\frac{16N_{21}}{\delta^2r^3}
+
\frac{8N_{111}}{\delta^3r^3}
<1.
\]

Alternatively, if every block variable occurs in at most

\[
\frac{\delta r+12}{18}
\]

bad boxes, the bounded-dependency endpoint applies.

### Prime-gap-scale block target

A constant-width ladder needs `K=T/2` width-two rungs. For the published target
`T=m^0.525`, partitioning one matching layer into `K` blocks gives the natural
scale

\[
K\asymp m^{0.525},
\qquad
r\asymp m^{0.475}.
\]

Each unpruned block then has `m^{1.9+o(1)}` canonical states and 36 times as many
full states.

The remaining theorem is now precise: construct blocks at this scale with

1. polynomial or constant clean-domain density `delta`;
2. a diffuse clean-deletion hypergraph packing `K` disjoint reservoirs;
3. small nonaxis blocker and anchor signature loads;
4. PP3ci profile counts below the displayed thresholds, or block occurrence
   `O(delta r)`;
5. protected trades neutralizing any small transversal core.

### Refuted or blocked shortcuts

- recursive boundary-only one-strip extension dies before side five;
- the original unconditioned one-strip shadow average is universally vacuous;
- unpruned row-lift first moment cannot scale;
- aligned off-diagonal block doubling is impossible;
- conditioning full small row-lift banks does not yield spread clean components;
- independent sheared row/column boxes cannot have positive constant
  matching-admissible density at sublinear width;
- canonical matching-block cleanliness already fails for one five-edge no-three
  matching;
- on the stored layers, canonical clean states are pinned to a one- or two-edge
  transversal and cannot provide two disjoint rungs;
- unrestricted rectangle repair to depth two gives no stored extension from
  source side seven onward.

The older row-lift and larger correlated-parabolic alternatives remain valid.

## PP4 — Prime-gap transfer theorem

### Status: PROVED UNDER PP2--PP3

If every sufficiently large `n` has a solved size `m` with

\[
0\le n-m\le w(m),
\]

then a prepared-seed extension of width `w(m)` gives `D(n)=2n` for every
sufficiently large `n`.

For solved sizes `m=p-1`, the published Baker--Harman--Pintz exponent `0.525`
requires width `m^(0.525+epsilon)` or a fixed-factor `C m^0.525` endpoint. A
polylogarithmic width does not currently give an unconditional transfer.

## PP5 — Finite exceptions

### Status: VERIFIER COMPLETE; CERTIFICATES VERIFIED FOR `2<=n<=10`

The exact verifier checks determinants, bounds, distinctness, point count, and
two points in every row and column. The eventual threshold and certificates
below it remain dependent on the asymptotic PP2--PP3 theorem.

## Computational tools added on this branch

- `verify_no_three_certificate.py`: exact certificate verifier;
- `search_boundary_extension.py`: prescribed-degree extension CSP;
- `analyze_reservoir_patch_loads.py`: exact arbitrary-reservoir loads;
- row-lift enumeration, projection, static, and sequential analyzers;
- parabolic matching and parameter sweeps;
- variable-reservoir, cycle-factorization, 2-SAT, binary, and multistate solvers;
- one- and two-rectangle repair searches;
- `analyze_matching_first_reservoirs.py`: exact matching-first decomposition and
  hypergeometric spread;
- `verify_universal_width_two_rung.py`: exhaustive adjacent-rung verifier;
- `analyze_matching_first_width_two.py`: canonical external-defect split;
- `analyze_matching_block_states.py`: clean-domain pruning diagnostics;
- `analyze_matching_block_loads.py`: PP3ca signature loads;
- `analyze_clean_rung_hypergraph.py`: exact clean-state packing and transversal;
- `analyze_full_width_two_block_bank.py`: all 36 geometries and packing data.

## Completion criterion

This branch is complete only when PP2 and PP3 provide a width large enough for
PP4, followed by verified PP5 coverage below the resulting threshold. It now
closes exact extension interfaces, matching availability, endpoint-adapted
width-two internal geometry, equal-margin state banks, local clean-density and
packing endpoints, and an explicit global profile inequality. It still lacks
the correlated secant-shadow preparation theorem and does not prove the
no-three-in-line conjecture.