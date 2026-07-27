# Canonically linked geometric-to-assignment coefficient bundles

CMR1902--CMR1909 produce a complete owner/fate manifest and its unique labelled
integer coefficient export.  CMR1862--CMR1869 then consume a labelled coefficient
table inside the denominator-cleared assignment certificate.

This chapter makes that handoff independently checkable.  A bundle contains:

- the complete owner/fate source manifest;
- a canonical SHA-256 source fingerprint;
- the exact uniform response denominator; and
- the downstream edge, pair and triple coefficient table.

Arithmetic validity does not rely on the fingerprint: the checker directly
revalidates the inline source manifest and compares the downstream table with the
recomputed export.  The fingerprint is a publication and provenance aid, not a
cryptographic theorem assumption.

## 1. Canonical source serialization

Serialize a JSON source manifest using:

- lexicographically sorted object keys;
- UTF-8;
- no insignificant whitespace; and
- the standard JSON representations of strings, integers, arrays and objects.

Let

\[
\operatorname{fp}(M)
=
\operatorname{SHA256}(\operatorname{canon}(M)).
\]

### Theorem CMR1910 -- PROVED

The canonical serialization and source fingerprint are deterministic functions of
the manifest value.

### Proof

The serialization rules select one byte string for every admissible finite JSON
value.  SHA-256 is then a deterministic function of that byte string. ∎

No collision-resistance claim is needed for the subsequent coefficient theorem,
because the source itself is included and checked directly.

## 2. Exact denominator inheritance

Let `Z=|PM(G)|` for the source host.

### Theorem CMR1911 -- PROVED

For a uniform-response coefficient bundle, the downstream row denominator must be

\[
\boxed{D=Z.}
\]

### Proof

Every primitive prescription coefficient exported by the source counts occurrences
against the same uniform response set `PM(G)`.  Its expectation is its integer
numerator divided by `Z`.  The checker recomputes `PM(G)` and requires exact
denominator equality. ∎

Any later common-denominator scaling belongs to the assignment certificate, not
to this raw geometric handoff.

## 3. Exact downstream table equality

Let

\[
c^{(r)}_{j}(P)
\]

be the owner/fate export from CMR1908.  Parse the downstream table into canonical
keys `(r,j,P)`.

### Theorem CMR1912 -- PROVED

A bundle is accepted only when its downstream coefficient table satisfies

\[
\boxed{
\widehat c^{(r)}_{j}(P)=c^{(r)}_{j}(P)
}
\]

for every rank, child and compatible prescription.

### Proof

The checker first validates the complete source manifest and recomputes its export.
It then parses every downstream coefficient into the same canonical key space and
requires dictionary equality. ∎

### Corollary CMR1913 -- PROVED

An accepted bundle contains:

- no omitted exported bin;
- no extra downstream bin;
- no duplicated bin;
- no altered coefficient value;
- no unknown child state; and
- no incompatible pair or triple prescription.

Thus the geometric source and assignment input are exactly the same integer table.

## 4. Transparent upper multiplicity

### Theorem CMR1914 -- PROVED

In an accepted bundle, downstream coefficient mass can exceed the number of
nondeleted raw witnesses only through explicit `dominated` multiplicities in the
owner/fate source.

### Proof

Retained and transferred witnesses export multiplicity one, deleted witnesses
export zero, and dominated witnesses export their declared positive integer
multiplicity.  CMR1912 forbids any later alteration. ∎

This makes every componentwise upper replacement visible at the primitive-witness
level.

## 5. Source fingerprint linkage

### Theorem CMR1915 -- PROVED

The checker rejects a bundle when its declared source fingerprint differs from the
canonical fingerprint of the inline source manifest.

Therefore accidental source/table mix-ups and unrecorded source edits are detected
before coefficient comparison.

This is a reproducibility property.  The mathematical exactness of CMR1912 follows
from direct source revalidation and table equality, not from a cryptographic
collision assumption.

## 6. Composition with the assignment certificate

Suppose:

1. the owner/fate source is accepted;
2. every nonretained evidence obligation is proved by its rule-specific verifier;
3. the geometric-to-assignment bundle is accepted;
4. the downstream labelled assignment certificate is accepted by
   `check_label_weighted_assignment_certificate.py`.

### Theorem CMR1916 -- PROVED

Under those hypotheses, the integer coefficients used by the accepted assignment
certificate are exactly the coefficients exported from the complete raw geometric
witness family after the proved fate map.  Consequently the accepted assignment
certificate proves

\[
\boxed{AX<X}
\]

for that corrected or componentwise upper labelled offspring table.

### Proof

CMR1906 reconstructs and partitions every primitive witness.  Rule-specific
verification justifies the nonretained fates.  CMR1912 identifies the exported
table with the assignment input.  CMR1866--CMR1867 then prove every strict
assignment row and hence `AX<X`. ∎

The theorem does not turn an unproved deletion or transfer identifier into a valid
mathematical correction.

## 7. Executable bundle endpoint

### Corollary CMR1917 -- PROVED

`check_geometric_assignment_bundle.py` implements the exact handoff.

It:

1. validates the complete owner/fate source;
2. checks its canonical SHA-256 fingerprint;
3. recomputes the exact uniform response denominator;
4. parses every downstream rank-one, rank-two and rank-three coefficient;
5. rejects unknown states, nonpositive values, duplicates and incompatible
   prescriptions;
6. requires exact equality with the source export.

Its deterministic self-test validates 300 bundles containing:

- 4,072 source witnesses;
- 3,125 exact labelled coefficient bins; and
- 4,138 units of exported coefficient mass.

It rejects ten independently corrupted bundles, including source-fingerprint,
denominator, omission, value, duplication, unknown-child, extra-bin, zero-value
and incompatibility failures.

The remaining frontier no longer includes an unchecked source-to-LP conversion.
It consists of constructing the actual 740-host owner/provenance manifests,
proving every deletion, domination and transfer obligation, and solving the
resulting labelled recurrent rows.
