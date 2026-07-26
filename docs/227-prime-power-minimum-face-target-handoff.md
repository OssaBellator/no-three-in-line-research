# Equal-minimum target handoff is a physical-cell deletion

CMR958--CMR981 reduce structural descent to pure factor targets, low-rank anchored
triggers, or a physical triple contained in the fixed complement/core.  The last
case is a target in the current minimum state.  If another minimum state destroys
that target, one can move to it without increasing potential.

The deletion must be physical-cell aware.  Removing only the old layer-labelled
edge would allow the same physical cell to reappear in the opposite layer.  Choose
a target cell omitted by the new minimum and delete both of its possible layer
labels.  The new minimum survives, while the physical target disappears from the
entire surviving family.

If no minimum destroys the target, the target is common to the minimum face.  A
four-endpoint bank expansion then either lowers the minimum, exposes a same-value
target-destroying minimum for the physical-cell cut, or leaves the target common
to the expanded minimum face.  Repeated equal-value handoffs consume monotone
labelled-edge stock unless a deleted physical cell is genuinely restored.

Fix a labelled two-layer state family on a physical board.  For a physical cell
`x`, let

\[
\widehat x=\{(0,x),(1,x)\}
\]

be its two possible layer-labelled copies.  Feasible joint states contain at most
one member of `\widehat x`.

Let `\mathcal M` be a minimum face, choose `S\in\mathcal M`, and let `T` be a
physical collinear triple contained in `S`.

## 1. Target variability inside the minimum face

### Theorem CMR982 -- PROVED

Exactly one of the following holds.

1. `T` is contained in every state of `\mathcal M`.
2. Some state `S'\in\mathcal M` omits at least one physical cell `x\in T`.

### Proof

Either universal containment holds or it has a counterexample.  A state which
does not contain the physical triple omits at least one of its three cells. ∎

## 2. A two-label cell cut gives same-value handoff

Assume branch 2 of CMR982 and choose `x\in T` omitted by `S'`.

### Theorem CMR983 -- PROVED

Delete every currently available labelled edge in `\widehat x`.  Then:

1. `S'` survives and the minimum value is unchanged;
2. the new minimum face is exactly
   \[
   \boxed{
   \{R\in\mathcal M:R\cap\widehat x=\varnothing\};
   }
   \]
3. no surviving feasible state contains the physical target `T`.

At least one currently available edge is deleted, namely the copy of `x` used by
`S`.

### Proof

The state `S'` omits the physical cell and therefore both labels, so it survives
with the old minimum value.  Restriction cannot lower the minimum; CMR926 gives
the face identity.  Every physical realization of `T` must use one of the two
labels of `x`, both of which are absent after the cut.  The selected state `S`
uses one copy, so the cut is strict. ∎

This is a minimum-preserving target handoff from `S` to the surviving face.

## 3. Fixed-vertex handoff chains are finite without restoration

Repeat CMR983 whenever the current selected minimum has a target omitted by
another current minimum.  Keep the host monotone between structural exits.

### Theorem CMR984 -- PROVED

Every handoff deletes at least one previously available labelled edge.  If the
labelled edge universe has size `u` and one minimum state of cardinality `k`
survives to the end of the segment, the number of handoffs is at most

\[
\boxed{u-k.}
\]

For saturated two-layer side `n`, this is at most `2n^2-2n`.

### Proof

The hosts form a nested decreasing chain.  CMR983 makes every handoff strict.
The final minimum state's `k` edges survive every deletion, leaving at most
`u-k` deletable labels. ∎

## 4. Reappearance pays physical restoration

Suppose a handoff deleted the physical-cell label set `\widehat x` and a later
minimum state again uses the physical cell `x`.

### Theorem CMR985 -- PROVED

At least one labelled copy of `x` underwent a genuine zero-to-one restoration.
If the same physical cell is cut in `r` distinct absence generations, there are
at least `r-1` genuine labelled-edge restorations, with total nonroot full-token
incidence at least

\[
\boxed{
(r-1)(p+1)(h-1).
}
\]

### Proof

