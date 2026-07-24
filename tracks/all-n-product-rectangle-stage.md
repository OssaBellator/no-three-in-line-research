# All-n product track: rectangle matching stage

**Branch:** `research/all-n-product-construction`

This stage follows the gauge-normalization and special-closure results in
Chapters 44--45. It replaces raw arbitrary-map enumeration by a structured
conflict-free perfect-matching problem.

## Current ledger

| Item | Current status |
|---|---|
| PC1 | **COMPLETE / RECTANGLE NORMAL FORM.** Every arbitrary-map one-inner-layer state for the side-two outer factor is a perfect matching of `n` four-corner rectangles and is automatically saturated. |
| PC2 | **SUBSTANTIAL PARTIAL.** Every bad triple is exactly either a diagonal two-rectangle conflict or a transversal three-rectangle conflict. Uniform conflict-degree bounds are proved. |
| PC3 | **PARTIAL POSITIVE.** Exact templates exist at base sides 2, 4, and 5, and none exists at base side 3. Template existence remains open at bases 6, 7, and 8 in the unrestricted rectangle model. |
| PC4 | **TWO SPECIAL CLOSURES PROVED.** The template transport theorems give factor-independent products `2 x 4 -> 8` and `2 x 5 -> 10`. No infinite closure class is known. |
| PC5 | **OPEN.** The special closures and finite witnesses do not imply arithmetic coverage. |
| PC6 | **REFORMULATED.** The next resampling problem is a conflict-free perfect matching in a complete four-partite four-uniform hypergraph with explicit rank-two and rank-three conflicts. |

## Rectangle normal form

After full gauge normalization, write the three independent permutations as

\[
p=\alpha_1,
\qquad
t=\tau,
\qquad
r=\beta_1\tau.
\]

For each `u in [n]`, the selected points are all four corners of

\[
R_u=
\{X_0(u),X_1(p(u))\}
\times
\{Y_0(t(u)),Y_1(r(u))\}.
\]

PX43 proves that every arbitrary-map PX28 state is uniquely of this form and
that every triple of permutations gives such a saturated state.

PX44 proves that every collinearity is one of:

1. two opposite corners of one rectangle plus one corner of another rectangle;
2. one corner from each of three distinct rectangles.

Thus template existence is equivalent to a perfect matching in

\[
\mathcal K_n=U\times P\times T\times R
\]

avoiding explicit two-edge diagonal conflicts and three-edge transversal
conflicts.

## Uniform conflict bounds

PX45 proves that one candidate rectangle has at most

\[
16n(n-1)^2
\]

compatible diagonal-conflict partners.

PX46 proves that two compatible candidate rectangles have at most

\[
64n(n-2)^2
\]

compatible transversal-conflict completions.

For a uniformly random perfect matching, the resulting upper bounds on expected
conflicts are

\[
\frac{8n^2}{n-1}
\]

for diagonal conflicts and

\[
\frac{32}{3}\frac{n^2(n-1)}{n-2}
\]

for transversal conflicts. The latter is quadratic, so a direct first-moment
argument cannot prove an infinite closure theorem.

## Exact small boundary

The complete normalized census gives:

| Base side | Template exists? |
|---:|---|
| 2 | yes |
| 3 | no |
| 4 | yes |
| 5 | yes |
| 6 | open in unrestricted rectangle model |
| 7 | open in unrestricted rectangle model |
| 8 | open in unrestricted rectangle model |

The affine one-layer subfamily has been exhausted and is empty at bases six and
seven, but arbitrary rectangle matchings are substantially more general.

## Exact next targets

1. **Conflict-degree sharpening.** Replace the universal quadratic transversal
   codegree by typical, orientation-specific, or admissible-layer bounds small
   enough for a conflict-free matching theorem.
2. **Resampling theorem.** Adapt a spread-matching, lopsided-local-lemma, or
   entropy-compression argument to the rank-two/rank-three rectangle conflict
   system.
3. **Recursive templates.** Construct successful rectangle matchings at an
   infinite sequence of base sides; a base-eight template would make the proved
   side-four closure iterable once to side sixteen.
4. **Structured obstruction.** Convert the base-three impossibility and the
   canonical `2 x 5` unsatisfiable core into matching-theoretic certificates.
5. **Two-inner-layer extension.** Determine whether the complete four-layer
   selector has an analogous lower-dimensional matching normal form.

## Verification

```bash
python scripts/verify_product_rectangle_reduction.py
python scripts/verify_product_rectangle_conflicts.py
python scripts/verify_product_gauge_census.py
python scripts/verify_product_universal_side_four_closure.py
python scripts/verify_product_affine_side_five_closure.py
```

The overall track remains incomplete: no infinite multiplicative closure class
or arithmetic coverage theorem has been proved.
