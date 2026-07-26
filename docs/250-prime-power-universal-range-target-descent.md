# No dirty selected owner of side at least four is terminal

CMR1158--CMR1165 attach a degree-two response bank to every active fixed target or
loaded line.  CMR1150--CMR1157 turn complete blockage of such a bank into an exact
unit-wall split.  The only scope distinction is whether the target still contains
an active residual edge or lies wholly in an already contracted fixed core.

If an active residual edge remains, move that edge in the current factor.  If all
three target edges are fixed, return to the stored lifted owner at which the
compatible core was conditioned.  Fixed-core reopening normalization then gives
reconditioning, a real lost-anchor edge, contraction, structural exit, or a
full-parent target bank.  Therefore a cycle-erased selected owner of residual side
at least four cannot be terminal while its induced minimum is dirty.

This is a universal-range descent theorem, not a completed prime-power theorem.
The descent may end in side below four, a prime-field/thin quotient base, or an
induced objective with all remaining physical conflicts stored in finite base
interfaces.

Fix one selected minimum state in a host-representable exact product with compatible
fixed core `P`.  Every physical triple of the lifted state has a unique split

\[
T=T_P\sqcup T_R,
\]

where `T_P subseteq P` and `T_R` consists of active residual labelled edges.

## 1. Target-location trichotomy

### Theorem CMR1166 -- PROVED

Every dirty physical target has exactly one of the following forms.

1. **Pure residual:** `|T_R|=3`.
2. **Anchored residual:** `1<=|T_R|<=2` and `1<=|T_P|<=2`.
3. **Fixed core:** `|T_R|=0` and `|T_P|=3`.

In the first two cases, moving any edge of `T_R` destroys the physical target.

### Proof

The two parts are disjoint and contain the three labelled realizations of the
physical target.  If a residual edge is removed, the complete three-cell target is
no longer selected. ∎

## 2. Residual targets have a current degree-two bank

### Theorem CMR1167 -- PROVED

Assume the current residual factor side is `n>=4` and `T_R` is nonempty.  Choose
`e in T_R`, lying in residual layer `ell`.  Extend `e` and the current protected
partial matching of that layer to a perfect matching `F_e` of the inherited layer
board.  Then

\[
K_{n,n}\setminus(F_e\cup M_{1-\ell})
\]

has a perfect matching.  Every corresponding joint state destroys `T`.

### Proof

The forbidden set is the union of two perfect matchings and has maximum degree at
most two.  Apply CMR128.  Every response omits `e`, so CMR1166 destroys the target.
∎

Restricted-host execution is governed by CMR1160--CMR1162.

## 3. Fixed-core targets return to their lifted owner

### Theorem CMR1168 -- PROVED

Assume `T_R` is empty.  Let `S` be the stored lifted minimum anchor at the owner
where the core containing `T` was conditioned.  At every attempted escape of `T`,
one of the following occurs.

1. `S` survives and the old core is reconditioned and recontracted.
2. A lower lifted minimum appears.
3. A labelled edge of `S` is missing and enters the finite loss stock.
4. An added edge enters the minimum core and contracts.
5. A strict factor, wall, or envelope exit occurs.
6. The lifted owner executes the degree-two target bank of CMR1158.

### Proof

Apply CMR1110--CMR1117.  When the scheduler actually tests an escape state which
moves one edge of `T`, use CMR1158 at the lifted owner. ∎

Thus a fixed target is not silently treated as movable inside a residual factor
whose endpoints have already been contracted.

## 4. Complete blockage is strict unit-wall descent

### Theorem CMR1169 -- PROVED

For either the current residual bank of CMR1167 or the lifted-owner bank of
CMR1168, if no response matching is feasible in the restricted host, then an
inclusion-minimal missing-edge cover gives an exact deficiency-one Hall wall.
Restoring one blocker edge is essential and yields the product

\[
\operatorname{PM}(G_e)
\cong
\{e\}
\times
\operatorname{PM}(G_A)
\times
\operatorname{PM}(G_B),
\qquad
 a+b=n-1.
\]

### Proof

Apply CMR1150--CMR1157 to the complete degree-two response bank. ∎

Every positive wall child has strictly smaller side.

## 5. Executable banks consume finite scheduler currency

### Theorem CMR1170 -- PROVED

If a response matching is feasible or becomes feasible after canonical host
normalization, then the target-destroying transition reaches strict improvement,
same-value target loss, robust surplus, protected growth, minimum loss,
blocker-cover update, contraction, structural exit, envelope expansion, or finite
base handling.

Every non-erased nonimproving continuation consumes one of the finite currencies
in CMR1139.

### Proof

Combine CMR1161 with CMR1136--CMR1140. ∎

## 6. No universal-range dirty terminal owner

### Theorem CMR1171 -- PROVED

A cycle-erased selected minimum owner of active residual side `n>=4` cannot be
terminal while its lifted physical minimum contains a collinear triple.

### Proof

Choose one dirty target.  If it has an active residual edge, apply CMR1167.  If it
is wholly fixed, apply CMR1168.  A feasible bank consumes scheduler currency or
improves by CMR1170.  A completely blocked bank strictly unit-wall descends by
CMR1169.  Immediate reconditioning and exact rollback are idempotent and are
absent from a cycle-erased terminal history. ∎

The theorem is about the selected canonical execution, not all parallel search
branches.

## 7. Finite strict-descent tree

### Theorem CMR1172 -- PROVED

Starting from active side `N`, repeated child-routing and blocker-wall descent has
a finite structural tree.  Along every selected lineage, positive factor side
strictly decreases.  Every unit-wall split lowers total active factor-side mass by
one, and the complete wall tree has at most `N` splits and `2N+1` nodes per
envelope epoch.

### Proof

Strict child sides are CMR1096.  Unit-wall mass decrease and tree bounds are
CMR741--CMR747 and CMR1156. ∎

No routing-history factor is required.

## 8. Universal-range target endpoint

### Corollary CMR1173 -- PROVED

Every dirty selected minimum in the universal degree-two range reaches at least
one of:

1. strict physical-potential improvement;
2. finite selected-scheduler currency expenditure;
3. exact unit-wall or strict child-product descent;
4. fixed-core reconditioning or a real lost-anchor edge;
5. envelope expansion;
6. active side below four or another explicit thin/base regime.

Consequently the remaining prime-power frontier is concentrated entirely in the
**finite base and thin-regime endpoint** and in verifying that all induced
interfaces produced by descent are represented in that base ledger.  There is no
remaining terminal dirty owner of active side at least four.

### Proof

Combine CMR1166--CMR1172. ∎

No all-`n` theorem is claimed.  Target-location splits, residual and lifted bank
routing, strict child/wall arithmetic, and terminal-owner alternatives are checked
in
[`scripts/verify_prime_power_universal_range_target_descent.py`](../scripts/verify_prime_power_universal_range_target_descent.py).
