# Secant-cover two-switch rectangle reduction

PP3ayp--PP3ayw extract a fixed-centre fan or a four-resource-disjoint bank from a
complete secant-shadow cover.  A covered witness-host cell `z` and one tentative
template cell `a` form one diagonal of a rectangle.  Replacing that diagonal by the
cross diagonal preserves the **total** row and column degree vector and omits both
cells lying in the designated source-invalid triple.

A fixed-infrastructure qualification is essential.  The direct switch preserves each
permanent controller block only when the two pivots lie in one common block.  When they
lie in different blocks, the pool-compatible paired construction PP3azk--PP3azr must be
used instead.  The propositions below record the direct saturation identity and its
same-block rectangle interpretation.

## 1. One secant rectangle

Let the tentative endpoint state contain

```text
a=(x_i,y_j),
```

and let a witness-clearing endpoint host contain

```text
z=(x_u,y_v),
```

with four distinct endpoint resources.  Suppose

```text
a,b,z are collinear
```

for another tentative cell `b`.  Define

```text
c=(x_i,y_v),
d=(x_u,y_j).
```

### Proposition PP3ayx -- PROVED

The states

```text
state 0: {a,z},
state 1: {c,d}
```

use the same two old columns and old rows, each once.  Replacing state 0 by state 1
preserves the total row/column degree vector.  State 1 contains neither `a` nor `z`, so
it does not contain the designated triple `{a,b,z}`.

#### Proof

The two states are the two perfect matchings of the two-by-two rectangle

```text
{x_i,x_u} x {y_j,y_v}.
```

The opposite diagonal omits both original diagonal cells. ∎

The cross cells may create other source, internal-triple, candidate-shadow, or anchor
incidences.  Those are residual state costs rather than direct recreation of the
designated secant certificate.

## 2. Joint source-trade interpretation

Let `D` be the original marked source package whose tentative state contains `a`, and
let `P` be the witness-clearing package whose tentative state contains `z`.

### Proposition PP3ayy -- PROVED

Selecting state 1:

1. deletes the current source endpoints whose resources generated `a` and `z`;
2. preserves the total degree vector;
3. retains every original removal-credit record attached to those deleted endpoints;
4. removes the targeted host certificate.

#### Proof

The cross cells use all four resources but no original diagonal cell.  Removal credit
is attached to deletion of the current source endpoint, not to the replacement pairing.
Apply PP3ayx. ∎

This proposition is a global saturation statement.  It does not by itself assert that
the cross cells remain inside the permanent macro rectangles.

## 3. Resource-disjoint secant banks

Take the four-resource-disjoint family

```text
(z_r,{a_r,b_r}),  r in [h].
```

### Theorem PP3ayz -- PROVED AS A DEGREE-PRESERVING RECTANGLE BANK / CONDITIONAL COMMON-BLOCK INTERFACE

The pairs `(a_r,z_r)` define resource-disjoint two-by-two rectangles.  Arbitrary
choices of their two diagonals preserve the total degree vector, and the cross state in
rectangle `r` deletes its designated secant certificate.

If, in addition, the resources of `a_r` and `z_r` belong to one common permanent
matching block for every `r`, the bank is pool-compatible and enters the preferred
cross-orientation rectangle chain directly.

For pivots in different permanent blocks, use the paired internal product switches
PP3azk--PP3azr.

#### Proof

Resource disjointness and PP3ayx give the global degree statement.  A same-block
rectangle uses only `X_i x Y_i`.  The different-block correction is PP3azq. ∎

## 4. Fixed-centre covers

Suppose one tentative pivot `a` is incident with covered witness cells

```text
z_1,...,z_h.
```

### Proposition PP3aza -- PROVED AS A CONDITIONAL DEGREE INTERFACE

Globally, choosing one rectangle `(a,z_r)` in the cross state is an exact conditional
rectangle-star operation: fix the centre choice, delete its resources, and complete
the residual matching/CSP.

For fixed infrastructure:

1. use this direct state when `a,z_r` lie in one permanent block;
2. otherwise use one tentative-block filler and one witness-block filler as in
   PP3azp, producing a conditional paired-switch star.

#### Proof

A matching uses one cell at the resources of `a`, so exactly one centre choice is
active.  PP3ayx gives the direct degree identity; PP3azp supplies the blockwise
correction. ∎

## 5. Preferred orientation and designated credit

### Theorem PP3azb -- PROVED / CONDITIONAL EXISTING RECTANGLE CONVERSION INTERFACES

For a same-block direct secant rectangle bank, or for the pool-compatible paired bank
of PP3azk--PP3azr, the preferred all-cross state has the following properties.

1. Every assigned secant certificate is absent.
2. Every designated original source endpoint is moved.
3. The complete original allocation-failure credit remains available.
4. Direct recreation of the targeted certificates has zero cost.
5. The residual objective consists only of source validity, finite-state interactions,
   and insertion cost in `Theta_E^+`.

Consequently the bank enters the preferred cross-orientation and multistate rectangle
chain.

#### Proof

In the direct same-block case use PP3ayx--PP3ayz.  In the general fixed-infrastructure
case use PP3azk--PP3azo.  The opposite diagonal or all-cross product omits every
designated pivot.  All remaining events form the bounded finite-state normal form. ∎

## 6. Complete secant-cover endpoint

### Corollary PP3azc -- PROVED / CONDITIONAL EXISTING RECTANGLE CONVERSION INTERFACES

A complete or positive-density secant-shadow cover has one of:

1. a fixed-centre conditional paired-switch star;
2. a target-size resource-disjoint paired four-state bank;
3. an axis secant pencil;
4. a current paid structure, source-valid joint completion, conditional Hall core,
   signed/multistate conflict core, or residual current concentration from the existing
   rectangle chain.

#### Proof

Apply PP3ayr--PP3ayu, then the direct same-block theorem or the paired correction
PP3azk--PP3azr. ∎

## 7. Revised source-host closure

### Corollary PP3azd -- PROVED / CONDITIONAL EXISTING RECTANGLE ENDPOINTS

After adjoining the old-grid endpoint-shadow potential, fixed-template witness descent,
and the corrected pool-compatible secant switch, the source-certificate host interface
is reduced to existing endpoint/rectangle terminal alternatives.

The remaining assembly task is the exact call-site audit that those rectangle endpoints
supply one of:

```text
current Theta_E^+ payment,
source-valid joint completion preserving the original credit,
or robust final-state completion.
```

The direct cross-pool switch is not used in the fixed-infrastructure argument.

The no-three-in-line conjecture remains unproved.
