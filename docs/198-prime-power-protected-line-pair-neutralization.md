# Protected target-line saturation yields global pair neutralisation

CMR748--CMR754 turn recurrent target lines into a finite simultaneous line
reserve. At reserve saturation the stored target triples occurred at different
times, so they must not be treated as a simultaneous target family. The correct
operation is instead to neutralise one fixed pair from many historical target
signatures in one new saturated state.

A globally compatible pair family can be omitted by both permutation layers at
once. A matching-vertex fan becomes either many distinct absent wall cells or one
fixed cell supporting many target signatures. Every later reuse is therefore an
edge-reintroduction event rather than fresh line stock.

Fix one closure-envelope epoch of side

\[
q=p^g,
\]

with invariant row sets for the two permutation layers. Let

\[
\mathscr L=\{L_1,\ldots,L_J\}
\]

be distinct protected target-line signatures in one dyadic primitive-height
band. With every line retain the exact historical physical target triple `T_i`
which first supplied that line.

## 1. Common-layer target-pair extraction

### Theorem CMR755 -- PROVED

For every `i`, the nonaxis target triple `T_i` contains a compatible pair of
cells from one permutation layer. One may choose these pairs canonically so that
one layer contains at least

\[
\boxed{J_0\ge\left\lceil\frac J2\right\rceil}
\]

of them. The resulting pairs

\[
P_1,\ldots,P_{J_0}
\]

are pairwise distinct, and every cell of every pair belongs to the fixed
matching board of that layer over the current envelope.

### Proof

Three target cells distributed between two layers have at least two cells in one
layer. Choose the lexicographically first same-layer pair in the majority layer
of each triple. One of the two layers is the majority layer for at least half the
line signatures.

Every target line is nonaxis, so the two cells of its chosen pair have distinct
source and target coordinates and form a compatible partial matching. A pair of
distinct physical cells determines its real line, hence distinct lines give
distinct chosen pairs. CMR172 keeps the layer row set over the envelope fixed, so
every historical pair remains a valid cell pair of the same labelled matching
board. ∎

The triples need not be simultaneously selected; only their physical pair
signatures are retained.

## 2. Matching-vertex fan or globally compatible pair bank

Fix an integer threshold `A>=1`.

### Theorem CMR756 -- PROVED

At least one of the following holds for the `J_0` chosen pairs.

1. **Matching-vertex fan.** One source or target matching vertex is incident with
   at least `A` pairs.
2. **Globally compatible pair bank.** There is a subfamily of size at least

   \[
   \boxed{
   R=\left\lfloor\frac{J_0}{4A}\right\rfloor
   }
   \]

   whose complete collection of `2R` cells is one partial matching.

### Proof

Apply the greedy argument of CMR355. If the maximum matching-vertex incidence is
at least `A`, the first branch holds. Otherwise choosing one pair and deleting
all pairs meeting one of its four matching vertices removes fewer than `4A`
pairs. The selected pairs therefore form a globally matching-compatible family
of at least the displayed size. ∎

## 3. Historical fan signatures split by physical cells

Suppose the fan branch supplies `M>=A` pairs incident with one matching vertex.
Every pair has one unique cell incident with that vertex.

### Theorem CMR757 -- PROVED

At least one of the following holds.

1. **Distinct-cell wall.** The fan uses at least

   \[
   \boxed{C\ge\lceil\sqrt M\rceil}
   \]

   distinct physical cells on the fixed source column or target row.
2. **Repeated-cell target star.** One physical cell `z` belongs to more than

   \[
   \boxed{\sqrt M}
   \]

   chosen pair signatures. The corresponding target lines are distinct and the
   other chosen cells are pairwise distinct.

### Proof

Let `C` be the number of incident physical cells. If
`C>=ceil(sqrt(M))`, use the first branch. Otherwise one cell has multiplicity
more than `M/C>sqrt(M)`. Two distinct lines through `z` cannot share another
physical cell, since two points determine a unique real line. ∎

This is the owner-labelled historical version of CMR390; no simultaneous target
claim is made.

## 4. Global neutralisation of the fan branch

Assume `q>=8`, and let `T` be the current live target which must be destroyed by
the next closure transition.

### Theorem CMR758 -- PROVED

The fan alternatives of CMR757 admit the following global neutralisations.

1. In the distinct-cell wall branch, apply any saturated target-destroying
   closure transition. In its final state at most two of the `C` wall cells are
   selected, one by each permutation layer. Hence at least

   \[
   \boxed{C-2}
   \]

   distinct wall cells are absent. Choosing one attached target-pair signature
   for each absent wall cell gives `C-2` neutralised historical target
   signatures with distinct absent witnesses.
2. In the repeated-cell branch, there is an ordered two-layer rematching which
   destroys `T` and leaves `z` absent from both layers. It therefore neutralises
   every stored target signature whose chosen pair contains `z`.

### Proof

A saturated two-layer state contains at most two selected physical cells on one
fixed grid column or row. This proves the first assertion after using CMR700 for
a target-destroying saturated transition.

For the second assertion, rematch the first layer over the full envelope while
forbidding its old matching, the current opposite-layer matching, the singleton
`z`, and the cells of `T` which belong to that board. These four sets have total
row and column degree at most four. Since `q>=8`, the allowed graph has minimum
degree at least `q/2`, so the Hall argument of CMR128 supplies a perfect
matching.

