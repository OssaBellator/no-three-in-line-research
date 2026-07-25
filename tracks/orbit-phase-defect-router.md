# Geometric routing of paid current defects

OP4l transfers a fixed fraction of protected-correction gain to current
violated geometric factors.  Its remaining output is therefore a
weighted family of real collinear triples, not an abstract implication
core.

This note gives the direct geometric router for that family.  At a
chosen point-load threshold, either one point anchors a paid factor
star or greedy deletion extracts many point-disjoint triples.  The
star enters OP1d, while the matching enters the divisor-capacity part
of OP4j directly.

No protected-switch hypothesis is used on the matching side.
OP4j.0 was needed only to derive point-disjointness from
switch-disjointness.  Here point-disjointness is the output of the
router itself.

## Paid defect hypergraph

Fix one current phase snapshot \(\omega\).  Let \(\mathcal F\) be a
finite family of distinct current violated OP1 factors.  Each
\(F\in\mathcal F\) retains:

- its real collinear triple \(T_F\);
- its OP1a current-zero source clause;
- its OP4g channel and carry records; and
- a factor-conservative payment \(p_F>0\).

Put

\[
P=\sum_{F\in\mathcal F}p_F.
\]

For a candidate point \(z\), define its paid load

\[
L(z)
=
\sum_{F:z\in T_F}p_F.
\]

Assume the active point set uses at most \(q\) modular-hyperbola
channels.  Every real factor uses at least two channels.

## OP4m.0 -- weighted star or point-disjoint matching

Fix thresholds \(\lambda,\mu>0\).

### Theorem OP4m.0 -- PROVED

The paid defect family has one of the following ordered outputs.

1. **Heavy current source factor.**  Some factor satisfies
   \[
   \boxed{p_F>\mu.}
   \]
2. **Paid point star.**  Every factor has \(p_F\leq\mu\), and some
   point \(z\) has
   \[
   \boxed{L(z)>\lambda.}
   \]
   Its star contains at least
   \[
   \boxed{
   M_z
   \geq
   \left\lfloor\frac{\lambda}{\mu}\right\rfloor+1
   }
   \]
   distinct real factors.
3. **Point-disjoint defect matching.**  Every factor has
   \(p_F\leq\mu\), every point has \(L(z)\leq\lambda\), and
   \(\mathcal F\) contains a point-disjoint subfamily \(M\) with
   \[
   \boxed{
   |M|
   \geq
   \left\lceil\frac{P}{3\lambda}\right\rceil.
   }
   \]

Every returned factor remains currently violated and keeps its payment
and complete geometric provenance.

### Proof

Return conclusion 1 if it occurs.  Otherwise every star factor has
payment at most \(\mu\).  If \(L(z)>\lambda\), then

\[
M_z\mu\geq L(z)>\lambda,
\]

which gives conclusion 2.

Now suppose every point load is at most \(\lambda\).  Repeatedly choose
one remaining factor and delete every remaining factor sharing one of
its three points.  The deleted payment in one step is at most

\[
\sum_{z\in T_F}L(z)\leq3\lambda.
\]

The chosen factors are point-disjoint.  If the process chooses \(m\)
factors, its deleted families partition \(\mathcal F\), so

\[
P\leq3m\lambda.
\]

This gives the displayed ceiling bound. \(\square\)

The factor threshold is needed only to convert paid point load into a
count of distinct geometric factors.  The low-point-load matching
bound uses payment directly and does not lose a factor-weight ratio.

## OP4m -- carry growth from either geometric branch

Retain

\[
\Delta_p^\star
=
\max\{
\Delta_p^{\rm prod},
\Delta_p^{\rm cross}
\}
\]

from OP1d, and put

\[
\Delta_p
=
\max_{1\leq n<p^2}\tau(n).
\]

### Theorem OP4m -- PROVED

In the non-heavy outputs of OP4m.0:

1. a paid point star returns at least
   \[
   \boxed{
   \left\lceil
   \frac{
   \left\lfloor\lambda/\mu\right\rfloor+1
   }{
   q(q+1)\Delta_p^\star
   }
   \right\rceil
   }
   \]
   distinct product-carry signatures or anchor-specific cross-carry
   levels;
