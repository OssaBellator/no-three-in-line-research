# Live composite-modulus theorem ledger continuation 4

The authoritative live ledger is split across:

- `composite-modulus-theorem-index-live.md` through CMR747;
- `composite-modulus-theorem-index-live-continuation.md` through CMR869;
- `composite-modulus-theorem-index-live-continuation-2.md` through CMR1197;
- `composite-modulus-theorem-index-live-continuation-3.md` through CMR1629; and
- this file from CMR1630 onward.

| IDs | Contents | Status | Location |
|---|---|---|---|
| CMR1630--1637 | Exact score-layer decomposition, superlevel matching-number bound, Konig cover certificate, direct return-selector criterion, integer threshold form, two-level heavy-edge envelope, geometric class specialization, and the superlevel endpoint | PROVED; random rational/integer score systems, exact covers and strict certificates checked | `docs/307-prime-power-return-assignment-superlevel-covers.md` |
| CMR1638--1645 | Monotonicity lemma, strong/overlap floors, singleton floor, universal integer budgets, rank-pure ranges, unavailable-edge reserve, rooted-trace specialization, and the universal-budget endpoint | PROVED; monotonicity and budget implications checked through side 500 | `docs/308-prime-power-line-clean-universal-budget-floors.md` |
| CMR1646--1653 | Total selector capacity, exact gap and restoration cap, critical-state exclusion, per-prescription capacity, mixed exact/residual capacities, return-assignment coupling, refined capacity threshold, and the capacity-gap endpoint | PROVED; random class systems, gap arithmetic, restoration caps and critical exclusions checked | `docs/309-prime-power-selector-capacity-gap-compiler.md` |
| CMR1654--1661 | Relabelling invariance, opposite-matching normalization, target normalization, residual stabilizer, canonical orbit code, orbit-invariant rows, certificate lifting, and the symmetry-normalized thin-table endpoint | PROVED; normalized hosts, canonical stabilizer actions and exact probability invariance checked | `docs/310-prime-power-fixed-interface-symmetry-normalization.md` |
| CMR1662--1669 | Raw/canonical host counts, exact response denominators, side-two failure, side-three forced contraction, side-four and side-five nonforced probability caps, capacity consequences, and the normalized thin-census endpoint | PROVED; 173 canonical hosts and 12,295 extendable rank-one/two prescriptions checked exhaustively | `docs/311-prime-power-normalized-thin-response-census.md` |
| CMR1670--1677 | Threshold class unions, class-supported assignment bound, source/target star covers, alternative-cover optimization, nested cover weights, direct rational dual, strict integer form, and the class-support endpoint | PROVED; random score systems, threshold unions, finite cover choices and strict duals checked | `docs/312-prime-power-return-class-support-covers.md` |
| CMR1678--1685 | Weighted rank/profile capacity envelope, exact and universal budget certificates, overflow localization, candidate-count conversion, unavailable-edge overflow, mixed exact/residual slack, and the profile-capacity endpoint | PROVED; random capacity systems, overflow witnesses and mixed slacks checked | `docs/313-prime-power-line-clean-profile-capacity-compiler.md` |
| CMR1686--1693 | Ambient rank-three stock, side-three forced rank-three rows, exact side-four/five rank-three censuses, complete probability table, expectation capacities, integer numerator capacities, and the rank-three endpoint | PROVED; all 15,469 canonical extendable rank-three instances checked exhaustively | `docs/314-prime-power-normalized-thin-rank-three-census.md` |
| CMR1694--1701 | Nonnegative auxiliary resolvent, effective core, constructive certificate lift, exact subcriticality equivalence, zero-self reduction, rational/integer certificates, block-diagonal elimination, and the auxiliary-block endpoint | PROVED; exact rational block systems, zero-self reductions and denominator clearings checked | `docs/315-prime-power-subcritical-auxiliary-block-elimination.md` |
| CMR1702--1709 | Exact prescription rank-mass identity, corrected-family bound, integer numerator conservation, forced-mass removal, pointwise/mass minimum, side-four/five capacities, integer capacity form, and the rank-mass endpoint | PROVED; rational response laws, rank identities, forced decompositions and combined capacities checked | `docs/316-prime-power-prescription-rank-mass-conservation.md` |

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Combined return-selector assignment

