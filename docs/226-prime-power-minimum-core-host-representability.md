# Conditioning the full feasible cylinder makes minimum-core contraction host-representable

CMR910--CMR973 use exact set-family contraction whenever a prescription is common
to the current minimum face.  The minimum face alone need not be all perfect
matchings of one residual host.  There is a canonical repair.

Before contracting the common prescription, condition the complete feasible
family on it.  The conditioned cylinder contains every old minimum state and is a
subfamily of the old feasible family.  Hence it has the same minimum value and
exactly the same minimum face.  Contracting the conditioned cylinder, rather than
only the face, produces a genuine residual matching system whose induced minimum
face is the contracted old face.

For one matching layer this is the ordinary endpoint-deleted bipartite host.  For
two layer-disjoint permutation layers it is the exact residual joint system:
remove the prescribed matching endpoints in their own layers and keep every
prescribed physical cell forbidden to the opposite layer.

Let `\mathcal F` be a nonempty finite feasible state family with potential
`\Phi`, minimum value `m`, and minimum face `\mathcal M`.  Let `P` be a compatible
labelled prescription satisfying

\[
P\subseteq R
\qquad
\text{for every }R\in\mathcal M.
\]

Define the full conditioned family

\[
\mathcal F_P
=
\{R\in\mathcal F:P\subseteq R\}.
\]

## 1. Conditioning preserves exactly the old minimum face

### Theorem CMR974 -- PROVED

The conditioned family is nonempty and

\[
\boxed{
\min_{R\in\mathcal F_P}\Phi(R)=m.
}
\]

Its minimum face is exactly

\[
\boxed{
\mathcal M(\mathcal F_P)=\mathcal M.
}
\]

### Proof

Every old minimum contains `P`, so `\mathcal M\subseteq\mathcal F_P` and the
conditioned minimum is at most `m`.  Since `\mathcal F_P\subseteq\mathcal F`, it
cannot be below `m`.  A conditioned state of value `m` is an old minimum, and
every old minimum is conditioned. ∎

No state outside the old minimum face is promoted to minimum.

## 2. Exact induced minimum after contraction

Put

\[
\mathcal F_P/P
=
\{R\setminus P:R\in\mathcal F_P\}
\]

and define

\[
\Phi_P(R')=\Phi(P\cup R').
\]

### Theorem CMR975 -- PROVED

Restriction is the exact bijection

\[
\boxed{
\mathcal F_P
\cong
\{P\}\times(\mathcal F_P/P),
}
\]

and

\[
\boxed{
\mathcal M/ P
=
\operatorname*{argmin}_{R'\in\mathcal F_P/P}\Phi_P(R').
}
\]

The induced minimum value remains `m`.

### Proof

Every conditioned state contains `P`, so removing and adjoining it are inverse.
Apply CMR974 and transport the objective through this bijection. ∎

Thus minimum-core contraction may always be performed inside a complete
conditioned cylinder.

## 3. One-layer matching-host representation

Let `H=(L,R;E)` be a balanced bipartite host and let `P` be a compatible partial
matching.  Write `H-P` for the host obtained by deleting the source and target
vertices covered by `P`.

### Theorem CMR976 -- PROVED

The perfect matchings of `H` containing `P` factor exactly as

\[
\boxed{
\{M\in\operatorname{PM}(H):P\subseteq M\}
\cong
\{P\}\times\operatorname{PM}(H-P).
}
\]

Consequently, if `P` is common to the minimum face of `\operatorname{PM}(H)`, the
contracted minimum face is exactly the minimum face of the residual host `H-P`
for the induced objective.

### Proof

A perfect matching containing `P` matches every covered source to its prescribed
target.  Restriction to the uncovered vertices is a perfect matching of `H-P`.
Conversely adjoining `P` reconstructs the unique full matching.  Apply CMR975. ∎

This does not require `P` to be essential in the full host.

## 4. Two-layer joint matching representation

Let a feasible joint state be an ordered pair `(M_0,M_1)` of perfect matchings in
labelled layer hosts `H_0,H_1`, with no shared physical grid cell.  Let

\[
P=P_0\sqcup P_1
\]

be a compatible labelled partial joint state: each `P_\ell` is a partial matching
in layer `\ell`, and the two parts use disjoint physical cells.

For each layer, remove the source and target vertices covered by `P_\ell`.  In the
remaining layer host, additionally forbid every physical cell used by
`P_{1-\ell}`.  Retain the ordinary residual layer-disjointness condition between
the two remaining matchings.  Call the resulting joint system `\mathcal J/P`.

