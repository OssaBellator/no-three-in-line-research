# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

The collision-free theorem ledger is split across

- `proofs/composite-modulus-theorem-index-live.md` through CMR747;
- `proofs/composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `proofs/composite-modulus-theorem-index-live-continuation-2.md` from CMR870.

## Established normal forms

- Same-value host expansions roll back exactly; lowering or infeasible-base
  expansions peel to added minimum-core contraction or strict improvement.
- Between contractions, normalized same-vertex-set hosts form nested decreasing
  chains.
- Minimum-core contraction is host-representable after conditioning the complete
  current cylinder on the common prescription.
- Exact protected/free, routing, unit-wall, essential-core, exchange-SCC and child
  products retain original geometric coordinates.
- Cross-factor triples are constants, pure one-factor atoms, or low-rank Cartesian
  coupling boxes.
- Physical restorations and edge lineages are owner-independent.

## Selected-minimum mode

For an actual minimum state `S`, every restriction preserving `S` preserves one
minimum. A chosen target and compatible labelled prescription can be forced using
at most

\[
2n^2-2n
\]

outside-anchor deletions. Exact contraction preserves minimum status for the
induced objective.

Routing recurrence is unnecessary on this selected path. At each factor host,
restrict immediately to the routing skeleton of one actual minimum. The resulting
child product is exact and every nonempty child has strictly smaller side.

Define

\[
\mathcal A(d)=\sum_{m=1}^{d}(2m^2+m+1).
\]

One selected strict-descent path has at most `mathcal A(d)` normalized host/routing
stages.

## Target banks and robust geometry

The targets of a dirty minimum form a 3-uniform hypergraph. For every `q>=2`,
either there are `q` physically disjoint targets or a cell cover of size at most
`3(q-1)`. The cover branch concentrates at least

\[
\left\lceil\frac{\Phi(S)}{3(q-1)}\right\rceil
\]

targets on one selected cell.

A disjoint target bank has a degree-two Hall escape destroying at least
`ceil(q/2)` targets simultaneously. A positive-gap target-destroying state which
loses load `D` and lies `g>=1` above the minimum creates at least `D+g` new
triples.

New triples split by physical entry rank:

- rank one gives a loaded old line or simultaneous secant star;
- rank at least two gives an entering pair with many third cells on one nonaxis
  line.

Simultaneous common-layer, cross-layer and loaded-line banks have direct protected
executions. No-growth large cores enter exact product descent.

## Parameter-free finite stocks

On the selected path, the branch-wide protected capacity is

\[
\mathfrak P_{\min}(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}2m(2m^2+m+1).
\]

The fresh deletion-root stock is

\[
\mathfrak D_{\min}(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}2m^2(2m^2+m+1).
\]

Canonical minimum-loss witnesses are permanent and distinct inside one normalized
segment. A coarse complete-branch stock is

\[
\mathfrak L(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}
(2m^2+m+1)(2m+1)(2m^2-2m).
\]

Rolled-back banks have a greedy missing-edge cover of size at most `2N^2`,
independent of bank cardinality. Returned cover edges are bulk-redeleted while the
stored minimum anchor survives.

A contracted core either reconditions and recontracts while its lifted anchor
survives, yields strict improvement, exposes a real missing anchor edge, contracts
an added core edge, or enters strict structural descent.

## Blocker covers and unit walls

If a blocker cover meets every perfect matching of a response graph, deleting the
cover destroys matchability and gives a Hall-deficient cut.

For an inclusion-minimal blocker cover `C`, every Hall witness `X` with
`Y=N_{G-C}(X)` satisfies

\[
C=E(G)\cap(X\times(R\setminus Y)),
\qquad
|X|-|Y|=1.
\]

Restoring any one blocker makes it essential. Its matching family factors exactly
as

\[
\operatorname{PM}(G_e)
\cong
\{e\}
\times
\operatorname{PM}(G_A)
\times
\operatorname{PM}(G_B),
\qquad a+b=n-1.
\]

Thus complete bank blockage is a strict unit-wall descent, not an arbitrary
terminal inventory.

## Universal and small-factor banks

Every active fixed target or loaded line in side at least four has a degree-two
full-layer response bank. A feasible response enters the minimum scheduler; a
fully blocked response gives the unit-wall descent.

Side three is exact: for every opposite permutation and target edge absent from
it, one 3-cycle contains the target edge and the other 3-cycle is the unique
response matching.

Side two is physically rigid. The two disjoint layers cover the complete `2x2`
board; a root side-two state is clean, while a residual side-two block conditions
and contracts into the induced fixed interface. Side-one factors are forced or
empty.

Every target surviving only in a small fixed interface has a canonical last-active
edge and a unique lifted response-bank owner of side at least three, unless the
whole root is the clean side-two base.

## Finite selected-scheduler response

After erasing exact duplicate bank attempts, same-value rollbacks, repeated
reconditioning and repeated unchanged skeleton selections, every nontrivial
canonical episode consumes finite owner, protected, deletion, loss, blocker-cover
or contraction currency, or strictly descends.

This proves finite response and structural descent. It does **not** prove that the
minimum value becomes zero.

## Critical nonclosure correction

A finite response tree can terminate at a dirty conditioned anchor when every
escape state has higher potential. The abstract family

\[
\Phi(S)=1,
\qquad
\Phi(Q_1)=\Phi(Q_2)=2
\]

already demonstrates this: both responses may destroy the old target and create
two replacements, while `S` remains the positive minimum. Conditioning on `S` can
produce a dirty singleton with the same induced minimum.

Therefore finite currency exhaustion, unit-wall descent and small-factor
classification are supporting reductions, not a minimum-zero proof.

For a response state `Q`, put

\[
L(Q)=|\mathcal T(S)\setminus\mathcal T(Q)|,
\qquad
N(Q)=|\mathcal T(Q)\setminus\mathcal T(S)|.
\]

The exact identity is

\[
\Phi(Q)-\Phi(S)=N(Q)-L(Q).
\]

A response distribution forces improvement only when

\[
\mathbb E N(Q)<\mathbb E L(Q).
\]

## Corrections retained

- Sequential two-layer rematching may reoccupy an old first-layer cell.
- Historical target lines and stars are not simultaneous families.
- One edge return may serve several neutralisations in one absence run.
- Removing one essential edge gives Hall deficiency exactly one.
- Aggressive batch deletion is branch-local.
- Differently masked leaf unions are not automatically one matching host.
- An empty intersection host has no assigned minimum.
- Conditioning on one support edge does not fix the other two layer labels of a
  physical target; four assignment classes are required.
- A one-layer line-clean cylinder does not itself remove an opposite-layer selected
  cell.
- Static token membership is not called restoration payment until an edge returns.
- Finite scheduler termination is not called potential improvement.

## Current open frontier

1. **Global target-versus-collateral inequality.** Construct canonical response-bank
   weights satisfying
   \[
   \sum_Bw_B\,\mathbb E_BN(Q)
   <
   \sum_Bw_B\,\mathbb E_BL(Q),
   \]
   or explicitly exhibit a lower-potential state.
2. **Lifted fixed-interface accounting.** Include anchored rank-zero/rank-one/rank-
   two collateral without double counting across unit-wall, child and envelope
   owners.
3. **Prime-field and thin regimes.** Establish the required weighted inequality in
   prime-field and low-height quotient/carry cases.
4. **Arbitrary side lengths.** Complete balanced-prime and CRT assembly while
   controlling mixed local-line/collision collateral.

## Bottom line

There is no complete proof. Through **CMR1197**, response banks, routing,
rollbacks, protected growth, blocker covers, unit walls, small factors and lifted
interface ancestry have finite canonical forms. The remaining problem is a genuine
quantitative inequality comparing destroyed targets with created collateral—not an
uncontrolled recurrence or terminal matching obstruction.
