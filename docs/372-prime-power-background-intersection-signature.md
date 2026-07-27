# Exact tracked-intersection occupancy signatures

CMR2094--CMR2101 bound every concurrent pencil by `n+k-1`. That bound is sharp only when
the common intersection belongs to the survivor background. This chapter records the
intersection occupancy exactly and tightens every unoccupied pencil.

Fix the finite tracked response-line universe and survivor background `B`.

## Theorem CMR2150 -- PROVED

For every rational intersection point `x` of tracked lines, define

\[
\epsilon_B(x)=
\begin{cases}
1,&x\in B,\\
0,&x\notin B.
\end{cases}
\]

A nonintegral rational intersection automatically has `epsilon_B(x)=0`, since survivor
background points have integer coordinates.

## Theorem CMR2151 -- PROVED

Let `L_1,...,L_k` be the complete tracked pencil through `x`. Then

\[
\boxed{
\sum_{i=1}^k h_B(L_i)
=
\left|B\cap\bigcup_{i=1}^k L_i\right|
+(k-1)\epsilon_B(x).
}
\]

Every background point other than `x` lies on at most one line of the pencil, while `x`
contributes once to the union and `k` times to the incidence sum.

## Theorem CMR2152 -- PROVED

The exact sharpened pencil bound is

\[
\boxed{
\sum_{i=1}^k h_B(L_i)
\le |B|+(k-1)\epsilon_B(x).
}
\]

Hence an unoccupied intersection gives the stronger bound

\[
\sum_i h_B(L_i)\le |B|,
\]

rather than the unconditional `|B|+k-1` bound.

## Theorem CMR2153 -- PROVED

For each background point `b`, let `d(b)` be the number of tracked response lines through
`b`. The exact global incidence identity is

\[
\boxed{
\sum_L h_B(L)=\sum_{b\in B}d(b).
}
\]

The certificate stores every point's exact tracked-line index set and the complete degree
distribution.

## Theorem CMR2154 -- PROVED

Every stored degree satisfies the previously proved finite concurrency bound

\[
d(b)\le\mu_s,
\qquad
\mu_4=7,
\quad
\mu_5=11.
\]

Thus the global incidence inequality is recovered as a direct corollary of the exact
degree identity.

## Theorem CMR2155 -- PROVED

The intersection signature stores for every pencil:

- its exact rational common point;
- its tracked line indices;
- the occupancy bit `epsilon_B(x)`;
- the incidence sum;
- the exact background union size;
- the sharpened bound and its slack.

All pencil records and point-degree records are protected by separate digests and one
final intersection-signature digest.

## Theorem CMR2156 -- PROVED

The intersection signature composes with the complete CMR2101 feasibility certificate.
Consequently every accepted record satisfies the line, pair, parallel, unconditional
pencil, global concurrency and local residual constraints before the sharpened
intersection identities are checked.

## Corollary CMR2157 -- PROVED

`scripts/check_prime_power_background_intersection_signature.py` validates arbitrary
side-four/five survivor backgrounds. Its deterministic suite exercises 500 systems and
every rational pencil in their finite line universes; twelve independent corruptions are
rejected.

This is an exact refinement for populated backgrounds. It is not a complete abstract
characterization of all realizable occupancy vectors.
