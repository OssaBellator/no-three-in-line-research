# Universal adjacent width-two matching rungs

The matching-first theorem supplies abundant four-edge reservoirs.  This chapter
shows that every such reservoir has a canonical internally no-three width-two
replacement.  No parabolic endpoint shape is needed.

## 1. The adjacent-pair state

Let the old side be `m`.  Choose four distinct old columns and rows, written in
increasing order as

\[
 c_1<c_2<c_3<c_4,
 \qquad
 y_1<y_2<y_3<y_4.
\]

Put

\[
 a=m+1,
 \qquad
 b=m+2.
\]

Define the movement and refill components

\[
 M=
 \{(c_1,a),(c_2,a),(c_3,b),(c_4,b)\},
\]

\[
 F=
 \{(a,y_1),(a,y_2),(b,y_3),(b,y_4)\}.
\]

Thus the two smaller old coordinates are paired on the first new coordinate and
the two larger old coordinates on the second.

### Proposition PP3bt -- PROVED

The eight-point set

\[
 Q=M\cup F
\]

is no-three-in-line.

#### Proof

The movement component has points on only the two horizontal lines `y=a` and
`y=b`, with exactly two points on each.  A triple in `M` would contain two
points on one of those horizontal lines and a third point on the other, so it
cannot be collinear.  Hence `M` is no-three-in-line.  The same argument with
rows and columns interchanged shows that `F` is no-three-in-line.

Now consider a triple meeting both components.  If it contains two points of
`M`, then either those two points lie on one horizontal line, or one lies in row
`a` with old column `c_1` or `c_2` and the other lies in row `b` with old column
`c_3` or `c_4`.  In the latter case both coordinates increase, so the internal
secant has positive slope.  Every line from a movement point to a refill point
has negative slope: its first coordinate increases from at most `m` to more
than `m`, while its second coordinate decreases from more than `m` to at most
`m`.  Therefore the third refill point cannot lie on the internal movement
secant.  A horizontal movement line cannot meet `F` because all refill rows are
old rows.

The case of two points of `F` and one point of `M` is symmetric.  Two refill
points in one new column determine a vertical line, while a pair using both new
columns has positive slope because the lower old rows are placed in column `a`
and the higher old rows in column `b`.  Every refill--movement cross line has
negative slope.  Thus no mixed triple exists. ∎

The proof is purely order-theoretic.  It works for arbitrary gaps among the old
coordinates.

## 2. Exact matching-reservoir extension

Let `S subseteq [m]^2` be saturated and no-three-in-line.  Suppose `D subseteq S`
is any perfect matching between the four columns `{c_1,c_2,c_3,c_4}` and the
four rows `{y_1,y_2,y_3,y_4}`.  Delete `D` and insert the adjacent-pair state `Q`.

### Theorem PP3bu -- PROVED

The resulting set

\[
 T=(S\setminus D)\cup Q
\]

has exactly two points in every row and column of `[m+2]^2` and has `2(m+2)`
points.  Its inserted set is internally no-three-in-line.  Moreover, `T` is
no-three-in-line if and only if:

1. no point of `Q` lies on a secant through two retained points of `S\setminus D`;
2. no pair of points of `Q` is collinear with one retained point.

#### Proof

Deleting `D` creates deficit one in each of the four selected old columns and
four selected old rows.  The movement component restores every selected old
column once and puts two points in each new row.  The refill component restores
every selected old row once and puts two points in each new column.  Hence all
row and column sums are two, and the net point gain is `8-4=4`.

Internal no-three follows from PP3bt.  The retained set is a subset of the
original no-three configuration.  Therefore every remaining possible triple is
of retained-retained-inserted or retained-inserted-inserted type, giving the two
exact conditions. ∎

This closes endpoint-adapted internal geometry for width two: every four-edge
matching-first reservoir has at least one canonical clean replacement state.

## 3. Consequence for the preparation route

Combining PP3bs and PP3bu gives, for every saturated source and every `m>=4`, a
bank of

\[
 2\binom{m}{4}
\]

layer-labelled width-two matching reservoirs, each with a deterministic
internally clean replacement.

The unresolved obstruction is now entirely external and inter-rung:

- retained-pair secants through inserted cells;
- retained anchors on inserted secants;
- triples using points from different width-two rungs.

The construction is useful despite having only one canonical state per fixed
reservoir.  State entropy may come from selecting the four source edges,
flipping incidence cycles, grouping several reservoirs into one multistate
variable, or adjoining protected rectangle/tomographic trades.

## 4. Relation to reverse ordering

Suppose several four-edge reservoirs are chosen so that their four-column blocks
and four-row blocks are both increasingly ordered.  Assign their two-coordinate
new intervals in reverse order.  Every adjacent-pair movement and refill
component has positive internal nonaxis secants, so PP3bm applies unchanged:
all cross-rung triples repeating one component are excluded, and rank-three
internal bad boxes can only involve three distinct rungs.

Thus the next structural target is a large ordered family of four-edge matching
reservoirs, together with enough reservoir/trade state entropy to control the
remaining distinct-rung bad boxes.