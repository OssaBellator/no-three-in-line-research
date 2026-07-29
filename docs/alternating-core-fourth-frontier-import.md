# Fourth frontier import for AC5 physical and geometric routing

**Branch:** `research/alternating-core-chain`

AC5ay--AC5be import exact common-hole deficiencies, RI collateral through rank three, arbitrary sparse final-state legality, all one-local off-diagonal BDA geometry, protected-event weight quantiles and finite phase-vector recurrence. This note imports the next physical reductions.

## AC5bf -- source-hole multiplicity import -- PROVED

For one AC endpoint switching graph and one cost sublevel `S`, define

\[
M_S=\sum_{a\in A}|S\cap H(a)|,
\qquad
\mu_S=\max_{b\in S}|\{a:b\in H(a)\}|.
\]

Then its exact Hall deficiency obeys

\[
\boxed{
\delta(S)
\le
\max\left\{
(|A|-|S|)_+,
\max_{1\le x\le\min\{|A|,\mu_S\}}
\left(x-|S|+\left\lfloor\frac{M_S}{x}\right\rfloor\right)_+
\right\}.
}
\]

Thus low-event flow can be certified from threshold size, total source-hole mass and maximum endpoint hole multiplicity. Failure returns one of those quantities or one explicit small source cut.

### Proof

Every endpoint common to the holes of an `x`-source cut contributes `x` incidences to the threshold hole mass, and no endpoint can be common to more than `mu_S` sources. Insert these facts into AC5ay. QED.

## AC5bg -- disjoint-support RI bank-readiness import -- PROVED UNDER THE LOCALITY CONTRACT

Suppose an RI block has `m` closed components with pairwise disjoint physical regions, every source-target-shift local replacement is legal in its own region, no constraint meets two regions except target ownership, and distinct sources choose distinct target components. Then all

\[
\boxed{m!h^m}
\]

permutation-times-shift states are legal physical states. Consequently the exact rank-one, rank-two and rank-three I6 collateral laws imported earlier apply without an additional abstract-lift assumption.

Failure is one least support overlap, illegal local state, cross-region constraint, nonbijective ownership, noninjective local state, or missing exterior/blocker/protected field.

### Proof

Disjoint local legality makes the physical union legal; the permutation enforces the only cross-region condition. Distinct indices give distinct states, so the uniform physical bank is the abstract I6 bank. QED.

## AC5bh -- complete off-diagonal BDA incidence import -- PROVED

The remaining nine off-diagonal balanced-floor templates have the following exact geometry:

1. `CD-A`: line coincidence only if `2hv=u(2h+q)`;
2. `CD-B`: line coincidence only if `2(h+q)v=u(2h+q)`;
3. `CD-C` and `CD-D`: no line coincidence for distinct roles;
4. `AB-A` and `AB-B`: radial-line concentration;
5. `AB-C` and `AB-D`: at most one shared context cell;
6. `CD-AB`: exactly one possible shared context point.

Together with AC5bb, all fifteen unordered off-diagonal BDA templates now have explicit incidence geometry. Remaining BDA work is weighted payment, owner realization and higher-rank routing.

### Proof

Use the exact `CD` affine-line equation and `AB` radial line. Substituting the four local vectors gives the two resonance equations, the two impossible equal-role equations, the radial/nonradial split, and the unique `CD-AB` intersection. QED.

## AC5bi -- canonical sparse prefix import -- PROVED

Let a sparse swap word move `r` rows and induce `s` nontrivial cycles in its final image permutation. It has an equivalent canonical implementation using

\[
\boxed{r-s\le r-1}
\]

row swaps. If every prefix must be structurally legal, the canonical two-layer audit uses at most

\[
\boxed{2r(r-1)}
\]

host/collision atoms. Hence arbitrary original word length is removed from the structural legality budget.

If the physical contract forbids equivalent-history replacement, that history dependence is returned as one explicit noncommutation field.

### Proof

Implement each length-`ell` cycle by `ell-1` pivot transpositions and apply AC5ba to every canonical prefix. QED.

## AC5bj -- phase-orbit cycle-sum import -- PROVED UNDER THE SCORE CONTRACT

Let a normalized nonzero phase vector have orbit size `R`. If traversal score decomposes as

\[
G_j=P_j-D_j+\Phi(\phi_j)-\Phi(\phi_{j+1}),
\]

then

\[
\boxed{
\sum_{j=0}^{R-1}G_j
=
\sum_jP_j-\sum_jD_j.
}
\]

Thus a full return yields a positive paying traversal, aggregate physical debt concentrated on one finite obstruction class, an exact balanced orbit eligible for one return ticket, or failure of the score/fixed-profile contract.

### Proof

The phase potential telescopes around the exact finite orbit. Compare total payment and total debt, then pigeonhole debt over the finite obstruction alphabet. QED.

## AC5bk -- polynomial protected-incidence import -- PROVED

Suppose operations eligible for protected address `p` carry a scalar parameter `t`, eligibility implies a nonzero polynomial equation `F_p(t)=0` of degree at most `d_p`, and at most `M_p` operations share one parameter. Then

\[
\boxed{|I_p|\le d_pM_p.}
\]

Therefore its exact protected-event capacity is bounded by the sum of the `d_pM_p` largest eligible operation weights. Failure is one zero-polynomial coefficient profile, excessive degree, excessive parameter multiplicity, failed address equation, or missing eligibility/lineage/context record.

### Proof

A nonzero degree-`d_p` polynomial has at most `d_p` roots; multiply by the physical fibre capacity and invoke AC5bc. QED.

## AC5bl -- strengthened physical continuation -- PROVED UNDER THE DECLARED CONTRACTS

An AC menu satisfying the imported contracts now has one continuation:

1. low-event flow certified by threshold size, total hole mass and endpoint multiplicity, or one exact small Hall-cut witness;
2. a fully physical disjoint-support RI bank with exact collateral through rank three, or one least readiness witness;
3. one explicit incidence output from every off-diagonal BDA template;
4. an `O(r^2)` canonical sparse prefix audit, one structural atom, or one noncommutation/nonstructural field;
5. a finite phase-orbit payment/debt/balanced-return output;
6. a polynomial-fibre protected capacity, or one exact coefficient/multiplicity obstruction;
7. or one existing AC4/AC5 payment, descent, reset, Hall-core or failed physical-contract branch.

This does not yet pay BDA connector/radial outputs, construct disjoint RI regions, prove the actual AC endpoint multiplicity bounds, establish sparse nonstructural guards, define all phase score decompositions, or derive every protected polynomial address map. It makes each remaining task an explicit finite physical object.

## Finite check

`scripts/verify_ac_fourth_frontier_import.py` checks the hole-mass deficiency bound, disjoint-support bank count, mixed BDA determinant identities, canonical permutation compression, cyclic score cancellation and polynomial-fibre capacity on finite abstractions.