2. a point-disjoint defect matching returns at least
   \[
   \boxed{
   \left\lceil
   \frac{
   \left\lceil P/(3\lambda)\right\rceil
   }{\Delta_p}
   \right\rceil
   }
   \]
   distinct exact canonical
   \((\text{channel profile},\text{product-carry signature})\)
   records.

Every record retains at least one paid current source factor.

### Proof

In the star case, apply OP1d to the \(M_z\) distinct real triples
through \(z\).  Its channel-pair extraction and divisor occupancy give
at least

\[
\left\lceil
\frac{M_z}{q(q+1)\Delta_p^\star}
\right\rceil
\]

records.  Insert the OP4m.0 lower bound for \(M_z\).

In the matching case, give each selected real factor its canonical
OP4j profile and product-carry signature.  The selected endpoint pairs
are disjoint because the full triples are point-disjoint.  The OP4j
divisor argument therefore bounds every exact profile/signature fibre
by \(\Delta_p\).  No switch-support assertion is needed.  Divide the
OP4m.0 matching bound by this capacity. \(\square\)

The selected factors need not retain a fixed fraction of \(P\); the
theorem asserts signature count and preserves each selected factor's
actual payment.  Any later weighted recurrence argument must use those
actual factor payments rather than assigning the deleted mass to the
matching.

## State-qualified signature interface

Use provenance roles distinct from the OP3k correction-centre and OP4k
rank-three-blocker roles:

\[
\mathsf{defect\mbox{-}star},
\qquad
\mathsf{defect\mbox{-}matching}.
\]

A returned signature at snapshot \(\omega\) contributes

\[
(\omega,\mathsf{role},\sigma)
\]

to the extended finite ledger.  If
\(\Sigma_{\rm star}\) and \(\Sigma_{\rm match}\) are the two finite
defect-signature universes, extend OP4k's role-tagged universe by the
disjoint union

\[
\bigl(
\{\mathsf{defect\mbox{-}star}\}\times\Sigma_{\rm star}
\bigr)
\;\dot\cup\;
\bigl(
\{\mathsf{defect\mbox{-}matching}\}\times\Sigma_{\rm match}
\bigr).
\]

The total number of strict ledger-growth rounds is therefore at most

\[
\boxed{
|\Omega|
\bigl(
|\Sigma_{\rm fan}|
+|\Sigma_3|
+|\Sigma_{\rm star}|
+|\Sigma_{\rm match}|
\bigr).
}
\]

The proof of OP4k applies verbatim:
either a current-new signature grows the ledger or one current-old
signature fibre is returned with its paid current source factors.
The role tag prevents an equal numerical carry tuple from identifying
a correction fan, a protected blocker, and a current defect.

For a point-disjoint matching whose factors all have payment at most
\(\mu\), an old exact profile/signature fibre contains at most
\(\Delta_p\) factors and hence payment at most

\[
\boxed{\mu\Delta_p.}
\]

Thus excessive recurrent matching payment forces a heavy factor or a
new defect token.  The analogous star statement holds after OP1d's
endpoint-disjoint extraction with capacity
\(\mu\Delta_p^\star\).

Replacing \(B_{\rm all}\) in OP4k.3 by the displayed extended token
capacity gives the same exact OP3b finite-descent bound.

## Exact interface after OP4m

OP4l's paid off-core and Hall-reuse outputs are no longer unclassified
factor families.

1. They contain one heavy paid current factor; or
2. they expose a paid point-star carry family; or
3. they expose quantitatively many exact carry signatures on
   point-disjoint current defects.

The remaining arithmetic frontier is recurrence of the role-tagged
defect signatures or treatment of one heavy paid factor.  Generic
gain-to-source payment and generic paid-factor geometric routing are
both complete.

`scripts/verify_phase_defect_router.py` exhausts all
\(\{0,1,2\}\)-weighted three-uniform hypergraphs on five abstract
points for the OP4m.0 star/matching bounds.  On every real
non-single-channel factor for \(p=11\), it checks heavy-factor,
paid-star, low-load matching, and canonical signature-capacity
outputs.
