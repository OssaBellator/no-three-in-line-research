# Executable clean-pair products for alternating-core BDA fronts

**Branch:** `research/alternating-core-chain`

AC3ec proves that an actual positive adjacent partner with no mixed scalar collision supplies exactly the five-cell support required by BDA5a. This note removes the remaining support-faithfulness hypothesis for that branch. The occupied scalar-slot bucket supplies private payment even when the adjacent partner was not selected as paid input. After a scope-complete decoder-envelope extraction, BDA5f--BDA5g apply verbatim with zero assigned payment on the unselected partner triple.

## Clean pair records

A clean pair record retains

$$
(P,h,H,q,d,u,v),
\qquad
|H-h|=q,
$$

its five current active cells

$$
P,
\quad P+hu\,d,
\quad P+hv\,d,
\quad P+Hu\,d,
\quad P+Hv\,d,
$$

all blocker occupancies on the four cross cells, its complete role decorations, and the private paid bucket attached to the occupied scale `h` by AC3dv.

Let `Omega(R)` be the nonempty local BDA5e menu for the clean pair `R`: an empty-diagonal switch, a full-diagonal phase flip, or the coupled two-blocker derangement, according to its exact blocker pattern.

## AC3el -- clean-pair support faithfulness -- PROVED FROM AC3ec AND BDA5a--BDA5e

Every actual-clean-partner record of AC3ed is a support-faithful BDA radial pair.

1. Its five active cells are current and use five distinct rows and columns.
2. Every local state in `Omega(R)` preserves both permutation layers and their disjointness.
3. Every local state destroys the occupied paid radial triple
   $$
   T_h(P)=\{P,P+hu\,d,P+hv\,d\}.
   $$
4. The adjacent triple `T_H(P)` may be assigned paid weight zero when it was not part of the selected AC occurrence family. The BDA5a--BDA5g conclusions remain valid because every local state still destroys it geometrically.

Thus no additional ordinary or reflected support-faithfulness hypothesis is required after AC3ec has selected the actual-clean-partner class.

### Proof

AC3ec proves the exact five-cell support criterion and current membership. BDA5a--BDA5e construct a nonempty legal local decoder menu and prove that every menu state removes at least one endpoint from each radial triple. Assigning zero paid weight to `T_H(P)` changes only the destroyed-payment ledger, not legality or collateral. The private occupied-slot payment from AC3dv remains certified. QED.

## Scope-complete decoder graph

For a clean pair `R`, let `E(R)` contain:

- all five active support cells;
- all four opposite-diagonal cross cells;
- every blocker or auxiliary cell used by any state in `Omega(R)`;
- the private occupied-slot paid bucket;
- every potential-factor, protected-bank, replacement, row, column, and feasibility scope meeting the local decoder.

Build the canonical AC3v primal graph on clean pair records by cliquing every shared envelope cell, potential scope, constraint scope, or paid bucket.

## AC3em -- paid clean-pair bank or finite overload -- PROVED

Let one exact clean-pair class have total privately paid weight `W_clean`. For every real `K>=1`, one of the following holds.

1. **Scoped paid overload.** One clean pair `R` has closed-neighbourhood paid load
   $$
   \boxed{L(R)>K w_R,}
   $$
   and AC2d returns one finite decoder-envelope incidence label.
2. **Executable clean-pair bank.** An independent family `I` has
   $$
   \boxed{
   \sum_{R\in I}w_R\ge W_{clean}/K.
   }
   $$
   Its decoder envelopes and private occupied-slot buckets are disjoint. Every product choice
   $$
   \prod_{R\in I}\Omega(R)
   $$
   is a legal two-layer state, and all represented occupied paid triples are destroyed in every product state.

### Proof

Apply AC2c to the weighted canonical primal graph. In the independent outcome, AC3v gives exact legality and collateral additivity, AC3w gives private-payment additivity, and BDA5f gives the legal heterogeneous decoder product. AC3el verifies the local support contract. QED.

## AC3en -- exact one-sided paid product criterion -- PROVED FROM BDA5g

Let `I` be an executable clean-pair bank and put

$$
D=\sum_{R\in I}w_R.
$$

Choose one state uniformly and independently from every `Omega(R)`. Let `F` be state-independent new collateral. For `r=1,2,3`, let `T_r` be the exact expected weight of collateral triples meeting exactly `r` selected decoder envelopes, with the BDA5g cylinder probabilities.

Then

$$
\boxed{
\mathbb E[\text{destroyed certified payment}]=D,
}
$$

$$
\boxed{
\mathbb E[\text{created collateral}]=F+T_1+T_2+T_3.
}
$$

If

$$
\boxed{D>F+T_1+T_2+T_3,}
$$

one legal product state strictly lowers the paid triple potential.

### Proof

Every product state destroys each occupied paid triple by AC3el, and the private buckets are disjoint by AC3em, so the destroyed certified weight is exactly `D`. BDA5g gives the exact creation probabilities and expected collateral. A strict expectation gap yields one improving state. QED.

## AC3eo -- failed clean-pair product router -- PROVED

If no product state improves, then

$$
F+T_1+T_2+T_3\ge D.
$$

Therefore one of the four named terms has weight at least

$$
\boxed{D/4.}
$$

Combining AC3em with AC3eg gives the following quantitative alternatives unless a finite scoped overload occurs.

- From an endpoint-front clean class, an executable bank has paid weight at least
  $$
  \frac{W_x}{32KR\rho L},
  $$
  and a failed product returns one of `F,T1,T2,T3` with weight at least
  $$
  \boxed{
  \frac{W_x}{128KR\rho L}.
  }
  $$
- From an oriented-variation clean class, an executable bank has paid weight at least
  $$
  \frac{W_x}{64KR\rho L},
  $$
  and a failed product returns one named term with weight at least
  $$
  \boxed{
  \frac{W_x}{256KR\rho L}.
  }
  $$

Each term retains the full denominator, role, anchor, scale-pair, blocker-menu and decoder-envelope profile and enters BDA3c--BDA3e or the existing rank-one/rank-two/rank-three collateral routers.

### Proof

Failure of the strict AC3en inequality gives the four-term sum bound; weighted pigeonhole gives `D/4`. AC3em supplies the factor `1/K`, and AC3eg supplies the clean-class source bounds. QED.

## Consequence

The actual-clean-partner output is no longer conditional on support faithfulness.

- The five-cell support is exact.
- The local decoder menu is nonempty and executable.
- Occupied-side payment is private and additive.
- Heterogeneous decoder products are legal.
- Failure returns one of four exact collateral ranks with explicit paid scale.

The remaining BDA pair work is arithmetic termination of the returned `F,T1,T2,T3` profiles and their finite scoped overloads, not construction of the clean decoder support.

## Finite check

`scripts/verify_ac_bda_clean_pair_product.py` checks singleton Hall payment, weighted scope extraction on all graphs through five vertices, exact product expectations for finite local menus, one-sided paid destruction, the four-term failed-bank split, and the `1/128` and `1/256` composed constants.