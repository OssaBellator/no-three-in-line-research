# Two target-disjoint direct-clean repair layers at `m=10`

`docs/351` constructs one globally injective locally coupled direct-clean policy
on all `12,786,720` optimal positive signed Hamilton states at `m=10`.  This
chapter duplicates every source and asks for two distinct clean targets per
source, with no target used by any other copy.  The resulting certificate gives
a strict predecessor-charge margin rather than mere nonamplification.

No asymptotic two-layer matching theorem is claimed.

## 1. Twofold fixed-sign matching deficit

Fix one sign mask `e`.  Duplicate every optimal positive source `(rho,e)` into
copies `(rho,e,0)` and `(rho,e,1)`.  Both copies have the same fixed-sign
adjacency to clean targets `(eta,e)`.

### Theorem PP3brh -- VERIFIED FINITELY / EXACT TWOFOLD FIXED-SIGN DEFICIT

Across all `1,024` sign fibres, the duplicated fixed-sign graph has

```text
25,573,440 source copies,
846,320,044 duplicated labelled edges.
```

Maximum fixed-sign matchings cover

```text
25,572,988 source copies,
```

leaving exactly

```text
452 unmatched copies in 226 sign fibres.
```

There are `304` original sources with only one distinct fixed-sign clean target.
These degree-one sources explain part, but not all, of the twofold deficit.

#### Verification

The checker reconstructs the complete `m=10` pair geometry and every optimal
orientation mask.  In each sign fibre it duplicates the source side, compresses
the clean target cycles, and runs Hopcroft--Karp.  The totals above are compared
with hard-coded regression values. ∎

The fixed-sign graph therefore does not itself contain two complete injective
layers, even though one layer exists in every fibre by `docs/351`.

## 2. Locally coupled augmentation

For an unmatched source copy, permit every direct-clean target whose sign change
is supported on the rotated owner triple.  If such a target is occupied, the
occupying ordinary source copy may be rerouted along its fixed-sign adjacency.

### Theorem PP3bri -- VERIFIED FINITELY / TWO TARGET-DISJOINT GLOBAL LAYERS

All `452` fixed-sign deficits can be augmented.  The completed matching covers
all `25,573,440` source copies and uses `25,573,440` distinct clean signed
targets.

The exact augmentation ledger is

```text
232 deficits enter a free locally coupled target directly,
220 deficits displace one fixed-sign source copy,
maximum augmenting-path source count = 2,
source vertices visited over all searches = 755,
target vertices visited over all searches = 7,032.
```

#### Verification

Begin with the disjoint union of the `1,024` maximum fixed-sign twofold
matchings.  Process the unmatched copies in canonical order.  An alternating
breadth-first search uses locally coupled edges from the deficit copy and
fixed-sign edges from every displaced ordinary copy.  Every search reaches a
free target after visiting at most two source vertices.  The final occupied
clean-target count is exactly twice the number of original sources. ∎

Partitioning the matched source copies by copy label produces two deterministic
repair maps.  They are individually injective, and their target images are also
disjoint from one another.

## 3. Strict half-charge consequence

### Corollary PP3brj -- PROVED / ONE-STEP HALF-CONTRACTION

Average the two deterministic repair layers with probability `1/2` each.  The
resulting direct-clean policy is row-stochastic and satisfies

```text
max_y sum_x P(x,y) <= 1/2.
```

#### Proof

Every source has one target in each layer.  Across both layers together, no
clean target is used more than once.  Hence any target column receives either
zero mass or one contribution of size `1/2`. ∎

After clean fibre regeneration and any stochastic clean-cycle heat step, the
inherited `L^infinity` density remains at most `1/2`.

This strengthens `docs/351` from an injective nonamplifying switch to a strict
finite contraction at the first nonforest size.  The remaining asymptotic task
is to construct two or more balanced injective layers uniformly throughout the
logarithmic frustration window.

Compile and run the exact certificate with

```bash
g++ -O3 -std=c++17 -Wall -Wextra -pedantic -fopenmp \
  scripts/check_m10_two_injective_repair_layers.cpp \
  -o /tmp/check_m10_two_injective_repair_layers

OMP_NUM_THREADS=12 \
  /tmp/check_m10_two_injective_repair_layers
```

The next theorem identifier after this chapter is `PP3brk`.
