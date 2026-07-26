# Secant-cover two-switch rectangle reduction

PP3ayp--PP3ayw extract a fixed-centre fan or a four-resource-disjoint bank from a
complete secant-shadow cover.  The missing degree-restoration observation is a
standard two-by-two switch.

A covered witness-host cell `z` and one tentative template cell `a` form one diagonal
of a rectangle.  Replacing that diagonal by the cross diagonal preserves every old
row and column degree and omits both cells lying in the designated source-invalid
triple.  Consequently the secant-cover branch rejoins the existing alternating
rectangle and preferred cross-orientation machinery.

## 1. One secant rectangle

Let the tentative endpoint state contain the arc cell

```text
a=(x_i,y_j).
```

Let a witness-clearing endpoint host contain the possible arc cell

```text
z=(x_u,y_v),
```

where the four endpoint resources are distinct.  Suppose one target certificate is

```text
a,b,z collinear,
```

with `b` another cell of the tentative internally no-three state.

Define the cross cells

```text
c=(x_i,y_v),
d=(x_u,y_j).
```

### Proposition PP3ayx -- PROVED

The two states

```text
state 0: {a,z},
state 1: {c,d}
```

use exactly the same two old columns and the same two old rows, each once.  Replacing
state 0 by state 1 therefore preserves every row and column degree.

State 1 does not contain either `a` or `z`, so it cannot contain the designated triple
`{a,b,z}`.

#### Proof

Both diagonals are perfect matchings of the two-by-two resource rectangle

```text
{x_i,x_u} x {y_j,y_v}.
```

The designated triple requires both `a` and `z`; neither belongs to the opposite
diagonal. ∎

The cross cells may create other source, internal-triple, candidate-shadow, or anchor
incidences.  Those are residual rectangle-state costs rather than recreation of the
designated secant certificate.

## 2. Joint source-trade interpretation

Let `D` be the original marked source set whose tentative endpoint state contains
`a`, and let `P` be the source-witness bank whose tentative clearing state contains
`z`.  The joint source trade deletes the corresponding source endpoints from both
packages.

### Proposition PP3ayy -- PROVED

Selecting state 1 still moves the source endpoint contributing old column `x_i`, the
source endpoint contributing old row `y_j`, and the two witness-bank endpoint
resources `x_u,y_v`.  Thus:

1. the original allocation-failure incidence attached to the moved `D` endpoint
   remains in the removal term;
2. the witness source endpoint is moved;
3. exact saturation is preserved by the cross pair; and
4. the targeted host certificate is absent.

#### Proof

The cross cells retain each of the four endpoint resources but pair them oppositely.
No original matching edge on those resources remains fixed.  The removal-credit
record depends on deletion of the current source endpoint, not on which opposite
row or column is used in its replacement.  Apply PP3ayx. ∎

This is the source-host analogue of the designated-credit cross orientation PP3pm--PP3pn.

## 3. Resource-disjoint secant banks become rectangle banks

Take the four-resource-disjoint family from PP3ayq:

```text
(z_r,{a_r,b_r}),  r in [h].
```

Choose `a_r` as the pivot template point in each record.  Assume the witness-bank
coordinate resources are disjoint from the tentative-state resources, as supplied by
the resource refinement preceding the clearing host.

### Theorem PP3ayz -- PROVED

The pairs `(a_r,z_r)` define `h` pairwise resource-disjoint two-by-two rectangles.
For every subset `J subseteq [h]`, independently choosing state 0 or state 1 in each
rectangle preserves the complete row/column degree vector on the union of their
resources.

Putting rectangle `r` in state 1 deletes its designated secant certificate
`a_r,b_r,z_r`.

#### Proof

PP3ayt gives distinct endpoint rows and columns for the cells `z_r` and pairwise
disjoint template pairs.  The tentative endpoint state is a matching, so distinct
pivot cells `a_r` use distinct rows and columns.  Cross-package resource refinement
makes the two coordinate pairs disjoint.  Hence the rectangles are resource-disjoint.
Apply PP3ayx independently in every block. ∎

