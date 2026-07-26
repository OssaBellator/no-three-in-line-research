# A global minimum descends through one exact product coordinate fibre

CMR958--CMR965 transport every cross-factor triple as a low-rank coupling atom.
After coupling normalization, the surviving minimum face need not itself be a
Cartesian product.  Factor descent does not require that stronger statement.
Choose one actual minimum state and freeze all product coordinates except one.
The chosen state remains minimum in that coordinate fibre.

Every triple meeting the frozen complement becomes constant or a rank-one/rank-
two anchored prescription in the variable factor.  The one-factor fibre can
therefore be normalized by the same minimum-preserving deletion/common-core
contraction rule.  If the chosen target is pure in the variable factor, target
load descends to that strict factor.  If it meets the complement, it becomes a
fixed certificate or a low-rank trigger.

This gives structural descent for one selected minimum.  It does not assert that
the projection of the complete minimum face is one matching-host family.

Use the exact product notation of CMR958.  Choose one product minimum

\[
R^*=C\sqcup\bigsqcup_{a\in A}R_a^*
\]

and one distinguished factor `b\in A`.  Put

\[
D_b=C\sqcup\bigsqcup_{a\ne b}R_a^*
\]

and define the coordinate fibre

\[
\mathcal K_b
=
\left\{
D_b\sqcup P:P\in\mathcal F_b
\right\}.
\]

## 1. Minimum status is inherited by every coordinate fibre

### Theorem CMR966 -- PROVED

The selected state `R^*` is minimum in `\mathcal K_b` for the original global
potential:

\[
\boxed{
\Phi(R^*)
=
\min_{P\in\mathcal F_b}\Phi(D_b\sqcup P).
}
\]

### Proof

Every fibre state is a state of the original exact product family.  A state in
the fibre with smaller potential would contradict global minimality of `R^*`. ∎

Thus no independent factor minimizer must be guessed.

## 2. Exact one-factor induced-potential decomposition

Let `\kappa(D_b)` count triples contained in the frozen complement, and let
`X_b(P)` count triples contained wholly in the variable factor state `P`.
A remaining triple meeting both `D_b` and `E_b` is called an anchored atom.

### Theorem CMR967 -- PROVED

For every `P\in\mathcal F_b`,

\[
\boxed{
\Phi(D_b\sqcup P)
=
\kappa(D_b)+X_b(P)
+
\sum_{T\in\mathfrak A_b(D_b)}
\mathbf 1_{T_b\subseteq P},
}
\]

where `T_b=T\cap E_b`.  Every active anchored prescription has rank

\[
\boxed{|T_b|\in\{1,2\}.}
\]

### Proof

Partition triples into those contained in `D_b`, those contained in `E_b`, and
those meeting both.  A mixed three-edge set meeting both sides has one or two
variable edges.  The frozen part is automatic, so occurrence is exactly local
containment of `T_b`. ∎

This is an exact induced objective on one residual factor.

## 3. Targets have three exact fibre locations

Let `T` be any physical target triple contained in `R^*`.

### Theorem CMR968 -- PROVED

Relative to factor `b`, exactly one of the following holds.

1. `T\subseteq D_b`: the target is a fixed complement certificate in the whole
   fibre.
2. `T\subseteq R_b^*`: the target is a pure factor target.
3. `T` meets both classes: its variable part is a compatible rank-one or rank-two
   prescription in `R_b^*`.

### Proof

The edge classes are disjoint and exhaust the selected state.  A three-edge set
is contained in one class or meets both.  The mixed local rank is one or two. ∎

Thus no target disappears during coordinate freezing.

## 4. Fibre anchored atoms delete or contract

Let `\mathcal M_b` be the minimum face of the coordinate fibre for the induced
objective in CMR967.  Let `T_b` be an anchored rank-one or rank-two prescription
active in at least one fibre minimum.

### Theorem CMR969 -- PROVED

At least one response is available.

1. Some fibre minimum omits an edge `e\in T_b`.  Deleting `e` from the variable
   factor preserves the fibre minimum and kills the anchored atom.
2. Every edge of `T_b` belongs to every fibre minimum.  Restrict to that minimum
   face and contract `T_b` exactly.

### Proof

Apply the minimum-face edge dichotomy CMR911 to the local prescription.  If it is
not wholly common, delete a noncommon edge.  Otherwise apply complete-core
contraction CMR912 on the fibre minimum face. ∎

The first branch remains a matching-host deletion when `\mathcal F_b` is a
matching-host family.  The second remains a set-family claim unless host
representability is separately proved.

## 5. Finite one-factor normalization

Repeat CMR969 on the first active anchored atom.

### Theorem CMR970 -- PROVED

If the variable factor initially has edge-universe size `E_b` and state
cardinality `d_b`, then after at most

\[
\boxed{E_b+d_b}
\]

responses, at least one holds.

1. A target or conflict is fixed entirely in the accumulated complement/core.
2. No anchored atom occurs in any surviving fibre minimum.

### Proof

Local deletions consume distinct factor edges and occur at most `E_b` times.
Contractions have total rank at most `d_b`.  The minimum face only shrinks, and
contraction residualises existing anchored prescriptions. ∎

## 6. Pure residual potential after fibre normalization

### Theorem CMR971 -- PROVED

In branch 2 of CMR970, every surviving fibre minimum satisfies

\[
\boxed{
\Phi(D_b\sqcup P)
=
\kappa(D_b)+X_b(P).
}
\]

If the selected minimum still contains a target not fixed in `D_b`, that target
is pure in the variable factor and contributes to `X_b(P)`.

### Proof

CMR967 has no active anchored summand after normalization.  CMR968 classifies the
selected target. ∎

The frozen constant need not be zero.

## 7. Strict product factors give strict structural descent

Suppose the exact product arises from a strict child-routing factor, a positive
unit-wall child, or a nontrivial essential-core contraction.  Let the current
factor side be `d` and the distinguished positive child side be `d_b`.

### Theorem CMR972 -- PROVED

One has

\[
\boxed{1\le d_b<d.}
\]

Therefore CMR966--CMR971 transfer the selected minimum and every nonfixed target
to a strictly smaller factor, unless a fixed complement certificate or low-rank
anchored trigger is produced first.

### Proof

Strict child routing lowers side by CMR683.  Unit-wall child sides sum to `d-1`,
so every positive child is smaller by CMR736.  Essential-core contraction removes
at least one matching pair. ∎

## 8. Coordinate-fibre descent endpoint

### Corollary CMR973 -- PROVED

After coupling normalization of an exact structural product, one selected global
minimum reaches at least one of:

1. a fixed complement/core physical target certificate;
2. a rank-one or rank-two anchored target trigger;
3. minimum-preserving deletion of a variable-factor edge;
4. exact contraction of a common anchored prescription;
5. a pure target and induced minimum in a strictly smaller factor;
6. owner/factor/wall/envelope exit or strict potential improvement.

Thus cross-factor potential does not block selected-minimum structural descent.
The remaining issues are to route fixed certificates and low-rank triggers into
the existing target-load/reserve machinery, and to make the residual set-family
continuation host-representable when contraction is only minimum-face common.

### Proof

Combine CMR966--CMR972 with the exact structural products and coupling transport
CMR958--CMR965. ∎

No all-`n` theorem is claimed.  Fibre minimum inheritance, induced-potential
classification, target locations, anchored-atom responses, normalization bounds,
and strict-side arithmetic are checked in
[`scripts/verify_prime_power_minimum_coordinate_fibre.py`](../scripts/verify_prime_power_minimum_coordinate_fibre.py).
