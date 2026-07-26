# The slab architecture cannot create a near-complete coordinate cover

PP3atc--PP3atg identify failure of a quadratic helper reservoir with a reserved set
of size `(1-o(1))m`.  The prime-patching architecture itself never creates such a
cover.

The only macroscopic old-coordinate commitment is the union of the `M` slab pools.
Its density is `ab+o(1)` with the fixed design condition `ab<1`.  Actual selected
patch endpoints, marked cells, helper cells, punctured controllers, new-label
coordinates and adaptive package commitments are all `o(m)`.  Hence every current
permutation layer retains a fixed positive fraction of its indices, while a target
helper host needs only `O(W^2)=O(R)=o(m)` indices.

## 1. Macroscopic slab reservation

Use the slab parameters

```text
M=floor(a m^(1/20)),
R=floor(b m^(19/20)),
ab<1.
```

Let `C_1,...,C_M` be the disjoint old-column slab intervals used for the matching
pools.

### Proposition PP3auj -- PROVED

The complete slab-coordinate reservation satisfies

```text
|C_1 union ... union C_M|=MR=(ab+o(1))m.
```

Consequently its complement has size

```text
(1-ab-o(1))m=Theta(m).
```

#### Proof

This is PP3gr.  The fixed inequality `ab<1` gives a positive limiting complement. ∎

The same statement holds for the transposed row-slab architecture.

## 2. All other internal commitments are sublinear

Let `B_small` contain every old index unavailable for one current repair package
outside the slab union, including:

1. marked endpoint indices and previously chosen helpers inside the package;
2. selected controller punctures;
3. actual macro endpoints selected from the pools;
4. boundary or new-label bookkeeping that reserves old indices;
5. the `O(W)` indices used by one fresh-helper epoch; and
6. any bounded finite-host padding.

### Proposition PP3auk -- PROVED

At the slab-optimal scale,

```text
|B_small|=o(m).
```

More precisely, the named contributions have scale at most

```text
O(MW+W+q)=m^(21/40+o(1))=o(m)
```

inside one package or epoch.

#### Proof

The installed patch width is `T=MW=m^(21/40+o(1))` by PP3gr.  A target marked or
helper block has size `O(W)`, and an epoch selects `O(W)` indices by PP3atq.  Bounded
padding is negligible.  Sum the contributions. ∎

Local source, transition, anchor and insertion exclusions are not included in
`B_small`; they belong to the complete support table and either admit an independent
set or yield a canonical converted structure.

## 3. Automatic reservoir under the actual reservation census

Put

```text
B_int=(C_1 union ... union C_M) union B_small.
```

### Theorem PP3aul -- PROVED

For every fixed `C>0` and every marked block of size `s<=W`, the available old-index
set satisfies

```text
|[m]\(B_int union D)|
>=
(1-ab-o(1))m
>
C s^2
```

for all sufficiently large `m`.

#### Proof

PP3auj--PP3auk give the first lower bound.  Since `s^2<=W^2=Theta(R)` and
`R=m^(19/20+o(1))=o(m)`, the fixed positive linear lower bound eventually exceeds
`Cs^2`. ∎

Thus the exact helper reservoirs required by PP3asy and PP3atf exist even if the
entire slab union is conservatively treated as unavailable.

## 4. Two-layer and adaptive compatibility

### Proposition PP3aum -- PROVED

The theorem applies simultaneously to both current permutation layers and throughout
a bounded layerwise cancellation package.  Earlier helper choices add only `O(W)`
indices to later reserved sets and do not alter the positive linear complement.

#### Proof

The reservation is by old coordinate index, so the same bound is valid in either
matching layer.  Adaptive additions are `o(m)` by PP3auk and PP3ate. ∎

Controller density remains irrelevant because selected controller helpers are
punctured after selection.

## 5. Exact internal-cover theorem

### Theorem PP3aun -- PROVED

Within the slab-optimal prime-patching architecture, failure to supply a
`Theta(s^2)` helper reservoir for some `s<=W` cannot be caused by:

1. the slab pools;
2. selected macro endpoints;
3. marked or helper cells from the current package;
4. controller punctures;
5. current-reference cascade history; or
6. any finite local source/insertion restriction.

Any such failure must add a genuinely external reservation of size

```text
(1-ab-o(1))m
```

beyond the complete internal census.

#### Proof

The first five families form `B_int` and leave the reservoir given by PP3aul.  The
sixth family is processed by the complete support dichotomy rather than coordinate
reservation.  Rearranging the failure inequality gives the displayed additional
cover. ∎

No such external reservation is part of the stated no-three-in-line patching
problem.

## 6. Automatic coordinate endpoint

### Corollary PP3auo -- PROVED

For the canonical slab architecture, near-complete coordinate cover is no longer an
internal frontier.  Every target or bounded marked endpoint package has the required
layerwise helper reservoirs automatically, including after:

1. splitting across the two current source layers;
2. selecting helpers before puncturing controllers;
3. resetting the current reference between epochs; and
4. reserving the complete slab pool union.

The only remaining coordinate-cover alternative would be an additional exogenous
rule not present in the construction.

## 7. Revised global frontier

### Corollary PP3aup -- PROVED

After PP3auj--PP3auo, the post-allocation repair architecture has no unresolved
coordinate, controller, common-layer, local-host, first-trade, insertion-payment or
historical-reference obstruction.

The concentrated frontier is the initial macro-patch allocation/completion theorem
and any genuinely different branch that does not use the controller-aware
slab-optimal random two-sided architecture.

The no-three-in-line conjecture remains unproved.
