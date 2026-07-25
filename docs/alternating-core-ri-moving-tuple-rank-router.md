# Current/new word router for RI moving channel tuples

**Branch:** `research/alternating-core-chain`

AC3bt--AC3cb reduce source-rank-two and source-rank-three active collateral to a finite moving-cell multiplicity alphabet and, on one heavy affine line, to at most four moving pairs, two repeated-channel triples, or eight three-channel triples. A moving position is state-dependent, but its realized physical cell need not automatically be absent from the pre-transition union. Likewise, the fixed cell in the `(1,1;N)` word may be an unchanged current context cell or a new RI closure cell. This note performs the exact pre-transition membership split and converts every heavy quadratic tuple into created-cell rank one, two or three.

## Position words

Fix the pre-transition two-layer union `M`. For one realized compatible active triple

$$
T=\{z_1,z_2,z_3\},
$$

define its current/new word

$$
\epsilon(T)=(\epsilon_1,\epsilon_2,\epsilon_3),
\qquad
\epsilon_i=\mathbf 1_{\{z_i\notin M\}}.
$$

Positions are ordered by the retained multiplicity word and channel tuple. In `(1,1;N)`, the third position is the fixed cell `N`.

## AC3fi -- seven-word membership alphabet -- PROVED

Every genuinely created triple has

$$
\boxed{
\epsilon(T)\in\{0,1\}^3\setminus\{(0,0,0)\}.
}
$$

Its created-cell rank is exactly

$$
\boxed{
\operatorname{nrk}_M(T)=\epsilon_1+\epsilon_2+\epsilon_3.
}
$$

Thus there are exactly seven possible current/new words, grouped into three rank-one words, three rank-two words and one rank-three word.

### Proof

Membership of each realized physical cell in the fixed initial union `M` is deterministic. A created triple cannot have all three cells in `M`, because then it was already present before the transition. The rank identity is the definition of AC3fa. The Hamming-weight counts are `binom(3,1)=3`, `binom(3,2)=3` and `binom(3,3)=1`. QED.

No assumption is made that an I6 moving position is new. The split records the actual physical membership.

## AC3fj -- quantitative membership localization -- PROVED

Let one exact source-coset/channel/multiplicity profile have raw candidate weight `S`. Partition its represented created triples by the seven words of AC3fi. One word has raw weight at least

$$
\boxed{S/7.}
$$

Consequently one created-cell rank has raw weight at least `S/3`, while one exact rank and position word has weight at least `S/7`.

Applied to AC3bx:

1. a selected source-rank-two channel/multiplicity class has one current/new word of raw weight at least
   $$
   \boxed{
   \frac{G}{84(m)_2}
   };
   $$
2. a selected source-rank-three channel tuple has one current/new word of raw weight at least
   $$
   \boxed{
   \frac{G}{28(m)_3}
   }.
   $$

The source-rank-two bound is uniform over all three multiplicity words. For the `(1,1;N)` word it safely includes both possibilities for the fixed position `N`.

### Proof

The seven words partition the created triples in the exact profile, so weighted pigeonhole gives `S/7`. AC3bx supplies `S>=G/(12(m)_2)` in source rank two and `S>=G/(4(m)_3)` in source rank three. QED.

## AC3fk -- heavy-line quadratic tuple outputs become rank outputs -- PROVED

Fix one exact affine line and one channel-tuple/multiplicity class of line weight `R`.

### Two moving cells and one fixed incidence

For `(1,1;N)`, AC3bv gives at most four ordered moving pairs. One moving pair therefore carries weight at least `R/4`, and one current/new word within that moving-pair/context-incidence family carries at least

$$
\boxed{R/28.}
$$

The selected word gives one of:

- rank one: one new moving or fixed cell with a current context pair;
- rank two: one exact pair of new cells with one current context cell;
- rank three: two new moving cells together with one new fixed closure cell.

The exact fixed-cell address remains an incidence parameter on the selected line; no false finite bound on the number of possible context cells is asserted.

### Repeated-channel moving triples

For `(2,1)` or `(1,2)`, AC3bv gives at most two exact moving triples. One exact triple and one current/new word carry at least

$$
\boxed{R/14.}
$$

The repeated-channel pair retains its exact symmetric secant address.

### Three-channel moving triples

For `(1,1,1)`, AC3bv gives at most eight exact moving triples. One exact triple and one current/new word carry at least

$$
\boxed{R/56.}
$$

In every case the output is now an AC3fa rank-one context, rank-two secant/two-arm record, or rank-three all-new literal tuple with the full quadratic-root branch word attached.

### Proof

Apply the finite moving-pair/triple multiplicities of AC3bv and then the seven-word split of AC3fi. QED.

## AC3fl -- corrected quadratic-tuple payment interpretation -- PROVED

A heavy moving pair, repeated-channel secant or exact quadratic-root triple returned by a failed I6 comparison is created collateral, not automatically a destroyed current-defect resource. Its current/new word determines which cells were already present and which were introduced by the I6 state.

Therefore:

1. no payment is assigned merely because the tuple lies on an exact line or quadratic branch;
2. the tuple is charged against the original fixed-edge bank in the failed expectation comparison;
3. a later transition intended to remove the tuple must identify an actual current certificate destroyed by that later move;
4. ticketing begins only when that executable later transition is selected.

### Proof

AC3bh already accounts for certified fixed-edge destruction and expected active collateral. The line/channel classification refines the collateral event but performs no state transition. In particular, a moving pair by itself is not a current collinear triple, and an all-new tuple has no pre-transition current certificate to charge. AC3f forbids treating either object as payment without a later destroyed-resource map. QED.

## Consequence

The active rank-two/rank-three RI frontier no longer asks for “payment of a quadratic tuple.” Every output has:

- one exact source/channel/multiplicity profile;
- one line or quadratic root branch word;
- one exact nonzero current/new word;
- one created-cell rank in `{1,2,3}`;
- full physical, scale, carry and repeated-channel secant data.

The remaining work is termination of the resulting rank-one context families, rank-two secants and rank-three all-new tuples, plus dense AC2d overload labels. Payment is required only for an eventual executable transition removing such a profile.

## Finite check

`scripts/verify_ac_ri_moving_tuple_rank_router.py` enumerates all three-position current/new words, verifies the rank counts, checks weighted seven-way localization, and verifies the constants `1/84`, `1/28`, `1/28`, `1/14` and `1/56` used above.
