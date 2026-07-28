# Slot-covered exceptional-fibre tradeoff batches

CMR2134--CMR2141 compute unrestricted, rank-three-constrained and zero-constrained scalar
selectors for one exceptional host. This chapter composes those certificates with a
complete slot-covered fibre batch and enforces exact exceptional-fibre coverage.

## Theorem CMR2182 — PROVED

Given one complete slot/fibre conformance certificate, the checker identifies the
exceptional fibres mechanically from their canonical host IDs. The expected exceptional
set is

\[
\boxed{\{f:\operatorname{host}(f)\text{ belongs to the canonical 89-host exceptional worklist}\}.}
\]

No user-supplied exceptional flag is trusted.

## Theorem CMR2183 — PROVED

For every exceptional fibre, its tradeoff certificate must agree with the populated
linked operation on fibre and host identity, complete survivor background, exact
background-selector certificate, and literal destroyed-current-triple threshold `T`.

Thus the values `M`, `M_3`, `M_0`, their penalties and their deltas are computed on the
same actual finite operation record.

## Theorem CMR2184 — PROVED

The exceptional tradeoff entries must cover the mechanically identified exceptional
fibre set exactly. Missing, duplicate and nonexceptional entries are rejected. This gives
exact exceptional coverage inside the supplied slot-covered batch.

## Theorem CMR2185 — PROVED

For every exceptional fibre, the strictness hierarchy

\[
\boxed{
\mathbf1_{M_3<T}\le\mathbf1_{M<T},
\qquad
\mathbf1_{M_0<T}\le\mathbf1_{M<T}
}
\]

is checked directly. The corresponding penalties remain nonnegative:

\[
M_3-M\ge0,\qquad M_0-M\ge0.
\]

## Theorem CMR2186 — PROVED

The batch reconstructs exact aggregate data, including exceptional operation and host
counts, zero-capable and hard-core fibre counts, response, background and destroyed-
triple totals, unrestricted/rank-three-constrained/zero-constrained strict counts, total
policy penalties, penalty distributions and the full-selected rank-three distribution.

All aggregate values are derived from the entry certificates and protected by the batch
digest.

## Theorem CMR2187 — PROVED

The eleven-host hard-core entries inherit the complete 20-chamber full-selector atlas.
The batch never substitutes the eleven raw rank-three-minimum chambers for the full
background-dependent response family.

The 78 zero-capable hosts retain their exact zero-constrained policy rather than assuming
that a zero-rank-three response is automatically the full selector.

## Theorem CMR2188 — HONEST COMPLETENESS BOUNDARY

Exceptional coverage is complete relative to the supplied slot-covered batch, and that
batch is complete relative to its supplied expected slot registry.

The result still does not prove that the expected slot registry is the genuine exhaustive
parent-rule enumeration. It also does not turn scalar threshold improvement into a
labelled recurrent-row or SCC contraction theorem.

## Corollary CMR2189 — EXECUTABLE ENDPOINT

`scripts/check_prime_power_exceptional_fibre_tradeoff_batch.py` composes slot-covered
batches with exact tradeoff certificates, includes deterministic synthetic complete-batch
regressions and rejects twelve independent corruptions.

The script was syntax-compiled in the publication environment. Its full dependency-backed
regression suite is embedded for execution in the repository's normal Python environment.
