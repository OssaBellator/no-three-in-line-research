# Iterative pruning of residual rank-one shadows

**Branch:** `research/rational-inverse-expansion`

RI5y freezes components with nonpositive original rank-one margin. A formerly rank-two or rank-three triple may then lose frozen-current prescriptions and appear as filtered rank one. This note proves that all such shadows can be absorbed by a finite monotone pruning procedure.

## Prescription words

For every new compatible active collateral triple `T`, record its component prescription word

$$
p(T) in {*,0,1}^k,
$$

where `*` is unprescribed, `0` requires the current state, and `1` requires the target state. The word has at most three prescribed entries.

Every new word contains at least one `1`. A word containing only `0` prescriptions would already be present in the original current matching.

Let `I` be a set of components still allowed to toggle; all components outside `I` are frozen current.

A word survives on `I` when it has no target prescription outside `I`. Its filtered rank is the number of prescribed entries inside `I`.

For `i in I`, let `L_i(I)` be the total weight of surviving words whose filtered rank is one and whose unique active prescription is `p_i=1`. These are the complete local rank-one shadows of component `i` in the `I`-bank.

## RI5aa -- monotone shadow-pruning core -- PROVED

Starting with all selected components `I_0`, define

$$
I_{t+1}={i in I_t: W_i>L_i(I_t)}.
$$

Then:

1. the sets form a descending chain and stabilize after at most `k` strict steps;
2. for `J subset I` and `i in J`,

$$
L_i(J)>=L_i(I);
$$

3. at the terminal set `I_*`, every surviving filtered rank-one word is counted in exactly one `L_i(I_*)`, and every other surviving new word has filtered rank two or three;
4. every terminal component has strictly positive local margin

$$
W_i-L_i(I_*)>0.
$$

### Proof

The definition gives `I_{t+1} subset I_t`, so stabilization takes at most one removal per strict step.

Let `J subset I` and fix `i in J`. A word counted by `L_i(I)` has the unique prescribed entry `i=1` inside `I`; every other index of `I` is unprescribed. Shrinking to `J` therefore cannot make that word impossible or increase its filtered rank. It remains local to `i`. Additional words whose removed prescriptions are current `0` may become local, so `L_i(J)>=L_i(I)`.

At a fixed point, the defining strict inequality holds for every retained component. By definition, every surviving filtered rank-one word has one unique target-prescribed component and is included in that component's local shadow cost. Any surviving uncharged new word therefore has filtered rank at least two, and at most three. QED.

## Removed components and disjoint shadow payment

Suppose component `i` is removed at stage `t`. Then

$$
W_i<=L_i(I_t).
$$

The local shadow families charged to different removed components are disjoint. A word local to `i` has `i` as its unique target prescription among all components that can still occur; it cannot later become a local word for another target component.

Consequently, if the pruning core is empty, the total assigned paid weight obeys

$$
W <= sum_{i removed at stage t} L_i(I_t),
$$

with the right side supported on disjoint component-labelled shadow families.

This is a paid structural output rather than a failed random bank.

## RI5ab -- shadow-free terminal product bank -- PROVED

Assume the terminal core `I_*` is nonempty. Freeze its complement current and toggle the core components independently and uniformly. Put

$$
G_*=sum_{i in I_*}(W_i-L_i(I_*)).
$$

Then `G_*>0`, and the expected assigned paid destruction minus all filtered rank-one active collateral is at least

$$
G_*/2.
$$

Every remaining uncharged active collateral triple has filtered rank two or three and therefore exact probability `1/4` or `1/8` according to its rank.

After conditional blocker repair, let `H_2^*`, `H_3^*`, and `B_*` be the exact residual active and blocker averages. If

$$
G_*/2>F+H_2^*+H_3^*+B_*,
$$

then one terminal-core state improves.

If `G_*/2>F` but the criterion fails, one of the three residual terms is at least

$$
(G_*/2-F)/3.
$$

### Proof

Each terminal component is targeted with probability `1/2`. Its assigned paid weight contributes at least `W_i/2`, while its complete local shadow family contributes exactly `L_i(I_*)/2`. Summing gives `G_*/2`.

RI5aa proves that every uncharged surviving active word has filtered rank two or three, so the product probabilities are exact. Conditional blocker repair is the RI5h--RI5l trichotomy. The expected-drift and three-way failure statements follow by averaging. QED.

## Interface to RI6

The active-layer completion bank now has no persistent rank-one recursion.

- An empty pruning core returns disjoint paid shadow families dominating all assigned component weight.
- A nonempty core has strictly positive local margins and no uncharged rank-one active collateral.
- Any failed terminal bank localizes only to genuine rank two, genuine rank three, or the explicit blocker-repair average.

The next active frontier is therefore the finite arithmetic classification of two-component and three-component interactions, not another rank-one decomposition.

## Finite check

`scripts/verify_rational_shadow_pruning.py` enumerates all prescription words of original rank at most three for small component sets, several complete integer weightings, and every small paid vector. It verifies monotonic local shadow costs, finite stabilization, disjoint removal charges, exact terminal expectations, absence of uncharged filtered rank one, and the three-way failure router.