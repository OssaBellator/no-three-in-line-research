# Weighted buffer-cover return amplification

PX351--PX355 classify a nonimproving terminal buffer bank by choosing one
external blocker from each state.  That loses useful information when every
state destroys more than one designated old certificate.  The exact debt is
weighted: if every buffer state destroys `D` designated certificates and has
no internal rank-three creation, then a nonimproving state must contain at
least `D` external blockers counted with multiplicity.

Double-counting this full debt amplifies the four PX354 sectors by `D`.
Every external blocker contains one or two fixed selected points.  A simple
support-matching argument then gives either one selected point contained in
many blockers, or a large same-layer/channel endpoint block whose rematching
suppresses many blockers simultaneously.

This chapter applies uniformly to coordinate rank one, directed paths,
generic rank one, and mixed two-buffer shadows.

## 1. Weighted buffer-cover inequality

Let `Omega` be one of the valid terminal buffer banks of PX347.  Assume

\[
|\Omega|\ge \frac{n^2}{4}.
\]

Suppose every state in `Omega` destroys at least `D>=1` designated old
certificates, creates no internal rank-three certificate, and is
nonimproving.

Let `B_1` be the multiset of external blocker certificates whose occurrence
determines exactly one buffer variable, and let `B_2` be the multiset whose
occurrence determines both buffer variables.  Multiplicity records distinct
geometric certificates, not merely dependency labels.

### Theorem PX356 -- PROVED

The full nonimprovement debt satisfies

\[
\boxed{
D|\Omega|\le n|B_1|+|B_2|.
}
\]

Consequently at least one of

\[
\boxed{|B_1|\ge \frac{Dn}{8}}
\]

or

\[
\boxed{|B_2|\ge \frac{Dn^2}{8}}
\]

holds.

### Proof

A nonimproving state has external creation at least `D`, because its old
designated destruction is at least `D` and its internal rank-three creation
is zero.  Sum the external creation count over all states.

A one-variable blocker can occur in at most `n` bank states, since the other
buffer variable is free.  A two-variable blocker determines its exact ordered
buffer pair and occurs in at most one state.  Double-counting blocker--state
incidences gives the first display.

If both alternatives failed, then

\[
n|B_1|+|B_2|<\frac{Dn^2}{8}+\frac{Dn^2}{8}
=\frac{Dn^2}{4}
\le D|\Omega|,
\]

contradicting the first display. \(\square\)

### Corollary PX357 -- PROVED

After pigeonholing over the exact PX352--PX353 dependency types, at least one
of the following holds.

1. One exact one-variable type contains at least

   \[
   \boxed{\frac{Dn}{48}}
   \]

   blocker certificates.
2. One exact two-variable type contains at least

   \[
   \boxed{\frac{Dn^2}{32}}
   \]

   blocker certificates.

### Proof

There are at most six one-variable types after both buffer sides are included,
and at most four two-variable types.  Apply PX356 and pigeonhole. \(\square\)

## 2. Fixed-support incidence graph

Every external blocker contains either:

- one inserted cell and two fixed selected points; or
- two inserted cells and one fixed selected point.

For a blocker `T`, let `S(T)` be its set of fixed selected points.  Thus

\[
1\le |S(T)|\le2.
\]

For a finite blocker family `C`, define

\[
\rho(C)=\max_z |\{T\in C:z\in S(T)\}|.
\]

### Theorem PX358 -- PROVED

The blocker supports contain a pairwise disjoint subfamily `Q` of size at
least

\[
\boxed{|Q|\ge \frac{|C|}{2\rho(C)}}.
\]

### Proof

Greedily choose one blocker support and delete every remaining blocker whose
support meets it.  A chosen support has at most two fixed points, and each
point belongs to at most `rho(C)` blockers.  Hence one choice deletes at most
`2rho(C)` blockers. \(\square\)

Assume the selected state is split into two permutation layers and at most
`q` channels.  Every fixed selected point has one of at most `2q`
layer/channel types.

### Theorem PX359 -- PROVED

From the disjoint blocker family in PX358 one can choose one fixed point from
at least

\[
\boxed{
 t\ge \frac{|C|}{8q\rho(C)}
}
\]

blockers so that all chosen points have one layer/channel type.  They occupy
distinct rows and columns.

Moving every chosen point away from its current position suppresses at least
`t` distinct blockers.

### Proof

The disjoint support family has at least `|C|/(2rho(C))` members and at least
that many fixed-point incidences.  Some layer/channel type occurs on at least
`|C|/(4q rho(C))` incidences.  One blocker support has at most two points of
that type, so the type is represented in at least

\[
|C|/(8q\rho(C))
\]

distinct blockers.  Choose one such point from each.  Disjointness of the
supports gives distinct selected points; membership in one permutation layer
gives distinct rows and columns.

