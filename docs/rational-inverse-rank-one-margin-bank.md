# Margin-filtered completion bank after rank-one decomposition

**Branch:** `research/rational-inverse-expansion`

RI5v writes the new rank-one active collateral exactly as a sum of component-local costs. This note uses that additivity to remove the original rank-one obstruction whenever its total cost is below the assigned paid weight.

## Local margins

For completion component `i`, retain:

- assigned paid weight `W_i`, guaranteed destroyed when the component is toggled to its target state;
- rank-one active collateral weight `R_i`, occurring exactly when that component is toggled to its target state.

Put

$$
W=sum_i W_i,\qquad R=sum_i R_i,
$$

and define the favorable component set

$$
I_+={i:W_i>R_i}.
$$

Its total positive margin is

$$
G=sum_{i in I_+}(W_i-R_i).
$$

## RI5y -- positive-margin product bank -- PROVED

Freeze every component outside `I_+` in its current state. Toggle the components in `I_+` independently and uniformly.

The expected assigned paid destruction minus the expected original rank-one active collateral is at least

$$
G/2.
$$

Moreover,

$$
G >= max(0,W-R).
$$

Hence whenever `W>R`, the filtered bank retains guaranteed expected paid-minus-rank-one margin at least

$$
(W-R)/2.
$$

### Proof

A favorable component is in its target state with probability `1/2`. Its assigned paid certificates then contribute expected destruction at least `W_i/2`, while RI5v gives exact expected rank-one cost `R_i/2`. Frozen components contribute neither assigned destruction nor original rank-one cost. Summing gives `G/2`.

The sum of the positive parts of the numbers `W_i-R_i` is at least their total sum `W-R`, and is nonnegative. QED.

## Residual active ranks

Consider a new active collateral triple not belonging to the original rank-one family already charged through the `R_i`.

If the triple prescribes a target state on any frozen component, it never occurs. Otherwise let `s(T)` be the number of prescribed favorable bits. Every occurring residual new triple satisfies

$$
1<=s(T)<=3.
$$

Its exact occurrence probability in the filtered bank is

$$
2^{-s(T)}.
$$

### Proof

Frozen current prescriptions are automatic, frozen target prescriptions are impossible, and every prescribed favorable bit fixes one independent fair toggle. If `s(T)=0`, every selected component cell used by the triple is current or common, while all outside cells are fixed current cells. The triple would then be contained in the original current matching, contradicting newness. A triple has only three cells, so `s(T)<=3`. QED.

## Conditional blocker repair

For every filtered active state, repair the blocker layer with the existing trichotomy:

1. no occupied active target cells: leave the blocker layer unchanged;
2. exactly one: use the RI5l auxiliary-transposition bank;
3. at least two: use the RI5h fixed-point-free replacement bank.

Thus every filtered active state has a valid conditional blocker menu.

## RI5z -- margin-filtered collateral criterion -- PROVED

Move every state-independent term into `F`. Let `H_s` be the exact expected residual active collateral from triples with filtered rank `s`, for `1<=s<=3`, using probability `2^{-s}`. Let `B_+` be the exact conditional blocker-repair average over the filtered cube.

If

$$
G/2 > F+H_1+H_2+H_3+B_+,
$$

then one filtered toggle-and-repair state strictly lowers the paid potential.

In particular, when `W>R`, the stronger but easier-to-check sufficient condition

$$
(W-R)/2 > F+H_1+H_2+H_3+B_+
$$

also gives an improving state.

If `G/2>F` but the first criterion fails, then at least one of

$$
H_1,\ H_2,\ H_3,\ B_+
$$

is at least

$$
(G/2-F)/4.
$$

### Proof

RI5y supplies expected paid-minus-original-rank-one margin `G/2`. The residual active terms have the exact filtered probabilities above, and `B_+` is the exact conditional blocker average. Negative expected drift gives an improving joint state.

The lower-bound version uses `G>=W-R`. Failure of the first criterion gives

$$
H_1+H_2+H_3+B_+ >= G/2-F,
$$

so one of the four nonnegative terms carries at least one quarter. QED.

## Complete rank-one dichotomy

The active rank-one frontier now has two exits.

1. **Rank-one dominant:** `R>=W`. Apply RI5x to obtain a heavy one-target or two-target hyperbola profile, a poor component ratio, or quantitative component spread.
2. **Paid dominant:** `W>R`. Apply RI5y--RI5z. The original rank-one term is absorbed into positive local margins, and any remaining failure lies in a residual filtered rank-one interaction, rank two, rank three, or the explicit blocker-repair average.

The residual `H_1` term is not an original one-component certificate: it arises only when a formerly higher-rank triple loses frozen current prescriptions. Its full original rank and frozen-bit word remain available as a finite profile label.

## Interface to RI6

RI5u no longer needs to carry the original active rank-one term indefinitely. Either that term already dominates the paid assignment and is geometrically localized by RI5x, or it is removed by the margin-filtered bank. The next active-layer frontier is therefore the finite classification of residual rank-one shadows and genuine rank-two/rank-three interactions.

## Finite check

`scripts/verify_rational_rank_one_margin_bank.py` exhausts small paid/collateral vectors, favorable subsets, all toggle states, and all compatible prescription words of size at most three. It verifies the expected local margin, the bound `G>=max(0,W-R)`, exact filtered occurrence probabilities, impossibility of new rank-zero residuals, and the four-way failure router.