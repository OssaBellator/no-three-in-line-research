# Literal post-response triple counts and exact best-response selectors

CMR1950--CMR1957 certify the response-pool upper inequality

\[
N_{\rm raw}(Q)-|\mathcal D(P,R)|
\le
B(Q)-U_{\rm pool}.
\]

This chapter verifies the left-hand side directly from the actual point sets. It
constructs the post-response configuration for every perfect matching, counts every
collinear triple, recovers the rank-one/two/three primitive-witness decomposition,
and selects a deterministic response of minimum exact triple change.

The certificate contains one accepted response-pool bundle. Its exact pre-response
point set is `P`, its removed subset is `R`, its surviving ordered background is
`B=P\setminus R`, and a response matching `Q` is inserted using its literal rook
coordinates.

## 1. Literal post-response configuration

For a response matching `Q`, define

\[
P_Q^+=B\cup Q.
\]

The source checker already requires `B` to be disjoint from the full response grid,
so this is a disjoint union of points.

### Theorem CMR1958 -- PROVED

For every enumerated response, `P_Q^+` is exactly the point configuration obtained
by removing `R` from `P` and inserting the response points of `Q`.

### Proof

The pool manifest requires ordered-list equality between the surviving points of
`P` and the source background `B`. The response is an explicitly enumerated perfect
matching, whose edges are the inserted grid coordinates. Background/grid
disjointness prevents identification of an inserted point with a survivor. ∎

## 2. Triple partition by response rank

Every collinear triple of `P_Q^+` contains zero, one, two or three response points.
Let `n_r(Q)` denote the number containing exactly `r` response points.

### Theorem CMR1959 -- PROVED

The collinear triples of `P_Q^+` form the disjoint partition

\[
\Psi(P_Q^+)
=
\Psi(B)+n_1(Q)+n_2(Q)+n_3(Q).
\]

### Proof

Count a post-response triple by the cardinality of its intersection with the
disjoint response set `Q`. Rank zero is precisely a background triple; the other
three ranks are disjoint and exhaustive. ∎

## 3. Primitive witnesses equal literal new triples

The primitive source reconstructs:

- rank one: one response point and one collinear unordered background pair;
- rank two: one compatible response pair and one collinear background point;
- rank three: one collinear response triple.

Let `W_r(Q)` be the number of rank-`r` primitive witnesses whose prescription is
contained in `Q`.

### Theorem CMR1960 -- PROVED

For every response and every `r` in `{1,2,3}`,

\[
\boxed{W_r(Q)=n_r(Q).}
\]

### Proof

At rank one, choosing the response point and the two background indices is exactly
choosing a post-response triple with one response point. At rank two, the response
pair and background index identify exactly one triple with two response points. At
rank three, the compatible response prescription is the triple itself. The source
uses canonical unordered indices and prescriptions, so the correspondences are
bijective. ∎

The executable checker verifies these three equalities separately, not merely their
sum.

## 4. Literal destroyed-triple identity

Let

\[
T=|\mathcal D(P,R)|.
\]

### Theorem CMR1961 -- PROVED

The direct triple counts satisfy

\[
\boxed{T=\Psi(P)-\Psi(B).}
\]

### Proof

A pre-response triple survives removal exactly when all three of its points lie in
`B`. Therefore the pre-response triples not counted in `\Psi(B)` are exactly the
triples meeting `R`, namely `\mathcal D(P,R)`. ∎

The checker computes both sides independently.

## 5. Exact response delta

Define the literal triple-potential change

\[
\Delta\Psi(Q)=\Psi(P_Q^+)-\Psi(P).
\]

### Theorem CMR1962 -- PROVED

For every response,

\[
\boxed{
\Delta\Psi(Q)
=
W_1(Q)+W_2(Q)+W_3(Q)-T.
}
\]

### Proof

Apply CMR1959 and CMR1960 to the post-response count, then subtract `\Psi(P)` and
use CMR1961. ∎

This equality is stronger than an upper estimate: it is the exact integer change of
the real-triple potential.

## 6. End-to-end pool comparison

Let `K=max_Q d(Q)` be the exact simultaneous deleted load and

\[
U_{\rm pool}=T-K.
\]

### Theorem CMR1963 -- PROVED

For every response, the literal direct delta satisfies

\[
\boxed{
\Delta\Psi(Q)
\le
B(Q)-U_{\rm pool}.
}
\]

### Proof

CMR1962 identifies the direct delta with the raw-witness-minus-destruction
expression used in CMR1953. Apply the response-pool inequality. ∎

The checker nevertheless verifies this inequality again after independently
constructing and counting `P_Q^+`, thereby testing the complete accounting chain.

## 7. Deterministic exact selector

Order responses lexicographically by their edge lists. Let

\[
\delta_* = \min_Q\Delta\Psi(Q)
\]

and choose `Q_*` as the lexicographically first minimizer.

### Theorem CMR1964 -- PROVED

`Q_*`, `delta_*`, and the number of minimizers are deterministic functions of the
finite certificate. If

\[
\boxed{\delta_*<0,}
\]

then `Q_*` is an explicit response that strictly lowers the real-triple potential.

### Proof

The response set is finite and every direct delta is an exactly computed integer.
The minimum exists. Lexicographic tie-breaking selects one unique minimizer. A
negative exact delta is precisely strict potential decrease. ∎

This selector does not use a sufficient upper model once the exact finite response
list is available.

## 8. Executable endpoint

### Corollary CMR1965 -- PROVED

`scripts/check_direct_response_triple_delta.py` implements the complete certificate.
It:

1. validates the full response-pool cancellation bundle;
2. reconstructs the literal pre-response, background and post-response point sets;
3. enumerates all collinear triples directly;
4. verifies the rank-one, rank-two and rank-three witness bijections;
5. verifies the destroyed-triple and exact-delta identities;
6. verifies the pool upper bound on every response;
7. publishes a canonical SHA-256 digest of all response records; and
8. publishes the deterministic exact minimizer.

Its built-in deterministic suite runs 300 systems and rejects ten independently
corrupted certificates. The suite includes the concrete side-five pool/coloring gap
source from CMR1950--CMR1957.

The certificate remains conditional on the transition claim that the supplied
pre-response point set and removal subset are the operation actually executed by
the parent policy. It closes the scalar geometry after those inputs are fixed; it
does not infer them from a historical trace or selector label.
