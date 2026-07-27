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
| CMR1710--1717 | Multiplicity-weighted line-clean expectation, rank-mass bound, forced subtraction, pointwise/count/mass minimum, large-load closure, integer numerator certificate, rooted-trace specialization, and the multiplicity-aware endpoint | PROVED; 720 rational laws, 2,040 rank identities, multiplicity bounds and strict large-load checks | `docs/317-prime-power-line-clean-rank-mass-large-load-closure.md` |
| CMR1718--1725 | Response-wise owned-submatching bound, owner-support expectation capacity, row/column cover form, fixed-owner conditional mass, weighted capacity, return-selector edge-score specialization, integer numerator form, and the owner-support endpoint | PROVED; 600 rational systems, 16,332 response-wise checks, 1,700 support capacities and 9,834 conditional-owner checks | `docs/318-prime-power-owner-support-rank-mass-capacities.md` |
| CMR1726--1733 | Support-local expectation, strict large-load closure, vertex-cover threshold, fixed finite-support threshold, prime-field reused-support specialization, weighted version, integer slack and multiplicity overflow, and the small-support endpoint | PROVED; 660 rational systems, 1,870 rankwise capacities, 660 strict closures and 601 overflow localizations | `docs/319-prime-power-owner-support-large-load-closure.md` |
| CMR1734--1741 | Rank-three injectivity, exact rank-two line-load formula, exact rank-one secant formula, line-load/secant bounds, primitive-direction form, explicit line-clean mass, owner-support specialization, and the geometric multiplicity endpoint | PROVED; 1,200 point systems, 16,649 collinear triples and exact rank-one/two/three multiplicity checks | `docs/320-prime-power-geometric-prescription-multiplicity-formulas.md` |
| CMR1742--1749 | Convex packing lemma, rank-one packed bound, linear relaxation, combined rankwise caps, explicit line-clean threshold, owner-support threshold, integer slack alternatives, and the packed-secant endpoint | PROVED; 100,000 exact packing systems and 1,200 finite-grid line-height systems checked | `docs/321-prime-power-packed-secant-multiplicity-bounds.md` |

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Combined return-selector assignment

For selector cap `T`, use the shared edge score

\[
h_T=g_{\rm ret}+Tg_{\rm sel}.
\]

The block may be certified by one exact assignment dual, a superlevel matching-
number bound, or explicit class-supported source/target covers. If class `s`
has score cap `H_s` and cover `C_s`, nested threshold unions give the dual
objective

\[
\sum_{z\in L\cup R}\max\{H_s:z\in C_s\}.
\]

An objective below one, or its denominator-cleared integer form, proves the
complete coupled block subcritical without adding incompatible return and
selector maxima.

### Line-clean capacities and geometric multiplicity

The exact strong, singleton and overlap response ratios have universal floors

\[
1/16,
\qquad
81/4096,
\qquad
1/256.
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
certifies the whole class family. Failure forces one candidate or unavailable-
edge coordinate above an explicit integer threshold.

For a background point set `B`, geometric prescription multiplicities are now
exact:

1. rank three has multiplicity one;
2. rank two multiplicity is `|B cap ell(x,y)|`;
3. rank one multiplicity is
   \[
   \sum_{\ell\ni x}C(|B\cap\ell|,2).
   \]

If `|B|=qH+r` with `0<=r<H` and every relevant background line has load at most
`H`, the exact packed rank-one cap is

\[
\Phi(|B|,H)=qC(H,2)+C(r,2).
\]

Thus one may take

\[
m_1\le\Phi(|B|,H_1),
\qquad
m_2\le H_2,
\qquad
m_3=1.
\]

The resulting explicit line-clean mass bound is

\[
\Phi(|B|,H_1)C(d,1)+H_2C(d,2)+C(d,3),
\]

with `C(d,r)-F_r` replacing the rank masses after forced contractions. A nonempty
line-clean host is a strict improvement whenever destroyed load exceeds the
applicable multiplicity-corrected mass.

### Selector capacity gaps

If exact selector class numerators have common denominator `D` and capacities
`a_chi<=C_chi`, put `C=sum C_chi`. When `C<D`, criticality is impossible and

\[
\eta=(D-C)/D,
\qquad
T_C=
\left\lfloor
\frac{D[2(n-1)+B]}{(n-1)(D-C)}
\right\rfloor.
\]

The cap `T_C` feeds directly into the shared return assignment. Critical
survivors must meet the exact capacity threshold retained by CMR1652.

### Owner-support capacities and small-support closure

Let `A` be an exact possible-owner edge set and let `mu(A)` be its matching
number. Distinct rank-`r` prescriptions owned in `A` have total probability mass
at most

\[
\mu(A)C(d-1,r-1).
\]

A source/target vertex cover of size `k` may replace `mu(A)` by `k`. With the
geometric multiplicity caps above, expected new owned collateral is at most

\[
\mu(A)
\left[
\Phi(|B|,H_1)+H_2(d-1)+C(d-1,2)
\right].
\]

Destruction above this quantity gives a strict response. Prime-field reused-
support states have support size one or two, subject to the condition that every
retained child owner lies in that support. Failure localizes a large owner
support, line height, secant packing value, or insufficient destroyed load.

### Symmetry-normalized thin tables

Every opposite matching and forbidden target is relabelled to

\[
(I_d,(0,1)).
\]

The residual stabilizer is `S_{d-2}`. The exact census through side five is:

| side | canonical executable hosts | matching-level endpoint |
|---:|---:|---|
| 2 | 0 | no extension-free response |
| 3 | 4 | every positive rank-at-most-three prescription is forced |
| 4 | 45 | nonforced caps `3/4`, `2/3`, `1/2` in ranks one, two, three |
| 5 | 124 | caps `2/3`, `2/5`, `1/4`; no forced positive rank-at-most-three prescriptions |

For every response law and rank `r`, distinct prescription probability mass is
exactly `C(d,r)`. Candidate multiplicity is now supplied by the line-load and
secant formulas rather than treated as an unnamed correction.

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
integer certificate after denominator clearing. The selector formula
`alpha+beta T<1` is the one-dimensional zero-self case.

## Active frontier

1. Prove host-uniform background line-height caps `H_1,H_2` for the exact owner,
   height, token, prefix, carry and interface classes.
2. Insert the packed secant caps into line-clean exact/universal budgets and
   certify the remaining low-load or high-height overflow classes.
3. Use the same geometric multiplicities and owner supports to bound the class
   scores of `h_T` and produce a shared return-selector dual below one.
4. Compile selector capacities using exact rook numerators, thin-table caps,
   distinct rank mass and the new line-load multiplicity formulas.
5. Enumerate genuinely new geometric offspring on the 45 side-four and 124 side-
   five canonical hosts, retaining line loads, multiplicities and absolute owners;
   certify and eliminate the resulting orbit tables.
6. Apply the packed small-support closure to reused-support states, then certify
   the surviving high-height or out-of-support rows and fully labelled collision/
   local-line SCCs.
7. Publish one strict integer quotient certificate and apply the proved CRT
   gluing protocol.
