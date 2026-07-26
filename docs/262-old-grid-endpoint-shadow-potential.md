# Old-grid endpoint-shadow potential

The restart potential counts blocker incidences at the movement/refill candidate cells
used by the macro patch.  A canonical endpoint repair also inserts old-grid cells.
Unary source-invalidity of such a cell was therefore classified in PP3axq--PP3axx as
source-host credit rather than current potential credit.

There is a fixed universe that removes this distinction.  The complete old grid
`[m]^2` is unchanged by every source repair, and every saturated source has exactly
`2m` points.  Subtracting the two unavoidable axis blocker pairs at every unoccupied
old-grid cell gives a nonnegative integer potential with an exact
insertion-minus-removal identity.

This turns every retained-pair obstruction to one proposed old-grid endpoint cell into
current potential credit.  The genuinely host-only source classes are reduced to
certificates containing at least two proposed inserted cells: anchored pairs,
transitions, and inserted triples.

## 1. The fixed old-grid universe

Let `S subseteq [m]^2` be a saturated no-three source.  Thus every row and column
contains exactly two points and

```text
|S|=2m.
```

For `z in [m]^2`, define

```text
b_S^old(z)
=
number of unordered pairs {p,q} subseteq S\{z}
with p,q,z collinear.
```

### Proposition PP3axy -- PROVED

For every `z in [m]^2`:

1. if `z notin S`, exactly two pairs counted by `b_S^old(z)` are axis pairs, namely
   the two source points in the column of `z` and the two source points in the row of
   `z`;
2. every other counted pair is nonaxis;
3. if `z in S`, then `b_S^old(z)=0`.

#### Proof

When `z notin S`, saturation supplies exactly two source points in its column and two
in its row.  These give one vertical and one horizontal pair.  A pair containing one
point from each axis cannot be collinear with `z` unless the line is one of the two
axes.  Hence every additional pair is nonaxis.

When `z in S`, any pair of other source points collinear with `z` would form a
collinear triple in `S`, contrary to the no-three hypothesis. ∎

## 2. Nonnegative endpoint-shadow excess

Define

```text
Xi_old(S)
=
sum_(z in [m]^2)
  (b_S^old(z)-2 1_(z notin S)).
```

### Proposition PP3axz -- PROVED

`Xi_old(S)` is a nonnegative integer.  It is exactly the total multiplicity of
nonaxis blocker pairs through unoccupied old-grid cells.

Moreover the subtracted baseline is constant:

```text
sum_z 2 1_(z notin S)=2(m^2-2m).
```

#### Proof

Proposition PP3axy shows that every summand is the number of additional nonaxis pairs
when `z notin S`, and is zero when `z in S`.  Saturation gives `|S|=2m`, so the number
of unoccupied old-grid cells is `m^2-2m`. ∎

Thus `Xi_old` is invariantly defined under arbitrary saturation-preserving source
repairs; no pool, controller, or reference layer is needed for the universe itself.

## 3. Exact pair-weight identity

For distinct source points `p,q`, put

```text
omega_old(p,q)
=
number of z in [m]^2\{p,q}
with p,q,z collinear.
```

### Proposition PP3aya -- PROVED

One has

```text
Xi_old(S)
=
sum_({p,q} subseteq S) omega_old(p,q)
 - 2(m^2-2m).
```

If a saturation-preserving source trade replaces a removal set `D` by an insertion
set `P`, with unchanged source `O`, then

```text
Xi_old((O union P))-Xi_old((O union D))
=
I_old(P;O)-C_old(D;O),
```

where

```text
C_old(D;O)
=
sum_(d in D,p in O) omega_old(d,p)
 + sum_({d,e} subseteq D) omega_old(d,e),
```

and `I_old` is the analogous sum over `P`.

#### Proof

Every triple counted by `b_S^old(z)` is represented uniquely by its source pair and
third grid cell, giving the first identity.  The baseline is constant by PP3axz.
Expand the pair sum before and after the trade.  Pairs contained in `O` cancel, leaving
exactly the displayed insertion and removal terms. ∎

This is the old-grid analogue of the dynamic candidate-cell identity PP3kx.

## 4. Unary endpoint-source certificates are potential credit

Let a canonical endpoint trade delete its marked source set `D` and propose one
old-grid replacement cell

```text
a=(x,y).
```

A unary source-invalid certificate is a retained pair `{p,q} subseteq S\D` collinear
with `a`.

### Proposition PP3ayb -- PROVED

