# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  The branch now has exact structural,
matching-bank and collateral-accounting reductions, but no theorem yet proves that
the resulting credit-reproduction system is subcritical for every inherited owner.

The critical honesty correction remains CMR1190--CMR1197:

> finite scheduler termination is not potential improvement.

The current advance is more quantitative.  CMR1198--CMR1317 replace the unspecified
bank-weight problem by explicit response-bank probabilities, pointwise local
collateral envelopes, unique live-credit ownership and an exact finite spectral
certificate target.

## 2. What is structurally closed

The proved chain includes:

1. **Inherited banks and envelopes, CMR123--CMR218.**  Parent banks, Hall walls,
   essentiality, exchange ancestry and closure envelopes.
2. **Line, carry and token geometry, CMR219--CMR438.**  Primitive heights, thin
   signatures, line-clean cylinders, stars, walls, packets and token return.
3. **Rollback and exact products, CMR439--CMR690.**  SCC factorisation, compatible
   paid pairs, protected/free products, child routing, essential-core recursion and
   forced-certificate escape.
4. **Target and return normalization, CMR691--CMR893.**  Finite owner stocks, target
   handoff, unit walls, protected line reserves, restoration ancestry, completeness
   branching and support concentration.
5. **Minimum-face dynamics, CMR894--CMR989.**  Minimum-anchor forcing, core
   deletion/contraction, complete host-transition normalization, cross-factor
   potential transport, host representability and target handoff.
6. **Robust target geometry, CMR990--CMR1093.**  Positive-gap surplus, corrected
   assignment signatures, entry-rank line/star decompositions, simultaneous
   execution, target-hypergraph packing and protected capacity.
7. **Parameter-free selected scheduler, CMR1094--CMR1197.**  Minimum-selected
   routing, permanent losses, fixed-core reconditioning, blocker covers, exact unit
   walls, small interfaces and the finite-response nonclosure correction.
8. **Exact target-collateral analysis, CMR1198--CMR1277.**  Permanent response-bank
   bounds, restricted feasibility penalties, corrected line energies, absolute
   entering-edge ownership, pointwise local envelopes, live-credit ledgers,
   reproduction matrices and rational Lyapunov certificates.
9. **Finite full-grid evidence, CMR1278--CMR1317.**  Standard/affine full-grid sides
   three through six have exact finite response classifications.  These statements
   are explicitly not transferred to scattered residual coordinates.

No local routing, rollback, blocker, wall, owner-reset or collateral-ownership
recurrence remains anonymous.

## 3. Exact current target: a subcritical offspring matrix

Every current physical triple is a live credit.  A newly created credit receives a
unique last-entering physical owner cell.  Targeting a parent credit class `sigma`
with a chosen feasible bank law creates an expected offspring vector.  Collecting
the rows gives a nonnegative matrix

\[
A_{\sigma\tau}=\mathbb E N_\tau(Q).
\]

A positive weighted potential decreases under every targeted response exactly when

\[
\boxed{Av<v.}
\]

For a finite nonnegative matrix this is equivalent to

\[
\boxed{\rho(A)<1.}
\]

A successful theorem may use an upper matrix `Ahat`; it is enough to show
`rho(Ahat)<1`.  The certificate can be exact and rational:

\[
\widehat Av\le v-\delta,
\qquad
v,\delta\in\mathbb Q_{>0}^{\Sigma}.
\]

After clearing denominators, this is a finite integer inequality.  Bounded omitted
collateral can be absorbed by the certificate slack.

## 4. Available row bounds

### Fixed-target permanent bound

For one degree-two response graph

\[
G=K_{n,n}\setminus(O\cup F),
\]

put

\[
\kappa_n=\left(\frac n{n-2}\right)^n\le16.
\]

A compatible rank-`r` prescription has probability at most

\[
\frac{\kappa_n}{(n)_r}.
\]

This gives an exact finite-bank upper row after enumerating the genuinely new
rank-one, rank-two and rank-three collateral atoms.

### Corrected line energy

For old state `S=O union M`, allowed response graph `G`, and
`M_G=M cap G`, the genuinely new atom counts are

\[
V_1=\sum_L\binom{o_L}{2}(g_L-m_L),
\]

\[
V_2=\sum_Lo_L\left(c_2(G_L)-\binom{m_L}{2}\right),
\]

\[
V_3=\sum_L\left(c_3(G_L)-\binom{m_L}{3}\right).
\]

The old-edge subtraction is mandatory.

### Pointwise local envelope

Every allowed response edge has

\[
\Lambda_S(a)
=
w_S(a)+\frac12\Delta_2(a)+\frac13\Delta_3(a),
\]

