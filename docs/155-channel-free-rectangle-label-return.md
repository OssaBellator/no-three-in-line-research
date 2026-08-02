# Channel-free terminal return through rectangle label permutations

PX391--PX410 formulate terminal return using selected endpoints grouped by
permutation-layer and hyperbola-channel type.  The recovered PX63 source has a
stronger invariant: every state in its rectangle normal form is controlled by
three label permutations `p,t,r`.  The two column labelings `t,r` are the actual
repair variables.  Permuting one labeling on a source set moves its two paired
rectangle corners together, preserves the full rectangle product state, and
suppresses every blocker assigned to either moved corner.

This removes the layer--channel parameter from terminal support compression.
Every fixed selected point belongs to exactly one of the two column-label
families, so blocker weight is pigeonholed over two types rather than `2q_ch`.
Large source sets give host-compatible label-permutation banks; small source
sets give a high-weight one-source child.  A one-source child has a linear bank
of label transpositions with zero internal three-new-cell collateral.

The result closes the channel-count hypothesis for the terminal-return branch.
It does not yet prove that every packet or arbitrary endpoint decoder can be
replaced by a rectangle-label decoder; that later invariant audit remains
separate.

## 1. Paired label coordinates of a rectangle state

Write the four points of rectangle `u` as

\[
T_0(u)=(X_0(u),Y_0(t(u))),
\qquad
T_1(u)=(X_1(p(u)),Y_0(t(u))),
\]

and

\[
R_0(u)=(X_0(u),Y_1(r(u))),
\qquad
R_1(u)=(X_1(p(u)),Y_1(r(u))).
\]

The two `T`-points form the selected pair in scalar column `Y_0(t(u))`; the two
`R`-points form the selected pair in scalar column `Y_1(r(u))`.

### Theorem PX411 -- PROVED

Every selected point of a rectangle state has a unique label address

\[
\boxed{(\xi,u,\epsilon)},
\qquad
\xi\in\{t,r\},\quad \epsilon\in\{0,1\}.
\]

For fixed `xi` and `u`, the two values of `epsilon` are the complete selected
pair in one scalar column.  Distinct source labels `u` give distinct scalar
rows in each copy and distinct scalar columns.

### Proof

This is the rectangle normal form PX43.  The maps `X_0`, `X_1 p`, `Y_0 t`, and
`Y_1 r` are injective, and the coarse row/column blocks separate the two
copies. \(\square\)

## 2. Exact host-compatible label rematching

Fix `xi in {t,r}` and a source set `U subseteq [n]`.  For a permutation
`pi in Sym(U)`, define

\[
\xi_\pi(u)=
\begin{cases}
\xi(\pi(u)),&u\in U,\\
\xi(u),&u\notin U.
\end{cases}
\]

Leave `p` and the other column labeling unchanged.

### Theorem PX412 -- PROVED

For every `pi`, the state obtained by replacing `xi` by `xi_pi` is again a
factor-compatible saturated rectangle state in the same orientation.

For each source `u in U`, the move replaces the complete paired column

\[
\{T_0(u),T_1(u)\}
\quad\hbox{or}\quad
\{R_0(u),R_1(u)\}
\]

by the corresponding pair carrying target label `xi(pi(u))`.

### Proof

Since `pi` permutes `U`, `xi_pi` is a permutation.  PX43 identifies every
triple `(p,t,r)` of permutations with a saturated rectangle state, and PX61
transports that normalized state to the same factor-compatible full host.
Both points carrying one label value move together, so every affected scalar
column still contains exactly two selected points. \(\square\)

This is stronger than rematching one canonical permutation layer: no point is
allowed to leave the rectangle product family.

## 3. Blocker debt compresses to one label family

Let `C` be a weighted family of external blockers.  Every blocker contains one
or two fixed selected points.  Assign each blocker to one of its fixed points.
For an assigned point `z`, let `xi(z) in {t,r}` and `u(z)` be its label family
and source index.

For `xi in {t,r}` and source `u`, put

\[
w_\xi(u)
=
\#\{T\in C:\xi(a(T))=\xi,\ u(a(T))=u\},
\]

with geometric multiplicity retained.

### Theorem PX413 -- PROVED

One label family `xi` carries total assigned weight

\[
\boxed{
W_\xi:=\sum_u w_\xi(u)\ge\frac{|C|}{2}.
}
\]

For every threshold `T>=1`, either:

1. at least `T` source labels have positive `w_xi`, giving a host-compatible
   label block of order at least `T` and suppression credit `W_xi`; or
2. one source label has assigned weight
   
   \[
   \boxed{w_\xi(u)>\frac{|C|}{2T}.}
   \]

### Proof

Pigeonhole assigned weight over `t,r`.  If fewer than `T` sources carry the
chosen family weight, one source exceeds the average `W_xi/T`. \(\square\)

No channel partition appears.

## 4. A derangement suppresses the full assigned label batch

Let `U` be the positive-weight source set in the chosen family.  Restrict to
permutations `pi` with no fixed point on `U`.

### Theorem PX414 -- PROVED

Every assigned blocker whose anchor source lies in `U` is absent after every
such label derangement.

### Proof

Let the blocker be assigned to selected point `z` of source `u`.  The parent
external blocker line is not the scalar row of `z`: after the parent switch the
row still contains exactly two selected points, so an external triple cannot
contain three points in that row.  Hence the blocker line meets the fixed scalar
row of `z` in the unique original cell `z`.

A label derangement moves both `xi`-points of source `u` to a different scalar
column.  In particular it moves `z` away from its unique blocker-line cell, so
the blocker is suppressed.  Historical recurrence likewise requires returning
the source label to its recorded target value. \(\square\)

