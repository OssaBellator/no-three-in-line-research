# Bucketed exact pseudorandom completion

PX141 gives a pseudorandom almost-perfect matching in the strong-complete host,
PX158--PX160 encode exact completion in a duplicated reservoir, and PX161
controls affine-triangle occurrences supported by one completion edge and two
old edges.  This chapter closes the remaining repeated-shape bookkeeping by
bucketing occurrences before they are presented to the conflict-free covering
theorem.

The point of the buckets is quantitative.  There are three free affine-shape
parameters for triangles.  After one completion row is fixed, the raw repeated-
shape count exceeds the mixed-conflict threshold by two powers of \(p\).  If
\(L\) occurrences are required to lie in one of \(p^\theta\) buckets, the count
acquires the factor

\[
p^{-\theta(L-1)}.
\]

Taking \(L\) fixed but large enough that

\[
\theta(L-1)>2
\]

creates the required polynomial margin while allowing \(p^\theta\) occurrences
of one shape in the final matching.

Throughout, let

\[
e(x,y)=(x,y,x-y,x+y)
\]

be a projected host edge.  Reservoir labels \(0,1\) indicate the old and
completion copies from PX158.

## 1. Balanced buckets

Fix \(\theta\in(0,1)\), put

\[
m=\lceil p^\theta\rceil,
\]

and partition \(\mathbb F_p\) into cells

\[
I_1,\ldots,I_m
\]

whose sizes differ by at most one.  Write \(\kappa(a)\) for the cell containing
\(a\).  Thus

\[
|I_b|\le 2p^{1-\theta}
\]

for all sufficiently large \(p\).

For a nonzero step \(h\), an allowed secant slope \(r\notin\{0,1,-1\}\), and a
base point \((u,a)\), write

\[
S(r;u,a,h)
=
\bigl((u,a),(u+h,a+rh)\bigr).
\]

Its **secant bucket** is

\[
\beta_2(u,a,h)=(h,\kappa(a)).
\]

There are at most

\[
2p^{1+\theta}
\]

secant buckets.

For a compatible affine-triangle shape

\[
\sigma=(r,t,s),
\]

write

\[
T(\sigma;u,a,h)
=
\bigl(
(u,a),
(u+h,a+rh),
(u+th,a+srh)
\bigr).
\]

Its **triangle bucket** is

\[
\beta_3(u,a,h)=\kappa(a).
\]

There are \(m\le2p^\theta\) triangle buckets.

The reservoir pattern of an occurrence records whether each of its two or
three edges lies in \(\mathcal H_1\) or \(\mathcal H_2\).  An occurrence is
called **new** when its pattern is not identically zero.

## 2. Local algebraic degrees

### Lemma PX162a -- PROVED

Fix one secant slope and one secant bucket.  Every selected projected edge lies
in at most two ordered secant occurrences in that bucket.

### Proof

If the edge is in the first role, its row and image determine \(u,a\), while the
bucket determines \(h\).  If it is in the second role, the same bucket again
determines \(h\), and then

\[
u=x-h,
\qquad
a=y-rh.
\]

There is at most one occurrence in each role.  Reservoir duplication cannot
increase the degree inside a matching because the two copies of a projected
partner use the same row.  \(\square\)

### Lemma PX162b -- PROVED

Fix one compatible triangle shape and one triangle bucket.  Any two selected
projected edges lie together in at most six ordered triangle occurrences.

### Proof

Assign the two edges to two distinct roles among the three ordered roles.  There
are six assignments.  For one assignment, the two row equations determine
\(u,h\), and the image equations determine \(a\) and test compatibility with the
third role.  Thus each assignment produces at most one occurrence. \(\square\)

These two local bounds are the deterministic extraction step used after the
covering theorem.

## 3. Bucket packing conflicts

Fix an integer \(L\ge6\).  Reservoir patterns are kept homogeneous inside every
conflict; this costs only a constant factor and makes the old/new edge counts
fixed.

### Secant packing conflicts

For one slope \(r\), one secant bucket \(b\), and one nonzero reservoir pattern
on two roles, take \(L\) pairwise edge-disjoint new secant occurrences with the
same \(r,b\).  Their union is a conflict.

There are three possible reservoir patterns.  If one pattern contains \(k\)
completion edges per occurrence, then every conflict has

\[
j_2=kL,
\qquad
j_1=(2-k)L.
\]

### Triangle packing conflicts

For one compatible shape \(\sigma\), one triangle bucket \(b\), and one nonzero
reservoir pattern on three roles, take \(L\) pairwise edge-disjoint new triangle
occurrences with the same \(\sigma,b\).  Their union is a conflict.

There are seven reservoir patterns.  If the pattern contains \(k\) completion
edges, then

\[
j_2=kL,
\qquad
j_1=(3-k)L.
\]

### Triangle star conflicts

Fix a shape, bucket, anchor role, anchor reservoir, and homogeneous reservoir
pattern on the two nonanchor roles.  Take \(L\) triangle occurrences which
share the anchor edge and whose two-edge petals are pairwise disjoint.

We include the star when either

