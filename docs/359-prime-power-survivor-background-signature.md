# Exact finite survivor-background signatures

CMR2030--CMR2045 compute the exact new-triple score of every response from a populated survivor background. This chapter proves that scalar response selection factors through a finite signature and removes the row/column gauge invisible to perfect matchings.

For side `s`, let `G_s={0,...,s-1}^2` and let `L_s` be the union of all normalized affine lines in the canonical response-line kernel.

## Theorem CMR2046 -- PROVED

The exact line-universe sizes are

\[
|L_4|=23,\qquad |L_5|=83.
\]

This follows by taking the canonical union over all 740 hosts and 9,260 responses.

## Theorem CMR2047 -- PROVED

For a finite background `B` disjoint from the response grid, define `p_B(q)` as the number of unordered background pairs collinear with grid point `q`, and define `h_B(L)=|B cap L|` for `L in L_s`. The absolute signature

\[
\Sigma_s(B)=((p_B(q))_{q\in G_s},(h_B(L))_{L\in L_s})
\]

has dimensions 39 on side four and 108 on side five. It determines every exact rank-one, rank-two and rank-three response count.

## Theorem CMR2048 -- PROVED

Write `p_ij=p_B((i,j))` and, for `i,j>0`, define

\[
d_{ij}=p_{ij}-p_{i0}-p_{0j}+p_{00}.
\]

For every response permutation `sigma`,

\[
\sum_i p_{i,\sigma(i)}=C_B+\sum_{i>0,\,\sigma(i)>0}d_{i,\sigma(i)},
\]

where `C_B` is independent of `sigma`. This is the exact row/column gauge decomposition.

## Theorem CMR2049 -- PROVED

Response selection depends only on the reduced signature

\[
\widehat\Sigma_s(B)=((d_{ij})_{1\le i,j<s},(h_B(L))_{L\in L_s}).
\]

Its dimensions are

\[
\boxed{32\text{ on side four},\qquad99\text{ on side five}.}
\]

## Theorem CMR2050 -- PROVED

The common baseline `C_B` together with the reduced cross-differences reconstructs every absolute rank-one response count exactly.

## Theorem CMR2051 -- PROVED

Every canonical response has an affine integer form `F_Q` such that

\[
\boxed{N_B(Q)=C_B+F_Q(\widehat\Sigma_s(B)).}
\]

The coefficients are one on selected cross-difference coordinates, `binom(r_Q(L),2)` on response-line occupancy coordinates, and constant term `W_3(Q)`.

## Theorem CMR2052 -- PROVED

Equal reduced signatures give identical response-score differences, minimizer sets and lexicographic full selectors for every host on that side. Equal common baselines additionally give identical absolute score vectors.

This is an exact scalar-selector quotient only. It does not identify owner, provenance, collision, interface, transition or labelled-child semantics.

## Corollary CMR2053 -- PROVED

`scripts/check_prime_power_background_signature.py` validates the complete basis and arbitrary stored certificates. The fixed basis digest is

\[
\texttt{385ebe3b5f44ae14b6e954623af154a0152cd33562c0bb0e0f2875f6041444fd}.
\]

Its deterministic suite checks 500 systems, 6,166 response scores and 1,706 background points, with minimum distribution `[[0,363],[1,105],[2,23],[3,5],[4,3],[5,1]]`, and rejects twelve corruptions.