## 5. Label-level forbidden degree and spread

Suppose the geometric forbidden set is a union of `h` partial matchings in the
scalar row--column graph, in addition to the current label diagonal.  A label
assignment `u -> v` inserts two geometric cells, one in each coarse row block.

### Theorem PX415 -- PROVED

Each geometric forbidden partial matching induces a forbidden graph on label
assignments of maximum source and target degree at most two.  Therefore the
label-level forbidden degree satisfies

\[
\boxed{\Delta_{\rm lab}\le1+2h,}
\]

where the one is the current label diagonal.

Whenever `|U|>=2 Delta_lab`, an allowed label derangement exists.  At residual
order at least `8 Delta_lab+2`, the optimized fixed-rank cylinder estimates
PX232--PX233 apply to the label permutation bank.

### Proof

For fixed source `u`, the paired assignment has two scalar source rows.  A
geometric partial matching forbids at most one target cell in each row, hence at
most two target label values.  Symmetrically, one target label supplies two
scalar columns and has at most two forbidden source labels.  Sum over the
historical partial matchings and add the diagonal.  Apply PX200 and
PX232--PX233 to the resulting label graph. \(\square\)

## 6. One-source terminal label transpositions

Let one source `u` in family `xi` carry designated blocker weight `D>=1`.  For a
fresh source label `a`, transpose the two label values `xi(u),xi(a)`.

### Theorem PX416 -- PROVED

Every allowed label transposition:

1. preserves factor compatibility and rectangle saturation;
2. moves both `xi`-points of `u` and both of `a`;
3. destroys every designated blocker assigned to source `u` whose recurrence
   cell is forbidden;
4. creates no triple consisting of three inserted cells.

If the inherited label forbidden degree is `Delta_lab`, at least

\[
\boxed{n-1-2\Delta_{\rm lab}}
\]

transposition partners are allowed before additional external blocker
exclusions.

### Proof

The invariant statement is PX412.  The four inserted points occupy exactly two
scalar columns, with two points in each.  Any three of them contain two points
from one column; their line is that scalar column, while the third point lies in
the other column.  Thus no internal inserted triple exists.

For source `u`, at most `Delta_lab` partners fail at each cross assignment
`u->a` and `a->u`.  Excluding `u` itself gives the count. \(\square\)

Order-two high-source children may be discharged by two sequential frozen label
transpositions.  Each step has the same zero-internal-triple property.

## 7. Channel-free weighted return

Assume a nonimproving terminal bank destroys `D` designated certificates.  By
PX357, one exact blocker type has family size at least `Dn/48` in the
one-variable case or `Dn^2/32` in the two-variable case.

### Theorem PX417 -- PROVED REDUCTION

For every threshold `T`, the blocker family yields either:

1. a host-compatible `t`- or `r`-label block of order at least `T`, with exact
   parent suppression credit at least
   
   \[
   \boxed{\frac{Dn}{96}}
   \]
   
   in the one-variable case, or
   
   \[
   \boxed{\frac{Dn^2}{64}}
   \]
   
   in the two-variable case; or
2. a one-source label child of designated weight greater than
   
   \[
   \boxed{\frac{Dn}{96T}}
   \]
   
   or respectively
   
   \[
   \boxed{\frac{Dn^2}{64T}.}
   \]

### Proof

Apply PX413 to the exact blocker family.  PX414 supplies the full assigned
suppression credit, and PX412 keeps the child inside the rectangle product
state space. \(\square\)

The former factors `q_ch` have disappeared.

## 8. Channel-free amplification and return depth

In a purely one-variable high-source chain, balance the two alternatives of
PX417 with

\[
T_j=\sqrt{\frac{nD_j}{96}}.
\]

### Theorem PX418 -- PROVED REDUCTION

Starting from `D_0>=1`, either a label block appears, or

\[
\boxed{
D_j
\ge
\left(\frac n{96}\right)^{1-2^{-j}}D_0^{2^{-j}}.
}
\]

With the actual PX64 line threshold `K=n^(1/3+o(1))`, after three high-source
returns one has

\[
D_3=n^{7/8-o(1)},
\]

and every coordinate or generic rank-one return gives a clean star of order

\[
\boxed{n^{13/24-o(1)}>n^{1/2}.}
\]

A two-variable return gives a one-source child of weight `Omega(n)` and hence a
rank-one star of order `n^(2/3-o(1))` at the next return, unless a loaded line or
large label block appears earlier.

### Proof

The recurrence is `D_(j+1)>=sqrt(nD_j/96)` and solves as in PX405.  The line-cap
exponents are PX407--PX408.  The constants improve because label-family
pigeonholing loses only a factor two. \(\square\)

### Corollary PX419 -- PROVED REDUCTION

The subpower layer--channel hypothesis in PX409 and PX410 is unnecessary for
actual rectangle-compatible terminal returns.  Terminal support compression,
high-source amplification, and terminal source moves can all be performed by
host-compatible `t/r` label permutations.

The remaining invariant frontier is narrower:

1. lift every large clean-star, radial, loaded-line, and packet child bank to a
   `t/r` label-permutation bank, including the collateral created by the paired
   copy of every moved label;
2. verify the finitely many below-threshold orders;
3. complete the exact potential descent inside the factor-compatible rectangle
   state space.

PX419 closes the channel-count hypothesis for terminal return only.  It does
not yet certify the host compatibility of every pre-existing large-block and
packet move.

## 9. Verification

Run

```bash
python scripts/verify_product_channel_free_label_return.py
```

The verifier checks the paired label representation, arbitrary subset
permutation invariance, blocker-weight compression over `t,r`, the induced
label forbidden-degree factor two, zero internal triples for label
transpositions, and the revised amplification constants.
