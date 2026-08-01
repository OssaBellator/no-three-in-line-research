# Convex support-chord embedding mismatch

`docs/588` equips every unary-to-unary ancestry edge with the size of its child subtree, interpreted as a canonical support-interval span. This chapter embeds those intervals into explicit coordinates and tests whether the span statistic is already a collinearity-risk statistic.

## 1. Canonical coordinate embedding

### Theorem PP3cta -- PROVED / LAMINAR PREORDER INTERVAL EMBEDDING

Number the encoded nodes in preorder by `0,1,...,n-1`. Every rooted subtree occupies one contiguous interval. The family of subtree intervals is laminar: any two are disjoint or one contains the other.

Map node `k` to the convex-lattice point

```text
p_k=(k,k^2).
```

Represent every ancestry support interval by the chord joining its endpoint points.

#### Proof

Preorder visits all nodes of a subtree consecutively, giving contiguity. Two rooted subtrees are either disjoint or related by ancestry, giving laminarity. ∎

## 2. Positive span with zero collinearity

### Theorem PP3ctb -- PROVED / INTERVAL SPAN IS NOT COLLINEARITY COUNT

At the thirty-leaf, nine-binary profile, the exact aggregate ancestry-edge count and interval span remain

```text
638045608200,
4963626417750.
```

Nevertheless, the convex embedding of `PP3cta` has no collinear triple of distinct support points, for any encoded tree and any size.

#### Proof

Three distinct points `(i,i^2),(j,j^2),(k,k^2)` have nonzero Vandermonde determinant proportional to

```text
(j-i)(k-i)(k-j).
```

Hence no three are collinear. The aggregate values follow from the exact dynamic program of `docs/588`. ∎

## 3. Decoder consequence

### Theorem PP3ctc -- PROVED / ADDITIONAL INCIDENCE DATA IS NECESSARY

Canonical interval span cannot be used directly as a geometric collinearity-risk coordinate. A coordinate-level support-chord decoder must introduce additional incidence structure beyond convex node positions and laminar ancestry intervals.

#### Proof

`PP3ctb` exhibits a coordinate realization with the full positive span aggregate but identically zero support-point collinearity. Therefore span alone does not determine the desired geometric conflict count. ∎

## 4. Exact audit

Run

```bash
python scripts/check_prefix_convex_chord_embedding.py
```

The checker reconstructs the full profile aggregates and audits all `539` encoded trees through size nine, including `553` unary-to-unary edges, for interval laminarity and convex noncollinearity. The general statements are proved above and do not depend on that finite cutoff.

## 5. Prime-patching consequence

The ancestry-aware dynamic program is a valid combinatorial interface, but the simplest convex coordinate embedding trivializes collinearity. The next decoder must specify actual support lines, endpoint reuse, or another incidence mechanism capable of producing the geometric risks charged by prime patching.
