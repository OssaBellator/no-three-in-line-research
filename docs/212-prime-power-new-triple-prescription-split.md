# A new target triple gives a constant-arity complete split

CMR830--CMR861 describe complete state exclusion through distinguishing rank and
exchange width. The target-driven scheduler has additional geometry. Every
nonimproving state which destroys a positive target family creates a genuinely
new collinear triple. Use that labelled triple as a rank-three prescription.

Every alternative state either omits one of the three labelled edges, giving one
of three single-edge deletion branches, or contains the whole triple. The latter
branch has a forced labelled conflict and enters the existing forced-certificate
handoff or exact factorisation. This preserves completeness with constant arity,
independently of the full matching distinguishing rank.

Let `\mathcal F` be a nonempty equal-cardinality family of labelled saturated
states, let `Q\in\mathcal F`, and let `C\subseteq Q` be any nonempty labelled
prescription. Put

\[
\mathcal F_C
=
\{R\in\mathcal F:C\subseteq R\}.
\]

## 1. Exact prescription split

### Theorem CMR862 -- PROVED

One has the exact union

\[
\boxed{
\mathcal F
=
\left(\bigcup_{f\in C}(\mathcal F-f)\right)
\cup
\mathcal F_C.
}
\]

Moreover

\[
\boxed{
\mathcal F\setminus\{Q\}
=
\left(\bigcup_{f\in C}(\mathcal F-f)\right)
\cup
(\mathcal F_C\setminus\{Q\}).
}
\]

### Proof

A state either contains every edge of `C` or omits at least one edge `f\in C`.
The rejected state contains all of `C`, so it belongs to no deletion branch and
is removed only from the conditioned branch in the second identity. ∎

The union need not be disjoint, but it is exact.

## 2. Side branches preserve every state omitting the prescription

### Theorem CMR863 -- PROVED

Every state `R` with `C\nsubseteq R` survives in at least one single-edge child
`\mathcal F-f`, with `f\in C\setminus R`. Every state containing `C` survives in
`\mathcal F_C`.

Consequently discarding empty deletion children preserves the union in CMR862.

### Proof

Choose any missing edge of `C`. The conditioned statement is definitional. A
child containing `R` is nonempty. ∎

Thus no improving state is lost by the prescription split.

## 3. Exact contraction of the conditioned prescription

Define

\[
\mathcal F_C/C
=
\{R\setminus C:R\in\mathcal F_C\}.
\]

### Theorem CMR864 -- PROVED

Restriction gives an exact bijection

\[
\boxed{
\mathcal F_C
\cong
\{C\}\times(\mathcal F_C/C).
}
\]

Every residual state has cardinality `k-|C|` when the original state cardinality
is `k`.

### Proof

Every conditioned state contains `C`. Removing and adjoining `C` are inverse. ∎

For a compatible labelled partial joint state, the corresponding matching-host
restriction removes the prescribed endpoints in their own layers and keeps the
fixed physical cells unavailable to the opposite layer.

## 4. Distinguishing rank persists conditionally

Assume `Q\in\mathcal F_C` and write `Q'=Q\setminus C`.

### Theorem CMR865 -- PROVED

One has

\[
\boxed{
\delta_{\mathcal F}(Q)
\le
|C|+
\delta_{\mathcal F_C/C}(Q').
}
\]

Equivalently,

\[
\boxed{
\delta_{\mathcal F_C/C}(Q')
\ge
\delta_{\mathcal F}(Q)-|C|.
}
\]

### Proof

Let `B'` distinguish `Q'` in the contracted conditioned family. Then
`C\cup B'` distinguishes `Q` in the full family: states omitting `C` fail the
`C` part, while states containing `C` are separated by `B'`. Minimise. ∎

A high-width state cannot lose more than `|C|` units of distinguishing rank by
conditioning on `C`.

## 5. Nonimproving target destruction supplies a new triple

Let `S` be the current anchor state and `Q` a target-destroying candidate. Let
`\mathcal T(U)` be the physical real triples of state `U`.

### Theorem CMR866 -- PROVED

If `Q` destroys at least one designated triple of `S` and

\[
\Phi(Q)\ge\Phi(S),
\]

then

\[
\boxed{
\mathcal T(Q)\setminus\mathcal T(S)\ne\varnothing.
}
\]

Choose the first new physical triple and retain its exact three labelled edges in
`Q`; call this labelled prescription `C_Q`.

### Proof

CMR698 gives at least as many new triples as designated lost triples. Positive
lost load therefore gives at least one new triple. Every selected physical cell
has one layer label in `Q`, producing the labelled prescription. ∎

The three labelled edges form a compatible partial joint state because they are
contained in `Q`.

## 6. Constant-arity complete response to one rejected candidate

### Theorem CMR867 -- PROVED

Let `Q` be nonimproving and target-destroying, and let `C_Q` be supplied by
CMR866. Then the complete feasible family splits into at most four structural
branches:

1. at most three viable single-edge deletion children `\mathcal F-f`, one for
   each `f\in C_Q`;
2. one conditioned branch `\mathcal F_{C_Q}`, in which the exact labelled
   collinear triple `C_Q` occurs in every surviving state.

Every state of the original family belongs to at least one branch.

### Proof

Apply CMR862--CMR863 with `|C_Q|=3`. ∎

This bound is independent of the matching exchange feedback width.

## 7. The conditioned branch is a forced-certificate branch

### Theorem CMR868 -- PROVED

Inside `\mathcal F_{C_Q}`, the labelled triple `C_Q` is a fixed candidate
conflict. The branch therefore reaches at least one of:

1. forced-certificate target handoff by CMR703;
2. exact contraction of `C_Q` as in CMR864, with residual state cardinality
   lowered by three;
3. deletion or essential-transfer action on a nonfixed residual prescription;
4. owner, factor, routing, or envelope change.

### Proof

The triple belongs to every conditioned state by definition. CMR703 converts a
forced physical triple into the target closure. The exact set-family contraction
is CMR864; matching-factor refinements use the existing essential and product
recursions. ∎

The conditioned branch is not silently discarded merely because it remains
dirty.

## 8. Geometric completeness endpoint

### Corollary CMR869 -- PROVED

Every nonimproving target-destroying candidate has a completeness-preserving
constant-arity response:

1. three or fewer single-edge deletion branches covering all states which omit
   its canonical new triple;
2. one forced-triple branch covering all states which retain that triple.

Along repeated conditioned continuations, each exact triple contraction lowers
labelled state cardinality by three; along deletion continuations, branch depth
is bounded by CMR833. The unresolved global issue is therefore not unbounded
local branch degree. It is compression of the resulting constant-arity tree, or
conversion of repeated forced-triple branches into target-load or potential
descent.

### Proof

Combine CMR866--CMR868 with the completeness and essential-core normal forms
CMR830--CMR861. ∎

No all-`n` theorem is claimed. Prescription unions, conditioned contraction,
distinguishing-rank persistence, new-triple existence, and constant-arity
coverage are checked in
[`scripts/verify_prime_power_new_triple_prescription_split.py`](../scripts/verify_prime_power_new_triple_prescription_split.py).
