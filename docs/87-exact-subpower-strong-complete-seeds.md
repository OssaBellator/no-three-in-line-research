# Exact subpower strong-complete seeds by bucketed covering

PX141 gives a pseudorandom almost-perfect matching in the strong-complete
exact-cover host. This chapter upgrades that result to a genuine perfect
matching by combining balanced buckets with the exact covering theorem of Joos,
Mubayi and Smith, *Conflict-free hypergraph matchings and coverings* (published
online in 2025).

The conclusion is weaker than the constant-multiplicity orbit conjecture, but it
is asymptotic and exact.

## 1. The duplicated-reservoir host

Let

\[
P=\{R_x:x\in\mathbb F_p\}.
\]

Take two disjoint copies of the other three exact-cover parts,

\[
Q=C^{(1)}\cup D^{(1)}\cup S^{(1)},
\qquad
R=C^{(2)}\cup D^{(2)}\cup S^{(2)}.
\]

For \(i=1,2\), put

\[
e_i(x,y)=
\{R_x,C_y^{(i)},D_{x-y}^{(i)},S_{x+y}^{(i)}\}.
\]

Let \(\mathcal H_i\) be the set of all such edges. Then \(\mathcal H_1\)
has one vertex in \(P\) and three in \(Q\), while \(\mathcal H_2\) has one
vertex in \(P\) and three in \(R\), exactly as required by the covering
theorem.

Add a mixed projection-collision conflict whenever an edge of \(\mathcal H_1\)
and an edge of \(\mathcal H_2\) use the same underlying column, difference, or
sum label. A \(P\)-perfect matching avoiding these conflicts projects to \(p\)
edges of the original host with distinct row, column, difference, and sum
labels, and hence to a strong-complete mapping.

## 2. Balanced line buckets

Fix a real number \(\beta>0\). Partition \(\mathbb F_p\) into

\[
B_0=\lceil p^\beta\rceil
\]

sets of sizes differing by at most one.

For every allowed affine slope

\[
r\notin\{0,1,-1\},
\]

every affine line \(y=rx+c\), and every row bucket, declare a conflict whenever
\(q_0\) projected host points on that line have all their row labels in that
bucket. Only sets which are matchings in the duplicated host are retained.

## Lemma PX148 -- PROVED

For fixed \(q_0\), the lifted line-bucket conflict hypergraphs obey the ordinary
and mixed boundedness conditions of the Joos--Mubayi--Smith theorem with a
positive power margin whenever

\[
\boxed{\beta(q_0-1)>1.}
\]

Every conflict-free projected matching has at most

\[
L=(q_0-1)B_0
\]

points on any allowed-slope affine line. Consequently, for every allowed slope,

\[
\boxed{
\mu_f(r)\le p(L-1).
}
\]

### Proof

There are \(p\) choices of slope, \(p\) choices of intercept, \(B_0\) buckets,
and at most \((2p/B_0)^{q_0}\) labelled row choices in one bucket. Thus the
number of conflicts is

\[
O\!\left(p^{q_0+2}B_0^{1-q_0}\right).
\]

After fixing one host edge, the line intercept is determined once the slope is
chosen, giving

\[
\Delta_1
=O\!\left(p^{q_0}B_0^{1-q_0}\right).
\]

After fixing at least two compatible host edges, the line and bucket are both
determined, and

\[
\Delta_j
=O\!\left((p/B_0)^{q_0-j}\right)
\qquad(2\le j<q_0).
\]

Choosing the inequalities with a small fixed slack gives conditions (C2)--(C3)
for the first reservoir. The same estimates, after multiplying conflicts with
\(j_2\) completion edges by their unavoidability \(p^{-j_2}\), give
(E2)--(E6) for the mixed reservoir. The one-completion-edge case is exactly the
case covered by (E5)--(E6). Constant copy assignments do not change any power of
\(p\).

Avoidance gives the line cap. For one slope, the selected points partition over
its \(p\) affine lines. If their occupancies are \(k_c\), then

\[
\mu_f(r)=\sum_c k_c(k_c-1)
\le(L-1)\sum_c k_c=p(L-1).
\]

\(\square\)

## 3. Buckets of edge-disjoint affine triangles

Fix one compatible affine-triangle shape

\[
\sigma=(r,t,s)
\]

from PX129. An ordered occurrence is determined by its first graph point and
its nonzero row scale

\[
d=x_2-x_1.
\]

Partition \(\mathbb F_p^*\) into

\[
B_1=\lceil p^\gamma\rceil
\]

balanced scale buckets. Declare a conflict whenever \(q_1\) occurrences of one
shape use the same scale bucket and have pairwise edge-disjoint supports. Again
retain only unions which are matchings after projection.

## Lemma PX149 -- PROVED

For fixed \(q_1\), the lifted triangle-bucket conflicts obey the required
ordinary and mixed boundedness conditions with a positive power margin whenever

\[
\boxed{\gamma(q_1-1)>2.}
\]

Suppose also that every allowed-slope line contains at most \(L\) selected
points. Then every conflict-free matching satisfies

