# Mixed-shadow decoding and packet recurrence in rectangle label space

PX420--PX436 lift first-generation and packet-correction moves to exact
rectangle label permutations.  The remaining host-invariant sectors use both
column labelings `t` and `r`: one selected cell from each label family, or a
rank-three certificate with two cells from one family and one from the other.

Each label assignment has two row copies, so there are four mixed copy patterns.
For every fixed pattern the anchor-line colouring is proper in source and target
labels.  Summing the four patterns gives the same two-bank destruction
inequality as PX256--PX259, with weights aggregated on label assignments.
Transpositions of `t` or `r` move paired columns and preserve the exact rectangle
normal form.

Packet recurrence is also label-level.  A typed packet cross is a two-cycle
event in the label permutation.  Forbidding that event prevents every geometric
copy certificate it represents, and historical label positions prevent return
to an already corrected old defect.

## 1. Paired mixed potential

Let `M_t,M_r` be the current label permutations on source sets of orders
`n_t,n_r`.  An assignment `e in M_t` supplies two geometric points `e^0,e^1`,
and similarly for `g in M_r`.

For an anchor set `Z`, define

\[
\Phi_{tr}
=
\sum_{z\in Z}
\sum_{\epsilon,\delta\in\{0,1\}}
\#\{(e,g)\in M_t\times M_r:
 e^\epsilon,g^\delta,z\text{ collinear}\}.
\]

### Theorem PX437 -- PROVED

`Phi_tr` is exactly the anchor-weighted mixed `(1,1)` triple count between the
paired `t`- and `r`-label blocks.

For fixed `z,epsilon,delta`, colouring one label assignment by the line through
its copy point and `z` is proper in every source and target label of that block.

### Proof

Every mixed triple chooses one copy point from each label assignment and hence
one of four copy patterns.  A fixed scalar row meets a nonvertical anchor line
in at most one cell, and a fixed scalar column meets it in at most one cell.
The typed source and target maps are injective. \(\square\)

## 2. Destruction by paired label transpositions

Let the inherited label forbidden degrees be `Delta_t,Delta_r`.  A
transposition in `t` swaps the target labels of two source labels and moves both
row-copy points of each source; define the `r` bank symmetrically.

### Theorem PX438 -- PROVED

Every current mixed geometric collision is destroyed by at least

\[
\boxed{n_t-1-2\Delta_t}
\]

allowed `t`-transpositions and at least

\[
\boxed{n_r-1-2\Delta_r}
\]

allowed `r`-transpositions.

Its total destruction multiplicity is therefore at least

\[
\boxed{
\delta_{tr}
=
n_t+n_r-2-2(\Delta_t+\Delta_r).
}
\]

### Proof

Fix a collision using copy `epsilon` of source `u` in the `t` block.  Among the
`n_t-1` transposition partners, at most `Delta_t` fail at each crossed label
assignment.  For every allowed partner, the chosen copy point changes scalar
column while retaining its row.  The line through the unchanged `r` copy point
and anchor meets that row only at the old cell, so the collision is destroyed.
The paired copy moved by the same label transposition does not preserve the old
collision.  The `r` argument is symmetric. \(\square\)

## 3. Aggregate two-label-bank inequality

For an off-permutation `t`-assignment `f`, define its full paired directional
shadow

\[
\lambda_{t\to r}(f)
=
\#\{(z,g,\epsilon,\delta):
 f^\epsilon,g^\delta,z\text{ collinear}
\},
\]

where `g in M_r`.  Define `S_(t->r)` by summing over off-permutation assignments,
and define the reverse direction similarly.

### Theorem PX439 -- PROVED

Summing over all allowed label transpositions in both blocks,

\[
\boxed{
\sum_{\omega\in\Omega_t}\Delta_\omega\Phi_{tr}
+
\sum_{\eta\in\Omega_r}\Delta_\eta\Phi_{tr}
\le
\mathcal S_{t\to r}
+
\mathcal S_{r\to t}
-
\delta_{tr}\Phi_{tr}.
}
\]

At a joint transposition-local minimum with positive mixed potential,

\[
\boxed{
\delta_{tr}\Phi_{tr}
\le
n_t(n_t-1)\Lambda_{t\to r}
+
n_r(n_r-1)\Lambda_{r\to t}.
}
\]

### Proof

PX438 counts old destruction.  In one label bank, every off-permutation label
assignment occurs in at most one source-pair transposition.  Every new mixed
collision is therefore charged once to its full paired directional shadow.
There is no collision using two new assignments from the same bank because a
mixed triple uses one `t` assignment and one `r` assignment.  Sum and then use
nonnegativity at a local minimum. \(\square\)

## 4. Heavy paired shadow returns to star or line

Fix an off-permutation label assignment `f` with directional shadow `Lambda`.
Its two copy points split the shadow.

### Theorem PX440 -- PROVED

One copy point of `f` has mixed anchor--selected-point shadow at least

\[
\boxed{\Lambda/2.}
\]

