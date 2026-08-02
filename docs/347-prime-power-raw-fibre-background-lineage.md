# Raw-fibre lineage reconstructs exact coordinate-labelled backgrounds

A raw-fibre lineage record contains the side, coordinate-labelled host,
deletion trace, target, background points, allowed response family and every
owner/fate/collision/line/interface/CRT provenance label.

## Theorem CMR1950 -- PROVED

The complete tuple is the exact raw-fibre background identifier.

## Theorem CMR1951 -- PROVED

A valid lineage record reconstructs one coordinate-labelled background and
response host without matching-orbit ambiguity.

## Theorem CMR1952 -- PROVED

Canonical serialization of the complete lineage tuple is injective on distinct
declared records.

## Theorem CMR1953 -- PROVED

Every lineage record enumerates exactly its allowed perfect-matching responses.

## Theorem CMR1954 -- PROVED

Complete line-energy kernels and labelled child rows are computed on the
reconstructed background, not on a host-only representative.

## Theorem CMR1955 -- PROVED

Mismatched side, host, target, background, response or provenance data is a
lineage corruption and is rejected.

## Theorem CMR1956 -- PROVED

A declared raw-fibre batch is complete exactly when identifiers are unique and
every expected record and response family is present.

## Corollary CMR1957 -- PROVED

Raw-fibre lineage is the finite bridge from matching denominators to exact
geometric and labelled rows. This chapter does not claim that the current batch
covers every global provenance fibre.

The reconstruction, response enumeration, injectivity and corruption checks are
implemented in
[`scripts/verify_prime_power_raw_fibre_background_lineage.py`](../scripts/verify_prime_power_raw_fibre_background_lineage.py).
