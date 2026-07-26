# Fully blocked ownership rows force anchor or macro-refill structure

The bottleneck-slack endpoint PP3mw--PP3mz leaves the extreme possibility that
the true movement ownership bottleneck is

```text
r_own=T.
```

At threshold `T-1`, a canonical Hall core then contains a movement label `A` and
macro `i` for which `A` has no compatible refill label at all.  Once individual
movement/refill controller denominators have fixed positive margin, summing the
exact nonedge certificate over all refill labels forces mass at scale `RT`:

```text
B_i+U_i(A)>delta R T.
```

The anchor term is a fixed-label anchor fibre and is converted by
PP3ali--PP3alm.  The macro refill-defect term contains either a target-size blocker
star or a target-order full resource bank.  Thus a completely blocked ownership
row is no longer an abstract assignment obstruction.

## 1. Mass identity for a dead movement row

Fix a macro `i` and movement label `A`.  Assume

```text
a_i(A)<=(1-gamma-delta)R
```

for one fixed `delta>0`, and suppose

```text
deg_(J_i^ctrl)(A)=0.
```

### Proposition PP3aln -- PROVED

One has

```text
B_i+U_i(A)>delta R T.
```

Consequently at least one of

```text
B_i>delta R T/2,
U_i(A)>delta R T/2
```

holds.

#### Proof

Every refill label `B` is a nonneighbor of `A`.  The exact union certificate
PP3lx gives

```text
a_i(A)+b_i(B)+u_i(A,B)>(1-gamma)R.
```

Sum over all `T` refill labels.  Using the movement-margin hypothesis gives

```text
T((1-gamma)R-a_i(A))
<
B_i+U_i(A),
```

and the left side is at least `delta RT`. ∎

The refill-row version is obtained by transposition.

## 2. Fixed-macro refill-defect extraction

Assume

```text
B_i=sum_B b_i(B)=U
```

is large.  For every unsafe refill entry `(i,B,e)` choose one noncontroller
blocker pair `{p,q}`.  Represent the entry by the four resources

```text
{B,e,p,q}.
```

For one fixed macro:

1. a typed refill label belongs to at most `R` entries;
2. a controller source point belongs to at most `T` entries as a controller;
3. a fixed blocker pair witnesses at most `T` refill entries;
4. a source point may have large blocker-endpoint degree, which is the star
   alternative below.

### Theorem PP3alo -- PROVED

For every integer `D>T`, at least one of the following holds.

1. Some source point occurs as a blocker endpoint in at least

   ```text
   (D-T)/T
   ```

   distinct blocker pairs.
2. There are at least

   ```text
   U/(4D)
   ```

   bad refill entries with distinct typed labels, distinct controllers,
   endpoint-disjoint blocker pairs, and no selected controller equal to a selected
   blocker endpoint.

#### Proof

Form the four-uniform resource hypergraph on the typed label and three source
resources.  If some source point has total degree at least `D`, at most `T` of its
incidences use it as a controller.  The remaining `D-T` incidences use it as a
blocker endpoint.  One fixed blocker partner pair contributes to at most `T`
entries, so there are at least `(D-T)/T` distinct blocker partners.

Otherwise every source resource has degree below `D`.  Typed-label degree is at
most `R`, and at the application below `R<D`.  Greedily selecting a hyperedge and
deleting all hyperedges meeting any of its four resources removes fewer than
`4D` entries per choice. ∎

## 3. Target-order consequence at the slab scale

Use

```text
R=Theta(W^2),
T=MW,
M=m^(1/20+o(1)).
```

Take

```text
D=WT.
```

Since `W->infinity`, one has `R<D` for all sufficiently large `m`.

### Corollary PP3alp -- PROVED

If

```text
B_i>=cRT
```

for one fixed constant `c>0`, then one macro contains either

1. a blocker source star with `(1-o(1))W` distinct partners; or
2. a full resource matching of size at least

   ```text
   (c/4+o(1))W.
   ```

