# Persistent unavailable crosses yield disjoint pair banks or one-arm concentration

CMR522--CMR526 reduce every continuously unavailable blocker which cannot be
absorbed to a row-column cross centred at one persistent cell.  In the
absorption-deficiency branch, every episode supplies one unavailable edge in
the central row and one unavailable edge in the central column.  Those two
edges are compatible.

This chapter records the exact geometry of those partner pairs.  Pair types
are indexed by a bipartite support graph between row-arm and column-arm
partners.  Distinct pair types determine distinct nonaxis lines and pairwise
disjoint equal-size line-clean cylinders.  König's theorem then yields either
a large two-arm pair bank or many distinct pair types sharing one fixed arm
edge.  The latter is an exact line-star bank.

The fixed paid pair may itself be unavailable.  This only adds a deterministic
restoration surcharge of at most two to the weighted line-clean selector.
Thus the persistent-cross branch reaches the same cheap-clean, collateral,
unavailable-inventory, token, and factorization alternatives as CMR502--CMR516.

Fix a parent block of side `m` and a persistent unavailable cell

\[
e=(u,v).
\]

A row-arm partner has the form

\[
r_y=(u,y),
\qquad y\ne v,
\]

and a column-arm partner has the form

\[
c_x=(x,v),
\qquad x\ne u.
\]

For every occurring partner type `(x,y)`, put

\[
Z_{x,y}=\{r_y,c_x\}.
\]

## 1. Cross-pair geometry

### Theorem CMR527 — PROVED

For every partner type `(x,y)`:

1. `Z_{x,y}` is a compatible two-edge partial matching;
2. its joining line `L_{x,y}` is nonaxis;
3. the map
   \[
   \boxed{(x,y)\longmapsto L_{x,y}}
   \]
   is injective.

### Proof

The two edges use source vertices `u,x` and target vertices `y,v`.  The
inequalities `x\ne u` and `y\ne v` give compatibility.  Hence their joining
line is neither vertical nor horizontal.

A nonaxis line meets the source row `u` in at most one grid cell and the target
column `v` in at most one grid cell.  Therefore `L_{x,y}` determines both
`r_y` and `c_x`, and consequently determines `(x,y)`. ∎

Thus distinct absorption-deficiency partner types already carry distinct line
signatures.

## 2. Pairwise disjoint equal-size cylinders

Delete the two source and two target vertices used by `Z_{x,y}` and put

\[
n=m-2.
\]

Apply the universal compatible-pair construction CMR492 on `L_{x,y}`.  Let

\[
\mathcal D_{x,y}
\]

be the resulting full-parent line-clean cylinder.

### Theorem CMR528 — PROVED

For every partner type,

\[
\boxed{|\mathcal D_{x,y}|=D_n.}
\]

Every state in the cylinder contains `Z_{x,y}`, avoids every other cell of
`L_{x,y}`, and has no rank-two candidate-only collateral on that line.

Moreover, for distinct partner types,

\[
\boxed{
\mathcal D_{x,y}\cap\mathcal D_{x',y'}=\varnothing.
}
\]

### Proof

The size and line-clean properties are CMR492--CMR493.

A perfect matching contains exactly one edge from source vertex `u` and
exactly one edge incident with target vertex `v`.  If it contains
`Z_{x,y}`, those two choices are respectively `r_y` and `c_x`.  Hence the
matching determines `(x,y)` uniquely and cannot belong to a cylinder for a
different pair type. ∎

Therefore every set of distinct partner types is automatically an exact
equal-size disjoint line-clean bank.  No additional disjointness selection is
needed.

## 3. Temporal multiplicity versus pair-type support

Suppose `R` absorption-deficiency episodes supply partner types.  Let

\[
\mu(x,y)
\]

be the number of occurrences of type `(x,y)`, and let

\[
M=
|\{(x,y):\mu(x,y)>0\}|
\]

be the number of distinct types.

### Theorem CMR529 — PROVED

For every integer `\lambda\ge2`, at least one of the following holds.

1. **Exact pair recurrence.** Some pair type occurs in at least `\lambda`
   episodes.
2. **Large pair-type support.**
   \[
   \boxed{
   M\ge
   \left\lceil\frac{R}{\lambda-1}\right\rceil.
   }
   \]

### Proof

If the first alternative fails, every nonzero multiplicity is at most
`\lambda-1`.  Therefore

\[
R=\sum_{x,y}\mu(x,y)\le(\lambda-1)M.
\]

Rearrange. ∎

The second branch supplies that many pairwise disjoint cylinders by CMR528.

## 4. Partner graph: two-arm bank or one-arm star

Define the **partner support graph**

\[
H_e=(Y,X;\mathcal E)
\]

whose left vertices are occurring row-arm partners `r_y`, whose right vertices
are occurring column-arm partners `c_x`, and whose support edge `yx` is present
exactly when the pair type `(x,y)` occurs.  Thus

\[
|\mathcal E|=M.
\]

### Theorem CMR530 — PROVED

