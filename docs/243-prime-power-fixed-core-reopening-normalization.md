# A contracted minimum core reconditions or exposes a lost anchor edge

CMR974--CMR981 make minimum-core contraction host-representable: first condition
the complete current cylinder on a compatible prescription `P`, then contract.
The remaining concern is reopening.  A later full-parent or structural response
may again permit states which omit `P`.

Minimum-anchor mode gives an exact normalization.  Store the lifted minimum state
`S` which contained `P`.  If `S` remains feasible in the later host, restrict again
to states containing `P`; this preserves the same minimum and restores the exact
conditioned cylinder.  If `S` is not feasible, some labelled edge of `S` is absent
from the later host and is a canonical loss witness.  A lower-valued later state is
strict improvement.

The theorem concerns host-representable one-layer or joint two-layer families on a
common ambient labelled state model.  Routing classes are always selected from the
stored anchor as in CMR1094, so routing relabelling alone cannot exclude `S`.

Let `F(H)` be the feasible family of a labelled host `H`, let `Phi` be the physical
triple potential, and choose

\[
S\in\mathcal F(H),
\qquad
\Phi(S)=m=\min_{R\in\mathcal F(H)}\Phi(R).
\]

Let `P subseteq S` be compatible and common to the current minimum face after a
minimum-preserving forcing pass.  The conditioned family is

\[
\mathcal F(H)_P
=
\{R\in\mathcal F(H):P\subseteq R\}.
\]

## 1. The lifted anchor survives exact contraction

### Theorem CMR1110 -- PROVED

Restriction and contraction give the exact bijection

\[
\mathcal F(H)_P
\cong
\{P\}\times\bigl(\mathcal F(H)_P/P\bigr),
\]

and the residual anchor `S-P` is minimum for the induced objective

\[
\Phi_P(R')=\Phi(P\cup R').
\]

The original state `S` is therefore a canonical lift of every later comparison
with the contracted branch.

### Proof

This is CMR906 and CMR974--CMR981. ∎

## 2. Surviving anchors recondition the old core

Let `H'` be a later host on the same ambient labelled state model.  Assume
`S in F(H')`.

### Theorem CMR1111 -- PROVED

If

\[
\min_{R\in\mathcal F(H')}\Phi(R)\ge m,
\]

then equality holds and the restricted family

\[
\mathcal F(H')_P
=
\{R\in\mathcal F(H'):P\subseteq R\}
\]

contains `S` with minimum value `m`.  It contracts host-representably on `P` with
induced minimum anchor `S-P`.

### Proof

The surviving state `S` has value `m`, so the later minimum is at most `m`; the
hypothesis gives equality.  Restricting to the `P`-containing subfamily preserves
`S`, hence preserves one minimum by CMR902.  Apply the conditioned-host contraction
of CMR974--CMR981. ∎

Thus states which omit `P` may be discarded on the selected minimum path whenever
the stored anchor survives.

## 3. A lower later minimum is strict improvement

### Theorem CMR1112 -- PROVED

If

\[
\min_{R\in\mathcal F(H')}\Phi(R)<m,
\]

then the later host supplies strict physical-potential improvement.  No reopening
ancestry is charged.

### Proof

The objective is the same physical triple potential on lifted states. ∎

## 4. Failure of the stored anchor exposes a real host loss

Assume `S notin F(H')`.  The state `S` remains a valid labelled matching or joint
state on the ambient vertices; feasibility in `F(H')` fails only through absence
of at least one required host edge.

### Theorem CMR1113 -- PROVED

There exists

\[
\boxed{f\in S\setminus E(H').}
\]

Choose the first such edge in the stored anchor order.  It is a canonical
lost-minimum witness.  Exactly one of the following holds:

1. `f in P`, so reopening the contracted core pays a core-edge loss;
2. `f in S\setminus P`, so the residual lifted anchor pays an ordinary anchor loss.

### Proof

A feasible matching state is contained in its host.  If every edge of `S` belonged
to `H'`, the same valid labelled state would be feasible there, contrary to the
assumption.  The displayed partition is exhaustive. ∎

No owner label can replace the physical missing-edge witness.

## 5. Same-value added edges do not reopen the core

### Theorem CMR1114 -- PROVED

Suppose `H'` is obtained from a host containing the conditioned cylinder by adding
edges, and the minimum value remains `m`.  Then the canonical expansion response
rolls back all added edges, after which the old `P`-conditioned cylinder and its
contraction remain valid.

If the expansion lowers the minimum, use CMR1112.  If its base is infeasible, an
added edge enters the new minimum core and contracts.

### Proof

Apply CMR952.  In the feasible same-value case the exact response is rollback to
the base.  The other cases are lowering improvement/contraction and infeasible-base
contraction. ∎

Hence restoration-only activity cannot reopen a contracted dirty interface for
free.

## 6. Repeated reopening attempts consume the loss stock

### Theorem CMR1115 -- PROVED

Along a normalized selected minimum execution, every attempted reopening of a
stored prescription `P` reaches at least one of:

1. reconditioning and exact recontraction by CMR1111;
2. strict improvement by CMR1112;
3. one canonical missing edge of the stored lifted anchor by CMR1113;
4. added-edge minimum-core contraction by CMR1114;
5. strict factor, wall, or envelope exit.

In branch 3, the witness is permanent inside the current normalized restriction
segment and is charged to CMR1103--CMR1106.

### Proof

Compare the later host with the stored lifted anchor.  If the anchor survives, use
CMR1111 or CMR1112 according to the minimum value.  If it fails, use CMR1113.
Normalize any added batch by CMR1114.  Structural vertex-set changes give the last
branch. ∎

## 7. Branch-wide reopening bound

### Theorem CMR1116 -- PROVED

Before strict improvement, added-core contraction, or structural exit, the number
of nontrivial fixed-core reopening attempts which are not immediately
reconditioned is at most the branch-wide loss stock

\[
\boxed{\mathfrak L(N,h)}
\]

from CMR1106.

### Proof

Every such attempt produces a canonical missing lifted-anchor edge by CMR1115.
Inside each normalized segment those witnesses are distinct and permanent by
CMR1103, and CMR1106 sums their complete owner-labelled stock. ∎

Immediate reconditioning attempts are idempotent and may be erased from a shortest
canonical history.

## 8. Fixed-core reopening endpoint

### Corollary CMR1117 -- PROVED

Fixed-core reopening is not an independent unbounded branch.  A contracted target
or interface on the selected minimum path:

1. remains conditioned and contracted while its stored anchor survives;
2. rolls back same-value added edges;
3. yields strict improvement if a lower minimum appears;
4. pays one permanent lost-anchor edge if the stored lift fails;
5. contracts an added minimum-core edge; or
6. enters strict factor/wall descent, envelope expansion, or finite base handling.

Combined with the parameter-free routing, protected-growth, deletion-root, and
minimum-loss stocks CMR1094--CMR1109, the remaining prime-power frontier is the
final global scheduler splice: prove that every dirty selected minimum invokes one
of these finite responses before the finite structural descent tree is exhausted.

### Proof

Combine CMR1110--CMR1116. ∎

No all-`n` theorem is claimed.  Lifted-anchor survival, reconditioning, missing-edge
witnesses, rollback, and reopening-stock arithmetic are checked in
[`scripts/verify_prime_power_fixed_core_reopening.py`](../scripts/verify_prime_power_fixed_core_reopening.py).
