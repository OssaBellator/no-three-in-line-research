# Alternating-core delegation to rational-inverse completion

**Branch:** `research/alternating-core-chain`

AC3am can localize a common-residual obstruction to one quotient-labelled arithmetic role. A normalized quotient edge is not yet a physical repair object: its occurrence-dependent base scale may vary, and the full physical hyperbola block may not be installed. This note gives the exact data contract needed to enter the rational-inverse branch and composes the existing RI5e--RI5ae machinery with the AC3am weight router.

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
- every finite AC role label that must survive the delegation, including carry, phase, component type, and blocker state;
- when already available, either a one-target affine address `(e,O)` or a two-target hyperbola-secant address `(x+y,xy)`.

For a root coset `A=cH`, image coset `C=F_r(c)H`, and base-scale coset `S=xH`, the physical column cosets are

$$
xH=S,
\qquad uH=CS,
\qquad zH=AS.
$$

A complete fibre is **scale coherent** when its two root witness sets contain one common base-scale coset. A weighted family is **scale faithful** when every coherent record has one chosen common scale at which its full paid weight is supported by actual physical witnesses.

After a scale `S` is fixed, define the proposed physical source block

$$
X_S=\bigcup_{\alpha=1}^m U_\alpha S
$$

and its target hyperbola matching

$$
T_S=\{(x,a/x):x\in X_S\}.
$$

The realization is **completion faithful** when the selected paid weight can be assigned to target columns of `X_S`, without duplication, so that installing the assigned target cell neutralizes the assigned current paid object. It is **support faithful** when every completion-component incompatibility and every later active or blocker collateral event is represented in the corresponding RI5 conflict and profile audit.

These are separate conditions. A quotient label alone proves none of scale, completion, payment, or support faithfulness.

## AC3at -- weighted scale-coherence router -- PROVED

Let a fixed normalized quotient role have total paid weight `W`. Partition its complete fibres into scale-incoherent and scale-coherent records, with weights `W_mis` and `W_coh`.

Then one of the following holds.

1. **Paid scale mismatch:**
   $$
   W_mis\ge W/2.
   $$
2. **Coherent paid half:**
   $$
   W_coh>W/2.
   $$

Assume the second outcome and choose one common scale for every coherent record using scale faithfulness. Let the represented scale classes have weights

$$
W_1,\ldots,W_k,
\qquad \sum_{j=1}^k W_j=W_coh.
$$

Then:

- one scale class has weight at least `W_coh/k`;
- for every integer `K>=1`, either `k<=K` and one class has weight greater than `W/(2K)`, or more than `K` physical scale classes are represented;
- for every cap `beta_s>0`, either one scale class has weight greater than `beta_s`, or
  $$
  k\ge W_coh/beta_s>W/(2beta_s).
  $$

Thus normalized concentration produces a paid mismatch, a quantitatively heavy physical scale, or paid physical-scale dispersion.

### Proof

The mismatch and coherent weights partition `W`, so one is at least half. Under scale faithfulness, choosing one common scale partitions all coherent paid weight into the displayed scale classes. The maximum class is at least the average. If every class is capped by `beta_s`, then `W_coh<=k beta_s`. QED.

## AC3au -- exact physical coset realization -- PROVED

Fix one selected scale class `S`. Multiplication by `S` is a bijection on the quotient group `F_p^*/H`. Consequently:

1. the `m` normalized source cosets remain `m` distinct physical cosets `U_alpha S`;
2. every actual fixed-edge witness has physical source, partner, and anchor cosets given by
   $$
   S,\qquad CS,\qquad AS;
   $$
3. the proposed block `X_S` has exactly `mh` columns and its target matching uses exactly the row block `aX_S^{-1}`.

For any nonnegative witness weights of total `P` and any physical-column cap `beta_z`, either one anchor column carries weight greater than `beta_z`, or the witnesses occupy at least `P/beta_z` distinct physical anchor columns. The same alternative holds for partner columns.

### Proof

Coset multiplication by `S` is invertible, so it preserves distinctness and cardinality. The three physical quotient identities are the definitions `u=F_r(c)x` and `z=cx`. The target rows are the image of `X_S` under the bijection `x -> a/x`. The weighted load statement is the inequality `P<=beta_z N` when `N` columns each carry load at most `beta_z`. QED.

## AC3av -- completion-debt and occupancy router -- PROVED FROM RI5f--RI5l

Fix one physical scale class of paid weight `P`, current active permutation matching `M_0`, blocker permutation matching `M_1`, and proposed block `X_S`. Assume completion faithfulness assigns nonnegative target-column weights

$$
w(x),\qquad x\in X_S,
\qquad \sum_{x\in X_S}w(x)=P.
$$

Apply RI5f to `M_0` and `T_S`. The block decomposes into internal cycles and boundary paths. Let `P_cyc` be the assigned paid weight on internal cycles and let `b` be the number of boundary paths.

