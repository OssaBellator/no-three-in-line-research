# Unary domain failure becomes a composite marked source-star trade

The domain threshold PP3ahh--PP3ahn leaves controller-domain-scale unary
insertion shadow.  This shadow has an exact post-trade interpretation.

Suppose a source-valid endpoint trade inserts a cell `a`.  If many values in one
movement or refill domain are lost because `a` and a retained source point block
the corresponding candidate, then after the trade `a` is itself a source point
belonging to all those blocker pairs.  The lost domain is therefore a genuine
source-star centred at the newly inserted point.

This permits a two-step paid conversion.  The first trade may create `C` star
incidences and need not decrease `Xi`.  A second marked endpoint trade moves the
new centre `a`, destroys those `C` incidences, and recreates only a controllable
fraction of them.  In the sum of the two exact potential identities, the
created and destroyed `C` terms cancel.  The composite trade is improving when
the remaining first-step cost and second-step foreign cost fit below the
original removal credit of the first trade.

Thus domain-scale unary shadow does not require a new geometric object.  It
returns to the marked source-star theorem, now as a second-generation star in
the post-trade source.

## 1. One inserted cell creates an exact source star

Let a source-admissible endpoint trade replace `R_0` by an inserted set `P`, and
put

```text
S_1=(S\R_0) union P.
```

Fix `a in P`, one macro pool `E_i`, and a movement label `A`.  Define

```text
F_M(a;i,A)
```

as the set of controller edges `e in E_i` for which the movement candidate

```text
z_e=(x_e,A)
```

is collinear with `a` and some retained point `p_e in S_1\{a}`, with
`{a,p_e}` a noncontroller blocker pair.  Define `F_F(a;i,B)` analogously for a
refill label `B`.

### Proposition PP3aho -- PROVED

For either type, if the fibre has size `C`, then:

1. its `C` candidate entries are distinct;
2. the retained partners `p_e` are distinct;
3. in the post-trade source `S_1`, the point `a` is a blocker endpoint in `C`
   distinct controller-shadow incidences.

Hence moving `a` supplies at least `C` units of exact dynamic removal credit.

#### Proof

Distinct controller edges at one label give distinct candidate cells.  By
source validity, one candidate cell has at most one retained witness for the
fixed inserted point, as in PP3ahh.

If one retained point `p` witnessed two different candidate cells at the same
movement label, the line `ap` would meet the horizontal row `A` twice, forcing
it to be horizontal.  That is impossible because `a` lies in the old endpoint
rectangle and `A` is a new row.  The refill argument is transposed.  Thus the
partners are distinct.

After the first trade, both `a` and every `p_e` belong to `S_1`, so each pair is
an actual noncontroller blocker of its candidate entry.  The dynamic `Xi`
potential counts all `C` incidences, and deleting `a` removes them. ∎

This is stronger than a support-degree certificate: it identifies the common
source endpoint that pays the next trade.

## 2. Domain loss forces one large inserted-centre fibre

Let `s=|P|`.  Suppose a base macro domain has size at least

```text
(gamma+xi)R
```

but, after unary shadow from `P` is inserted, its size is below `gamma R`.
Assign every removed value to one causing inserted cell and to movement or
refill type.

### Theorem PP3ahp -- PROVED

Some inserted cell `a in P` and one of the two types has a fibre satisfying

```text
C > xi R/(2s).
```

The post-trade source therefore contains a source-star centre of that degree.

#### Proof

More than `xi R` values were removed.  Split them between movement and refill
causes and then among the at most `s` inserted cells.  One of the `2s` classes
has size greater than `xi R/(2s)`.  Proposition PP3aho converts that class into
the displayed source star. ∎

At every active scale `s=m^(kappa+o(1))`, `kappa<19/40`, this lower bound is

```text
m^(19/20-kappa+o(1)),
```

which is at least target width and is much larger in the marked-cycle and
two-scale endpoint ranges.

## 3. Exact cancellation in a two-step trade

Let the first trade `T_1` have exact removal credit `R_1`.  Decompose its
insertion cost as

```text
I_1=C+J_1,
```

where `C` is a selected set of post-trade star incidences centred at `a`, and
`J_1` is every other insertion cost.

Let a second controller-preserving marked trade `T_2` move `a`.  Write

```text
I_2=I_self+J_2,
```

where `I_self` is recreation of the selected `C` star incidences and `J_2` is
all other second-step insertion cost.

### Proposition PP3ahq -- PROVED

The total two-step potential change satisfies

```text
Xi(S_2)-Xi(S_0)
<=
J_1+I_self+J_2-R_1.
```

Any additional removal credit of the second trade only improves the inequality.

#### Proof

The first dynamic identity gives

