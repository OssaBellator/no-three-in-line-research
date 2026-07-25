# Complete-cross and line-refined pivot saturation

**Branch:** `research/alternating-core-chain`

AC3gn--AC3gq reduce repeated decorated pivot execution to one terminal local profile: for one current pivot and retained role, all canonical partner signatures have already appeared. This note identifies the exact current geometry of that profile. The partner rectangles cover the complete row-and-column cross through the pivot, the opposite layer occupies exactly two cells of that cross, and the blocker occupancies have only two possible global patterns. A weighted saturation record also localizes to one real line through the pivot and can be restarted once with that line as an additional finite role label.

## Setup

Normalize the pivot layer by relabelling rows. Thus the pivot layer is

$$
M_0=\{(c,c):0\le c<n\},
$$

and the pivot is

$$
z=(0,0).
$$

Write the opposite permutation layer as

$$
M_1=\{(c,b(c)):0\le c<n\},
$$

where `b` is a derangement because the two layers are disjoint.

For every partner column `c!=0`, the pivot-layer partner is `(c,c)` and the desired opposite diagonal is

$$
X_c=(0,c),
\qquad
Y_c=(c,0).
$$

Let

$$
\beta=b(0),
\qquad
\delta=b^{-1}(0).
$$

Disjointness gives `beta!=0` and `delta!=0`.

## AC3gr -- complete pivot-cross identity -- PROVED

The union of the desired cross cells over all partner columns is exactly

$$
\boxed{
\{X_c,Y_c:1\le c<n\}
=
(\{0\}\times([n]\setminus\{0\}))
\cup
(([n]\setminus\{0\})\times\{0\}).
}
$$

In particular, the `n-1` partner rectangles generate every nonpivot cell in the pivot column and every nonpivot cell in the pivot row, each exactly once.

### Proof

As `c` runs through `1,...,n-1`, the cells `X_c=(0,c)` are exactly the nonpivot cells of column zero, while the cells `Y_c=(c,0)` are exactly the nonpivot cells of row zero. The two sets are disjoint. QED.

## AC3gs -- exact fused/split blocker law -- PROVED

The opposite layer occupies exactly two cells of the complete pivot cross:

$$
(0,\beta),
\qquad
(\delta,0).
$$

Consequently the partner-rectangle blocker counts have exactly one of the following forms.

1. **Fused pattern:** `beta=delta`. The unique partner `c=beta` has both desired cross cells blocked, and every other partner is empty. Thus the occupancy multiset is
   $$
   \boxed{\{2,0^{\,n-2}\}.}
   $$
2. **Split pattern:** `beta!=delta`. Partners `c=beta` and `c=delta` each have one blocked cross cell, and every other partner is empty. Thus the occupancy multiset is
   $$
   \boxed{\{1,1,0^{\,n-3}\}.}
   $$

There are no other saturation blocker patterns. In particular, every saturated pivot has at least `n-3` empty partner rectangles, and the fused case has `n-2`.

### Proof

A pivot-column cross `X_c=(0,c)` belongs to `M_1` exactly when `b(0)=c`, so exactly `X_beta` is blocked. A pivot-row cross `Y_c=(c,0)` belongs to `M_1` exactly when `b(c)=0`, so exactly `Y_delta` is blocked. These two occupied cross cells belong to the same partner rectangle exactly when `beta=delta`; otherwise they belong to two different rectangles. QED.

## Weighted line localization

Fix a full partner-saturation record at pivot `z` carrying current paid role weight `W_role`. Every represented current certificate is a collinear triple containing `z`. Assign each certificate to its unique real line through `z`.

The two-layer union has at most `2n-1` other current cells, so at most `2n-1` real lines through `z` contain a represented certificate.

## AC3gt -- heavy saturated pivot line -- PROVED

One real line `ell` through `z` carries paid saturated-role weight at least

$$
\boxed{
\frac{W_{\rm role}}{2n-1}.
}
$$

If the saturation record came from AC3gp applied to a pivot bucket of total weight `W` and a retained alphabet of size `L`, then one line carries at least

$$
\boxed{
\frac{W}{L(2n-1)}.
}
$$

The selected profile retains the pivot, pivot layer, exact line, current certificate set, complete partner cross, fused/split blocker type, all local blocker rows and the original arithmetic/geometric role.

### Proof

Every represented triple belongs to one unique line through `z`. Each such line contains at least one current cell other than `z`, and there are at most `2n-1` such cells in the union. Weighted pigeonhole gives the first bound. AC3gp gives `W_role>=W/L`, proving the second. QED.

## One finite line refinement

Encode a line through a grid cell by its primitive unoriented integer direction. A safe global bound for the number of possible directions is

$$
(2n-1)^2-1<4n^2.
$$

Refine the retained role label `lambda` to

$$
\lambda^\ell=(\lambda,\operatorname{dir}(\ell)).
$$

If the original retained role alphabet has size `L`, the line-refined alphabet has size less than `4Ln^2`. Applying AC3gn with the refined labels gives the safe signature bound

$$
\boxed{
|\Sigma_{\rm line}(n,L)|
\le 8Ln^{10}.
}
$$

## AC3gu -- line-refined saturation router -- PROVED

Let a full partner-saturation record arise from a pivot bucket of total weight `W`. Select the heavy line from AC3gt and use its refined role label. Exactly one of the following holds.

1. **New line-decorated pivot:** one canonical partner signature with the refined line label has not appeared. Executing it destroys the entire pivot bucket of weight `W` and exposes a new element of `Sigma_line`.
2. **Full line-partner saturation:** every canonical partner signature has already appeared with the same pivot, layer, line direction and retained role. The output carries paid current line weight at least
   $$
   \boxed{W/(L(2n-1))}
   $$
   and has one exact fused or split blocker pattern from AC3gs, together with at least `n-3` previously exposed empty-rectangle signatures.

A mixed epoch of strict AC2d support descent and new line-decorated pivot exposure is controlled by

$$
\boxed{
\Xi_{\rm line}(U,E)
=
N|E|+N-|U|
}
$$

and has at most

$$
\boxed{
N|\Sigma_{\rm line}|+N-1
}
$$

nonterminal transitions.

### Proof

AC3gt supplies the line and its paid weight. Apply the AC3go dichotomy in the expanded finite role alphabet. Every partner decoder still removes the pivot and therefore destroys the whole bucket, not only the selected line class. The signature count follows from AC3gn with fewer than `4Ln^2` refined labels. The potential proof is identical to AC3gq: strict support descent raises `N-|U|`, while a new signature raises `N|E|` by `N` and can lose at most `N-1` in the support term. QED.

## Consequence

A full partner-saturation output is no longer an unstructured recurrence state. It has:

- a complete row-and-column cross through one current pivot;
- exactly two opposite-layer cells on that cross;
- one fused or split blocker pattern;
- a current fixed-centre line profile carrying at least `W/(L(2n-1))`;
- and, after one finite direction refinement, either a new signature or a full line-partner-saturation record.

The remaining saturation frontier is now the exact line-saturated profile. It is suitable for the fixed-centre/anchor-star machinery or for arithmetic classification using its retained carry, denominator, RI, channel, closure or blocker label. No diffuse local blocker pattern remains.

## Finite check

`scripts/verify_ac_saturation_cross_router.py` exhausts normalized disjoint permutation pairs on grids three through eight, verifies complete-cross coverage, the exact two occupied cross cells, every fused/split occupancy multiset, partner-signature distinctness, weighted line pigeonholes, the `8Ln^10` refined signature bound and every transition inequality for `Xi_line`.