For every selected-line threshold `K`, that copy point either lies on a line
containing more than `K` selected points of the opposite label block or centres
an endpoint-disjoint clean star of order at least

\[
\boxed{
\frac{\Lambda}{2(L_Z^{tr}+K)}.
}
\]

The star endpoints can be extracted to one rectangle point type and hence one
host-compatible label block with only an additional factor four loss.

### Proof

Pigeonhole the paired shadow over the two copy points.  Apply the incidence
matching argument PX259 to the heavier copy.  Then apply PX420 to the selected
star endpoints. \(\square\)

Thus mixed `(1,1)` return preserves the same clean-star/loaded-line geometry.

## 5. Mixed rank-three lift

A mixed rank-three certificate uses either two distinct assignments from `t`
and one from `r`, or the reverse.  By PX425 it uses at most one copy point from
each assignment.

### Theorem PX441 -- PROVED REDUCTION

The mixed rank-three anchor decoder PX260--PX262 lifts to paired label blocks
with at most eight copy-pattern families.  Its destruction multiplicities,
matching-cylinder ranks, and loaded-line/clean-star output types are unchanged
up to absolute constants.

Every correcting transposition is a host-compatible permutation of `t` or `r`.

### Proof

Partition certificates by the copy choice of each of their three label
assignments.  For a fixed pattern, the proper-colouring and transposition proof
of PX260--PX262 uses only injectivity of typed source rows and target columns,
which holds by PX411.  There are at most `2^3=8` patterns. \(\square\)

## 6. Packet-complement events are label two-cycles

Fix a typed packet level

\[
P\subseteq U\times V
\]

from PX428.  For two vertex-disjoint arcs

\[
u\to v,
\qquad s\to w
\]

in `P`, define the complementary label event

\[
\boxed{
C_{u,s}^{v,w}
=
\{\pi(u)=w,\ \pi(s)=v\}.
}
\]

### Theorem PX442 -- PROVED

For every copy pattern, selecting the complementary event is exactly selecting
the packet cross certified by the two typed arcs.  Forbidding the label event
suppresses all geometric copy certificates represented by that cross.

If an old selected packet defect is corrected by transposing the two targets,
recreating that old defect requires returning both sources to their historical
label assignments; the inherited historical label diagonal prevents this.

### Proof

The first statement is the typed cross identity PX429.  Copy choices change the
row coordinates but not the label assignment event.  The second statement is
exact: the old selected defect used the two original source--target assignments,
so its return contains both historical positions. \(\square\)

Thus one label event may pay several geometric copy certificates at once.

## 7. Joint typed packet release

Let `mathfrak P` be a family of `k` typed packets, allowing both row copies.
Forbid every complementary label event from every packet, together with the
ordinary label forbidden graph of degree `Delta_lab`.

### Theorem PX443 -- PROVED REDUCTION

The joint packet release theorem PX217--PX218 applies in label space after
replacing the packet count by the number of typed packet families.  In
particular, for

\[
\boxed{h\ge32\max(1,\Delta_{\rm lab},k),}
\]

the avoiding label-permutation family has density at least

\[
\boxed{e^{-4\Delta_{\rm lab}-4k}}
\]

inside `S_h`, with the corresponding fixed-rank and conditioned cylinder
bounds.

There are at most two typed copies of every scalar packet family, and duplicate
complementary label events are imposed only once.

### Proof

Each typed packet is a partial matching by PX428.  The canonical-event conflict
calculation of PX217 depends only on that partial-matching property and on the
ordinary forbidden degree.  It therefore applies to label assignments.
Conditioning is PX218. \(\square\)

## 8. Rectangle-host invariant closure for mixed and packet sectors

### Theorem PX444 -- PROVED REDUCTION

The following decoder moves can all be implemented as permutations of the
rectangle label variables `t,r`:

1. clean-star, radial, and loaded-line neutralizations, by PX427;
2. selected packet corrections and packet blocker countdowns, by PX431--PX436;
3. mixed `(1,1)` and mixed rank-three transposition decoders, by PX437--PX441;
4. typed packet-complement and joint-release constraints, by PX442--PX443;
5. actual terminal return, by PX411--PX419.

Every such move preserves:

- the PX43 rectangle normal form;
- exact row and column degree two;
- the two independent column-label permutations;
- factor compatibility supplied by PX61;
- historical recurrence constraints translated to label assignments.

All paired-copy effects change only absolute constants or the inherited label
forbidden degree.  The remaining global frontier is no longer host membership
of the geometric moves.  It is:

1. insert the label-level constants into one unified strict potential ledger;
2. verify finite orders below the explicit spread and divisor thresholds;
3. prove that the iterative label-level repair reaches zero bad triples rather
   than only a local improving state.

PX444 is an invariant-preservation reduction, not exact all-side closure.

## 9. Verification

Run

```bash
python scripts/verify_product_paired_label_mixed_shadow.py
```

The verifier checks the four copy-pattern proper colourings, paired
transposition destruction, aggregate directional-shadow accounting, typed
packet cross events, and duplicate event compression.
