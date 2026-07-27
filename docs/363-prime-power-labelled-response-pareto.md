# Exact labelled response vectors and Pareto pruning

The scalar selector minimizes one number.  A labelled recurrent proof instead sees a
nonnegative coefficient vector indexed by child states.  This chapter reconstructs
that vector for every response directly from the accepted geometric assignment bundle
and removes responses that can never help any strictly positive child weighting.

Let `C` be the ordered child-state set exported by one owner/fate source.  For a
response `Q`, let `v_c(Q)` be the sum of all accepted coefficient bins assigned to
child `c` whose response prescription is contained in `Q`.

## Theorem CMR2078 -- PROVED

Every available response has one exact labelled child vector

\[
\boxed{v(Q)=(v_c(Q))_{c\in C}\in\mathbf Z_{\ge0}^{C}.}
\]

The vector is determined by the validated source, its exact coefficient table and the
literal response matching.  No coefficient may be omitted, duplicated or silently
relabelled.

## Theorem CMR2079 -- PROVED

The coordinate sum is exactly the exported scalar response score:

\[
\boxed{S(Q)=\sum_{c\in C}v_c(Q).}
\]

Thus the existing unweighted assignment score is the all-ones specialization of the
labelled vector, not a separate approximation.

## Theorem CMR2080 -- PROVED

Responses with identical child vectors are indistinguishable for every child-weight
functional.  The checker therefore forms an exact duplicate-vector quotient and keeps
the complete ordered response list attached to every vector.

This quotient concerns the accepted coefficient vector only.  Duplicate vectors do
not imply identical geometric children, transition labels or future substructure.

## Theorem CMR2081 -- PROVED

For vectors `x,y`, say that `x` dominates `y` when

\[
x_c\le y_c\quad\text{for every }c,
\qquad
x_c<y_c\quad\text{for at least one }c.
\]

If `v(Q')` dominates `v(Q)`, then `Q` may be discarded for every strictly positive
child-weight vector.  The exact componentwise Pareto frontier therefore contains all
responses that can minimize a strictly positive linear child score.

## Theorem CMR2082 -- PROVED

For positive integer child weights `w_c>0`, define

\[
S_w(Q)=\sum_{c\in C}w_c v_c(Q).
\]

Every minimizer of `S_w` is Pareto-minimal.  Indeed, a dominating vector would have
strictly smaller weighted score because every weight is positive.

The converse is not claimed: a finite Pareto vector need not be exposed by a chosen
weight vector.

## Theorem CMR2083 -- PROVED

For any supplied positive integer weight map, the lexicographically first minimizer of
`S_w` is deterministic.  The certificate publishes its response, vector, weighted
score, minimizer count and Pareto status, together with the independent all-ones scalar
selector.

## Theorem CMR2084 -- PROVED

Scalar and labelled response quality are different interfaces:

1. the full real-triple selector minimizes `N_B(Q)`;
2. the exported all-ones selector minimizes `sum_c v_c(Q)`;
3. a weighted labelled selector minimizes `S_w(Q)`.

Agreement or disagreement among these selectors is exact data.  A scalar policy
penalty is not automatically a componentwise or weighted labelled penalty, and
unlabelled destroyed-triple credit cannot be assigned to children without a separate
routing theorem.

## Corollary CMR2085 -- PROVED

`scripts/check_prime_power_labelled_response_pareto.py` validates arbitrary geometric
assignment bundles and positive child weights, reconstructs every response vector,
checks scalar totals, publishes the duplicate quotient and exact Pareto frontier, and
rejects twelve independent corruptions.

Its deterministic 300-system suite is generated from accepted owner/fate sources.  It
proves checker coverage only; it does not certify any unresolved real recurrent SCC.
