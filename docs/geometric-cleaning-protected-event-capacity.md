# Finite protected-event capacities for clean-height routing

**Branch:** `research/geometric-cleaning`

GC4u--GC4y separate a compatible same-token fan into clean-height-safe
operations and unsafe operations carrying one least protected-event address.
The remaining protected-height output is weighted demand `H_p` on a finite
address dictionary. This note closes that output whenever occurrence-faithful
capacities are available.

Use the notation of the clean-height same-token router. Thus

\[
W=W_{\rm safe}+\sum_{p\in\mathcal P_H}H_p.
\]

For every protected-event address `p`, let `U_p>=0` be a declared upper
capacity for unsafe operation demand carrying least address `p`, and put

\[
U=\sum_{p\in\mathcal P_H}U_p.
\]

The capacities must be occurrence-faithful: aliases are aggregated first, and
one physical event occurrence is not counted as independent capacity in two
addresses.

## GC4z -- exact protected-capacity dichotomy -- PROVED

Exactly one of the following continuations is available:

1. one address is overloaded, `H_p>U_p`;
2. every address respects capacity and
   \[
   \boxed{W_{\rm safe}\ge W-U.}
   \]

### Proof

If no address is overloaded, sum `H_p<=U_p` over the address dictionary and
subtract from the exact partition of `W`. QED.

This uses the actual capacity sum, not the coarser dictionary bound
`K_H max_p U_p`.

## GC4aa -- capacity-safe same-token payment -- PROVED UNDER THE EXISTING
## SAME-TOKEN CONTRACTS

Assume every protected address respects capacity and `W>U`. Let `r` be the
noncommon reuse bound and `kappa>=1` the payment normalization from GC4q--GC4t.
Then the safe subfan gives either:

1. a clean-height-preserving joint installation with current payment at least
   \[
   \boxed{
   \omega_\pi+\frac{W-U}{2r\kappa};
   }
   \]
2. a clean-height-safe weighted Hall deficiency greater than
   \[
   \boxed{
   \frac{W-U}{2\kappa}.
   }
   \]

### Proof

GC4z gives `W_safe>=W-U>0`. Apply the same-token payment/Hall-core theorem to
the safe subfan. Its exact bounds are
`omega_pi+W_safe/(2r kappa)` and `W_safe/(2kappa)`. Substitute the lower bound
for `W_safe`. Every selected safe subfamily preserves clean height by GC4u.
QED.

## GC4ab -- relative-capacity clean-height router -- PROVED

Suppose

\[
U\le\eta W,
\qquad 0\le\eta<1.
\]

Then one obtains:

1. clean-height-preserving current payment at least
   \[
   \omega_\pi+\frac{(1-\eta)W}{2r\kappa};
   \]
2. a clean-height-safe Hall deficiency greater than
   \[
   \frac{(1-\eta)W}{2\kappa};
   \]
3. or one exact protected-event capacity overload `H_p>U_p`.

For `eta=1/2`, the payment and deficiency constants recover the previous
safe-half losses, but the failure is strengthened from a merely heavy address
to a certified demand/capacity overload.

### Proof

Use GC4z. In the capacity-respecting branch, `W-U>=(1-eta)W` and GC4aa applies.
QED.

## GC4ac -- labelled-fan composition with finite capacities -- PROVED

Let an original same-token, same-role fibre have weight `W_0` and conflict
degree at most `Gamma`. Let GC4l retain a compatible family of weight

\[
W\ge\frac{W_0}{\Gamma+1}.
\]

If the protected-event capacities on that retained family satisfy

\[
U\le\eta\frac{W_0}{\Gamma+1},
\qquad 0\le\eta<1,
\]

then the fibre yields:

1. clean-height-preserving current payment at least
   \[
   \boxed{
   \omega_\pi+
   \frac{(1-\eta)W_0}{2r\kappa(\Gamma+1)};
   }
   \]
2. a clean-height-safe Hall deficiency greater than
   \[
   \boxed{
   \frac{(1-\eta)W_0}{2\kappa(\Gamma+1)};
   }
   \]
3. one exact protected-event capacity overload;
4. or one conflict-degree, inventory, separability, lineage, context or
   occurrence-capacity field fails.

### Proof

Apply GC4ab to the compatible family. Since
`U<=eta W_0/(Gamma+1)<=eta W` need not follow from `W>=W_0/(Gamma+1)` in that
direction, use the sharper direct estimate from GC4z:

\[
W_{\rm safe}\ge W-U
\ge
\frac{(1-\eta)W_0}{\Gamma+1}.
\]

Apply the same-token payment theorem to this safe weight. QED.

## Corrected GC5 frontier

Finite protected-height dictionaries are now quantitatively sufficient once
their occurrence-faithful total capacity is smaller than retained same-token
demand. A failure is an exact address overload rather than an unstructured
clean-height obstruction.

The remaining work is to prove such capacities for the actual protected-event
geometries, remove or pay overloaded protected events, neutralize the returned
minimal Hall cores, handle target-common/global blockers, replenishable donors,
non-tagged feedback, context causes, pool depletion and local superregular
resampling.

## Finite check

`scripts/verify_gc_protected_event_capacity.py` exhausts small integer safe and
unsafe weight partitions and capacity vectors. It verifies the exact capacity
dichotomy, the `W-U` safe-weight bound, relative-capacity constants and the
labelled-fan composition inequalities.
