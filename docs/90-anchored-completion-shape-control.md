# Anchored affine-triangle control for exact completion

PX158--PX159 separate the old and completion reservoirs and encode projection
collisions as mixed conflicts.  This chapter performs two further checks.

1. The projection-collision system satisfies the one-new-edge hypotheses of the
   Joos--Mubayi--Smith covering theorem.
2. The pseudorandom almost-matching from PX141 can simultaneously control every
   affine-triangle completion anchored at one prospective new edge.

The second point isolates the only repeated-shape mechanism involving exactly
one completion edge.

## 1. Projection collisions are mixed-bounded

Use the duplicated host from PX158, let \(d=p\), and let
\(\mathcal D_{\rm proj}\) consist of all projection-collision pairs

\[
\{e_0(x,y),e_1(x',y')\}.
\]

Every conflict has \(j_1=j_2=1\).

## Theorem PX160 -- PROVED USING AN EXTERNAL COVERING THEOREM

Fix \(\varepsilon\in(0,1)\) and any fixed conflict-size parameter
\(\ell\ge4\).  For all sufficiently large primes, the duplicated host and
\(\mathcal D_{\rm proj}\) satisfy the mixed-bounded hypotheses of the
Joos--Mubayi--Smith conflict-free covering theorem.

Consequently, if \(\mathcal C\) is any
\((p,\ell,\varepsilon)\)-bounded conflict system on \(\mathcal H_1\), there is
a row-perfect matching

\[
M\subseteq\mathcal H_1\cup\mathcal H_2
\]

which is \(\mathcal C\cup\mathcal D_{\rm proj}\)-free.  Its projection is a
perfect matching of the original strong-complete host, and its old-reservoir
part is \(\mathcal C\)-free.

### Proof

The host conditions follow from PX158:

\[
\delta_P(\mathcal H_1)=\Delta(\mathcal H_1)=p,
\qquad
\Delta_2(\mathcal H_1)=1,
\]

\[
\Delta_R(\mathcal H_2)=\delta_P(\mathcal H_2)=p,
\qquad
d_{\mathcal H_2}(x,v)\le1.
\]

It remains to check the mixed conflict conditions from the one-new-edge
version of the covering theorem.  A conflict containing a fixed completion row
\(x\) has unavoidability \(p^{-1}\).  PX158 gives

\[
A((\mathcal D_{\rm proj})_x)
=
\frac{p(3p-2)}p
=
3p-2
\le p^{1+\delta}
\]

for every fixed \(\delta>0\) and sufficiently large \(p\).  This is the
required \((E2)\) estimate for \(j_1=j_2=1\).

If one old edge is fixed, at most three completion edges in row \(x\) collide
with it, so the weighted link is at most

\[
\frac3p\le p^{-\varepsilon},
\]

which is \((E3)\).  For one fixed completion edge, its old-edge degree is

\[
3p-2\le\ell p,
\]

which is \((E5)\).  Conditions \((E4)\) and \((E6)\) are vacuous in this
\((1,1)\) system.  The external covering theorem now gives the row-perfect
matching, and PX159 gives its projection. \(\square\)

PX160 solves exact-cover bookkeeping, but it does not assert that a geometric
or affine-shape property imposed only on \(\mathcal H_1\) survives after the
completion edges are added.

## 2. Anchored affine-triangle weights

Let

\[
\sigma=(r,t,s)
\]

be a compatible affine-triangle shape, so

\[
r\notin\{0,1,-1\},
\qquad
t,s\notin\{0,1\},
\]

and

\[
t\ne\pm rs,
\qquad
t-1\ne\pm r(s-1).
\]

An ordered occurrence has the form

\[
(u,a),
\quad
(u+h,a+rh),
\quad
(u+th,a+srh),
\qquad h\ne0.
\]

Fix a prospective completion edge \(e\) and one of the three roles
\(i\in\{0,1,2\}\).  For a matching \(M\) in the old host, write

\[
A_{e,\sigma,i}(M)
\]

for the number of labelled occurrences of shape \(\sigma\) in which \(e\)
occupies role \(i\) and the other two edges belong to \(M\).

## Theorem PX161 -- PROVED USING THE PX141 EXTERNAL INPUT

For every fixed \(\eta\in(0,1)\), all sufficiently large primes have an
almost-perfect matching \(M\) satisfying all conclusions of PX141 and,
simultaneously, the uniform anchored estimate

\[
\boxed{
A_{e,\sigma,i}(M)\le p^\eta
}
\]

for every host edge \(e\), every compatible affine shape \(\sigma\), and every
role \(i\).

Thus one prospective completion edge can create at most

\[
3p^\eta
\]

new occurrences of any fixed affine shape using two old edges.

### Proof

Fix \((e,\sigma,i)\).  Define a two-uniform tuple weight
\(\theta_{e,\sigma,i}\) on pairs of old host edges by counting the nonzero
steps \(h\) which, together with the anchored edge \(e\), produce the given
labelled occurrence.  Exact affine parametrisation gives

\[
\theta_{e,\sigma,i}(\mathcal H_p)=p-1.
\]

A pair has weight at most two, and fixing one member of the pair leaves weight
at most two.  These are the exact finite counts checked by the verifier.

The raw total \(p-1\) is too small for direct application of the pseudorandom
matching theorem.  Pad it as in PX141.  Let \(J_e\) be the indicator weight on
all two-edge matchings whose four-coordinate vertices are disjoint from
\(e\).  There are

\[
(p-1)(p-3)
\]

individual host edges disjoint from \(e\), and therefore

\[
J_e(\mathcal H_p)=\Theta(p^4),
\qquad
\|J_e\|_1=O(p^2),
\qquad
\|J_e\|_2=1.
\]

Put

\[
\alpha=p^{-2+\eta/2},
\qquad
W_{e,\sigma,i}=\theta_{e,\sigma,i}+\alpha J_e.
\]

Then

\[
W_{e,\sigma,i}(\mathcal H_p)=\Theta(p^{2+\eta/2}),
\]

while every rank-one concentration norm is \(O(p^{\eta/2})\), and every
rank-two atom has bounded weight.  Hence, after reducing the tracking exponent
by a fixed factor depending on \(\eta\), this is a trackable rank-two test
function in the Ehard--Glock--Joos theorem used by PX141.

There are only

\[
O(p^2)\cdot O(p^3)\cdot3=O(p^5)
\]

anchored tests, so they may all be included simultaneously with the secant,
triangle, and matching-size tests from PX141.  The resulting matching obeys

\[
W_{e,\sigma,i}(M)=O(p^{\eta/2}),
\]

uniformly.  Since \(\theta\le W\), this is at most \(p^\eta\) for sufficiently
large \(p\), proving the theorem. \(\square\)

## 3. What remains

PX161 removes concentrated repeated shapes supported by one completion edge
and two old edges.  The remaining completion terms involve at least two new
edges:

- two new edges and one old edge;
- three new edges.

Their expected fixed-shape loads have the correct scale under a pseudorandom
completion, but obtaining simultaneous tail bounds for all \(O(p^3)\) shapes
is still the central exact-completion problem.  A successful conflict encoding
must use higher-arity repeated-shape conflicts or a direct concentration theorem;
pairwise repeated-occurrence conflicts have insufficient polynomial margin in
the covering theorem's raw degree conditions.

## Verification

Run

```bash
python scripts/verify_product_anchored_triangle_weights.py
```

The verifier checks compatibility, anchored mass, pair multiplicity, link
weights, and the clean padding reservoir through prime order thirteen.
