# Alternating-core layered menu incidence envelope

This note records AC5bo--AC5bs.  It composes a menu that is presented as a finite union of exact incidence layers with the reverse-load transportation and Hall-core obstruction routes already on the branch.

## Contract

Fix finite left and right sets `L,R`.  For each menu layer `i in I`, retain an exact conditioned edge set `E_i' subseteq L x R`.

For `x in L`, write

- `d_i(x)=|N_{E_i'}(x)|`;
- `m_x(y)=|{i:(x,y) in E_i'}|`;
- `omega(x)=sum_y (m_x(y)-1)_+`.

For `y in R`, let `D_i(y)=|N^-_{E_i'}(y)|` and `D_i=max_y D_i(y)`.  All layers, conditioning deletions and duplicate endpoints must be retained exactly.

## Results

### AC5bo — exact layer-union degree identity

For the union graph `E=union_i E_i'`,

`deg_E(x)=sum_i d_i(x)-omega(x)`.

Thus duplicate endpoints are the only loss when layerwise left degrees are aggregated.

### AC5bp — reverse-load aggregation

The union reverse load satisfies

`max_y deg_E^-(y) <= sum_i D_i`.

No disjointness of the right endpoints is required.

### AC5bq — conditioned minimum-degree envelope

If an unconditioned layer gives degree at least `a_i(x)` and conditioning deletes at most `b_i(x)` incident edges, then

`deg_E(x) >= sum_i (a_i(x)-b_i(x))-omega(x)`.

Taking the minimum over `x` gives one explicit forward-degree parameter `d`.

### AC5br — threshold Hall bound

Let `D=max_y deg_E^-(y)`.  For every `X subseteq L`,

`D (|X|-|N_E(X)|)_+ <= |X|(D-d)_+`.

Combined with AC5be--AC5bi, the threshold deficiencies obtained from these layered parameters bound the exact minimum endpoint cost.

### AC5bs — obstruction routing

If the resulting threshold budget fails, retain the canonical least Hall-deficient set `X`, its neighborhood and the complete missing rectangle `X x (R\N_E(X))`.  AC5bj--AC5bn then partitions that rectangle into exact obstruction classes and either pays it from the class bank or returns a named overload/reset.

## Proof

The degree identity counts every right endpoint once and subtracts all duplicate layer occurrences.  The reverse-load inequality follows because a union edge contributes to at least one layer and is counted at most once in the union.  For a nonempty `X`, edge counting gives

`d|X| <= e(X,N_E(X)) <= D|N_E(X)|`.

Rearrangement gives AC5br.  The remaining statements are direct composition with the existing threshold layer-cake and missing-rectangle routers.

## Finite audit

Run:

`python scripts/verify_ac_layered_menu_incidence.py`

The deterministic audit checks:

- 8,000 layered menu systems;
- 24,012 exact layers;
- 226,606 layer edges;
- 28,535 conditioning deletions;
- 1,823 deficient systems;
- 5,711 retained missing-rectangle incidences.

## Scope

This theorem does not prove the geometric values of the layer degrees, conditioning losses, overlap excesses or reverse loads.  It requires a complete finite layer dictionary and exact endpoint identities.  Omitted layers, unrecorded duplicate endpoints, dynamic dictionaries or nonlocal legality return reset.  AC5, AC6 and the no-three-in-line conjecture remain open.
