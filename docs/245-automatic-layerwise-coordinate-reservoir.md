# Layerwise square-root coordinate reservoirs are automatic

PP3asl--PP3ass reduce a non-co-layered target package to one marked block `D_a` in
each of the two permutation layers of a saturated source.  PP3ast--PP3asz remove
active-controller density from the helper preparation.  The only remaining
coordinate hypothesis was that layer `a` contain `Theta(|D_a|^2)` unreserved
indices.

At the slab scale this is automatic under every standard `o(m)` reservation.  The
largest possible layerwise helper demand is `O(W^2)=O(R)`, while

```text
R=m^(19/20+o(1))=o(m).
```

Thus a layer can fail only when a genuinely global condition reserves
`(1-o(1))m` of its coordinates.  Moderate coordinate erosion cannot be terminal.

## 1. Scale separation

Use

```text
R=m^(19/20+o(1)),
W=sqrt(R)=m^(19/40+o(1)).
```

### Proposition PP3ata -- PROVED

For every `s<=W` and fixed constant `C>0`,

```text
C s^2 <= C R = o(m).
```

#### Proof

The displayed exponent gives `R/m=m^(-1/20+o(1))->0`. ∎

The constant `C` absorbs the finite restriction to a convenient square-root host
and any bounded duplication of helper roles.

## 2. One-layer reservoir theorem

Let one permutation layer have index set `[m]`.  Let `B` be the indices unavailable
for genuinely global reasons: previously committed endpoints, external reservations,
fixed boundary coordinates, or other restrictions that are not represented inside
the joint local support hypergraph.

### Theorem PP3atb -- PROVED

Fix `C>0` and a marked block of size `s<=W`.  If

```text
|B|=o(m),
```

then for all sufficiently large `m` there is an unreserved set

```text
H subseteq [m]\(B union D)
```

with

```text
|H| >= C s^2.
```

#### Proof

The available set has size at least `m-o(m)-W=(1-o(1))m`.  By PP3ata,
`Cs^2=o(m)`. ∎

No controller-disjointness condition is imposed; selected controller helpers are
punctured afterwards by PP3asu--PP3asx.

## 3. Exact failure certificate

### Corollary PP3atc -- PROVED

If a layer with marked block `D`, `|D|=s<=W`, does not contain `Cs^2` unreserved
indices, then

```text
|B| > m-|D|-Cs^2
     = (1-o(1))m.
```

Thus helper shortage is an explicit near-complete coordinate-cover obstruction.

#### Proof

The complement of `B union D` has size below `Cs^2`; rearrange and apply PP3ata. ∎

The theorem distinguishes genuine reservation from local inadmissibility.  Local
source, transition, anchor, endpoint, and insertion restrictions belong in
`K_blind`; dense failure there produces a canonical target structure rather than
being charged to `B`.

## 4. Two-layer simultaneous preparation

Let the saturated source layers be `P_0,P_1`, and partition a marked set as

```text
D=D_0 dot-union D_1,
s_a=|D_a|,
s=s_0+s_1<=W.
```

Let `B_a` be the genuinely global reserved indices in layer `a`.

### Theorem PP3atd -- PROVED

If `|B_0|,|B_1|=o(m)`, then for every fixed `C>0` there are layerwise helper
reservoirs `H_0,H_1` satisfying

```text
|H_a|>=C max(s_a^2,1)
```

for every occupied layer.  Their total requested size satisfies

```text
sum_a |H_a| = O(s_0^2+s_1^2+1)=O(s^2)=O(R)=o(m).
```

#### Proof

Apply PP3atb in each occupied layer and PP3asm to the total demand.  The layers are
edge-disjoint, so their helper choices do not conflict. ∎

For bounded nonempty blocks the constant `1` supplies the finite complete-support
host.

## 5. Adaptive layerwise packages

Within one complete insertion-cancellation package, helper indices used by an
earlier layer trade may be added to the reserved set of a later trade.

### Proposition PP3ate -- PROVED

For a bounded number of layerwise trades moving total marked size `s<=W`, all
indices committed inside the package have total size `O(s)`.  Adding them to every
later reserved set preserves the hypothesis `|B_a|=o(m)` and does not affect
PP3atd.

#### Proof

Each strictly alternating trade uses at most one helper per marked cell, up to a
bounded finite-host padding for blocks of size at most two.  Hence the package uses
`O(s)=O(W)=o(m)` indices. ∎

This permits the zero-cost layer cycles to be selected sequentially against the
actual current source.

## 6. Automatic standard second-host theorem

### Theorem PP3atf -- PROVED / CONDITIONAL GLOBAL RESERVATION INTERFACE

For a target endpoint package of size `s<=W` in the saturated two-layer architecture,
assume only:

1. every local source, transition, anchor, distinguished-endpoint, endpoint-edge,
   and insertion condition has the finite joint normal form;
2. the genuinely global reserved-coordinate set in each occupied layer is `o(m)`;
3. puncturing `O(W)` selected controllers preserves the fixed positive allocation
   margin.

Then the layerwise critical helper reservoirs exist automatically.  Consequently the
package has one of:

1. a sequence of zero-cost layer cycles giving complete insertion cancellation;
2. a canonical converted structure of target order;
3. a genuinely global near-complete coordinate cover in one occupied layer;
4. a global condition outside the finite local normal form;
5. failure of the two-layer endpoint replacement architecture.

#### Proof

Use PP3atd--PP3ate for the reservoirs, PP3asy in each layer, and PP3asq for the
composite payment. ∎

## 7. Revised coordinate frontier

### Corollary PP3atg -- PROVED

Shortage of a `Theta(s_a^2)` helper reservoir is no longer an independent moderate-
density obstruction.  It is exactly one of:

1. a near-complete global coordinate cover of size `(1-o(1))m` in an occupied layer;
2. a target-size local support structure extracted from the joint rank-three table;
3. failure of the saturated two-layer endpoint architecture.

Under standard `o(m)` reservations, helper coordinates are automatic even when the
marked set is split between layers and every available helper is initially a
controller.

The no-three-in-line conjecture remains unproved.
