# Every fixed-owner edge deletes against the minimum face or contracts

CMR902--CMR909 show that one actual minimum-potential state can be preserved
through all outside-anchor deletions.  A recurrent physical edge need not be part
of the current target.  The correct object is therefore the complete face of
minimum-potential states.

At one fixed owner, every labelled edge has an exact dichotomy.  Either some
minimum state avoids it, in which case deleting the edge preserves a minimum, or
every minimum state contains it, in which case it belongs to the common minimum
core and contracts exactly.  After contracting the whole common core, the
residual minimum family has empty core, so every residual edge is avoidable by
another minimum state.

This closes the fixed-owner, fixed-edge loop at the level of finite state
families.  The remaining issue is dynamic and geometric: owner changes can alter
the feasible family and its minimum face, and a contracted set-family face need
not itself be representable as all perfect matchings of one residual host.

Let `\mathcal F` be a nonempty finite equal-cardinality family of labelled
saturated states and let

\[
m=\min_{R\in\mathcal F}\Phi(R).
\]

Define the minimum face

\[
\mathcal M(\mathcal F)
=
\{R\in\mathcal F:\Phi(R)=m\}.
\]

## 1. The minimum face is the complete set of preserved witnesses

### Theorem CMR910 -- PROVED

The family `\mathcal M(\mathcal F)` is nonempty.  A restriction
`\mathcal A\subseteq\mathcal F` contains a state of potential `m` if and only if

\[
\mathcal A\cap\mathcal M(\mathcal F)\ne\varnothing.
\]

### Proof

Finiteness gives a minimum.  A state has potential `m` exactly when it belongs to
the displayed face. ∎

Thus preserving one member of the minimum face is equivalent to preserving the
current minimum value.

## 2. Exact edge dichotomy on the minimum face

Fix any labelled physical edge `e` in the ambient owner universe.

### Theorem CMR911 -- PROVED

Exactly one of the following holds.

1. **Minimum-avoiding branch.** Some `S\in\mathcal M(\mathcal F)` omits `e`.
   Then deleting `e` preserves the minimum value `m`.
2. **Minimum-core branch.** Every `S\in\mathcal M(\mathcal F)` contains `e`.
   Then `e` belongs to the common intersection
   \[
   E_{\min}
   =
   \bigcap_{S\in\mathcal M(\mathcal F)}S.
   \]

### Proof

Either the universal containment statement holds or it has a counterexample.
In the latter case that counterexample survives deletion of `e` and has potential
`m`.  The two cases are disjoint. ∎

The dichotomy is about the minimum face, not essentiality in the full matching
host.

## 3. Exact contraction of the complete minimum core

Put

\[
E_{\min}
=
\bigcap_{S\in\mathcal M(\mathcal F)}S
\]

and

\[
\mathcal M/E_{\min}
=
\{S\setminus E_{\min}:S\in\mathcal M(\mathcal F)\}.
\]

### Theorem CMR912 -- PROVED

Restriction gives the exact bijection

\[
\boxed{
\mathcal M(\mathcal F)
\cong
\{E_{\min}\}
\times
\bigl(\mathcal M/E_{\min}\bigr).
}
\]

If