### Theorem CMR977 -- PROVED

Conditioned joint states factor exactly:

\[
\boxed{
\{(M_0,M_1)\in\mathcal J:P\subseteq M_0\sqcup M_1\}
\cong
\{P\}\times(\mathcal J/P).
}
\]

If `P` is common to the joint minimum face, its contraction is the minimum face
of `\mathcal J/P` for the induced objective.

### Proof

In each layer, restriction removes the prescribed matching endpoints.  A
residual matching cannot use a prescribed cell of the opposite layer, so those
cells are forbidden explicitly.  All remaining physical disjointness conditions
are unchanged.  Adjoining `P_0,P_1` is inverse to restriction.  Apply CMR975. ∎

The residual layer sides may differ when `|P_0|\ne|P_1|`; the exact joint-state
bijection remains valid.

## 5. Conditioning respects exact product factors

Suppose

\[
\mathcal F
=
\{C\}\times\prod_{a\in A}\mathcal F_a
\]

on disjoint factor edge classes, and write

\[
P=P_C\sqcup\bigsqcup_aP_a.
\]

### Theorem CMR978 -- PROVED

The conditioned family is the exact product

\[
\boxed{
\mathcal F_P
=
\{C\}\times
\prod_{a\in A}(\mathcal F_a)_{P_a},
}
\]

provided `P_C\subseteq C`; it is empty otherwise.  After contraction, each
nonempty local prescription contracts in its own factor, while fixed-core parts
remain fixed.

### Proof

Containment of `P` is equivalent to independent containment of every local part
because the factor edge classes are disjoint. ∎

Thus conditioning a common minimum prescription does not destroy an existing
exact product representation.

## 6. The induced triple potential is transported exactly

### Theorem CMR979 -- PROVED

Under any of the contractions CMR975--CMR978, every original physical triple `T`
contributes to the induced objective through the residual prescription

\[
T\setminus P.
\]

In particular:

- triples contained in `P` become constants;
- triples meeting `P` become rank-one or rank-two anchored prescriptions;
- pure and mixed residual triples retain the exact low-rank box decomposition of
  CMR958--CMR965.

### Proof

For every conditioned state `P\cup R'`,

\[
T\subseteq P\cup R'
\iff
T\setminus P\subseteq R'.
\]

Apply the rank classification of CMR962. ∎

No geometric conflict is discarded by host reconstruction.

## 7. Iterated minimum-core contraction stays representable

Start from a one-layer host, a joint two-layer host system, or an exact product of
such systems.  At every step let `P_i` be any compatible prescription common to
the current minimum face.  Condition the complete current feasible family on
`P_i`, contract it, and use the induced objective.

### Theorem CMR980 -- PROVED

Every step has a complete residual host or joint-product representation of the
forms CMR976--CMR978.  The contracted old minimum face is exactly the minimum face
of that residual system.

If the initial state cardinality is `k`, the sum of contracted ranks satisfies

\[
\boxed{
\sum_i|P_i|\le k.
}
\]

### Proof

Apply CMR974--CMR979 inductively.  Each contraction lowers residual state
cardinality by its prescription rank, so the total cannot exceed `k`. ∎

This removes the host-representability caveat for contractions made common on the
minimum face, provided the full conditioned cylinder is retained.

## 8. Host-representable minimum-core endpoint

### Corollary CMR981 -- PROVED

Every minimum-face common prescription arising from fixed-edge, coupling-atom,
anchored-fibre, target-pair, or added-edge contraction has an exact continuation:

1. condition the complete current matching or joint-state cylinder on the
   prescription;
2. retain exactly the same minimum face and value;
3. contract to a genuine residual host or exact residual product;
4. transport every triple as a constant, pure conflict, or low-rank anchored/mixed
   prescription;
5. continue with strictly smaller residual state cardinality.

Therefore host representability is no longer an obstruction for minimum-core
contractions themselves.  The remaining structural frontier is fixed-interface
and envelope transport: control certificates which stay in the conditioned core,
and prove that repeated wall/child/envelope descent reaches a zero-potential
state or spends a finite target/reserve budget.

### Proof

Combine CMR974--CMR980 with the minimum-core contraction sources CMR910--CMR973.
∎

No all-`n` theorem is claimed.  Conditioned minimum faces, induced contraction,
one-layer matching cylinders, joint two-layer residual systems, factorwise
conditioning, potential transport, and iterated rank budgets are checked in
[`scripts/verify_prime_power_minimum_core_host_representability.py`](../scripts/verify_prime_power_minimum_core_host_representability.py).
