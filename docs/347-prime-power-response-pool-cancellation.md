# Exact response-pool cancellation is the scalar optimum

Static conflict coloring still assigns one fixed destroyed triple to every deleted
witness across all hypothetical responses.  The real-triple potential does not
retain such labels.  Only one response is executed, and every destroyed current
triple is one interchangeable unit of scalar potential decrease.

Therefore the exact scalar question is not how to color all deleted witnesses
simultaneously.  It is how many deleted witnesses can occur together in one
response.

## 1. Exact simultaneous deletion load

For each response `Q`, define

\[
d(Q)
=
\#\{w\in W_{\rm del}:P(w)\subseteq Q\}.
\]

Put

\[
\boxed{K=\max_{Q\in\operatorname{PM}(G)}d(Q).}
\]

### Theorem CMR1950 -- PROVED

The checker computes the complete integer histogram of `d(Q)` and the exact maximum
`K` by enumerating every response matching.

### Proof

The owner/fate source supplies the complete deleted witness set and every response
prescription.  Direct containment testing gives each `d(Q)`. ∎

## 2. Pool sufficiency

Let

\[
T=|\mathcal D(P,R)|
\]

be the number of current triples destroyed by the removal.

### Theorem CMR1951 -- PROVED

If

\[
\boxed{T\ge K,}
\]

then every response's deleted witnesses can be cancelled against distinct destroyed
current triples.

### Proof

For a selected response `Q`, exactly `d(Q)<=K<=T` deleted units require payment.
Choose any `d(Q)` distinct members of the destroyed-triple pool.  The scalar
potential assigns no further label to those units. ∎

No destroyed triple is used twice in the one executed response.

## 3. Pool capacity is exact

### Theorem CMR1952 -- PROVED

`K` is the minimum size of an interchangeable destroyed-triple pool sufficient for
all responses.

### Proof

CMR1951 proves sufficiency.  A response attaining `d(Q)=K` requires `K` distinct
unit payments, so any pool of size less than `K` fails on that response. ∎

This is an exact finite maximum, not an optimization relaxation.

## 4. Maximal unused scalar credit

Define

\[
\boxed{U_{\rm pool}=T-K.}
\]

### Theorem CMR1953 -- PROVED

`U_pool` is the largest response-independent number of destroyed scalar triple
credits that remain after all deleted occurrences are paid in every response.

### Proof

CMR1951 leaves at least `T-K` credits in every response.  A response attaining `K`
uses `K` credits, so no larger uniform remainder is possible. ∎

## 5. Exact responsewise inequality

Let `N_raw(Q)` be the complete raw primitive-witness count and `B(Q)` the accepted
nondeleted/dominated export score.

### Theorem CMR1954 -- PROVED

Every response satisfies

\[
\boxed{
N_{\rm raw}(Q)-T
\le
B(Q)-U_{\rm pool}.
}
\]

### Proof

Write `N_raw=N_keep+d(Q)`.  The export satisfies `B>=N_keep`, and `d(Q)<=K` by
definition.  Therefore

\[
N_{\rm raw}(Q)-T
\le
B(Q)+K-T
=
B(Q)-U_{\rm pool}.
\]

∎

## 6. Dominance over static reservation

Let `chi` be the deleted-witness conflict-graph chromatic number and let
`D=#W_del`.

### Theorem CMR1955 -- PROVED

\[
\boxed{K\le\chi(\Gamma_{\rm del})\le D.}
\]

Consequently

\[
U_{\rm pool}
\ge
U_{\rm col}
\ge
U_{\rm inj}.
\]

### Proof

In any proper coloring, all deleted witnesses occurring in one response are
pairwise adjacent and therefore receive distinct colors.  Thus `d(Q)<=chi` for
every `Q`, so `K<=chi`.  Coloring every vertex separately gives `chi<=D`.  Subtract
these capacities from `T`. ∎

The inequality can be strict on the actual geometric checker surface.  The
regression suite includes a side-five source with nine deleted primitive witnesses,

\[
K=2,
\qquad
\chi=3.
\]

Thus the scalar pool retains one more destroyed credit than every static coloring.

## 7. Strictness and assignment integration

Put

\[
A_B=\sum_QB(Q),
\qquad
M_B=\max_QB(Q),
\qquad
Z=|\operatorname{PM}(G)|.
\]

### Theorem CMR1956 -- PROVED

The exact scalar criteria are

\[
\boxed{A_B<ZU_{\rm pool}}
\]

for at least one improving response, and

\[
\boxed{M_B<U_{\rm pool}}
\]

for every response to improve.

Any proved numerator upper bound `L` may replace `A_B`.  In nested assignment
currency it is enough that

\[
\boxed{6l_1+3l_2+l_3<6ZU_{\rm pool}.}
\]

### Proof

Apply CMR1954 exactly as in CMR1924 and CMR1932. ∎

Relative to static coloring, each additional pool credit contributes `Z` average
slack units and one uniform slack unit.

## 8. Executable endpoint

### Corollary CMR1957 -- PROVED

`scripts/check_response_pool_cancellation_bundle.py` validates:

1. the owner/fate source;
2. exact pre-response and surviving geometry;
3. the complete destroyed-triple pool;
4. the response histogram of deleted occurrences;
5. the exact pool capacity `K`;
6. the static colored certificate on the same source and geometry;
7. the exact downstream coefficient bundle;
8. all pool, coloring and injective slack identities; and
9. the responsewise inequality of CMR1954.

Its deterministic self-test validates 300 systems containing:

- 4,477 primitive witnesses;
- 1,317 deleted witnesses;
- 820 destroyed current triples;
- total exact pool capacity 420;
- total static coloring capacity 520;
- 100 credits saved beyond static coloring;
- 897 credits saved beyond global injection;
- 400 unused pool credits;
- 3,051 exact coefficient bins;
- 3,624 units of coefficient mass;
- 5,849 exported numerator units;
- 127 average-strict systems;
- seven uniform-strict systems; and
- 100 systems whose average strictness is certified by the pool but not by the
  supplied static coloring.

It rejects ten independently corrupted certificates.

The pool theorem concerns the unlabeled scalar real-triple potential.  Labelled
recurrent offspring still require the owner/provenance coefficient bundle and the
final weighted assignment certificate.
