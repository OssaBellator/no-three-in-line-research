# Source-independent derivation of the expected global family

CMR2278--CMR2285 validate a global integer quotient relative to an explicit expected family
manifest. This chapter removes the possibility that the manifest is copied from the populated
rows by deriving it from a separate finite recurrence skeleton.

## Theorem CMR2286 — PROVED AS AN INTERFACE

A recurrence skeleton contains one canonical parent clause for every expected global parent.
Each clause records

\[
(\text{parent},\text{row kind},\text{source rule},\text{source case},
 \text{expected block or interface row},\text{evidence}).
\]

The clause contains no selected fibre, selected response, populated row digest or computed
margin.

## Theorem CMR2287 — PROVED

Parent clauses are canonically ordered and duplicate-free. Recurrent clauses name exactly one
expected integer block and no interface-row ID. Return, interface and off-diagonal clauses name
exactly one interface-row ID and no recurrent block.

Every interface-row ID is unique and every global parent occurs once.

## Theorem CMR2288 — PROVED

The expected family manifest is reconstructed mechanically from the skeleton:

\[
\boxed{
\begin{aligned}
\mathcal B&=\{\text{block IDs named by recurrent clauses}\},\\
\mathcal I&=\{\text{row IDs named by nonrecurrent clauses}\},\\
\mathcal P&=\{\text{all clause parents}\}.
\end{aligned}}
\]

The resulting family ID, evidence string and manifest digest are canonical.

## Theorem CMR2289 — PROVED

The family manifest embedded in the global quotient must equal the skeleton-derived manifest
exactly. Thus expected block, interface-row and parent coverage cannot be chosen after reading
the populated quotient family.

## Theorem CMR2290 — PROVED

Every final global row is bound back to its unique skeleton clause. Parent, row kind and source
rule/case must agree. Recurrent rows must use the clause's expected block and canonical
`recurrent::<block>::<parent>` row ID; nonrecurrent rows must use the exact expected interface
row ID.

## Theorem CMR2291 — PROVED

The certificate publishes exact recurrent/nonrecurrent parent counts, block-parent census,
row-kind census, every row binding and all skeleton, manifest, row and certificate digests.

## Theorem CMR2292 — HONEST EXHAUSTIVENESS BOUNDARY

The construction proves that the expected family is independent of the populated quotient
relative to the supplied recurrence skeleton. It does not prove that the skeleton is the
actual exhaustive recurrence or that its source rule and case statements are mathematically
correct.

## Corollary CMR2293 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_global_family_skeleton.py` validates the source-independent parent
clauses, derives the expected family manifest and binds every populated global row to its
unique skeleton clause.

The checker was syntax-compiled in the publication environment. No genuine exhaustive
recurrence skeleton is yet supplied.
