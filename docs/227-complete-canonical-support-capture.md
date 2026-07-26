# Complete canonical support capture at a marked centre

PP3ann--PP3ant define the residual helper-support hypergraph and give a support-
independent block or a near-linear terminal pencil.  The support-free branch was
stated with a residual-weight condition.  In the marked single-cycle normal form
that condition is unnecessary.

After the marked centre is fixed, every nonzero canonical source-invalid event and
every nonzero `Xi` insertion pattern uses at least one helper endpoint index.  The
only formal zero-helper insertion classes are a diagonal unary arc and a
transposition; both are identically absent from a single-cycle state.

Consequently the residual helper-support hypergraph captures the complete source
and insertion objective.  A support-independent helper block is automatically
source-valid and has zero insertion cost.  Failure is entirely a terminal support
pencil or an external host condition.

## 1. Helper ranks of the canonical source classes

Fix a marked endpoint index `c`.  Count helper indices other than `c` in one
canonical source-invalid signature.

### Proposition PP3aod -- PROVED

The nonzero source classes have the following helper-support sizes.

```text
rank-two unary source:          1
anchored transition:            2
rank-four anchored pair:        3
rank-four inserted triple:      3
rank-five inserted triple:      4
rank-six inserted triple:       5
```

In particular every nonzero source-invalid event has nonempty helper support of
size at most five.

#### Proof

Subtract the one fixed marked index from the endpoint-index support ranks in
PP3yc, PP3xw, PP3xp, and PP3jk.  A transition is a directed two-step path through
or adjacent to the centre and therefore uses two additional indices. ∎

A source-invalid event supported only on the marked centre does not exist.

## 2. Helper ranks of the canonical insertion classes

Under the single-cycle law, the support-ranked `Xi` normal form is

```text
A_1, A_2, B_2, B_3, B_4.
```

### Proposition PP3aoe -- PROVED

The two zero-helper or proper-cycle classes vanish identically:

```text
A_1=0,
B_2=0
```

on every single-cycle state.  Every remaining positive insertion pattern has
helper-support size

```text
rank-two unary A_2:   1
rank-three binary B_3: 2
rank-four binary B_4:  3.
```

#### Proof

`A_1` is a diagonal arc and `B_2` is a transposition, so both are forbidden by
PP3yx and PP3zb.  The remaining helper ranks are their endpoint-index support
ranks minus the fixed marked index. ∎

Thus every positive insertion weight selected by a single-cycle state is attached
to one nonempty helper support of size at most three.

## 3. Complete residual support hypergraph

Let `H_all(c)` contain, once each, the helper-index support of every positive
canonical source-invalid signature and every positive `Xi` insertion signature
at `c`, after all deterministic proper-cycle classes have been deleted.

### Theorem PP3aof -- PROVED

If a helper set `I_0` is independent in `H_all(c)`, then every single-cycle state
on

```text
{c} union I_0
```

is source-valid and has total `Xi` insertion cost zero.

#### Proof

By PP3aod, a selected source-invalid event would contribute a nonempty support
edge contained in `I_0`, contradicting independence.  By PP3aoe, every nonzero
insertion pattern has the same property.  The only insertion classes without a
nonempty helper support are zero in every single cycle. ∎

The conclusion is independent of event multiplicity and insertion weight.

### Corollary PP3aog -- PROVED

Suppose moving the marked centre has exact removal credit `R_c>0`.  If
`H_all(c)` has an independent helper set of size `b-1`, any single-cycle state on
that block is source-valid and satisfies

```text
Xi(S')-Xi(S)=-R_c<0.
```

Hence it gives a strict pool-compatible paid improvement without a first-moment
estimate.

#### Proof

The insertion cost is zero by PP3aof.  Apply PP3kx. ∎

This is the strongest possible paid outcome at the marked centre.

## 4. Terminal insertion-pencil classification

Apply PP3ano to `H_all(c)` with maximum helper rank `k_0=5`.  If the independent
branch fails, pigeonhole the finite canonical class and typed role of the fixed
core.

### Proposition PP3aoh -- PROVED

A terminal **insertion** pencil has one of the following forms.

1. `A_2`: a fixed incoming or outgoing unary arc axis with a variable partner.
2. `B_3`: a fixed-centre directed two-arc path pencil, in a predecessor, middle,
   or successor role.
3. `B_4`: a fixed centre arc with a variable remote partner arc, possibly after
   one further fixed-partner localization.

Each has `N^(1-o(1))` distinct positive helper extensions when the adaptive
subpolynomial filler size of PP3anp is used.

#### Proof

The helper ranks from PP3aoe are one, two, and three.  A fixed completion core has
size one less than the corresponding helper support.  Pigeonhole the finite
incoming/outgoing, path-role, and arc-orientation choices. ∎

These are exactly the geometries already isolated in the fixed-centre insertion
chapters.

## 5. Reconciliation with existing conversion theorems

### Theorem PP3aoi -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Every terminal insertion pencil in PP3aoh enters an existing target-size
conversion chain.

1. The `A_2` pencil is the fixed-axis arc star PP3abk--PP3abl and yields a
   comparable-cost arc-petal bank through PP3ada--PP3adg.
2. The `B_3` pencil is a fixed-centre path role.  The middle role enters the paid
   two-resource choice-grid chain PP3aco--PP3acs; an outer role yields a
   noncentral-resource-disjoint path-petal bank through PP3act--PP3acz.
3. The `B_4` pencil is a centre-arc partner fibre.  Positive-support avoidance,
   partner-star/matching extraction, fixed-cell fan thresholding, and final-domain
   bypass are PP3acc--PP3ach and PP3ago--PP3agz.

Because the terminal pencil size is `N^(1-o(1))`, every extracted family contains
a `W`-sized subbank with polynomial slack.

#### Proof

The geometric identifications are PP3abl, PP3abn, and PP3acc.  Apply the cited
petal, grid, fan, and domain theorems.  The scale comparison is PP3anp and
`N>>W`. ∎

The theorem is a reconciliation statement: the remaining work lies at the paid
conversion endpoints of those established chains, not in a new insertion-support
geometry.

## 6. Revised marked-centre endpoint

### Corollary PP3aoj -- PROVED

At a free or one-controller-punctured marked centre, exactly one of the following
occurs.

1. A support-independent helper block gives a source-valid zero-insertion strict
   improvement.
2. A terminal source pencil is converted or excluded by PP3anu--PP3aoc.
3. A terminal insertion pencil enters the arc-petal, path-petal, choice-grid,
   partner-fan, or final-domain conversion chains of PP3aoi.
4. An external controller-pool, distinguished-endpoint, Hall, alternating, or
   source-host condition fails.

There is no separate support-free insertion-weight frontier and no diffuse
residual support frontier.

The live problems are now the paid endpoints of a short list of explicit petal,
grid, and fan structures; controller-puncture reserve exhaustion; and branches
outside robust final allocation.

The no-three-in-line conjecture remains unproved.