1. the anchor is old, or
2. the anchor is new and at least one petal role is new.

Thus every included star contains at least two completion edges.  The excluded
case is exactly one new anchor with two old petals in every occurrence; PX161
controls that sector directly.

## Theorem PX162 -- PROVED USING AN EXTERNAL COVERING THEOREM

For every fixed \(\theta>0\) and sufficiently small covering exponent
\(\varepsilon>0\), choose \(L\) so that

\[
\boxed{
\theta(L-1)>2+2\varepsilon.
}
\]

Then the union

\[
\mathcal D_{\rm bucket}
\]

of all secant packing, triangle packing, and included triangle star conflicts is
\((p,3L,\varepsilon)\)-simply bounded in the duplicated host.

Equivalently, it satisfies the mixed-bounded conditions of the
Joos--Mubayi--Smith conflict-free covering theorem with polynomial margin.

### Proof: secant packing counts

Fix a completion row \(x\).  For one distinguished secant occurrence containing
that row and one fixed secant bucket, there are

\[
O\left(\frac{p^2}{(p-1)m}\right)
\]

choices of \((u,a,h)\).  Every further occurrence in the same bucket has

\[
O\left(\frac{p^3}{(p-1)m}\right)
\]

choices.  Summing over the \(O(p)\) slopes and the \(O((p-1)m)\) buckets gives

\[
\left|(\mathcal D_{\rm sec})_x^{(j_1,j_2)}\right|
\le
C_L\frac{p^{3L}}{((p-1)m)^{L-1}}.
\]

Every conflict has unavoidability \(p^{-j_2}\), and
\(j_1+j_2=2L\).  Therefore

\[
A\left((\mathcal D_{\rm sec})_x^{(j_1,j_2)}\right)
\le
C_L p^{j_1+1-\theta(L-1)}.
\]

Prescribing \(j'\) old edges removes at least \(j'\) scalar choices.  Prescribing
a second completion row removes one more.  Hence

