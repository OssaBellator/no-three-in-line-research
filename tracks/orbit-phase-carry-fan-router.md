# Carry routing for phase-factor fans

OP3i localizes a paid high-conflict family to wide corrections,
action-literal correction kernels, or variable-rooted factor fans.
Only the last output is directly a family of geometric OP1 checks.
This note converts it, with explicit losses, into the carry objects
already controlled by the
[secant-star](../docs/24-secant-star-carry-dispersion.md) and
[same-channel](../docs/26-same-channel-cross-carries-and-wrap-centers.md)
arithmetic.

The conversion has two finite pigeonhole steps.  A repeated
orbit-block phase contains only \(h\) candidate cells, so one actual
cell anchors many distinct triple factors.  The other two points of
those triples form a secant star through that cell.  After fixing their
two hyperbola channels and extracting an endpoint-disjoint family,
same-channel pairs disperse into anchor-specific cross carries and
mixed-channel pairs disperse into product-carry signatures.  Every
fixed signature has divisor-controlled occupancy.

Thus a paid factor-fan class cannot remain an opaque collection of
numerical carry records.  It forces quantified growth of one named
carry-signature family.

## OP1b -- exact orbit-state and raw-carry ranges

Let

\[
K=\langle\lambda\rangle\leq\mathbb F_p^\times
\]

have order \(h\), let \(C=xK\), and retain the O1 orbit block

\[
A_{C,t}^{(a)}
=
\left\{
\left(u,\left\langle\frac{a}{\lambda^t u}\right\rangle_p\right):
u\in C
\right\},
\qquad
t\in\mathbb Z/h\mathbb Z.
\]

Write

\[
B_C=\bigcup_t A_{C,t}^{(a)}.
\]

For a point \(P=(u,v)\in H_c\), define its product carry by

\[
\kappa_c(P)=\frac{uv-c}{p},
\]

where \(c\in\{1,\ldots,p-1\}\) is the standard representative.  For
\(\alpha\in\{1,\ldots,p-1\}\), define coordinate wraps

\[
W_{\alpha,1}(P)=\left\lfloor\frac{\alpha u}{p}\right\rfloor,
\qquad
W_{\alpha,2}(P)=\left\lfloor\frac{\alpha v}{p}\right\rfloor.
\]

### Lemma OP1b -- PROVED

The O1 block and its raw carry fields satisfy:

1. every state has \(h\) cells;
2. the \(h\) states are pairwise disjoint and partition the
   \(h^2\)-cell block \(B_C\);
3. state \(t\) lies on the single channel
   \[
   H_{a\lambda^{-t}};
   \]
4. for every state cell,
   \[
   \boxed{0\leq\kappa_c(P)\leq p-2;}
   \]
5. for every scalar \(\alpha\),
   \[
   \boxed{
   0\leq W_{\alpha,1}(P),W_{\alpha,2}(P)\leq\alpha-1.
   }
   \]

Consequently, for fixed \(t,c,\alpha\), the raw numerical triple

\[
\bigl(\kappa_c,W_{\alpha,1},W_{\alpha,2}\bigr)
\]

has at most

\[
\boxed{(p-1)\alpha^2}
\]

possible values.

### Proof

Multiplication by \(\lambda^t\) permutes \(C\).  Hence every state uses
the same \(h\) columns and the same \(h\) rows.  If a cell occurred in
states \(s,t\), its row formula would give

\[
\lambda^s=\lambda^t,
\]

so \(s=t\) modulo \(h\).  The \(h\) disjoint states each have \(h\)
cells, proving the block partition.  Multiplying the two coordinates
of a state-\(t\) cell gives \(a\lambda^{-t}\) modulo \(p\), proving the
channel statement.

For standard representatives \(1\leq u,v,c<p\), the congruence

\[
uv\equiv c\pmod p
\]

and \(0<uv<p^2\) give

\[
uv=c+p\kappa_c(P),
\qquad
0\leq\kappa_c(P)\leq p-2.
\]

Finally \(0<\alpha u,\alpha v<\alpha p\), which gives the wrap bounds.
Multiplying the three range sizes proves the cardinality statement.
\(\square\)

The bound is deliberately not called a uniform compression theorem:
it grows with \(p\).  The next lemmas show that factor fans need only
one carry coordinate whose level occupancy is already controlled.

## OP1c -- geometric provenance and point anchoring

Tag every original OP1 factor by its defining real triple.  Under OP2n
restriction, retain that tag on the residual factor.  When identical
residual factors are merged, retain the union of their tag sets.

### Provenance lemma -- PROVED

The OP2g--OP2n reductions preserve pairwise disjoint, nonempty ancestor
sets on every retained factor, and preserve every forbidden literal
whose variable remains in the factor scope.  Consequently, distinct
residual factors sharing a surviving block literal admit distinct
original OP1 triple ancestors sharing the same literal.

### Proof

