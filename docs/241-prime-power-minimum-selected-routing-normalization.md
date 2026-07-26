# A selected minimum fixes its routing skeleton without recurrence

CMR656--CMR663 decompose one residual matching host into exact child-prefix
products after fixing a vertex-routing skeleton.  The historical formulation used
routing recurrence to find one frequently repeated skeleton.  Minimum-anchor mode
is stronger: choose one actual minimum state and restrict immediately to the
routing skeleton which it already realizes.  The minimum survives, so no routing
history or recurrence threshold is needed on the selected proof path.

Fix a balanced factor host `H` of side `d>=1` inside an inherited prime-power
parent, and let

\[
\Psi:\operatorname{PM}(H)\to\mathbb Z_{\ge0}
\]

be any induced objective obtained after fixing external factors and a compatible
core.  Choose

\[
M_*\in\operatorname{PM}(H),
\qquad
\Psi(M_*)=\min_{M\in\operatorname{PM}(H)}\Psi(M).
\]

Let `Gamma_* = Gamma(M_*)` be the CMR659 vertex-routing skeleton of `M_*` at the
first strict child-prefix split.

## 1. Minimum-preserving routing restriction

### Theorem CMR1094 -- PROVED

The restricted family

\[
\mathcal F_*
=
\operatorname{PM}(H;\Gamma_*)
\]

is nonempty, contains `M_*`, and satisfies

\[
\boxed{
\Psi(M_*)
=
\min_{M\in\mathcal F_*}\Psi(M).
}
\]

### Proof

The chosen matching realizes `Gamma_*`, so `M_*` belongs to the restricted
family.  The restricted family is a subfamily of `PM(H)`, hence no member has
objective below the global minimum `Psi(M_*)`. ∎

Thus routing selection is an anchor-preserving restriction in the sense of
CMR902.

## 2. Exact product at the selected skeleton

### Theorem CMR1095 -- PROVED

Writing the routing blocks of `Gamma_*` as

\[
(X_{rs},Y_{rs})_{r,s\in\mathbb F_p},
\]

one has the exact bijection

\[
\boxed{
\mathcal F_*
\cong
\prod_{r,s}
\operatorname{PM}\bigl(H[X_{rs},Y_{rs}]\bigr).
}
\]

The selected minimum corresponds to the tuple of its child restrictions.

### Proof

This is CMR659 applied to the realized skeleton `Gamma_*`. ∎

No averaging over routing classes is used.

## 3. Every nonempty child is strict

Let

\[
d_{rs}=|X_{rs}|=|Y_{rs}|.
\]

### Theorem CMR1096 -- PROVED

If `d>=2`, then every nonempty selected child factor satisfies

\[
\boxed{1\le d_{rs}\le d-1.}
\]

At least two child factors are nonempty.

### Proof

CMR657 says at least one of the source or target projections splits at the next
base-`p` digit.  If some child had `d_{rs}=d`, every source vertex would lie in
`X_r` and every target vertex in `Y_s`; both projections would occupy one child
class, contradicting that split.  Since the child loads sum to `d`, no child has
load `d` and at least two are positive. ∎

Thus every coordinate continuation from the selected product has strictly smaller
factor side and lies in a strict prefix descendant.

## 4. Routing-changing histories are absent on the selected path

### Theorem CMR1097 -- PROVED

At a fixed host stage, the canonical minimum execution may remain entirely inside
`PM(H;Gamma_*)`.  It therefore performs no routing-skeleton change before one of:

1. a minimum-preserving host restriction;
2. minimum-core contraction;
3. strict child-factor descent;
4. unit-wall or other exact product descent;
5. envelope change;
6. strict objective improvement.

In particular, the routing-recurrence threshold `lambda` and the epoch factor
`1+R_m(lambda)` are unnecessary for this selected minimum path.

### Proof