Then rematch the second layer while forbidding its old matching, the newly
selected first-layer matching, `z`, and its board cells of `T`. The same degree
bound applies. The final two-layer state is saturated, layer-disjoint, avoids
`z` globally, and avoids every cell of `T` in both layers, so the current target
is destroyed. Every stored signature containing `z` is absent. ∎

The ordered construction explicitly forbids the live target in the second
layer; it does not use the false naive sequential-rematching claim CMR138.

## 5. Global neutralisation of a compatible pair bank

Let `P_1,...,P_R` be the compatible family from CMR756 and put

\[
Q=P_1\sqcup\cdots\sqcup P_R.
\]

Thus `Q` is a partial matching of `2R` physical cells.

### Theorem CMR759 -- PROVED

Assume `q>=8`. There is an ordered two-layer closure transition whose final state

1. destroys the current live target `T`;
2. avoids every physical cell of `Q` in both permutation layers;
3. preserves saturation, layer disjointness, and both invariant envelope row
   sets.

Consequently all `R` historical target-pair signatures are simultaneously
neutralised in one current state.

### Proof

For the first layer, forbid the old layer matching, the current opposite-layer
matching, `Q`, and the board intersection of `T`. The first two families have
combined degree at most two, while `Q` and `T` each have degree at most one.
Hence the total forbidden degree is at most four, and `q>=8` gives an allowed
perfect matching by CMR128.

For the second layer, forbid its old matching, the new first-layer matching,
`Q`, and `T`. The same degree bound gives a perfect matching. Both final layers
avoid `Q` and `T`; their row sets and column sets are unchanged. ∎

The size of `Q` is irrelevant to the degree estimate because it is one partial
matching.

## 6. Quantitative reserve extraction

### Theorem CMR760 -- PROVED

Let

\[
A=\left\lceil\sqrt{J_0/2}\right\rceil,
\qquad J_0\ge8.
\]

At reserve saturation, one obtains at least one of the following owner-labelled
outputs.

1. A compatible pair bank of size

   \[
   R=\left\lfloor\frac{J_0}{4A}\right\rfloor
   \ge
   \left\lfloor\sqrt{\frac{J_0}{18}}\right\rfloor,
   \]

   globally neutralised by CMR759.
2. A distinct-cell wall with at least

   \[
   \left\lceil (J_0/2)^{1/4}\right\rceil-2
   \]

   distinct absent target-cell witnesses after CMR758.
3. One physical cell supporting more than

   \[
   (J_0/2)^{1/4}
   \]

   distinct target-line signatures, globally forbidden by CMR758.

### Proof

CMR756 gives either the compatible branch or a fan of size `M>=A`. In the fan
branch apply CMR757 and CMR758; since `sqrt(M)>=sqrt(A)>=(J_0/2)^{1/4}`, the
last two bounds follow.

For the compatible branch, write `x=sqrt(J_0/2)>=2`. Then

\[
A=\lceil x\rceil\le\frac32x.
\]

Therefore

\[
\frac{J_0}{4A}
\ge
\frac{J_0}{6\sqrt{J_0/2}}
=
\sqrt{\frac{J_0}{18}},
\]

and taking floors gives the result. ∎

## 7. First return of a neutralised signature is edge payment

### Theorem CMR761 -- PROVED

Start from one of the final neutralising states above.

1. If a neutralised wall signature later reappears as its exact physical target,
   its chosen distinct absent witness cell undergoes an absent-to-present
   transition.
2. If a target from a repeated-cell star reappears, the common cell `z` has been
   reintroduced.
3. If a target from the compatible pair bank reappears, both cells of its chosen
   pair have each undergone at least one absent-to-present transition since the
   neutralising state.

If `k` distinct compatible-bank targets reappear, these transitions involve
`2k` distinct physical cells. If `k` distinct wall-witness targets reappear,
they involve `k` distinct physical cells.

### Proof

Every recorded witness cell is absent in the neutralising state. A later target
contains all cells of its stored chosen pair, so every absent pair cell must
become selected before or at the first later occurrence. In the compatible
branch all pair cells are distinct because their union is a partial matching. In
the wall branch the witnesses were chosen distinct. ∎

Every such return carries the entering-edge, absence-run, target-cell, and exact
full-token charges of CMR413, CMR519, and CMR707--CMR710.

## 8. Protected-line saturation endpoint

### Corollary CMR762 -- PROVED

A saturated protected target-line reserve inside an envelope of side `q>=8`
reaches at least one of:

1. a matching-vertex historical fan, refined to a distinct-cell wall or a
   repeated-cell target star;
2. one globally neutralised compatible target-pair bank;
3. a current target-destroying two-layer state in which many historical target
   signatures are absent;
4. permanent disappearance of those signatures from the later target history;
5. first-return edge reintroduction with distinct-cell multiplicity as in
   CMR761;
6. the existing recurrent-cell deletion, returned-edge ancestry, unit-wall,
   contraction, owner-change, or envelope-expansion alternatives.

Thus the CMR754 saturation branch is no longer only a height-localised line
family. It produces a current saturated state which globally neutralises a
quantitative historical target-pair reserve. Any reuse of that reserve is paid
by explicit physical edge returns.

### Proof

Apply CMR755--CMR760 and then CMR761. Structural returns use CMR713--CMR747, and
crossing moves use CMR193. ∎

No all-`n` theorem is claimed. The finite fan/matching extraction, degree-four
Hall bounds, global two-layer avoidance, and quantitative thresholds are checked
in
[`scripts/verify_prime_power_protected_line_pair_neutralization.py`](../scripts/verify_prime_power_protected_line_pair_neutralization.py).
