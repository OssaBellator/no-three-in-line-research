# Paid rectangle decoding for RI companion outputs

**Branch:** `research/alternating-core-chain`

AC3dn--AC3dt give private current-factor payment for companion records, break the root involution with one ticket, and extract compatible absent-anchor or four-point-line banks. One logical gap remains: installing an absent companion anchor does not itself destroy the privately paid original factor, because the original anchor survives the one-cell completion. This note supplies the valid paid move. Once both companion anchors are current, switch their active rectangle to the opposite diagonal and repair the blocker layer. The switch removes both anchors, destroys all four current triples on the companion line, and leaves only an exact midpoint/secant collateral profile.

## Companion rectangle

Fix one nonfixed companion fibre at base `x`. Write

$$
E_x=\{P_x,P_{gx}\},
$$

$$
A=B_{cx}=(a_0,b_0),
\qquad
Z=B_{c^\dagger x}=(a_1,b_1).
$$

The four cells

$$
L_x=E_x\cup\{A,Z\}
$$

are distinct and collinear whenever both anchors are current. Since the active layer is a matching,

$$
a_0\ne a_1,
\qquad
b_0\ne b_1.
$$

Define the opposite rectangle diagonal

$$
C=(a_0,b_1),
\qquad
D=(a_1,b_0).
$$

## AC3et -- exact companion-rectangle geometry -- PROVED

Replacing `A,Z` by `C,D` preserves the active row and column sets. The cells `C,D` are distinct and are not active while `A,Z` are active.

Every one of the four three-subsets of `L_x` is a current collinear certificate. After the rectangle switch, among the four support cells

$$
E_x\cup\{C,D\}
$$

there is at most one collinear triple. More precisely, for any point `Q` on the line through `A,Z`,

$$
\boxed{
Q,C,D\text{ are collinear}
\iff
2Q=A+Z
}
$$

coordinatewise. Thus the only possible internal replacement triple is

$$
\{Q,C,D\}
$$

where one fixed-edge point is the exact midpoint of the two anchors; at most one of `P_x,P_{gx}` can satisfy this condition.

### Proof

The rectangle diagonals use the same two rows and columns, so the switch preserves the matching sets. Translate `A` to the origin and write

$$
Z=(\Delta_x,\Delta_y),
\qquad
C=(0,\Delta_y),
\qquad
D=(\Delta_x,0),
$$

with `Delta_x Delta_y != 0`. The two diagonal lines `AZ` and `CD` meet at the rectangle centre

$$
(\Delta_x/2,\Delta_y/2).
$$

Hence a point `Q` on `AZ` also lies on `CD` exactly when it is that midpoint, which is the displayed coordinate identity. The four old triples are collinear because all four old support points lie on one line. QED.

## AC3eu -- exact two-layer rectangle decoder -- PROVED

Assume `A,Z` are active. Switch the active diagonal

$$
\{A,Z\}\longrightarrow\{C,D\}.
$$

Let

$$
t=|\{C,D\}\cap M_1|\in\{0,1,2\}.
$$

A legal blocker repair always exists.

1. `t=0`: leave the blocker layer unchanged.
2. `t=1`: transpose the unique blocked target with any other blocker cell.
3. `t=2`: transpose the two blocker rows; equivalently, the blocker layer takes `A,Z` while the active layer takes `C,D`.

Every resulting state preserves both permutation layers and their disjointness, removes both anchors from the active layer, and destroys all four current triples on `L_x`. In particular it destroys the privately paid original factor

$$
T_x^c=E_x\cup\{A\}.
$$

### Proof

The active switch is a two-column matching switch. The blocker argument is the same fixed-point-free row-permutation proof as RI5h--RI5m: after the active layer uses `C,D`, every nontrivial permutation of blocker rows on the selected target columns avoids the active cells. In the singleton case, an auxiliary blocker transposition has the same rectangle property. Since both old anchors leave the active layer, every three-subset of `L_x` is destroyed. QED.

## AC3ev -- direct off-family decoder bank -- PROVED

Let one exact off-family current-companion class have total paid weight `V`. Use the row-column-disjoint `1/31` extraction of AC3ds, but build the AC3v graph from the full rectangle-decoder envelopes of AC3eu, including every blocker repair, potential scope, protected condition, and private paid factor.

For every `K>=1`, either:

1. one finite decoder-envelope incidence label has paid closed-neighbourhood load greater than `K` times its own weight; or
2. an independent executable rectangle-decoder family has private paid weight
   $$
   \boxed{D\ge V/(31K).}
   $$

Choose independently from each local blocker-repair menu. Let `R` denote new active rectangle cells and `B` new blocker-repair layer-cells. Every new collateral triple has one of the three nonempty masks

$$
R,\qquad B,\qquad RB.
$$

If no product state improves, one exact mask has expected collateral at least

$$
\boxed{D/3\ge V/(93K).}
$$

If the off-family branch came from an unmatched class of weight `U`, then `V>=U/3`, so the returned mask has weight at least

$$
\boxed{U/(279K).}
$$

The `R` and `RB` masks further retain whether the triple contains exactly one of `C,D`—a fixed-centre context star—or both, an exact cross-pair secant. The unique internal secant possibility is the midpoint label of AC3et.