CMR1094 preserves the chosen minimum after the one-time routing restriction, and
CMR1095 supplies the exact product in which all later local choices are made.
A change of routing class would only enlarge the restricted family and is not
needed to retain the selected minimum.  The listed events are precisely the
existing host, contraction, product, and envelope exits. ∎

This statement is specific to minimum-anchor analysis.  A complete enumeration of
all feasible states may still traverse many routing classes.

## 5. Lambda-free owner-stage stock

Recall the static host-stage bound

\[
H_m=2m^2+m+1.
\]

Define

\[
\boxed{
\mathcal A(d)
=
\sum_{m=1}^{d}H_m
=
\sum_{m=1}^{d}(2m^2+m+1).
}
\]

### Theorem CMR1098 -- PROVED

Along one selected strict factor-descent path beginning at side `d`, the number of
host-and-selected-routing owner stages is at most

\[
\boxed{\mathcal A(d).}
\]

### Proof

CMR691 gives at most `H_m` monotone host stages at side `m`.  CMR1097 chooses one
routing skeleton at each such stage.  Strict child recursion visits every positive
side at most once, so sum over `m=1,...,d`. ∎

The bound is cubic in `d` and has no recurrence parameter.

## 6. Lambda-free protected capacity

At side `m`, the two protected matchings together acquire at most `2m` fresh
edges.  Put

\[
\mathcal P_{\min}(d)
=
\sum_{m=1}^{d}2mH_m
\]

and

\[
\boxed{
\mathfrak P_{\min}(N,h)
=
(h+1)(2N+1)\mathcal P_{\min}(N).
}
\]

### Theorem CMR1099 -- PROVED

Across one complete selected minimum closure branch, total owner-labelled fresh
protected growth is at most

\[
\boxed{
\mathfrak P_{\min}(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}2m(2m^2+m+1).
}
\]

### Proof

Apply the `2m` local capacity once to every owner stage counted by CMR1098.  A
complete unit-wall tree has at most `2N+1` nodes and the closure chain at most
`h+1` envelope epochs.  Multiply. ∎

This replaces the degree-six, `lambda`-dependent capacity of CMR1089 by a
parameter-free degree-four polynomial for the selected minimum execution.

## 7. Lambda-free deletion-root stock

For a coarse two-layer bound, one owner stage of side `m` has at most `2m^2`
labelled host edges.  Define

\[
\boxed{
\mathfrak D_{\min}(N,h)
=
(h+1)(2N+1)
\sum_{m=1}^{N}2m^2(2m^2+m+1).
}
\]

### Theorem CMR1100 -- PROVED

The number of fresh owner-labelled structural deletion roots on the complete
selected minimum branch is at most `mathfrak D_min(N,h)`.

Returned redeletions are descendants of earlier roots and are not charged again
as fresh roots.

### Proof

At each selected owner stage charge a fresh structural deletion to its current
labelled host edge.  Use the `2m^2` edge stock, CMR1098 for the path stages,
CMR742 for the wall-tree nodes, and the `h+1` envelope epochs. ∎

## 8. Selected-routing endpoint

### Corollary CMR1101 -- PROVED

For minimum-anchor prime-power analysis, routing-support recurrence is not an
independent endpoint.  Every nontrivial factor is restricted immediately to the
routing skeleton of one actual minimum, factors exactly into strict child hosts,
and continues with:

1. parameter-free finite owner-stage stock `mathcal A(d)`;
2. parameter-free branch-wide protected capacity `mathfrak P_min(N,h)`;
3. parameter-free fresh deletion-root stock `mathfrak D_min(N,h)`;
4. strict child-side descent, host restriction, contraction, wall/product descent,
   envelope exit, or objective improvement.

### Proof

Combine CMR1094--CMR1100. ∎

No all-`n` theorem is claimed.  Minimum preservation, exact product
factorization, strict child sides, and the parameter-free owner/capacity arithmetic
are checked in
[`scripts/verify_prime_power_minimum_selected_routing.py`](../scripts/verify_prime_power_minimum_selected_routing.py).
