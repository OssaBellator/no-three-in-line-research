# All-n product track: mixed-sector decoder and nested-depth stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`tracks/all-n-product-causal-sign-stage.md`](all-n-product-causal-sign-stage.md).
PX249--PX255 extract and execute the coordinate-star two-block move. PX256--
PX262 decode every mixed rank-at-most-three sector back to a loaded line or
clean star. PX263--PX266 show that the recursive endpoint blocks can be chosen
nested and reach a polylogarithmic terminal core in `O(log log N)` generations
with only subpower cumulative spread loss. PX267--PX269 sharpen the actual
first-generation two-layer bank to an essentially `e^2` cylinder factor.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Coordinate heavy-cell field | **DECODED STRUCTURALLY** | PX249--PX252 give a Hall rectangle, compatible heavy centres, overlap extraction, and an executable two-block skeleton. |
| Dependent two-block spread | **COMPLETE** | PX253--PX255 give product cylinders and a causal mixed-collateral ledger without assuming independence. |
| Mixed `(1,1)` sector | **DECODED** | PX256--PX259 give a two-bank transposition inequality and local-minimum loaded-line/clean-star extraction. |
| Mixed `(2,1)` and `(1,2)` sectors | **DECODED** | PX260--PX262 reduce them to the one-block rainbow decoder with the opposite matching as anchor set. |
| Nested recursive extraction | **COMPLETE FOR PX195 OUTPUTS** | PX263 proves later endpoint blocks can be selected inside the current block. |
| Quantitative recursion depth | **LOG-LOGARITHMIC** | PX264--PX265 give exact-order adaptive thinning and `O(log log N)` depth to a polylogarithmic terminal core. |
| Cumulative spread | **SUBPOWER** | PX266 gives total loss `exp(O((log log N)^2))=N^o(1)`. |
| Actual first-generation degree-two bank | **SHARPENED** | PX267--PX269 give one-point trimming and cylinder factor `(1-2/s)^(-s)=e^(2+o(1))`. |
| Strict recursive sign | **OPEN** | Mixed sectors decode structurally, but amortized destruction versus recreation is not yet globally negative. |
| Terminal-core absorption | **OPEN** | The polylogarithmic final block has no universal exact absorber yet. |
| Infinite exact closure | **OPEN** | No all-side doubling theorem follows yet. |

## Immediate frontier

1. Prove a strict-sign-or-child theorem: every nonterminal clean-star, radial,
   coordinate-field, or mixed-shadow state either improves immediately or
   produces the next nested block with a charged reduction in a multiscale
   potential.
2. Construct a universal absorber for the terminal
   `O(Delta_0+log log N)` block.
3. Apply the causal packet ledger in the remaining
   `t<=N^(1/2+o(1))` diffuse-defect range.
4. Assemble the nested decoder into the PX63 product seed.

The probability theory no longer requires an absolute recursion depth. The
remaining obstruction is an amortized geometric sign and the terminal core.

## Verification

```bash
python scripts/verify_product_coordinate_star_field.py
python scripts/verify_product_coupled_two_block_spread.py
python scripts/verify_product_two_block_rainbow_decoder.py
python scripts/verify_product_mixed_rank_three_decoder.py
python scripts/verify_product_nested_recursion_depth.py
python scripts/verify_product_two_layer_regular_spread.py
```

The classical no-three-in-line conjecture and exact infinite product closure
remain open.
