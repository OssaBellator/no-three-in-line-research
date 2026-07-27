# Geometric candidate routing manifests preserve every primitive witness

The integer assignment-certificate checker validates arithmetic relative to a
declared labelled coefficient table.  A separate source compiler is needed to
show that the geometric edge, pair and triple coefficients were populated without
omitting or duplicating candidates.

This chapter gives such a compiler for the raw geometric line-energy coefficients.
It lists the primitive background witnesses rather than storing only aggregate
multiplicities.  Every witness receives exactly one declared child label before
aggregation into the final Lyapunov manifest.

The checker validates geometric incidence, extendability and exact witness
conservation.  It does not determine whether an arbitrary child-label string is
the semantically correct owner, collision, interface or CRT state; the rule that
assigns those labels remains a separate labelled-transition verifier.

Let `G` be a finite bipartite response host of side `d`, and let

\[
B=(b_0,\ldots,b_{N-1})
\]

be a list of distinct background points disjoint from the response grid.

## 1. Primitive geometric witnesses

For an extendable response edge `x`, define its rank-one witness set

\[
\mathcal W_1(x)
=
\left\{\{i,j\}:0\le i<j<N,\ b_i,b_j,x\text{ are collinear}\right\}.
\]

For an extendable compatible response pair `P={x,y}`, define

\[
\mathcal W_2(P)
=
\left\{i:b_i,x,y\text{ are collinear}\right\}.
\]

For an extendable compatible response triple `P`, define

\[
\mathcal W_3(P)
=
\begin{cases}
\{\star\},&P\text{ is collinear},\\
\varnothing,&P\text{ is not collinear}.
\end{cases}
\]

### Theorem CMR1894 -- PROVED

The raw geometric prescription coefficients are exactly

\[
\boxed{a_1(x)=|\mathcal W_1(x)|,}
\]

\[
\boxed{a_2(P)=|\mathcal W_2(P)|,}
\]

and

\[
\boxed{a_3(P)=|\mathcal W_3(P)|.}
\]

### Proof

Every unordered background pair through `x` determines one line through `x` and
contributes one to `C(|B cap ell|,2)`.  Conversely every pair counted by that
binomial coefficient is one witness in `W_1(x)`.  The rank-two formula counts the
background points on the unique line through the response pair.  Rank three has
one primitive response triple precisely when its three response points are
collinear. ∎

Thus the witness representation is equivalent to the exact multiplicity formulas,
but retains the individual geometric objects that may receive different labels.

## 2. Extendability-complete routing surface

An edge, pair or triple is **extendable** when it is contained in at least one
perfect response matching of `G`.

### Theorem CMR1895 -- PROVED

A complete raw routing manifest consists of:

1. one record `(x,{i,j},child)` for every rank-one witness in every extendable
   edge;
2. one record `(P,i,child)` for every rank-two witness in every extendable pair;
3. one record `(P,star,child)` for every collinear extendable response triple;
4. no record for a nonextendable prescription or a nonexistent witness.

Exact equality between the computed witness sets and the manifest record keys is
necessary and sufficient for witness conservation.

### Proof

The displayed records are merely the disjoint union of all three computed witness
sets indexed by their extendable prescriptions.  Set equality gives neither
omission nor duplication. ∎

The checker recomputes every perfect matching, extendable prescription and
collinearity relation from the manifest itself.

## 3. Rank-one routing conservation

### Theorem CMR1896 -- PROVED

Suppose every rank-one witness record carries one child label `j`.  Define

\[
c^{(1)}_j(x)
=
\#\left\{w\in\mathcal W_1(x):w\text{ is labelled }j\right\}.
\]

Then

\[
\boxed{\sum_jc^{(1)}_j(x)=a_1(x)}
\]

for every extendable edge.

### Proof

The exact manifest partitions `W_1(x)` by its declared child label. ∎

The individual background pair remains available to a rule-specific owner or
provenance checker.

## 4. Rank-two and rank-three routing conservation

### Theorem CMR1897 -- PROVED

With

\[
c^{(2)}_j(P)
=
\#\left\{w\in\mathcal W_2(P):w\text{ is labelled }j\right\},
\]

one has

\[
\boxed{\sum_jc^{(2)}_j(P)=a_2(P)}
\]

for every extendable pair.

### Theorem CMR1898 -- PROVED

For an extendable response triple `P`, the exact route family satisfies

\[
\boxed{\sum_jc^{(3)}_j(P)=a_3(P)\in\{0,1\}.}
\]

### Proof

Both statements are the partition identity for their corresponding witness sets.
∎

## 5. Export to the integer assignment manifest

### Theorem CMR1899 -- PROVED

Aggregating the witness records by `(rank,child,prescription)` produces the exact
nonnegative integer geometric coefficient table required by CMR1862--CMR1869.
For positive integer child weights `X_j`, the weighted primitive scores obtained
from the exported table are

\[
q_{\rm geo}(x)=\sum_jX_jc^{(1)}_j(x),
\]

\[
b_{\rm geo}(P)=\sum_jX_jc^{(2)}_j(P),
\qquad
t_{\rm geo}(P)=\sum_jX_jc^{(3)}_j(P).
\]

### Proof

The export counts the exact records in each labelled bin.  Multiplication by fixed
child weights and summation is the label linearization of CMR1838. ∎

No floating-point or probabilistic reconstruction is required.

## 6. Corrected and upper rows

### Theorem CMR1900 -- PROVED

The raw witness manifest may be transformed into a corrected or componentwise
upper offspring table only by an explicit second-stage rule that records, for every
raw witness, exactly one of:

1. retained and routed to a labelled child;
2. deleted by a verified correction rule;
3. transferred to a separately certified off-diagonal or auxiliary state; or
4. dominated by a declared upper coefficient.

Dropping a raw witness without one of these records is not certified by the raw
manifest or by the arithmetic assignment checker.

### Proof

CMR1895 certifies the complete raw candidate set.  Any smaller or differently
routed table requires a map from every element of that set to its stated fate.
The four listed outcomes are the available exact or dominating interpretations.
∎

This theorem preserves the honesty boundary between raw geometric multiplicity,
corrected genuinely-new offspring and labelled recurrence.

## 7. Executable routing checker

### Corollary CMR1901 -- PROVED

The geometric coefficient-source layer now has an executable publication format.

1. Store the exact response host and distinct background points.
2. Store the declared child-label vocabulary.
3. Store one record for every rank-one background-pair witness.
4. Store one record for every rank-two background-point witness.
5. Store one record for every collinear extendable response triple.
6. Recompute perfect matchings, extendability and all witness sets.
7. Reject unknown labels, duplicate records, incompatible prescriptions,
   nonexistent witnesses, omissions and extraneous routes.
8. Aggregate accepted records directly into the integer assignment manifest.

The standalone checker
[`scripts/check_geometric_candidate_routing_manifest.py`](../scripts/check_geometric_candidate_routing_manifest.py)
validates external JSON manifests.  Its built-in deterministic test validates 500
random finite hosts containing 6,063 primitive geometric witnesses and rejects
corrupted witness and label records.

Passing this checker proves raw geometric candidate conservation.  It does not by
itself prove the semantics of the declared child labels or any correction rule.
Those labels must still be generated or checked by the corresponding owner,
collision, local-line, interface and CRT transition compilers.
