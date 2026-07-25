# Quantitative composition of AC3am with the BDA adapter

**Branch:** `research/alternating-core-chain`

AC3an--AC3aq begin with one role-pure family. AC3am begins one step earlier, with a common residual literal whose blockers are split by arithmetic role and residual rank. This note composes the two routers and records the exact loss from the original common-residual weight.

## AC3ar -- common-residual denominator-role composition -- PROVED UNDER HYPOTHESES

Let `F_x` be an AC3am common-residual family of total current paid weight `W_x`. Assume:

1. there are at most `K` arithmetic role labels;
2. the selected role is a bounded-denominator role with a paid- and support-faithful BDA realization;
3. `rho>=1` is the secondary-multiplicity threshold used in AC3am;
4. the realization has denominator bound `Q` and direction-shape bound `M`.

Put

$$
L=L_{Q,M}=N_M^2\sum_{q=2}^Q q
$$

as in AC3an.

Then one exact BDA arithmetic profile has paid weight at least

$$
\boxed{
S\ge \frac{W_x}{2K\rho L}.
}
$$

More precisely:

- in the AC3am rank-one fixed-exclusion outcome, one exact profile has weight at least `W_x/(2KL)`;
- in the repeated-residual-pair outcome, one exact profile has weight at least `W_x/(2KL)`;
- in the secondary-dispersion outcome, one exact profile has weight at least `W_x/(2Krho L)`.

The selected profile then enters AC3ao--AC3aq and returns a heavy exact atom, the explicit dispersed-anchor inequality, an executable compatible BDA decoder family, or one of the five affine anchor chains.

If the denominator `q` is fixed by the role label, replace `L` by the sharper value

$$
L=qN_M^2.
$$

### Proof

AC3am first selects one role-and-rank class of weight at least `W_x/(2K)`. In the rank-one and repeated-pair outcomes no further weight loss is required. In the secondary-dispersion outcome AC3am selects pairwise-distinct secondary blocks of weight at least a `1/rho` fraction of that class. Thus in all cases a BDA-realized subfamily has weight at least `W_x/(2Krho)`, with the stronger bound omitting `rho` in the first two cases.

AC3an then selects one exact arithmetic profile at loss at most `L`. AC3ao--AC3aq give the stated outputs. QED.

## AC3as -- bounded-shape or paid large-direction output -- PROVED

Let a BDA-labelled role-pure family have total weight `W`, but do not assume a direction-shape bound in advance. For any threshold `M>=1`, exactly one of the following weighted alternatives may be selected:

1. records with
   $$
   max\{||d||_infinity,||e||_infinity\}\le M
   $$
   carry weight at least `W/2`, and AC3an applies to that subfamily with an additional factor at most two;
2. records with
   $$
   max\{||d||_infinity,||e||_infinity\}>M
   $$
   carry weight greater than `W/2`, giving a paid large-direction output.

Therefore the bounded-shape hypothesis in AC3ar is not silently assumed. At every chosen threshold it either holds on a constant fraction of the current paid mass or fails through one explicit geometric escape.

### Proof

The two classes partition the records. One has weight at least half the total. QED.

## Interface consequence

For an actual AC3am denominator role, the integration task is now ordered.

1. Apply AC3as at the shape threshold supplied by the local channel/carry geometry.
2. On the bounded-shape side, apply AC3ar and the exact BDA scalar/co-anchor router.
3. On the large-direction side, classify the paid direction growth through the existing AC carry-signature potential or geometric cleaning interface.

Thus direction shape is either quantitatively available for BDA or is itself a paid structural output. It is no longer an unrecorded premise of the delegation.

## Finite check

`scripts/verify_ac_bda_delegation.py` also checks the `1/(2Krho L)` composition loss and the bounded-shape versus large-direction weight partition on exhaustive small integer weight systems.