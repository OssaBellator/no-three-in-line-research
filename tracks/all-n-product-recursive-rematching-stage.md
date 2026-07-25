# All-n product track: bounded-depth recursive rematching stage

**Branch:** `research/all-n-product-construction`

This stage continues the low-syndrome repair route after PX183--PX195. Uniform
endpoint rematching has unavoidable logarithmic internal collateral, but
arithmetic rematching and square-root thinning remove that rank-three loss.
The remaining two-replacement/one-background sector is an exact family of
proper-colouring collisions, and transposition descent returns every large
local minimum to the same loaded-line or clean-star geometry used by the
first-generation neutralization banks.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Internal rematching collateral | **CONTROLLED** | PX185--PX190 give arithmetic `O(t)` collateral or universal `O(s)` collateral after square-root thinning. |
| Background collision encoding | **COMPLETE** | PX191--PX192 identify the mixed `T_2` sector with repeated colours in proper line-pencil colourings. |
| Collision decoder | **COMPLETE** | PX193--PX195 give aggregate transposition descent and extract a loaded line or clean star at every large local minimum. |
| Recursive bank existence | **COMPLETE AT FIXED DEPTH** | PX196--PX197 give an explicit spread family after adding all earlier replacement positions to the forbidden graph. |
| Conditioning stability | **COMPLETE** | PX198--PX199 give two-sided cylinder estimates and preserve spread under compatible bounded-rank exposure. |
| Sharp executability | **COMPLETE** | PX200 proves the optimal general threshold `t>=2Delta` for an allowed replacement matching. |
| Absolute depth bound | **OPEN** | No proof yet shows that two or three generations always dominate accumulated collateral. |
| Infinite exact closure | **OPEN** | The recursive decoder is not yet a terminating all-side doubling theorem. |

## Completed tasks in this stage

### 1. Residual cylinder theorem

For a forbidden-position graph of maximum degree `Delta`, every compatible
rank-`r` partial matching with residual order at least `8Delta` has between

\[
e^{-4\Delta}(t-r)!
\quad\text{and}\quad
(t-r)!
\]

allowed extensions. Under the uniform allowed measure, its cylinder probability
is within an `e^(4Delta)` factor in either direction of the unrestricted scale
`1/(t)_r`.

### 2. Conditional stability

Conditioning on any extendable compatible partial matching simply deletes its
rows and columns. The residual forbidden graph has the same maximum-degree
bound, so the same spread estimate applies without multiplying constants. This
is the exact sequential-exposure statement needed for certificate accounting
inside one recursive neutralization generation.

### 3. Sharp Hall threshold

The allowed-position graph has minimum degree at least `t-Delta`. Hence
`t>=2Delta` guarantees a perfect matching by Hall's theorem. The threshold is
sharp: at `t=2Delta-1`, a forbidden `K_(Delta,Delta)` is a union of `Delta`
partial matchings and leaves `Delta` rows with only `Delta-1` allowed columns.

For recursion depth `d`, where the forbidden degree is at most `d+1`, this gives

\[
t\ge2(d+1)
\]

for mere executability and

\[
t\ge8(d+1)
\]

for the present quantitative spread theorem.

## Remaining proof tasks

1. **Depth-two mass accounting.** Combine PX190, PX194, and the PX198--PX199
   conditional cylinders to show that two generations destroy more old
   certificate mass than they create.
2. **Extraction persistence.** Prove that the clean star or loaded line extracted
   at generation two retains enough endpoint-disjoint mass after generation-one
   forbidden positions are imposed.
3. **Generational potential.** Find a potential that charges newly created
   `T_2` collisions to a strictly smaller reservoir of anchors, directions, or
   endpoint pairs.
4. **Bounded-depth dichotomy.** Prove that failure after a fixed number of
   generations forces a structured core already covered by an arithmetic bank
   or finite absorber.
5. **Closure conversion.** Insert the terminating recursive decoder into the
   universal `O(n log n)` product seed PX63 without losing factor transport or
   exact row-column saturation.

## Verification

```bash
python scripts/verify_product_bounded_forbidden_spread.py
```

The verifier checks the LLL inequalities, exact allowed matching counts,
conditioning-stable cylinder bounds at the first nontrivial thresholds, the
sharp Hall obstruction, and the two recursion-depth thresholds.

The classical no-three-in-line conjecture and infinite product closure remain
open.
