# Noncircular operation-slot registries for genuine fibre population

The current `fibre_id` contains a digest of the populated source manifest. It is a
stable identity for an existing fibre, but it is not by itself an independently
expected key: one cannot list such IDs before constructing the source data that enter
their definition. This chapter introduces a parent-rule operation slot that exists
before witness population.

## Theorem CMR2118 -- PROVED

Expected population and populated fibre identity are different layers.

A **slot** is the exact canonical tuple

\[
\boxed{
(\text{parent state},\text{ operation kind},\text{ operation key},
 \text{ expected raw host},\text{ ordered state labels}).
}
\]

Its full tuple is the mathematical identity. A deterministic `slot_id` and record
digest are fingerprints checked together with the tuple; no hash-only identity claim
is made.

## Theorem CMR2119 -- PROVED

A canonical expected registry is reconstructed solely from the parent-rule source and
its slot tuples. Slots must be sorted by `slot_id`, duplicate IDs and duplicate exact
cores are rejected, and every expected raw host must belong to the 740-host canonical
catalogue.

The registry is therefore logically independent of the later population entries.

## Theorem CMR2120 -- PROVED

A population entry maps one operation slot to one concrete source-dependent fibre and
stores

\[
(\text{slot ID},\text{ host ID},\text{ fibre ID},\text{ source digest}).
\]

The population record digest protects this mapping. The slot remains stable when
witness serialization changes; the fibre identity continues to protect the exact
populated source.

## Theorem CMR2121 -- PROVED

For any expected registry and supplied population list, the checker reconstructs
exactly:

1. expected but missing slots;
2. supplied but unexpected slots;
3. multiply populated slots; and
4. slots whose populated host differs from the expected canonical host.

All lists are sorted and included in the audit digest.

## Theorem CMR2122 -- PROVED

A population is complete exactly when

\[
\boxed{
\text{missing}=\text{unexpected}=\text{duplicate}=\text{host mismatch}=\varnothing.
}
\]

Neither the number of records, coverage of all 740 raw hosts, nor equality between a
batch's own records and its own expected list can replace an independently derived slot
registry.

## Theorem CMR2123 -- PROVED

Operation-slot completeness is noncircular: the parent rule fixes the expected slots,
and populated fibre/source digests are attached only afterward. This supersedes the
weaker practice of treating source-dependent fibre IDs as the sole expected registry
key.

A real theorem must still prove that the parent-rule slot enumeration itself is
exhaustive and duplicate-free.

## Theorem CMR2124 -- PROVED

A deterministic regression registry contains 180 slots over 24 parent states, 20 raw
hosts and three operation kinds. The checker verifies:

- a partial population covering 120 of 180 slots with 60 missing;
- a complete population covering all 180 slots; and
- a corrupted audit with exactly one missing slot, one unexpected slot, two duplicate
  slots and one host mismatch.

The fixed synthetic registry digest is

\[
\texttt{c598f730fc90132714e960ab9d73cf4bd0c8bbf3de20bb430a30b3cb8c1bfb24}.
\]

These are interface regressions. They are not the genuine expected slot registry.

## Corollary CMR2125 -- PROVED

`scripts/check_prime_power_operation_slot_registry.py` validates expected slot
registries and exact population-gap audits and rejects twelve independent corruptions.

The branch still lacks the actual parent-rule slot enumerator and genuine slot
population. This theorem fixes the keying and completeness standard that those data
must satisfy; it does not manufacture the missing operations.
