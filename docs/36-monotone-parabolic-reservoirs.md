# Monotone parabolic matching reservoirs

The row-lift investigations separate two difficulties:

1. constructing an internally no-three replacement with the correct row and
   column deficits;
2. keeping that replacement clear of the retained core.

This chapter closes the first difficulty for one explicit matching-reservoir
architecture.  The construction has square-root coordinate width and leaves only
the two external certificate classes from PP2b.

## 1. A monotone two-branch parabola

Fix integers

\[
 t\ge2,\qquad L\ge2,\qquad 1\le d<L,
\]

and an integer offset `A`.  Put

\[
 P_{A,L,d}(t)
 =
 \{(A+Lj^2,j),(A+Lj^2+d,j):0\le j<t\}.
\]

### Proposition PP3ac -- PROVED

The set `P_{A,L,d}(t)` has the following properties.

1. It has `2t` distinct points, exactly two in every displayed row, and at
   most one in every displayed column.
2. It is no-three-in-line.
3. Every nonhorizontal secant has positive slope.

#### Proof

For consecutive row indices,

\[
 A+Lj^2+d
 <
 A+L(j+1)^2,
\]

because `d<L<=L(2j+1)`.  Hence the two columns in row `j` lie strictly before
the two columns in row `j+1`.  This proves distinctness and the positive-slope
claim.

A collinear triple cannot contain both points of one row and a point of a
different row, because the first two determine a horizontal line.  We may
therefore assume that its row indices `a,b,c` are distinct.

If all three points lie on the same branch, they lie on one nondegenerate
parabola

\[
 x=A+Ly^2+\varepsilon d,
\]

which a line meets at most twice.

Otherwise exactly one of the three branch labels differs from the other two.
If the exceptional point has row index `c`, direct expansion of the determinant
gives, up to sign,

\[
 (a-b)\bigl(L(c-a)(c-b)\pm d\bigr).
\]

The first factor is nonzero.  The product `(c-a)(c-b)` is a nonzero integer,
so

\[
 |L(c-a)(c-b)|\ge L>d.
\]

The second factor is also nonzero.  The cases in which the exceptional point
has row index `a` or `b` are identical after relabelling.  Thus no collinear
triple exists. ∎

The transposed set has the analogous properties: two points in each displayed
column, at most one in each displayed row, and every nonvertical secant has
positive slope.

## 2. Sign separation between the two cross rectangles

Let the old grid be `[m]^2` and put

\[
 N=\{m+1,\ldots,m+t\}.
\]

### Lemma PP3ad -- PROVED

Let

\[
 M\subseteq [m]\times N,
 \qquad
 F\subseteq N\times[m].
\]

Assume that `M` and `F` are individually no-three-in-line and every nonaxis
secant inside either set has positive slope.  Then `M union F` is
no-three-in-line.

#### Proof

A line joining a point of `M` to a point of `F` has negative slope: its
horizontal coordinate increases from at most `m` to more than `m`, while its
vertical coordinate decreases from more than `m` to at most `m`.

A triple meeting both components would contain two points from one component
and one from the other.  The internal pair determines either a positive-slope
line or an axis-parallel line.  It cannot be the negative-slope cross line.
Axis-parallel lines also cannot meet both rectangles because their old and new
coordinate ranges are disjoint.  Therefore no cross-component triple exists.
Together with the internal hypotheses, this proves the claim. ∎

## 3. Exact matching-reservoir patch

Choose offsets `A,B` such that the two coordinate sets

\[
 C_A
 =
 \{A+Lj^2,A+Lj^2+d:0\le j<t\},
\]

\[
 Y_B
 =
 \{B+Lj^2,B+Lj^2+d:0\le j<t\}
\]

lie in `[m]`.

Let `S subseteq [m]^2` be saturated and no-three-in-line.  A **parabolic
matching reservoir** is a set `D subseteq S` of `2t` points such that every
column in `C_A` and every row in `Y_B` occurs exactly once in `D`.  Equivalently,
`D` is a perfect matching between those old coordinate sets.

