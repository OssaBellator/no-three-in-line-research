# Union-safe heterogeneous BDA products and rank-one suppression

**Branch:** `research/bounded-denominator-absorbers`

BDA5ai--BDA5ak replace the old full-blocker phase flip by a union-safe local repair. This note propagates that correction through the heterogeneous product and rank-one-suppression ledgers. The key replacement for the old envelope claim is column-supported blocker transport: auxiliary blocker rows need not belong to the five active-support rows, but every blocker row permutation can be confined to columns of the same five-column radial support.

## Canonical local role states

Fix one clean co-anchored adjacent radial pair with five support columns

$$
C_R=\{c_0,c_1,c_2,c_3,c_4\}.
$$

For one role, let its active endpoints be

$$
A=(c_i,r_i),\qquad B=(c_j,r_j),
$$

and its desired opposite diagonal be

$$
C=(c_i,r_j),\qquad D=(c_j,r_i).
$$

The complement `C_R\setminus\{c_i,c_j\}` has three columns. Fix an order on those columns.

- If neither `C` nor `D` is blocked, use the empty-diagonal active switch.
- If exactly one is blocked, use the BDA5ai singleton repair and choose the first complementary support column whose blocker row is not the old endpoint row that would be restored. At most one complementary column owns that row, so at least two choices remain.
- If both are blocked, use the first two complementary support columns in the BDA5ai four-row repair.

Apply this rule separately to the two radial roles `u` and `v`.

## BDA5al -- canonical two-state union-safe menu -- PROVED

Every clean radial pair has exactly two canonical union-safe decoder states

$$
\boxed{
\Omega_{\rm safe}(R)=\{s_R^u,s_R^v\}.
}
$$

For each state:

1. the active layer switches exactly one radial role to its opposite diagonal;
2. the blocker repair changes rows only in a subset of the five support columns `C_R`;
3. both old endpoints of the switched role are absent from the final two-layer union;
4. both paid radial triples are destroyed;
5. both permutation layers and their disjointness are preserved.

### Proof

The complement of either role rectangle inside `C_R` has three columns. In the singleton case, only the unique blocker owner of one old endpoint row is forbidden as an auxiliary, so a canonical admissible support column exists. In the full case, any two complementary support columns work. BDA5ai proves legality and exclusion of both old endpoints from the union. BDA5aj then destroys both paid radial triples. The `u`- and `v`-states differ in their active switched endpoints, so the menu has exactly two states. QED.

## BDA5am -- union-safe heterogeneous simultaneous decoder -- PROVED

Let `F` be a family of clean radial pairs whose five-cell supports use pairwise disjoint row sets and pairwise disjoint column sets. Choose arbitrarily

$$
s_R\in\Omega_{\rm safe}(R)
\qquad(R\in\mathcal F).
$$

Then the union of the chosen local states is a legal two-layer permutation state and destroys both paid radial triples of every represented pair.

No occupancy regularization and no decoder-type loss are required.

### Proof

The active changes use only the pair's five support rows and columns, so active changes from distinct pairs are disjoint.

For one pair, the blocker repair is a permutation of the blocker rows originally occupying a subset

$$
K_R\subseteq C_R.
$$

Distinct pairs have disjoint support-column sets, hence disjoint sets `K_R`. Because the blocker layer is a permutation, the blocker-row sets originally occupying those disjoint column sets are also disjoint. Therefore the local blocker row permutations commute and their union remains a permutation.

Each local repair is disjoint from the locally switched active layer by BDA5ai. A cross-pair active/blocker cell collision would require a common column, impossible because the support-column sets are disjoint. Cells outside all selected supports are unchanged. Finally BDA5aj gives union-level destruction of both paid triples in every local state. QED.

The auxiliary blocker rows need not lie in the active-support row set. The proof uses disjoint support columns and the permutation property of the blocker layer, not the false stronger claim that every changed cell remains inside the five-by-five support rectangle.

## BDA5an -- exact union-safe product collateral -- PROVED

