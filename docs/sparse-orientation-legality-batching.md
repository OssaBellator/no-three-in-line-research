# Mixed-orientation creator/destroyer legality batching

**Branch:** `research/sparse-algebraic-spread`

SAS5gb--SAS5gt install negative collateral, execute opposite destroyers and reverse composed-only outputs. The remaining physical gap is simultaneous legality: one operation square may have several creator/opposite-destroyer orientations, and a locally valid square family need not be jointly executable because candidate words can share columns, constraints or boundary atoms.

This note treats orientations as alternatives rather than multiplying them. A finite legality inventory is followed by a bounded-degree compatible-subbatch theorem. Failure retains the exact base-state single-swap or cross-legality witness.

## Oriented square candidates

Let `Q` be a weighted family of operation squares with weights `w_Q>=0` and total weight

\[
W=\sum_Q w_Q.
\]

For each square `Q`, let `M_Q` be its finite menu of oriented creator/opposite-destroyer realizations. A candidate is **base legal** when:

1. the creator single swap is legal in the original base state;
2. the opposite-destroyer single swap is legal in the original base state;
3. the declared creator-first two-stage word is legal at every intermediate state;
4. its exact current, negative, neutral and barrier ledgers are the branch ledgers already assigned to that square.

Every rejected orientation receives its least failure reason from a fixed finite dictionary:

- creator-base illegality;
- destroyer-base illegality;
- creator/destroyer cross interaction;
- column or endpoint collision;
- constraint or label conflict;
- boundary, context or omitted-legality reset.

A base-legal candidate carries a set `S(m)` of physical **constraint atoms**: used columns, endpoints, exact records, labels, boundary resources and any other atom whose sharing would invalidate additive execution.

## SAS5hi -- exact orientation-legality inventory -- PROVED

Every oriented square candidate is either base legal or has one canonical least failure reason from the displayed dictionary together with the exact square, orientation, operation stage and physical witness atom.

Consequently no failed orientation is discarded merely as “incompatible”: its base single-swap or cross-stage obstruction remains an exact weighted output.

### Proof

Test the legality conditions in the declared order and return the first failed condition with its exact physical witness. If all tests pass, the candidate is base legal by definition. The order makes the address canonical. QED.

## Compatible candidate graph

Assume every square has at least `m>=1` base-legal candidates. Retain the first `m` in the canonical orientation order. Form a conflict graph `H` on the retained candidates:

- all candidates from the same square are pairwise adjacent;
- candidates from different squares are adjacent when their constraint-atom sets intersect.

Give every candidate from square `Q` weight `w_Q`. An independent set selects at most one orientation per square and is jointly constraint compatible.

Assume:

\[
|S(m)|\le r
\]

for every retained candidate, and every physical constraint atom belongs to at most `Lambda` retained candidates globally.

## SAS5hj -- bounded candidate conflict degree -- PROVED

The maximum degree of `H` is at most

\[
\boxed{
\Gamma=(m-1)+r(\Lambda-1).
}
\]

### Proof

A candidate conflicts with the other `m-1` alternatives of its own square. Each of its at most `r` atoms belongs to at most `Lambda-1` other retained candidates. Union counting gives the bound; overlaps only reduce the true degree. QED.

## SAS5hk -- quantified compatible oriented subbatch -- PROVED

There is an independent set of retained candidates whose total square weight is at least

\[
\boxed{
\frac{m}{m+r(\Lambda-1)}W.
}
\]

The selected candidates use distinct squares and form a simultaneously constraint-compatible creator/opposite-destroyer subbatch.

### Proof

A graph of maximum degree `Gamma` is `(Gamma+1)`-colourable. The total weight of all retained candidate vertices is exactly `mW`, because each square contributes `m` alternatives of weight `w_Q`. One colour class has weight at least `mW/(Gamma+1)`. It is independent, and substituting SAS5hj's value of `Gamma+1` gives the bound. Same-square adjacency ensures at most one selected orientation per square. QED.

This theorem treats orientations as a menu. It does not charge the weight of all `m` alternatives as simultaneously realized output.

## Missing-orientation mass

If some squares have fewer than `m` base-legal candidates, define their weighted missing incidence

\[
U=\sum_Q w_Q\,(m-|M_Q^{\rm legal}|)_+.
\]

Let the failure dictionary have `L_fail` exact reason classes after fixing the finite word and physical role alphabets.

## SAS5hl -- failed legality concentrates on one exact obstruction -- PROVED

One exact failure-reason class carries missing incidence weight at least

\[
\boxed{
U/L_{\rm fail}.
}
\]

It is one of the base creator, base destroyer, cross-interaction, collision, constraint/label or boundary/context outputs of SAS5hi.

### Proof

Assign every missing canonical orientation slot its least failure reason. These classes partition the total missing incidence `U`. Weighted pigeonhole gives the claim. QED.

## SAS5hm -- mixed-orientation legality router -- PROVED UNDER THE ADDITIVE-EXECUTION CONTRACT

For every weighted family of localized operation squares and a declared target menu size `m`, one of the following occurs:

1. every square has `m` base-legal orientations and SAS5hk supplies a compatible subbatch of weight at least `mW/[m+r(Lambda-1)]`;
2. a positive creator/destroyer execution margin on that subbatch gives the existing aggregate descent/payment route;
3. the selected subbatch returns the existing current-only, neutral-repair, barrier or recycled-word outputs with no additional orientation loss;
4. or missing orientation mass localizes by SAS5hl to one exact base-swap, cross-stage, collision, constraint/label or boundary/context obstruction.

Thus mixed-orientation legality is reduced to finite local tests plus one explicit conflict-incidence parameter `Lambda`. Base-state single-swap admissibility is not assumed implicitly.

### Proof

Use SAS5hi to classify every orientation. If all menus have size at least `m`, apply SAS5hj--SAS5hk and then the existing additive two-stage energy ledgers to the independent set. Otherwise apply SAS5hl. QED.

## Updated SAS frontier

The creator/opposite-destroyer legality problem now has an exact menu interface. Remaining SAS6 work is to:

- bound `r` and `Lambda` uniformly for each localized arithmetic word family;
- pay the returned heavy base/cross/constraint obstruction;
- close global aggregate barriers and neutral high-incidence fibres;
- resolve boundary profiles and exact balanced standard-grid compression.

## Finite check

`scripts/verify_sas_orientation_legality_batching.py` enumerates finite square menus and constraint-atom systems, checks the conflict-degree bound, computes maximum-weight independent sets on small instances and verifies the guaranteed retained weight and failure-reason pigeonhole bound.