At least one of the following weighted outputs is available.

1. **Installable cycle mass:**
   $$
   P_cyc\ge P/2.
   $$
   These cycle targets preserve their active-layer row set exactly.
2. **Heavy boundary path:** one boundary path `Q` has
   $$
   w(Q)>P/(2b).
   $$
   If every target-column atom has weight at most `beta`, then
   $$
   |Q|>P/(2b beta).
   $$

Every chosen boundary path is closed by its RI5h closure cell. For any selected union of closed paths and internal cycles, the full active target is occupancy-installable in both permutation layers:

- zero desired blocker cells: install directly;
- at least two desired blocker cells: use the RI5h derangement;
- exactly one desired blocker cell: use the RI5l auxiliary transposition.

Hence scale-localized completion debt is never left as an abstract missing-cell set. It returns installable cycle mass, one explicit paid alternating path, or an occupancy-executable family of closed completion components. The remaining issue is the exact RI5s--RI5ae collateral comparison.

### Proof

The component and weighted alternatives are RI5f--RI5g. Closing a boundary path preserves the same active rows and columns by RI5h. RI5h handles blocker occupancy zero or at least two, and RI5l handles the singleton. QED.

## AC3aw -- finite decorated RI profile localization -- PROVED

Let a scale-localized completion family have paid weight `P`, and let

$$
sigma:\mathcal F\to\Sigma
$$

be any exact profile map with `|Sigma|=L`. The profile may record component type, quotient label, physical scale, carry word, blocker occupancy, one-target direction/offset, or two-target secant data.

Then one exact profile class carries paid weight at least

$$
\boxed{P/L}.
$$

If the RI toggle-bank comparison fails later and produces a terminal active term, RI5ac--RI5ae refine this selected class to one of thirteen component words and one of two geometries: one target cell with a context pair, or an exact two-target secant.

### Proof

The profile fibres partition the paid family. The terminal refinement is the proved RI5ac--RI5ae router. QED.

## AC3ax -- quantitative AC3am-to-RI delegation -- PROVED UNDER HYPOTHESES

Let an AC3am common-residual family have total paid weight `W_x`. Assume:

1. at most `R` arithmetic role labels;
2. secondary multiplicity threshold `rho>=1`;
3. the selected role is arithmetically RI-realized;
4. scale, completion, paid, and support faithfulness hold;
5. `K>=1` is a chosen scale-count threshold;
6. an optional exact decoration alphabet has size `L>=1`.

Then the selected quotient-role subfamily has weight at least

$$
W_role\ge W_x/(2Rrho),
$$

with the stronger bound omitting `rho` in the AC3am fixed-exclusion and repeated-pair outputs.

After AC3at, one of the following occurs.

1. **Paid physical-lift mismatch:** incoherent fibres carry at least
   $$
   W_x/(4Rrho).
   $$
2. **Paid scale dispersion:** more than `K` physical scale classes occur.
3. **One physical scale:** one scale class carries at least
   $$
   \boxed{W_x/(4Rrho K)}.
   $$
   After the optional exact profile split, one decorated class carries at least
   $$
   \boxed{W_x/(4Rrho K L)}.
   $$

On the selected physical scale, AC3au--AC3av return a heavy physical anchor or partner column, physical-column spread, installable cycle mass, a heavy boundary path, or an occupancy-executable completion-component family. If the full target block is already installed, RI5a--RI5c apply directly. Otherwise the component family enters RI5s--RI5ae with its actual collateral profile.

No normalized quotient role is declared terminal before this physical-scale and completion audit.

### Proof

AC3am loses at most `2Rrho`. AC3at loses at most another factor two when selecting the coherent half and at most `K` when selecting one scale. AC3aw loses at most `L`. AC3au and AC3av give the physical outputs. The direct bank-ready case is RI5a--RI5c; the completion case is RI5s--RI5ae. QED.

## Exact remaining geometry

The abstract quotient-to-physical adapter is complete under explicit hypotheses. For every actual AC quotient role, the remaining proof obligations are now finite and visible.

1. Identify its normalized RI component and complete fixed-edge fibres.
2. Produce actual root witness scale sets and prove scale faithfulness.
3. Preserve the current paid weight through one coherent scale choice.
4. Define a completion-faithful assignment to target columns of `X_S`.
5. Prove support faithfulness for RI component toggles, blocker repair, and terminal profiles.
6. Route the explicit scale-mismatch, scale-dispersion, heavy-column, and heavy-boundary-path outputs through AC, geometric cleaning, BDA, or orbit-phase structure.

The missing theorem is therefore role realization and collateral closure, not another quotient pigeonhole argument.

## Finite check

`scripts/verify_ac_ri_delegation.py` exhausts small weighted scale-set systems, finite scale assignments, subgroup-coset identities, completion-debt decompositions, closed boundary paths, and the quantitative `1/(4Rrho K L)` composition loss.