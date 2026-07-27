# Canonical raw-host linkage for owner and provenance fibres

The canonical 740-host catalogue supplies stable raw primary keys, while the
owner/fate source supplies background geometry, entry order, state records, and
primitive witness fates.  This chapter closes the data-linkage gap between those two
surfaces.

A fibre-linkage certificate contains:

1. one accepted owner/fate source manifest;
2. one canonical raw `host_id` and catalogue record digest;
3. one response policy and selected response;
4. the complete parent state-label tuple; and
5. exact source, label, response-list, fibre, and linkage fingerprints.

## 1. Allowed-edge identification

For a raw catalogue record `H`, let `A(H)` be the complement of its exact forbidden
edge set inside the side-`s` response grid.

### Theorem CMR2014 -- PROVED

Across the complete 740-host catalogue, the map

\[
H\longmapsto A(H)
\]

is injective.

### Proof

The checker constructs `A(H)` for every catalogue record and rejects any duplicate
frozen edge set.  All 740 values are distinct. ∎

Thus an owner/fate source's exact side and allowed-edge set identify one raw host
without trusting its declared host ID.

## 2. Host-ID and record-digest linkage

### Theorem CMR2015 -- PROVED

A fibre-linkage certificate is accepted only when:

1. the source allowed-edge set reconstructs a catalogue host `H`;
2. the declared `host_id` equals the canonical ID of `H`; and
3. the declared catalogue record digest equals the full digest of `H`.

### Proof

The checker reconstructs `H` from the allowed-edge map of CMR2014, then compares the
ID and digest by exact string equality. ∎

This prevents a source from borrowing the slack, selector, or priority data of a
different raw host.

## 3. Complete response-list equality

### Theorem CMR2016 -- PROVED

The source response family must equal the catalogue response family exactly, in
canonical order.  Consequently the source denominator equals the catalogue value
`Z(H)`.

### Proof

The owner/fate checker re-enumerates every perfect matching of the source allowed
edges.  The linkage checker converts each response edge set to its permutation and
compares the full ordered list with the catalogue record.  Equality of list lengths
gives the denominator equality. ∎

## 4. Policy-separated response selection

The linkage surface supports two explicit policies:

- `canonical-rank3-selector`;
- `declared-response`.

### Theorem CMR2017 -- PROVED

Under `canonical-rank3-selector`, the selected response must equal the canonical
lexicographically first rank-three minimizer of CMR1991.  Under `declared-response`,
the selected response may be any member of the exact response family.

### Proof

The first policy compares directly with the canonical selector manifest.  The second
checks exact membership in the catalogue response list. ∎

The policy field prevents a freely chosen response from being presented as the
canonical minimizer.

## 5. Mandatory state-label tuple

Every linked fibre stores nonempty strings for the ordered keys

\[
(\text{provenance},\text{collision},\text{local-line},\text{interface},
\text{root},\text{thin},\text{CRT}).
\]

### Theorem CMR2018 -- PROVED

The linkage checker rejects missing, additional, reordered, or empty parent state
labels and fingerprints the exact label tuple.

### Proof

The checker requires exact ordered-key equality, validates every value as a nonempty
string, and recomputes the canonical label digest. ∎

### Honesty boundary

CMR2018 proves that labels are present and stably linked.  It does not prove that any
label has the declared geometric or transition semantics.  Those remain obligations
of the collision, local-line, interface, root, thin, CRT, and provenance verifiers.

## 6. Source and fibre identity

### Theorem CMR2019 -- PROVED

The canonical source digest fingerprints the complete owner/fate manifest.  The
fibre ID is the raw host ID together with a digest of the exact source and state-label
tuple.  Therefore changing the background, entry order, state graph, fates, or parent
labels changes the fibre identity.

### Proof

Both identifiers are deterministic canonical SHA-256 values over the displayed data.
The checker recomputes them from the inline source and labels. ∎

No security theorem is needed: the complete inline objects are also directly
revalidated.

## 7. Exact linkage claims

### Theorem CMR2020 -- PROVED

For every accepted linked fibre, the checker recomputes and stores:

1. side and exact denominator;
2. uniform rank-three slack;
3. canonical rank-three minimum;
4. selected response rank-three count;
5. whether the selection is the canonical minimizer;
6. source response and primitive-witness counts;
7. the state-label digest; and
8. the complete response-list digest.

Every declared claim must equal the recomputed value.

### Proof

Each field is reconstructed from the accepted catalogue record, selector manifest,
owner/fate validation summary, selected response, or exact labels. ∎

## 8. Executable endpoint

### Corollary CMR2021 -- PROVED

`scripts/check_prime_power_raw_host_fibre_linkage.py` implements the complete linkage
surface.  Its deterministic suite validates 300 mixed-policy linked fibres containing
3,815 response records and 4,096 primitive witnesses, split evenly between canonical
selector and declared-response policies.  Twelve independently corrupted
certificates are rejected.

Passing this checker proves exact raw-host, response-family, policy, source, and label
linkage.  It does not prove the actual parent operation, the meaning of the labels,
nonretained fate evidence, or strict contraction of a labelled recurrent block.
