# Alternating-core delegation to rational-inverse completion

**Branch:** `research/alternating-core-chain`

This note gives a generic normalized-to-physical adapter for quotient-labelled paid objects which are genuinely destroyed by physical completion components. It remains useful for movable collateral or debt-payment objects.

Canonical paid OP4g root factors follow a different route. AC3bf proves their hyperbola root cells are fixed by completion, so they enter the closed-completion I6 bank of AC3bg--AC3bj rather than AC3ax.

## RI-realized alternating records

Fix a prime `p`, nonzero hyperbola parameters `a,b`,

$$
r=b/a,
$$

and a multiplicative subgroup `H` of order `h`. Let one normalized order-two quotient component use at most four source cosets

$$
U_1H,\ldots,U_mH,
\qquad 1\le m\le4.
$$

A weighted alternating-core record is **arithmetically RI-realized** when it carries:

- the normalized quotient component and one complete fixed-edge fibre;
- the exact root and image labels used by the rational map `F_r`;
- the actual base-scale cosets represented by witnesses of both roots;
- one current paid weight `w`;
- every finite AC role label which must survive the delegation;
- when available, a one-target affine address `(e,O)` or two-target secant address `(x+y,xy)`.

For root coset `A=cH`, image coset `C=F_r(c)H`, and base-scale coset `S=xH`, the physical column cosets are

$$
xH=S,
\qquad uH=CS,
\qquad zH=AS.
$$

A complete fibre is **scale coherent** when the two root witness sets contain one common base-scale coset. A weighted family is **scale faithful** when every coherent record has one chosen common scale at which its paid weight is supported by actual physical witnesses.

After a scale `S` is fixed, define

$$
X_S=\bigcup_{\alpha=1}^m U_\alpha S,
$$

and

$$
T_S=\{(x,a/x):x\in X_S\}.
$$

A generic paid object is **component payable** when it can be assigned to one actual RI5f completion component whose target state removes that object. The assignment is faithful when every paid portion is assigned once and the full RI5 active/blocker event audit contains every resulting collateral event.

This condition is deliberately separate from quotient and scale realization. Canonical current hyperbola-root factors are not component payable; AC3bf is the exact obstruction.

## AC3at -- weighted scale-coherence router -- PROVED

Let a fixed normalized quotient role have total paid weight `W`. Partition complete fibres into scale-incoherent and scale-coherent records, with weights `W_mis` and `W_coh`.

One of the following holds.

1. **Paid scale mismatch:**
   $$
   W_mis\ge W/2.
   $$
2. **Coherent paid half:**
   $$
   W_coh>W/2.
   $$

On the coherent side, choose one common scale for every record. If `k` scale classes occur, one carries at least `W_coh/k`. For every threshold `K>=1`, either more than `K` scales occur or one class carries more than `W/(2K)`. Under a scale-atom cap `beta_s`, either one class exceeds `beta_s` or more than `W/(2beta_s)` scales occur.

### Proof

The mismatch and coherent weights partition `W`. The scale classes partition the coherent weight. Apply weighted pigeonhole. QED.

## AC3au -- exact physical coset realization -- PROVED

Fix one selected scale `S`. Multiplication by `S` is a bijection on `F_p^*/H`. Therefore:

1. the `m` normalized source cosets remain `m` distinct physical cosets `U_alpha S`;
2. every witness has physical source, partner, and anchor cosets
   $$
   S,\qquad CS,\qquad AS;
   $$
3. `X_S` has exactly `mh` columns and `T_S` uses exactly the row block `aX_S^{-1}`.

For physical anchor or partner weights of total `P` and column cap `beta`, either one column exceeds `beta` or at least `P/beta` distinct columns occur.

### Proof

Coset multiplication is invertible, and `u=F_r(c)x`, `z=cx`. The load statement is weighted pigeonhole. QED.

## AC3av -- completion-debt and occupancy router -- PROVED FROM RI5f--RI5l

Fix a physical scale, current active permutation `M_0`, blocker permutation `M_1`, and proposed block `X_S`. RI5f decomposes the relative completion into internal cycles and boundary paths. Closing every boundary path by its RI5h closure cell gives row-column-disjoint closed components.

For any nonnegative weights assigned to the components, of total `P`, either:

1. internal cycles carry at least `P/2`; or
2. one of `b` boundary paths carries more than `P/(2b)`.

If every component atom is capped by `beta`, the heavy path has length greater than `P/(2b beta)`.

Every selected union is occupancy-installable in two layers:

- zero desired blocker cells: install directly;
- at least two: use the RI5h derangement;
- exactly one: use the RI5l auxiliary transposition.

### Proof

The component and weighted alternatives are RI5f--RI5g. RI5h closes boundary paths and handles zero/multiple blockers; RI5l handles the singleton. QED.

## AC3aw -- finite decorated RI profile localization -- PROVED

Let a scale-localized physical family have paid weight `P`, and let an exact profile map use `L` values. One profile carries weight at least

$$
P/L.
$$

The profile may record component type, quotient label, scale, carry word, blocker occupancy, affine address, or secant data. If a component-toggle comparison fails, RI5ac--RI5ae refine it to one of thirteen component words and one of two geometries.

### Proof

Weighted pigeonhole, followed by the proved RI terminal router. QED.

## AC3ax -- generic movable AC3am-to-RI delegation -- PROVED UNDER HYPOTHESES

Let an AC3am common-residual family have weight `W_x`. Assume:

1. at most `R` arithmetic role labels;
2. secondary threshold `rho>=1`;
3. the selected role is arithmetically and scale faithfully RI-realized;
4. its selected paid objects are component payable with a faithful one-component assignment;
5. at most `K` physical scales occur;
6. an exact decoration alphabet has size `L`.

Then one of the following occurs:

1. paid scale mismatch of weight at least `W_x/(4Rrho)`;
2. more than `K` physical scales;
3. one physical decorated component-payable class of weight at least
   $$
   \boxed{W_x/(4Rrho K L)},
   $$
   which enters RI5s--RI5ae.

The factor `rho` is omitted in the fixed-exclusion and repeated-pair outcomes.

### Proof

AC3am loses at most `2Rrho`. AC3at loses at most two to the coherent side and at most `K` to one scale. AC3aw loses at most `L`. The component-payable hypothesis supplies the RI5s paid assignment. QED.

## Correct interface discipline

There are now two distinct physical RI routes.

1. **Generic movable payment:** use AC3ax and the component-toggle bank.
2. **Canonical current OP root payment:** use AC3be and AC3bf--AC3bj. The paid roots are fixed by completion; every I6 state is installed directly through one common closure.

No normalized quotient role is declared terminal before its scale and physical audit, and no fixed current hyperbola root is incorrectly charged to a completion component.

## Finite check

`scripts/verify_ac_ri_delegation.py` checks the scale router, physical coset identities, completion-debt decomposition, closure, blocker occupancy, and generic quantitative loss. The canonical correction and closed bank are checked independently by `scripts/verify_ac_ri_closed_fixed_edge.py`.
