# Line-supported binary covers

The congestion-cover theorem PP3lb is purely combinatorial.  Binary
controller-shadow conflicts also carry geometric witnesses: two endpoint cells
conflict because they lie with one controller candidate on one line.  This
chapter shows that one rich witness line is easy rather than hard.  The true
obstruction is overlap of many witness lines on the same endpoint resources.

## 1. Endpoint traces of nonaxis lines

Let `X` and `Y` be the selected old-column and old-row sets of a tied endpoint
rectangle.  For a line `ell`, put

\[
P(\ell)=\ell\cap(X\times Y).
\]

### Proposition PP3lm -- PROVED

If `ell` is neither vertical nor horizontal, then `P(ell)` is a matching in the
endpoint-resource bipartite graph: no two of its cells share an old column or an
old row.

#### Proof

A nonvertical line meets each old column in at most one point, and a nonhorizontal
line meets each old row in at most one point. ∎

Every line containing two compatible endpoint cells is automatically nonaxis.

## 2. One witness line has congestion one

Fix a controller candidate point `z` on a nonaxis line `ell`.  Let

\[
\mathcal B_{z,\ell}
\subseteq
\binom{P(\ell)}2
\]

be any binary shadow conflicts assigned to the witness `(z,ell)`.

### Proposition PP3ln -- PROVED

Choose one cell `a_ell in P(ell)` when the trace is nonempty and put

\[
C_{z,\ell}=P(\ell)\setminus\{a_\ell\}.
\]

Then `C_z,ell` covers every conflict in `mathcal B_z,ell` unless the only
uncovered pair would have both endpoints equal to `a_ell`, which is impossible.
Moreover

\[
\boxed{\Delta(C_{z,\ell})\le1.}
\]

#### Proof

Every conflict has two distinct cells in `P(ell)`, so at least one is different
from the single survivor `a_ell`.  Proposition PP3lm shows that the deleted cells
use pairwise distinct left and right resources. ∎

In particular, a common-candidate line with linearly many endpoint intersections
is absorbed by a unary matching.  Its size does not create congestion.

## 3. A family of witness lines

Assign every binary conflict `B in mathcal B` one witness pair `(z_B,ell_B)` such
that both cells of `B` lie in `P(ell_B)` and `z_B in ell_B`.  Let `mathcal L` be
the resulting set of typed witness lines.  For each `lambda in mathcal L`, choose
one survivor cell from its trace and delete all other trace cells.  Let `C_L` be
the simple union of the deleted cells.

For an endpoint resource `v`, define its witness-line incidence

\[
d_{\mathcal L}(v)
=
|\{\lambda\in\mathcal L:
P(\lambda)\text{ contains a cell incident with }v\}|,
\]

and put

\[
D_{\mathcal L}=\max_v d_{\mathcal L}(v).
\]

### Theorem PP3lo -- PROVED

The set `C_L` is a binary cover and

\[
\boxed{
\Delta(C_{\mathcal L})
\le
D_{\mathcal L}.
}
\]

#### Proof

Each assigned conflict is covered inside its witness line by PP3ln.  For a fixed
resource `v`, Proposition PP3lm gives at most one trace cell incident with `v` on
each typed witness line.  Hence at most `d_L(v)` deleted cells of the union use
`v`. ∎

Overlaps of the same deleted cell among several witness lines only improve the
bound because `C_L` is a simple union.

## 4. Low-overlap binary endpoint

### Corollary PP3lp -- PROVED

If the binary shadow support admits a witness assignment satisfying

\[
D_{\mathcal L}=o(q),
\]

then it has a unary cover of resource congestion `o(q)`.  Consequently:

1. PP3lb gives the same conclusion for the fractional optimum;
2. if the residual zero-unary host is superregular and its source pair/triple
   counts satisfy PP3lc, there is a source-admissible endpoint trade with zero
   insertion shadow;
3. if the residual host has no perfect matching, PP3ld returns a Hall rectangle
   whose macroscopic part was already present before the line cover.

Thus a large number of binary conflicts is harmless when their witness lines have
low endpoint-resource overlap.

## 5. Exact line-overlap obstruction

### Corollary PP3lq -- PROVED

Fix any witness assignment of all binary conflicts.  At least one of the following
holds.

1. The assigned line family gives a cover with congestion `o(q)` and PP3lp
   applies.
2. Along a subsequence there is a constant `rho>0` and one typed endpoint
   resource incident with traces of at least

   \[
   \boxed{\rho q}
   \]

   distinct typed witness lines.

#### Proof

The cover of PP3lo has congestion at most `D_L`.  If `D_L=o(q)`, use the first
alternative.  Otherwise `D_L>=rho q` along a subsequence for some fixed positive
`rho`, which is exactly the second alternative. ∎

This is stronger than the binary-fan statement PP3ks.  A fan with many distinct
controller candidates is precisely a pencil of many witness lines through the
fan centre cell; the two endpoint resources of that cell lie in every trace.

## 6. Revised binary geometry

The binary branch is now separated into two independent parameters.

- **Cover congestion** `tau^*(mathcal B)` from PP3le measures the best possible
  unary absorption without choosing geometric witnesses.
- **Witness-line overlap** `D_L` measures the congestion of the canonical
  geometric cover obtained by leaving one survivor on every candidate line.

A single rich line, a line clique, or a resource-disjoint collection of rich
lines is not an obstruction: each is covered with bounded congestion.  The
remaining geometric binary target is a linear pencil of distinct candidate lines
through common endpoint resources, or the fractional dual packing of PP3le when
no low-overlap witness assignment exists.
