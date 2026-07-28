# Exact synchronization of integer weights across quotient blocks

Cross-block state identification may force two local block weights to represent one global
weight. This chapter derives every rational block-scale relation forced by those shared
states, rejects inconsistent cycles and clears denominators exactly.

## Theorem CMR2262 — PROVED AS AN INTERFACE

For block `b`, let `w_b(s)` be its primitive positive local state weight. Every global state
class containing local members `(b,s)` and `(c,t)` imposes

\[
\boxed{\alpha_b w_b(s)=\alpha_c w_c(t)}
\]

on positive rational block scales `alpha_b` and `alpha_c`.

## Theorem CMR2263 — PROVED

The shared-state constraints generate a labelled block-ratio graph. Starting from the
lexicographically first block in each connected component, the checker propagates exact
`Fraction` scales.

Every repeated path and every cycle must give the same scale. A conflicting shared-state
ratio is rejected.

## Theorem CMR2264 — PROVED

For each connected ratio component, the checker clears every propagated denominator and then
divides the common gcd of the resulting block multipliers.

The published multipliers are therefore the canonical minimal positive integer multipliers
realizing all shared-state equalities in that component.

## Theorem CMR2265 — PROVED

Every global state receives one component weight

\[
\boxed{W_g=m_b\,w_b(s)}
\]

for any local member `(b,s)` of that state. The value is checked against every member and
must be independent of the chosen block.

## Theorem CMR2266 — PROVED

Every local integer quotient row is scaled by its block multiplier. Local target coordinates
are mapped to global states and merged when several local targets belong to one global
class.

The exact scaled identity is checked:

\[
\boxed{
W_p-B_p-\sum_g A_{p,g}W_g=M_p.
}
\]

Here `B_p` and `M_p` are the scaled fixed offset and margin, while `A_{p,g}` remains a
nonnegative integer multiplicity.

## Theorem CMR2267 — PROVED

The certificate publishes every ratio component, block multiplier, global component weight,
scaled row, minimum scaled margin and all component/state/row digests.

## Theorem CMR2268 — HONEST SCALE BOUNDARY

Shared global states determine relative block scales only inside connected overlap
components. Distinct components remain independently normalized until return or interface
rows choose their relative global multipliers.

## Corollary CMR2269 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_cross_block_weight_synchronization.py` validates the state
identification certificate, derives exact rational scale ratios, clears denominators,
publishes minimal integer block multipliers and verifies every scaled quotient row.

The checker was syntax-compiled in the publication environment. No genuine connected family
of populated quotient blocks is yet supplied.
