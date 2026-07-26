# Recurrent robust signatures stabilize to one exact labelled residual-pair class

CMR990--CMR997 convert every minimum-robust target escape into entering-edge/new-
triple incidences. A recurrent basic signature fixes one labelled entering edge
`e` and one physical triple `U`, but the other two cells of `U` may change layer
labels between episodes.

There are at most four such assignments. Recurrence of `(e,U)` therefore
stabilizes one exact labelled residual pair after a finite partition. The
important scope point is that conditioning on `e` alone does **not** fix those two
labels. The rank-two transfer is exact only inside the corresponding fixed
`(e,U,P)` assignment class.

The signature uses absolute parent-grid coordinates and layer labels, not a
factor or envelope owner. Owner relabelling cannot create a new signature. If a
structural contraction removes one prescribed endpoint, that signature lineage
terminates; otherwise the same absolute signature continues.

Fix a physical triple

\[
U=\{x,y,z\}
\]

and one labelled edge

\[
e=(\ell,x)
\]

at the cell `x`. An occurrence of the basic signature `(e,U)` is a labelled
state `Q` which contains `e` and contains the physical cells `x,y,z`.

## 1. Every occurrence has one residual labelled pair

### Theorem CMR998 -- PROVED

For every occurrence `Q`, the cells `y,z` have unique selected layer labels in
`Q`. Let

\[
P_Q(U,e)
\]

be those two labelled edges. Then:

1. `P_Q(U,e)` is a compatible labelled rank-two partial joint state;
2.
   \[
   \boxed{
   U\subseteq |Q|
   \iff
   \{e\}\cup P_Q(U,e)\subseteq Q;
   }
   \]
3. the physical cells of `e` and `P_Q(U,e)` lie on the same real line.

### Proof

A feasible joint state selects each physical cell in at most one layer, so the
labels of `y,z` are unique. The three labelled edges are a subset of one feasible
state and are therefore compatible. Their physical cells are exactly `U`. ∎

## 2. There are at most four residual pair types

### Theorem CMR999 -- PROVED

For fixed `(e,U)`, the residual pair has at most

\[
\boxed{2^2=4}
\]

possible labelled types.

### Proof

Each of the two remaining physical cells independently belongs to one of the two
permutation layers. ∎

Compatibility may eliminate some of the four assignments.

## 3. Basic recurrence stabilizes one exact pair

### Theorem CMR1000 -- PROVED

If the basic signature `(e,U)` occurs in `r` episodes, one exact labelled residual
pair occurs in at least

\[
\boxed{
\left\lceil\frac r4\right\rceil
}
\]

of them.

### Proof

Partition the episodes by the at most four pair types of CMR999. ∎

The resulting exact labelled triple `\{e\}\cup P` is fixed across those selected
episodes.

## 4. Exact assignment-class partition

For a feasible family `\mathcal F`, put

\[
\mathcal F-e=\{R\in\mathcal F:e\notin R\},
\qquad
\mathcal F_e=\{R\in\mathcal F:e\in R\},
\]

and let

\[
\mathcal F_{e,U}
=
\{R\in\mathcal F_e:U\subseteq |R|\}.
\]

For every compatible labelled pair type `P` on the cells `y,z`, define

\[
\mathcal F_{e,U,P}
=
\{R\in\mathcal F:\{e\}\cup P\subseteq R\}.
\]

### Theorem CMR1001 -- PROVED

The family has the disjoint decomposition

\[
\boxed{
\mathcal F
=
(\mathcal F-e)
\sqcup
(\mathcal F_e\setminus\mathcal F_{e,U})
\sqcup
\bigsqcup_{P}\mathcal F_{e,U,P},
}
\]

where the last union ranges over at most four compatible pair types. Equivalently,

\[
\boxed{
\mathcal F_{e,U}
=
\bigsqcup_P\mathcal F_{e,U,P}.
}
\]

Every occurrence of `(e,U)` belongs to exactly one fixed-pair class. The branch
`\mathcal F-e` removes all such occurrences, while conditioning only on `e`
retains their possible four-way layer variation.

### Proof

A state either omits `e` or contains it. A state containing `e` either omits at
least one of the physical cells of `U` or contains all three. In the last case,
the two remaining cells have one unique pair of layer labels by CMR998, so the
assignment classes are disjoint and exhaustive. ∎

## 5. Fixed-class conditioning transfers exactly to the pair

### Theorem CMR1002 -- PROVED

Fix one compatible residual pair `P`. Then

\[
\boxed{
\mathcal F_{e,U,P}
=
\{R\in\mathcal F:\{e\}\cup P\subseteq R\}.
}
\]

