# A minimum-potential anchor selects one complete structural path

CMR830--CMR901 distinguish two proof modes.  A complete existence search must
retain every unknown improving state and therefore uses disjoint prescription
branching.  A minimal-counterexample or minimum-potential argument is different:
one may choose an actual minimum state `S` of the current finite family.  Any
restriction which preserves `S` automatically preserves at least one minimum,
because no strictly better state exists to be lost.

This observation makes the anchor-preserving deletion machinery complete for the
specific task of analysing a positive minimum.  Every target-destroying
alternative supplies a new triple containing an edge outside the minimum anchor.
Deleting one such edge rejects the alternative and preserves the minimum.  After
at most the complete nonanchor edge stock, the chosen target and then any chosen
labelled subprescription of the anchor become fixed.  Exact contraction preserves
minimum status for the induced residual objective.

The theorem does not prove that a positive minimum is impossible.  It removes
branch width from that proof mode and leaves only restoration, anchor loss,
forced-core escape, strict descent, or potential improvement.

Let `\mathcal F` be a nonempty finite family of labelled saturated two-layer
states on a side-`n` board.  Every state has cardinality `2n`.  Let `\Phi` be the
real-triple potential and choose

\[
S\in\mathcal F,
\qquad
\Phi(S)=\min_{R\in\mathcal F}\Phi(R).
\]

## 1. Any anchor-preserving restriction retains a minimum

### Theorem CMR902 -- PROVED

For every subfamily `\mathcal A\subseteq\mathcal F` with `S\in\mathcal A`,

\[
\boxed{
\Phi(S)=\min_{R\in\mathcal A}\Phi(R).
}
\]

In particular, deleting any collection of labelled edges disjoint from `S`
retains one global minimum of the original family.

### Proof

Every state of `\mathcal A` is a state of `\mathcal F`, so its potential is at
least `\Phi(S)`.  The state `S` remains in `\mathcal A`. ∎

Equal-potential alternatives may be discarded; one minimum is retained.

## 2. A target-destroying alternative exposes a nonanchor edge

Fix a physical target triple

\[
T\subseteq |S|.
\]

Let `Q\in\mathcal F` omit at least one cell of `T`.  Since `S` is minimum,
`\Phi(Q)\ge\Phi(S)`, and CMR866 supplies a canonical new labelled triple
`C_Q\subseteq Q` which is not a physical triple of `S`.

### Theorem CMR903 -- PROVED

One has

\[
\boxed{C_Q\setminus S\ne\varnothing.}
\]

Deleting any edge

\[
f_Q\in C_Q\setminus S
\]

preserves `S`, rejects `Q`, and cannot create a new feasible state or matching
prescription.

### Proof

If every labelled edge of `C_Q` belonged to `S`, then all three physical cells
would belong to `S` and would form the same collinear triple there, contrary to
the choice of `C_Q`.  The edge `f_Q` lies in `Q` and not in `S`; deleting it
removes `Q` and preserves `S`.  Restricting a state family cannot activate a
state or prescription. ∎

This is a singleton no-good cut selected by the known minimum witness.

## 3. Quadratic minimum-preserving target forcing

Starting with `\mathcal F`, repeatedly choose the first surviving state `Q`
which omits `T`, choose the first edge of `C_Q\setminus S`, and delete that edge.

### Theorem CMR904 -- PROVED

The process uses at most

\[
\boxed{2n^2-2n}
\]

deletions and terminates with a nonempty family `\mathcal F_T` satisfying

\[
\boxed{
S\in\mathcal F_T,
\qquad
T\subseteq |R|
\text{ for every }R\in\mathcal F_T.
}
\]

The anchor `S` is still minimum in `\mathcal F_T`.

### Proof

Every selected edge is currently present, lies outside `S`, and is permanently
deleted during the pass.  The two labelled hosts contain at most `2n^2` edges,
while `S` contains `2n`; hence at most `2n^2-2n` such edges exist.  Termination
means no surviving state omits `T`.  Minimum preservation is CMR902. ∎

No completeness tree is required because the witness to be preserved is known.

## 4. Any anchor prescription can be forced with the same edge pool

Let `P\subseteq S` be any fixed labelled prescription.  Continue the same
monotone pass.  Whenever a surviving state `R` omits part of `P`, choose the
first edge of `R\setminus S` and delete it.

### Theorem CMR905 -- PROVED

Every such state has `R\setminus S\ne\varnothing`.  The combined target-forcing
and prescription-forcing pass still uses at most

