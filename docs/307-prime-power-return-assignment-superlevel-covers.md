# Superlevel vertex covers certify the combined return assignment

CMR1582--CMR1589 reduce the return-selector block to one assignment problem with
nonnegative rational edge score

\[
h_T(a)=g_{\rm ret}(a)+Tg_{\rm sel}(a).
\]

A direct assignment dual is exact, but its edgewise inequalities may still be
large.  This chapter gives a finite threshold certificate.  At every positive
score level, retain only the superlevel graph and its matching number.  The
layer-cake identity bounds every perfect matching by a weighted sum of those
matching numbers.  By Konig's theorem, each matching number has an equally small
vertex-cover witness.

This does not prove the resulting bound is below one in every geometric class.
It converts the remaining return assignment into finitely many matching or
vertex-cover inequalities which can be attacked by owner, height, token, prefix
and carry structure.

Let `G=(L,R,E)` be a finite bipartite response host with at least one perfect
matching and let

\[
h:E\to\mathbb Q_{\ge0}
\]

be any nonnegative rational score.  In the return-selector application use
`h=h_T`.

## 1. Exact finite layer decomposition

Let the distinct positive score values be

\[
0<\tau_1<\tau_2<\cdots<\tau_m,
\qquad \tau_0=0,
\]

and define the nested superlevel graphs

\[
E_j=\{a\in E:h(a)\ge\tau_j\}.
\]

### Theorem CMR1630 -- PROVED

For every perfect matching `Q` of `G`,

\[
\boxed{
\sum_{a\in Q}h(a)
=
\sum_{j=1}^m(\tau_j-\tau_{j-1})|Q\cap E_j|.
}
\]

### Proof

For one edge of score `h(a)=tau_k`, its contribution on the right is

\[
\sum_{j=1}^k(\tau_j-\tau_{j-1})=\tau_k=h(a).
\]

Sum this identity over the edges of `Q`. ∎

## 2. Superlevel matching-number upper bound

Let

\[
\mu_j=\nu(E_j)
\]

be the maximum matching size of the bipartite graph `(L,R,E_j)`.

### Theorem CMR1631 -- PROVED

The assignment optimum satisfies

\[
\boxed{
\max_{Q\in\operatorname{PM}(G)}\sum_{a\in Q}h(a)
\le
\sum_{j=1}^m(\tau_j-\tau_{j-1})\mu_j.
}
\]

### Proof

For every perfect matching `Q`, the set `Q cap E_j` is a matching in `E_j`, so

\[
|Q\cap E_j|\le\mu_j.
\]

Insert these inequalities into CMR1630 and maximize over `Q`. ∎

The inequality may be strict because one perfect matching need not attain all
superlevel matching numbers simultaneously.  It is nevertheless one honest
upper bound for the shared return-selector assignment, not a sum of separate
return and selector maxima.

## 3. Vertex-cover certificate

### Theorem CMR1632 -- PROVED

For each `j`, there is a vertex cover

\[
C_j\subseteq L\cup R
\]

of the superlevel graph `E_j` satisfying

\[
\boxed{|C_j|=\mu_j.}
\]

Consequently any explicit covers `C_j` certify

\[
\boxed{
\max_Q\sum_{a\in Q}h(a)
\le
\sum_{j=1}^m(\tau_j-\tau_{j-1})|C_j|.
}
\]

### Proof

Konig's theorem identifies maximum matching size and minimum vertex-cover size
in every finite bipartite graph.  Apply it separately to each `E_j`, then use
CMR1631. ∎

The cover vertices retain source and target provenance.  They may therefore be
chosen or bounded using owner rows, target columns, primitive-height bands,
absolute tokens, prefix classes, carry classes or fixed-interface labels.

## 4. Direct return-selector spectral certificate

Use the score `h_T` of CMR1584.

### Theorem CMR1633 -- PROVED

If superlevel covers satisfy

