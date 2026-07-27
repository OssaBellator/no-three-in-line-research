# Destroyed current triples certify one-for-one geometric witness cancellation

CMR1902--CMR1909 require every primitive geometric witness to receive one explicit
fate. A `deleted` fate is intentionally not justified merely by a nonempty
evidence string.

This chapter supplies one exact rule-specific deletion mechanism. The manifest
contains:

- the complete accepted owner/fate source;
- the exact point set immediately before the response operation;
- the indices of the points removed before the response is inserted; and
- one cancellation record for every deleted primitive witness.

After removal, the surviving points must equal the source manifest's
`background_points` in the same order. Thus the background indices used by
rank-one and rank-two primitive witnesses retain an exact geometric meaning.

A cancellation record reserves one current collinear triple destroyed by the
removal. Destroyed triples cannot be reused.

## 1. Exact destroyed-triple reconstruction

Let `P` be the finite pre-response point set and let `R` be the subset removed
before the response is inserted. Define

\[
\mathcal D(P,R)
=
\left\{
T\in\binom P3:
T\text{ is collinear and }T\cap R\ne\varnothing
\right\}.
\]

### Theorem CMR1918 -- PROVED

After removing `R`, the current collinear triples destroyed by that removal are
exactly

\[
\boxed{\mathcal D(P,R).}
\]

### Proof

A current triple survives precisely when all three of its points remain. Hence a
current collinear triple is destroyed precisely when it contains at least one
removed point. ∎

The checker reconstructs this set from integer coordinates. It does not accept a
declared destroyed-triple list as an oracle.

## 2. Exact surviving-background linkage

### Theorem CMR1919 -- PROVED

An accepted cancellation manifest satisfies

\[
\boxed{P\setminus R=B}
\]

as an ordered list, where `B` is the `background_points` list of the owner/fate
source.

Consequently every background-point or background-pair index in the source refers
to the corresponding surviving pre-response point.

### Proof

The checker removes exactly the declared indices from `pre_response_points` and
requires direct ordered-list equality with the inline source background. ∎

This detects accidental use of a different parent configuration.

## 3. Unique deletion-evidence surface

Every deleted source witness must carry a unique evidence identifier. A
cancellation record has the form

\[
(\text{evidence identifier},\text{ destroyed triple}).
\]

### Theorem CMR1920 -- PROVED

An accepted manifest gives a bijection between:

1. deleted primitive-witness evidence identifiers; and
2. cancellation records.

There are no missing, duplicate or extraneous deletion records.

### Proof

The checker extracts every deleted evidence identifier from all three source ranks,
rejects repeated identifiers, and requires exact set equality with the identifiers
in the cancellation list. ∎

## 4. Injective destroyed-credit reservation

Let `C` be the image of the cancellation records inside
`\mathcal D(P,R)`.

### Theorem CMR1921 -- PROVED

The cancellation map is injective:

\[
\boxed{|C|=\#\{\text{deleted primitive witnesses}\}.}
\]

Every reserved value is an actual destroyed current triple, and no destroyed triple
is assigned to two deleted witnesses.

### Proof

Each record is checked against the reconstructed set `\mathcal D(P,R)`. Repeated
destroyed triples are rejected. CMR1920 gives one record per deleted witness. ∎

The theorem is response-independent. Therefore the restriction of the map to the
deleted witnesses occurring in any particular response remains injective.

## 5. Responsewise cancellation

For a response matching `Q`, let:

- `N_raw(Q)` be the number of occurring primitive geometric witnesses before fate
  processing;
- `N_del(Q)` be the number of occurring witnesses whose fate is `deleted`;
- `B(Q)` be the occurrence score exported by the owner/fate source after deleted
  witnesses are omitted and explicit dominated multiplicities are applied; and
- `T=|\mathcal D(P,R)|`.

### Theorem CMR1922 -- PROVED

For every response,

\[
N_{\mathrm{del}}(Q)\le |C|
\]

and the deleted occurrences may be cancelled against distinct triples destroyed by
the same operation.

### Proof

The global map of CMR1921 is injective. Its restriction to the deleted witnesses
whose prescriptions occur in `Q` is therefore injective into `C`. ∎

### Theorem CMR1923 -- PROVED

Put

\[
U=T-|C|,
\]

the number of destroyed current triples not reserved for deleted-witness
cancellation. Then every response satisfies

\[
\boxed{
N_{\mathrm{raw}}(Q)-T
\le
B(Q)-U.
}
\]

### Proof

Write `N_raw=N_keep+N_del`, where `N_keep` counts nondeleted primitive witnesses
with multiplicity one. The source export satisfies `B(Q)>=N_keep(Q)` because
retained and transferred witnesses export one unit and dominated witnesses export
an explicit multiplicity at least one. Also `N_del(Q)<=|C|` by CMR1922. Hence

\[
N_{\mathrm{raw}}(Q)-T
\le
B(Q)+|C|-T
=
B(Q)-U.
\]

∎

Thus the unused destruction credit is not consumed by deleted-witness accounting
and remains available for a strict potential comparison.

## 6. Exact strictness criteria

Let

\[
Z=|\operatorname{PM}(G)|,
\qquad
A_B=\sum_Q B(Q),
\qquad
M_B=\max_Q B(Q).
\]

### Theorem CMR1924 -- PROVED

The following are valid scalar potential certificates.

1. If
   \[
   \boxed{A_B<ZU,}
   \]
   then the average net triple change is negative, so at least one response strictly
   lowers the triple potential.
2. If
   \[
   \boxed{M_B<U,}
   \]
   then every response strictly lowers the triple potential.

### Proof

Sum CMR1923 over all `Z` responses for the first statement. For the second,
CMR1923 is negative response-by-response. ∎

These criteria concern the scalar real-triple potential. Label-weighted recurrent
rows may still require the downstream Lyapunov certificate.

## 7. Executable endpoint

### Corollary CMR1925 -- PROVED

`scripts/check_geometric_destroyed_triple_cancellation.py` implements the complete
finite certificate.

It:

1. revalidates the owner/fate source;
2. reconstructs the pre-response and surviving point sets;
3. enumerates all destroyed current collinear triples;
4. extracts every deleted witness and requires unique evidence;
5. checks exact deletion-record coverage;
6. checks injective destroyed-triple reservation;
7. computes the unused destruction credit `U`;
8. verifies the responsewise inequality of CMR1923 on every response.

Its deterministic self-test validates 300 systems containing:

- 3,761 primitive witnesses;
- 832 deleted witnesses;
- 1,304 destroyed current triples;
- 472 unused destroyed-triple credits; and
- 2,310 exact responsewise inequalities.

It rejects ten independently corrupted manifests.

The checker proves cancellation relative to the supplied exact pre-response point
set and removed indices. A policy-specific transition verifier must still establish
that those points and removals are the ones actually executed in the parent state.
