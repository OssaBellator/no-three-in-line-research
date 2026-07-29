# Fifth frontier import for AC5 physical execution

**Branch:** `research/alternating-core-chain`

AC5bf--AC5bl import source-hole multiplicity, disjoint physical RI banks, complete off-diagonal BDA incidence geometry, canonical sparse prefixes, phase-orbit cycle sums and polynomial protected capacities. This note imports the next extraction and payment reductions.

## AC5bm -- RI conflict-graph subbank import -- PROVED

Let the closed RI components form a conflict graph whose edges record physical-region overlap, cross-region constraints or incompatible exterior records. Every independent set satisfying the local replacement hypotheses is a physical I6 subbank.

If the graph has maximum degree `Delta`, a subbank exists on at least

\[
\boxed{\left\lceil\frac m{\Delta+1}\right\rceil}
\]

components. With component paid weights `w_a`, one independent family has weight at least

\[
\boxed{\sum_a\frac{w_a}{d(a)+1}}
\ge
\boxed{\frac{\sum_aw_a}{\Delta+1}}.
\]

Failure returns one high-conflict component/neighbourhood or one local readiness defect.

### Proof

Use greedy independent-set extraction for cardinality and the random-order closed-neighbourhood argument for weighted extraction, then apply AC5bg on the independent family. QED.

## AC5bn -- exceptional endpoint trimming import -- PROVED

For a low-event endpoint set `S`, let `M_S` be total source-hole incidence and let

\[
T_\tau=\{b\in S:\nu(b)>\tau\}.
\]

Then

\[
\boxed{|T_\tau|\le\left\lfloor\frac{M_S}{\tau+1}\right\rfloor.}
\]

After deleting `T_tau`, every retained endpoint has multiplicity at most `tau`, so AC5bf gives a computable retained-set Hall-deficiency bound. The AC menu may optimize over `tau`, paying the exceptional endpoints separately or returning one concentrated hole-star witness.

### Proof

Every exceptional endpoint contributes at least `tau+1` incidences. Apply AC5bf to the retained set. QED.

## AC5bo -- complete weighted BDA overlap import -- PROVED

If two declared context lines meet in at most one cell, they cannot share a context-pair address. Consequently every nonresonant mixed `CD`/`AB` template has zero role-side pair overlap.

The only mixed templates capable of overlap are resonant `CD-A`, resonant `CD-B`, radial `AB-A` and radial `AB-B`. In each such case the families split exactly into line-supported common weight `O` and two address-disjoint residuals of weights `W_u-O,W_v-O`.

Together with AC5bb, every off-diagonal BDA comparison now yields a collision, connector/resonant/radial line family, or two address-disjoint role families. Remaining work is payment and owner realization, not overlap geometry.

### Proof

A common pair supplies two common line points. BDA5bu--BDA5bw classify precisely when this is possible; pointwise minimum weights give the exact overlap decomposition. QED.

## AC5bp -- state-local sparse guard import -- PROVED

Let a sparse final permutation move `r` rows, and let the nonstructural contract contain `K` state-local predicates. The canonical implementation requires at most

\[
\boxed{Kr}
\]

guard evaluations, in addition to the earlier `2r(r-1)` structural tests.

Any signed transition charge of the form

\[
c(M,M')=\Psi(M')-\Psi(M)
\]

is preserved exactly by canonical replacement. For an arbitrary antisymmetric charge, the difference between the original and canonical word is the circulation on their closed comparison walk. Failure is one state-local guard, nonzero cycle defect, antisymmetry defect or explicitly history-dependent field.

### Proof

Evaluate the finite guard dictionary on the at most `r` canonical states. Potential differences telescope; antisymmetry identifies path-sum difference with closed-walk circulation. QED.

## AC5bq -- zero-vector decoration recurrence import -- PROVED UNDER THE FINITE-PROFILE CONTRACT

Fix a zero quotient-invariant profile with a deterministic physical-decoration map on a dictionary of size `K`. Every history reaches its first repeated decoration within `K` transitions and consumes at most `K-1` first-visit tickets.

On the eventual decoration cycle, any score decomposition

\[
G_j=P_j-D_j+\Psi(d_j)-\Psi(d_{j+1})
\]

has cyclic sum `sum P_j-sum D_j`. The return therefore yields a paying traversal, concentrated classified debt, one exactly balanced decoration-cycle ticket, or one finite-profile/score defect.

### Proof

Use the pigeonhole principle on the deterministic decoration orbit and telescope the decoration potential around its eventual cycle. QED.

## AC5br -- affine protected-line polynomial import -- PROVED

For three cells moving affinely in one operation parameter,

\[
X_i(t)=x_i+t u_i,
\]

collinearity is a polynomial equation

\[
\boxed{c_0+c_1t+c_2t^2=0.}
\]

If the coefficient triple is nonzero and at most `M_p` physical operations share one parameter, the protected address has incidence at most

\[
\boxed{2M_p}
\]

and capacity at most the sum of its `2M_p` largest eligible weights. Failure is the exact coefficient-degeneracy profile, excessive fibre multiplicity, or a failed affine/eligibility record.

### Proof

Expand the determinant of the two affine difference vectors. A nonzero quadratic has at most two roots; apply AC5bk. QED.

## AC5bs -- strengthened execution continuation -- PROVED UNDER THE DECLARED CONTRACTS

An AC menu now has one exact continuation:

1. a weighted physical RI subbank extracted from the conflict graph, or one high-conflict/readiness witness;
2. low-event flow after deleting at most `M_S/(tau+1)` high-multiplicity endpoints, or one hole-star/mass witness;
3. a collision, paid-line candidate or two address-disjoint families for every off-diagonal BDA comparison;
4. an `O(r^2+Kr)` sparse structural/state-local audit, preserved endpoint potential, or one exact cycle/lineage defect;
5. a finite zero- or nonzero-vector physical recurrence with payment, classified debt or balanced-cycle ticket;
6. a degree-two protected-line capacity, or one coefficient/fibre obstruction;
7. or one existing AC4/AC5 payment, descent, Hall-core, reset or failed physical contract.

This does not yet bound the actual RI conflict graph, pay every BDA line family, prove total low-cost hole mass, identify every sparse guard potential, construct every physical decoration dictionary, or affine-parameterize every protected event. It replaces those gaps by explicit finite graphs, stars, lines, cycles and coefficient profiles.

## Finite check

`scripts/verify_ac_fifth_frontier_import.py` checks the conflict-graph bounds, exceptional endpoint count, line-pair disjointness, canonical path/cycle identity, finite decoration recurrence and quadratic collinearity formula on finite abstractions.