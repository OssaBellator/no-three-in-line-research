# Geometric labels for implication factors

The OP4d implication bicycle retains the OP1 ancestor factor of every
edge.  OP4e can use the rational inverse classification only when those
local factors induce one consistent quotient label at every repeated
literal.

There are two separate issues.

1. A geometric factor must first supply an exact rational transition,
   or an exact carry alternative.
2. The transitions supplied by different factors must agree at their
   shared Boolean literals.

The first issue is finite-field geometry.  The second is a labelled
constraint problem.  A Boolean implication by itself solves neither
one.  This note supplies both exact interfaces.

## Factor notation

Let \(p\) be an odd prime.  All affine coordinates are represented in
\(\{1,\ldots,p-1\}\), and

\[
H_a
=
\left\{
\left(x,\left\langle\frac ax\right\rangle_p\right):
x\in\mathbb F_p^\times
\right\}.
\]

For a point \(P=(x,y)\in H_a\), retain the product carry

\[
\kappa_a(P)=\frac{xy-a}{p}.
\]

Take a distinct modularly collinear triple.  Its channel profile is
one of:

1. \(3\): all three points lie on one channel;
2. \(2+1\): two points lie on \(H_a\) and one lies on \(H_b\);
3. \(1+1+1\): the three points lie on three different channels.

The first profile is impossible.  A line meets the nondegenerate
conic \(xy=a\) in at most two affine points.

For the \(2+1\) profile write

\[
P_x=\left(x,\left\langle\frac ax\right\rangle_p\right),
\qquad
P_u=\left(u,\left\langle\frac au\right\rangle_p\right),
\qquad
B_z=\left(z,\left\langle\frac bz\right\rangle_p\right),
\]

and put

\[
r=\frac ba,\qquad c=\frac zx,\qquad g=\frac ux.
\]

## OP4g -- factor label-or-carry theorem

### Theorem OP4g -- PROVED

Every distinct OP1 ancestor factor has exactly one of the following
two lossless records.

1. **Two-channel rational record.**  In channel profile \(2+1\),
   both endpoint orientations give rational inverse records.  For the
   displayed orientation,
   \[
   c\in
   D_r=\mathbb F_p^\times\setminus\{1,r\},
   \qquad
   \boxed{
   g=F_r(c)=\frac{c(1-c)}{r-c}.
   }
   \]
   Put
   \[
   c^\dagger
   =
   \tau_r(c)
   =
   \frac{r(c-1)}{c-r}.
   \]
   Then
   \[
   F_r(c^\dagger)=g,
   \qquad
   \boxed{cc^\dagger=rg}.
   \]
   Thus, for every multiplicative subgroup
   \(H\leq\mathbb F_p^\times\), the quotient labels
   \[
   A=cH,\quad
   B=c^\dagger H,\quad
   C=gH,\quad
   R=rH
   \]
   satisfy
   \[
   \boxed{B=RCA^{-1}.}
   \]

   Reversing the two same-channel endpoints gives
   \[
   c^-=\frac zu=\frac cg,\qquad
   g^-=g^{-1},
   \]
   and
   \[
   \boxed{
   \{c^-,\tau_r(c^-)\}
   =
   g^{-1}\{c,\tau_r(c)\}.
   }
   \]
   These are the two allowed secant normalizations of the unordered
   factor.

   If the triple is really collinear, its two cross carries agree:
   \[
   \boxed{
   \kappa_z(x)=\kappa_z(u).
   }
   \]
   Hence the rational record also retains one exact CF1 cross-carry
   level.

2. **Three-channel carry record.**  In channel profile \(1+1+1\),
   there is no same-channel endpoint pair and therefore no preferred
   \(F_r\) secant normalization.  Choosing any of the three points as
   the star centre makes the other two points a mixed-channel endpoint
   pair.  The factor returns all three product-carry signatures
   \[
   \boxed{
   \bigl(\kappa_{a_j}(P_j),\kappa_{a_k}(P_k)\bigr),
   \qquad \{i,j,k\}=\{1,2,3\},
   }
   \]
   together with their endpoint channels and chosen centre.

