# Product growing-direction theorem index

This local index records the frontier after exact subpower strong-complete seeds
and fixed-family protected spread.  The main switching index reaches PX175; the
results below sharpen the obstruction to polynomially growing direction
families.

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

## Current exact boundary

The direct protected route now has three independent growth barriers.

1. PX175 requires a polynomially large direction family for any fixed
   polynomial transversal-codegree saving.
2. PX176--PX178 rule out bounded-index, moderately indexed, and near-linear
   cyclotomic shortcuts to that family with subpower rank-three spread.
3. PX181--PX182 prove that every exact switching or absorber which remains
   inside the protected state space must itself have polynomial support.

Therefore a successful protected construction must be globally mixed at the
same scale as the direction family.  The viable forms are a growing-uniformity
exact-cover theorem, a high-index globally nonlinear algebraic family, or a
global switching/nibble process with polynomial-support moves.

The low-syndrome repair route is not subject to PX181 because its local moves
need not preserve every low direction at every intermediate state.  It is now
the main complementary route.
