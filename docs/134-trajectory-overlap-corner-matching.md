# Trajectory overlap produces a compatible corner matching

PX291--PX293 reduce every genuinely immobile terminal block to a completely
forbidden row and column whose forbidden cells are supplied, apart from bounded
base degree, by historical position matchings.  The next question is whether the
two saturated trajectories interact.  They do whenever their historical level
sets overlap, and every overlap level produces one compatible corner-completion
cell.

## 1. Historical level overlap

Let the terminal block have order `m`, historical depth `d`, and base forbidden
degree at most `Delta_0`.  Let `v` be a fully forbidden row and `u` a fully
forbidden column.  Define

\[
I_v=\{j: H_j\text{ contains an edge in row }v\},
\qquad
J_u=\{j: H_j\text{ contains an edge in column }u\}.
\]

PX292 gives

\[
|I_v|,|J_u|\ge m-\Delta_0.
\]

### Theorem PX294 -- PROVED

The common-level set satisfies

\[
\boxed{
|I_v\cap J_u|
\ge
\max\{0,2(m-\Delta_0)-d\}.
}
\]

### Proof

Both sets lie in `[d]`, so inclusion--exclusion gives

\[
|I_v\cap J_u|
=|I_v|+|J_u|-|I_v\cup J_u|
\ge 2(m-\Delta_0)-d.
\]

The left side is nonnegative. \(\square\)

Thus every trajectory-saturated core with

\[
2(m-\Delta_0)>d
\]

has at least one historical level simultaneously meeting the saturated row and
column.

## 2. Corner completion cells

Fix `j in I_v cap J_u`.  Since `H_j` is a partial matching, it contains unique
edges

\[
(v,a_j),\qquad (b_j,u).
\]

Unless these are the same edge `(v,u)`, partial-matching compatibility gives

\[
a_j\ne u,\qquad b_j\ne v.
\]

Associate the corner-completion cell

\[
q_j=(b_j,a_j).
\]

### Theorem PX295 -- PROVED

After discarding the possible degenerate level with the single edge `(v,u)`,
the cells

\[
Q=\{q_j:j\in I_v\cap J_u\}
\]

form a partial matching: their row coordinates are distinct and their column
coordinates are distinct.  Consequently

\[
\boxed{
|Q|\ge
\max\{0,2(m-\Delta_0)-d-1\}.
}
\]

### Proof

Historical positions of the row endpoint `v` occur in distinct columns, so the
`a_j` are distinct.  Historical positions of the column endpoint `u` occur in
distinct rows, so the `b_j` are distinct.  Therefore the pairs `(b_j,a_j)` have
no repeated row or column.  At most one common level can consist of the edge
`(v,u)`. \(\square\)

The family `Q` is therefore already compatible with the matching geometry.  It
is not merely a set of candidate cells.

## 3. Allowed-corner versus owned-corner dichotomy

Partition

\[
Q=Q_{\rm allow}\mathbin{\dot\cup}Q_{\rm forb}.
\]

Every cell in `Q_forb` has a causal owner: either the bounded base graph `F_0`
or at least one historical matching `H_k`.  Assign each forbidden corner to its
earliest owner in the ordered list

\[
F_0,H_1,\ldots,H_d.
\]

### Theorem PX296 -- PROVED

For every threshold `theta in [0,1]`, one of the following holds.

1. **Executable corner field:**
   \[
   |Q_{\rm allow}|\ge \theta |Q|.
   \]
2. **Causally concentrated child field:** some owner class contains at least
   \[
   \boxed{
   \frac{(1-\theta)|Q|}{d+1}
   }
   \]
   forbidden corner cells.

In the second outcome those cells still form a partial matching.

### Proof

If the first outcome fails, then `|Q_forb|>(1-theta)|Q|`.  The earliest-owner
partition has `d+1` classes, so one class has at least the displayed average.
Every subclass of `Q` remains a partial matching. \(\square\)

This is an exact terminal strict-sign-or-child reduction: a positive fraction of
the overlap corners is directly executable, or a `1/(d+1)` fraction is assigned
to one older causal layer.

## 4. Quantitative terminal consequence

### Corollary PX297 -- PROVED

Put

\[
q=\max\{0,2(m-\Delta_0)-d-1\}.
\]

Taking `theta=1/2`, every trajectory-saturated terminal core has either

\[
\boxed{|Q_{\rm allow}|\ge q/2}
\]

compatible allowed corner cells, or one causal owner contains at least

\[
\boxed{q/(2(d+1))}
\]

compatible forbidden corner cells.

Since `d=O(log log N)`, the child-concentration loss is only polylogarithmic and
therefore `N^{o(1)}`.

This does not yet prove that the allowed corner field extends to a globally
improving principal trade, nor that every concentrated historical owner has the
required geometric decoder.  It replaces the unstructured trajectory-reset
problem by those two exact alternatives.

## 5. Verification

Run

```bash
python scripts/verify_product_trajectory_overlap_corners.py
```

The verifier exhausts all pairs of historical level sets through depth eight,
checks the overlap inequality, constructs abstract matching-valued corner
families, and verifies the owner-class averaging bound.