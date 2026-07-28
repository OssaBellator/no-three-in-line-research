# Weighted constraint-load batching for oriented swap menus

**Branch:** `research/sparse-algebraic-spread`

SAS5hi--SAS5hm give a compatible oriented subbatch when every constraint atom occurs in at most `Lambda` candidates.  Cardinality incidence can be too crude when square weights are highly nonuniform.  This note replaces it by a weighted-load dichotomy: either one exact physical atom is already heavy, or a compatible batch survives with an explicit weighted local-minimum bound.

## Weighted candidate system

Retain `m>=1` base-legal oriented candidates for every operation square `Q`, each carrying square weight `w_Q>0`.  Candidates from one square are alternatives and are pairwise conflicting.  A candidate `v` carries a set `S(v)` of at most `r` physical constraint atoms.

For an atom `a`, define its candidate-weight load

\[
\Lambda_w(a)=\sum_{v:a\in S(v)}w_v,
\]

where `w_v=w_Q` for a candidate from square `Q`.

Fix a load threshold `tau>0`.

## SAS5hn -- exact weighted atom alternative -- PROVED

Either some exact physical constraint atom satisfies

\[
\boxed{\Lambda_w(a)>\tau,}
\]

or every atom has weighted load at most `tau`.

In the first case the atom, together with its physical type, column/endpoint/record address and incident oriented candidates, is a heavy exact legality obstruction.

### Proof

This is the exhaustive threshold split applied to the exact atom loads.  No candidate weight is discarded. QED.

## SAS5ho -- weighted conflict-neighbourhood bound -- PROVED

Assume every atom load is at most `tau`.  For a candidate `v` from square `Q`, the total weight of its conflict neighbours is at most

\[
\boxed{(m-1)w_Q+r\tau.}
\]

### Proof

The other `m-1` alternatives of square `Q` contribute exactly `(m-1)w_Q`.  Every remaining conflict shares at least one atom of `S(v)`.  Summing the total incident weight over at most `r` atoms contributes at most `r tau`; overlaps only overcount. QED.

## SAS5hp -- weighted local-minimum independent set -- PROVED

For any finite weighted graph with positive vertex weights `w_v`, there is an independent set of weight at least

\[
\boxed{
\sum_v
\frac{w_v^2}{w_v+\sum_{u\sim v}w_u}.
}
\]

### Proof

Give vertex `v` an independent exponential clock of rate `w_v` and select it when its clock is the unique minimum in its closed neighbourhood.  Adjacent vertices cannot both be selected, so the selected set is independent.  The probability that `v` is selected is

\[
\frac{w_v}{w_v+\sum_{u\sim v}w_u}.
\]

Multiply by `w_v`, sum expectations and choose one outcome attaining at least the expectation. QED.

## SAS5hq -- compatible batch under weighted atom caps -- PROVED

If every atom has weighted load at most `tau`, there is a compatible oriented subbatch of total square weight at least

\[
\boxed{
\sum_Q
\frac{m w_Q^2}{m w_Q+r\tau}.
}
\]

If additionally every square weight satisfies `w_Q>=w_0>0`, then the retained weight is at least

\[
\boxed{
\frac{m w_0}{m w_0+r\tau}W,
\qquad W=\sum_Qw_Q.
}
\]

### Proof

Apply SAS5hp to the candidate conflict graph.  By SAS5ho, a candidate from `Q` has closed-neighbourhood weight at most `m w_Q+r tau`, so each of its `m` alternatives contributes at least `w_Q^2/(m w_Q+r tau)` to the local-minimum sum.  Summing over squares gives the first display.  For the second,

\[
\frac{m w_Q^2}{m w_Q+r\tau}
=w_Q\frac{m w_Q}{m w_Q+r\tau}
\ge
w_Q\frac{m w_0}{m w_0+r\tau}.
\]

QED.

## SAS5hr -- weighted legality-load router -- PROVED UNDER THE ADDITIVE-EXECUTION CONTRACT

For every localized oriented square family and threshold `tau`, one of the following occurs:

1. missing legal orientations localize to the exact base/cross failure classes of SAS5hl;
2. one exact constraint atom has weighted load greater than `tau` by SAS5hn;
3. all atom loads are at most `tau`, and SAS5hq gives a compatible oriented subbatch with the displayed retained weight;
4. the selected batch gives the existing descent, current-only payment, neutral-repair, barrier or recycled-word output;
5. or a physical atom, square weight, operation word, base state, boundary or legality interpretation changes, giving an explicit reset.

Thus unknown cardinality incidence `Lambda` is no longer the only route.  A word family may instead prove weighted atom caps, while failure produces a heavy exact physical column, endpoint, record, constraint or boundary atom.

### Proof

First apply the missing-menu inventory.  On the remaining legal candidates use the threshold split SAS5hn.  The light-load branch uses SAS5ho--SAS5hq and the existing additive execution ledger.  Contract changes are returned rather than silently identified. QED.

## Updated SAS frontier

For each arithmetic word family it is now enough to establish either:

- a cardinality incidence bound `Lambda` for SAS5hk; or
- a weighted atom-load cap `tau` for SAS5hq.

Failure of the second route is itself a quantified exact obstruction.  Remaining SAS6 work is payment of those heavy atoms, global barrier and neutral outputs, boundary profiles and exact balanced compression.

## Finite check

`scripts/verify_sas_weighted_constraint_load.py` enumerates small oriented candidate systems, computes exact atom loads and maximum-weight independent sets, and verifies the weighted local-minimum guarantee.