```text
Xi(S_1)-Xi(S_0)=C+J_1-R_1.
```

Moving `a` destroys all selected star incidences, so the second identity gives

```text
Xi(S_2)-Xi(S_1)
<=
I_self+J_2-C.
```

Add the two displays.  The created and removed `C` terms cancel exactly. ∎

Thus the first trade is allowed to create a very large star.  Its size is not a
net cost of the composite conversion.

## 4. Self-recapture can be made negligible relative to the first credit

Let the post-trade matching layer containing `a` provide an ambient marked bank
of size `Q_a`.  Choose a source-valid marked subbank of size `q_a` and let `K`
be its marked cylinder distortion.  PP3agk gives

```text
E I_self
<=
K C(q_a-2)/(Q_a-2).
```

### Proposition PP3ahr -- PROVED / CONDITIONAL ON MARKED HOST PREPARATION

Assume:

```text
R_1 -> infinity,
C <= R,
Q_a=Omega(R),
```

and the marked source-valid host permits every sufficiently slowly growing
`q_a` below the established upper scales.  Then `q_a` may be chosen so that

```text
E I_self=o(R_1).
```

#### Proof

The assumptions give

```text
Q_a R_1/C=Omega(R_1)->infinity.
```

Choose `q_a->infinity` sufficiently slowly that

```text
q_a/Q_a=o(R_1/C)
```

and below all marked source-valid upper scales.  With `K=1+o(1)`, PP3agk gives
the result. ∎

For a free centre the ambient layer has size `Theta(m)`; for a captive centre
the dynamic pool coordinate set has size `Theta(R)`.  Both dominate the active
star fibre.

## 5. Composite improvement theorem

### Theorem PP3ahs -- PROVED / CONDITIONAL COMPOSITE PAID INTERFACE

Assume the setup of PP3ahq and a marked source-valid second-step law.  If

```text
J_1+E[I_self+J_2] < R_1,
```

then some supported pair of source-admissible trades preserves the controller
infrastructure and strictly decreases `Xi` from `S_0` to `S_2`.

In particular, under PP3ahr it is sufficient that

```text
J_1=o(R_1),
E J_2=o(R_1).
```

#### Proof

Take expectations in PP3ahq.  The displayed inequality makes the expected
composite change negative, so one supported two-step outcome has negative
change.  Both steps are source-admissible and controller-preserving by
hypothesis. ∎

This theorem uses the original first-step removal credit to pay only genuinely
uncancelled collateral.  The intermediate star is an accounting bridge, not a
new unpaid cost.

## 6. Handoff from unary arc-petal and resource-bank states

### Corollary PP3aht -- PROVED / CONDITIONAL COMPOSITE INTERFACE

Consider a source-valid active endpoint state produced by an arc-petal,
resource-bank, transition, or marked filler selection.  Suppose its nonunary
binary shadow is domain-absorbed by PP3aha--PP3ahg and its base controller
domains have fixed margin.

Then at least one of the following occurs.

1. The unary shadow fits the margin and the final allocation completes directly
   by PP3ahk.
2. A domain loses its margin, and PP3ahp produces a newly inserted source-star
   centre of degree `Omega(R/s)`.
3. The two-step theorem PP3ahs combines the original trade with a marked move of
   that centre and strictly decreases `Xi`.
4. The first-step nonstar cost, second-step foreign cost, marked source
   preparation, or distinguished endpoint host is nonnegligible.

#### Proof

Apply PP3ahk when the unary degree condition holds.  Otherwise use PP3ahp,
followed by PP3aho and PP3ahs. ∎

For a fixed-axis arc-petal bank, the domain-scale alternative
`A_2=Omega(RW)` from PP3ahm therefore feeds a second-generation source-star
unless the mass is spread without destroying any individual macro-domain
margin.

## 7. Revised unary endpoint

### Corollary PP3ahu -- PROVED

Controller-domain-scale unary shadow has two exact forms.

1. It is spread across macro domains and does not prevent the robust final
   allocation.
2. It destroys one domain margin and creates a newly inserted source-star centre
   of degree `Omega(R/s)`, whose incidences cancel in a composite marked trade.

The remaining unary work is no longer raw domain-scale support.  It is:

- uncancelled first-step or second-step foreign insertion cost;
- marked source or transition preparation;
- distinguished endpoint-host failure;
- lack of a robust base allocation margin;
- a branch where the first trade has no growing removal credit.

## 8. Finite diagnostic

The script

```text
scripts/check_unary_domain_composite_star.py
```

finds the largest inserted-cell unary domain fibre in a finite source-valid
state, verifies distinct source partners, compares it with the
`xi R/(2s)` pigeonhole threshold, and evaluates the exact composite potential
upper bound.