Initially every factor has one private ancestor.  Satisfied-factor and
subsumption deletions merely discard ancestor sets.  Restriction and
unit reduction do not copy a factor and do not change forbidden values
on surviving variables.  Duplicate merging replaces disjoint tag sets
by their union.  Induction over the reduction trace proves the claim.
\(\square\)

Let \(\mathcal F(B,t)\) be a family of distinct realizable OP1 triple
factors whose forbidden assignment contains the block literal
\((B,t)\), where \(B\) has order \(h\).  Let \(T_Q\) be the real
collinear candidate triple defining factor \(Q\).

### Lemma OP1c -- PROVED

Some cell \(z\in A_{B,t}\) occurs in at least

\[
\boxed{
\left\lceil\frac{|\mathcal F(B,t)|}{h}\right\rceil
}
\]

of the triples \(T_Q\).

More generally, suppose \(\mathcal F(B)\) is a family of distinct OP1
factors containing \(B\) in their scopes but using arbitrary forbidden
phases there.  Then some phase \(t\) and some
\(z\in A_{B,t}\) occur together in at least

\[
\boxed{
\left\lceil\frac{|\mathcal F(B)|}{h^2}\right\rceil
}
\]

factors.

### Proof

If \(Q\) contains the forbidden literal \((B,t)\), realizability of its
canonical OP1 check says that every cell of \(T_Q\cap B\) lies in
\(A_{B,t}\), and this intersection is nonempty.  Thus the incidences
between \(\mathcal F(B,t)\) and the \(h\) state cells number at least
\(|\mathcal F(B,t)|\).  Pigeonhole proves the first box.

For the second statement, first pigeonhole the \(h\) forbidden phases
and then apply the first statement.  Equivalently, pigeonhole directly
over the \(h^2\) cells of the O1 block. \(\square\)

No factor multiplicity is hidden here.  The factors are distinct
geometric triple certificates.  If a weighted implementation merges
identical soft factors, its merged weight must be carried through a
weighted incidence version instead of being expanded into fictitious
copies.

## OP1d -- point-star carry dispersion

Assume the candidate points under consideration lie in a union of
\(q\) distinct modular-hyperbola channels.  Fix a candidate point
\(z\) and a family \(\mathcal T_z\) of \(M\) distinct real collinear
triples

\[
\{z,P,Q\}.
\]

For one channel \(H_c\), put

\[
\Delta_p^{\rm prod}
=
\max_{1\leq N<p^2}\tau(N).
\]

For a same-channel secant through an anchor on a different channel,
use the cross carry from CF1 and put

\[
\Delta_p^{\rm cross}
=
\max_{1\leq N\leq(p-2)^2}\tau(N).
\]

Finally let

\[
\Delta_p^\star
=
\max\{\Delta_p^{\rm prod},\Delta_p^{\rm cross}\}
=p^{o(1)}.
\]

### Theorem OP1d -- PROVED

There are an unordered channel pair and an endpoint-disjoint subfamily
\(\mathcal E\subseteq\mathcal T_z\) such that

\[
\boxed{
|\mathcal E|
\geq
\left\lceil\frac{M}{q(q+1)}\right\rceil.
}
\]

Moreover one of the following holds.

1. The two endpoint channels are distinct, and \(\mathcal E\) occupies
   at least
   \[
   \boxed{
   \left\lceil
   \frac{M}{q(q+1)\Delta_p^\star}
   \right\rceil
   }
   \]
   distinct product-carry signatures.
2. The endpoints lie on one channel different from the channel of
   \(z\), and \(\mathcal E\) occupies at least the same displayed
   number of anchor-specific cross-carry levels.

### Proof

Partition the \(M\) endpoint pairs \(\{P,Q\}\) by their unordered
channel pair.  There are

\[
\binom{q+1}{2}=\frac{q(q+1)}2
\]

types, so one type contains at least

\[
\left\lceil\frac{2M}{q(q+1)}\right\rceil
\]

pairs.

If its channels are distinct, regard the pairs as a bipartite graph.
For a fixed endpoint \(P\), the line \(zP\) meets the other modular
hyperbola in at most two points.  Thus the graph has maximum degree at
most two and its edges split into two matchings.  One matching has at
least half the edges.

If both endpoints lie on one channel, that channel differs from the
channel of \(z\), since one real line cannot contain three points of a
single modular hyperbola.  The endpoint pairs are already disjoint:
one endpoint determines its line through \(z\), and that line has at
most one other point on its channel.

This proves the first box.  In the mixed-channel case, SC1--SC2 show
that a fixed product-carry signature supports at most
\(\Delta_p^{\rm prod}\) endpoint-disjoint pairs.  In the same-channel
case, CF1--CF2 show that a fixed cross-carry level supports at most
\(\Delta_p^{\rm cross}\) real secant pairs.  Divide by the appropriate
occupancy cap and use \(\Delta_p^\star\). \(\square\)

The theorem uses real collinearity only after the modular channel
partition.  It makes no inference from a modular secant to a real
triple.

## OP1e -- factor-fan to carry-signature growth