After the cut neither label is available.  A later state using `x` requires one
copy to become available again.  Distinct generations are separated by such a
restoration.  Apply CMR413. ∎

A layer switch does not evade payment.

## 5. Bank expansion has an exact minimum response

Let `H` be the current host with minimum value `m`, and let `H^+\supseteq H` be a
same-vertex-set expansion which makes at least one CMR700 four-endpoint bank state
destroying `T` feasible.  Let `\mathcal M^+` be the expanded minimum face.

### Theorem CMR986 -- PROVED

At least one of the following holds.

1. `m(H^+)<m`: strict potential improvement.
2. `m(H^+)=m` and some state of `\mathcal M^+` omits `T`: apply CMR983 inside
   `H^+` and obtain a same-value physical-cell handoff.
3. `m(H^+)=m` and every state of `\mathcal M^+` contains `T`: the target is
   minimum-robust under this bank expansion.

### Proof

Expansion cannot raise the minimum.  Under equality, apply the target variability
dichotomy CMR982 to the expanded minimum face. ∎

The feasible bank state itself may have value above `m`; branch 3 records exactly
that possibility.

## 6. A minimum-robust physical target has a labelled conditioned cylinder

Assume branch 3 of CMR986 and choose any selected minimum `R\in\mathcal M^+`.
Let `C_R` be the three exact layer-labelled edges by which `R` realizes `T`.

### Theorem CMR987 -- PROVED

The full conditioned family

\[
(\mathcal F(H^+))_{C_R}
\]

has minimum value `m`, contains `R`, and contracts to a host-representable
residual joint system by CMR974--CMR977.  The physical target becomes a constant
fixed-core conflict in the induced objective.

There are at most eight possible labelled realizations of `T` across the expanded
minimum face.

### Proof

The conditioned family is a subfamily of the expanded family and contains the
minimum `R`, so its minimum value is exactly `m`.  Apply the joint conditioned-
cylinder factorisation CMR977.  Three physical cells have at most `2^3` layer
assignments. ∎

This is a structural normalization, not a removal of the dirty certificate.

## 7. Finite target cuts or recurrence

Consider `J` same-value target-handoff episodes on one fixed labelled edge
universe.  Assign each episode the first physical cell cut by CMR983.

### Theorem CMR988 -- PROVED

For every `\lambda\ge2`, at least one of:

1. one physical cell is cut in at least `\lambda` distinct absence generations;
2. the number of handoffs is at most
   \[
   \boxed{J\le(\lambda-1)n^2.}
   \]

In branch 1, CMR985 gives at least `\lambda-1` labelled-edge restorations.

### Proof

There are `n^2` physical cells.  If no cell has `\lambda` cut generations, each
has at most `\lambda-1`; sum.  The restoration statement is CMR985. ∎

This is coarser than CMR984 but tracks physical rather than labelled recurrence.

## 8. Minimum-face target-handoff endpoint

### Corollary CMR989 -- PROVED

A physical target in a selected minimum state reaches at least one of:

1. minimum-preserving physical-cell deletion and same-value handoff;
2. a finite monotone handoff chain;
3. recurrent physical-cell restoration with exact token payment;
4. strict potential improvement in a four-endpoint bank expansion;
5. a minimum-robust target common to the expanded minimum face;
6. one of at most eight labelled conditioned cylinders and exact target
   contraction;
7. owner/factor/wall/envelope exit.

Thus layer reassignment and minimum-face multiplicity do not create an anonymous
target cycle.  The remaining prime-power branch is the minimum-robust fixed-core
target: show that repeated bank expansions around it force potential decrease,
reserve/envelope expenditure, or a recurrent physical-cell/line witness already
covered by the historical-pair ledgers.

### Proof

Combine CMR982--CMR988 with CMR700--CMR703 and the conditioned host representation
CMR974--CMR981. ∎

No all-`n` theorem is claimed.  Physical target variability, two-label cell cuts,
minimum-face restriction, monotone handoff depth, restoration payment, bank
responses, labelled conditioning, and recurrence arithmetic are checked in
[`scripts/verify_prime_power_minimum_face_target_handoff.py`](../scripts/verify_prime_power_minimum_face_target_handoff.py).
