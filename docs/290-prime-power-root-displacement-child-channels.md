# Depth-zero exact translations split into strict root child channels

CMR1493 leaves parent-scale depth-zero translations among the recurrent
same-owner cores.  Their arithmetic has one additional exact structure.

If a displacement has first-separation depth zero, then its residue modulo `p`
is nonzero.  Fixing the owner's root full-prefix cell therefore fixes a
different partner child cell and one exact quotient carry.  Within that one
channel all pairs are automatically endpoint-disjoint; no alternating-path
factor two is lost.

After a selected root routing skeleton is fixed, a response partner lies in a
distinct sibling factor, while a fixed partner lies in the fixed core.  The
candidate becomes one of the anchored or cross-factor atoms of
CMR958--CMR960, with local rank at most two in every factor.  The owner factor
has strict side `p^(k-1)` and is handled by coordinate-fibre normalization.

Retain an inherited envelope

\[
[0,p^k)^2,
\qquad k\ge1,
\]

and a nonzero exact displacement

\[
\Delta=(\Delta_x,\Delta_y)
\]

of first-separation depth zero:

\[
\boxed{
(\Delta_x,\Delta_y)\not\equiv(0,0)\pmod p.
}
\]

Let `E_Delta` be a finite weighted family of ordered pairs

\[
(a,b),
\qquad b=a+\Delta,
\qquad 0<w(a,b)\le1.
\]

## 1. Root residue determines the partner child and quotient carry

For a source residue

\[
r=(r_x,r_y)\in\{0,\ldots,p-1\}^2,
\]

define

\[
r'(r)=r+\Delta\pmod p
\]

using the standard representatives in `{0,...,p-1}`, and put

