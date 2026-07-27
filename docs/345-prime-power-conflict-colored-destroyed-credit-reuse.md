# Response-compatible reuse of destroyed-triple cancellation credits

CMR1918--CMR1925 reserve a different destroyed current triple for every deleted
primitive witness.  That global injection is valid but unnecessarily strong.
Two deleted witnesses that never occur in one response do not need simultaneous
payment and may therefore share one destroyed-triple credit.

This chapter gives the exact static reuse surface.  It retains one declared credit
for each deleted witness, but allows several witnesses to name the same destroyed
triple when their response prescriptions are mutually incompatible.

## 1. Deleted-witness conflict graph

Let `W_del` be the deleted primitive witnesses in one accepted owner/fate source.
For `w in W_del`, let `P(w)` be its response prescription.  Define the graph

\[
\Gamma_{\rm del}=(W_{\rm del},E)
\]

by

\[
ww'\in E
\quad\Longleftrightarrow\quad
\exists Q\in\operatorname{PM}(G):
P(w)\cup P(w')\subseteq Q.
\]

### Theorem CMR1934 -- PROVED

The checker reconstructs `Gamma_del` exactly from the response host and the deleted
witness prescriptions.

### Proof

It enumerates every perfect matching of the declared host and tests prescription
containment.  Two witnesses are adjacent precisely when at least one enumerated
response contains both prescriptions. ∎

Repeated primitive witnesses with the same prescription are distinct vertices and
are adjacent, because they occur simultaneously whenever that prescription occurs.

## 2. Independent sets may share one credit

### Theorem CMR1935 -- PROVED

Let `I` be an independent set of `Gamma_del`.  One destroyed current triple may be
assigned to every witness in `I` without paying two deleted occurrences in any one
response.

### Proof

If one response contained two vertices of `I`, those vertices would be adjacent by
the definition of `Gamma_del`, contradicting independence.  Hence each response
contains at most one assigned witness from `I`. ∎

The theorem is about one execution of one selected response.  It does not claim
that the same destroyed triple is used several times in one execution.

## 3. Proper credit colorings

A static credit assignment maps each deleted witness to one actual member of

\[
\mathcal D(P,R),
\]

the reconstructed set of current triples destroyed by the removal.  Witnesses
mapped to one destroyed triple form one color class.

### Theorem CMR1936 -- PROVED

A static assignment is responsewise valid exactly when each color class is an
independent set of `Gamma_del`.

### Proof

If a color class is independent, CMR1935 shows that its destroyed triple pays at
most one occurring deletion in every response.  Conversely, if two adjacent
witnesses share one credit, a response witnessing their adjacency requires that
credit twice, so the assignment is invalid. ∎

Thus a valid static assignment is precisely a proper coloring whose colors are
labelled by distinct destroyed current triples.

## 4. Minimum static reservation

### Theorem CMR1937 -- PROVED

The minimum number of destroyed triples required by any static witness-to-credit
assignment is

\[
\boxed{\chi(\Gamma_{\rm del}).}
\]

A static assignment exists if and only if

\[
|\mathcal D(P,R)|\ge \chi(\Gamma_{\rm del}).
\]

### Proof

CMR1936 identifies valid assignments with proper colorings.  The least number of
colors in a proper coloring is the chromatic number.  Each color must be represented
by a distinct actual destroyed triple. ∎

No polynomial-time optimization claim is made.  A supplied coloring is checked
directly.

## 5. Clique lower-bound optimality

### Theorem CMR1938 -- PROVED

Suppose a manifest uses `k` destroyed credits and supplies a clique of `k` deleted
witnesses in `Gamma_del`.  Then the static assignment is optimal:

\[
\boxed{k=\chi(\Gamma_{\rm del}).}
\]

### Proof

Every proper coloring uses different colors on all vertices of a clique, so
`chi>=k`.  The supplied valid `k`-coloring gives `chi<=k`. ∎

The checker validates the clique pair-by-pair.  It does not trust a declared
chromatic number.

## 6. Residual static destruction credit

Let

\[
T=|\mathcal D(P,R)|,
\qquad
k=\#\{\text{used destroyed credits}\},
\qquad
U_{\rm col}=T-k.
\]

For a response `Q`, let `N_raw(Q)` be the complete raw primitive-witness count and
let `B(Q)` be the accepted nondeleted/dominated export score.

### Theorem CMR1939 -- PROVED

Every response satisfies

\[
\boxed{
N_{\rm raw}(Q)-T
\le
B(Q)-U_{\rm col}.
}
\]

### Proof

Write `N_raw=N_keep+N_del`.  The export satisfies `B>=N_keep`.  A proper `k`-coloring
has at most one occurring deleted witness in each color, so `N_del(Q)<=k`.  Hence

\[
N_{\rm raw}(Q)-T
\le
B(Q)+k-T
=
B(Q)-U_{\rm col}.
\]

∎

Compared with global injection, the static reuse gain is

\[
\#W_{\rm del}-k.
\]

## 7. Static strictness criteria

Put

\[
Z=|\operatorname{PM}(G)|,
\qquad
A_B=\sum_Q B(Q),
\qquad
M_B=\max_Q B(Q).
\]

### Theorem CMR1940 -- PROVED

The following are sufficient scalar certificates:

\[
\boxed{A_B<ZU_{\rm col}}
\]

for at least one improving response, and

\[
\boxed{M_B<U_{\rm col}}
\]

for every response to improve.

### Proof

Sum CMR1939 for the average criterion and apply it responsewise for the uniform
criterion. ∎

## 8. Executable endpoint

### Corollary CMR1941 -- PROVED

`scripts/check_geometric_conflict_colored_cancellation.py` validates the complete
static reuse certificate.  It:

1. revalidates the owner/fate source;
2. reconstructs the exact pre-response and surviving point sets;
3. enumerates all destroyed current triples;
4. reconstructs every deleted witness prescription;
5. builds the exact conflict graph;
6. validates each destroyed-credit color class;
7. optionally validates a matching clique lower bound;
8. computes used, saved and unused credits; and
9. checks the responsewise inequality of CMR1939.

Its deterministic self-test validates 300 systems containing:

- 3,061 primitive witnesses;
- 657 deleted witnesses;
- 363 used destroyed credits;
- 294 credits saved relative to global injection;
- 300 unused destroyed credits;
- 292 conflict edges;
- 213 clique-matched optimality certificates; and
- 1,923 exact responsewise inequalities.

It rejects ten independently corrupted manifests.

Static coloring is not the scalar optimum in general.  The next certificate drops
the requirement that one witness keep one fixed credit across all hypothetical
responses and instead uses the exact simultaneous deletion load.