\[
\Delta^A_{j',0}
\le
C_L p^{j_1-j'+1-\theta(L-1)},
\]

and

\[
A\left((\mathcal D_{\rm sec})_{x,y}^{(j_1,j_2)}\right)
\le
C_L p^{j_1-\theta(L-1)}.
\]

The weaker inequality \(\theta(L-1)>1+2\varepsilon\) would already suffice for
this sector.

### Proof: triangle packing counts

There are \(O(p^3)\) compatible shapes.  In one fixed triangle bucket, a
distinguished occurrence containing row \(x\) has

\[
O(p^2/m)
\]

choices, while every further occurrence has \(O(p^3/m)\) choices.  Summing over
shapes and buckets gives

\[
\left|(\mathcal D_{\rm tri})_x^{(j_1,j_2)}\right|
\le
C_L\frac{p^{3L+2}}{m^{L-1}}.
\]

Since \(j_1+j_2=3L\), weighting by \(p^{-j_2}\) yields

\[
A\left((\mathcal D_{\rm tri})_x^{(j_1,j_2)}\right)
\le
C_Lp^{j_1+2-\theta(L-1)}.
\]

Again, fixing \(j'\) old edges removes at least \(j'\) scalar choices, and a
second completion row removes one more.  Thus

\[
\Delta^A_{j',0}
\le
C_Lp^{j_1-j'+2-\theta(L-1)},
\]

\[
A\left((\mathcal D_{\rm tri})_{x,y}^{(j_1,j_2)}\right)
\le
C_Lp^{j_1+1-\theta(L-1)}.
\]

The displayed choice of \(L\) gives the required \(p^{-\varepsilon}\) margins.

### Proof: triangle star counts

After fixing the shape, anchor role, and reservoir pattern, one star is
parametrised by

\[
(r,t,s),
\qquad
\text{the anchor edge},
\qquad
h_1,\ldots,h_L.
\]

Hence a fixed completion row lies in at most

\[
C_Lp^{L+4}
\]

stars.  Prescribing \(j'\) old edges removes at least \(j'\) of these scalar
choices: in a homogeneous included pattern there is at most one old petal per
occurrence, apart from a possible common old anchor.  Two fixed completion rows
remove at least two choices.  Consequently

\[
A\left((\mathcal D_{\rm star})_x^{(j_1,j_2)}\right)
\le
C_Lp^{j_1+3-L},
\]

\[
\Delta^A_{j',0}
\le
C_Lp^{j_1-j'+3-L},
\]

and

\[
A\left((\mathcal D_{\rm star})_{x,y}^{(j_1,j_2)}\right)
\le
C_Lp^{j_1+2-L}.
\]

Since \(L\ge6\), these estimates have more than the required margin.  Every
bucket conflict has at least two completion edges, so the one-new-edge
conditions are vacuous.  This proves the theorem. \(\square\)

## 4. Extraction from a conflict-free perfect matching

Apply the Joos--Mubayi--Smith covering theorem to

\[
\mathcal D_{\rm proj}\cup\mathcal D_{\rm bucket},
\]

where \(\mathcal D_{\rm proj}\) is the projection-collision system from PX160.
In the first-stage pseudorandom matching, simultaneously track the PX141
secant and triangle weights and all PX161 anchored triangle weights.  These are
polynomially many trackable functions and may be included in the same
application of the external matching theorem.

Let \(M=M_0\cup M_1\) be the resulting row-perfect matching.  PX159 projects it
to a perfect matching of the original strong-complete host.

### Secants

Fix a slope and one secant bucket.  For each of the three reservoir patterns,
the graph of new secant occurrences has matching number below \(L\).  By PX162a
its maximum degree is at most two.  A maximal matching therefore covers all its
edges with at most \(2(L-1)\) vertices, giving at most \(4(L-1)\) occurrences.
Summing over the three patterns gives at most

\[
12(L-1)
\]

new occurrences per secant bucket.

There are at most \(2p^{1+\theta}\) secant buckets, so

\[
\mu_{\rm new}(r)
\le
24(L-1)p^{1+\theta}.
\]

### Triangles

Fix a shape and one triangle bucket.  In each of the seven reservoir patterns,
the new-occurrence three-graph has matching number below \(L\).  The union
therefore has a vertex cover of size at most

\[
21(L-1).
\]

For an old anchor edge, every incident new occurrence belongs to one of at most
nine homogeneous star sectors.  Each link graph has matching number below
\(L\) and maximum degree at most six by PX162b, so the anchor degree is at most

\[
108(L-1).
\]

For a new anchor, the sectors containing another new edge satisfy the same
bound.  The remaining sector has the new anchor and two old petals.  PX161
bounds those occurrences by \(3p^\alpha\), where \(\alpha>0\) is the tracking
exponent used in the first stage.  Hence every edge in the vertex cover has
degree at most

\[
3p^\alpha+108(L-1).
\]

The number of new occurrences of one shape in one triangle bucket is therefore
at most

\[
21(L-1)\bigl(3p^\alpha+108(L-1)\bigr).
\]

Summing over at most \(2p^\theta\) triangle buckets gives

\[
\tau_{\rm new}(\sigma)
\le
C_Lp^{\theta+\alpha}.
\]

## Theorem PX163 -- PROVED USING EXTERNAL MATCHING THEOREMS

For every fixed \(\eta>0\), all sufficiently large primes \(p\) have a strong
complete mapping

\[
f_p:\mathbb F_p\to\mathbb F_p
\]

such that

\[
\boxed{
\mu(f_p)\le p^{1+\eta},
\qquad
\tau(f_p)\le p^\eta.
}
\]

### Proof

Choose

\[
\theta=\alpha=\eta/3
\]

and then choose \(L\) satisfying PX162.  Track the PX141 old secant and triangle
weights with exponent \(\alpha\), and the PX161 anchored weights with the same
exponent.  The old matching has

\[
\mu_{\rm old}(r)=O(p),
\qquad
\tau_{\rm old}(\sigma)\le p^\alpha.
\]

The extraction bounds above give

\[
\mu_{\rm new}(r)=O_L(p^{1+\theta}),
\qquad
\tau_{\rm new}(\sigma)=O_L(p^{\theta+\alpha}).
\]

Since

\[
\theta<\eta,
\qquad
\theta+\alpha=2\eta/3<\eta,
\]

all constants are absorbed by the displayed powers for sufficiently large
\(p\).  \(\square\)

This is an exact, not almost-perfect, pseudorandom strong-complete seed theorem.
It replaces the former deterministic seed conjecture by a weaker but
asymptotically sufficient subpower statement.

## Corollary PX164 -- PROVED

For every fixed \(\eta>0\) and all sufficiently large primes, there is an affine-
orbit probability distribution on strong-complete mappings whose normalized
rank-one, rank-two, and rank-three cylinder constants satisfy

\[
\boxed{
K_1=1,
\qquad
K_2\le p^\eta,
\qquad
K_3\le p^\eta.
}
\]

Moreover, the conditional two-stage protected-rainbow construction of PX131
has joint rank-three cylinder constant at most \(p^{2\eta}\).

### Proof

Apply PX129 to the seed from PX163, replacing \(\eta\) there by a smaller fixed
exponent if necessary.  Then apply the conditional composition argument from
PX131. \(\square\)

## 5. Boundary after exact completion

PX163 closes the exact strong-complete seed bottleneck at subpower loss.  It
does not by itself finish the all-\(n\) product theorem.  The remaining task is
to insert the \(p^{o(1)}\) protected cylinder constants into the direction-
stratified rectangle conflict estimates and choose the protected-height cutoff
so that the polynomial high-direction codegree saving dominates every
subpower loss.

This is now an exponent-balancing problem rather than an exact-completion or
lattice-absorption problem.

## Verification

Run

```bash
python scripts/verify_product_bucketed_completion_conflicts.py
```

The verifier checks balanced bucket fibres, secant local degree, triangle pair
codegree, row-role fibre bounds, and the symbolic exponent choices at prime
orders \(7,11,13,17\).  The asymptotic existence conclusion uses the
Ehard--Glock--Joos pseudorandom matching theorem and the Joos--Mubayi--Smith
conflict-free covering theorem.
