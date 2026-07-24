# Oversampled refined label matching: graph bounds and coordinate barrier

PP3ff requires a matching of movement/refill label pairs whose source-edge
domains are simultaneously fixed-pair safe and same-edge-anchor safe.  Average
boundary-shadow and bad-label incidence control the size and matching number of
that refined graph.  However, selecting `W` numerical labels from a larger
`L`-label interval does not by itself produce a saturated width-`W` grid patch.
This chapter records both the valid graph estimates and that coordinate barrier.

## 1. Average fixed-pair compatibility

Let `A_0,B_0` be candidate movement and refill label sets, both of size `L`.  Use
the notation of PP3ea and put

\[
 b_M(A)=R-|C_A|,
 \qquad
 b_R(B)=R-|D_B|.
\]

Define

\[
 \mathcal S_M=\sum_{A\in A_0}b_M(A),
 \qquad
 \mathcal S_R=\sum_{B\in B_0}b_R(B).
\]

Let `G_gamma` join `(A,B)` when

\[
 |C_A\cap D_B|\ge\gamma R.
\]

### Proposition PP3fs -- PROVED

The number of missing edges of `G_gamma` is at most

\[
 \boxed{
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}.
 }
\]

Consequently

\[
 \boxed{
 |E(G_\gamma)|
 \ge
 L^2
 -
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}.
 }
\]

#### Proof

For every label pair,

\[
 |C_A\cap D_B|
 \ge
 R-b_M(A)-b_R(B).
\]

Therefore a missing edge satisfies

\[
 b_M(A)+b_R(B)>(1-\gamma)R.
\]

Summing `b_M(A)+b_R(B)` over all `L^2` pairs gives
`L\mathcal S_M+L\mathcal S_R`.  Each missing pair contributes more than
`(1-gamma)R`. ∎

## 2. Removing same-edge-anchor-heavy label pairs

Fix `0<epsilon<gamma`.  Let `J_{gamma,epsilon}` be the refined graph from PP3ff,
so an edge of `G_gamma` remains only when

\[
 |U_{A,B}|\le\epsilon R.
\]

Define the exact bad-label incidence

\[
 \mathcal U
 =
 \sum_{A\in A_0}\sum_{B\in B_0}|U_{A,B}|.
\]

Let `mathcal E=mathcal E(E,F)` be the divisor energy from PP3fe.  Then
`mathcal U<=mathcal E`.

### Proposition PP3ft -- PROVED

The refined graph satisfies

\[
 \boxed{
 |E(J_{\gamma,\epsilon})|
 \ge
 L^2
 -
 L\frac{\mathcal S_M+\mathcal S_R}{(1-\gamma)R}
 -
 \frac{\mathcal U}{\epsilon R}.
 }
\]

Hence also the weaker arithmetic bound obtained by replacing `mathcal U` with
`mathcal E`.  Moreover,

\[
 \boxed{
 \nu(J_{\gamma,\epsilon})
 \ge
 \left\lceil\frac{|E(J_{\gamma,\epsilon})|}{L}\right\rceil.
 }
\]

#### Proof

At most `mathcal U/(epsilon R)` label pairs have
`|U_{A,B}|>epsilon R`.  Remove them from the PP3fs edge lower bound.

By König's theorem, a maximum matching and a minimum vertex cover have the same
size.  A cover vertex meets at most `L` edges, so
`|E(J)|<=nu(J)L`. ∎

The exact incidence can be substantially smaller than the divisor energy because
several retained anchors may witness the same bad source edge for one label
pair.

## 3. The coordinate-budget obstruction

### Refutation PP3-R5 -- PROVED

The following shortcut is false:

> choose `W<L` matched numerical label pairs from an `L`-label reservoir and
> regard the result as a saturated width-`W` macro patch.

#### Proof

Suppose the reservoir consists of actual new coordinates in
`[m+1,m+L]`.  A patch using only `W<L` of those rows and columns leaves every
unselected coordinate with zero points, so it is not saturated on `[m+L]^2`.
If a selected coordinate is greater than `m+W`, the patch is not contained in
`[m+W]^2` either.

Relabelling an arbitrary selected subset to consecutive coordinates is not a
grid affine transformation in general and need not preserve collinearity,
fixed-pair safety, or the same-edge product equations. ∎

Thus PP3fs--PP3ft are valid graph statements, but oversampling is not a free
single-macro construction.

## 4. Correct allocation interface

### Proposition PP3fu -- PROVED UNDER A SATURATION-COMPATIBLE ALLOCATION HYPOTHESIS

Assume the `L` movement labels and `L` refill labels are all actual final new
coordinates and an allocation procedure assigns every one of them to macro
variables, with exactly two slot points ultimately placed on every coordinate.
Suppose one macro receives `W` matched pairs from `J_{gamma,epsilon}` and its
refined domains have size at least `(gamma-epsilon)R`.  If

\[
 \boxed{
 48(2W)^2\le(\gamma-\epsilon)^2R,
 }
\]

then that macro's slot choices can be made internally no-three and clean of
fixed-pair and same-edge-anchor source triples, without changing the margins
prescribed by the global allocation.

#### Proof

Once the global allocation supplies the `W` actual final row/column labels, the
macro is exactly in the setting of PP3ff.  Apply that theorem. ∎

The missing premise is essential: every final new coordinate must be allocated,
not discarded.

## 5. Normalized graph form

Put

\[
 \sigma
 =
 \frac{\mathcal S_M+\mathcal S_R}{RL},
 \qquad
 \eta_U
 =
 \frac{\mathcal U}{RL^2},
 \qquad
 \eta_E
 =
 \frac{\mathcal E}{RL^2}.
\]

### Corollary PP3fv -- PROVED

The abstract refined graph has matching number at least

\[
 \boxed{
 L\left(
 1-
 \frac{\sigma}{1-\gamma}
 -
 \frac{\eta_U}{\epsilon}
 \right)
 }
\]

up to the integer ceiling.  The weaker arithmetic form replaces `eta_U` by
`eta_E`.

This estimate is useful inside a valid global label-allocation theorem.  It does
not by itself reduce the numerical coordinate span.

## 6. Revised target

There are now two valid ways to exploit a large compatibility graph.

1. **No oversampling:** take `L=W`, prove a perfect matching directly, and apply
   PP3ff.
2. **Global allocation:** let all `T=MW` final new rows and columns be candidate
   labels for several macros, allocate every label exactly once, and find one
   global matching whose edges are refined-safe for the macro owning each
   movement label.

The second route can use the average graph estimates PP3fs--PP3fv while
preserving saturation.  Its unresolved theorem is a balanced global allocation,
not the deletion of unused coordinate labels.