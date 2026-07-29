# Fundamental-cycle detection of sparse history defects

**Branch:** `research/sparse-algebraic-spread`

SAS5hx--SAS5ia show that an antisymmetric transition charge is safe under canonical path replacement exactly when the relevant closed-walk circulation vanishes. This note reduces that condition to a finite fundamental-cycle dictionary.

Let `Q=(V,E)` be a finite undirected graph of legal sparse matching states and allowed swap transitions. Give every oriented edge an antisymmetric charge

\[
c(v,u)=-c(u,v).
\]

Choose a spanning forest `T` of `Q`, with one root in each component.

## SAS5ib -- canonical tree potential -- PROVED

For a vertex `v`, define `Psi(v)` as the charge sum along the unique oriented tree path from its component root to `v`. Then every oriented tree edge satisfies

\[
\boxed{c(u,v)=\Psi(v)-\Psi(u).}
\]

### Proof

The root-to-`v` tree path is the root-to-`u` path followed by `(u,v)`, or the reverse orientation of that identity. Antisymmetry handles the reversed case. QED.

## SAS5ic -- fundamental defect formula -- PROVED

For every non-tree edge `e={u,v}`, orient it as `(u,v)` and define

\[
\boxed{D_e=\Psi(u)+c(u,v)-\Psi(v).}
\]

Then `D_e` is exactly the circulation on the fundamental cycle formed by `e` and the tree path from `v` back to `u`.

### Proof

The tree-path charge from `v` to `u` is `Psi(u)-Psi(v)`. Adding `c(u,v)` gives the displayed value. QED.

## SAS5id -- exact coboundary criterion -- PROVED

The edge charge `c` is a state coboundary,

\[
c(u,v)=\Phi(v)-\Phi(u)
\]

for some potential `Phi`, if and only if

\[
\boxed{D_e=0\qquad(e\in E\setminus T).}
\]

When this holds, the canonical tree potential `Psi` is such a `Phi` up to one additive constant per connected component.

### Proof

A coboundary has zero circulation on every cycle, so every `D_e` vanishes. Conversely, SAS5ib gives the potential identity on tree edges. If every `D_e=0`, the defining formula gives the same identity on every non-tree edge. QED.

## SAS5ie -- finite defect dictionary and concentration -- PROVED

If `Q` has `kappa` connected components, the number of fundamental defects is

\[
\boxed{\beta=|E|-|V|+\kappa.}
\]

If the total absolute defect mass is

\[
D=\sum_{e\in E\setminus T}|D_e|,
\]

then either all charges are a coboundary, or one fundamental cycle satisfies

\[
\boxed{|D_e|\ge D/\beta.}
\]

### Proof

A spanning forest has `|V|-kappa` edges, leaving `beta` non-tree edges. If `D>0`, pigeonhole its sum over those `beta` defects. QED.

## SAS5if -- complete finite history router -- PROVED

For every finite legal-state graph and antisymmetric sparse transition charge, one exact continuation holds:

1. every fundamental defect vanishes, so the charge is an endpoint potential and canonical replacement preserves it;
2. one least non-tree edge returns a nonzero fundamental-cycle defect;
3. one connected component, edge orientation, antisymmetry, state identity or transition-legality field is not fixed;
4. the legal-state graph is not finite under the declared physical profile, producing one outer-profile failure.

Thus history dependence does not require comparison with every possible original word. It is completely represented by at most `|E|-|V|+kappa` fundamental cycle values.

## Corrected SAS6 frontier

Structural, state-local and antisymmetric history auditing are now finite. Remaining work is to build the actual finite legal-state graph for each arithmetic/line/boundary/owner/payment profile, prove its transition charges are coboundaries, or pay the returned fundamental defects and lineage failures.

## Finite check

`scripts/verify_sparse_fundamental_cycle_defects.py` enumerates small state graphs and antisymmetric edge charges, constructs spanning forests, checks the fundamental-cycle formula and verifies the exact coboundary criterion.