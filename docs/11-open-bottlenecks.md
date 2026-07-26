# Open bottlenecks and research roadmap

## 1. Current proof status

The no-three-in-line conjecture remains open.  The branch now has a large finite
response and structural-descent theory, but no theorem yet forces a positive
minimum of the real-triple potential to become zero.

The central correction is CMR1190--CMR1197:

> finite scheduler termination is not potential improvement.

A dirty minimum may have only higher-valued escape states.  Restriction and exact
contraction can terminate at a dirty singleton with the same positive induced
objective.  Every completion claim must therefore exhibit an actual lower-
potential state or an averaging inequality which guarantees one.

## 2. What is structurally closed

The proved chain now includes the following normal forms.

1. **Inherited banks and envelopes, CMR123--CMR218.**  Parent banks, Hall walls,
   essentiality, exchange ancestry, and closure envelopes.
2. **Line, carry and token geometry, CMR219--CMR438.**  Primitive heights, thin
   signatures, line-clean cylinders, stars, walls, packets, token return, and
   cycle erasure.
3. **Rollback and exact products, CMR439--CMR690.**  SCC factorisation, mixed
   cycles, compatible paid pairs, protected/free products, child routing,
   essential-core recursion, and forced-certificate escape.
4. **Target and return normalization, CMR691--CMR893.**  Finite owner stocks,
   target handoff, unit Hall walls, protected line reserves, global restoration
   ancestry, completeness branching, and support concentration.
5. **Minimum-face dynamics, CMR894--CMR989.**  Disjoint leaf compression,
   minimum-anchor forcing, minimum-core deletion/contraction, complete host
   transition normalization, cross-factor potential transport, host-
   representability, and physical target handoff.
6. **Robust target geometry, CMR990--CMR1093.**  Positive-gap surplus, corrected
   four-assignment signatures, entry-rank line/star decompositions, simultaneous
   common/cross-layer execution, target-hypergraph packing, and protected capacity.
7. **Parameter-free selected scheduler, CMR1094--CMR1141.**  Minimum-selected
   routing, permanent minimum-loss witnesses, fixed-core reconditioning,
   parameter-free blocker covers, and finite response currencies.
8. **Terminal matching structures, CMR1142--CMR1189.**  Linear Hall walls,
   inclusion-minimal unit blocker walls, fixed-target and loaded-line degree-two
   banks, side-three exact responses, side-two rigidity, and lifted small-interface
   target ancestry.

No local routing, rollback, blocker, wall, loaded-line, small-factor, or owner-reset
recurrence remains anonymous.

## 3. Principal bottleneck: target versus collateral

For a selected minimum `S` and response state `Q`, define

\[
L(Q)=|\mathcal T(S)\setminus\mathcal T(Q)|,
\qquad
N(Q)=|\mathcal T(Q)\setminus\mathcal T(S)|.
\]

The exact identity is

\[
\Phi(Q)-\Phi(S)=N(Q)-L(Q).
\]

A probability distribution on a response bank forces strict improvement only when

\[
\boxed{
\mathbb E N(Q)<\mathbb E L(Q).
}
\]

The missing global theorem must produce this inequality for at least one canonical
bank or a weighted combination of banks.

### Required weighted form

A sufficient statement is the existence of nonnegative weights `w_B`, not all
zero, such that

\[
\boxed{
\sum_Bw_B\,\mathbb E_BN(Q)
<
\sum_Bw_B\,\mathbb E_BL(Q).
}
\]

The bank classes have already been reduced to a finite list:

- active residual target banks;
- lifted fixed-core target banks;
- loaded-line banks;
- simultaneous common-layer and cross-layer star banks;
- minimal blocker unit-wall children;
- side-three singleton responses;
- rigid side-one/two induced interfaces.

## 4. Remaining technical bottlenecks

### Fixed-interface collateral accounting

A response may destroy one active target while creating triples using contracted
core edges.  The next theorem must count these anchored rank-zero, rank-one and
rank-two contributions without charging the same physical triple at several
factor, wall, envelope or lifted-owner levels.

A promising owner is the canonical last-active edge of CMR1182--CMR1189.  Assign
every created triple to the last of its three edges to become active or fixed.
This should give a disjoint ancestry partition of collateral.

### Bank averaging after blocker factorisation

An infeasible response bank minimalizes to a deficiency-one Hall wall.  Restoring
one blocker gives an exact product with child-side sum `n-1`.  The weighted
inequality must be stable under this product split:

- either one child bank has negative expected new-minus-lost value;
- or cross-child coupling atoms contribute a separately bounded correction.

CMR958--CMR973 supply the exact coupling boxes needed for this calculation.

### Prime-field and thin regimes

The selected response-bank construction is not intrinsically prime-power, but the
available collateral estimates still use prefix height, carry, full-token and
closure-envelope structure.  Prime-field and height-one owners need a replacement
weighting or an explicit finite bank inequality.

### CRT assembly

Synchronized CRT saturation is exact, but real triples can project as
collision/collision, collision/local-line, local-line/collision, or
local-line/local-line.  A final assembly theorem must retain these local line and
carry signatures; the invalid local modular-arc premise cannot be used.

## 5. Open lemmas in recommended order

1. **Canonical collateral owner.**  Partition every created physical triple by one
   last-active edge/owner so no collateral is counted twice.
2. **One-bank expectation.**  Compute exact or upper-bounded `E N(Q)` for the
   degree-two fixed-target bank, including fixed-core anchored triples.
3. **Target matching bank inequality.**  Average the simultaneous escape from a
   disjoint target family and compare its destroyed load with rank-split collateral.
4. **Unit-wall stability.**  Prove the weighted target-collateral inequality is
   inherited by at least one strict child of a minimal blocker wall.
5. **Small-interface closure.**  Show rigid side-one/two interfaces contribute only
   owner-assigned anchored collateral already counted at their lifted bank owner.
6. **Prime-field/thin endpoint.**  Establish the weighted inequality without a
   nonroot prefix-depth budget.
7. **CRT weighted assembly.**  Combine local inequalities while controlling mixed
   collision and local-line signatures.

## 6. Computational priorities

- Enumerate complete response banks for small sides and record the exact pair
  `(L(Q),N(Q))`, split by residual/core rank and line ownership.
- Solve linear programs for nonnegative bank weights satisfying strict expected
  target advantage.
- Test whether last-active-edge ownership makes all collateral classes disjoint.
- Measure the correction caused by low-rank cross-factor coupling boxes under
  unit-wall and child products.
- Enumerate side-three and side-four fixed-target banks with arbitrary fixed-core
  prescriptions, not only pure residual targets.
- Test synchronized CRT products using the full four-pattern projection taxonomy.

## 7. Current proved endpoint

Through **CMR1197**:

- selected routing is fixed directly from an actual minimum;
- same-vertex-set losses and fixed-core reopenings have finite parameter-free
  stocks;
- rolled-back banks have finite missing-edge covers;
- minimal covers are exact deficiency-one unit walls;
- fixed targets and loaded lines have executable-or-wall response banks;
- side three has an exact response and root side two is clean;
- small fixed-interface targets have lifted response-bank owners;
- finite response is explicitly separated from the missing minimum-decrease
  inequality.

There is still no complete proof.  The next genuine advance must be a quantitative
target-versus-collateral inequality, not another recurrence bound.
