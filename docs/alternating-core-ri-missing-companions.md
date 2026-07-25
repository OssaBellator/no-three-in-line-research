# Missing-companion geometry for one-sided RI fibres

**Branch:** `research/alternating-core-chain`

AC3ba returns incomplete rational fibres, while AC3bc--AC3bd may return one-root physical-scale imbalance. Both outputs consist of paid occurrences whose companion root is not available with matching selected payment. This note constructs the exact same-base companion of every occurrence and routes it to a carry defect, an off-family current factor, or a row-column-regular one-cell completion family.

## Same-base companion

Fix one exact ordered channel pair and one admissible rational fibre. Write

$$
r=b/a,
\qquad
c^\dagger=\tau_r(c),
\qquad
g=F_r(c)=F_r(c^\dagger),
$$

so

$$
cc^\dagger=rg.
$$

A paid occurrence on the `c` root has physical cells

$$
P_x=(x,\langle a/x\rangle_p),
\qquad
P_{gx}=(gx,\langle a/(gx)\rangle_p),
\qquad
B_{cx}=(cx,\langle b/(cx)\rangle_p).
$$

Define its formal same-base companion anchor and triple by

$$
\widehat B_x=
B_{c^\dagger x},
$$

$$
\widehat T_x=
\{P_x,P_{gx},\widehat B_x\}.
$$

## AC3db -- exact modular companion -- PROVED

The formal companion has the same normalized image `g` and is modularly collinear. Its columns satisfy

$$
\boxed{
(cx)(c^\dagger x)=r x(gx).
}
$$

The original and companion anchors are related by the fixed multiplier

$$
\boxed{
\frac{c^\dagger x}{cx}=\frac{c^\dagger}{c}.
}
$$

### Proof

The rational involution identity gives `F_r(c^dagger)=g`, so the modular secant equation

$$
r x(gx)=z(x+gx-z)
$$

holds with `z=c^dagger x`. The product identity is `cc^dagger=rg`, multiplied by `x^2`. The anchor ratio is immediate. QED.

## Real-lift companion defect

Let

$$
\Delta\kappa_x=
\kappa_{c^\dagger x}(x)-
\kappa_{c^\dagger x}(gx)
$$

be the exact cross-carry discrepancy of the formal companion.

## AC3dc -- three-way companion router -- PROVED

Every unmatched paid occurrence has exactly one of the following outputs.

1. **Companion carry defect:**
   $$
   \Delta\kappa_x\ne0.
   $$
   The occurrence returns the exact nonzero carry signature together with `(r,c,c^dagger,g,x)` and the original factor payment.
2. **Off-family current companion:**
   $$
   \Delta\kappa_x=0
   $$
   and the cell `B_{c^dagger x}` is already present in the current configuration. Then `widehat T_x` is an actual current really collinear factor sharing the fixed edge `{P_x,P_{gx}}`. It is an explicit current-defect resource outside the selected companion payment.
3. **Absent-anchor completion desire:**
   $$
   \Delta\kappa_x=0
   $$
   and `B_{c^dagger x}` is absent. Then one cell, with exact column, row, channel, scale and carry address, completes the current fixed edge to a really collinear companion factor.

These cases partition the unmatched occurrence measure.

### Proof

AC3db gives modular collinearity. Equality of the two cross carries is exactly the real-lift condition for the companion secant. Under carry equality, the two same-channel cells are already current. The companion is therefore an actual current factor precisely when its anchor cell is current; otherwise that anchor is the unique missing cell. QED.

## Row-column support of one exact fibre

Aggregate unmatched occurrence weight by the exact base column `x`. For one base `x`, retain one weighted record carrying the total unmatched payment at that base.

The three cells involved in the original fixed edge and formal companion have column multipliers

$$
\mathcal C=\{1,g,c^\dagger\}
$$

relative to `x`. Their row coordinates are `a/x` times the multipliers

$$
\mathcal R=\{1,g^{-1},c/g\},
$$

because

$$
\frac{b}{c^\dagger x}
=
\frac{a}{x}\frac{c}{g}.
$$

## AC3dd -- bounded support-conflict degree -- PROVED

Join two distinct base columns `x,y` when the corresponding three-cell supports

$$
\{P_x,P_{gx},B_{c^\dagger x}\},
\qquad
\{P_y,P_{gy},B_{c^\dagger y}\}
$$

share a row or a column. The conflict graph has maximum degree at most

$$
\boxed{16.}
$$

Consequently it has a row-column-disjoint subfamily carrying at least

$$
\boxed{1/17}
$$

of the aggregated weight.

### Proof

A column collision implies

$$
y/x\in\mathcal C\mathcal C^{-1}.
$$

A row collision implies

$$
y/x\in\mathcal R\mathcal R^{-1}.
$$

Each quotient set has at most nine elements and both contain `1`. Their union therefore has at most seventeen elements, of which at most sixteen are nontrivial. For a fixed `x`, every nontrivial ratio determines at most one conflicting `y`, so the degree is at most sixteen. A greedy proper colouring uses at most seventeen colours; one colour carries at least one seventeenth of the weight. QED.

The selected family has distinct source cells, partner cells and companion anchors, with no row or column reused across records. Full nonadditive certificate conflicts may then be added through the canonical AC3v conflict graph.

## AC3de -- weighted missing-companion output -- PROVED

Let one exact fibre/root/profile class have unmatched paid weight `U`. Then one of the three AC3dc cases has weight at least `U/3`.

1. A carry-defect family has weight at least `U/3`. It enters the AC3a carry-signature exposure/reuse router after splitting by any required finite carry decoration.
2. An off-family current-companion family has weight at least `U/3`. Its members are genuine current defects sharing their paid fixed-edge provenance and enter the AC3f--AC3h resource-eligibility audit.
3. An absent-anchor family has weight at least `U/3`, and AC3dd returns a row-column-disjoint one-cell completion family of weight at least
   $$
   \boxed{U/51.}
   $$

For an additional finite arithmetic profile alphabet of size `L`, the corresponding lower bounds are divided by at most `L`.

### Proof

The three companion cases partition `U`. Weighted pigeonhole selects one. Apply AC3dd to the absent-anchor class. QED.

## AC3df -- unified incomplete/imbalance interface -- PROVED

The paid incomplete-fibre output of AC3ba and the one-root scale-imbalance output of AC3bc--AC3bd now have one common terminal interface. After localizing an exact fibre, root sign and desired finite decorations, they return:

1. a paid nonzero companion carry signature;
2. a paid family of off-selection current companion factors;
3. a paid row-column-disjoint family of exact one-cell companion completions;
4. or the previously proved heavy exact atom/profile alternative before localization.

Every output retains the original current factor, its fixed edge, exact base scale, missing root, companion anchor, quotient labels and cross-carry data. What remains is installation/payment of the one-cell completion family and no-recycling treatment of a repeated off-family companion resource; the rational fibre itself is no longer unclassified.

## Finite check

`scripts/verify_ac_ri_missing_companions.py` enumerates small-prime rational fibres, verifies the same-base companion identities and real/modular split, constructs the row-column support graph, checks the degree-sixteen bound, and verifies the `1/17` and `1/51` weighted constants.