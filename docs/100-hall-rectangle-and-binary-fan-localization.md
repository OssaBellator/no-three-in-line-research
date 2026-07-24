# Hall-rectangle and binary-fan localization

PP3jz turns unary failure into a forbidden Hall rectangle, while PP3kg--PP3kh
turn binary failure into a cubic support core.  This chapter decomposes those
objects into the exact line and resource structures available to the next
protected trade.

## 1. Colouring a Hall rectangle by its cause

The complement of the zero-unary host `G_0` is the union of five simple
families:

1. diagonal cells;
2. cells occupied by the retained opposite layer;
3. source-secant unary cells;
4. designated recapture cells;
5. residual unary insertion-shadow cells.

The first two families are matchings and together contain at most `2q` cells.
For every other forbidden cell choose one witness type among source secant,
recapture, and unary insertion shadow.

### Proposition PP3ko -- PROVED

Let `X times Y` be a Hall rectangle of area

\[
 A=|X||Y|.
\]

One of the three nontrivial witness types is assigned at least

\[
 \boxed{
 \dfrac{A-2q}{3}
 }
\]

cells of the rectangle.

In particular, if `|X|,|Y|>=alpha q`, then for all sufficiently large `q` one
witness type occupies at least

\[
 \dfrac{\alpha^2}{4}q^2
\]

rectangle cells.

#### Proof

At most `q` diagonal cells and at most `q` opposite-layer occupied cells occur in
the whole endpoint rectangle.  Assign every remaining forbidden cell one of the
three witness types and pigeonhole.  If `A>=alpha^2q^2`, then
`(A-2q)/3>=alpha^2q^2/4` for sufficiently large `q`. ∎

Thus a macroscopic Hall rectangle contains a quadratic core of one geometric
kind; it is not merely a mixture of unrelated unary exclusions.

## 2. Recapture-dominated rectangles

There are exactly `q` designated recapture lines, one for each retained resource
entry, and each is a partial matching in the endpoint rectangle by PP3jo.
Assign every recapture cell to one designated line containing it.

### Proposition PP3kp -- PROVED

Suppose at least `c q^2` distinct cells are assigned to designated recapture
lines, where `0<c<=1`.  Then at least

\[
 \boxed{
 \dfrac{c}{2-c}q
 }
\]

of the designated lines are assigned at least `cq/2` endpoint cells.  In
particular there are `Omega_c(q)` resource-disjoint designated lines, each
meeting the endpoint rectangle in `Omega_c(q)` selected-coordinate cells.

#### Proof

Let `r` lines have assigned load at least `cq/2`.  Every line contains at most
`q` endpoint cells.  Hence the total assigned load is at most

\[
 rq+(q-r)\dfrac{cq}{2}.
\]

Comparing with `cq^2` and rearranging gives

\[
 r\ge\dfrac{c}{2-c}q.
\]

The designated entries were resource-disjoint in PP3hy. ∎

This is a genuine tomographic line bank: both the number of lines and the number
of endpoint intersections per line are linear.

## 3. Generic witness-line dichotomy

Source-secant and unary-shadow cells also lie on nonaxis witness lines, although
the number of possible witness lines need not be `q`.

### Proposition PP3kq -- PROVED

Assign `E` distinct endpoint cells to witness lines, each containing at most `q`
endpoint cells.  For every `D>=1`, either:

1. one witness line is assigned at least `D` cells; or
2. at least `E/D` distinct witness lines are used.

#### Proof

If every used line has load below `D`, at least `E/D` lines are needed. ∎

For a quadratic Hall core, taking `D=sqrt(q)` yields either a line with
`sqrt(q)` endpoint intersections or at least `Omega(q^(3/2))` distinct witness
lines.  Additional source/controller resource labels may then be pigeonholed or
matched according to the witness type.

## 4. From a binary resource star to one endpoint-cell fan

A binary shadow-support event is an unordered pair of compatible endpoint cells.
It uses two distinct left and two distinct right typed resources.

### Proposition PP3kr -- PROVED

Let `v` be one typed endpoint resource and suppose

\[
 d_2(v)\ge\rho q^2.
\]

Then there is one endpoint cell `a` incident with `v` and at least

\[
 \boxed{\rho q}
\]

distinct compatible endpoint cells `b` such that `{a,b}` has positive binary
controller shadow.

#### Proof

At most `q` endpoint cells are incident with one typed resource.  Every binary
event counted by `d_2(v)` contains exactly one of those cells.  Pigeonhole the
at least `rho q^2` distinct events among at most `q` choices of `a`.  The partner
cell determines the simple event, so the retained partners are distinct. ∎

Call this a **binary shadow fan** centred at `a`.

## 5. Candidate-line structure inside a binary fan

For every fan partner `b`, choose one controller candidate point `z_b` blocked
by the pair `{a,b}`.  Thus `a,b,z_b` are collinear.

### Proposition PP3ks -- PROVED

Let a binary fan have `H` partner cells.  For every `D>=1`, one of the following
holds.

1. One controller candidate point `z` is assigned at least `D` partners; all
   those partners lie on the one line `az`.
2. At least `H/D` distinct controller candidate points are used.

#### Proof

Pigeonhole the `H` assigned partners by their chosen controller candidate.  For a
fixed candidate `z`, every assigned partner lies on the line through `a` and
`z`. ∎

With `H=Omega(q)` and `D=sqrt(q)`, the binary star therefore gives either a
common-candidate line with `Omega(sqrt(q))` endpoint intersections or
`Omega(sqrt(q))` distinct controller candidates.

## 6. Complete cubic-core endpoint

### Corollary PP3kt -- PROVED

Suppose the binary shadow support satisfies

\[
 |B|\ge c q^3.
\]

Then at least one of the following holds.

1. **Linear binary fan:** one endpoint cell has `Omega_c(q)` compatible shadow
   partners.  This fan has the candidate-line dichotomy PP3ks.
2. **Resource-disjoint binary bank:** there are `Omega_c(q)` binary shadow events
   whose four typed endpoint resources are pairwise disjoint.

#### Proof

Apply PP3kh with

\[
 D=\dfrac c2q^2.
\]

In the star case, PP3kr gives a cell fan with at least `cq/2` partners.  In the
matching case, PP3kh gives at least

\[
 \dfrac{cq^3}{4(cq^2/2)}
 =
 \dfrac q2
\]

resource-disjoint events. ∎

The binary obstruction is now represented by either one explicit secant fan or
a linear independent conflict bank.  A successful next trade need not attack an
unstructured cubic family.

## 7. Revised conversion targets

The remaining support-concentrated cases have the following concrete forms.

- A Hall rectangle whose nontrivial cells contain a quadratic source-secant,
  recapture, or unary-shadow core.
- In the recapture case, a linear tomographic bank of linear-rich designated
  lines.
- In the binary case, a linear endpoint-cell fan with candidate-line structure,
  or a linear resource-disjoint binary conflict bank.
- A captive source-star centre from PP3kn.

These are the exact inputs for the next rectangle, tomographic, or dynamically
relabelled controller trade.
