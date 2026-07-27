# Exact prescription collapse for heavy local rank inventories

**Branch:** `research/geometric-cleaning`

GC2dw--GC2ea reduce failure of one bridge, chord or transversal neutralization to a large fixed-switch cost or one heavy rank-one, rank-two or rank-three prospective inventory. This note removes the remaining diffuse local inventory. The falling-factorial factor in GC2dz exactly cancels the number of matching prescriptions, leaving one constant-weight exact prescription and then one polynomially heavy exact certificate.

## Local inventory model

Fix one witness `v` with designated matching block of size `t>=7`, source weight `a_v`, fixed cost `f_v<a_v`, and rank inventory `T_r(v)` for one `r in {1,2,3}`.

Every listed rank-`r` prospective certificate has:

- one exact ordered prescription of `r` distinct matching cells in the moved block;
- exactly `3-r` fixed board cells outside that prescription;
- one occurrence-faithful physical certificate identity after exact aliases are aggregated.

There are at most `(t)_r` ordered matching prescriptions. After a prescription is fixed, the safe fixed-completion stocks are

`K_1=binom(N^2,2)`,

`K_2=N^2`,

`K_3=1`.

If additional lineage, label or context data create more physical identities, that least missing field is returned as an exact occurrence-address failure rather than hidden in these stocks.

## GC2eb -- matching-prescription pigeonhole -- PROVED

One exact ordered matching prescription carries prospective weight at least

`T_r(v)/(t)_r`.

### Proof

Partition the occurrence-faithful rank-`r` inventory by its ordered required matching cells. There are at most `(t)_r` classes. Weighted pigeonhole gives the bound. QED.

## GC2ec -- failed margin gives constant prescription weight -- PROVED

Suppose no local matching state gives strict descent and the single-witness matching contract holds. If `f_v<a_v`, GC2dz supplies one rank `r` satisfying

`T_r(v)>=(a_v-f_v)*(t)_r/384`.

For that rank, one exact matching prescription has weight at least

`(a_v-f_v)/384`.

### Proof

Apply GC2eb and cancel the factor `(t)_r`. QED.

This is independent of the matching-block size.

## GC2ed -- exact fixed-completion collapse -- PROVED UNDER THE PHYSICAL CERTIFICATE CONTRACT

Inside the prescription selected by GC2ec, one exact prospective certificate has weight at least

- rank one:

  `(a_v-f_v)/[384*binom(N^2,2)]`;

- rank two:

  `(a_v-f_v)/(384*N^2)`;

- rank three:

  `(a_v-f_v)/384`.

### Proof

A rank-one certificate has two fixed cells, so there are at most `binom(N^2,2)` unordered fixed pairs. A rank-two certificate has one fixed cell, giving at most `N^2` choices. A rank-three certificate has no fixed completion after its three moved cells are prescribed. Partition the selected prescription weight over these physical completions and apply weighted pigeonhole. QED.

The resulting object records its exact supporting line, moved-cell roles, fixed cells and current/prospective lineage status.

## GC2ee -- local rank-inventory router -- PROVED

Every exact bridge, chord or transversal witness has one continuation:

1. a legal local matching state with strict cleaning descent;
2. fixed-switch cost `f_v>=a_v`;
3. one exact prospective rank-one certificate of weight at least
   `(a_v-f_v)/[384*binom(N^2,2)]`;
4. one exact prospective rank-two certificate of weight at least
   `(a_v-f_v)/(384*N^2)`;
5. one exact prospective rank-three certificate of weight at least
   `(a_v-f_v)/384`;
6. or one exact matching, occurrence, lineage, label or context failure.

### Proof

Use GC2ea. In its heavy-rank branch apply GC2ec and GC2ed. All other alternatives are unchanged. QED.

Thus local failure no longer ends in an inventory indexed by all matching states. It ends in one exact physical rank-three certificate occurrence.

## GC2ef -- uniform-gap version -- PROVED

If `f_v<=(1-theta)a_v` for some `theta in (0,1]` and no local state descends, then the exact certificate returned by GC2ee has weight at least

- `theta*a_v/[384*binom(N^2,2)]` in rank one;
- `theta*a_v/(384*N^2)` in rank two;
- `theta*a_v/384` in rank three.

For a compatible family whose witnesses all satisfy this fixed-cost gap, either the product move descends by GC2dt or at least one exact witness returns one of these physical certificate addresses.

### Proof

The gap assumption gives `a_v-f_v>=theta*a_v`. Substitute into GC2ed. The family statement applies the one-witness router to any witness whose local margin fails. QED.

## Corrected GC frontier

The three heavy local rank inventories are now reduced to one exact prospective certificate with explicit weight. The remaining work is to charge or neutralize that exact certificate through current-factor payment, created-collateral lineage, GC4 recursion, high pair-codegree, or one declared global-context failure.

## Finite check

`scripts/verify_geometric_local_rank_prescription_collapse.py` samples weighted rank inventories. It checks the `(t)_r` prescription cancellation, the three fixed-completion stocks and the uniform-gap constants.
