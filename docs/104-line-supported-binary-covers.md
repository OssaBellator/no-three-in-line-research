# Line-supported binary covers

The congestion-cover theorem PP3lb is purely combinatorial. Binary
controller-shadow conflicts also carry geometric witnesses: two endpoint cells
conflict because they lie with one controller candidate on one line. This chapter
shows that one rich witness line is easy rather than hard. The true obstruction
is overlap of many witness lines on the same endpoint resources.

## 1. Allowed endpoint traces of nonaxis lines

Let

\[
G_0=(L,R;E)
\]

be the zero-unary endpoint host, with selected old-column and old-row coordinate
sets `X` and `Y`. For a line `ell`, put

\[
P_E(\ell)
=
\ell\cap\{(x,y):(x,y)\text{ represents an edge of }E\}.
\]

Thus `P_E(ell)` contains only endpoint cells that are actually present in the
matching host.

### Proposition PP3lm -- PROVED

If `ell` is neither vertical nor horizontal, then `P_E(ell)` is a matching in the
endpoint-resource bipartite graph: no two of its cells share an old column or an
old row.

#### Proof

A nonvertical line meets each old column in at most one point, and a nonhorizontal
line meets each old row in at most one point. Passing to the subset belonging to
`E` preserves this property. ∎

Every line containing two compatible endpoint cells is automatically nonaxis.

## 2. One witness line has congestion one

Fix a controller candidate point `z` on a nonaxis line `ell`. Let

\[
\mathcal B_{z,\ell}
\subseteq
\binom{P_E(\ell)}2
\]

be any binary shadow conflicts assigned to the witness `(z,ell)`.

### Proposition PP3ln -- PROVED

Choose one cell

\[
a_\ell\in P_E(\ell)
\]

when the trace is nonempty and put

\[
C_{z,\ell}=P_E(\ell)\setminus\{a_\ell\}.
\]

Then `C_{z,ell}` covers every conflict in `mathcal B_{z,ell}`. Moreover

\[
\boxed{\Delta(C_{z,\ell})\le1.}
\]

#### Proof

Every conflict has two distinct cells in `P_E(ell)`, so at least one is different
from the single survivor `a_ell`. Proposition PP3lm shows that the deleted cells
use pairwise distinct left and right resources. ∎

In particular, a common-candidate line with linearly many allowed endpoint
intersections is absorbed by a unary matching. Its size does not create
congestion.

## 3. A family of witness lines

Assign every binary conflict

\[
B\in\mathcal B
\]

one witness pair `(z_B,ell_B)` such that both cells of `B` lie in `P_E(ell_B)` and
`z_B` lies on `ell_B`. Let `mathcal L` be the resulting set of typed witness
lines. For each `lambda in mathcal L`, choose one survivor cell from its allowed
trace and delete all other trace cells. Let

\[
C_{\mathcal L}
\]

be the simple union of the deleted cells.

For an endpoint resource `v`, define its witness-line incidence

\[
d_{\mathcal L}(v)
=
|\{\lambda\in\mathcal L:
P_E(\lambda)\text{ contains a cell incident with }v\}|,
\]

and put

\[
D_{\mathcal L}=\max_v d_{\mathcal L}(v).
\]

### Theorem PP3lo -- PROVED

The set `C_mathcal L` is a binary cover contained in `E`, and

\[
\boxed{
\Delta(C_{\mathcal L})
\le
D_{\mathcal L}.
}
\]

#### Proof

Each assigned conflict is covered inside its witness line by PP3ln. For a fixed
resource `v`, Proposition PP3lm gives at most one allowed trace cell incident with
`v` on each typed witness line. Hence at most `d_mathcal L(v)` deleted cells of
the simple union use `v`. ∎

Overlaps of the same deleted cell among several witness lines only improve the
bound.

## 4. Low-overlap binary endpoint

### Corollary PP3lp -- PROVED

If the binary shadow support admits a witness assignment satisfying

\[
D_{\mathcal L}=o(q),
\]

then it has a unary cover of resource congestion `o(q)`. Consequently:

1. the fractional optimum satisfies
   \[
   \tau^*(\mathcal B)\le D_{\mathcal L}=o(q);
   \]
2. if the residual zero-unary host is superregular and its source pair/triple
   counts satisfy PP3lc, there is a source-admissible endpoint trade with zero
   insertion shadow;
3. if the residual host has no perfect matching, PP3ld returns a Hall rectangle
   whose macroscopic part was already present before the line cover.

Thus a large number of binary conflicts is harmless when their witness lines have
low endpoint-resource overlap.

## 5. Exact line-overlap obstruction

### Corollary PP3lq -- PROVED

Consider any sequence of binary-shadow instances together with one chosen witness
assignment in each instance. At least one of the following holds.

1. Along the sequence,
   \[
   D_{\mathcal L}=o(q),
   \]
   so PP3lp applies.
2. Along a subsequence there is a constant `rho>0` and one typed endpoint resource
   incident with allowed traces of at least
   \[
   \boxed{\rho q}
   \]
   distinct typed witness lines.

#### Proof

The cover of PP3lo has congestion at most `D_mathcal L`. If this quantity is
`o(q)`, use the first alternative. Otherwise its ratio to `q` is bounded below by
some fixed positive constant along a subsequence, which is exactly the second
alternative. ∎

This is stronger than the binary-fan statement PP3ks. A fan with many distinct
controller candidates is precisely a pencil of many witness lines through the
fan centre cell; the two endpoint resources of that cell lie in every allowed
trace.

## 6. Revised binary geometry

The binary branch is now separated into two independent parameters.

- **Cover congestion** `tau^*(mathcal B)` from PP3le measures the best possible
  unary absorption without choosing geometric witnesses.
- **Witness-line overlap** `D_mathcal L` measures the congestion of the canonical
  geometric cover obtained by leaving one survivor on every candidate line.

A single rich line, a line clique, or a resource-disjoint collection of rich
lines is not an obstruction: each is covered with bounded congestion. The
remaining geometric binary target is a linear pencil of distinct candidate lines
through common endpoint resources, or the fractional dual packing of PP3le when
no low-overlap witness assignment exists.
