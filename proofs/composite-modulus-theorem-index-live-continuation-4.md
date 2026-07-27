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

The branch still does not prove the all-`n` conjecture.

## Current exact certificate surfaces

### Combined return-selector assignment

For selector cap `T`, use the shared edge score

\[
h_T=g_{\rm ret}+Tg_{\rm sel}.
\]

The block may be certified by one exact assignment dual or by the finite
superlevel bound

\[
\max_Q\sum_{a\in Q}h_T(a)
\le
\sum_j(\tau_j-\tau_{j-1})\nu(E_j).
\]

By Konig's theorem, every matching number may be replaced by the size of one
explicit source/target vertex cover.  After denominator clearing, a cover sum
strictly below the common denominator proves the complete coupled block
subcritical.

### Universal line-clean budgets

The exact strong, singleton and overlap response ratios are strictly increasing
for `d>=4`.  Their universal floors are

\[
\frac1{16},
\qquad
\frac{81}{4096},
\qquad
\frac1{256}.
\]

Thus, with destroyed load `D` and weighted candidate count `W_d`, the automatic
universal budgets are

\[
W_d\le\left\lceil\frac{D(d)_3}{16}\right\rceil-1,
\]

\[
W_d\le\left\lceil\frac{81D(d)_3}{4096}\right\rceil-1,
\]

and

\[
W_d\le\left\lceil\frac{D(d)_3}{256}\right\rceil-1.
\]

Rooted traces require only the strong and singleton budgets.

### Selector capacity gap

If exact selector class numerators have common denominator `D` and proved
capacities `a_chi<=C_chi`, put `C=sum C_chi`.  When `C<D`, criticality is
impossible and the selector has exact return-splice gap

\[
\eta=\frac{D-C}{D}
\]

with restoration cap

\[
T_C
=
\left\lfloor
\frac{D[2(n-1)+B]}{(n-1)(D-C)}
\right\rfloor.
\]

This cap feeds directly into the shared return assignment.

### Symmetry-normalized thin tables

Every opposite matching and forbidden target is relabelled to

\[
(I_d,(0,1)).
\]

The remaining stabilizer is `S_{d-2}`.  One exact rook row need be computed per
canonical stabilizer orbit, provided all owner, collision, local-line and CRT
labels are relabelled equivariantly and retained.

The exact census through side five is:

| side | canonical executable hosts | matching-level endpoint |
|---:|---:|---|
| 2 | 0 | no extension-free response |
| 3 | 4 | every response unique; all extendable rank-at-most-two prescriptions forced |
| 4 | 45 | nonforced probability caps `3/4` in rank one and `2/3` in rank two |
| 5 | 124 | probability caps `2/3` in rank one and `2/5` in rank two; no forced prescriptions |

## Active frontier

1. Bound the superlevel graphs of `h_T` by owner, line-height, token, prefix,
   carry and interface classes and produce a cover sum below one.
2. Put inherited candidate and unavailable-edge counts inside the universal or
   exact line-clean integer budgets.
3. Compile exact critical-selector class capacities and eliminate every class
   with positive denominator slack; certify the survivors individually.
4. Enumerate genuinely new geometric offspring on the 45 side-four and 124
   side-five canonical hosts, then extend the normalized table only to larger
   thin sides still required by structural reductions.
5. Certify the remaining reused-support and fully labelled collision/local-line
   SCCs, publish one strict integer quotient certificate, and apply the proved
   CRT gluing protocol.
