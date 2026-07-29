# Sixth frontier import for AC5 quantitative payment routing

**Branch:** `research/alternating-core-chain`

AC5bm--AC5bs import RI conflict-graph extraction, high-multiplicity endpoint trimming, weighted BDA overlap closure, sparse state-local auditing, zero-vector decoration recurrence and affine protected-line capacities. This note imports the next quantitative payment reductions.

## AC5bt -- heavy RI conflict-neighborhood import -- PROVED

Fix a requested RI subbank size `q>=2` and total component paid weight `W`. If the component conflict graph has no independent set of size `q`, then one component `v` has closed conflict neighborhood weight

\[
\boxed{w(N[v])\ge\frac{W}{q-1}.}
\]

Thus failure to extract the requested physical bank returns one heavy center-and-neighborhood object, whose incident edges retain their least overlap, cross-constraint, owner, occurrence or exterior-field labels.

### Proof

Take a maximal independent set. It has at most `q-1` vertices and its closed neighborhoods cover the component inventory. Pigeonhole the total paid weight over those neighborhoods. QED.

## AC5bu -- weighted exceptional endpoint/source-star import -- PROVED

For one low-event endpoint set `S`, give endpoint `b` weight `lambda_b` and define weighted hole mass

\[
\mathcal M_S=\sum_{b\in S}\nu(b)\lambda_b.
\]

For `T_tau={b:nu(b)>tau}`,

\[
\boxed{
\sum_{b\in T_\tau}\lambda_b
\le
\frac{\mathcal M_S}{\tau+1}.
}
\]

Moreover one source has weighted hole star at least

\[
\boxed{\mathcal M_S/|A|.}
\]

Hence large exceptional event weight concentrates on one source-local star.

### Proof

Every exceptional endpoint contributes at least `tau+1` times its weight to `mathcal M_S`. The second identity for weighted hole mass is a sum over source stars; pigeonhole. QED.

## AC5bv -- BDA line matching/star import -- PROVED

Let a connector, resonant or radial BDA line carry pair-address weight `W_L`. If every context cell belongs to at most `d` positive-weight addresses, the line contains a vertex-disjoint pair family of weight at least

\[
\boxed{W_L/(2d-1).}
\]

Otherwise one context cell lies in more than `d` pair addresses and is returned as a high-incidence line star.

### Proof

Greedily select pair addresses in decreasing weight order. Each selected pair deletes at most `2d-1` addresses of no greater weight. QED.

## AC5bw -- sparse fundamental-cycle import -- PROVED

Let `Q` be the finite legal-state graph for one sparse physical profile, and let `c` be an antisymmetric transition charge. Choose a spanning forest. The charge is an endpoint potential if and only if all

\[
\boxed{|E(Q)|-|V(Q)|+\kappa(Q)}
\]

fundamental-cycle defects vanish. Otherwise one non-tree edge returns a least nonzero cycle defect. Thus comparison with arbitrary original histories is replaced by one finite cycle-basis audit.

### Proof

Integrate `c` along the spanning forest to define a tree potential. A non-tree edge satisfies the same potential identity exactly when its fundamental-cycle circulation is zero. QED.

## AC5bx -- factorized decoration-dictionary import -- PROVED

Suppose the nonreconstructible physical decoration fields have alphabets of sizes `K_1,...,K_r`. Then the zero-vector decoration dictionary has size at most

\[
\boxed{K\le\prod_{i=1}^rK_i.}
\]

A deterministic history repeats within `K` transitions. Fields reconstructible from the current board, quotient profile and remaining fields contribute no independent factor. If `K_i<=C_i n^{a_i}`, the complete recurrence stock is polynomial with exponent `sum_i a_i`.

### Proof

Compatible decorations form a subset of the product alphabet. Reconstruction makes projection onto the remaining coordinates injective. Apply AC5bq. QED.

## AC5by -- polynomial protected-event chart import -- PROVED

For three polynomial cell trajectories, let

\[
p=\deg(X_2-X_1),\qquad q=\deg(X_3-X_1).
\]

Their collinearity determinant has degree at most `p+q`. If it is nonzero and at most `M` physical operations share one parameter, the chart has incidence at most

\[
\boxed{(p+q)M}
\]

and top-weight capacity `S((p+q)M)`. A finite piecewise-polynomial chart dictionary is handled by summing these chart capacities. Failure is one identically-zero coefficient profile, excessive degree/fibre multiplicity, or a chart/alias/lineage defect.

### Proof

Each determinant monomial uses one coordinate from each difference vector, so its degree is at most `p+q`. Apply the polynomial root bound and AC5bk. QED.

## AC5bz -- strengthened quantitative continuation -- PROVED UNDER THE DECLARED CONTRACTS

An AC menu now has one exact continuation:

1. a requested physical RI subbank, or one conflict neighborhood carrying at least `W/(q-1)` paid weight;
2. trimmed low-event flow with exceptional weight at most `mathcal M_S/(tau+1)`, or one weighted source-hole star;
3. a disjoint BDA pair stock of weight at least `W_L/(2d-1)`, or one high-incidence context-cell star;
4. a sparse endpoint potential, or one fundamental-cycle/antisymmetry/lineage defect from a finite state graph;
5. a factorized polynomial-size decoration recurrence, or one least field/reconstruction/compatibility defect;
6. a polynomial protected-event capacity, or one coefficient/degree/fibre/chart obstruction;
7. or one existing AC4/AC5 payment, descent, Hall-core, reset, ticket or failed physical contract.

This does not yet pay every returned neighborhood or star, construct every finite state graph and decoration alphabet, or produce every polynomial chart. It reduces those gaps to explicit weighted local objects and finite dictionaries.

## Finite check

`scripts/verify_ac_sixth_frontier_import.py` checks the conflict-neighborhood cover, weighted exceptional-star bounds, line matching estimate, fundamental-cycle criterion, product decoration stock and polynomial determinant degree on finite abstractions.