# Exact affine chambers for background-dependent selectors

CMR2051 writes every exact response score as a common background baseline plus an affine integer form on the reduced survivor-background signature. This chapter publishes the finite row library and the exact lexicographic chamber criterion.

## Theorem CMR2054 -- PROVED

Every canonical response `Q` has affine row

\[
F_Q(d,h)=\sum_{(i,j)\in Q,\,i,j>0}d_{ij}+\sum_L\binom{r_Q(L)}2h_L+W_3(Q).
\]

The row is determined solely by the coordinate-labelled response geometry.

## Theorem CMR2055 -- PROVED

Across all 9,260 response occurrences there are exactly 39 distinct affine rows: six on side four and 33 on side five.

## Theorem CMR2056 -- PROVED

Let a host's responses be ordered lexicographically as `Q_0,...,Q_{Z-1}`. Then `Q_i` is the deterministic full selector exactly when

\[
F_{Q_i}(x)<F_{Q_j}(x)\quad(j<i)
\]

and

\[
F_{Q_i}(x)\le F_{Q_j}(x)\quad(j>i).
\]

The common rank-one baseline cancels from every comparison.

## Corollary CMR2057 -- PROVED

Each deterministic selector region is an integer polyhedral chamber. Facets against lexicographically earlier responses are strict; facets against later responses are non-strict. Every populated signature belongs to exactly one deterministic chamber.

## Theorem CMR2058 -- PROVED

The 740 host chambers contain 125,448 ordered response comparisons: 378 on side four and 125,070 on side five. Deduplication by affine-row pair leaves 1,086 ordered pairs: 30 on side four and 1,056 on side five.

## Theorem CMR2059 -- PROVED

The global row library, a host's ordered row-digest list and one reduced background signature reconstruct every response score up to the common baseline, the complete minimizer set and the deterministic full selector. No new collinearity test is required after the signature is certified.

## Theorem CMR2060 -- PROVED

A fixed 500-system suite evaluates 6,376 response rows and 5,876 selected-chamber inequalities. Every affine selector agrees with the independently reconstructed exact background-signature selector.

These are interface checks, not estimates of chamber frequencies on the still-unpopulated real fibres.

## Corollary CMR2061 -- PROVED

`scripts/check_prime_power_selector_chamber_manifest.py` validates the full row library, host chamber lists and ordered row-pair census. Its fixed digest is

\[
\texttt{34ced8ddcb096a238e91d576754e8d77c924c667ae122e991c99c473fa882b27}.
\]

The mutation suite rejects twelve corruptions. The chambers are exact for scalar response selection only; they do not identify labelled child states or prove recurrent contraction.