Let \(B\) be an orbit block of order \(h\).  Suppose a correction
centre has a variable-rooted fan of \(t\) distinct OP1 factors through
\(B\), as in OP3g.  The same conclusion applies to a geometrically
faithful OP2g--OP2n residual fan by choosing distinct ancestors using
OP1c.  Assume all candidate cells in those factors lie in a union of
\(q\) hyperbola channels.

### Theorem OP1e -- PROVED

The factor fan contains a point-anchored, endpoint-disjoint secant
subfamily occupying at least

\[
\boxed{
\left\lceil
\frac{t}{h^2q(q+1)\Delta_p^\star}
\right\rceil
}
\]

distinct product-carry signatures or anchor-specific cross-carry
levels.

The correction centre retains its full individual gain; the displayed
loss applies only to the size of its geometric carry certificate.

### Proof

OP3h first retains at least

\[
\left\lceil\frac th\right\rceil
\]

factors with one forbidden phase on \(B\).  OP1c then finds one cell
in at least

\[
\left\lceil\frac{t}{h^2}\right\rceil
\]

of their triples.  Apply OP1d and its per-signature occupancy bound.
Nested ceiling division gives the displayed integer lower bound.
Nothing changes the gain \(g_i\) attached to the correction centre.
\(\square\)

## OP3j -- paid carry-aware correction router

Retain the hypotheses of OP3f and OP3i.  Suppose:

- every orbit-block order is at most \(h\), where \(h\geq2\);
- every factor has rank at most \(r\) (with \(r=3\) for OP1);
- the candidate universe uses at most \(q\) hyperbola channels; and
- every residual factor fan retains the OP1 ancestor provenance of
  OP1c; and
- \(D>s\,t(t-1)\).

### Theorem OP3j -- PROVED

For a correction family of total individual gain \(G\), at least one
of the following holds.

1. An executable correction batch has gain at least
   \[
   \boxed{\frac{G}{2D}.}
   \]
2. Wide high-degree corrections carry gain greater than
   \[
   \boxed{\frac G4.}
   \]
3. One fixed action-literal correction-kernel type carries gain greater
   than
   \[
   \boxed{\frac G{12},}
   \]
   and every paid centre has a repeated action-literal kernel of size
   at least
   \[
   \boxed{
   \left\lceil\frac{t}{r(h-1)}\right\rceil.
   }
   \]
4. Factor-fan centres carry gain greater than
   \[
   \boxed{\frac G{12},}
   \]
   and every paid centre has a point-star carry certificate with at
   least
   \[
   \boxed{
   \left\lceil
   \frac{t}{h^2q(q+1)\Delta_p^\star}
   \right\rceil
   }
   \]
   distinct product or cross-carry signatures.

### Proof

Apply OP3f and then OP3i.  Its variable-overlap and single-factor
classes are the action-literal outputs of OP3h.  The variable class has
kernel size at least

\[
\left\lceil\frac{t}{h-1}\right\rceil,
\]

while the single-factor class has size at least

\[
\left\lceil\frac{t}{r(h-1)}\right\rceil.
\]

The latter is a uniform lower bound for either class.  If OP3i returns
the factor-fan class, apply OP1e to every paid centre.  OP3i supplies
the stated gain fractions. \(\square\)

## Interface after OP1b--OP1e and OP3j

The numerical carry fields now have an exact role in the phase decoder.

1. Raw carry records have explicit finite ranges, but no false
   \(p\)-independent compression is claimed.
2. A paid geometric factor fan cannot concentrate indefinitely on one
   raw signature: it creates a quantified family of product or
   anchor-specific cross-carry signatures.
3. Action-literal correction kernels and wide corrections remain
   separate paid structured outputs instead of being forced into an
   inapplicable secant-star theorem.
4. Every loss from total correction gain to geometric signature count
   is explicit in \(D,s,t,h,q\), and \(\Delta_p^\star\).

[`orbit-phase-signature-recurrence.md`](orbit-phase-signature-recurrence.md)
performs the cross-round accounting.  OP3k conserves split gain and
returns either state-qualified first-exposure ledger growth or one
paid high-reuse signature among centres at the current snapshot.
Corrections from different snapshots are not combined.  OP3l then
returns a deeper action-literal kernel or a paid current
support-disjoint correction bank.  OP4a--OP4c project that bank exactly
to 2-SAT plus explicit rank-three transversals.  The remaining
termination theorem is arithmetic: classify the repeated
action-literal kernels, contradictory implication chains,
rank-three transversals, and wide OP2n action CSPs.  Bounded-denominator
absorbers are still needed only when the aligned carry identities place
a subsequent closure step in the perfect-interpolation branch.

`scripts/verify_phase_carry_fan_router.py` checks O1 block partitions
and carry ranges, enumerates real OP1 factors in small bounded-channel
universes, verifies the phase-to-point pigeonhole, and checks the
product/cross-carry occupancy and endpoint-disjoint extraction bounds.
