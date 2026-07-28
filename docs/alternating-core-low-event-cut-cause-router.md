# Cause localization for low-event AC5 Hall cuts

**Branch:** `research/alternating-core-chain`

AC5ag--AC5aj identify the exact min-cost protected-safe flow and show that failure returns one endpoint-cost threshold together with a Hall-deficient flawed-state set. This note turns that cut into a finite physical cause overload whenever the complete restricted menu has balanced candidate degree.

## Threshold-bad candidate incidences

Fix a batch size `t`, endpoint cost `c_t`, and one threshold `1<=k<=C_t`. Let

`B_<k={b:c_t(b)<k}`.

Let `X subseteq A` be a flawed-state set and put

`N_k(X)=N(X) intersect B_<k`,

`delta_k(X)=(|X|-|N_k(X)|)_+`.

Assume the **balanced complete-candidate contract** at this threshold:

1. every `a in X` has exactly `d>=1` labelled candidate incidences in the complete menu;
2. every output state receives at most `d` such candidate incidences from `X`;
3. a candidate incidence is **good** only when its operation is physically legal and its endpoint lies in `B_<k`;
4. every candidate incidence which is not good has one least exact threshold-bad address from a finite dictionary `P_k`;
5. an address records whether the endpoint has cost at least `k` or which physical legality, blocker, ownership, context, pool, boundary or event field fails;
6. aliases are aggregated only after the operation and threshold fields are fixed;
7. missing fields or changed candidate laws are named failures or outer resets.

Write `K_k=|P_k|`. For `p in P_k`, let `L_(k,p)(X)` be the number of candidate incidences from `X` with address `p`. These are threshold-incidence loads; the same physical operation may have different addresses at different thresholds.

## AC5ak -- Hall deficiency forces threshold-bad incidence -- PROVED

For every `X subseteq A`,

`sum_(p in P_k)L_(k,p)(X)>=d delta_k(X)`.

### Proof

The complete candidate stock leaving `X` has size `d|X|`. Every good incidence ends in `N_k(X)`, and each state in that neighbourhood receives at most `d` candidate incidences. Hence there are at most `d|N_k(X)|` good incidences. The remaining threshold-bad stock is at least

`d|X|-d|N_k(X)|=d(|X|-|N_k(X)|)`

when the latter is positive, and the displayed inequality follows after taking the positive part. QED.

## AC5al -- one exact bad cause carries the cut -- PROVED

If `delta_k(X)>0`, one exact threshold-bad address satisfies

`L_(k,p)(X)>=ceil(d delta_k(X)/K_k)`.

In particular, for the cut returned by AC5aj,

`L_(k,p)(X)>=d t|A|/(C_t K_k)`

for one threshold/address pair, up to the integer ceiling.

### Proof

Pigeonhole the AC5ak load over the `K_k` exact addresses. AC5aj supplies `delta_k(X)>=t|A|/C_t`. QED.

The selected load is an operation-incidence demand through one cause. It is not automatically distinct certificate weight.

## AC5am -- threshold-capacity criterion -- PROVED

Suppose every threshold-bad address `p in P_k` has a certified capacity `gamma_(k,p)` on candidate incidences from any cut. Then

`delta_k<=d^(-1) sum_(p in P_k)gamma_(k,p)`,

where `delta_k` is the maximum low-event Hall deficiency at threshold `k`.

### Proof

Choose a set attaining `delta_k`. AC5ak gives `d delta_k` threshold-bad incidences, while the capacity assumptions bound their total by `sum_p gamma_(k,p)`. QED.

A capacity violation returns the exact threshold, cause address, excess load and complete operation field.

## AC5an -- global safe-flow criterion from cause capacities -- PROVED

If

`sum_(k=1)^C_t sum_(p in P_k) gamma_(k,p)<d t|A|`,

then

`sum_(k=1)^C_t delta_k<t|A|`,

so AC5ah gives one protected-safe state with `N_high=0` and `N_cur<=t-1`.

The same statement holds for the multistep endpoint cost and its threshold dictionaries.

### Proof

Sum AC5am over the thresholds and divide by `d`. Apply AC5ah, or AC5ai for the multistep cost. QED.

## AC5ao -- low-event cut/cause router -- PROVED UNDER THE DECLARED CONTRACTS

Every restricted-menu AC5 flow has one continuation:

1. the total threshold-cause capacity is below `d t|A|`, giving a protected-safe state or path;
2. one threshold/address capacity is exceeded;
3. one failed-flow Hall cut returns an exact threshold-bad cause with load at least `d t|A|/(C_t K_k)`;
4. or one balanced-degree, candidate-completeness, endpoint-cost, operation, blocker, ownership, context, event-inventory or boundary field fails.

Thus a failed sublevel Hall expansion no longer remains an abstract cut. It is localized to one high-event or physical blocker address with an explicit candidate-incidence load.

## Corrected AC5 frontier

Restricted-menu flow now has an exact geometric failure object: a low-event Hall cut forces a finite threshold/cause overload, and certified total cause capacity proves the desired protected-safe flow directly.

The remaining work is to bound those cause capacities for pivot, BDA, RI, target and petal menus, or pay the returned high-event/blocker atom through alternate switches, current factors, tickets or pool depletion.

## Finite check

`scripts/verify_ac_low_event_cut_cause_router.py` enumerates small balanced labelled switching menus, endpoint costs and blocked operations. It checks the `d delta` bad-incidence bound, exact cause concentration, threshold-capacity inequality and the summed safe-flow criterion.