Fix an integer `s\ge2`.  At least one of the following holds.

1. **Two-arm matching bank.**  The graph `H_e` has a matching of size at least
   `s`.  Hence there are `s` partner types using `2s` distinct noncentral cross
   edges.  Their line-clean cylinders are equal-size and pairwise disjoint.
2. **One-arm partner star.**  Some fixed row-arm or column-arm edge belongs to
   at least
   \[
   \boxed{
   \left\lceil\frac{M}{s-1}\right\rceil
   }
   \]
   distinct partner types.  Those types determine that many distinct nonaxis
   lines through the fixed partner cell and that many equal-size pairwise
   disjoint line-clean cylinders.

### Proof

If the maximum matching number of `H_e` is at least `s`, take such a matching.
Its support edges have distinct left and right endpoints, giving `2s` distinct
partner edges.  Apply CMR527--CMR528.

Otherwise, König's theorem gives a vertex cover of `H_e` of size at most
`s-1`.  The incidences from the cover vertices to support edges total at least
`M`, because every support edge meets the cover.  One cover vertex therefore
has degree at least `\lceil M/(s-1)\rceil`.  Its incident support edges share
one fixed partner cell.  CMR527 makes their joining lines distinct, and CMR528
gives the disjoint equal-size cylinders. ∎

The concentration branch is thus not an arbitrary repeated partner edge.  It
is an exact line-star bank centred at one cell of the persistent cross.

## 5. Weighted selection with an unavailable paid-pair surcharge

Fix one compatible paid pair `Z` and its line-clean cylinder.  Let

\[
c_Z=|Z\setminus E(G)|
\in\{0,1,2\}
\]

be the number of paid-pair edges currently unavailable.  After deleting the
paid-pair endpoints, let `B_L` be the unavailable allowed residual edges and,
for a residual derangement `\delta`, let

\[
r_L(\delta)=|\delta\cap B_L|.
\]

The total restoration count is

\[
T_Z(\delta)=c_Z+r_L(\delta).
\]

Let `X_L(\delta)` and `A_L` be the candidate-only collateral count and the
CMR502--CMR503 expectation bound.

### Theorem CMR531 — PROVED

For every integer `q\ge1`, some line-clean completion satisfies

\[
\boxed{
X_L(\delta)+\frac{T_Z(\delta)}q
\le
A_L+
\frac{c_Z}{q}
+
\frac{|B_L|}{q(n-1)}.
}
\]

In particular, if

\[
\boxed{
A_L+
\frac{c_Z}{q}
+
\frac{|B_L|}{q(n-1)}
<1,
}
\]

then one completion has

\[
\boxed{
X_L(\delta)=0,
\qquad
T_Z(\delta)<q.
}
\]

For an absorption-deficiency pair, both paid edges are unavailable at the
episode in which the pair is exposed, so `c_Z=2`.  The selector therefore
requires only the deterministic surcharge `2/q`.

Every restored edge in the paid pair or residual completion has the usual
exact labelled full-token incidence `(p+1)(h-1)`.

### Proof

The paid-pair cost `c_Z` is constant throughout the cylinder.  CMR502 gives

\[
\mathbb E r_L(\delta)=\frac{|B_L|}{n-1},
\]

and CMR333 gives `\mathbb E X_L(\delta)\le A_L`.  Average the displayed
weighted quantity.  If its upper bound is below one, the nonnegative integer
`X_L(\delta)` must vanish and then `T_Z(\delta)/q<1`.

The token statement is CMR413 applied to the distinct restored edges. ∎

Thus unavailability of the two fixed cross partners does not invalidate the
line-clean bank; it is an explicit additive cost.

## 6. Trace contacts immediately yield one-arm token structure

Suppose `R` distinct rooted-arm cylinders expose paid-line trace contacts with
the persistent cell `e`.  CMR526 supplies `R` distinct witness cells in the
union of row `u` and column `v`.

### Theorem CMR532 — PROVED

At least one arm of the persistent cross contains

\[
\boxed{
d\ge\left\lceil\frac R2\right\rceil
}
\]

distinct trace witnesses.

Consequently, at every chosen nonroot depth, that arm yields either

\[
\boxed{
\text{one full token containing at least }
\left\lceil\sqrt d\right\rceil
\text{ unavailable witnesses},
}
\]

or at least

\[
\boxed{
\left\lfloor\sqrt d\right\rfloor
}
\]

pairwise disjoint unavailable full-token witnesses.

### Proof

The row and column arms meet only in the central cell `e`, and CMR526 excludes
`e` from the selected trace witnesses.  Hence the `R` distinct witnesses split
disjointly between the two arms, so one arm contains at least
`\lceil R/2\rceil`.  Apply CMR515 to that row or column star. ∎

The trace-contact half of CMR525 is therefore already paid by the heavy-token
or dispersed-token ledger.

## 7. Repeated exact pair types: reintroduction or a persistent paid pair

Fix one pair type

\[
Z=\{r_y,c_x\}
\]

