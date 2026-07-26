# All three collateral ranks admit a local entering-edge envelope

CMR1230--CMR1237 remove the permanent constant from rank-one collateral.  The same
owner decomposition gives a distribution-free envelope for rank two and rank
three.  The price is a local maximum over response matchings containing one edge;
that maximum is itself a matching-assignment or rooted line-profile quantity.

Retain the corrected fixed-target setup with old state

\[
S=O\cup M,
\]

and degree-two response graph

\[
G=K_{n,n}\setminus(O\cup F),
\qquad n\ge4.
\]

For compatible distinct response edges `a,b`, let `L(a,b)` be their unique real
line and define

\[
q_2^S(a,b)
=
\mathbf 1_{\{a,b\}\not\subseteq M}\,o_{L(a,b)}.
\]

For a response matching `R` containing `a`, put

\[
\tau_2^S(a,R)
=
\sum_{b\in R\setminus\{a\}}q_2^S(a,b).
\]

Also define

\[
\tau_3^S(a,R)
=
|\{\{b,c\}\subseteq R\setminus\{a\}:
 a,b,c\text{ are collinear and }\{a,b,c\}\not\subseteq M\}|.
\]

## 1. Every allowed edge extends to a bank matching

### Theorem CMR1238 -- PROVED

Every edge `a in E(G)` belongs to at least one perfect matching of `G`.

### Proof

The graph `G` is `(n-2)`-regular and bipartite.  Every finite regular bipartite
graph decomposes into perfect matchings: Hall gives one perfect matching, removing
it leaves a regular bipartite graph of degree one less, and induction completes the
factorisation.  Hence every edge belongs to one member of the decomposition. ∎

Thus all edge-conditioned maxima below are taken over nonempty families.

## 2. Exact local incidence identities

Let `N_r(R)` be the number of new physical triples of response rank `r`.

### Theorem CMR1239 -- PROVED

For every response matching `R`,

\[
\boxed{
N_2(R)
=
\frac12
\sum_{a\in R}\tau_2^S(a,R),
}
\]

and

\[
\boxed{
N_3(R)
=
\frac13
\sum_{a\in R}\tau_3^S(a,R).
}
\]

### Proof

A rank-two new triple consists of one `O` cell and one response pair `{a,b}` not
wholly contained in `M`.  The line of the pair contains exactly `o_{L(a,b)}`
choices of fixed cell.  The pair is seen once from `a` and once from `b`, giving
the factor one half.

A rank-three new triple is a collinear response triple not wholly contained in
`M`.  It is seen from each of its three edges, giving the factor one third. ∎

Together with CMR1230, these identities count only genuinely new triples.

## 3. Local collateral envelopes

For `a in E(G)`, define

\[
\Delta_2(a)
=
\max_{R\in PM(G):a\in R}\tau_2^S(a,R),
\]

\[
\Delta_3(a)
=
\max_{R\in PM(G):a\in R}\tau_3^S(a,R),
\]

and

\[
\boxed{
\Lambda_S(a)
=
w_S(a)
+
\frac12\Delta_2(a)
+
\frac13\Delta_3(a).
}
\]

### Theorem CMR1240 -- PROVED

For every response matching `R`,

\[
\boxed{
N(R)
\le
\sum_{a\in R}\Lambda_S(a).
}
\]

### Proof

Use the exact rank-one identity CMR1230 and CMR1239.  For every `a in R`, replace
`tau_2^S(a,R)` and `tau_3^S(a,R)` by their maxima over all bank matchings containing
`a`.  Sum the resulting inequalities. ∎

This bound is pointwise and does not use a response distribution or a permanent
estimate.

## 4. Row and column full-collateral bound

Define

\[
\mathcal R_\Lambda(G,S)
=
\min\left\{
\sum_x\max_{y:(x,y)\in G}\Lambda_S(x,y),
\sum_y\max_{x:(x,y)\in G}\Lambda_S(x,y)
\right\}.
\]

### Theorem CMR1241 -- PROVED

Every response matching satisfies

\[
\boxed{
N(R)
\le
\sum_{a\in R}\Lambda_S(a)
\le
\mathcal R_\Lambda(G,S).
}
\]

Consequently every probability distribution on the bank satisfies

\[
\boxed{
\mathbb E N(R)
\le
\mathcal R_\Lambda(G,S).
}
\]

### Proof

