# Product growing-direction and second-generation repair index

This local index records the frontier after exact subpower strong-complete seeds
and fixed-family protected spread. The main switching index reaches PX175; the
results below sharpen the obstruction to polynomially growing direction
families and develop the complementary repair route. The active task ledger is
[`tracks/all-n-product-recursive-rematching-stage.md`](../tracks/all-n-product-recursive-rematching-stage.md).

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
| PX189 | Every movable endpoint family has a subset of size `Omega(sqrt(t))` whose complete candidate grid has only `O(s^4)` compatible collinear triples | PROVED | `docs/102-square-root-endpoint-thinning.md` |
| PX190 | The uniform degree-two-forbidden bank on the thinned block has only `O(s)` expected internal collateral | PROVED | `docs/102-square-root-endpoint-thinning.md` |
| PX191 | Every background anchor defines a proper line-pencil edge-colouring of the rematching graph | PROVED | `docs/103-background-anchor-rainbow-reduction.md` |
| PX192 | Two-replacement/one-background collateral is exactly the repeated-colour count across all anchor colourings | PROVED | `docs/103-background-anchor-rainbow-reduction.md` |
| PX193 | Every current anchor-colour collision is destroyed by at least `2(s-6)` executable transpositions | PROVED | `docs/104-background-rainbow-transposition-decoder.md` |
| PX194 | The background-rainbow transposition bank satisfies the exact aggregate improvement inequality | PROVED | `docs/104-background-rainbow-transposition-decoder.md` |
| PX195 | A collision-local minimum has a heavy off-matching anchor shadow, yielding a loaded line or clean star | PROVED | `docs/104-background-rainbow-transposition-decoder.md` |
| PX196 | A matching graph with forbidden degree `Delta` has at least `e^(-4Delta)t!` allowed permutations and uniform `e^(4Delta)/(t)_r` spread | PROVED | `docs/105-bounded-forbidden-matching-spread.md` |
| PX197 | Every fixed-depth recursive neutralization bank remains nonempty with an explicit spread constant | PROVED | `docs/105-bounded-forbidden-matching-spread.md` |
| PX198 | Every compatible cylinder with residual order at least `8Delta` has two-sided `e^(plus/minus 4Delta)/(t)_r` probability bounds | PROVED | `docs/105-bounded-forbidden-matching-spread.md` |
| PX199 | The bounded-forbidden spread estimate is stable under arbitrary compatible partial-matching conditioning | PROVED | `docs/105-bounded-forbidden-matching-spread.md` |
| PX200 | Forbidden maximum degree `Delta` guarantees an allowed perfect matching at the sharp threshold `t>=2Delta` | PROVED | `docs/105-bounded-forbidden-matching-spread.md` |
| PX201 | Weighted endpoint thinning simultaneously controls every rank-at-most-three support sector | PROVED | `docs/106-support-excess-thinning-and-cycle-core.md` |
| PX202 | Conditioned bounded-forbidden spread transfers support-sector counts to expected certificate load | PROVED | `docs/106-support-excess-thinning-and-cycle-core.md` |
| PX203 | The only undamped diagonal-free sectors are rematching transpositions and directed three-cycles | PROVED | `docs/106-support-excess-thinning-and-cycle-core.md` |
| PX204 | A support-sector load smaller than the guaranteed destroyed mass yields a strictly improving rematching | PROVED | `docs/106-support-excess-thinning-and-cycle-core.md` |

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

The low-syndrome repair route now has a support-sensitive, conditioning-stable
recursive decoder.

- PX183--PX184 identify the uniform-bank logarithmic barrier.
- PX185--PX190 remove the internal rank-three logarithm, either structurally on
  arithmetic blocks or universally by square-root thinning.
- PX191--PX195 identify the remaining `T_2` sector with simultaneous-rainbow
  collisions and decode every large collision-local minimum back into a loaded
  line or clean star.
- PX196--PX197 show that bounded-depth recursive neutralization remains
  executable after earlier positions are added to the forbidden set.
- PX198--PX199 show that bounded compatible exposure preserves two-sided
  fixed-rank cylinder scale on the residual bank.
- PX200 lowers the sharp executability threshold to `t>=2Delta`; quantitative
  spread still uses `t>=8Delta`.
- PX201--PX202 convert endpoint-index support excess directly into powers of the
  thinning probability, including under bounded-rank conditioning.
- PX203 shows that only transposition pairs and directed three-cycles avoid this
  power saving; the transposition contribution is already bounded by selected
  line occupancy.
- PX204 gives the exact destroyed-mass versus support-load improvement criterion.

The next obligation is now quantitative rather than organizational: bound the
support-two rank-one load, the support-three/support-four rank-two loads, and the
support-excess rank-three loads along one decoder generation strongly enough to
apply PX204 twice. An absolute recursion depth or monotone generational potential
is still open, and no exact infinite product closure is claimed yet.
