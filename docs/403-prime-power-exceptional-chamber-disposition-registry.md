# Exact dispositions for all exceptional selector chambers

The CMR2110 worklist fixes 232 zero-selector chambers and 20 hard-core chambers. This chapter
turns those aggregate obligations into one explicit open/closed record per chamber and permits
direct linkage to final quotient row theorems.

## Theorem CMR2398 — PROVED AS AN INTERFACE

The checker rebuilds and validates the canonical exceptional-selector worklist. Every chamber
receives a source-independent chamber ID derived from:

- host ID and host-worklist digest;
- chamber kind;
- selected response index and affine-row digest;
- selected permutation and rank-three count; and
- selector-chamber digest.

## Theorem CMR2399 — PROVED

The exact chamber universe contains

\[
\boxed{232\text{ zero-selector chambers}+20\text{ hard-core chambers}=252.}
\]

The chamber registry must cover this universe exactly and in canonical kind/host/index order.
Missing, duplicate, unexpected and reordered chamber records are rejected.

## Theorem CMR2400 — PROVED

Every chamber has status `open` or `closed`. An open chamber requires null proof fields. A
closed chamber must use exactly one proof kind:

1. final global-row theorem;
2. direct chamber proof;
3. survivor-signature infeasibility proof; or
4. host-union proof.

## Theorem CMR2401 — PROVED

A `global-row-theorem` disposition must name a row in the exact quotient semantic-refinement
certificate. Its theorem ID, theorem locator and theorem digest must equal that row's semantic
theorem record exactly.

Other proof kinds require null row and theorem IDs and one nonempty proof locator/digest pair.

## Theorem CMR2402 — PROVED

The registry publishes separate exact censuses and digests for zero-selector and hard-core
dispositions, together with the complete proof-kind distribution.

## Theorem CMR2403 — PROVED

Two independent readiness flags are reconstructed:

\[
\boxed{
\texttt{exceptional\_zero\_rows\_ready}
\iff\text{all 232 zero-selector chambers are closed},
}
\]

and

\[
\boxed{
\texttt{hard\_core\_rows\_ready}
\iff\text{all 20 hard-core chambers are closed}.
}
\]

The complete disposition flag is their conjunction.

## Theorem CMR2404 — HONEST CHAMBER BOUNDARY

A closed disposition proves exact documentary coverage and, for row-linked closures, exact
identity with a final quotient theorem record. It does not verify chamber feasibility,
infeasibility, threshold strictness, labelled contraction or the cited mathematical proof.

## Corollary CMR2405 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_exceptional_chamber_disposition_registry.py` reconstructs the fixed
252-chamber universe, validates exact dispositions and publishes the separate 232-zero and
20-hard-core closure fronts.

The checker was syntax-compiled locally. No genuine chamber closure bank or dependency-backed
execution is claimed.
