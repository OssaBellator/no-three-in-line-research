# Disjoint prescription branching compresses terminal leaves by forced targets

CMR862--CMR893 give a complete split of one nonimproving target-destroying
candidate and polynomial control along each path.  Their deletion children may
overlap.  Ordering the selected prescription and assigning every state to its
first missing edge makes the split disjoint.  Iteration gives a partition tree.
Terminal leaves with the same forced physical target may then be unioned, and an
eight-way layer-assignment split compresses them to polynomially many fixed
labelled-triple classes.

This is a set-family compression theorem.  A union of leaves carrying different
masks need not be the perfect-matching family of one bipartite host.  Host
factorisation must still be applied leafwise, or after a separate
representability result.

Fix a labelled two-layer board of side `n`.  Its labelled edge universe has size
at most `2n^2`.  All state families below have equal cardinality.

## 1. Ordered prescriptions give a disjoint partition

Let `C=(c_1,...,c_r)` be an ordered compatible labelled prescription.  Define

\[
\mathcal F_j(C)
=
\{R\in\mathcal F:c_1,\ldots,c_{j-1}\in R,\ c_j\notin R\},
\qquad 1\le j\le r,
\]

and

\[
\mathcal F_{r+1}(C)=\{R\in\mathcal F:C\subseteq R\}.
\]

### Theorem CMR894 -- PROVED

The children are pairwise disjoint and

\[
\boxed{
\mathcal F=\bigsqcup_{j=1}^{r+1}\mathcal F_j(C).
}
\]

### Proof

A state omitting part of `C` has a unique first missing edge.  A state containing
all of `C` belongs only to the last child. ∎

For `r=3`, this is a disjoint four-way refinement of CMR862.

## 2. Exact fixed-prefix normalisation

Put `P_j={c_1,...,c_{j-1}}`, with `P_{r+1}=C`.

### Theorem CMR895 -- PROVED

Restriction gives the exact bijection

\[
\boxed{
\mathcal F_j(C)
\cong
\{P_j\}\times\bigl(\mathcal F_j(C)/P_j\bigr).
}
\]

If `C` is a compatible partial joint matching, the matching-host refinement
contracts the fixed endpoints in their own layers and retains the corresponding
physical cells as forbidden cells in the opposite layer.

### Proof

Every state in the child contains the same prefix.  Removing and adjoining that
prefix are inverse operations.  Compatibility is inherited from a feasible state
containing `C`. ∎

## 3. A new target triple contains an undecided edge

At a node of a monotone prescription tree, some labelled edges are fixed in every
state and some are deleted from every state.  Let `S` be a feasible anchor, let
`Q` be a nonimproving state destroying a target of `S`, and let `C_Q` be the
canonical new labelled triple from CMR866.

### Theorem CMR896 -- PROVED

At least one edge of `C_Q` is neither fixed nor deleted.  After removing already
fixed edges, the residual prescription

\[
C_Q^\circ=C_Q\setminus E_{\mathrm{fix}}
\]

is nonempty and consists entirely of undecided edges.

### Proof

The physical triple underlying `C_Q` is not a triple of `S`, so one of its
labelled cells is absent from `S`.  Every fixed edge belongs to `S`, while no
deleted edge belongs to the feasible state `Q`. ∎

## 4. Finite disjoint target-resolution tree

Fix a baseline `B` and put

\[
\mathcal F_{\ge B}=\{R\in\mathcal F:\Phi(R)\ge B\}.
\]

If this family is nonempty, recurse as follows.  At a node with family
`\mathcal A`, choose a minimum-potential state `S` and its first physical target
`T`.  If every state contains `T`, stop.  Otherwise choose the first state `Q`
omitting `T`.  Since `S` minimises potential on the node,
`\Phi(Q)\ge\Phi(S)`, so CMR866 supplies `C_Q`.  Split on the nonempty undecided
prescription `C_Q^\circ` using CMR894 and discard empty children.

### Theorem CMR897 -- PROVED

Every root-to-leaf path has length at most

\[
\boxed{2n^2.}
\]

Each internal step fixes or deletes at least one previously undecided labelled
edge.