\[
q(r)=\frac{r+\Delta-r'(r)}p\in\mathbb Z^2.
\]

### Theorem CMR1494 -- PROVED

For every source residue `r`,

\[
\boxed{r'(r)\ne r.}
\]

If

\[
a=r+pA,
\qquad
b=r'+pB,
\]

then

\[
\boxed{B=A+q(r).}
\]

Thus one source root cell determines exactly one distinct partner root cell
and one exact quotient displacement.

### Proof

Depth zero means at least one coordinate of `Delta` is nonzero modulo `p`, so
translation by `Delta` changes the residue pair.  The identity

\[
r'+pB=r+pA+\Delta
\]

rearranges to the displayed quotient formula. ∎

This formula includes all coordinate carries, including negative
displacements and boundary-crossing source residues.

## 2. One heavy root channel is already private

Partition `E_Delta` by the source residue of `a`.  Let

\[
\mu_\Delta=\sum_{(a,b)\in E_\Delta}w(a,b).
\]

### Theorem CMR1495 -- PROVED

At most `p^2` source-residue channels occur.  Some channel `E_r` satisfies

\[
\boxed{
\mu_r:=
\sum_{(a,b)\in E_r}w(a,b)
\ge
\frac{\mu_\Delta}{p^2}.
}
\]

All pairs in `E_r` are pairwise endpoint-disjoint.  Consequently

\[
\boxed{|E_r|\ge\lceil\mu_r\rceil.}
\]

### Proof

Pigeonhole over the `p^2` source residues.

Distinct source endpoints have distinct translates.  A source endpoint has
residue `r`, while every partner endpoint has residue `r'(r) ne r`; hence no
source endpoint can equal a partner endpoint from the same channel.  The
complete endpoint family is disjoint.  Pair weights are at most one. ∎

Unlike the general path extraction of CMR1479, no half-mass loss occurs after
one root channel is fixed.

## 3. Residual blocker payment inside one root channel

Use the residual support

\[
J(a,b)=
\begin{cases}
\{a\},&b\in O,\\
\{a,b\},&b\text{ is a response partner}.
\end{cases}
\]

### Theorem CMR1496 -- PROVED

The supports `{J(a,b):(a,b) in E_r}` are nonempty and pairwise disjoint.
Every response-edge set meeting all of them satisfies

\[
\boxed{
|F|\ge |E_r|\ge\lceil\mu_r\rceil.
}
\]

For a current mask `F`, the unhit root-channel mass `u_r(F)` satisfies

\[
\boxed{
\max\{|F|,u_r(F)\}\ge\frac{\mu_r}{2}
\ge\frac{\mu_\Delta}{2p^2}.
}
\]

### Proof

CMR1495 gives endpoint-disjointness.  In the fixed-partner branch the distinct
owners are the residual supports.  In the response branch both endpoints are
residual and all are distinct.  Apply the proof of CMR1486. ∎

Thus depth zero also has an exact private-reserve currency before any child
normalization.

## 4. Quotient normalization is injective

For one fixed root channel `(r,r')`, define

\[
\pi_r(a)=\frac{a-r}{p},
\qquad
\pi_{r'}(b)=\frac{b-r'}p.
\]

### Theorem CMR1497 -- PROVED

Both quotient maps are injective on the channel, and every pair becomes

\[
\boxed{
\pi_{r'}(b)=\pi_r(a)+q(r)
}
\]

inside coordinate boxes of side `p^(k-1)`.

Pair weights, pair identities and the residual-support disjointness of
CMR1496 are preserved.

### Proof

Each map is restriction of subtraction followed by exact division by `p` on
one residue class, so it is injective.  CMR1494 gives the displacement
identity.  Injectivity preserves all labelled pair and support incidences. ∎

The source and partner quotient coordinates belong to differently labelled
root child cells; this is a cross-child channel, not a claim that the two
factors are one common matching host.

## 5. Cross-child candidates have low local rank

Fix an exact selected root-routing product.  Let the source child cell of the
owner be factor `A_r`.

### Theorem CMR1498 -- PROVED

Every candidate incidence in one root channel has one of the following exact
forms.

1. **Fixed-partner channel.**  The partner belongs to the fixed opposite
   layer.  Relative to the variable child factors, the candidate is an
   anchored atom.
2. **Response-partner channel.**  The partner lies in the distinct child
   factor `A_{r'}`.  The candidate is a cross-factor atom.

In either case every residual factor has local rank at most two, and the
possible positive residual-rank patterns are among

\[
\boxed{
(1),\ (2),\ (1,1),\ (2,1),\ (1,1,1).
}
\]

The canonical owner edge lies in the source factor `A_r`.

### Proof

The owner and response partner, when present, lie in the distinct child cells
given by CMR1494.  A fixed partner belongs to the fixed core.  The third cell
is fixed or lies in one residual factor.  Apply the exhaustive coupling
classification CMR959.  The canonical owner is the source endpoint by the
definition of the packed class. ∎

## 6. Strict child-factor normalization

### Theorem CMR1499 -- PROVED

Assume `k>=2`.  The source owner factor has side

\[
\boxed{p^{k-1}<p^k.}
\]

Freeze all other routing factors at one selected minimum and apply
CMR966--CMR972 to the source coordinate fibre.  Before any return to a
recurrent root-channel state, at least one of the following occurs.

1. Minimum-preserving deletion of a rank-one or rank-two anchored edge.
2. Exact contraction of a common anchored prescription.
3. A fixed complement/core certificate.
4. A pure target and induced minimum in the strict child factor.
5. A later owner, wall, host or envelope exit.
6. Strict potential improvement.

Every newly created credit after entering the child response owner belongs to
that active child factor by CMR1319.

### Proof

CMR1498 supplies exactly the anchored/coupling hypotheses of
CMR966--CMR971.  The root child side is `p^(k-1)`, which is positive and
strictly smaller for `k>=2`.  Apply CMR972 and last-entering factor ownership
CMR1319. ∎

Accordingly, a policy which pays the root channel by selected child routing
places all successful child, deletion, contraction and later-owner exits on
the existing structural transfer DAG.

## 7. Prime-field terminal channel

### Theorem CMR1500 -- PROVED

When `k=1`, every root child factor has side one.  The quotient coordinates in
CMR1497 are both `(0,0)`.  Therefore a depth-zero root channel reaches only:

1. a forced one-layer side-one edge which contracts;
2. an empty disjoint two-layer side-one factor;
3. a fixed-interface anchored trigger;
4. minimum-preserving deletion or contraction of its rank-one/rank-two
   prescription.

There is no positive-side child response bank below the prime-field root.

### Proof

CMR1497 gives quotient side `p^(k-1)=1`.  Apply the side-one classification
CMR1180 and the anchored-atom normalization CMR969--CMR970. ∎

This does not by itself prove the prime-field diagonal certificate: recurrent
root routing, fixed-interface target ownership and loaded-line alternatives
still require their weighted comparison.

## 8. Quantitative depth-zero splice and endpoint

Let `M_0` be the depth-zero exact-displacement mass supplied by CMR1475.

### Corollary CMR1501 -- PROVED

Some root child channel has mass at least

\[
\boxed{\frac{M_0}{p^2}}
\]

on pairwise endpoint-disjoint translated pairs.  It has at least

\[
\boxed{\left\lceil\frac{M_0}{p^2}\right\rceil}
\]

distinct pairs, and every residual blocker meeting all their private supports
has at least that many edges.

The channel then has one exact structural response:

1. for `k>=2`, low-rank coupling normalization and strict owner-child descent
   as in CMR1499;
2. for `k=1`, side-one contraction or a fixed-interface/low-rank terminal
   trigger as in CMR1500;
3. otherwise, explicit recurrence of the same absolute root channel.

Hence the anonymous depth-zero translation branch is replaced by a finite
root-channel stock with deterministic quotient carry, private blocker cost
and a canonical strict-child response.  The remaining diagonal object is the
recurrent root-channel/fixed-interface core itself, together with repeated
nonroot tokens, reused residual supports and the one-owner loaded-line core.

No all-`n` theorem is claimed.  Root-channel arithmetic, weighted
concentration, endpoint privacy, quotient carries, low-rank patterns and
strict child sides are checked in
[`scripts/verify_prime_power_root_displacement_child_channels.py`](../scripts/verify_prime_power_root_displacement_child_channels.py).
