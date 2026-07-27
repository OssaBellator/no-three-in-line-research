# Exact selector-chamber worklist for all exceptional raw hosts

The 89 uniform-critical or uniform-excess raw hosts require complete background-
dependent response selection. This chapter links each exceptional host to the global
39-row affine library and publishes the exact selector chambers relevant to its rank-
three worklist.

## Theorem CMR2110 -- PROVED

Every exceptional priority record is linked to its canonical catalogue digest and its
ordered affine response rows. The resulting worklist contains exactly 89 hosts:

\[
\boxed{78\text{ zero-rank-three-capable},\qquad11\text{ positive-minimum hard core}.}
\]

## Theorem CMR2111 -- PROVED

For a zero-rank-three response `Q_i` of an exceptional host with lexicographically
ordered rows `F_0,...,F_{Z-1}`, its exact full-selector chamber is

\[
F_i<F_j\quad(j<i),
\qquad
F_i\le F_j\quad(j>i).
\]

The union over all zero-rank-three responses is therefore exactly the set of reduced
survivor signatures for which the deterministic full selector has rank-three load zero.
No geometric approximation or average is used.

## Theorem CMR2112 -- PROVED

The 78 zero-capable exceptional hosts contain exactly

\[
\boxed{232}
\]

zero-rank-three response chambers. Their per-host chamber distribution is

\[
\boxed{[[1,13],[2,13],[3,22],[4,23],[5,7]].}
\]

Thus 13 hosts have only one scalar chamber capable of retaining zero rank-three load,
while seven hosts have five such chambers.

## Theorem CMR2113 -- PROVED

The 232 zero-selector chambers contain 2,134 hostwise affine inequalities. After
deduplication by ordered selected/competing affine-row pair and strictness flag, only
349 distinct conditions remain.

Each inequality is stored as an exact sparse integer difference in the residual
rank-one cross coordinates, tracked-line occupancy coordinates and rank-three constant.

## Theorem CMR2114 -- PROVED

The eleven positive-minimum hard-core hosts require an all-response chamber atlas, not
only the raw rank-three-minimum responses. Their response families contain exactly 20
full-selector chambers:

- nine two-response hosts; and
- two one-response hosts.

Only 11 of these 20 chambers select a raw rank-three minimum. The minimum distribution
remains nine chambers at one triple and two at four triples.

## Theorem CMR2115 -- PROVED

Background rank-one and rank-two terms can make the full selector choose a nonminimum
rank-three response on a hard-core host. Therefore a hard-core proof may not restrict
its search to the 11 raw minimum chambers unless it separately proves the required
background inequalities.

The 20 hard-core chambers use 18 hostwise inequalities but only two distinct ordered
affine-row conditions, reflecting the common two-response geometry of the nine
nontrivial hard-core hosts.

## Theorem CMR2116 -- PROVED

A deterministic 500-system exceptional-host regression has selected rank-three
distribution

\[
\boxed{[[0,395],[1,91],[4,14]].}
\]

On every zero-capable host, membership in the published zero-chamber union agrees
exactly with the full selector having rank-three load zero. On every hard-core host,
the selected row belongs to the complete 20-chamber atlas.

These are fixed synthetic-background regression counts, not estimates of real-fibre
frequencies.

## Corollary CMR2117 -- PROVED

`scripts/check_prime_power_exceptional_selector_chamber_worklist.py` links the
exceptional priority manifest, canonical catalogue and affine chamber library, validates
the complete chamber worklist, and rejects twelve independent corruptions. Its fixed
digest is

\[
\texttt{113fe7949eab855927e1f1756a52df2a2c6e0871afc87cfe3e8bd325fe010044}.
\]

The worklist determines exact scalar response regions. It does not supply the genuine
survivor signatures, destroyed thresholds, child vectors or recurrent-row semantics.
