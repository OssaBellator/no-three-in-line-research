# Cancellation of invariant child-subtree triples

CMR99 leaves a weak node-rank-one collateral class. Part of that class is not
collateral at all: triples wholly inside one child subtree are translated
vertically as a rigid set when the parent reciprocal map changes, so they occur
with exactly the same multiplicity before and after every node repair.

Retain one nonroot node `(s,a,ell)` and write a column in child digit `xi` as

\[
x=a+p^s\xi+p^{s+1}q.
\]

Under a local node state with output digit `eta`, its row is

\[
y=P_{\ell,s}(a)+p^s\eta+p^{s+1}H_q.
\]

The descendant map `q -> H_q` is unchanged by the parent-node repair.

## 1. Exact determinant invariance

### Theorem CMR100 — PROVED

For three selected points in one child digit `xi`, their exact determinant is

\[
p^{2s+2}
\Delta\bigl((q_i,H_{q_i})_{i=1}^3\bigr),
\]

independent of the replacement output digit `eta` and independent of every other
parameter of the new parent map.

Consequently, every recursive-compatible node state has exactly the same number
of real collinear triples wholly contained in each child subtree as the old
state.

### Proof

Subtract the common column offset `a+p^s xi` and the common row offset

\[
P_{\ell,s}(a)+p^s\eta
\]

from the three points. Each remaining coordinate is divisible by `p^(s+1)`.
Bilinearity of the determinant gives the displayed factor and removes `eta`
entirely. ∎

## 2. Sharpened node-bank collateral

Let `I(A)` be the number of old real triples consisting of three changed-layer
points whose columns lie in one common child subtree of the node block `A`.
By CMR100, every replacement state contains exactly `I(A)` such triples.

Let `U_1^{ext}` be the node-rank-one certificate count from CMR99 after deleting
all certificates with three replacement cells in one child subtree. Thus every
remaining rank-one certificate contains one or two replacement cells and at
least one fixed point from `Z=S\setminus A`.

### Corollary CMR101 — PROVED

For a uniform recursive-compatible node state,

\[
\mathbb E\bigl[\Phi(S_{F'})-\Phi(Z)-I(A)\bigr]
\le
\frac{h}{h(p-2)+1}U_1^{ext}
+
\frac{U_2+U_3}{h(p-2)+1}.
\]

Hence some node state improves the total potential whenever

\[
D(A)-I(A)
>
\frac{h}{h(p-2)+1}U_1^{ext}
+
\frac{U_2+U_3}{h(p-2)+1}.
\]

### Proof

Partition the new triples touching the replacement block into the invariant
three-cell child-subtree triples and all remaining certificates. CMR100 makes
the first contribution exactly `I(A)` in every state. Apply the CMR96 cylinder
bounds to the remaining node-rank classes.

The same `I(A)` triples are included in the old defect count `D(A)`. Subtracting
`I(A)` from both sides of the potential comparison gives the criterion. ∎

The unresolved weak class is therefore strictly external: one or two points in
one child subtree together with at least one point outside that subtree. It is a
finer-scale secant-shadow problem, not an internal descendant triple core.

The determinant identity is checked in
[`scripts/verify_prime_power_child_core_cancellation.py`](../scripts/verify_prime_power_child_core_cancellation.py).