The two-channel record also retains all three star-centre routes.  The
singleton-channel centre gives the same-channel product signature and
the common cross-carry level.  Either repeated-channel centre gives a
mixed-channel product-carry signature.

Consequently, failure to use the rational record never erases the
source factor: the same factor remains available to the OP1d
product/cross-carry router.

### Proof

Real collinearity implies modular collinearity.  In profile \(2+1\),
the modular secant identity is

\[
r x u=z(x+u-z).
\]

Dividing by \(x^2\) gives

\[
rg=c(1+g-c),
\]

or equivalently

\[
(r-c)g=c(1-c).
\]

All coordinates are nonzero.  The two points on \(H_a\) are distinct,
so \(g\ne1\).  If \(c=1\), then the preceding identity gives
\((r-1)g=0\), which is impossible because \(r\ne1\) and \(g\ne0\).
If \(c=r\), it gives \(r(1-r)=0\), also impossible.  Thus
\(c\in D_r\) and the displayed formula for \(F_r\) follows.

The equation determining a normalized anchor parameter at fixed
transition \(g\) is

\[
X^2-(1+g)X+rg=0.
\]

One root is \(c\).  Its other root is

\[
\frac{rg}{c}
=
\frac{r(1-c)}{r-c}
=
\tau_r(c).
\]

Vieta's formula proves \(cc^\dagger=rg\), and substitution proves
\(F_r(c^\dagger)=g\).  Passing to \(H\)-cosets proves the quotient
identity.

For the reverse orientation,

\[
c^-=\frac cg,\qquad g^-=g^{-1}.
\]

Direct substitution gives

\[
\tau_r(c^-)=\frac rc
=
\frac{\tau_r(c)}g,
\]

which proves the reverse-pair formula.

For standard representatives, CF1 gives

\[
\kappa_z(x)
=
\frac{(x-z)(y_u-w)-(b-a)}p,
\]

\[
\kappa_z(u)
=
\frac{(u-z)(y_x-w)-(b-a)}p.
\]

Their difference times \(p\) is the integer determinant of
\(B_z,P_x,P_u\).  It vanishes exactly for a real factor.

Finally, every point satisfies the exact identity

\[
xy=a+p\kappa_a(P).
\]

Choosing each point in turn as centre therefore produces the three
claimed product-carry signatures.  In profile \(1+1+1\), every
endpoint pair is mixed-channel. \(\square\)

## From local root pairs to literal labels

Fix a quotient

\[
Q=\mathbb F_p^\times/H.
\]