Every unary source-invalid certificate for `a` is a nonaxis incidence counted by
`Xi_old(S)`.  Deleting either retained endpoint `p` or `q` removes one unit of
`Xi_old` credit, unless the incidence disappears earlier through a favourable source
or universe deletion.

#### Proof

The vertical axis pair through `a` contains the marked source edge using old column
`x`, and the horizontal axis pair contains the marked source edge using old row `y`.
Both are absent from the retained source `S\D`.  Hence a retained blocker pair is
nonaxis.  It contributes one unit to the summand at `a`, and the pair-weight identity
PP3aya removes that unit when either endpoint is deleted. ∎

Multiplicity is preserved: several proposed cells blocked by the same retained pair,
or several retained pairs blocking one proposed cell, contribute separately.

## 5. Enlarged fixed restart potential

Let

```text
Theta_E(S)=Xi_cell(S)+Lambda_E(S)
```

be the fixed-infrastructure potential from PP3aux--PP3avf.  Define

```text
Theta_E^+(S)=Theta_E(S)+Xi_old(S).
```

### Theorem PP3ayc -- PROVED

`Theta_E^+` is a nonnegative integer comparable across every pool-compatible,
saturation-preserving repair.  Its exact change is the sum of the three exact
insertion-minus-removal identities for:

1. movement/refill candidate-cell excess;
2. active same-slot anchor incidence; and
3. old-grid endpoint-shadow excess.

#### Proof

The first two terms are PP3aux--PP3avf.  The third is PP3aya.  Their universes and
subtracted baselines are fixed under the stated repair, so the identities add. ∎

A strict decrease of any one term while the other two are nonincreasing gives strict
`Theta_E^+` progress.

## 6. Support rank is unchanged

An insertion incidence for `Xi_old` is generated by either:

```text
one inserted source point + one retained source point + one old-grid target cell,
```

or

```text
two inserted source points + one old-grid target cell.
```

### Proposition PP3ayd -- PROVED

Under a strictly alternating marked/helper cycle, every positive `Xi_old` insertion
signature has nonempty ordinary-helper support of rank at most two.  Adding all
`Xi_old` signatures to the complete restart-support table therefore keeps its total
rank at most three.

#### Proof

A new--old pair uses one selected replacement cell and hence at most one ordinary
helper.  A new--new pair uses at most two selected replacement cells and hence at most
two ordinary helpers.  Strict alternation makes the support nonempty exactly as in
PP3arq.  The source-invalid triple classes already have rank at most three. ∎

All weight-based `A_2/B_3/B_4`, fixed-axis, path, partner-fan, star, matching, and
fixed-core localization arguments are unchanged when their nonnegative insertion
weight includes `Xi_old`.

## 7. Unary source support becomes a current paid branch

### Theorem PP3aye -- PROVED / CONDITIONAL EXISTING CURRENT CONVERSION INTERFACES

Let a complete endpoint-support table produce a target-order unary retained-pair
source star, matching, or endpoint bank.  When the proposed unary cells lie in the old
grid, exactly one of the following occurs.

1. Permanent-block realization creates zero `Theta_E^+` insertion and deletes all
   designated unary incidences, strictly decreasing `Theta_E^+`.
2. A dense current support branch produces another current credited structure handled
   by the existing direct-payment chain.

The unary structure is not a host-only branch.

#### Proof

Attach each unary certificate to one retained blocker endpoint.  By PP3ayb it is a
current `Xi_old` credit record.  Permanent-block partition and first-deletion
accounting are identical to PP3axa--PP3axf.  Add the rank-at-most-two `Xi_old`
insertion table to the complete rank-three support host by PP3ayd.  In the independent
branch the insertion cost in every component of `Theta_E^+` is zero, so PP3aya gives
strict payment.  Dense branches enter the existing weight-agnostic current conversion
interfaces. ∎

Repeated-centre unary stars retain full multiplicity and may be paid by moving only
the centre through the bounded complete-support host.

## 8. Revised source-certificate frontier

### Corollary PP3ayf -- PROVED

After replacing `Theta_E` by `Theta_E^+`, unary retained-pair source obstruction is no
longer part of the cumulative host-credit frontier.

Every remaining genuinely host-only certificate contains at least two proposed
inserted source cells:

1. an anchored pair;
2. a transition certificate; or
3. an inserted-source triple.

For one internally no-three tentative endpoint state with `k=O(s)` inserted cells,
the anchored-pair and transition certificates lie on at most

```text
binom(k,2)=O(s^2)
```

distinct pair-lines.  The next frontier is therefore a fixed pair-line assignment
energy, not unary secant-shadow regeneration.

The no-three-in-line conjecture remains unproved.
