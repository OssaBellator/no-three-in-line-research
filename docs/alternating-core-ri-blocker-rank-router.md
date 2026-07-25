# Created-cell rank for crossed-blocker complexes

**Branch:** `research/alternating-core-chain`

AC3cp--AC3ct classify every selected blocker prescription by one of nine path/cycle types, exact rectangle anchors, crossed cells and all-I6 product laws. The remaining frontier was previously phrased as payment for a crossed-cell tuple or closure-star output. These are blocker collateral profiles of the already paid closed I6 bank. The correct immediate invariant is their pre-transition current/new word and created-cell rank.

## Crossed positions and current context

Fix the pre-transition two-layer union `M`. A blocker collateral triple in AC3ct contains:

- `a` crossed cells `z_ij`, where `1<=a<=3`;
- `3-a` unchanged blocker context cells.

The unchanged context cells belong to `M`. A crossed cell is absent from the old blocker matching, but it may coincide with a cell of the old active layer; therefore it must be tested against the full initial union rather than declared new automatically.

Order the crossed positions by the retained partial-permutation arc order and define

$$
\epsilon_r=\mathbf 1_{\{z_r\notin M\}},
\qquad 1\le r\le a.
$$

## AC3fm -- exact crossed-cell membership word -- PROVED

For a genuinely created blocker collateral triple,

$$
\boxed{
(\epsilon_1,\ldots,\epsilon_a)
\in
\{0,1\}^a\setminus\{0^a\}.
}
$$

Its pre-transition created-cell rank is

$$
\boxed{
\operatorname{nrk}_M(T)=\epsilon_1+\cdots+\epsilon_a.
}
$$

For fixed crossed count `a`, there are exactly

$$
\boxed{2^a-1}
$$

possible words: one for `a=1`, three for `a=2`, and seven for `a=3`.

### Proof

The noncrossed cells are unchanged blocker context and hence lie in `M`. Membership of each crossed physical cell in `M` is fixed. If every crossed cell also belonged to `M`, all three cells of the triple were present before the repair and the triple was not newly created. The rank identity follows from the definition. QED.

## AC3fn -- eleven-state crossed-count/word localization -- PROVED

Let one exact blocker arc/anchor-kind/arithmetic profile have raw collateral weight `S`. The joint label consists of the crossed count `a` and one nonzero word in `\{0,1\}^a`. The number of joint labels is exactly

$$
\sum_{a=1}^3(2^a-1)=1+3+7=11.
$$

Therefore one exact crossed-count/current-new word carries raw weight at least

$$
\boxed{S/11}
$$

and has created-cell rank one, two or three.

For a fixed crossed count class of weight `S_a`, one word carries at least

$$
\boxed{
\frac{S_a}{2^a-1}.
}
$$

Under the large-blocker output of AC3ct, one joint rank profile has raw weight at least

$$
\boxed{
\frac{(t)_sG}{1188\,2^{2s}L}
}
$$

because `1188=108*11`. With the exact sharp derangement probability, the corresponding bound is

$$
\boxed{
\frac{G}{396\,p_{t,s}^{\rm sharp}\,2^{2s}L}
}
$$

because `396=36*11`.

### Proof

The eleven joint labels partition the profile, so weighted pigeonhole gives `S/11`. Substitute the two AC3ct profile bounds. The within-count statement is the same argument on the `2^a-1` words. QED.

When `a=1`, the output is one crossed-cell completion literal against a current blocker pair. When `a=2`, it is a crossed-pair secant through one current context cell. When `a=3`, it is an all-new crossed-cell tuple.

## AC3fo -- product-law preservation and corrected payment -- PROVED

The AC3cr path and cycle identities depend only on the exact physical crossed cells and their anchors. Refining a blocker profile by crossed count and current/new word leaves every identity unchanged.

Thus:

1. an all-I6 path still satisfies
   $$
   \prod \mu_{i_ri_{r+1}}
   =
   \left(\prod \lambda_{i_{r+1}}\right)
   \frac{x_{i_0}}{x_{i_k}};
   $$
2. an all-I6 cycle still satisfies
   $$
   \prod \mu_{i_ri_{r+1}}=\prod\lambda_{i_r};
   $$
3. a profile containing a closure anchor enters the AC3fe--AC3fh fixed-term rank interface with its exact crossed-rectangle provenance;
4. no crossed-cell tuple or closure path is assigned payment merely for being explicit collateral;
5. payment and ticketing begin only when a later legal transition identifies a current certificate it destroys.

### Proof

The current/new refinement records initial membership and does not alter any coordinate, arc, anchor or product parameter, so AC3cr remains literal. The payment statement follows from the same AC3f accounting used in AC3fh and AC3fl: AC3bh has already charged the blocker collateral against the original fixed-edge bank, while recording the failed profile performs no transition. QED.

## Consequence

Every heavy blocker output now retains:

- one of nine arc graph types;
- one exact anchor-kind word;
- one crossed count `a`;
- one nonzero current/new word;
- created-cell rank one, two or three;
- one affine direction and offset;
- every exact all-I6 path/cycle product law;
- every closure boundary-path address when a closure anchor occurs.

The remaining blocker frontier is arithmetic termination of rank-one crossed-cell contexts, rank-two crossed secants and rank-three crossed tuples, plus their finite AC2d overload labels. “Closure-star payment” and “crossed-tuple payment” are no longer open lemmas at the collateral-classification stage.

## Finite check

`scripts/verify_ac_ri_blocker_rank_router.py` enumerates crossed counts one through three, all eleven joint current/new labels, verifies the rank map, exhausts bounded eleven-bin weighted ledgers, and checks the constants `1188` and `396`.
