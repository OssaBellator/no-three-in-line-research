# Disjoint prescription branching compresses terminal leaves by forced targets

CMR862--CMR893 give a complete split of one nonimproving target-destroying
candidate and polynomial control along every root-to-leaf path.  The split there
is an exact union, but its deletion children may overlap.  For global branch
accounting it is useful to make the split disjoint.

Order the edges of the selected prescription and assign every state to the first
prescription edge which it omits.  The remaining child contains the entire
prescription.  Iterating this rule gives a genuine partition tree rather than a
covering tree.  Terminal leaves forced by the same physical target may then be
unioned without losing the certificate.  Splitting once more by the eight layer
assignments of that target compresses an arbitrarily large leaf family to a
polynomial number of fixed labelled-triple classes.

The result is a set-family compression theorem.  A union of leaves with different
masks need not itself be the perfect-matching family of one bipartite host.  Exact
host factorisation must therefore be applied leafwise, or after a separate
representability theorem.  No such representability is assumed below.

Fix a labelled two-layer board of side `n`.  Its labelled edge universe has size
at most

\[
2n^2.
\]

All state families below consist of equal-cardinality saturated states.

## 1. Ordered prescriptions give a disjoint partition

Let

\[
C=(c_1,\ldots,c_r)
\]

be an ordered compatible labelled prescription.  For a state family
`\mathcal F`, define

\[
\mathcal F_j(C)
=
\{R\in\mathcal F:
 c_1,\ldots,c_{j-1}\in R,
 c_j\notin R\},
\qquad 1\le j\le r,
\]

and

\[
\mathcal F_{r+1}(C)
=
\{R\in\mathcal F:C\subseteq R\}.
\]

### Theorem CMR894 -- PROVED

The families `\mathcal F_1(C),\ldots,\mathcal F_{r+1}(C)` are pairwise
disjoint and

\[
\boxed{
\mathcal F
=
\bigsqcup_{j=1}^{r+1}\mathcal F_j(C).
}
\]

### Proof

A state which does not contain all of `C` has a unique first missing edge in the
fixed order.  It belongs to the corresponding child and to no other child.  A
state containing every edge of `C` belongs only to the last child. ∎

For `r=3`, this is a disjoint four-way refinement of CMR862.

## 2. Every child has an exact fixed-prefix normalisation

Put

\[
P_j=\{c_1,\ldots,c_{j-1}\}.
\]

Every state of `\mathcal F_j(C)` contains `P_j`; the first `r` children also omit
`c_j`.

### Theorem CMR895 -- PROVED

Restriction gives an exact bijection

\[
\boxed{
\mathcal F_j(C)
\cong
\{P_j\}\times\bigl(\mathcal F_j(C)/P_j\bigr).
}
\]

For the last child, `P_{r+1}=C`.  If `C` is a compatible partial joint matching,
then the matching-host refinement contracts the endpoints of the fixed edges in
their own layers and retains their physical cells as forbidden cells in the
opposite layer.

### Proof

Every state in the child contains exactly the same fixed prefix.  Removing and
adjoining that prefix are inverse operations.  Compatibility is inherited from
`C`, which is contained in one feasible state. ∎

## 3. A new target triple always contains an undecided edge

Consider a node of a monotone prescription tree.  Some labelled edges have
already been fixed in every state and some have already been deleted from every
state.  Let `S` be a feasible anchor at the node and let `Q` be a nonimproving
state which destroys a target of `S`.  Let `C_Q` be the canonical new labelled
triple from CMR866.

### Theorem CMR896 -- PROVED

At least one edge of `C_Q` is neither fixed nor deleted at the current node.
After removing already fixed edges, the residual ordered prescription

\[
C_Q^\circ
=
C_Q\setminus E_{\mathrm{fix}}
\]

is nonempty and consists entirely of currently undecided edges.

### Proof

The physical triple underlying `C_Q` is not a triple of `S`.  Hence at least one
of its physical cells, with its label in `Q`, is absent from `S`.  Every fixed
labelled edge belongs to `S`, so that edge is not fixed.  No deleted edge belongs
to the feasible state `Q`.  Thus at least one edge is undecided, and every
nonfixed edge of `C_Q` is undeleted. ∎

## 4. The disjoint target-resolution tree has finite depth

Fix a baseline value `B` and let

\[
\mathcal F_{\ge B}
=
\{R\in\mathcal F:\Phi(R)\ge B\}.
\]

If this family is empty, a strict improvement below `B` already exists.  Otherwise
build the following tree recursively.

At a node with nonempty family `\mathcal A`, choose a state `S` of minimum
potential in `\mathcal A` and choose the first physical target triple `T` of
`S`.  If every state of `\mathcal A` contains `T`, stop and label the node by
`T`.  Otherwise choose the first state `Q` which omits `T`.  Since `S` minimises
potential on `\mathcal A`,

