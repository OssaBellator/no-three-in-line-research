# Canonical primary keys and exact response records for all 740 raw hosts

The side-four/five geometric layer has repeatedly been enumerated by the same finite
loop: start with the diagonal and target edge forbidden, add one partial-matching
deletion set, and retain the host when at least one perfect response matching
survives.

This chapter promotes that implicit loop into a canonical primary-key catalogue.
Every later operation geometry, owner/fate source, direct response census, pool
certificate, semantic state record and assignment row can now name the same raw host
without relying on enumeration position or a prose description.

For side `s`, put

\[
\Delta_s=\{(i,i):0\le i<s\},
\qquad
\tau=\{(0,1)\},
\]

and let

\[
E_s=[s]^2\setminus(\Delta_s\cup\tau).
\]

A raw deletion set `D` is a partial matching in `E_s`. Its forbidden edge set is

\[
F(s,D)=\Delta_s\cup\tau\cup D.
\]

The response family is

\[
\operatorname{PM}(s,D)
=
\{\pi\in S_s:(i,\pi(i))\notin F(s,D)\text{ for every }i\}.
\]

Only pairs `(s,D)` with nonempty response family are retained.

## 1. Exact raw-host identity

### Theorem CMR1974 -- PROVED

Two canonical raw-host records represent the same host if and only if their sides and
canonical sorted deletion-edge lists are equal:

\[
\boxed{
(s,D)=(s',D')
\iff
s=s'\text{ and }D=D'.
}
\]

### Proof

The fixed diagonal and target edge are functions of the side. Therefore equality of
the side and deletion set gives equality of the complete forbidden edge set and hence
the host. Conversely, the canonical record stores the side and every deletion edge,
so unequal data define unequal raw records. ∎

The displayed `host_id` is a compact SHA-256-derived key for this exact pair. The
mathematical identity is the pair `(s,D)` itself; no theorem depends on cryptographic
collision resistance. The checker verifies that all 740 generated keys are distinct.

## 2. Exact response reconstruction

### Theorem CMR1975 -- PROVED

For every retained raw host, the catalogue response list is exactly
`\operatorname{PM}(s,D)`, ordered lexicographically as permutations.

### Proof

The checker enumerates every permutation of `[s]` and retains it precisely when none
of its rook edges belongs to `F(s,D)`. This is the defining condition above.
Permutation enumeration is deterministic and complete. ∎

Thus a downstream certificate can recover the same response denominator and
prescription universe from the primary key alone.

## 3. Exact rank-three response records

For a response permutation `pi`, let

\[
\psi_3(\pi)
=
\#\left\{
\{i,j,k\}\in\binom{[s]}3:
(i,\pi(i)),(j,\pi(j)),(k,\pi(k))
\text{ are collinear}
\right\}.
\]

### Theorem CMR1976 -- PROVED

Every response record stores the exact integer `psi_3(pi)`. Consequently the derived
fields satisfy

\[
\boxed{
Z=|\operatorname{PM}(s,D)|,
\qquad
A_3=\sum_{\pi\in\operatorname{PM}(s,D)}\psi_3(\pi),
\qquad
S_3=Z-A_3.
}
\]

The stored response-triple histogram is exactly the multiplicity distribution of
`\psi_3`.

### Proof

For each enumerated response, the checker constructs its rook points and tests every
unordered triple by the integer cross-product collinearity identity. It then sums and
tabulates those exact values. ∎

## 4. Record and catalogue fingerprints

### Theorem CMR1977 -- PROVED

Each record digest is computed from every identity and derived field except the digest
itself. The catalogue digest is computed from the ordered complete list of all full
records.

Any change to a side, deletion edge, forbidden edge, response permutation, response
triple count, denominator, numerator, slack or histogram changes the canonical value
validated by the checker.

### Proof

The validator independently rebuilds the entire canonical catalogue and requires
direct JSON-value equality, in addition to checking the displayed digests. Therefore
acceptance does not rely on a hash comparison alone. ∎

The current complete catalogue digest is

\[
\boxed{\texttt{f333bc7dda6fc5aa0de25336f641d4d444b601be0ff27ab59c9853361f6d1d92}.}
\]

## 5. Complete finite census

### Theorem CMR1978 -- PROVED

The catalogue contains exactly

\[
\boxed{86+654=740}
\]

raw hosts and

\[
\boxed{9260}
\]

response occurrences.

Its rank-three sign split is exactly

\[
\boxed{
651\text{ strict},\qquad
44\text{ critical},\qquad
45\text{ excess}.
}
\]

All 740 host IDs and all 740 record digests are distinct.

### Proof

The checker exhausts every partial matching in `E_4` and `E_5`, discards precisely
those with no surviving perfect matching, and verifies the displayed totals and
distinctness counts. ∎

## 6. Reload equality and no silent drift

### Theorem CMR1979 -- PROVED

A stored full catalogue is accepted if and only if it equals the independently
reconstructed canonical catalogue in every field and carries the exact claims and
catalogue digest.

### Proof

The validator rebuilds the expected object from the defining finite enumeration and
requires direct equality of the host list and claims. Missing hosts, extra hosts,
reordered or altered response data and changed derived fields are rejected. ∎

This gives future generated data a reproducible reload boundary.

## 7. Common primary key for all remaining frontiers

### Theorem CMR1980 -- PROVED

Suppose a downstream finite certificate cites a `host_id` and the corresponding
catalogue record digest. If both agree with the accepted canonical catalogue, then
its raw side, deletion matching, forbidden edge set, response list, denominator and
rank-three data are fixed uniquely.

### Proof

CMR1974 fixes the raw identity. CMR1975 and CMR1976 deterministically reconstruct all
listed derived data. Direct digest linkage detects accidental attachment to a
different catalogue record. ∎

This theorem links data; it does not validate the downstream certificate's additional
background, removal, owner, semantic or assignment claims.

## 8. Executable endpoint

### Corollary CMR1981 -- PROVED

`scripts/check_prime_power_canonical_raw_host_catalogue.py` implements the complete
catalogue.

It can:

1. reconstruct and validate the canonical catalogue;
2. write a full deterministic JSON catalogue;
3. reload and compare a stored catalogue exactly;
4. verify all response and rank-three fields;
5. verify the fixed whole-catalogue digest;
6. reject host-ID and record-digest collisions; and
7. reject ten independently corrupted catalogue variants.

The primary keys are raw coordinate-labelled host identifiers. They are not symmetry
quotients and do not identify owner/provenance fibres that have different actual
background or transition geometry.
