# Odd-path surplus Hall criterion

This chapter sharpens the degree-two centre-conflict formula in `docs/676` by
compressing the complete second-stage graph into one structural statistic.

Let `H` be the bipartite centre-conflict graph after selecting `q`
resource-disjoint motifs. The three-good-centres law gives

```text
|V(H)| = 3q.
```

Assume every vertex of `H` has degree at most two.

## PP3dde — Exact odd-path surplus formula

Every connected component of `H` is an isolated vertex, a path, or an even cycle.
Let `o(H)` be the number of odd-order path components, counting isolated vertices
as one-vertex paths.

Then

```text
alpha(H) = (|V(H)| + o(H))/2.
```

Indeed, a path on `s` vertices contributes `ceil(s/2)`, while an even cycle on
`s` vertices contributes `s/2`. Summing the component formulas gives the identity.

Equivalently, every odd path contributes one unit of surplus over the baseline
`|V(H)|/2`; even paths and even cycles contribute no surplus.

## PP3ddf — Sharp two-stage Hall threshold

Substituting `|V(H)|=3q`, at least 28 centres remain exactly when

```text
3q + o(H) >= 56.
```

Thus the exact required odd-path counts are

```text
q=10: o(H)>=26,
q=11: o(H)>=23,
q=12: o(H)>=20,
q=13: o(H)>=17,
q=14: o(H)>=14,
q=15: o(H)>=11,
q=16: o(H)>=8,
q=17: o(H)>=5,
q=18: o(H)>=2,
q>=19: no odd-path surplus is required.
```

This is equivalent to the matching-loss budgets in `docs/676`, but it exposes the
precise component structure a coordinate host must produce.

## PP3ddg — Structural promotion interface

A host-level Hall proof may now be split into three exact certificates:

1. the first-stage resource lists and component packing give `q` selected motifs;
2. the complete selected-centre conflict graph is bipartite with maximum degree
   two;
3. its number of odd path components satisfies `o(H)>=56-3q`.

No maximum-matching computation is then needed: the retained count follows from
component parity alone. Even cycles are especially costly because they consume
centres without contributing odd-path surplus.

## Verification

`scripts/check_hall_odd_path_surplus.py` exhausts all 10,172 bipartite
maximum-degree-two graphs whose two sides have size at most four. For each graph it
computes the exact independence number and verifies

```text
2*alpha(H)=|V(H)|+o(H).
```

It also checks the sharp Hall-scale thresholds above on explicit path-component
multisets.

## Evidence boundary

This remains a conditional promotion interface. No asymptotic coordinate host has
yet supplied the selected motif family, the complete centre-conflict graph, and
the required odd-path surplus while simultaneously satisfying the source- and
host-defect restrictions.