The resulting object is exactly an alternating rectangle bank with a preferred cross
orientation.

## 4. Fixed-centre covers become conditional rectangle stars

Suppose PP3ayr gives one tentative template point `a` incident with a family of covered
cells

```text
z_1,...,z_h.
```

The rectangles `(a,z_r)` share the two resources of `a`, so at most one of them can be
selected in one matching state.

### Proposition PP3aza -- PROVED

A fixed-centre secant fan is an exact conditional rectangle-star problem:

1. choose one allowed centre rectangle `(a,z_r)`;
2. put that rectangle in the cross state;
3. delete its four used resources; and
4. complete the residual endpoint matching and finite-state CSP.

If every conditioned choice fails, the failures give the same conditional Hall
rectangles, heavy partner fibres, or residual paid/source cores as the fixed-cell
binary-fan chain.

#### Proof

A perfect matching uses one replacement at the fixed resources of `a`, so exactly one
centre choice is active.  After it is fixed, all remaining decisions lie on the
residual resources.  This is the conditional-host identity of PP3wv--PP3wx, with the
cross diagonal as the preferred centre state. ∎

The weights now record source-host and current-potential residuals, but the matching
factorization is identical.

## 5. Preferred orientation preserves designated credit

### Theorem PP3azb -- PROVED / CONDITIONAL EXISTING RECTANGLE CONVERSION INTERFACES

For a resource-disjoint secant rectangle bank, the all-cross state has the following
properties.

1. Every designated secant certificate assigned to the bank is absent.
2. Every original marked source endpoint used by a rectangle is moved.
3. The complete original allocation-failure credit attached to those endpoints remains
   available.
4. Direct recreation of the targeted secant certificates contributes zero.
5. The remaining objective consists only of residual source validity, cross-rectangle
   finite-state conflicts, and insertion cost in `Theta_E^+`.

Consequently the bank enters the preferred cross-orientation chain
PP3pm--PP3pr and its later cross-block, signed-CSP, and paid-residual refinements.

#### Proof

Items 1--3 are PP3ayy--PP3ayz.  Item 4 is the same opposite-diagonal observation as
PP3pm.  Every other triple or potential incidence is a residual state signature on one,
two, or three rectangle variables, exactly the finite-state normal form used by the
rectangle chain. ∎

This theorem is conditional only on the existing rectangle conversion endpoints; it
introduces no new geometric state type.

## 6. Complete secant-cover endpoint

### Corollary PP3azc -- PROVED / CONDITIONAL EXISTING RECTANGLE CONVERSION INTERFACES

A complete or positive-density secant-shadow cover of a permitted endpoint host has
one of the following outcomes.

1. A fixed-centre conditional rectangle star.
2. A target-size resource-disjoint alternating rectangle bank with preferred cross
   orientation.
3. An axis secant pencil.
4. A current paid structure, source-valid joint completion, conditional Hall core,
   signed cross-conflict core, or residual paid/source concentration produced by the
   existing rectangle chain.

#### Proof

Apply PP3ayr--PP3ayu and then PP3aza--PP3azb. ∎

Thus complete secant-shadow coverage is not a new terminal geometry.  It is a route
back into the already developed rectangle conversion architecture.

## 7. Revised source-host closure

### Corollary PP3azd -- PROVED / CONDITIONAL EXISTING RECTANGLE ENDPOINTS

After adjoining the old-grid endpoint-shadow potential, fixed-template witness descent,
and the two-switch reduction, the source-certificate host interface has been reduced
to the existing endpoint/rectangle terminal alternatives.

The remaining assembly task is no longer an arbitrary cumulative rich-line theorem.
It is the exact call-site audit that the rectangle endpoints invoked in PP3azb supply
one of:

```text
current Theta_E^+ payment,
source-valid joint completion preserving the original credit,
or robust final-state completion.
```

Any rectangle endpoint that returns only another host certificate must be followed
through the same typed credit distinction of PP3axq--PP3axx.

The no-three-in-line conjecture remains unproved.
