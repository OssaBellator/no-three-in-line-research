# Exact source provenance for declarative parent-rule clauses

CMR2158--CMR2165 provide a finite clause enumerator but deliberately do not prove that its
cases, domains and exclusions are the genuine mathematical rule. This chapter adds a
complete source-reference graph for every enumerated ingredient.

## Theorem CMR2190 — PROVED AS AN INTERFACE

A source record is the exact tuple

\[
(\text{source ID},\text{kind},\text{locator},\text{statement digest},\text{note}).
\]

Allowed source kinds are definition, case split, lemma, finite-domain statement,
exclusion and computation. Source IDs are unique, records are canonical, and each record
is protected by its own digest.

## Theorem CMR2191 — PROVED

Every parent case in the clause manifest has exactly one provenance link record containing
one or more source IDs. The case-link set must cover the parent-case registry exactly, with
no missing or extraneous case IDs.

At least one cited source must be a definition, case split or lemma.

## Theorem CMR2192 — PROVED

Every rule clause has exactly one provenance link record. Clause links cover the complete
clause set exactly, and each clause cites at least one definition or lemma source.

## Theorem CMR2193 — PROVED

Every finite parameter axis is identified by its exact pair

\[
(\text{clause ID},\text{axis name}).
\]

The axis-provenance links must equal the complete axis set reconstructed from the clause
manifest. Each axis cites a definition, domain statement, lemma or computation.

## Theorem CMR2194 — PROVED

Every excluded parameter row is identified by

\[
(\text{clause ID},\operatorname{SHA256}(\text{canonical row})).
\]

The exclusion-provenance links cover the exact excluded-row set, and each row cites an
exclusion statement, lemma or computation.

## Theorem CMR2195 — PROVED

Source use is checked bidirectionally:

\[
\boxed{\text{every link resolves to a known source and every source is used by a link}.}
\]

Dangling citations and unused source records are both rejected. The checker publishes
source-kind and source-use censuses plus separate digests for every link family.

## Theorem CMR2196 — HONEST SEMANTIC BOUNDARY

A passed certificate proves complete traceability relative to the supplied statements and
locators. It does not prove that a cited statement is correct, that the locator denotes the
intended theorem, or that the cited statements jointly establish genuine parent-rule
exhaustiveness.

## Corollary CMR2197 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_rule_source_provenance.py` validates the clause manifest,
source registry, exact case/clause/axis/exclusion coverage, admissible source kinds,
bidirectional source use and all component digests.

The script was syntax-compiled in the publication environment. A genuine certificate still
requires the actual mathematical rule sources.
