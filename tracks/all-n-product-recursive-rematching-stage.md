# All-n product track: bounded-depth recursive rematching stage

**Branch:** `research/all-n-product-construction`

This stage continues the low-syndrome repair route after PX183--PX195. Uniform
endpoint rematching has unavoidable logarithmic internal collateral, but
arithmetic rematching and square-root thinning remove that rank-three loss.
The remaining mixed collateral is organized by the number of endpoint indices
used by each matching certificate.

The exact reduction is now sharper: endpoint-index support beyond matching rank
pays an additional power of the thinning probability. Under square-root
thinning, the rank-two support-two sector is constant-scale, support three is
linear in the new block order, and only support four can remain superlinear.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Internal rematching collateral | **CONTROLLED** | PX185--PX190 give arithmetic `O(t)` collateral or universal `O(s)` collateral after square-root thinning. |
| Background collision encoding | **COMPLETE** | PX191--PX192 identify the mixed `T_2` sector with repeated colours in proper line-pencil colourings. |
| Collision decoder | **COMPLETE** | PX193--PX195 give aggregate transposition descent and extract a loaded line or clean star at every large local minimum. |
| Recursive bank existence | **COMPLETE AT FIXED DEPTH** | PX196--PX197 give an explicit spread family after adding all earlier replacement positions to the forbidden graph. |
| Conditioning stability | **COMPLETE** | PX198--PX199 give two-sided cylinder estimates and preserve spread under compatible bounded-rank exposure. |
| Sharp executability | **COMPLETE** | PX200 proves the optimal general threshold `t>=2Delta` for an allowed replacement matching. |
| Support-sensitive thinning | **COMPLETE** | PX201--PX202 give simultaneous weighted sector thinning and conditioned certificate-load transfer. |
| Short-cycle core | **CLASSIFIED** | PX203 proves that only rematching transpositions and directed three-cycles avoid support-excess decay. |
| Improvement endpoint | **COMPLETE CONDITIONALLY ON LOADS** | PX204 converts any support-sector load bound below guaranteed destroyed mass into a strict improvement. |
| Rank-two support three | **CONTROLLED** | PX205--PX206 identify directed two-paths and bound their thinned contribution linearly under bounded line occupancy. |
| Rank-two support four | **OPEN / UNIQUE SUPERLINEAR SECTOR** | Two disjoint source-to-target arcs can still contribute on the original `t` scale. |
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

### 4. Support-sector thinning

A rank-`r` replacement certificate uses between `r` and `2r` endpoint indices.
If it uses `u` indices, independent endpoint thinning with probability `q`
retains it with probability exactly `q^u`. PX201 chooses one block of order at
least `qt/2` while simultaneously keeping every weighted rank-at-most-three
support sector within sixteen times this expectation.

PX202 combines that thinning with PX198--PX199. Relative to ordinary rank-`r`
matching scale, a support-`u` family gains

\[
q^{u-r}.
\]

This gain survives compatible bounded-rank conditioning.

### 5. Short-cycle classification

Because every recursive bank forbids the current endpoint positions, diagonal
candidate cells are absent. PX203 then gives the exact minimal-support sectors:

- rank one has no support-one sector;
- rank-two support two is exactly a transposition pair;
- rank-three support three is exactly a directed three-cycle.

For square-root thinning, every other sector gains at least `t^(-1/2)`. If
selected-line occupancy is at most `L_Z`, the undamped rank-two transposition
core has expected contribution at most

\[
128e^{4\Delta}L_Z.
\]

### 6. Rank-two support paths

PX205 classifies every diagonal-free rank-two certificate as one of:

1. a directed two-cycle on two endpoint indices;
2. a directed path on three endpoint indices;
3. two directed arcs from a two-element source set to its disjoint two-element
   target set.

The exact pattern counts are

\[
\binom t2,
\qquad
t(t-1)(t-2),
\qquad
12\binom t4.
\]

Under line occupancy `L_Z`, PX206 converts these into expected square-root-thinned
loads of orders

\[
O(L_Z),
\qquad
O(L_Zs),
\qquad
O(L_Zs^2),
\]

respectively, where `s=Theta(sqrt(t))`. Thus support four is the unique
rank-two sector that can remain superlinear in the new block size.

### 7. Improvement criterion

PX204 states the exact endpoint needed for termination. If every bank state
destroys at least `D_*` old certificates and

\[
e^{4\Delta}
\sum_{r=1}^3\sum_{u=r}^{2r}
\frac{W_{r,u}(J)}{(s)_r}
<D_*,
\]

then one allowed matching strictly lowers the total potential. The same
criterion holds after bounded-rank conditioning.

## Remaining proof tasks

1. **Rank-two support-four bound.** Prove `W_(2,4)=O(t^3)` after the PX195
   loaded-line/clean-star extraction, or identify the exact obstruction to that
   estimate.
2. **Support-four decoder.** If `W_(2,4)>>t^3`, extract a common anchor pencil,
   endpoint-disjoint star, biclique, or bounded-support batch that can be
   neutralized recursively.
3. **Rank-one support-two bound.** Control the weighted number of one-replacement,
   two-background certificates strongly enough that `W_(1,2)/t^(3/2)` is below
   the destroyed-mass scale.
4. **Rank-three support-excess constants.** Insert the known geometric counts from
   PX189 into PX202 with constants compatible with the guaranteed destruction.
5. **Spread constant sharpening.** Replace the crude `e^(4Delta)` bound for the
   actual union-of-few-partial-matchings forbidden graphs, especially when
   `Delta=2` or `3`.
6. **Depth-two mass accounting.** Combine the sector estimates with PX194 and
   PX204 to show that two generations destroy more old certificate mass than they
   create.
7. **Extraction persistence.** Prove that the clean star or loaded line extracted
   at generation two retains enough endpoint-disjoint mass after generation-one
   forbidden positions are imposed.
8. **Generational potential.** Charge newly created `T_2` collisions to a strictly
   smaller reservoir of anchors, directions, support sectors, or endpoint cycles.
9. **Closure conversion.** Insert a terminating recursive decoder into the
   universal `O(n log n)` product seed PX63 without losing factor transport or
   exact row-column saturation.

The immediate mathematical target is now item 1 or item 2. The support-three
subproblem is no longer an asymptotic barrier; the only potentially superlinear
rank-two certificates use four distinct endpoint indices.

## Verification

```bash
python scripts/verify_product_bounded_forbidden_spread.py
python scripts/verify_product_support_excess_thinning.py
python scripts/verify_product_rank_two_support.py
```

The new verifiers exhaust the relevant rank-at-most-three and rank-two partial
matching spaces, check exact support classifications and counts, verify Bernoulli
support scaling and weighted allowed-bank load transfer, and check the
square-root sector inequalities.

The classical no-three-in-line conjecture and infinite product closure remain
open.
