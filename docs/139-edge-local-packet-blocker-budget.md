# Edge-local packet blocker budget

PX305--PX310 use a matching of packet corrections and Bernoulli thinning to pay
all packet mass above a linear threshold.  The remaining linear regime can be
reduced without another global packet estimate.  A single correcting
transposition has no support-two or support-three interaction with other
corrections.  Its complete creation list is the first-order list of PX307.

This gives an exact local dichotomy.  The correction is already improving, or
one of its three first-order sectors is large and decodes to a clean-star or
loaded-line child.  More precisely, only `c_e-w_e+1` prospective blockers need
to be assigned and suppressed before the correction becomes strictly
improving.

## 1. Exact one-correction ledger

Fix a packet correction edge `e={r,s}` with old packet weight `w_e>=1`.  Let its
two prospective cells be `f_e^1,f_e^2`, and retain the fixed-point set `X_e` and
coefficients

\[
\mu_e(f_e^1),\qquad \mu_e(f_e^2),\qquad \lambda_e
\]

from PX307.  Put

\[
c_e=\mu_e(f_e^1)+\mu_e(f_e^2)+\lambda_e.
\]

### Theorem PX319 -- PROVED

Executing only the correction `e` satisfies

\[
\boxed{
\Phi(M\triangle e)-\Phi(M)\le -w_e+c_e.
}
\]

Consequently `w_e>c_e` gives an immediate strict improvement.

### Proof

Apply PX305 to the singleton correction matching `Q={e}` with `p=1`.  A
singleton bank has no creation certificate supported on two or three distinct
correction edges, so `C_2(Q)=C_3(Q)=0`.  PX307 gives `C_1(Q)=c_e`. \(\square\)

## 2. Nonimprovement exposes a star or loaded line

Assume the relevant line occupancy is at most `K` in the sense of PX228 and
PX308.

### Theorem PX320 -- PROVED

If the correction `e` is not certified improving by PX319, then

\[
\boxed{c_e\ge w_e.}
\]

At least one of the following holds.

1. One prospective cell `f_e^i` centres an endpoint-disjoint secant star of
   order at least

   \[
   \boxed{\frac{w_e}{3K}}.
   \]

2. The fixed set `X_e` contains at least

   \[
   \boxed{\frac{w_e}{3}}
   \]

   points on the line through `f_e^1,f_e^2`; hence the current state contains a
   loaded-line child of that order on the same line.

### Proof

Noncertification of improvement means `w_e<=c_e`.  One of the three nonnegative
summands defining `c_e` is at least `w_e/3`.  If a `mu` term is large, PX228
extracts a star of order at least `mu/K`.  If `lambda_e` is large, its definition
already counts that many fixed current points on the common line of the two
prospective cells. \(\square\)

### Corollary PX321 -- PROVED

Fix integer thresholds `T,L>=1`.  If no prospective correction cell centres a
star of order `T` and no relevant fixed line contains `L` points, then every
nonimproving packet correction satisfies

\[
\boxed{w_e<2KT+L.}
\]

Equivalently, every correction with `w_e>=2KT+L` is immediately improving or
produces one of those two structural children.

### Proof

Absence of the star outcome gives both `mu` terms smaller than `KT`; absence of
the line outcome gives `lambda_e<L`.  Hence `c_e<2KT+L`.  Combine with
`w_e<=c_e` for a nonimproving correction. \(\square\)

## 3. Exact blocker budget

Let `B_e` be the set of the `c_e` distinct prospective triples counted by PX307.
A blocker in `B_e` is either:

1. one prospective cell together with two fixed points, a clean-star-ray child;
2. both prospective cells together with one fixed point, a pair-line/radial
   child.

Work in the frozen-switch interface: the two correction rows, their old target
columns, and the two prospective cells remain fixed while a deeper bank
neutralizes designated blockers.  PX253--PX255 provide the coupled-block spread
interface, and PX278 supplies ancestor safety for the designated line
certificates.

### Theorem PX322 -- PROVED

Suppose `w_e<=c_e`.  After assigning and permanently suppressing any

\[
\boxed{b_e=c_e-w_e+1}
\]

distinct blockers from `B_e`, the correction `e` becomes strictly improving.
Thus every packet correction has an exact finite strict-sign-or-child sequence:

1. execute it immediately when `w_e>c_e`; or
2. convert at most `c_e-w_e+1` first-order blockers into deeper clean-star or
   pair-line children, then execute it.

### Proof

Suppressing one distinct blocker removes one prospective triple from the
singleton creation list.  After suppressing `b_e` blockers, the remaining
creation coefficient is at most

\[
c_e-b_e=w_e-1.
\]

PX319 then gives potential change at most `-1`.  Ancestor safety prevents a paid
blocker from returning during the frozen-switch recursion. \(\square\)

### Corollary PX323 -- PROVED

The residual range

\[
D_{\rm pkt}<12hK^2
\]

has no remaining packet-specific concentration problem.  Choosing any positive
correction edge reduces it to either an immediate strict improvement or a finite
list of clean-star/pair-line child obligations.  The unresolved sign is exactly
the general child-neutralization interface already present outside the packet
sector.

This does not by itself close the clean-star/radial branch.  It removes the
bounded linear packet residue as an independent frontier.

## 4. Verification

Run

```bash
python scripts/verify_product_packet_blocker_budget.py
```

The verifier exhausts integer sector weights through a fixed range, checks the
one-third structural dichotomy, the local threshold of PX321, and the exact
`c_e-w_e+1` blocker countdown of PX322.