#### Proof

Apply PP3alo with `D=WT`.  The star branch gives

```text
(D-T)/T=W-1.
```

The matching branch gives

```text
U/(4WT)
>=
cRT/(4WT)
=
(c/4)(R/W)
=
(c/4+o(1))W.
```

∎

Thus positive density inside one macro is enough even when the global bad-entry
density is `o(1/M)`.

## 4. Conversion of the fixed-macro resource bank

The resource matching from PP3alp already has distinct refill labels, distinct
controllers, endpoint-disjoint blocker pairs, and no controller/blocker overlap.
Pigeonhole blocker-pair layer type and choose one endpoint per pair in a common
permutation layer.  Puncture any chosen endpoint that is an active controller
elsewhere; its designated entry is controlled by the opposite selected controller
and therefore survives.

### Theorem PP3alq -- PROVED / CONDITIONAL ENDPOINT-HOST INTERFACE

A fixed-macro refill-defect core of mass `Omega(RT)` has one of the following
outcomes.

1. A free or punctured blocker source star of target size.
2. A controller-disjoint credited endpoint bank of size `Omega(W)`.
3. A strict paid controller-shadow improvement after recapture-free thinning.
4. Robust final-state direct completion.
5. A positive-density ambient unary, rank-three, or rank-four foreign support
   core.
6. An explicit source, transition, anchor, Hall, alternating,
   distinguished-endpoint, or endpoint-host obstruction.
7. Controller-puncture reserve exhaustion or failure of the initial allocation
   certificate.

#### Proof

Convert the star by PP3agh--PP3akj.  Convert the matching using PP3hz, batch
puncturing PP3akl, and the credited-line/recapture-free/final-state chain
PP3afn--PP3ajx. ∎

## 5. Fully blocked true ownership bottleneck is closed

### Corollary PP3alr -- PROVED / CONDITIONAL CONVERSION INTERFACE

Assume all movement and refill fibres have a fixed controller margin as in
PP3alh.  If the true movement ownership bottleneck satisfies

```text
r_own=T,
```

then the initial source contains one of:

1. a fixed-label anchor row of mass `Omega(RT)`;
2. a fixed-macro refill-defect core of mass `Omega(RT)`;
3. a target-size free or punctured source star;
4. a target-order credited endpoint bank;
5. paid improvement, robust completion, foreign-support concentration, explicit
   host failure, puncture-reserve exhaustion, or initial-certificate failure.

#### Proof

At threshold `T-1`, PP3my supplies a Hall-deficient set.  Its all-bad rectangle
contains a pair `(A,i)` with true row nondegree greater than `T-1`, hence equal to
`T`.  Apply PP3aln.  Convert the anchor branch with PP3ali--PP3alm and the macro
refill branch with PP3alp--PP3alq. ∎

### Proposition PP3als -- PROVED

The same conclusion cannot be inferred solely from the truncated score value
`r_score=T`, because the score may equal `T` while the true row still has
compatible refill labels.  A score-only proof must either recover a true dead row
from its Hall core or use the explicit numerator/denominator mass that caused the
truncation.

#### Proof

The score `rho_i(A)` is an upper bound on true nondegree and is truncated at `T`.
Equality of the upper bound does not imply equality of the true nondegree. ∎

This distinction prevents an unjustified replacement of the true ownership graph
by its defect-score majorant.

## 6. Revised ownership endpoint

### Corollary PP3alt -- PROVED

After PP3alc--PP3alr, the remaining movement ownership frontier has no individual
margin collapse and no completely dead true ownership row.  It consists of:

1. a nontrivial Hall bottleneck at some threshold strictly below `T`;
2. score truncation without a true dead row, requiring numerator/denominator
   localization;
3. macro-total controller or excess-shadow mass below the fixed-macro positive-
   density scale;
4. explicit marked/endpoint-host failure or puncture-reserve exhaustion;
5. branches that insist on one-step potential descent.

No completion of the no-three-in-line conjecture is claimed.
