# Product growing-direction and second-generation repair index

This local index records the frontier after exact subpower strong-complete seeds
and fixed-family protected spread. The main switching index reaches PX175; the
results below sharpen the obstruction to polynomially growing direction
families and redirect the complementary repair route.

| ID | Statement | Status | Location |
|---|---|---|---|
| PX174 | Every positive primitive direction has an explicit rectangle pair with `Omega(n^3/h)` transversal completions | PROVED | `docs/95-polynomial-direction-growth-necessity.md` |
| PX175 | Polynomial rectangle codegree saving requires polynomially many protected directions | PROVED | `docs/95-polynomial-direction-growth-necessity.md` |
| PX176 | An index-`d` cyclotomic seed with packet size `m=(p-1)/d` has affine-triangle multiplicity at least `(m)_3/(p-2)` | PROVED | `docs/96-cyclotomic-protection-spread-barrier.md` |
| PX177 | Subpower affine-orbit spread for a cyclotomic seed requires index at least `p^(2/3-o(1))` | PROVED | `docs/96-cyclotomic-protection-spread-barrier.md` |
| PX178 | Near-linear cyclotomic orthomorphisms can omit `m-3` linear slopes but still have rank-three constant `Omega(p^2)` | PROVED USING FEAR--WANLESS | `docs/96-cyclotomic-protection-spread-barrier.md` |
| PX179 | The complete order-thirteen direction/spread census has the exact four recorded populations | PROVED FINITE | `docs/97-direction-protection-spread-census.md` |
| PX180 | One order-seventeen direction-minimal strong seed omits seven finite slopes and has triangle multiplicity forty | PROVED FINITE | `docs/97-direction-protection-spread-census.md` |
| PX181 | Every nontrivial trade preserving `s` distinct linear colourings has support at least `s+1` | PROVED | `docs/98-protected-trade-support-barrier.md` |
| PX182 | Protecting all primitive directions through height `H` forces every exact protected trade to move `Omega(H^2)` rows | PROVED | `docs/98-protected-trade-support-barrier.md` |
| PX183 | Deleting two forbidden partial matchings from an arithmetic `t x t` block still leaves `Omega(t^4 log t)` compatible collinear triples | PROVED | `docs/99-uniform-rematching-logarithmic-barrier.md` |
| PX184 | The uniform degree-two-forbidden matching bank has expected internal collateral `Omega(t log t)` | PROVED | `docs/99-uniform-rematching-logarithmic-barrier.md` |
| PX185 | The conic permutation `g(x)=x/(x-1)` with one completed value has exactly `(p-1)/2` modular triples and line occupancy at most three | PROVED | `docs/100-arithmetic-low-collateral-rematching.md` |
| PX186 | Every prime arithmetic rematching block with degree-two forbidden positions has an avoiding matching with at most `16p` internal real triples | PROVED | `docs/100-arithmetic-low-collateral-rematching.md` |
| PX187 | The conic permutation has secant multiplicity at most `p+3` and affine-triangle multiplicity at most eight | PROVED | `docs/101-arithmetic-rematching-mixed-collateral.md` |
| PX188 | Arithmetic conic rematching has an explicit mixed-background collateral bound after forbidden-position repair | PROVED | `docs/101-arithmetic-rematching-mixed-collateral.md` |

## Current exact boundary

The direct protected route has three independent growth barriers.

1. PX175 requires a polynomially large direction family for any fixed
   polynomial transversal-codegree saving.
2. PX176--PX178 rule out bounded-index, moderately indexed, and near-linear
   cyclotomic shortcuts to that family with subpower rank-three spread.
3. PX181--PX182 prove that every exact switching or absorber which remains
   inside the protected state space must itself have polynomial support.

Therefore a successful protected construction must be globally mixed at the
same scale as the direction family.

The low-syndrome repair route has a different, now sharper boundary.

- PX183--PX184 prove that the uniform first-generation neutralization bank has
  an intrinsic logarithmic internal-collateral loss on arithmetic endpoint
  sets.
- PX185--PX188 remove that logarithm on prime arithmetic blocks and reduce the
  remaining repair inequality to averaged and maximum one-/two-point shadow
  terms.

The next viable repair theorem is an inverse-additive alternative for the
movable endpoint pairs: extract a large coupled arithmetic block and apply
PX188, or prove that additive expansion disperses the `C_1`, `C_2`, and
`Lambda_1` certificate masses enough for the original spread bank to improve.

No exact infinite product closure is claimed yet.
