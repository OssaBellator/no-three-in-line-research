# Residual realizability structure of survivor-background signatures

CMR2046--CMR2061 reduce scalar response selection to grid pair counts and occupancies
on the finite canonical response-line universe.  Those coordinates are not arbitrary:
every tracked response line contributes a known collection of background pairs to each
grid-point pair count.  This chapter removes that forced contribution and exposes the
remaining nonnegative residual.

For side `s`, let `L_s` be the canonical response-line universe.  For a survivor
background `B`, write

\[
p_B(q)=\#\{\{b_1,b_2\}\subset B:q,b_1,b_2\text{ collinear}\},
\qquad h_B(L)=|B\cap L|.
\]

## Theorem CMR2070 -- PROVED

For every response-grid point `q`, the background pairs counted by `p_B(q)` partition
uniquely according to their supporting affine line.  The contribution from tracked
response lines is

\[
t_B(q)=\sum_{\substack{L\in L_s\\q\in L}}\binom{h_B(L)}2.
\]

The summands are disjoint because two distinct background points determine one affine
line.

## Theorem CMR2071 -- PROVED

Define the residual pair count

\[
\boxed{u_B(q)=p_B(q)-t_B(q).}
\]

Then `u_B(q)` is a nonnegative integer for every grid point.  Equivalently every
realizable absolute background signature satisfies the exact finite inequalities

\[
\boxed{
p_B(q)\ge
\sum_{\substack{L\in L_s\\q\in L}}\binom{h_B(L)}2
}
\qquad(q\in G_s).
\]

These are necessary realizability constraints.  They are not asserted to be a complete
characterization of all realizable signatures.

## Theorem CMR2072 -- PROVED

For a response `Q`, put `r_Q(L)=|Q\cap L|`.  On one tracked line, the rank-one,
rank-two and rank-three contributions combine by Vandermonde's identity:

\[
r_Q(L)\binom{h_B(L)}2
+\binom{r_Q(L)}2h_B(L)
+\binom{r_Q(L)}3
=
\binom{h_B(L)+r_Q(L)}3-\binom{h_B(L)}3.
\]

This remains valid when `r_Q(L)` is zero or one; hence all lines in `L_s`, not merely
the pair-support lines of the current response, may be used uniformly.

## Theorem CMR2073 -- PROVED

The exact new-triple score has the residual line-cluster factorization

\[
\boxed{
N_B(Q)
=
\sum_{q\in Q}u_B(q)
+
\sum_{L\in L_s}
\left[
\binom{h_B(L)+r_Q(L)}3-
\binom{h_B(L)}3
\right].
}
\]

The first term counts background pairs whose supporting line is outside the tracked
line universe.  The second term counts every new triple supported on a tracked line.
The two classes are disjoint and exhaustive.

## Theorem CMR2074 -- PROVED

The perfect-matching row/column gauge applies to the residual grid weights `u_B(q)`.
For `i,j>0`, define

\[
e_{ij}=u_{ij}-u_{i0}-u_{0j}+u_{00}.
\]

Then `sum_{q in Q}u_B(q)` is one response-independent baseline plus the selected
cross-differences `e_ij`.  Thus the residual selector dimensions remain

\[
\boxed{32\text{ on side four},\qquad99\text{ on side five}.}
\]

The change from `p` to `u` adds realizability structure without increasing selector
dimension.

## Theorem CMR2075 -- PROVED

A residual signature consisting of

1. the residual cross-differences;
2. the residual common baseline; and
3. the tracked line occupancies

reconstructs every absolute response score exactly.  Equal reduced residual signatures
give identical response-score differences, minimizer sets and lexicographic scalar
selectors on every host of the same side.

This remains a scalar quotient only.  Equal residual signatures do not identify
owners, fates, state labels, transitions or labelled offspring vectors.

## Theorem CMR2076 -- PROVED

A deterministic 500-system suite checks arbitrary canonical hosts and backgrounds,
verifies all nonnegative residual inequalities, compares the residual formula with the
independent absolute-signature and literal-collinearity scores response by response,
and checks the reduced residual gauge reconstruction.

The suite is an interface regression, not a frequency estimate for the unpopulated
real fibres.

## Corollary CMR2077 -- PROVED

`scripts/check_prime_power_background_residual_signature.py` validates arbitrary stored
certificates, records residual and tracked pair masses, publishes the exact scalar
selector, and rejects twelve independent corruptions.

Passing proves the stated finite partition and score identities.  It does not prove
that an arbitrary nonnegative residual vector is geometrically realizable, or that a
scalar selector contracts a labelled recurrent block.