Delete `D` and insert

\[
 M=
 \{(A+Lj^2,m+1+j),(A+Lj^2+d,m+1+j):0\le j<t\},
\]

\[
 F=
 \{(m+1+j,B+Lj^2),(m+1+j,B+Lj^2+d):0\le j<t\}.
\]

Put `Q=M union F` and `X=S setminus D`.

### Theorem PP3ae -- PROVED

The parabolic matching operation has the following exact properties.

1. `X union Q` has exactly two points in every row and column of
   `[m+t]^2`.
2. `Q` has `4t` distinct points and is internally no-three-in-line.
3. The operation adds exactly `2t` net points.
4. `X union Q` is no-three-in-line if and only if:
   - no point of `Q` lies on a secant through two points of `X`;
   - no pair of points of `Q` is collinear with a point of `X`.

#### Proof

Deleting the matching creates deficit one in every coordinate of `C_A` and
`Y_B`.  The movement component restores every column of `C_A` once and gives
two points to every new row.  The refill component restores every row of `Y_B`
once and gives two points to every new column.  The two cross rectangles are
disjoint.  This proves the degree statement and distinctness.

Each component is an affine translate of the set in PP3ac or its transpose.
It is internally no-three and has positive nonaxis secants.  PP3ad excludes all
triples meeting both components.  Thus `Q` is internally no-three.

The point count changes by `4t-2t=2t`.  Since `S` and hence `X` are
no-three, every remaining possible triple has either two retained points and
one inserted point, or one retained point and two inserted points.  The two
displayed conditions exclude exactly those classes. ∎

This is a deterministic internally clean PP3 interface.  It removes the
candidate-only triple term entirely; the unresolved work is preparation of a
matching reservoir whose two external certificate classes vanish or can be
selected away in a larger bank.

## 4. Square-root coordinate width

The largest old coordinate used by one component is

\[
 A+L(t-1)^2+d.
\]

### Corollary PP3af -- PROVED

A translated parabolic coordinate set fits in `[m]` whenever

\[
 L(t-1)^2+d\le m-1.
\]

For the smallest parameters `L=2,d=1`, every width

\[
 \boxed{
 t\le
 1+\left\lfloor\sqrt{\frac{m-2}{2}}\right\rfloor
 }
\]

fits geometrically.

This is a genuine square-root internal patch width.  It is smaller than the
one-shot width required by the currently published prime-gap exponent in PP4b,
so it does not complete the all-`n` transfer by itself.

## 5. Coarse external certificate bounds

### Proposition PP3ag -- PROVED

Let `Q` be a parabolic patch and let `X` be the retained core.

1. A line determined by two points of `X` contains at most eight points of `Q`.
2. For a fixed anchor `x in X`, the pairs of points of `Q` collinear with `x`
   form a matching on `Q` and hence number at most `2t`.

Consequently the number of external triple certificates is at most

\[
 8\binom{|X|}{2}+2t|X|.
\]

#### Proof

The patch is the union of four nondegenerate parabolic branches.  A line meets
each branch at most twice, proving the first assertion.

Because `Q` is no-three, two secant pairs through one external anchor cannot
share a point: otherwise the anchor and the shared patch point would determine
one line containing at least three patch/anchor incidences.  Thus the pairs form
a matching on the `4t` patch points and there are at most `2t` of them.  Summing
over retained pairs and retained anchors gives the displayed bound. ∎

The bound is intentionally coarse.  Its role is to show that the internal
multiscale triple population has disappeared; only retained-core incidence must
now be regularized.

## 6. Exact finite analyzer

The script

```bash
python scripts/analyze_parabolic_matching_reservoir.py \
  certificates/prime-patching-small.json --widths 2
```

searches every feasible translation, enumerates every matching reservoir, checks
saturation and internal geometry, and reports the two external certificate
classes separately.  All calculations use exact integer determinants.