which occurs at episode times when both edges are unavailable.  Let `I(r_y)`
and `I(c_x)` count absent-to-present reintroductions of the two edges during
the envelope epoch.

Call a **joint absence run** a maximal interval on which both paid edges stay
continuously unavailable and which contains at least one selected occurrence.

### Theorem CMR533 — PROVED

The number `\rho(Z)` of joint absence runs satisfies

\[
\boxed{
\rho(Z)
\le
1+I(r_y)+I(c_x).
}
\]

Hence, if the pair type occurs `\lambda` times, one joint absence run contains
at least

\[
\boxed{
\left\lceil
\frac{\lambda}
{1+I(r_y)+I(c_x)}
\right\rceil
}
\]

occurrences.

Equivalently, for every integer `\sigma\ge2`, either one joint absence run
contains at least `\sigma` occurrences, or

\[
\boxed{
I(r_y)+I(c_x)
\ge
\left\lceil\frac{\lambda}{\sigma-1}\right\rceil-1.
}
\]

### Proof

Between two consecutive joint absence runs, at least one of the two edges
becomes available.  That transition contributes one absent-to-present
reintroduction to one of the two edge counts.  Thus every gap between joint
runs is charged injectively in chronological order to a reintroduction, giving
the run bound.

Pigeonhole gives the largest-run estimate.  If every joint run has at most
`\sigma-1` selected occurrences, then
`\lambda\le\rho(Z)(\sigma-1)`; combine this with the run bound and rearrange.
∎

Inside a long joint run, the fixed compatible pair is continuously unavailable
but CMR531 applies at every chosen epoch with the same paid-pair surcharge
`c_Z=2`.

## 8. Combined persistent-cross endpoint

### Corollary CMR534 — PROVED

Suppose one central cell remains continuously unavailable through `r`
persistent-aware line-clean episodes and is never absorbed.  Fix integers

\[
\lambda,s,\sigma,q\ge2.
\]

After discarding at most half the occurrences, at least one of the following
exact endpoints is reached.

1. **Trace-token endpoint.**  One row or column arm has the CMR532 heavy-token
   or dispersed-token alternative.
2. **Exact pair recurrence with temporal payment.**  One pair type occurs at
   least `\lambda` times.  Then CMR533 gives either reintroduction payment or a
   jointly persistent compatible paid pair, to which the weighted selector
   CMR531 applies with surcharge two.
3. **Large two-arm pair bank.**  At least `s` pair types have pairwise distinct
   row and column partners.  They give `s` disjoint equal-size line-clean
   cylinders and `2s` distinct cross edges.
4. **One-arm line-star bank.**  A fixed partner cell is incident with at least
   \[
   \boxed{
   \left\lceil
   \frac{
     \left\lceil
       \lceil r/2\rceil/(\lambda-1)
     \right\rceil
   }{s-1}
   \right\rceil
   }
   \]
   distinct pair types, hence with that many distinct paid lines and disjoint
   equal-size cylinders.

Every cylinder in alternatives 2--4 obeys the CMR531 cheap-clean selection
inequality.  Failure of the selector returns frozen collateral,
unavailable-edge depletion, heavy/dispersed token structure, or forced
factorization through CMR504--CMR516.

### Proof

CMR525 places at least `\lceil r/2\rceil` occurrences in either the trace class
or the absorption-pair class.  In the trace class apply CMR532.

In the pair class, CMR529 gives exact recurrence or at least

\[
M\ge
\left\lceil
\frac{\lceil r/2\rceil}{\lambda-1}
\right\rceil
\]

distinct pair types.  In the recurrence branch apply CMR533 and CMR531.  In
the support branch apply CMR530 with threshold `s`.  Finally apply
CMR531 and the earlier weighted-selection endpoints to the resulting
cylinders. ∎

## 9. Revised frontier

The persistent row-column cross is no longer an unstructured temporal
obstruction.

- Trace contacts immediately give one heavy arm and hence token structure.
- Deficiency pairs form an injective family of paid lines.
- Distinct pair types give pairwise disjoint equal-size line-clean cylinders.
- König yields a large two-arm bank or an exact one-arm line-star bank.
- Repeated exact pairs pay reintroduction or become jointly persistent.
- Unavailable paid edges cost only a deterministic surcharge of at most two.

The remaining prime-power task is now **ancestry payment for persistent
pair/star banks**.  One must show that repeated failure of the CMR531 selector
across the nested envelope chain pays protected-reserve depletion, repeated
full-token return, a fixed quotient/carry signature, deletion ancestry, or a
strict envelope expansion.  CMR174 limits strict envelope expansions to the
parent depth.

No all-`n` theorem is claimed.  Pair-line injectivity, cylinder disjointness,
partner-graph alternatives, restoration marginals, joint absence runs, and
trace-arm arithmetic are checked in
[`scripts/verify_prime_power_persistent_cross_pair_bank.py`](../scripts/verify_prime_power_persistent_cross_pair_bank.py).