### Proof

CMR896 gives a nonempty undecided prescription.  Every ordered child either
deletes its first missing residual edge or fixes the whole residual prescription.
There are at most `2n^2` labelled edges. ∎

## 5. Terminal leaves force physical targets

### Theorem CMR898 -- PROVED

The recursion terminates.  Its nonempty leaves form a disjoint partition of
`\mathcal F_{\ge B}`.  Every leaf `\mathcal L` has a canonical physical target
`T(\mathcal L)` with

\[
\boxed{
T(\mathcal L)\subseteq |R|
\quad\text{for every }R\in\mathcal L.
}
\]

### Proof

Finite depth is CMR897.  Every internal split is the disjoint partition CMR894.
A node is terminal exactly when every surviving state contains its chosen target.
∎

## 6. Equal-target leaves merge as set families

Let `\mathfrak T_n` be the physical collinear triples of the grid.  Certainly

\[
|\mathfrak T_n|\le\binom{n^2}{3}.
\]

Define

\[
\mathcal G_T
=
\bigsqcup_{\mathcal L:T(\mathcal L)=T}\mathcal L.
\]

### Theorem CMR899 -- PROVED

The nonempty `\mathcal G_T` form the disjoint partition

\[
\boxed{
\mathcal F_{\ge B}
=
\bigsqcup_{T\in\mathfrak T_n}\mathcal G_T,
}
\]

and every state in `\mathcal G_T` contains `T`.  Thus an arbitrary number of
terminal leaves compresses to at most

\[
\boxed{\binom{n^2}{3}}
\]

physical-target classes.

### Proof

Each leaf has one canonical target label.  Grouping by that label preserves the
leaf partition and the leafwise forced-target assertion. ∎

## 7. Eight layer assignments give fixed labelled triples

Order the cells of `T`.  Every state containing `T` gives a unique assignment
`\sigma\in\{0,1\}^3`.  Let `\mathcal G_{T,\sigma}` contain the states with that
assignment.

### Theorem CMR900 -- PROVED

For every `T`,

\[
\boxed{
\mathcal G_T
=
\bigsqcup_{\sigma\in\{0,1\}^3}\mathcal G_{T,\sigma}.
}
\]

Every nonempty class has one fixed compatible labelled triple
`C_{T,\sigma}`, and

\[
\boxed{
\mathcal G_{T,\sigma}
\cong
\{C_{T,\sigma}\}
\times
\bigl(\mathcal G_{T,\sigma}/C_{T,\sigma}\bigr).
}
\]

### Proof

Layer assignment is unique.  In a nonempty class the corresponding labelled
edges occur in every state and are compatible because they occur in a saturated
state.  Restriction and adjoining are inverse. ∎

## 8. Polynomial terminal-certificate compression

### Corollary CMR901 -- PROVED

For every baseline `B`:

1. if a state of potential below `B` exists, strict improvement is already
   available;
2. independently, whenever `\mathcal F_{\ge B}` is nonempty, it is a disjoint
   union of at most
   \[
   \boxed{8\binom{n^2}{3}}
   \]
   fixed labelled-triple classes, each admitting exact rank-three set-family
   contraction.

If `|\mathcal F_{\ge B}|=M`, one class has size at least

\[
\boxed{
\frac{M}{8\binom{n^2}{3}}.
}
\]

### Proof

The improvement statement is definitional.  Apply CMR898--CMR900 to the
nonimproving subfamily and pigeonhole among at most `8|\mathfrak T_n|` classes.
∎

This closes leaf-count proliferation at one target-resolution stage.  It does not
identify unions of differently masked leaves with one common matching host, and
repeated contraction can still create many fixed-core histories.  The next
frontier is owner-compatible memoisation of these polynomial certificate classes,
or a common target-load/restoration charge independent of inherited masks.

No all-`n` theorem is claimed.  Ordered partitions, undecided-edge progress,
finite-depth recursion, target grouping, layer-assignment grouping, and density
bounds are checked in
[`scripts/verify_prime_power_disjoint_leaf_compression.py`](../scripts/verify_prime_power_disjoint_leaf_compression.py).
