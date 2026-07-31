# Provenance-typed boundary catalogue extraction

`docs/549` gives a correct finite adapter once local marker blocks and seams are
supplied with additive signatures.  The missing step is not another semigroup
lemma: it is identifying those signatures with the actual boundary-controller
geometry.  This chapter makes that evidence obligation machine-readable.

A catalogue entry records its block length, local point set, controller ports,
action vector, loss vector, seam type, source file, and evidence level.

## 1. Catalogue-lineage certificate

### Theorem PP3con -- PROVED / BOUNDARY CATALOGUE LINEAGE AUDIT

A finite sequence of marker catalogues can be safely composed only when every
renaming or replacement is accompanied by an explicit signature-preserving map.
Equality of asymptotic roles, mean costs, or semigroup conductors is not such a
map.

#### Proof

The adapter consumes exact local data: lengths determine concatenation, ports
determine seam legality, and signatures determine the additive output.  Two
catalogues with different block alphabets or signatures may have the same
limiting rate while producing different finite boundary states.  Therefore a
composition proof requires an explicit map preserving every consumed field. ∎

## 2. First-appearance barrier for the four/seven catalogue

### Theorem PP3coo -- PROVED / FOUR-SEVEN FIXTURE PROVENANCE

The stored boundary lineage uses the following length alphabets:

```text
docs/519: {2,3};
docs/525: {1,2,4};
docs/531: {1,2,3};
docs/537: {1,4,7};
docs/544 and docs/549: {4,7}.
```

No signature-preserving map between these catalogues is recorded.  In
particular, the phase-locked four/seven catalogue first appears as a stored
fixture rather than as an extraction from a prime-patching boundary block.
Consequently the numerical row `7/120` remains fixture-backed.

#### Proof

The six source records are finite and are listed in
`certificates/prime-patching-provenance-audit-555-560.json`.  Their block-length
sets are not constant, and every source role is marked `stored_fixture` or
`adapter_fixture`.  The independent geometric-source field is empty.  The
provenance conclusion follows directly from the typed adapter requirement in
`PP3con`. ∎

## 3. Exact promotion contract

### Theorem PP3cop -- PROVED / BOUNDARY DATA-EXTRACTION CONTRACT

A boundary row may be promoted to `geometric_verified` once a finite certificate
supplies:

1. the local point set of every block;
2. oriented controller ports and seam compatibility;
3. direct defect, action, controller, and loss signatures;
4. a reconstruction of every concatenated word from those local objects;
5. a machine-checkable link to the geometric definitions used by the patch.

These fields are sufficient for `docs/549`; omission of any consumed field keeps
the row conditional.

#### Proof

With all five items, local verification establishes every block and seam, and
additivity reconstructs the global signature exactly.  Conversely, each item is
read by either the legality or accounting part of the adapter, so omitting it
leaves an unverified input. ∎

## 4. Stored exact audit

The audit `scripts/check_boundary_catalogue_provenance.py` checks six lineage
stages, five distinct length alphabets, the phase thresholds `60,67,74`, and the
stored `7/120` row for every length through 2000.  It also verifies that no stage
is marked as an independent geometric source.

## 5. Prime-patching consequence

The boundary frontier is now separated into two tasks: the arithmetic
four/seven scheduler is complete, while the geometric block-and-seam extraction
is explicitly open.  Future work can replace the empty source field without
changing the downstream adapter or ledger.