A perfect matching uses one edge in each source row and target column.  Bound each
chosen edge weight by the maximum in its row or column and take the smaller total.
The expectation statement follows from the pointwise bound. ∎

Unlike CMR1202, this estimate has no factor `kappa_n` at any rank.

## 5. Pointwise target improvement or complete blockage

### Theorem CMR1242 -- PROVED

If

\[
\boxed{
\mathcal R_\Lambda(G,S)<D_S(e),
}
\]

then every response matching in the complete bank has potential strictly below
`Phi(S)`.

For a restricted current host, exactly one of the following occurs.

1. Some bank matching is feasible, and every such feasible response is a strict
   improvement.
2. No bank matching is feasible, and the complete bank enters the minimal
   deficiency-one unit-wall descent CMR1150--CMR1157.

### Proof

CMR1203 gives `L(R)>=D_S(e)` for every response.  CMR1241 gives
`N(R)<=mathcal R_Lambda`.  Hence

\[
\Phi(Q_R)-\Phi(S)
=N(R)-L(R)<0.
\]

The restricted-host alternatives are feasibility versus complete bank blockage;
apply CMR1160 and CMR1150--CMR1157 in the blocked branch. ∎

This criterion requires no unavailable-edge penalty because it controls every bank
state pointwise.

## 6. Rank-two envelopes are maximum-weight matching problems

Fix `a=(x,y)`.  Delete its source and target vertices from `G`.  For every residual
edge `b`, assign weight `q_2^S(a,b)`.

### Theorem CMR1243 -- PROVED

\[
\boxed{
\Delta_2(a)
=
\max_{R'\in PM(G-a)}
\sum_{b\in R'}q_2^S(a,b),
}
\]

where `G-a` denotes the residual graph after removing the endpoints of `a`.

### Proof

Restriction gives a bijection between bank matchings containing `a` and perfect
matchings of `G-a`.  Under that bijection, `tau_2^S(a,R)` is exactly the displayed
residual assignment weight. ∎

Thus `Delta_2(a)` is polynomial-time computable for a fixed finite owner and can be
localized by line height or prefix class.

## 7. Large local envelopes give loaded lines or rooted stars

### Theorem CMR1244 -- PROVED

Fix an allowed edge `a`.

1. Some line through `a` contains at least
   \[
   \boxed{
   \left\lceil\frac{\Delta_2(a)}{n-1}\right\rceil
   }
   \]
   cells of the fixed opposite matching `O`, unless `Delta_2(a)=0`.
2. Let `R_a` attain `Delta_3(a)`, and fix `s>=2`.  Then either one line through `a`
   contains at least `s+1` other edges of `R_a`, or at least
   \[
   \boxed{
   \left\lceil\frac{\Delta_3(a)}{\binom s2}\right\rceil
   }
   \]
   distinct lines through `a` contain at least two other edges of `R_a` which
   participate in new rank-three triples.

### Proof

For rank two, `tau_2^S(a,R)` is a sum of at most `n-1` nonnegative line loads
`o_{L(a,b)}`.  At its maximum, one summand is at least the average.

For rank three, write the witnessed local count as a sum over lines through `a` of
new compatible pairs among the other response edges.  If no line has more than `s`
other response edges, every line contributes at most `binom(s,2)`.  Count positive
summands. ∎

The second branch is a rooted response-layer secant star; the first is a loaded
response line.

## 8. Full local-envelope endpoint

### Corollary CMR1245 -- PROVED

Every fixed-target bank now has one of the following quantitative responses.

1. `mathcal R_Lambda(G,S)<D_S(e)`, so every feasible bank response improves.
2. Complete bank blockage gives strict unit-wall descent.
3. One edge has large corrected rank-one opposite-layer secant load.
4. One edge has large rank-two assignment load and therefore a loaded opposite
   line.
5. One edge has large rank-three load and therefore a loaded response line or a
   rooted response-layer star.

The global CMR1196 frontier is therefore reduced to aggregating these local
edge-line certificates over target cells and forbidden extensions.  No probability
loss is needed once the local envelopes are controlled.

No all-`n` theorem is claimed.  Exact local incidence identities, envelope bounds,
row/column control, assignment representation and line/star consequences are
checked in
[`scripts/verify_prime_power_full_collateral_envelope.py`](../scripts/verify_prime_power_full_collateral_envelope.py).
