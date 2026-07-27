# Exact rank-three-constrained selector tradeoffs on exceptional hosts

The complete exceptional chamber atlas shows which response minimizes the full
background-dependent new-triple count. This chapter quantifies the exact cost of also
requiring minimum raw rank-three load, or zero raw rank-three load when available.

Fix an exceptional host `H`, survivor background `B`, and destroyed-current-triple count
`T`. For every response `Q`, let `N_B(Q)` be its exact new-triple count.

## Theorem CMR2134 -- PROVED

The unrestricted full minimum is

\[
M(B)=\min_Q N_B(Q).
\]

Its exact scalar operation delta is `M(B)-T`, and the full selector is strictly improving
exactly when

\[
\boxed{M(B)<T.}
\]

## Theorem CMR2135 -- PROVED

Let

\[
m_3=\min_Q\psi_3(Q)
\]

and define the rank-three-constrained minimum

\[
M_3(B)=\min_{\psi_3(Q)=m_3}N_B(Q).
\]

The lexicographically first minimizer in this restricted family is reconstructed exactly.
Its operation delta is `M_3(B)-T`.

## Theorem CMR2136 -- PROVED

The exact rank-three constraint penalty is

\[
\boxed{\pi_3(B)=M_3(B)-M(B)\ge0.}
\]

This is the scalar price of insisting on a raw rank-three-minimum response after the
rank-one and rank-two background terms are included.

## Theorem CMR2137 -- PROVED

Rank-three-constrained strictness implies unrestricted strictness:

\[
M_3(B)<T\Longrightarrow M(B)<T.
\]

The converse can fail precisely when

\[
M(B)<T\le M_3(B).
\]

Thus a full scalar improvement may be lost by imposing the raw rank-three selector.

## Theorem CMR2138 -- PROVED

On each of the 78 zero-rank-three-capable exceptional hosts, define

\[
M_0(B)=\min_{\psi_3(Q)=0}N_B(Q).
\]

Then

\[
\boxed{\pi_0(B)=M_0(B)-M(B)\ge0}
\]

and a zero-rank-three response is strictly improving exactly when `M_0(B)<T`.
Membership in the published 232-chamber zero-selector union agrees exactly with the
unrestricted full selector itself having rank-three load zero.

## Theorem CMR2139 -- PROVED

On the eleven positive-minimum hard-core hosts, the constrained family is the raw
rank-three-minimum family, but the unrestricted selector is evaluated over the complete
20-chamber atlas. The checker never assumes that one of the eleven raw minimum chambers
is the full selector.

## Theorem CMR2140 -- PROVED

For every response the certificate stores the exact tuple

\[
(\psi_1,\psi_2,\psi_3,N_B(Q),N_B(Q)-T)
\]

together with its unrestricted, rank-three-constrained and zero-constrained membership
flags. All minima, penalties, lexicographic selectors and strictness claims are
reconstructed from this table.

## Corollary CMR2141 -- PROVED

`scripts/check_prime_power_exceptional_selector_tradeoff.py` validates arbitrary
exceptional-host tradeoff certificates. Its deterministic suite exercises 500
host/background/threshold systems over all 89 exceptional hosts and its mutation suite
rejects twelve independent corruptions.

These penalties are scalar response-policy quantities. They do not prove operation
legality, labelled child routing or recurrent contraction.
