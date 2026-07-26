# Side three has an exact target bank; side two is physically rigid

CMR1166--CMR1173 pass residual side below four to the finite base ledger.  The
joint two-layer base can be sharpened explicitly.

At side three, a target edge `e` is absent from the fixed opposite permutation.
After relabelling the opposite permutation as the identity, `e` is a nonfixed
cell.  Exactly one of the two 3-cycles contains `e`; use that 3-cycle as the
forbidden extension.  The other 3-cycle is disjoint from both and is the response
matching.  Thus the fixed-target degree-two bank works at side three without the
general `n>=4` Hall theorem.

At side two, the two disjoint permutation layers are the two perfect matchings of
`K_{2,2}` and together select every physical cell.  No internal layer rematching
can change the physical selected set.  The block is therefore a rigid physical
interface: choose one labelled assignment, condition on it, and contract the
whole block.  A root side-two state is clean because a `2x2` grid has no three
distinct collinear cells.

## 1. Relabelled side-three permutations

Fix the opposite layer as the identity permutation on `{0,1,2}`.  Let `e=(i,j)`
with `i ne j`.

### Theorem CMR1174 -- PROVED

Exactly one derangement of three objects contains `e`, and the other derangement
is disjoint from both that derangement and the identity.

### Proof

The two derangements are the two directed 3-cycles.  From source `i`, one sends
`i` to each of the two nonfixed targets.  Hence exactly one contains `e`.  The two
3-cycles and the identity partition all nine cells of `K_{3,3}`. ∎

The statement is invariant under relabelling the opposite permutation.

## 2. Exact side-three target response

### Theorem CMR1175 -- PROVED

Let `M_o` be the fixed opposite permutation on a side-three joint block and let
`e notin M_o` be a selected target edge in the rematched layer.  There are unique
perfect matchings `F_e,R_e` such that

\[
e\in F_e,
\qquad
K_{3,3}=M_o\sqcup F_e\sqcup R_e.
\]

The response `R_e` avoids `e` and `M_o`, so replacing the current layer by `R_e`
preserves saturation and physical layer disjointness and destroys every target
containing `e`.

### Proof

Relabel `M_o` as the identity and apply CMR1174, then undo the relabelling. ∎

Thus side three belongs to the executable target-bank range.

## 3. Restricted side-three response

### Theorem CMR1176 -- PROVED

At a restricted side-three host, exactly one of the following holds.

1. The singleton response matching `R_e` is feasible and enters the minimum
   trichotomy.
2. Some edge of `R_e` is unavailable.  The singleton bank has a one-edge minimal
   blocker cover; restoring that blocker makes it essential and yields the unit-
   wall factorisation with residual side sum two.

### Proof

The complete response bank is `{R_e}`.  If it is infeasible, choose one missing
edge.  A one-edge cover is inclusion-minimal.  Apply CMR1153--CMR1156. ∎

## 4. Side-two joint states cover the complete board

### Theorem CMR1177 -- PROVED

`K_{2,2}` has exactly two perfect matchings.  Any physically disjoint ordered pair
of permutation layers uses those two matchings and therefore has physical selected
set

\[
\boxed{[2]\times[2].}
\]

There are two labelled layer assignments, exchanged by swapping the layers, but
only one physical selected set.

### Proof

The identity and transposition are the only permutations of two objects and are
disjoint.  Their union is all four cells. ∎

Consequently the physical triple potential is independent of the side-two layer
assignment.

## 5. A root side-two state is clean

### Theorem CMR1178 -- PROVED

The complete physical `2x2` grid contains no three distinct collinear cells.
Hence every saturated root side-two joint state has potential zero.

### Proof

A nonaxis or axis line meets a `2x2` grid in at most two distinct cells. ∎

This settles the genuine root joint base at side two.

## 6. Side-two residual blocks contract as rigid interfaces

Let a side-two joint block occur inside a larger induced objective.  Choose the
labelled assignment realized by the selected minimum anchor; it contains four
labelled edges.

### Theorem CMR1179 -- PROVED

Conditioning the complete current cylinder on those four edges preserves the
selected minimum, produces a singleton side-two block, and contracts the complete
block host-representably.  Every physical triple involving block cells is carried
exactly into the induced fixed-interface objective.

### Proof

The chosen state is an actual minimum.  Apply CMR902 and the host-representable
conditioning/contraction theorem CMR974--CMR981 to the full compatible block
prescription. ∎

Thus side-two residual geometry is transferred upward rather than treated as an
internally movable factor.

## 7. Side-one factors

### Theorem CMR1180 -- PROVED

A one-layer side-one matching factor has one forced edge and contracts immediately.
A physically disjoint two-layer side-one joint factor is empty.  No three-cell
physical target can lie wholly in such a factor.

### Proof

`K_{1,1}` has one edge.  Two disjoint perfect matchings cannot both use it. ∎

Anchored conflicts involving the forced edge are transferred to the fixed
interface by induced contraction.

## 8. Small joint-factor endpoint

### Corollary CMR1181 -- PROVED

The joint-factor finite base has the following exact form.

1. Side three: every active target has a unique singleton response bank; feasibility
   gives the minimum trichotomy and blockage gives unit-wall descent.
2. Side two at the root: the saturated physical board is clean.
3. Side two as a residual block: the physical block is rigid and contracts into
   the induced fixed interface.
4. Side one: forced one-layer edges contract; a disjoint two-layer factor is empty.

The remaining base issue is therefore not ordinary joint matching geometry.  It is
bookkeeping for induced fixed interfaces across prime-field/thin structural owners
and the final CRT assembly.

### Proof

Combine CMR1174--CMR1180. ∎

No all-`n` theorem is claimed.  Side-three permutation partitions, singleton bank
responses, side-two rigidity, root cleanliness, and small-factor contraction are
checked in
[`scripts/verify_prime_power_small_joint_factor_base.py`](../scripts/verify_prime_power_small_joint_factor_base.py).