\[
\boxed{2n^2-2n}
\]

deletions in total and terminates with

\[
\boxed{P\subseteq R}
\]

for every surviving state.

### Proof

If `R\setminus S` were empty, equal cardinality would force `R=S`, but `S`
contains `P`.  All deletions in both phases come from the same finite edge set
outside `S` and are distinct. ∎

In particular one may force the exact labelled assignment of a physical target,
a same-layer pair, or one residual trigger edge.

## 5. Exact contraction preserves induced minimality

Assume the pass has made a compatible prescription `P\subseteq S` common to
every surviving state.  Put

\[
\mathcal F/P
=
\{R\setminus P:R\in\mathcal F\},
\]

and define the induced objective

\[
\Phi_P(R')
=
\Phi(P\cup R').
\]

### Theorem CMR906 -- PROVED

Restriction is the exact bijection

\[
\boxed{
\mathcal F
\cong
\{P\}\times(\mathcal F/P),
}
\]

and the contracted anchor `S'=S\setminus P` satisfies

\[
\boxed{
\Phi_P(S')
=
\min_{R'\in\mathcal F/P}\Phi_P(R').
}
\]

### Proof

Common containment of `P` makes restriction and adjoining inverse.  Every
residual state lifts to one original state, and `S` was minimum among those
lifts. ∎

Thus exact contraction does not require a new minimizer search or an unproved
potential decomposition.

## 6. Minimum-preserving target contraction

Choose a target `T` of `S` and run CMR904.  Choose the exact labelled assignment
of `T` in `S` and force that labelled prescription by CMR905.

### Theorem CMR907 -- PROVED

Before any restoration or owner exit, one reaches a surviving family in which
that labelled target is fixed in every state and contracts exactly by three
labelled edges.  The residual anchor is minimum for the induced objective.

If only a same-layer pair or residual target edge is selected for contraction,
the corresponding rank-two or rank-one induced target is preserved exactly.

### Proof

CMR904 forces the physical target.  CMR905 forces its anchor layer assignment.
Apply CMR906.  Partial prescriptions use the same restriction identity. ∎

The resulting fixed dirty certificate still requires the existing handoff,
ancestry, wall, product, or envelope escape machinery; it is not itself a
contradiction.

## 7. Restoration is the only way to reuse a deleted nonanchor edge

Let `D\subseteq E\setminus S` be the set deleted during the minimum-anchor pass.
Suppose a later same-vertex-set host again makes some edges of `D` available.

### Theorem CMR908 -- PROVED

1. Every returned edge of `D` is a genuine physical restoration and carries the
   exact CMR413 full-token incidence.
2. If the stored anchor `S` remains feasible, every returned edge of `D` may be
   deleted again simultaneously.
3. If `S` is no longer feasible, one of its `2n` labelled edges is missing and is
   a canonical anchor-loss witness.

### Proof

The edges of `D` were absent after the pass, so later availability is a physical
zero-to-one transition.  Since `D\cap S=\varnothing`, deleting all returned
members preserves `S`.  If `S` fails, at least one of its edges is absent.  These
are CMR777, CMR800, and CMR801 specialised to the minimum anchor. ∎

## 8. Minimum-anchor endpoint

### Corollary CMR909 -- PROVED

At one fixed labelled owner, analysis of a minimum-potential state reaches at
least one of:

1. at most `2n^2-2n` distinct nonanchor deletions;
2. a chosen physical target forced in the surviving minimum branch;
3. a chosen labelled target prescription fixed and contracted exactly;
4. a residual minimum for the induced lower-cardinality objective;
5. simultaneous redeletion of restored nonanchor edges;
6. one missing anchor edge and forward deletion ancestry;
7. essential contraction, product or wall descent, owner change, or envelope
   expansion;
8. strict potential improvement after an external escape operation.

Therefore global completeness-tree width is not an obstruction for a proof by
analysis of an actual minimum.  The remaining issue is dynamic: rule out an
infinite sequence of restoration, anchor-loss, and owner-exit episodes which
keeps producing a positive induced minimum.

### Proof

Combine CMR902--CMR908 with the existing restoration forest and structural-exit
normal forms CMR777--CMR893. ∎

No all-`n` theorem is claimed.  Minimum preservation, outside-anchor deletion,
target and prescription forcing, induced-objective contraction, and restoration
responses are checked in
[`scripts/verify_prime_power_minimum_anchor_path.py`](../scripts/verify_prime_power_minimum_anchor_path.py).
