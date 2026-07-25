# Exact direction-protection versus spread census

PX176--PX178 prove that affine packets obstruct rank-three spread in
cyclotomic constructions.  This chapter records the corresponding exact finite
picture in the full strong-complete state space, without assuming cyclotomic
structure.

For a permutation \(f:\mathbb F_p\to\mathbb F_p\), let

\[
Z(f)=
\left\{
c\in\mathbb F_p:
\text{the graph of }f\text{ has no secant of slope }c
\right\}.
\]

Equivalently,

\[
c\in Z(f)
\quad\Longleftrightarrow\quad
x\longmapsto f(x)-cx
\text{ is a permutation}.
\]

Every strong-complete map has

\[
\{0,1,-1\}\subseteq Z(f).
\]

Thus \(|Z(f)|-3\) is the number of additional finite directions protected by
that seed.

The graph has \(p\) points and never determines the vertical direction.  Hence
it determines exactly

\[
p-|Z(f)|
\]

projective directions.  The Rédei--Megyesi theorem states that a noncollinear
\(p\)-point set in \(AG(2,p)\) determines at least

\[
\frac{p+3}{2}
\]

directions.  Therefore every nonlinear permutation satisfies

\[
|Z(f)|\le\frac{p-3}{2}.
\]

## Theorem PX179 -- PROVED FINITE

Among the \(4,524\) strong-complete mappings of order thirteen, the exact joint
census of omitted finite slopes and affine-triangle multiplicity is

| \(|Z(f)|\) | \(	au(f)\) | Number of maps |
|---:|---:|---:|
| 3 | 8 | 2,028 |
| 5 | 24 | 1,352 |
| 3 | 48 | 1,014 |
| 12 | 156 | 130 |

The last row is exactly the affine family.  Every nonlinear map with additional
protected directions lies in the second row.  It determines

\[
13-5=8=\frac{13+3}{2}
\]

directions and is therefore direction-minimal in the Rédei--Megyesi theorem.

In particular, at the first nonlinear order:

- the best-spread seeds, with \(	au=8\), protect no direction beyond
  \(0,1,-1\);
- protecting two additional finite slopes raises the exact triangle maximum to
  \(24\);
- maximal direction omission and good rank-three spread do not coexist.

### Proof

Enumerate all strong-complete mappings by exact-cover backtracking.  For each
mapping, enumerate all ordered graph secants and all PX129 affine-triangle
shapes.  The four displayed populations exhaust all \(4,524\) maps.  The affine
subfamily has size

\[
p(p-3)=13\cdot10=130,
\]

so the final row is exactly affine.  Every nonlinear map in the second row has
five omitted finite slopes, hence eight determined directions, attaining the
Rédei--Megyesi lower bound. \(\square\)

## Theorem PX180 -- PROVED FINITE

The order-seventeen permutation

\[
\begin{aligned}
f_{17}={}&(0,12,7,5,14,2,9,16,6,13,1,10,8,3,15,4,11)
\end{aligned}
\]

is strong complete and satisfies

\[
\boxed{
Z(f_{17})=\{0,1,2,3,8,11,16\},
\qquad
\tau(f_{17})=40.
}
\]

It protects four additional finite slopes and determines

\[
17-7=10=\frac{17+3}{2}
\]

directions.  Thus it is again direction-minimal.

The order-seventeen unprotected seeds from PX132 can have

\[
\tau=6.
\]

Consequently the first explicit seed with several additional protected slopes
has a triangle maximum more than six times larger.

### Proof

Direct enumeration verifies that

\[
f_{17},
\qquad x-f_{17}(x),
\qquad x+f_{17}(x)
\]

are permutations.  Exact secant enumeration gives the displayed omitted set,
and exact affine-triangle enumeration gives maximum \(40\).  The map is
nonlinear, and the direction count attains the Rédei--Megyesi lower bound.
\(\square\)

## 3. Interpretation

PX179--PX180 do not prove that every growing protected family forces large
triangle multiplicity.  They identify the first two exact regimes where extra
direction protection occurs, and both are extremal Rédei-type configurations
with substantially worse spread.

Together with PX176--PX178, the evidence points to a three-way distinction.

1. **Pseudorandom seeds:** small \(	au\), but typically only the mandatory
   omitted slopes.
2. **Direction-minimal seeds:** omit about half the slopes, but contain strong
   affine packet structure and have much larger \(	au\).
3. **Required missing regime:** omit a prescribed polynomially smaller set of
   low directions while remaining globally pseudorandom.

The third regime is precisely what PX175 requires and what current finite-field
constructions do not yet supply.

## External input

The direction lower bound used to identify extremality is the
Rédei--Megyesi theorem: a noncollinear \(p\)-point subset of
\(AG(2,p)\) determines at least \((p+3)/2\) directions.  A modern short proof is
Gábor Somlai, *A new proof of Rédei's theorem on the number of directions*,
Archiv der Mathematik 122 (2024), 461--466; arXiv:2212.12823.

## Verification

Run

```bash
python scripts/verify_product_direction_spread_census.py
```

The verifier exhausts all order-thirteen strong-complete mappings, reproduces
the four-row census, and checks the order-seventeen certificate exactly.
