# Canonical batch manifests for genuine operation fibres

The remaining proof frontier requires actual owner/provenance fibres rather than more
unkeyed synthetic examples.  This chapter defines the reloadable batch object into
which those genuine operations must be placed.  Each entry composes three independent
certificates over one source:

1. linked literal operation geometry and the full scalar selector;
2. the residual survivor-background signature; and
3. the labelled response-vector/Pareto certificate.

The built-in suite uses synthetic accepted operations solely to test the interface.  It
does not claim that the real fibre population has been supplied.

## Theorem CMR2086 -- PROVED

A batch entry is accepted only when all three component certificates use the same:

- canonical host record;
- owner/fate source fingerprint;
- complete response family;
- survivor background; and
- geometric assignment bundle.

The residual selector must equal the linked literal full selector and must have the
same minimum new-triple score.  The labelled bundle must carry the identical source
fingerprint.

## Theorem CMR2087 -- PROVED

Every accepted entry produces one canonical operation record containing:

- fibre and host IDs;
- source and component-certificate digests;
- side, policy and selector-signature dimension;
- response, witness, background and destroyed-triple counts;
- full and policy-selected responses and exact policy penalty;
- residual and tracked pair masses; and
- labelled vector, Pareto and weighted-selector counts.

The record digest covers every field.

## Theorem CMR2088 -- PROVED

A batch is ordered canonically by `fibre_id` and contains no duplicate fibre ID.  This
prevents one operation from being counted twice under different insertion order or
file layout.

Distinct fibre IDs remain distinct even when they share a host, background signature,
scalar selector or labelled coefficient vector.

## Theorem CMR2089 -- PROVED

The checker reconstructs exact aggregate censuses from the canonical records,
including:

- sides, policies and host multiplicities;
- responses, witnesses, backgrounds and destroyed triples;
- strict scalar selectors and policy/full-selector matches;
- total policy penalty;
- residual and tracked pair masses; and
- unique, Pareto and dominated labelled-response totals.

No aggregate value is trusted from the supplied manifest.

## Theorem CMR2090 -- PROVED

Batch completeness is always relative to an explicit sorted list of expected fibre
IDs.  If such a list is supplied, the batch is marked complete exactly when its
canonical fibre-ID list equals that expected list.

## Theorem CMR2091 -- PROVED

If no expected fibre-ID list is supplied, the batch is marked incomplete regardless
of how many operations it contains.  A finite sample, a large sample or one record per
raw host is not silently promoted to the genuine owner/provenance population.

## Theorem CMR2092 -- PROVED

The canonical record list, reconstructed aggregate claims, component certificates and
coverage declaration are protected by one batch SHA-256 digest.  Reloading and
revalidation reproduce the same records and census exactly.

## Corollary CMR2093 -- PROVED

`scripts/check_prime_power_real_fibre_batch_manifest.py` validates arbitrary batches.
Its deterministic interface suite constructs 120 distinct accepted operation fibres,
checks both undeclared and explicitly declared coverage modes, and rejects twelve
independent corruptions of ordering, identity, component linkage, coverage and
aggregate claims.

This is the publication format for the next data-population phase.  It does not supply
the missing real operations, prove parent-rule legality, prove fate semantics, or
contract any labelled recurrent SCC.