For an occurrence \(e:\ell\to\ell'\) whose source factor has channel
profile \(2+1\), OP4g gives two possible secant normalizations.  Each
normalization gives:

\[
R_e\in Q,\qquad
C_e\in Q,\qquad
\{A_e,B_e\}\subseteq Q,
\]

with

\[
A_eB_e=R_eC_e.
\]

The pair is unordered because the occurrence may place either root
label at either endpoint literal.  A chosen record certifies the OP4e
edge precisely when

\[
\{A_\ell,A_{\ell'}\}=\{A_e,B_e\}.
\]

Indeed,

\[
A_{\ell'}=R_eC_eA_\ell^{-1}.
\]

The requirement that one literal receive one label at all of its
occurrences is the essential global condition.

## OP4h -- exact bicycle compatibility gate

Let

\[
\ell_0\longrightarrow\ell_1\longrightarrow\cdots
\longrightarrow\ell_s=\ell_0
\]

be a source-labelled OP4d bicycle containing no unary-saturation
edge.  It has

\[
s\leq4m-2.
\]

### Theorem OP4h -- PROVED

For every fixed quotient \(Q\), there is an exact finite audit with
the following outputs.

1. **Carry output.**  If an occurrence has a three-channel source
   factor, return that occurrence and its three mixed product-carry
   routes.
2. **Root mismatch.**  If the rational occurrences do not have one
   common root coset \(R\), return the first differing occurrence.
   Its full OP4g carry record is retained.
3. **Rational-admissible bicycle.**  Choose one of the two secant
   normalizations at each occurrence and assign one quotient label
   \(A_\ell\) to every used literal so that
   \[
   \{A_\ell,A_{\ell'}\}=\{A_e,B_e\}
   \]
   on every occurrence.  The resulting labels and edge colours
   certify
   \[
   \boxed{
   A_{\ell'}=RC_eA_\ell^{-1}
   }
   \]
   everywhere, so OP4e applies without another geometric hypothesis.
4. **Literal-root mismatch.**  If no such choice exists, return the
   complete finite normalization/propagation conflict table.  Every
   conflict names a literal, an incident source factor, its required
   root pair, and the inconsistent label.

For a fixed normalization vector, compatibility is decided by at most
two linear propagations around the connected bicycle.  Without
pre-oriented provenance, the full audit uses at most

\[
\boxed{2^{s+1}}
\]

linear propagation trials.  If every occurrence already specifies its
secant orientation, only two trials are needed.

### Proof

First check the local product identities and the common root coset.
For a fixed normalization vector, every edge has one unordered pair
\(\{A_e,B_e\}\).

Choose the first edge.  There are at most two ways to place its pair on
its two endpoint literals.  Once one endpoint of any other edge is
labelled, its other endpoint is forced: \(A_e\) forces \(B_e\), and
\(B_e\) forces \(A_e\).  Propagate through the connected edge set.
A repeated literal either receives its existing label or exposes a
specific conflict.  A loop is compatible exactly when
\(A_e=B_e\).

Thus two propagations decide a fixed normalization vector.  There are
at most two OP4g normalizations per occurrence, giving the stated
bound.  If a propagation succeeds, every edge has its two root labels,
and

\[
A_eB_e=RC_e
\]

immediately gives the directed OP4e law.  If every propagation fails,
the collected local contradictions exhaust every allowed
normalization and first-edge placement, proving incompatibility.
\(\square\)

## Exact interface to the remaining frontier

OP4g--OP4h remove the former generic “unlabelled implication factor”
output.

1. A successful audit enters OP4e with literal labels, edge colours,
   one root coset, and source-factor proofs on every occurrence.
2. A three-channel occurrence enters the established mixed
   product-carry router.
3. A root or literal mismatch retains, edge by edge, the exact
   product signatures and cross-carry levels of its source factors.
   [`orbit-phase-syndrome-payment.md`](orbit-phase-syndrome-payment.md)
   supplies the exact payment gate: either the selected bicycle keeps
   factor-conservative current-defect weight or a comparable payment
   escapes to explicit off-core current factors.
   [`orbit-phase-defect-router.md`](orbit-phase-defect-router.md)
   routes that escape to a heavy factor, paid point star, or
   point-disjoint carry-signature family.
4. The audit is exact but can be exponential when the source
   provenance does not orient its secants.  A polynomial orientation
   theorem would improve the decoder runtime, but is not needed for
   the structural alternative.

[`orbit-phase-paid-edge-density.md`](orbit-phase-paid-edge-density.md)
proves OP4i for a selected certified quotient edge.  Protected-bank
gain does not automatically transfer to an implication bicycle.  Once
factor-conservative occurrence payment is supplied, OP4i returns
complete rational-orbit density, one-sided orbit growth with explicit
completion deficits, one heavy repeated source factor, or quantified
product-carry growth.

The next independent endpoints are therefore the RI5
row-column-preserving conversion of the dense fixed-edge output and
recurrence/treatment of the OP4m heavy-factor or paid defect-signature
outputs.
The formerly separate rank-three ledger obligation is closed by
[`orbit-phase-blocker-ledger.md`](orbit-phase-blocker-ledger.md);
its remaining output is one bounded current recurrent blocker fibre.

`scripts/verify_phase_geometric_labels.py` exhausts every modularly
collinear triple in the nonzero grids for
\(p=5,7,11,13\).  It checks the channel trichotomy, both secant
normalizations, exceptional-domain exclusions, rational fibres,
quotient product laws for every quotient order, real cross-carry
equivalence, and all star-centre product-carry records.  It also
compares the fixed-normalization propagation algorithm with brute
force on every small cycle instance and exercises successful,
orientation-dependent, root-mismatch, literal-mismatch, and
three-channel carry outputs.