\[
\Phi_{E_{\min}}(R')
=
\Phi(E_{\min}\cup R'),
\]

then every residual state has induced potential exactly `m`.

### Proof

Every minimum state contains the complete intersection.  Removing and adjoining
it are inverse.  The induced-potential statement is the definition of the
minimum face. ∎

The common core is a compatible partial joint state because it is contained in
every saturated state of the face.

## 4. Complete-core contraction leaves no residual fixed edge

### Theorem CMR913 -- PROVED

The residual minimum family has empty common core:

\[
\boxed{
\bigcap_{R'\in\mathcal M/E_{\min}}R'
=
\varnothing.
}
\]

Consequently every residual edge belonging to one residual minimum state is
omitted by another residual minimum state.

### Proof

An edge common to every residual state would lift to an edge common to every
original minimum state but absent from `E_{\min}`, contradicting the definition
of the complete intersection. ∎

This is the minimum-potential analogue of complete essential-core
normalisation.

## 5. Recurrent fixed-owner edges have an immediate response

Suppose an edge `e` is genuinely restored at the same labelled owner.

### Theorem CMR914 -- PROVED

Relative to the current minimum face, at least one exact action is available.

1. If `e\notin E_{\min}`, choose a minimum state avoiding `e` and delete `e`
   again while preserving the minimum value.
2. If `e\in E_{\min}`, contract `e` as part of the exact minimum-core
   factorisation CMR912, lowering residual state cardinality by one.

### Proof

Apply CMR911.  In the first branch the avoiding minimum state witnesses feasible
redeletion.  In the second branch common containment gives exact set-family
contraction. ∎

No target membership assumption is used.

## 6. Repeated noncore restoration is pure paid reopening

Fix one owner and suppose the minimum value remains `m`.  Let `e` be outside the
current minimum core whenever it is restored.

### Theorem CMR915 -- PROVED

Every restoration of `e` can be followed by a minimum-preserving redeletion.
Between `r` distinct deletion generations of `e` there are at least `r-1`
genuine physical restorations, carrying exact labelled nonroot full-token
incidence

\[
\boxed{
(r-1)(p+1)(h-1).
}
\]

After canonical redeletion, the minimum face is contained in the same
`e`-avoiding subfamily as before.  Thus the reopening creates no new minimum-face
structural state unless some other edge, owner, or envelope datum changes.

### Proof

CMR914 gives redeletion against an avoiding minimum state.  Distinct deletion
generations require intervening zero-to-one transitions.  CMR413 gives the token
identity.  Reimposing the same deletion restores the same edge constraint. ∎

## 7. Minimum-core growth has finite rank

Consider a nested sequence of minimum-value subfamilies

\[
\mathcal M_0\supseteq\mathcal M_1\supseteq\cdots
\]

obtained by minimum-preserving deletions at one labelled owner.  Let

\[
E_i=\bigcap_{S\in\mathcal M_i}S.
\]

### Theorem CMR916 -- PROVED

The common cores are monotone:

\[
E_0\subseteq E_1\subseteq\cdots.
\]

If every state has cardinality `k`, then

\[
\boxed{|E_i|\le k}
\]

and strict core growth occurs at most `k` times.  Contracting every newly common
edge lowers the residual cardinality by the same total amount.

### Proof

Intersecting fewer states can only enlarge the intersection.  Every core is a
subset of every size-`k` state.  Distinct strict growth steps add at least one new
edge, and exact contraction removes exactly the accumulated core rank. ∎

For a saturated two-layer side-`n` state, `k=2n`.

## 8. Fixed-owner minimum-face endpoint

### Corollary CMR917 -- PROVED

At one fixed labelled owner, every repeatedly restored edge reaches at least one
of:

1. minimum-preserving redeletion;
2. exact minimum-core contraction and strict residual-cardinality descent;
3. repeated genuine restoration with exact full-token payment;
4. loss of the previous minimum value through strict potential improvement;
5. a change of another physical edge, the matching owner, factor, wall, or
   envelope.

Hence a fixed edge cannot remain an unresolved recurrence inside one unchanged
minimum face.  The residual prime-power problem is to control how minimum faces
and their common cores change across owner transitions, and to reconnect the
set-family minimum-core contraction with the geometric matching-host and target-
load ledgers.

### Proof

Combine CMR911--CMR916 with the owner-independent restoration and lineage results
CMR777--CMR829. ∎

No all-`n` theorem is claimed.  Minimum-face dichotomy, complete-core
contraction, residual core-freeness, restoration responses, and monotone core
growth are checked in
[`scripts/verify_prime_power_minimum_face_edge_dichotomy.py`](../scripts/verify_prime_power_minimum_face_edge_dichotomy.py).