### Proof

AC3ds gives the factor `1/31`; AC2c applied to the full decoder graph gives the factor `1/K` or a finite overload. AC3eu destroys every private paid factor, while AC3v and AC3w give exact legality, payment, and collateral additivity. A new triple must use a new active rectangle cell, a new blocker cell, or both. Failure of strict improvement makes the three expected mask weights sum to at least `D`; pigeonhole gives `D/3`. QED.

## Absent-anchor preparation

Now assume `Z` is absent from the active layer. Let

$$
y=M_0^{-1}(b_1)
$$

be the current owner column of its desired row. The canonical one-cell completion replaces

$$
(a_1,M_0(a_1)),
\qquad
(y,b_1)
$$

by

$$
Z=(a_1,b_1),
\qquad
Q=(y,M_0(a_1)).
$$

The original anchor `A`, both fixed-edge cells, and their rows and columns are untouched. Hence the intermediate active state contains the four-point line `L_x`, while the closure cell `Q` lies outside its rows and columns.

Repair every blocker intersection with the two new active cells `Z,Q` by the exact zero/singleton/two-cell menu. Then apply AC3eu to `A,Z` and repair the second active switch.

## AC3ew -- absent-anchor install-and-decode transition -- PROVED

Every absent-anchor companion record has a nonempty legal composite menu consisting of:

1. the canonical one-cell active completion installing `Z` and closure `Q`;
2. an exact blocker repair for intersections with `Z,Q`;
3. the active companion-rectangle switch `A,Z -> C,D`;
4. an exact blocker repair for intersections with `C,D`.

Every composite state preserves both permutation layers, leaves the fixed edge `E_x` unchanged, removes the original anchor `A`, and therefore destroys the private paid factor `T_x^c`.

The installation closure `Q` lies outside the companion-rectangle rows and columns, so the second switch does not disturb it. The transition consumes the capacity-one unordered-fibre/base ticket of AC3dp.

### Proof

The one-cell completion is the `|Z|=1` case of AC3ep and preserves the original factor support. Its blocker repair is AC3eq with at most two selected new active cells. The intermediate state contains `A,Z`, so AC3eu applies. The two stages use disjoint active row-column scopes except for the deliberately installed anchor `Z`; the closure cell remains outside the rectangle. The final switch removes `A`, certifying destruction of `T_x^c`. QED.

## AC3ex -- absent-anchor composite bank and seven-mask router -- PROVED

Enlarge the AC3dq one-cell-completion envelope to include every state of AC3ew. Its proof is unchanged: for every `K>=1`, an absent-anchor class of paid weight `W` gives a finite scoped overload or an independent executable composite family of weight at least

$$
\boxed{D\ge W/K.}
$$

For a final new collateral triple, record which of the following stage alphabets it meets:

- `A`: installation target or closure cells;
- `B`: cells introduced by either blocker repair;
- `R`: final active rectangle cells `C,D`.

The seven nonempty masks partition all new collateral. If no product state improves, one exact mask has expected collateral at least

$$
\boxed{D/7.}
$$

Composed with the `U/51` absent-anchor extraction of AC3de, a failed composite bank returns one exact mask of weight at least

$$
\boxed{U/(357K)}
$$

unless a finite scoped overload occurs.

Masks meeting `R` retain the one-cross-star/two-cross-secant split and the midpoint label of AC3et. Masks avoiding `R` are pure installation/blocker profiles and enter the AC3ep--AC3es completion routers.

### Proof

AC3ew supplies a nonempty local paid decoder. AC3v and AC3w give exact product legality and additivity on the independent envelope family. Every final new triple meets at least one of the three stage alphabets. Failure makes the seven mask expectations sum to at least `D`, so one is at least `D/7`. Finally use `D>=U/(51K)`. QED.

## AC3ey -- corrected companion payment interpretation -- PROVED

The private original factor of AC3dn is a valid charge for the rectangle-decoder transition of AC3eu or AC3ew, not for bare companion-anchor installation.

Bare installation leaves the original anchor `A` and therefore leaves `T_x^c` current. The paid certificate is destroyed only when the companion rectangle is switched. Both the direct and absent-anchor decoders consume the same capacity-one unordered-fibre/base ticket of AC3dp, so immediate root reversal remains impossible.

### Proof

The one-cell completion changes the desired anchor column and its row-owner column, neither of which is the original-anchor column; hence `A` survives. AC3eu removes `A`. Ticket identity follows from the unchanged unordered fibre/base address. QED.

## Consequence

The companion frontier now has an actual paid move.

- Off-family four-point lines admit a direct legal rectangle decoder.
- Absent anchors admit a canonical install-and-decode composite transition.
- Every transition destroys the private original factor and consumes the existing fibre ticket.
- Failure returns finite rectangle-star/secant, blocker, installation, or midpoint profiles with explicit constants.

The remaining work is arithmetic termination of those returned masks and their finite overload labels, not construction of a paid companion transition.

## Finite check

`scripts/verify_ac_ri_companion_rectangle_decoder.py` exhausts normalized direct and absent-anchor rectangle systems, all disjoint blocker permutations and both repair stages, verifies the midpoint identity, protected fixed-edge support, three- and seven-mask routers, and the constants `1/279` and `1/357`.