Choose independently and uniformly from the two-state menus `Omega_safe(R)`. Let `D` be the total distinct paid weight destroyed by the family.

For a candidate collateral triple `C`, let `J(C)` be the set of local decoder supports containing one of its cells. Since the support-column sets are disjoint and a triple has three cells,

$$
\boxed{|J(C)|\le3.}
$$

Let `m_C` be the number of local binary state tuples on `J(C)` that create `C`. Then

$$
\boxed{
\Pr(C\text{ is created})
=
\frac{m_C}{2^{|J(C)|}}.
}
$$

After moving state-independent collateral into `F`, define

$$
T_r
=
\sum_{|J(C)|=r}
 w_C\frac{m_C}{2^r},
\qquad r=1,2,3.
$$

If

$$
\boxed{D>F+T_1+T_2+T_3,}
$$

one union-safe heterogeneous product state strictly lowers the paid union-triple potential.

### Proof

BDA5al gives two equally weighted states per support. A collateral event depends only on the states indexed by `J(C)`, so exactly `m_C` of the `2^{|J(C)|}` local tuples create it. Linearity of expectation gives the displayed collateral sum, while BDA5am destroys paid weight `D` in every product state. QED.

## BDA5ao -- rank-one suppression survives unchanged -- PROVED

Normalize every rank-one triple which occurs in both local role states into the fixed term `F`. For one pair write

$$
A_R(u),\qquad A_R(v)
$$

for the remaining rank-one weights created only by the corresponding role state. Define

$$
B_1=\sum_R\min\{A_R(u),A_R(v)\},
$$

$$
I_1=\sum_R|A_R(u)-A_R(v)|.
$$

Then

$$
\boxed{T_1=B_1+\frac{I_1}{2}.}
$$

Choosing the cheaper role at every pair gives a legal union-safe product with actual rank-one collateral exactly `B_1`. If its actual rank-two and rank-three collateral are `C_2,C_3`, then

$$
\boxed{C_2\le4T_2,\qquad C_3\le8T_3.}
$$

Consequently,

$$
\boxed{D>F+B_1+4T_2+8T_3}
$$

implies an improving union-safe product. If `D>F` but this criterion fails, then at least one of

$$
\boxed{B_1\ge\frac{D-F}{3},}
$$

$$
\boxed{T_2\ge\frac{D-F}{12},}
$$

$$
\boxed{T_3\ge\frac{D-F}{24}}
$$

holds.

### Proof

The floor/imbalance identity is the two-number identity

$$
\frac{a+b}{2}=\min(a,b)+\frac{|a-b|}{2}
$$

summed over pairs. BDA5am permits arbitrary independent choices, so the cheaper-role product is legal.

A collateral triple depending on `r` supports has each realizing binary tuple at probability `2^{-r}`. If the deterministic cheaper-role tuple creates it, its indicator is at most `2^r` times its product probability. This gives the factors `4` and `8`. The failed-router constants follow by pigeonholing the three nonnegative terms `B_1,4T_2,8T_3`. QED.

## Correction and consequence

For the union potential:

- BDA5am supersedes the product-legality proof of BDA5f;
- BDA5an supersedes BDA5g with the exact denominator `2^{|J(C)|}`;
- BDA5ao supersedes BDA5h--BDA5j without changing their numerical suppression and failed-router constants;
- every downstream product envelope must include the canonical singleton or full-block auxiliary blocker columns and all replacement cells.

The propagation frontier through heterogeneous products and rank-one suppression is therefore closed. The remaining BDA frontier is termination of the balanced floor, rank-two/rank-three profiles, affine anchor chains and finite transition cycles.

## Finite check

`scripts/verify_bda_union_safe_products.py` exhausts all derangements on the normalized five-column support, both canonical role states, every blocker occupancy, heterogeneous products on up to three disjoint supports, exact binary product events, floor/imbalance systems, higher-rank event bounds and the failed-router constants. It also records the full-block phase-flip regressions.