Each chosen point belongs to its assigned blocker.  A rematching avoiding the
current position removes that point from the blocker triple, so the blocker is
suppressed. \(\square\)

## 3. High-point versus large-block return

### Theorem PX360 -- PROVED REDUCTION

For every threshold `R>=1`, a blocker family `C` has one of two outcomes.

1. **Weighted one-point child.**  Some selected point belongs to at least `R`
   blockers.  Treating that point as an order-one child gives designated old
   destruction at least `R`; the two-buffer cycle of PX342 moves it without
   internal rank-three creation.
2. **Movable endpoint block.**  There is a same-layer/channel endpoint block of
   order

   \[
   \boxed{
   t>\frac{|C|}{8qR}
   }
   \]

   whose rematching suppresses one assigned blocker per endpoint.

The parent terminal cycle remains frozen while the child is processed.  After
the child move, the parent blocker coordinate decreases by at least the
number of suppressed blockers, and the original terminal-core destruction is
still available when the parent cycle executes.

### Proof

If `rho(C)>=R`, use the first outcome.  Otherwise PX359 gives

\[
t\ge |C|/(8q\rho(C))>|C|/(8qR).
\]

Ancestor safety follows because recreating an assigned blocker requires the
chosen fixed point to return to its unique historical position.  This is the
frozen-switch interface of PX324--PX329. \(\square\)

This theorem does not assume that the candidate cells in the blocker family
form a matching.  Compatibility is extracted from the fixed selected points,
which are the objects actually moved to suppress the blockers.

## 4. Quantitative return from the four buffer sectors

### Theorem PX361 -- PROVED REDUCTION

Suppose a terminal buffer bank with designated destruction `D` is
nonimproving.

For every threshold `R>=1`, at least one of the following occurs.

1. A weighted one-point child has designated destruction at least `R`.
2. A same-type endpoint block has order greater than

   \[
   \boxed{\frac{Dn}{384qR}.}
   \]
3. One exact two-variable blocker type contains a selected point lying in at
   least

   \[
   \boxed{\frac{Dn}{64}}
   \]

   blockers.

### Proof

If the one-variable outcome of PX357 occurs, apply PX360 to a family of size
at least `Dn/48`.  This gives items 1 or 2.

If the two-variable outcome occurs, its family has size at least `Dn^2/32`.
The saturated selected background has at most `2n` fixed points.  Every
blocker has at least one fixed point, so incidence averaging gives one point
in at least

\[
(Dn^2/32)/(2n)=Dn/64
\]

blockers. \(\square\)

### Corollary PX362 -- PROVED

For an original terminal core, `D>=1`.

- A one-variable concentration gives either a one-point child of weight at
  least `R`, or an endpoint block of order greater than

  \[
  n/(384qR).
  \]
- A two-variable concentration gives a one-point child of weight at least

  \[
  n/64.
  \]

Thus the quadratic generic-rank-one and mixed-shadow sectors return
immediately to a linearly weighted one-point child.  The coordinate-rank-one
and directed-path sectors return to either a weighted one-point child or a
large compatible endpoint block.

## 5. Amplification chain

Put

\[
A=\frac{n}{384q}.
\]

When only the one-variable outcome persists, choose at a child of designated
weight `D_j` the threshold

\[
R_j=\sqrt{A D_j}.
\]

Ignoring harmless integer rounding, PX361 gives either an endpoint block of
order at least `R_j`, or a one-point child of designated weight at least
`R_j`.

### Theorem PX363 -- PROVED REDUCTION

Along a chain consisting only of weighted one-point returns,

\[
\boxed{
D_j\ge A^{1-2^{-j}}
}
\]

from the initial value `D_0=1`.

At any generation the alternative endpoint block has the same lower-bound
scale.  For `q=n^{o(1)}`, after two returns this scale is

\[
\boxed{n^{3/4-o(1)},}
\]

which lies strictly above the square-root ambient threshold and enters the
large-block theorem PX334--PX335.

### Proof

The recurrence is

\[
D_{j+1}\ge\sqrt{A D_j}.
\]

Induction gives

\[
D_j\ge A^{1/2+1/4+\cdots+1/2^j}
=A^{1-2^{-j}}.
\]

For `j=2` the exponent is `3/4`. \(\square\)

PX363 is a return-amplification theorem, not full closure.  A high-weight
one-point child may still generate another weighted terminal cover.  What is
new is that this cannot remain at constant scale: after at most two
one-variable returns, either a genuinely large endpoint block appears or the
one-point designated weight has already reached `n^(3/4-o(1))`.

## 6. Verification

Run

```bash
python scripts/verify_product_weighted_buffer_return.py
```

The verifier checks the weighted cover constants, the support-matching bound,
the layer/channel extraction coefficient, the quadratic-sector averaging, and
the exact amplification recurrence.