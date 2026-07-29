# Third frontier import for alternating-core event and recurrence routing

**Branch:** `research/alternating-core-chain`

AC5ap--AC5ax import shifted endpoint quantiles, bounded conditioning, bank-ready RI ranks one and two, diagonal BDA separation, and finite sparse structural alphabets.  This note imports the next exact reductions: threshold-local common holes, bank-ready RI rank three, arbitrary swap words, one-local BDA connector lines, simultaneous phase-vector recurrence, and protected-event weight quantiles.

## AC5ay -- exact common-hole threshold import -- PROVED

For one AC candidate graph `Gamma subseteq A x B`, put

\[
H(a)=B\setminus N_\Gamma(a),
\qquad
H(X)=\bigcap_{a\in X}H(a).
\]

For an endpoint-cost sublevel `B_<k`, its exact Hall deficiency is

\[
\boxed{
\delta_k=
\max_{\varnothing\ne X\subseteq A}
\bigl(|X|-|B_{<k}|+|B_{<k}\cap H(X)|\bigr)_+.
}
\]

Hence

\[
\boxed{
\operatorname{OPT}(c)=\sum_k\delta_k.
}
\]

The same formula holds after compatible endpoint conditioning by intersecting every set with the surviving endpoint set.

### Proof

An endpoint is outside the neighbourhood of `X` exactly when it lies in every hole set `H(a)`, so `B\setminus N(X)=H(X)`.  Substitute into the deficiency form of Hall's theorem and then use the endpoint-cost threshold identity. QED.

## AC5az -- bank-ready RI rank-three import -- PROVED UNDER THE PHYSICAL BLOCK HYPOTHESES

Let one installed RI block have `m` source cosets of subgroup order `h`.  For a weighted multiset of compatible rank-three prescriptions using distinct source and target cosets, with raw weight `Q_3`,

\[
\boxed{
\mathbb E C_3=\frac{Q_3}{(m)_3h^3}.
}
\]

Together with the earlier rank-one and rank-two laws, the complete distinct-coset rank-at-most-three collateral is

\[
\boxed{
\frac{Q_1}{mh}
+\frac{Q_2}{(m)_2h^2}
+\frac{Q_3}{(m)_3h^3}.
}
\]

Repeated-coset and blocker-repair terms retain their actual correlation laws.

### Proof

A rank-three prescription fixes three coset-permutation images and three shifts, leaving `(m-3)!h^(m-3)` of the `m!h^m` I6 states.  Use weighted linearity. QED.

## AC5ba -- arbitrary sparse swap-word structural import -- PROVED

Let a finite word of row swaps induce a permutation `alpha` of the moved-row support `R`, so the final first-layer image at row `i` is `pi(alpha(i))`.  Final structural legality is equivalent to, for every moved row,

\[
\boxed{
(i,\pi(\alpha(i)))\in E(G)
}
\]

and, in two layers,

\[
\boxed{
\pi(\alpha(i))\ne\rho(i).
}
\]

Thus the complete final-state structural cause alphabet has at most `2|R|` atoms.  Required intermediate states are checked by applying the same criterion to each declared prefix permutation.

### Proof

The word only permutes the distinct current images on `R`, so bijectivity is automatic.  Exactly the displayed host edges and row-local layer collisions can change. QED.

## AC5bb -- off-diagonal one-local BDA connector import -- PROVED

For distinct one-local channel vectors `z,z'` and roles `u,v`, any context-pair address present under both role/channel states either has the exact collision `uz=vz'` or lies on the unique connector line

\[
\boxed{
\operatorname{line}(P+uz,P+vz').
}
\]

If both role-side families have weight at least `Q`, then either connector overlap has weight at least `Q/2`, or both exclusive address families have weight greater than `Q/2`.  This closes the overlap geometry of all six unordered one-local off-diagonal BDA templates.

### Proof

A common context pair determines one line containing both local cells.  Aggregate aliases and remove the pointwise minimum weight from both role families to obtain the exact overlap/exclusive decomposition. QED.

## AC5bc -- protected-event weight-quantile import -- PROVED

For each protected address `p`, let `d_p` be an occurrence-faithful incidence cap and let

\[
S_p(d_p)
\]

be the sum of the `d_p` largest weights among operations physically eligible for `p`.  Then

\[
\boxed{
H_p\le S_p(d_p),
\qquad
U\le\sum_pS_p(d_p).
}
\]

If the aggregate top-weight capacity is at most `eta W`, the clean-height same-token router retains the existing payment and Hall-deficiency bounds with factor `1-eta`; failure is one exact incidence, eligibility or record obstruction.

### Proof

Among subsets of at most `d_p` eligible operations, the largest possible total weight is the sum of the `d_p` largest weights.  Sum over addresses and invoke the geometric-cleaning capacity router. QED.

## AC5bd -- simultaneous phase-vector recurrence import -- PROVED UNDER THE FIXED-PROFILE CONTRACT

For a complete normalized phase profile with component invariant vector

\[
\Omega=(\Omega_1,\ldots,\Omega_\kappa)
\in(\mathbb Z/h\mathbb Z)^\kappa,
\]

repeated use has exact quotient orbit size

\[
\boxed{
\frac{h}{\gcd(h,\Omega_1,\ldots,\Omega_\kappa)}.
}
\]

A capacity-one ticket for each noninitial vector phase bounds reset-free nontrivial recurrence by one less than this order.  The zero vector is quotient-trivial and enters physical payment or a non-gauge-invariant obstruction.

### Proof

The least positive multiplier killing every component is the lcm of the component additive orders, equal to the displayed common-modulus gcd formula. QED.

## AC5be -- strengthened exact continuation -- PROVED UNDER THE DECLARED CONTRACTS

An AC menu satisfying the imported physical hypotheses now has one continuation:

1. exact low-event flow via the common-hole threshold deficiencies;
2. exact bank-ready RI collateral through rank three;
3. one connector/exclusive/collision BDA output for every one-local off-diagonal comparison;
4. one structural atom from an arbitrary sparse swap word, or a nonstructural guard;
5. clean-height-safe payment/Hall deficiency from protected-event weight quantiles, or one exact protected-address obstruction;
6. a finite normalized phase-vector orbit, physical return, descent, reset or stutter;
7. or one already named AC4/AC5 overload or failed physical contract.

This import does not prove the required common-hole intersection bounds, classify the nine BDA templates involving `CD` or `AB`, establish physical bank readiness, or pay zero-vector/zero-shift physical returns.  It converts all of those gaps into explicit finite terms of the existing AC4/AC5 routers.

## Finite check

`scripts/verify_ac_third_frontier_import.py` checks the common-hole deficiency identity, rank-three I6 count, arbitrary image-permutation structural criterion, connector-line overlap, top-weight capacity and component-vector order on finite instances.