\[
\Phi(Q)\ge\Phi(S).
\]

CMR866 supplies `C_Q`; split on the nonempty undecided prescription `C_Q^\circ`
using CMR894, discarding empty children.

### Theorem CMR897 -- PROVED

Every root-to-leaf path of this recursion has length at most

\[
\boxed{2n^2.}
\]

More precisely, every internal step fixes or deletes at least one previously
undecided labelled edge.

### Proof

CMR896 makes the residual prescription nonempty and undecided.  In the ordered
partition, each child either deletes its first missing residual edge or fixes the
entire residual prescription; in either case at least one undecided edge receives
its first permanent status on that path.  There are at most `2n^2` labelled
edges. ∎

The bound is deliberately coarse.  Contractions and surviving-state cardinality
can only shorten a path.

## 5. Terminal leaves force physical targets

### Theorem CMR898 -- PROVED

The recursion terminates after finitely many steps.  Its nonempty leaves form a
disjoint partition of `\mathcal F_{\ge B}`.  Every leaf `\mathcal L` has one
canonical physical target triple `T(\mathcal L)` satisfying

\[
\boxed{
T(\mathcal L)\subseteq |R|
\quad\text{for every }R\in\mathcal L.
}
\]

### Proof

Finite depth is CMR897.  Every internal split is the disjoint partition CMR894,
so induction gives a disjoint partition of the root family.  A node is terminal
exactly when every surviving state contains its chosen target. ∎

The target labels may differ between leaves.

## 6. Leaves with the same target merge exactly as set families

Let `\mathfrak T_n` be the set of physical collinear triples in the `n\times n`
grid.  Certainly

\[
|\mathfrak T_n|
\le
\binom{n^2}{3}.
\]

For `T\in\mathfrak T_n`, define

\[
\mathcal G_T
=
\bigsqcup_{\mathcal L:\,T(\mathcal L)=T}\mathcal L.
\]

### Theorem CMR899 -- PROVED

The nonempty families `\mathcal G_T` form a disjoint partition

\[
\boxed{
\mathcal F_{\ge B}
=
\bigsqcup_{T\in\mathfrak T_n}\mathcal G_T,
}
\]

and every state in `\mathcal G_T` contains the same physical target `T`.
Consequently an arbitrarily large terminal leaf set compresses to at most

\[
\boxed{\binom{n^2}{3}}
\]

physical-target classes.

### Proof

Each leaf has one canonical target label, so grouping leaves by that label
preserves disjointness and covers every leaf.  The forced-target assertion holds
leafwise and therefore on their union. ∎

## 7. Eight layer assignments give fixed labelled triples

Order the three cells of a physical target `T`.  Every labelled two-layer state
containing `T` assigns each cell to one of two layers, giving one word

\[
\sigma\in\{0,1\}^3.
\]

Let `\mathcal G_{T,\sigma}` be the states of `\mathcal G_T` with assignment
`\sigma`.

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
`C_{T,\sigma}`.  Restriction gives the exact set-family bijection

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

Every state has a unique layer assignment for the three physical cells.  In a
nonempty class, the resulting labelled edges occur in every state and are
compatible because they are contained in a saturated state.  Remove and adjoin
the fixed triple. ∎

## 8. Polynomial terminal-certificate compression

### Corollary CMR901 -- PROVED

For every baseline `B`, exactly one of the following holds.

1. A state with potential below `B` exists.
2. The nonimproving family `\mathcal F_{\ge B}` is a disjoint union of at most
   \[
   \boxed{
   8\binom{n^2}{3}
   }
   \]
   fixed labelled-triple classes, each admitting exact rank-three set-family
   contraction.

If `\mathcal F_{\ge B}` has size `M`, one class has size at least

\[
\boxed{
\frac{M}{8\binom{n^2}{3}}.
}
\]

### Proof

If the improving family is nonempty, use branch 1.  Otherwise apply CMR898--
CMR900 and pigeonhole among the at most `8|\mathfrak T_n|` classes. ∎

This closes leaf-count proliferation at one target-resolution stage.  It does not
yet identify unions of differently masked leaves with one common matching host,
and repeated rank-three contraction can still create many different fixed-core
histories.  The next frontier is therefore owner-compatible memoisation of these
polynomial certificate classes, or a common target-load/restoration charge which
does not depend on their inherited masks.

No all-`n` theorem is claimed.  Ordered partitions, undecided-edge progress,
finite-depth recursion, target grouping, layer-assignment grouping, and density
bounds are checked in
[`scripts/verify_prime_power_disjoint_leaf_compression.py`](../scripts/verify_prime_power_disjoint_leaf_compression.py).
