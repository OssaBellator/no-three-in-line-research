# Selected-helper puncturing removes the controller-density obstruction

PP3ari--PP3aro prepared a controller-disjoint helper reservoir by assuming that the
active-controller density of one permutation layer is bounded away from one.
PP3arp--PP3ask then used a square-root-size helper block from that reservoir.

The density hypothesis is unnecessary.  Choose the helper block first while ignoring
controller-preservation singleton constraints.  Puncture only the selected helpers
that happen to be active controllers, together with selected marked controllers.
At target scale this removes at most `2W=o(R)` controller values.  Every robust
allocation margin survives, and the active candidate universe only shrinks.

Thus even a layer of controller density one can supply a target helper block.  The
real requirement is an unreserved coordinate reservoir, not a controller-disjoint
one.

## 1. Controller-blind joint support

Let `D` be a marked set of size `s<=W` in one permutation layer and let `H` be an
unreserved ordinary index set of size `Theta(s^2)`.  The indices in `H` may all be
active controllers.

Construct a joint support hypergraph

```text
K_blind
```

from every positive local source, transition, anchor, distinguished-endpoint,
endpoint-edge, and insertion obstruction, but do **not** include the singleton rule
that merely forbids moving an active controller.  Controller preservation will be
enforced by puncturing selected controllers after the helper block is chosen.

### Proposition PP3ast -- PROVED

The hypergraph `K_blind` has rank at most three.  Every support records an actual
geometric or source/insertion obstruction, not controller membership alone.

#### Proof

This is PP3ase applied to the same strictly alternating local patterns after deleting
one artificial constraint family.  Removing a family cannot increase rank. ∎

## 2. Select first, puncture second

Let `H_0 subseteq H` be independent in `K_blind`, with `|H_0|=s`.  Put

```text
A=(D union H_0) cap E,
```

where `E` is the active-controller set in the layer.

### Proposition PP3asu -- PROVED

One has

```text
|A|<=2s<=2W.
```

After puncturing every controller value indexed by `A`:

1. every selected marked and helper index is controller-free;
2. every surviving controller outside `D union H_0` remains fixed by the strictly
   alternating cycle;
3. every candidate universe and every controller-aware safe domain only improves,
   except for the loss of at most `|A|` unavailable controller values.

#### Proof

The cardinality bound is immediate.  Apply one-controller puncture monotonicity
PP3ake and controller-domain monotonicity PP3ajm successively to the values of `A`.
Candidate entries controlled by punctured values are deleted, while all other safety
conditions can only improve after source/controller deletion. ∎

## 3. Margin survives target-scale selected puncturing

### Theorem PP3asv -- PROVED

Assume every original macro-label domain has size at least

```text
(gamma+xi)R
```

for fixed `xi>0`.  If `s<=W=sqrt(R)`, then after selected puncturing every domain has
size at least

```text
(gamma+xi)R-2W
>=
(gamma+xi/2)R
```

for all sufficiently large `R`.

Hence every balanced ownership and global label-matching certificate at margin
`gamma+xi/2` survives.

#### Proof

PP3asu loses at most `2W` values from any one domain.  Since `2W/R=2/sqrt(R)->0`,
this is below `xi R/2` for large `R`.  Certificate monotonicity is PP3ajq--PP3ajr. ∎

The same argument works for any `s=o(R)`; the square-root case has substantial
slack.

## 4. Independence survives puncturing

### Proposition PP3asw -- PROVED

After puncturing `A`, the helper set `H_0` remains free of every positive local
support represented in `K_blind`.

#### Proof

Puncturing deletes candidate entries and removes controller roles.  It cannot create
a new source-invalid, transition, anchor, endpoint-edge, or insertion signature on a
previously safe selected pattern.  Equivalently, the post-puncture positive support
hypergraph is a subhypergraph of the pre-puncture `K_blind` restricted to surviving
entries.  Since `H_0` was independent before puncturing, it remains independent. ∎

This is the selected-set analogue of retained-original domain monotonicity.

## 5. Zero-cost cycle at arbitrary controller density

### Theorem PP3asx -- PROVED / CONDITIONAL FINITE LOCAL NORMAL FORM

Suppose `K_blind` has an independent set `H_0` of size `s`.  Puncture `A` and use the
strictly alternating cycle on `D union H_0`.  Then the resulting trade:

1. moves every member of `D` and `H_0`;
2. preserves the permutation layer and saturation;
3. fixes every unpunctured active controller;
4. satisfies every encoded local source, transition, anchor, distinguished-endpoint,
   edge-host, and pool constraint;
5. is source-valid;
6. has insertion cost zero.

#### Proof

After puncturing, every selected index is controller-free by PP3asu.  Independence is
preserved by PP3asw.  Apply the fused-support cycle theorem PP3asf--PP3asg. ∎

No upper bound on the original controller density is used.

## 6. Critical dichotomy without controller-disjoint preparation

### Theorem PP3asy -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Let `|D|=s` and `|H|=Theta(s^2)`.  Exactly one of the following occurs.

1. `K_blind` has an independent `s`-set.  After puncturing at most `2s` selected
   controllers, PP3asx gives a zero-cost source-valid cycle.
2. One genuine local constraint family has `Omega(s^2)` rank-two support,
   `Omega(s^3)` rank-three support, or `Omega(s^2)` individually forbidden indices,
   and therefore yields an `Omega(s)` canonical converted structure.
3. A genuinely global condition outside the rank-three local normal form remains.
4. The layer does not contain `Theta(s^2)` unreserved indices.

#### Proof

Apply the exact square-root counting theorem PP3arr to `K_blind`.  The independent
branch is PP3asx.  Dense branches are converted by PP3art after finite type
refinement. ∎

The controller set contributes no singleton erosion because selected controllers are
punctured after selection.

## 7. Interaction with complete insertion cancellation

### Corollary PP3asz -- PROVED

In the second-cycle cancellation theorem PP3asa and its layerwise extension PP3aso,
controller density `1-o(1)`—including density one—is not an internal obstruction.
For each layer block:

1. select helpers against `K_blind`;
2. puncture only selected marked/helper controllers;
3. use the resulting zero-cost cycle;
4. charge deleted candidate entries favourably through nested-potential monotonicity
   or entrywise telescoping.

The complete first insertion table is still cancelled.  The remaining failures are:

1. shortage of unreserved coordinates at the `Theta(s_a^2)` scale;
2. a target-size converted genuine local certificate;
3. a global condition outside the finite local normal form;
4. a package not representable as layerwise endpoint replacement.

Active-controller density itself is no longer a frontier.

The no-three-in-line conjecture remains unproved.
