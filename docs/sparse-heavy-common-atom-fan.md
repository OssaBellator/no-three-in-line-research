# Heavy common-atom fan and residual compatibility

**Branch:** `research/sparse-algebraic-spread`

SAS5hn--SAS5hr return one exact physical constraint atom whose oriented-candidate weight is heavy, or a globally compatible batch. This note analyzes the heavy-atom branch. Candidates sharing one atom form a common-atom fan. Under a union-safe execution contract the common atom is counted once; only the residual atoms create pairwise incompatibility. The residual system either exposes a second heavy atom or admits a quantified compatible subbatch.

The shared-atom execution contract is essential. If the common atom is capacity one and cannot be shared, the output is an exact capacity overload rather than a compatible batch.

## Common-atom candidate fan

Fix one exact physical atom `a` and let `Q_a` be the weighted family of operation squares having at least one base-legal oriented candidate containing `a`. Square `Q` has weight `w_Q` and exactly `m_Q>=1` retained candidates in the fan.

For a retained candidate `u`, write

\[
 S^\circ(u)=S(u)\setminus\{a\}
\]

for its residual constraint atoms. Assume

\[
 |S^\circ(u)|\le r_\circ.
\]

For each residual atom `b`, define its weighted candidate load

\[
 L_b=\sum_{u:b\in S^\circ(u)}w_{Q(u)}.
\]

Candidates of the same square are alternatives and therefore conflict. Candidates of different squares conflict when their residual atom sets intersect.

## SAS5hs -- exact common-atom union ledger -- PROVED UNDER THE SHARED-ATOM CONTRACT

Suppose the physical operation represented by `a` may be installed or paid once for the whole selected fan, and every other interaction is represented in `S^circ(u)`. Then any independent set in the residual conflict graph gives a jointly executable family in which:

1. the common atom `a` is counted exactly once;
2. at most one orientation is selected from each square;
3. all noncommon constraint atoms are disjoint;
4. the existing two-stage energy and collateral ledgers add over the selected squares after the one common-atom debit.

### Proof

Same-square adjacency enforces one orientation per square. Residual independence makes all noncommon atoms disjoint. The shared-atom contract permits the single common occurrence to serve the entire selected fan, so it is debited once rather than once per candidate. The existing additive ledger then applies to the disjoint residual supports. QED.

## SAS5ht -- second-heavy-atom alternative -- PROVED

For any threshold `tau>=0`, either some residual atom satisfies

\[
 \boxed{L_b>\tau,}
\]

in which case `(a,b)` is an exact two-atom heavy obstruction, or every residual atom has load at most `tau`.

The first alternative retains the physical square, orientation, operation stage, record, column, endpoint, label and boundary fields of both atoms.

### Proof

This is the exhaustive dichotomy obtained by taking the maximum residual atom load. QED.

## SAS5hu -- weighted residual conflict bound -- PROVED

Assume every residual atom has load at most `tau`. For a candidate `u` from square `Q`, the total weight of its open conflict neighbourhood is at most

\[
 \boxed{
 (m_Q-1)w_Q+r_\circ\tau.
 }
\]

### Proof

The other `m_Q-1` alternatives of the same square contribute `(m_Q-1)w_Q`. Each of the at most `r_circ` residual atoms belongs to candidates of total weight at most `tau`. Union counting can overcount candidates sharing several residual atoms, so it is a valid upper bound. QED.

## SAS5hv -- compatible common-atom subfan -- PROVED

Under the light residual-load alternative, there is an independent set of candidates of total square weight at least

\[
 \boxed{
 \sum_{Q\in\mathcal Q_a}
 \frac{m_Qw_Q^2}{m_Qw_Q+r_\circ\tau}.
 }
\]

Under the shared-atom contract this is a jointly executable common-atom fan with `a` paid once.

### Proof

Apply the weighted local-minimum independent-set inequality

\[
 \alpha_w(H)\ge
 \sum_{u\in V(H)}
 \frac{w_u^2}{w_u+w(N(u))}.
\]

SAS5hu bounds the denominator for a candidate of square `Q` by `m_Qw_Q+r_circ tau`. Summing the identical contribution over the `m_Q` retained candidates of `Q` gives the displayed term. SAS5hs converts the independent set to a union-safe physical execution. QED.

## SAS5hw -- heavy legality-atom router -- PROVED UNDER THE COMMON-ATOM EXECUTION CONTRACT

Every heavy exact atom returned by SAS5hn has one continuation:

1. the common atom is not shareable, giving an exact capacity overload at `a`;
2. one residual atom is heavy, giving the exact two-atom obstruction `(a,b)` from SAS5ht;
3. all residual loads are light and SAS5hv supplies a quantified compatible common-atom fan with `a` counted once;
4. the selected fan enters the existing descent, current-only payment, neutral-repair, barrier or recycled-word ledgers;
5. or a square, orientation, owner, lineage, context, boundary or legality field changes, giving an explicit reset.

Thus the heavy-atom branch is reduced to a one-time common debit, a heavier two-atom concentration, or an executable residual-independent fan. It is no longer an unstructured high-incidence output.

## Updated SAS frontier

The remaining SAS6 legality work is now concentrated on:

- paying or excluding exact one-atom capacity overloads and two-atom heavy obstructions;
- verifying the common-atom execution contract for each localized arithmetic word family;
- closing aggregate barrier and neutral outputs;
- boundary profiles and exact balanced standard-grid compression.

## Finite check

`scripts/verify_sas_heavy_common_atom_fan.py` generates finite common-atom candidate systems, checks the heavy-second-atom alternative, constructs the residual conflict graph, computes exact maximum-weight independent sets on small instances and verifies the displayed weighted lower bound.