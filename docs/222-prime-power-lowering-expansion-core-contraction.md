# Every lowering expansion contains a contractible added edge

CMR934--CMR941 show that a same-value expansion is exactly rollbackable.  It
remains to understand an expansion which strictly lowers the current minimum.
Every state at the new lower level uses at least one added edge, because the old
host contained no state of that value.

Apply the minimum-face edge dichotomy to the added batch.  An added edge omitted
by some new minimum may be deleted while preserving the new minimum value.  If
all added edges could be deleted this way, the old host would still contain a
state at the lower value, a contradiction.  Hence before the batch is exhausted,
one added edge belongs to every surviving new minimum state and contracts exactly.

Thus an expansion has only two structurally relevant outcomes: same-value
rollback or strict minimum-face contraction.  If the lower value is already the
desired global potential improvement, the scheduler may stop earlier.

Let `H\subseteq H'` be hosts on fixed labelled vertex sets, let

\[
A=H'\setminus H,
\]

and assume both feasible state families are nonempty with

\[
m(H')<m(H).
\]

Put `m'=m(H')`.

## 1. The added batch hits every new minimum

### Theorem CMR942 -- PROVED

Every state `R\in\mathcal M(H')` uses at least one edge of `A`:

\[
\boxed{R\cap A\ne\varnothing.}
\]

### Proof

A state avoiding `A` is contained in `H'-A=H` and would be feasible in the old
host.  If it had value `m'<m(H)`, this would contradict the definition of
`m(H)`. ∎

Hence `A` is an edge transversal of the new minimum face.

## 2. Avoidable added edges peel without raising the new minimum

Let `G` be any intermediate host with

\[
H\subseteq G\subseteq H'
\]

and `m(G)=m'`.  Let `e\in G\setminus H`.

### Theorem CMR943 -- PROVED

If some state of `\mathcal M(G)` omits `e`, then

\[
\boxed{m(G-e)=m'}
\]

and

\[
\boxed{
\mathcal M(G-e)
=
\{R\in\mathcal M(G):e\notin R\}.
}
\]

### Proof

The omitting minimum state survives deletion, so the new value is at most `m'`.
Restriction cannot lower a minimum, so equality holds.  Apply CMR926 for the face
identity. ∎

This is a minimum-preserving peel of one added edge.

## 3. Peeling must encounter a minimum-core edge

Order the added edges as `A=(a_1,...,a_s)`.  Start with `G_0=H'`.  At step `i`,
if some current minimum omits `a_i`, set `G_i=G_{i-1}-a_i`; otherwise stop.
Edges already absent are skipped.

### Theorem CMR944 -- PROVED

The procedure stops before all edges of `A` are deleted.  At the stopping step,
the current added edge `a_i` belongs to every state of
`\mathcal M(G_{i-1})`.

### Proof

CMR943 preserves value `m'` after every peel.  If all added edges were deleted,
the final host would be `H` and would still have minimum `m'`, contradicting
`m(H)>m'`.  Therefore a first unpeelable added edge exists, and unpeelability is
exactly common containment in the current minimum face. ∎

## 4. The stopping edge contracts exactly

### Theorem CMR945 -- PROVED

Let `e` be the first unpeelable added edge from CMR944 and let `G` be the current
host.  Then

\[
e\in E_{\min}(G)
\]

and restriction gives the exact set-family factorisation

\[
\boxed{
\mathcal M(G)
\cong
\{e\}
\times
\bigl(\mathcal M(G)/e\bigr).
}
\]

Residual state cardinality decreases by one, and every residual state has induced
potential `m'`.

### Proof

The edge belongs to every current minimum state by CMR944.  Apply CMR912 to this
common edge and restrict the induced objective. ∎

The edge need not be essential in the complete perfect-matching host; it is
essential in the current minimum face.

## 5. Exact peel/contraction budget

### Theorem CMR946 -- PROVED

A lowering expansion with added batch `A` reaches an added-edge minimum-core
contraction after at most

\[
\boxed{|A|-1}
\]

minimum-preserving peels.  Counting the final contracted edge, at most `|A|`
added-edge responses are used.

### Proof

Each peel removes one distinct edge of `A`.  CMR944 stops before all are removed.
∎

## 6. Record improvement or structural descent

Fix a record potential value `r`, the smallest value reached before the expansion.

### Theorem CMR947 -- PROVED

For a lowering expansion `H\subseteq H'`, at least one of the following holds.

1. `m(H')<r`, giving a new strict global record improvement.
2. `r\le m(H')<m(H)`, and CMR944--CMR946 produce exact contraction of one added
   edge while preserving the new minimum value.

### Proof

Compare `m(H')` with `r`.  In the second case apply the lowering-expansion
contraction theorem. ∎

Thus a decrease which only recovers an earlier potential band still pays strict
residual-cardinality descent.

## 7. Mixed transitions inherit the same contraction

Let `H_0,H_1` be arbitrary same-vertex-set hosts and put `K=H_0\cap H_1`.  Assume
`\mathcal F(K)` is nonempty and

\[
m(H_1)<m(K).
\]

### Theorem CMR948 -- PROVED

The expansion factor `K\subseteq H_1` contains an added edge from
`H_1\setminus H_0` which becomes common to the peeled minimum face and contracts
exactly after at most

\[
|H_1\setminus H_0|-1
\]

peels.

### Proof

Apply CMR942--CMR946 to the expansion from `K` to `H_1`.  Its added batch is
`H_1\setminus K=H_1\setminus H_0`. ∎

If `\mathcal F(K)` is empty, the transition already has the lost-old-minimum
witness of CMR937.

## 8. Lowering-expansion endpoint

### Corollary CMR949 -- PROVED

Every same-vertex-set host expansion reaches at least one of:

1. same-value exact rollback;
2. new record potential improvement;
3. minimum-preserving peeling followed by exact contraction of an added edge;
4. a lost-old-minimum witness in the restriction factor of a mixed transition;
5. contraction, owner/factor/wall descent, or envelope change.

Consequently no added-edge batch can produce a nonimproving, noncontracting
minimum-face transition.  The remaining dynamic branch consists of monotone
restriction, minimum-loss ancestry, and structural vertex-set changes.

### Proof

Use CMR934--CMR948. ∎

No all-`n` theorem is claimed.  Added-batch transversality, minimum-preserving
peeling, forced stopping, exact contraction, record-level alternatives, and mixed
transition transfer are checked in
[`scripts/verify_prime_power_lowering_expansion_contraction.py`](../scripts/verify_prime_power_lowering_expansion_contraction.py).
