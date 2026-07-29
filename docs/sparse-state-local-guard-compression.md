# State-local guard compression and sparse history defects

**Branch:** `research/sparse-algebraic-spread`

SAS5hu--SAS5hw replace an arbitrary swap word by a canonical implementation with at most `r-1` swaps. This note identifies broad nonstructural contracts that are preserved or finitely audited under that replacement.

Let `M` denote the complete current matching state together with every fixed host, layer, boundary, owner and context field used by a proposed operation.

## SAS5hx -- state-local guard compression -- PROVED

Suppose the nonstructural legality contract is a finite dictionary of predicates

\[
G_1(M),\ldots,G_K(M)
\]

that depend only on the current complete state and fixed context, not on the path used to reach it. Let a final image permutation move `r` rows and have `s` nontrivial cycles. Its canonical implementation has `L=r-s<=r-1` noninitial prefixes.

It is enough to evaluate the guard dictionary on the initial state and those `L` canonical prefix states. Thus the complete nonstructural state-local audit uses at most

\[
\boxed{K(r-s+1)\le Kr}
\]

predicate evaluations, independent of the original word length.

### Proof

By hypothesis guard truth is a function of the current state. The canonical implementation visits exactly `L+1` states including the initial state. Evaluating every predicate there is necessary and sufficient for the canonical path. QED.

## SAS5hy -- coboundary history charges are endpoint invariants -- PROVED

Suppose a signed transition charge on legal swap edges has the form

\[
c(M,M')=\Psi(M')-\Psi(M)
\]

for one real-valued state potential `Psi`. Then every path from `M_0` to `M_1` has total charge

\[
\boxed{
\sum c(M_j,M_{j+1})=\Psi(M_1)-\Psi(M_0).
}
\]

Consequently replacing an original word by the canonical implementation preserves the total charge exactly.

### Proof

The potential differences telescope. QED.

## SAS5hz -- exact cycle-defect router -- PROVED

Let `P` be the original swap path and `Q` the canonical path with the same endpoints. For an arbitrary transition charge `c`,

\[
\boxed{C(P)-C(Q)=C(P\cdot\overline Q),}
\]

where `overline Q` is the reversed canonical path and the right side is the circulation on the resulting closed walk.

Therefore one of the following holds:

1. `c` is certified as a coboundary and canonical replacement preserves it;
2. the closed-walk circulation is zero for this word and replacement is charge-safe;
3. one nonzero cycle defect is returned as the exact history-dependence witness;
4. one guard is not state-local because it refers to an earlier occurrence, chosen path, consumed donor or transition lineage.

### Proof

Reverse-path charges subtract the canonical path sum, so concatenation gives the displayed identity. A coboundary has zero circulation on every closed walk by SAS5hy. QED.

## SAS5ia -- complete word-length-free audit -- PROVED UNDER THE LOCAL CONTRACT

For a final permutation on `r` moved rows, a contract consisting of:

- structural host/layer predicates;
- `K` state-local nonstructural predicates;
- coboundary transition charges;

has a canonical audit using at most

\[
\boxed{2r(r-1)+Kr}
\]

atomic structural/guard evaluations, plus endpoint evaluation of each potential. Any remaining failure is one structural atom, one state-local guard, one nonzero cycle defect, or one explicitly history-dependent field.

## Corrected SAS6 frontier

Arbitrary word length is now removed from structural and state-local nonstructural legality. Remaining work is to express the actual arithmetic, collinearity, boundary, owner and payment guards as state predicates or coboundaries, and to pay the exact cycle defects or lineage fields when they are not.

## Finite check

`scripts/verify_sparse_state_local_guard_compression.py` enumerates small permutation paths, verifies canonical guard-count bounds, telescoping endpoint charges and the original-versus-canonical cycle-defect identity.