# Occupancy decomposition of the closed RI blocker average

**Branch:** `research/alternating-core-chain`

AC3bh installs one closed-completion I6 active state and then repairs the blocker permutation conditionally. Its exact blocker term `B` mixes singleton auxiliary transpositions, small derangement tables, and large normalized derangement banks. This note separates those regimes quantitatively.

## Conditional blocker terms

Let `Omega` be the I6 state bank, with

$$
N=|Omega|=m!h^m.
$$

For `eta in Omega`, let `t_eta` be the number of active cells in the lifted state which are occupied by the current blocker layer. Let `b_eta` be the exact expected variable blocker collateral under the conditional repair menu for that active state.

State-independent blocker factors are already in `F`. If `t_eta=0`, no blocker cell moves, so its variable blocker contribution is zero.

Define

$$
B_1=\frac1N\sum_{t_eta=1}b_eta,
$$

$$
B_{2:6}=\frac1N\sum_{2\le t_eta\le6}b_eta,
$$

$$
B_{\ge7}=\frac1N\sum_{t_eta\ge7}b_eta.
$$

## AC3bk -- exact blocker-occupancy split -- PROVED

The closed-bank blocker average satisfies

$$
\boxed{B=B_1+B_{2:6}+B_{\ge7}.}
$$

Consequently, if `B>=D`, one of the three occupancy terms is at least `D/3`.

### Proof

The zero, singleton, small-multiple, and large-multiple occupancy classes partition the I6 states. The zero class has no variable blocker move. The identity follows by partitioning the exact conditional average, and the final statement is pigeonhole. QED.

## AC3bl -- singleton raw-profile amplification -- PROVED FROM RI5m--RI5r

Assume

$$
B_1\ge D.
$$

Then some I6 active state `eta` with `t_eta=1` has conditional singleton collateral

$$
b_eta\ge D.
$$

Let `T_eta` be the total raw weight of its variable crossed-cell blocker triples. RI5m gives

$$
b_eta\le\frac{T_eta}{n-1},
$$

so

$$
\boxed{T_eta\ge(n-1)D.}
$$

For any exact profile map with `L` values, one profile has raw weight at least

$$
\boxed{\frac{(n-1)D}{L}.}
$$

The profile may retain the RI5o channel type and the RI5q--RI5r primitive direction, affine offset, auxiliary column, and context pair. Hence a heavy singleton average produces one heavy exact affine-address profile or the proved direction/parallel-offset spread alternative.

### Proof

Because `B_1` is an average over all `N` I6 states, the average over its nonempty singleton subfamily is at least `B_1`; one state has conditional value at least `D`. Apply the RI5m cylinder cap and weighted pigeonhole. QED.

## AC3bm -- finite small-derangement output -- PROVED

Assume

$$
B_{2:6}\ge D.
$$

Then some active state has blocker occupancy

$$
2\le t\le6
$$

and conditional variable blocker collateral at least `D`. Its complete repair menu is one of five finite exact derangement tables.

For any exact profile map of size `L`, one profile in that state has raw candidate weight at least

$$
\boxed{D/L.}
$$

The returned profile retains `t`, the exact derangement table, blocker prescription rank, moved rows and columns, and all arithmetic labels of the corresponding active state.

### Proof

As in AC3bl, one state has conditional value at least the occupancy-class average. Expected collateral never exceeds the raw total candidate weight. A finite profile split loses at most `L`. QED.

AC3ch--AC3ck subsequently resolve the five tables into exact overlap/cycle types and give sharp rank-specific cylinder probabilities. AC3bm remains the stronger rank-unspecified raw bound; AC3ck gives the sharper exact-rank/type record.

## AC3bn -- large-derangement rank amplification -- PROVED FROM RI5j

Assume

$$
B_{\ge7}\ge D.
$$

For each large-occupancy state, split its variable blocker collateral by prescription rank `s=1,2,3`. Then some active state with occupancy `t>=7` and some rank `s` have conditional expected collateral at least

$$
D/3.
$$

The original RI5j cap gives the valid baseline

$$
T_{eta,s}\ge\frac{(t)_sD}{384},
$$

and after a profile split,

$$
\frac{(t)_sD}{384L}.
$$

AC3cl--AC3cn supersede this baseline. The exact extension formula yields the sharp probability `p_{t,s}^{sharp}` and the stronger bounds

$$
\boxed{
T_{eta,s}\ge\frac{D}{3p_{t,s}^{sharp}}
\ge\frac{(t)_sD}{9},
}
$$

and

$$
\boxed{
\text{one profile has weight at least }
\frac{D}{3p_{t,s}^{sharp}L}
\ge\frac{(t)_sD}{9L}.
}
$$

## AC3bo -- blocker output after a failed closed fixed-edge bank -- PROVED

Let

$$
G=\left(1-\frac1{mh}\right)W-F>0.
$$

If AC3bi returns the blocker alternative, then

$$
B\ge G/4.
$$

One of the following follows.

1. **Singleton affine profile.** One singleton state and one exact profile have raw weight at least
   $$
   \boxed{\frac{(n-1)G}{12L}.}
   $$
2. **Finite small derangement profile.** One state with `2<=t<=6` and one exact profile have raw weight at least
   $$
   \boxed{\frac{G}{12L}.}
   $$
   AC3ch--AC3ck additionally return an exact rank and overlap/cycle type with their sharp probability.
3. **Large normalized rank profile.** One state with `t>=7`, one rank `s<=3`, and one exact profile have raw weight at least
   $$
   \boxed{\frac{(t)_sG}{108L}.}
   $$
   The exact sharp bound is `G/(36p_{t,s}^{sharp}L)`.

### Proof

AC3bk selects one occupancy regime at loss at most three. Apply AC3bl or AC3bm in the first two cases. In the large case use AC3cn with `D=G/12`. QED.

## Frontier after AC3bk--AC3co

The blocker term is no longer a mixed conditional expectation and its probability theory is complete. It exits through exactly one of:

- the existing singleton crossed affine-address router;
- one exact small overlap/cycle prescription type;
- one exact large partial-permutation profile `(t,s,q)` with inclusion-exclusion probability.

The remaining blocker task is arithmetic classification and termination of one selected exact profile, not control of the repair bank.

## Finite check

`scripts/verify_ac_ri_blocker_average.py` checks the occupancy partition and the original baseline constants. `scripts/verify_ac_ri_small_derangements.py` exhausts the five small tables. `scripts/verify_ac_ri_derangement_extension_formula.py` checks the exact all-occupancy extension formula, sharp caps, and the improved AC3bo large-profile constant.