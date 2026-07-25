# Alternating-core payment for one-sided BDA scalar fronts

**Branch:** `research/alternating-core-chain`

BDA5ae--BDA5ah replace the former dispersed-anchor inequality by an exact pair/endpoint/variation router on the interlaced scalar paths. This note imports that result into the alternating-core BDA adapter. Endpoint slots and oriented `q`-step deficits inherit disjoint paid buckets from the exact AC profile, so their reopening payment is automatic and their remaining conflict problem is scope-complete rather than arithmetic.

## Setup

Retain one exact paid-faithful AC3an profile

$$
\pi=(q,d,e,\xi)
$$

with canonical scalar slots

$$
h_j=h_0+jm,
\qquad
q=gm,
$$

and aggregated weights `w_{P,j}` from AC3ao. Put

$$
S=\sum_P\sum_j w_{P,j}.
$$

The aggregation partitions the underlying paid AC records by exact anchor and scale. Hence distinct slots have disjoint paid buckets.

## AC3du -- exact AC pair/front trichotomy -- PROVED FROM BDA5ae--BDA5ah

For every `0<=theta<=1`, one exact paid-faithful profile returns one of:

1. **Co-anchored pair bank:** a radially slot-disjoint family of genuine `h,h+q` pairs carrying paid weight at least
   $$
   \boxed{\theta S/2.}
   $$
2. **Endpoint front:** a family of distinct extreme scalar slots carrying paid weight greater than
   $$
   \boxed{(1-\theta)S/2.}
   $$
3. **Oriented variation front:** a parity-selected slot-disjoint family of exact one-sided `q`-partner deficits carrying paid excess greater than
   $$
   \boxed{(1-\theta)S/4.}
   $$

Every endpoint record retains an anchor `P`, scale `h`, path residue and missing outward direction. Every variation record retains

$$
(P,h,\pm,q,e_{P,h}),
$$

where `e_{P,h}>0` is paid current mass unmatched at the adjacent scale `h+q` or `h-q`. All original denominator, direction, scalar-residue, role and affine decorations are preserved.

### Proof

AC3ao supplies exactly the weighted interlaced paths used by BDA5ae--BDA5ah, with no loss of paid weight. Apply BDA5af and BDA5ag. QED.

## AC3dv -- private slot-bucket payment -- PROVED

In either one-sided output of AC3du, give every selected record the paid bucket of its occupied scalar slot as a private resource.

- Endpoint slots are distinct.
- The selected variation parity uses every scalar slot at most once.

Therefore the selected paid buckets are pairwise disjoint. For any finite record subfamily `X`, the union of its private resources has exactly `|X|` capacity-one labels after aggregation, or exactly the sum of the integer multiplicity capacities before aggregation. Thus the AC3f capacitated Hall inequalities hold with equality.

A selected endpoint or oriented-front record can pay at most one reopening from its private slot bucket. Reappearance of the same anchor/scale/profile record is an explicit support-reuse event and must consume an additional finite ticket or return to a terminal carry/BDA/RI label.

### Proof

The slot aggregation in AC3ao is a partition of the paid occurrence family. AC3du's endpoint extraction uses distinct vertices, and its parity-selected variation extraction uses each path vertex at most once. Hence no selected records share an underlying paid bucket. The Hall statement is the same singleton-resource identity as AC3do. QED.

## AC3dw -- scope-complete one-sided-front router -- PROVED

Let a selected endpoint or oriented-front family have total paid weight `W_front`. Build the full AC3v conflict graph on the corresponding formal missing-partner objects. Its edges include:

- row, column, cell and replacement overlap;
- private paid-set overlap;
- every potential factor meeting two or more front objects;
- feasibility and protected-bank constraints;
- opposite-layer and nonadditive collateral interactions.

Because AC3dv gives private disjoint payment, AC2c implies that for every `K>=1` one of the following holds.

1. **Labelled paid overload:** one front object has closed-neighbourhood paid load greater than `K` times its own weight, and AC2d localizes the overload to one finite arithmetic/support label.
2. **Privately paid compatible front bank:** an independent family carries paid weight at least
   $$
   \boxed{W_{front}/K,}
   $$
   with exact additive payment and collateral under AC3v.

The compatible family retains explicit formal partner scales. It is therefore ready for one of three geometric conclusions: install the missing radial partner, prove strict effective-denominator descent, or return a support-faithfulness failure with one exact anchor/scale/direction profile.

### Proof

Apply AC2c to the scope-complete weighted conflict graph. AC3dv supplies disjoint private paid resources, and AC3v supplies exact additivity on independent sets. QED.

## AC3dx -- quantitative composition with AC3am -- PROVED

Suppose an AC3am denominator role of paid weight `W_x` reaches one exact BDA profile with

$$
S\ge\frac{W_x}{2R\rho L},
$$

using the notation of AC3ar. Choose `theta=1/2`. Before the full scoped-conflict loss, one of the following has paid weight at least:

$$
\boxed{
\frac{W_x}{8R\rho L}
}
$$

for a genuine pair bank,

$$
\boxed{
\frac{W_x}{8R\rho L}
}
$$

for an endpoint front, or

$$
\boxed{
\frac{W_x}{16R\rho L}
}
$$

for an oriented variation front.

After applying AC3dw with parameter `K`, the endpoint and variation outputs yield a compatible privately paid bank at the corresponding bound divided by `K`, unless a labelled paid overload occurs.

The factor `rho` is omitted in the fixed-exclusion and repeated-residual-pair cases exactly as in AC3ar.

### Proof

Substitute the AC3ar lower bound for `S` into the `theta=1/2` constants of AC3du, then apply AC3dw. QED.

## Consequence

The ordinary and reflected BDA adapters no longer end at a numerical dispersed-anchor inequality. At one exact scalar profile they now return:

- an executable candidate `h,h+q` pair family, still subject to support faithfulness;
- a privately paid family of extreme scalar records;
- or a privately paid family of oriented missing-partner records.

The remaining BDA geometry is installation/descent for these explicit fronts, support faithfulness for the true pair family, the five affine heavy-load chains, and higher-rank collateral. Payment eligibility for the one-sided scalar front is closed.

## Finite check

`scripts/verify_ac_bda_one_sided_fronts.py` checks the `theta=1/2` composition constants, endpoint and parity-slot disjointness, singleton Hall payment, and the weighted AC2c compatible-bank router on exhaustive small abstract front systems.
