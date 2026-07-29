# Physical-label concentration of sparse fundamental defects

**Branch:** `research/sparse-algebraic-spread`

SAS5ib--SAS5if reduce every antisymmetric sparse history charge to the fundamental-cycle defects of one spanning forest. This note resolves nonzero defect mass into one finite physical cause and one sign.

Let `E_nt=E(Q)\setminus T` be the non-tree edges and let `D_e` be the fundamental defect of oriented edge `e`. Fix a finite ordered label dictionary

\[
\mathcal L=\{\ell_1,\ldots,\ell_K\}
\]

covering arithmetic, collinearity, boundary, owner, payment, donor, occurrence and lineage causes. Assign each non-tree edge its least valid label.

## SAS5ig -- exact labeled defect partition -- PROVED

For label `ell_j`, put

\[
D_j=\sum_{\substack{e\in E_{nt}\\\operatorname{label}(e)=\ell_j}} |D_e|.
\]

Then

\[
\boxed{
D:=\sum_{e\in E_{nt}}|D_e|
=
\sum_{j=1}^K D_j.
}
\]

### Proof

Every non-tree edge has exactly one least label, so the labeled edge classes partition the fundamental defect dictionary. QED.

## SAS5ih -- one heavy defect label and sign -- PROVED

One label satisfies

\[
\boxed{D_j\ge D/K.}
\]

Within that label, define

\[
D_j^+=\sum_{\operatorname{label}(e)=\ell_j}(D_e)_+,
\qquad
D_j^-=
\sum_{\operatorname{label}(e)=\ell_j}(-D_e)_+.
\]

Then one sign satisfies

\[
\boxed{
\max\{D_j^+,D_j^-\}
\ge
\frac{D}{2K}.
}
\]

### Proof

Pigeonhole SAS5ig over labels. Since `D_j=D_j^++D_j^-`, pigeonhole once more over the two signs. QED.

## SAS5ii -- edge-level defect witness inside a class -- PROVED

Let `beta_j` be the number of non-tree edges carrying label `ell_j`. If `D_j>0`, one such edge satisfies

\[
\boxed{
|D_e|\ge \frac{D_j}{\beta_j}
\ge
\frac{D}{K\beta_j}.
}
\]

If the sign-refined class contains `beta_j^sigma` edges, one edge of the heavy sign has magnitude at least `D/(2K beta_j^sigma)`.

### Proof

Pigeonhole the absolute or sign-refined defect mass over the corresponding finite edge class. QED.

## SAS5ij -- complete labeled history router -- PROVED

For one finite legal-state graph and one antisymmetric transition charge, one exact continuation holds:

1. every fundamental defect vanishes, so the charge is an endpoint potential;
2. one physical label carries absolute cycle-defect mass at least `D/K`;
3. one directed sign of that label carries at least `D/(2K)`;
4. one least non-tree edge realizes the edge-level bound from SAS5ii;
5. or one edge lacks a fixed label, orientation, antisymmetry, state identity, transition-legality or occurrence record.

Thus sparse history failure is reduced to one finite physical defect class and, when needed, one directed cycle witness. This is suitable for owner-specific debt concentration, directed payment, or a class-specific cycle ticket.

## Corrected SAS6 frontier

History dependence is finite and physically labeled. Remaining work is to construct the actual legal-state graphs, show the concrete charge labels pay or cancel, and handle lineage fields not represented by finite state data.

## Finite check

`scripts/verify_sparse_labeled_fundamental_defects.py` enumerates finite defect dictionaries and verifies the label, sign and edge-level concentration bounds.