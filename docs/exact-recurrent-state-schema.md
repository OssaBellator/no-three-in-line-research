# Exact recurrent-state manifest schema

This document defines the first machine-checkable surface for the
`research/exact-recurrent-lyapunov-audit` branch.

## Scope

The manifest records one finite labelled recurrent block and a proposed strict
Lyapunov certificate. The checker validates exact rational arithmetic for the
**declared** block. It does not establish that the block contains every physical
state or that its coefficients were compiled correctly from Euclidean geometry.

A successful manifest therefore has two levels of status:

1. **arithmetic validity:** every declared row satisfies `Ax<x` exactly;
2. **proof eligibility:** state completeness and coefficient provenance are
   separately established by mathematical arguments and executable compilers.

The checker always reports `all_n_proved_by_checker = 0`.

## JSON schema

The root object has the form:

```json
{
  "schema": "exact-recurrent-lyapunov/v1",
  "research_status": "description",
  "declared_state_set_complete": false,
  "coefficient_provenance_complete": false,
  "states": [
    {"id": "state-name", "weight": "positive rational"}
  ],
  "rows": [
    {
      "parent": "state-name",
      "offspring": {"child-state": "nonnegative rational"},
      "slack": "positive rational"
    }
  ]
}
```

All rational numbers are strings accepted by Python's exact `Fraction` parser,
for example `"7"`, `"3/5"` or `"-2/9"`. State weights and row slacks must be
positive. Offspring coefficients must be nonnegative.

Exactly one row is required for every declared state. Omitted child coefficients
are interpreted as zero. Unknown child labels, duplicate states, duplicate rows,
negative coefficients, incomplete row coverage and inexact slack declarations
are rejected.

## Exact row identity

For parent `i`, state weights `x_j` and declared offspring coefficients `A_ij`,
the checker computes

\[
L_i=\sum_j A_{ij}x_j
\]

and requires the declared slack to equal

\[
\epsilon_i=x_i-L_i>0.
\]

Thus every accepted row satisfies

\[
\sum_j A_{ij}x_j=x_i-\epsilon_i<x_i.
\]

No floating-point arithmetic is used.

## Completeness obligations outside the checker

### Physical state completeness

A state extractor must prove that every recurrent physical configuration maps to
one declared label. The label must retain every field that may change the future
response law, including:

- exact active matching host;
- current and structural owner;
- protected registry and reserve state;
- line-height, carry and collision profiles;
- return, restoration and selector status;
- ancestry and factor position;
- prime-field, prime-power or CRT provenance;
- operation-family and intermediate-state legality data.

A quotient is invalid if two merged physical states have different legal child
laws and no proved common componentwise upper row.

### Coefficient provenance completeness

Every nonzero coefficient must be traceable to one of:

- exact finite enumeration of legal responses;
- a proved symbolic counting identity;
- a proved responsewise componentwise upper bound;
- a verified assignment-dual or occupancy certificate whose hypotheses are
  attached to the parent label.

The compiler must include all rank-one, rank-two and rank-three geometric terms,
return costs, selector costs, restoration costs, protected-reserve debits and
recreated historical certificates. A term may not be charged to two different
credits.

### Execution closure

The row law must cover the actual legal repair operation, including every
intermediate state. A final endpoint that is safe only after passing through an
illegal intermediate state is not a valid response.

### Global closure

Even a complete strict recurrent block proves only termination of that block. A
full no-three-in-line proof additionally needs a well-founded entry/descent
argument, construction correctness at termination, prime and prime-power
interfaces, arbitrary-side assembly and finite-exception coverage.

## Falsification records

A failed block should be published rather than hidden. Recommended records are:

```json
{
  "kind": "realizable-supercritical-row",
  "parent": "state-id",
  "witness": "path or embedded data",
  "reason": "exact offspring lower bound prevents strictness"
}
```

or

```json
{
  "kind": "state-quotient-collision",
  "label": "merged-label",
  "physical_witnesses": ["witness-a", "witness-b"],
  "reason": "different legal offspring laws"
}
```

Other useful negative outputs include an exact recurrent cycle, a missing
operation, an unavoidable illegal intermediate state, or a finite saturated host
with no move in the installed bank.

## Proof-eligibility flags

The initial checker accepts two declarations:

```text
declared_state_set_complete
coefficient_provenance_complete
```

It reports `proof_eligible_under_manifest_declarations = 1` only when both are
true. This is deliberately a declaration-level flag, not independent verification.
Future compilers should replace declarations by digests of state-extraction and
coefficient-provenance manifests.

## Version-one limitations

Version one intentionally checks only the final finite matrix inequality. It does
not yet encode:

- contracted assignment duals;
- host perfect-matching extendability;
- geometric source traces;
- operation-registry coverage;
- parent/child descent ranks;
- auxiliary SCC resolvents;
- all-`n` transfer data.

Those surfaces should be added only after a first nontrivial physically complete
recurrent block has been reconstructed. The branch prioritizes exactness of one
small block over breadth of another abstract interface.
