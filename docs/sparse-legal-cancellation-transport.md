# Sparse legal cancellation transport

This note records SAS5jb--SAS5jf. It replaces assumed opposite-sign pairing by an exact matching criterion.

## Contract

For each retained boundary coordinate, expand positive and negative output multiplicities into unit occurrences. Join a positive unit to a negative unit exactly when the physical cancellation pair is legal and preserves every retained support, lineage and guard field.

Orient the smaller sign class as the left side of this bipartite graph.

## Theorem block SAS5jb--SAS5jf

Let `P` and `N` be the positive and negative unit counts, `mu` the maximum legal matching size, and `delta` the maximum Hall deficiency on the smaller sign side. Then:

1. `mu = min(P,N) - delta`;
2. full coordinate cancellation is possible exactly when every Hall inequality holds;
3. the residual variation after maximum legal cancellation is
   `P+N-2mu = |P-N| + 2delta`;
4. thus residual output splits exactly into unavoidable net boundary and compatibility-deficiency mass;
5. when `delta>0`, the least deficient sign subset and its legal neighbourhood are a canonical cancellation obstruction.

Coordinates remain independent only when the complete physical contract says cross-coordinate pairing is unnecessary.

## Consequence

The signed boundary theorem can now use actual legal pairings. Either the full algebraic cancellation is realized physically, or one exact sign-pair Hall cut carries all additional residual variation.

## Finite audit

Run:

`python scripts/verify_sas_legal_cancellation_transport.py`

The audit brute-forces maximum matchings and all Hall subsets in random coordinatewise cancellation graphs.

## Scope

This result does not prove that the concrete opposite-sign graph satisfies Hall, nor does it complete balanced compression, SAS6 or the no-three-in-line conjecture.