Restriction gives the exact bijection

\[
\boxed{
\mathcal F_{e,U,P}
\cong
\{e\}\times
(\mathcal F_{e,U,P}/e),
}
\]

and every residual state in `\mathcal F_{e,U,P}/e` contains the same rank-two
prescription `P`. For every `R\in\mathcal F_e`,

\[
\boxed{
R\in\mathcal F_{e,U,P}
\iff
P\subseteq R\setminus\{e\}.
}
\]

If `\mathcal F` is a matching-host or joint-state cylinder, first conditioning
the complete cylinder on `\{e\}\cup P` and then contracting `e` is
host-representable by CMR974--CMR981. It is not necessary, and is generally
incorrect, to assert that all of `\mathcal F_e` has one fixed pair.

### Proof

The physical cells represented by `\{e\}\cup P` are exactly `U`. Inside the
fixed assignment class, removing and adjoining `e` are inverse operations, and
`P` remains common after contraction. Host representability follows by
conditioning on the complete compatible prescription before contraction. ∎

If `P` lies in one layer it enters the compatible-pair line-cylinder machinery;
if it spans the two layers it enters the rank-two product-rectangle and
essential-transfer machinery.

## 6. Absolute signatures are owner-independent

### Theorem CMR1003 -- PROVED

The augmented signature

\[
(e,U,P)
\]

is determined by absolute parent-grid cells and layer labels. Changing only the
envelope, routing, factor, wall, or certificate owner does not change it.

Under structural descent, exactly one of the following holds.

1. The labelled edge and pair remain in the residual vertex sets, and the same
   absolute signature continues.
2. A prescribed endpoint contracts or leaves the selected factor, terminating
   that signature lineage and paying strict structural descent.

### Proof

Owner labels are bookkeeping attached to the same absolute selected cells. Exact
product ownership gives one child for every nonfixed edge; endpoint contraction
removes that edge from the residual system. ∎

Thus recurrence counts are not multiplied by owner changes.

## 7. Global augmented-signature stock

Let

\[
\mathcal S_N
=
2N^2\binom{N^2-1}{2}
\]

be the basic stock from CMR994 on the ambient parent board.

### Theorem CMR1004 -- PROVED

The complete augmented stock is at most

\[
\boxed{4\mathcal S_N.}
\]

For robust episodes with designated loads `D_i` and gaps `g_i`, and every
`\mu\ge2`, either one exact augmented signature occurs at least `\mu` times or

\[
\boxed{
\sum_i(D_i+g_i)
\le
4(\mu-1)\mathcal S_N.
}
\]

For one-target robust episodes,

\[
\boxed{
K
\le
2(\mu-1)\mathcal S_N
}
\]

unless one exact augmented signature recurs `\mu` times.

### Proof

Each assigned basic signature has at most four residual pair labels. Refine every
assigned incidence by its actual pair type. CMR993 gives at least
`\sum_i(D_i+g_i)` assigned incidences. If every augmented signature has
multiplicity at most `\mu-1`, multiply the augmented stock by that threshold.
Each one-target episode contributes at least two incidences. ∎

## 8. Absolute signature endpoint

### Corollary CMR1005 -- PROVED

Every minimum-robust target-surplus history reaches at least one of:

1. an explicit finite augmented-signature bound CMR1004;
2. one exact labelled edge, physical target line, and residual labelled pair
   recurring together;
3. deletion of the common support edge;
4. the exact four-assignment partition of CMR1001;
5. host-representable conditioning on `\{e\}\cup P`, contraction of `e`, and
   rank-two pair transfer inside one fixed class;
6. same-layer pair-cylinder or cross-layer product-rectangle recursion;
7. endpoint contraction, strict factor/wall descent, protected-line/reserve
   payment, envelope expansion, or strict potential improvement.

Thus envelope and factor ownership no longer obscure robust-target recurrence,
and the layer-assignment ambiguity is finite and explicit. The remaining frontier
is the global rank-two/line budget for one exact augmented signature: prove that
its repeated pair or line recurrence exhausts a protected reserve, creates a
Hall/prefix/carry obstruction, or forces minimum decrease.

### Proof

Combine CMR998--CMR1004 with CMR990--CMR997, the edge lineage, conditioned-host,
pair-cylinder, and product-rectangle endpoints. ∎

No all-`n` theorem is claimed. Residual-pair extraction, four-type stabilization,
disjoint assignment classes, fixed-class contraction, owner independence,
augmented stock, and recurrence bounds are checked in
[`scripts/verify_prime_power_absolute_signature_pair.py`](../scripts/verify_prime_power_absolute_signature_pair.py).
