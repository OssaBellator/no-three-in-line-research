# Every dirty small-factor interface target has a lifted response-bank owner

CMR1174--CMR1181 make side three executable and side two physically rigid.  A
residual side-two block can still participate in a physical collinear triple with
cells already fixed outside the block.  After conditioning the rigid block, such a
triple lies wholly in the accumulated fixed interface.

This is bookkeeping rather than a new geometric obstruction.  Every fixed
interface edge has a unique structural ancestry.  For a fixed physical target,
choose the last of its three labelled edges to become fixed and trace that edge
backward.  Unless the complete root has side two, the lineage reaches a unique
lifted owner of side at least three at which the full target is selected and at
least one target edge is still active.  The side-three or universal degree-two
response bank therefore belongs to that target.

Fix one selected minimum lineage and its sequence of exact contractions and product
descents.  Every selected physical edge retains its absolute parent-grid cell and
layer label.

## 1. Every fixed edge has a unique backward lineage

### Theorem CMR1182 -- PROVED

If a labelled physical edge ends in the accumulated fixed interface, then before
its fixation it follows one unique chain of residual factor owners.  At every exact
product it belongs to exactly one child factor, until it is contracted or absorbed
into the fixed interface.

### Proof

This is the unique edge-ownership theorem CMR822--CMR825. ∎

Branching products do not duplicate the backward edge lineage.

## 2. Canonical last-fixation edge of a target

Let

\[
T=\{e_1,e_2,e_3\}
\]

be the exact labelled realization of a physical target in the final accumulated
fixed interface.  Order contraction/fixation events by execution time and break
ties by the fixed edge ordering.

### Theorem CMR1183 -- PROVED

There is one canonical edge `e_*(T)` whose fixation event is last among the three
target edges.  Immediately before that event, the lifted selected state contains
all three target cells and `e_*(T)` is still active in one residual factor.

### Proof

The finite event order has a last element.  Earlier target edges remain selected as
fixed interface data, while the last edge remains selected in its residual factor
until its fixation. ∎

Thus every final fixed target has a canonical last-active owner.

## 3. Last-active owners of side at least three have a response bank

### Theorem CMR1184 -- PROVED

If the residual factor containing `e_*(T)` immediately before fixation has side at
least three, then the lifted target has an exact target-destroying response bank.

1. At side three use the unique singleton response CMR1175.
2. At side at least four use the degree-two bank CMR1158.

Restricted-host feasibility gives the minimum scheduler; complete blockage gives
the minimal unit-wall descent.

### Proof

The lifted target contains the active edge `e_*(T)`.  Apply the cited bank theorem
and then CMR1160--CMR1162. ∎

## 4. Small last-active owners lift to the nearest larger ancestor

Assume the last-active owner has side one or two.  Trace `e_*(T)` backward through
its unique owner lineage until the first ancestor whose active factor side is at
least three.

### Theorem CMR1185 -- PROVED

If the ambient root side is at least three, such an ancestor exists.  At that
ancestor:

1. the stored lifted anchor still contains all three physical target cells;
2. the edge `e_*(T)` is active or belongs to the selected factor interface which
   immediately precedes its strict side-one/two descendant;
3. leaving the selected routing/interface class and moving `e_*(T)` is represented
   by the full-layer target bank of CMR1175 or CMR1158.

### Proof

Strict child and unit-wall sides decrease from the ambient root.  A side-one/two
owner in a root of side at least three has an earlier ancestor before the descent
crosses below three.  Lifted anchors reconstruct every contracted and child edge
in absolute coordinates.  Unique ownership identifies the factor/interface
containing `e_*(T)`.  The target was selected throughout the lifted anchor lineage,
so the response bank may be formed at that ancestor. ∎

The bank need not lie in the already restricted child host; unavailable bank edges
are handled by the blocker-cover and unit-wall theorems.

## 5. Root side two cannot carry a dirty fixed target

### Theorem CMR1186 -- PROVED

If no ancestor of side at least three exists, the complete root side is at most
two.  A saturated root side-two joint state is clean by CMR1178, and a side-one
joint state does not exist.  Hence a dirty final fixed target cannot occur in this
branch.

### Proof

Apply CMR1177--CMR1180. ∎

Thus every dirty final interface target in a nontrivial root has a lifted bank
owner.

## 6. Lifted bank responses are already normalized

### Theorem CMR1187 -- PROVED

At the canonical lifted bank owner of CMR1184 or CMR1185, every response reaches at
least one of:

1. strict potential improvement;
2. same-value target-cell loss;
3. robust-surplus protected/line/star execution;
4. blocker-cover update and minimal unit-wall descent;
5. fixed-core reconditioning or a real lost lifted-anchor edge;
6. strict factor/wall/envelope descent or finite base handling.

### Proof

Combine CMR1134--CMR1173. ∎

No new small-factor response type is introduced.

## 7. Target-owner ancestry is finite

### Theorem CMR1188 -- PROVED

The canonical lifted owner of one final target is found along one physical edge
lineage of length at most

\[
L_{\mathrm{edge}}(N,h)
=(h+1)(\mathcal A(N)+1).
\]

Distinct owner relabellings without a host or structural change do not create new
ancestry positions.

### Proof

Use CMR825 on the edge `e_*(T)` and the routing normalization CMR1094--CMR1101. ∎

A target may share its owner and response bank with other targets; this only
reduces the required stock.

## 8. Small-interface ancestry endpoint

### Corollary CMR1189 -- PROVED

A physical target which survives only as fixed interface data after side-one/two
contractions is not a new terminal obstruction.  It has a canonical lifted owner
of side at least three with an exact target-destroying response bank, unless the
whole root has side two and is already clean.

Consequently the remaining frontier is no longer small-factor target geometry.
It is the final **global assembly of lifted-owner responses** across prime-field,
thin quotient/carry, and CRT decompositions, together with explicit finite
construction checks at the remaining root bases.

### Proof

Combine CMR1182--CMR1188. ∎

No all-`n` theorem is claimed.  Last-fixation ownership, backward edge lineages,
small-owner lifting, root cleanliness, and ancestry bounds are checked in
[`scripts/verify_prime_power_small_interface_target_ancestry.py`](../scripts/verify_prime_power_small_interface_target_ancestry.py).