For selector cap `T`, use the shared edge score

\[
h_T=g_{\rm ret}+Tg_{\rm sel}.
\]

The block may be certified by one exact assignment dual, a superlevel matching-
number bound, or explicit class-supported source/target covers.  If class `s`
has score cap `H_s` and cover `C_s`, nested threshold unions give the dual
objective

\[
\sum_{z\in L\cup R}\max\{H_s:z\in C_s\}.
\]

An objective below one, or its denominator-cleared integer form, proves the
complete coupled block subcritical without adding incompatible return and
selector maxima.

### Line-clean capacities

The exact strong, singleton and overlap response ratios have universal floors

\[
\frac1{16},
\qquad
\frac{81}{4096},
\qquad
\frac1{256}.
\]

Rank/profile/geometric class capacities compile into

\[
\widehat W
=
\sum_\chi c_{r(\chi)}C_\chi
+(m+1)B(d-1)(d-2),
\]

where

\[
c_1=(d-1)(d-2),
\qquad c_2=d-2,
\qquad c_3=1.
\]

If `widehat W` fits the exact or universal budget, one positive integer slack
certifies the whole class family.  Failure forces one candidate or unavailable-
edge coordinate above an explicit integer threshold.

### Selector capacity gaps

If exact selector class numerators have common denominator `D` and capacities
`a_chi<=C_chi`, put `C=sum C_chi`.  When `C<D`, criticality is impossible and

\[
\eta=\frac{D-C}{D},
\qquad
T_C=
\left\lfloor
\frac{D[2(n-1)+B]}{(n-1)(D-C)}
\right\rfloor.
\]

The cap `T_C` feeds directly into the shared return assignment.  Critical
survivors must meet the exact capacity threshold retained by CMR1652.

### Symmetry-normalized thin tables

Every opposite matching and forbidden target is relabelled to

\[
(I_d,(0,1)).
\]

The residual stabilizer is `S_{d-2}`.  The exact census through side five is:

| side | canonical executable hosts | matching-level endpoint |
|---:|---:|---|
| 2 | 0 | no extension-free response |
| 3 | 4 | every positive rank-at-most-three prescription is forced |
| 4 | 45 | nonforced caps `3/4`, `2/3`, `1/2` in ranks one, two, three |
| 5 | 124 | caps `2/3`, `2/5`, `1/4`; no forced positive rank-at-most-three prescriptions |

For every response law and rank `r`, prescription probability mass is exactly

\[
\sum_{P:\operatorname{rank}P=r}\Pr(P\subseteq Q)=\binom dr.
\]

Thus a geometric class uses the minimum of its pointwise probability capacity
and the conserved rank-mass capacity.  Forced contractions subtract one full
unit each.

### Auxiliary-module elimination

If a certified auxiliary block `D` satisfies `rho(D)<1`, its exact excursion
resolvent is

\[
R_D=(I-D)^{-1}\ge0.
\]

For

\[
M=
\begin{pmatrix}A&B\\C&D\end{pmatrix},
\]

one has

\[
\rho(M)<1
\quad\Longleftrightarrow\quad
\rho\bigl(A+B(I-D)^{-1}C\bigr)<1.
\]

The reduction and certificate lift are rational and become a finite strict
integer certificate after denominator clearing.  The selector formula
`alpha+beta T<1` is the one-dimensional zero-self case.

## Active frontier

1. Prove host-uniform score caps and small source/target covers for the geometric
   classes of `h_T`, producing a shared return-selector dual below one.
2. Put inherited candidate and unavailable-edge capacities inside the exact or
   universal line-clean budgets; certify only the finitely many overflow classes.
3. Compile selector capacities using exact rook numerators, thin-table caps and
   conserved rank mass, eliminating every class with positive denominator slack.
4. Enumerate genuinely new geometric offspring on the 45 side-four and 124 side-
   five canonical hosts, certify the resulting orbit tables, and eliminate each
   certified auxiliary table by its exact resolvent.
5. Certify the remaining reused-support and fully labelled collision/local-line
   SCCs, publish one strict integer quotient certificate, and apply the proved
   CRT gluing protocol.
