# Incidence-derived capacities for protected-height events

**Branch:** `research/geometric-cleaning`

GC4z--GC4ac convert occurrence-faithful protected-event capacities into
clean-height-safe payment or an exact overload.  This note gives a direct way to
construct those capacities from bounded event incidence and operation weights.

Use the same-token fan notation.  Every unsafe operation `y` has weight
`lambda_y>0` and one least protected-event address `p(y)`.

## GC4ad -- exact address demand identity -- PROVED

For each address `p`, let

\[
I_p=\{y:p(y)=p\}.
\]

Then

\[
\boxed{H_p=\sum_{y\in I_p}\lambda_y.}
\]

The sets `I_p` partition the unsafe operations after aliases are aggregated.

### Proof

This is the definition of least-address demand together with the exact
least-address partition from GC4u. QED.

## GC4ae -- incidence-times-weight capacity -- PROVED

Suppose one has occurrence-faithful bounds

\[
|I_p|\le d_p,
\qquad
\lambda_y\le L_p\quad(y\in I_p).
\]

Then

\[
\boxed{H_p\le U_p:=d_pL_p.}
\]

Consequently

\[
\boxed{
U=\sum_pU_p
\le
\sum_pd_pL_p.
}
\]

### Proof

Sum at most `d_p` nonnegative terms, each at most `L_p`, in the identity from
GC4ad. QED.

## GC4af -- uniform finite-dictionary corollary -- PROVED

If the protected dictionary has size `K_H`, every address has incidence at most
`d`, and every operation weight is at most `L`, then either one declared
incidence/weight bound fails or

\[
\boxed{U\le K_HdL.}
\]

Hence, whenever

\[
K_HdL\le\eta W,
\qquad0\le\eta<1,
\]

GC4ab gives clean-height-preserving payment at least

\[
\omega_\pi+\frac{(1-\eta)W}{2r\kappa},
\]

or a clean-height-safe Hall deficiency greater than

\[
\frac{(1-\eta)W}{2\kappa},
\]

or one exact incidence/weight/capacity obstruction.

### Proof

Apply GC4ae with `d_p=d` and `L_p=L`, then invoke GC4ab. QED.

## GC4ag -- weighted incidence router -- PROVED

More generally, choose any declared address capacities `d_pL_p`.  A protected
height obstruction now has one of four exact forms:

1. an address occurs in more than `d_p` unsafe operations;
2. one operation at that address has weight greater than `L_p`;
3. all local bounds hold and the total capacity sum is small enough for the
   clean-height-safe GC4aa payment/Hall-core continuation;
4. the total certified capacity is large and is retained as the explicit
   quantitative obstruction `sum_p d_pL_p`.

No protected-event cause remains merely “finite but unbounded.”

### Proof

If a local bound fails, return its least witness.  Otherwise GC4ae constructs
valid occurrence-faithful capacities and GC4z--GC4ac apply. QED.

## Corrected GC5 frontier

The protected-height branch is reduced to proving concrete address incidence
and operation-weight bounds.  Once those bounds make `sum_p d_pL_p` smaller
than retained same-token demand, clean height is preserved quantitatively.
Remaining work is the geometry of those incidence bounds, payment of overloaded
addresses, neutralization of returned Hall cores, target-common/global blockers,
replenishable donors, non-tagged feedback, context causes and pool depletion.

## Finite check

`scripts/verify_gc_protected_event_incidence.py` exhausts small address
partitions, operation weights and declared incidence/weight caps.  It checks the
exact demand identity, `d_pL_p` capacities and the uniform dictionary bound.