\[
\boxed{
\tau_f(\sigma)
\le9(q_1-1)B_1L
}
\]

for every compatible shape \(\sigma\).

### Proof

There are \(O(p^3)\) shapes. For a fixed shape and scale bucket, an occurrence
has \(p^2\) choices of its first point and at most \(2p/B_1\) choices of scale.
Hence a labelled collection of \(q_1\) edge-disjoint occurrences has count

\[
O\!\left(p^{3q_1+3}B_1^{1-q_1}\right).
\]

Fixing one host edge removes two field parameters, so

\[
\Delta_1
=O\!\left(p^{3q_1+1}B_1^{1-q_1}\right).
\]

Fixing two host edges removes four parameters. If they belong to one occurrence,
they also determine its scale bucket; if they belong to different occurrences,
each removes two parameters separately. In either case

\[
\Delta_2
=O\!\left(p^{3q_1-1}B_1^{1-q_1}\right).
\]

For three or more fixed edges, the raw dimension saving is already at least the
required codegree saving; a complete fixed occurrence additionally determines
the shape and bucket. These estimates give (C2)--(C3), and the same
unavoidability calculation as in PX148 gives (E2)--(E6) for every split between
the two reservoirs.

Now form the three-uniform multihypergraph whose vertices are the selected host
edges and whose hyperedges are the ordered occurrences of \(\sigma\) in one
fixed scale bucket. Its matching number is at most \(q_1-1\). A selected edge
belongs to at most \(3L\) occurrences: according to its role, another occurrence
point lies on one of the three fixed slopes

\[
r,
\qquad \frac{s}{t}r,
\qquad \frac{s-1}{t-1}r,
\]

and compatibility makes all three slopes different from \(0,1,-1\). A maximal
matching therefore covers every occurrence and gives at most

\[
3(q_1-1)\cdot3L=9(q_1-1)L
\]

occurrences in the bucket. Sum over the \(B_1\) buckets. \(\square\)

## Theorem PX150 -- PROVED USING AN EXTERNAL COVERING THEOREM

For every fixed \(\eta>0\), all sufficiently large primes \(p\) admit a
strong-complete mapping \(f:\mathbb F_p\to\mathbb F_p\) satisfying

\[
\boxed{
\mu(f)\le p^{1+\eta},
\qquad
\tau(f)\le p^\eta.
}
\]

Consequently the affine-similarity orbit of \(f\) has rank-two and rank-three
cylinder constants at most \(p^\eta\), after increasing the threshold prime if
necessary.

### Proof

It is enough to prove the statement for \(0<\eta<1\). Put

\[
\beta=\gamma=\eta/4.
\]

Choose fixed integers \(q_0,q_1\) so large that

\[
\beta(q_0-1)>1,
\qquad
\gamma(q_1-1)>2,
\]

with additional fixed slack. Let \(\ell\) exceed both \(q_0\) and \(3q_1\),
and then choose the small parameter in the Joos--Mubayi--Smith theorem below
that slack.

The two reservoir hosts are exactly \(p\)-regular on all four relevant parts,
and are linear. Thus (H1)--(H4) hold with \(d=p\). The mixed
projection-collision pairs satisfy (E2), (E3), (E5), and (E6): a fixed
completion edge has at most \(3p\) conflicting first-reservoir edges, while a
fixed first-reservoir edge and row leave only constantly many choices.

PX148 and PX149 verify all remaining ordinary and mixed conflict conditions.
The more general form of the covering theorem explicitly permits conflicts with
one completion-reservoir edge. It therefore gives a \(P\)-perfect matching
avoiding projection collisions and every bucket conflict. Projection produces a
strong-complete map.

The line cap is

\[
L=O(p^\beta),
\]

so PX148 gives

\[
\mu(f)=O(p^{1+\beta})\le p^{1+\eta}
\]

for sufficiently large \(p\). PX149 gives

\[
\tau(f)
=O(p^{\beta+\gamma})
=O(p^{\eta/2})
\le p^\eta.
\]

Finally apply the exact orbit formulas PX129. \(\square\)

## 4. Boundary

PX150 proves the deterministic seed scale required by the affine-orbit route up
to an arbitrarily small power loss. It does not prove the constant bounds seen
through order 53, and it still protects only the two linear colourings reduced
to \(x-f(x)\) and \(x+f(x)\).

The remaining product bottleneck is therefore no longer existence of an exact
spread seed for two directions. It is one of:

1. extend the construction to a growing low-direction family;
2. show that subpower two-direction spread already regularises all remaining
   primitive directions after the PX81 height decomposition; or
3. combine several two-direction reservoirs without losing saturation.

## 5. Verification

Run

```bash
python scripts/verify_product_bucketed_exact_seed.py
```

The verifier checks the finite pattern counts, line-cap implication, triangle
occurrence-degree bound, and duplicated-reservoir projection on small primes.
The asymptotic existence conclusion uses the cited Joos--Mubayi--Smith covering
theorem.