\[
\boxed{
\sum_{j=1}^m(\tau_j-\tau_{j-1})|C_j|<1,
}
\]

then

\[
\boxed{\alpha+T\beta<1}
\]

and the coupled return-selector block has spectral radius below one.

### Proof

CMR1584--CMR1586 identify `alpha+T beta` with an assignment expectation bounded
by the assignment optimum.  CMR1632 bounds that optimum by the displayed cover
sum.  Apply the exact two-row criterion CMR1562. ∎

Thus one may certify the block without displaying a separate assignment dual.
The covers themselves are a combinatorial dual certificate.

## 5. Exact integer form

Assume all scores have common denominator `D>0`.  Put

\[
H(a)=Dh(a)\in\mathbb Z_{\ge0}
\]

and let

\[
0<\ell_1<\cdots<\ell_m,
\qquad \ell_0=0,
\]

be the distinct positive integer values of `H`.

### Theorem CMR1634 -- PROVED

The strict block certificate is the integer inequality

\[
\boxed{
\sum_{j=1}^m(\ell_j-\ell_{j-1})|C_j|<D.
}
\]

Every cover may be checked using only edge incidences in the corresponding
integer superlevel graph

\[
\{a:H(a)\ge\ell_j\}.
\]

### Proof

Multiply the CMR1633 inequality by `D`. ∎

This certificate is compatible with the integer Lyapunov and labelled CRT
formats of CMR1270--CMR1277 and CMR1622--CMR1629.

## 6. Two-level coarse envelope

Suppose

\[
0\le h(a)\le L
\]

on every edge.  Fix a threshold `c` with `0<=c<=L`, and let `r` be the matching
number of the strict superlevel graph

\[
E_{>c}=\{a:h(a)>c\}.
\]

### Theorem CMR1635 -- PROVED

Every perfect matching of side `d=|L|=|R|` satisfies

\[
\boxed{
\sum_{a\in Q}h(a)
\le
 dc+r(L-c).
}
\]

Hence

\[
\boxed{dc+r(L-c)<1}
\]

is an immediately checkable return-selector certificate.

### Proof

Give every edge the baseline cost `c`.  A perfect matching has `d` edges.  At
most `r` of them lie in `E_{>c}`, and each such edge has excess at most `L-c`. ∎

This is useful when geometry proves that high-score owner classes have small
matching number even if many low-score edges remain.

## 7. Geometric class specialization

Let every edge have a finite exact class

\[
\sigma(a)\in\mathcal S
\]

and suppose

\[
h(a)\le H_{\sigma(a)}.
\]

### Theorem CMR1636 -- PROVED

Apply CMR1631--CMR1634 to the class score

\[
\widehat h(a)=H_{\sigma(a)}.
\]

For each class threshold, it is enough to bound the matching number or exhibit a
vertex cover in the union of all classes whose score reaches that threshold.
The resulting cover sum is an honest upper bound for the exact return-selector
assignment.

### Proof

Pointwise domination gives `h<=hat h`.  Assignment objectives are monotone in
edge scores.  Apply the preceding theorems to `hat h`. ∎

No independence between classes is assumed.

## 8. Superlevel-certificate endpoint

### Corollary CMR1637 -- PROVED

The combined return-selector frontier now has three nested exact certificate
forms.

1. The full rational assignment dual of CMR1585--CMR1587.
2. A finite superlevel matching-number or Konig-cover certificate.
3. A two-level heavy-edge matching-number envelope.

The second and third forms retain the shared response matching and therefore do
not add incompatible return and selector extrema.  The remaining numerical task
is to prove small superlevel matching numbers or covers from inherited owner,
line-height, token, prefix, carry and interface geometry.  No all-`n` theorem is
claimed.

Layer decompositions, assignment bounds, exact Konig covers, two-level envelopes
and strict integer certificates are checked in
[`scripts/verify_prime_power_return_assignment_superlevel_covers.py`](../scripts/verify_prime_power_return_assignment_superlevel_covers.py).