and every response matching satisfies

\[
N(Q)\le\sum_{a\in R}\Lambda_S(a).
\]

Row/column maxima give a distribution-free bank bound.  Failure of the resulting
improvement inequality forces a quantitatively loaded rank-one, rank-two or
rank-three line/star certificate.

### Target aggregation

The exact identity

\[
\sum_{e\in E(S)}D_S(e)=3\Phi(S)
\]

implies that, absent improvement or complete bank blockage, one target cell and one
absolute entering edge carry a local envelope of scale at least

\[
\frac{3\Phi(S)}{2n^2}.
\]

This is the current bridge from a global positive minimum to one local offspring
row.

## 5. Remaining technical bottlenecks

### Line/height/carry matrix construction

Partition last-entering owners by a finite signature containing enough information
to bound their rank-one, rank-two and rank-three line profiles.  Populate an honest
upper offspring matrix using:

- primitive line height and dyadic bands;
- prefix/full-token cells;
- carry signatures;
- loaded-line and secant-star absorption;
- unavailable-edge and Hall-wall exits.

The needed statement is not merely a large-line dichotomy.  The weighted sum of
all offspring classes in each row must be strictly below the parent weight.

### Product and wall triangularity

CMR1218 assigns every entering edge to one unique residual factor, but a physical
triple can touch several factors through fixed interfaces.  The next product lemma
must order credit classes so that the upper offspring matrix is block triangular,
or bound the off-diagonal interface block within the rational certificate slack.

CMR1273 gives constructive gluing once that ordering is proved.

### Scattered residual coordinates

The standard-grid side-three/four/five/six classifications are root/affine finite
theorems.  A residual factor may use scattered source and target coordinates in the
parent board.  Its real-line energy must be recomputed in those inherited
coordinates; the finite root tables cannot be imported by relabelling.

### Prime-field and thin regimes

The response-bank and spectral formalism is not intrinsically prime-power, but the
strongest row bounds still use nonroot prefix height, carry and envelope structure.
Height-one and remaining thin owners need direct finite rows or a replacement
signature system.

### CRT assembly

Synchronized CRT saturation is exact, but real triples project as
collision/collision, collision/local-line, local-line/collision or
local-line/local-line.  CRT offspring classes must retain these projection and
carry types.  The invalid local modular-arc premise cannot be used.

## 6. Open lemmas in recommended order

1. **Owner-signature matrix.**  Define a finite last-entering edge signature and
   prove that its row counts dominate every exact created triple once.
2. **Rank-two assignment bound by height.**  Bound `Delta_2(a)` using primitive-line
   height or prefix/carry classes rather than a raw maximum-weight matching.
3. **Rank-three rooted-star row.**  Convert `Delta_3(a)` into offspring classes whose
   weighted return is below the parent target credit or is absorbed structurally.
4. **Product triangularity.**  Order pure-child and anchored-interface credits so
   unit-wall and child products admit the CMR1273 gluing certificate.
5. **Rational certificate search.**  Enumerate finite rows on small inherited owners,
   solve for a candidate `v`, and export exact integer inequalities.
6. **Prime-field/thin certificate.**  Build the same rows without a nonroot prefix
   budget.
7. **CRT block assembly.**  Glue local matrices while controlling mixed collision
   and local-line offspring.

## 7. Computational priorities

- Enumerate exact offspring vectors, not only `(L,N)` totals, for fixed-target banks
  in inherited coordinate sets.
- Search for rational `v>0` satisfying `Ahat v<v`; clear denominators and retain the
  integer certificate and slack.
- Test height/carry coarse partitions for honest upper-matrix domination.
- Measure whether last-entering ownership makes cross-factor offspring genuinely
  block triangular.
- Extend standard-grid finite response searches cautiously; record equal-potential
  trap SCCs rather than extrapolating strict descent.
- Test synchronized CRT products using the complete four-pattern projection
  taxonomy.

## 8. Current proved endpoint

Through **CMR1317**:

- one fixed-target bank has explicit permanent and availability inequalities;
- every created triple has one absolute entering-edge and last-creation owner;
- corrected rank-split line energy and pointwise local envelopes are exact;
- optimized target-cell envelopes concentrate positive minima into quantitative
  line/star certificates;
- the weighting problem is exactly a finite spectral-radius problem with rational
  certificates;
- extension-free ambient response families have an exact matching description;
- standard full grids through side six have explicit finite classifications, with
  the side-six one-layer trap SCC and its two-layer clean escape recorded honestly.

There is still no complete proof.  The next genuine advance must prove a
subcritical offspring matrix in inherited coordinates, not merely add another
finite response or recurrence bound.
