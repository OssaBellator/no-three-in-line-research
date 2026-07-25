# Blocker Hall cuts as one-centre hard-target fans

**Branch:** `research/alternating-core-chain`

AC3iz gives at least `n-2` genuinely missing blocker-host cells in every
minimal Hall cut.  AC3jd--AC3jh assign those cells finite unary hard-check
roles.  This note extracts the missing geometry which is stronger than total
incidence: one blocker row or one blocker column is incident with a linear
number of missing cells.

Those cells are alternative values of one permutation variable.  Their unary
hard checks therefore form exactly the distinct-target current-context system
of AC3aj.  The Hall obstruction is routed to unconditional target exclusions,
a common residual literal, support-disjoint residual blockers, a same-owner
fan, or a many-owner resource star.

## Hall-cut degrees

Retain the canonical Hall core `X` and destination complement `Z` from AC3iz.
Put

\[
m=|X|,
\qquad
s=|Z|=n-m+1.
\]

The genuine defect set is

\[
\mathcal H(X)\subseteq X\times Z
\]

and satisfies

\[
|\mathcal H(X)|
\ge
ms-\min\{m,s\}-1.
\]

For `a in X`, let `d_X(a)` be its defect degree into `Z`.  For `b in Z`, let
`d_Z(b)` be its defect degree from `X`.

A source `a` represents one current blocker row whose target values are the
destination columns.  A destination `b` represents, after passing to the
inverse blocker permutation, one blocker column whose target values are the
source rows.

## AC3ji -- one Hall-cut centre has linear missing degree -- PROVED

Let

\[
a_0=\min\{m,s\},
\qquad
b_0=\max\{m,s\}.
\]

Some source row or destination column satisfies

\[
\boxed{
\max\left\{
\max_{a\in X}d_X(a),
\max_{b\in Z}d_Z(b)
\right\}
\ge
\begin{cases}
 n-2,&a_0=1,\\
 b_0-1,&a_0\ge2.
\end{cases}
}
\]

In particular, for every `n>=3`, one centre has at least

\[
\boxed{\lfloor n/2\rfloor}
\]

genuinely missing target cells.

### Proof

Count the defect edges on the smaller side of the cut.  One vertex on that
side has degree at least

\[
\left\lceil
\frac{ms-a_0-1}{a_0}
\right\rceil.
\]

If `a_0=1`, this is `b_0-2=n-2`.  If `a_0>=2`, it is at least

\[
\left\lceil b_0-1-1/a_0\right\rceil=b_0-1.
\]

Since `m+s=n+1`, the larger side has size at least `ceil((n+1)/2)`, so
`b_0-1>=floor(n/2)`.  Degree on the source side is a blocker-row target fan;
degree on the destination side is the same statement for the inverse blocker
permutation. QED.

## Role-pure targets at one centre

Choose the least centre attaining the AC3ji bound, with row orientation taking
priority over inverse-column orientation.  Let `T` be its set of genuinely
missing target cells.  Assign every target its canonical unary role word from
AC3je and its exact hard-check and owner tokens.

## AC3jj -- one role retains a centred target fan -- PROVED

One unary role `lambda` occurs on at least

\[
\boxed{
 u
 \ge
 \left\lceil
 \frac{\lfloor n/2\rfloor}{R_{\rm un}}
 \right\rceil
}
\]

distinct target values of the same blocker row or inverse blocker column.

If every owner token of that role accounts for at most `rho` target values in
the fixed context, the selected fan contains at least

\[
\boxed{
\left\lceil\frac{u}{\rho}\right\rceil
}
\]

distinct owner tokens.

More generally, for every integer `D>=1`, either one owner token is assigned to
more than `D` selected targets, or at least

\[
\boxed{\left\lceil u/D\right\rceil}
\]

distinct owners occur.

### Proof

Pigeonhole the at least `floor(n/2)` target cells over the `R_un` unary role
words.  The owner statements are the ordinary bounded-fibre and maximum-load
pigeonhole inequalities. QED.

At exact-check resolution, one check is activated by at most one target, so
`rho=1`.

## Current-context residual scopes

Normalize the selected centre to one permutation block `v`.  Its current value
is the current blocker destination in row orientation, or the current blocker
source in inverse-column orientation.  Every selected missing cell is a
distinct target value `a` of `v`.

Choose its least activated canonical hard check `C_a`.  By AC3jg,

\[
f_{C_a}|_{S_{C_a}\setminus\{v\}}
=
\omega|_{S_{C_a}\setminus\{v\}}.
\]

When the unary hard-check rank is at most three, the effective residual scope
has size zero, one or two.

Let `U_0` be the selected targets with an empty effective residual and `U_+`
the remaining targets.  For each target in `U_+`, retain one nonempty effective
residual scope.  For a residual variable `x`, let `d(x)` be the number of
selected targets whose retained blocker uses `x`.

## AC3jk -- centred missing targets enter the cross-centre router -- PROVED

For every integer `Delta>=1`, the role-pure target family of size `u` satisfies
at least one of:

1. **Unconditional target stock:**
   \[
   \boxed{|U_0|\ge\lceil u/2\rceil.}
   \]
2. **Common current residual literal:** one exact residual literal occurs in
   more than `Delta` distinct target blockers.
3. **Support-disjoint residual targets:** there are at least
   \[
   \boxed{
   \left\lceil\frac{u}{4\Delta}\right\rceil
   }
   \]
   selected targets whose retained nonempty residual scopes are pairwise
   disjoint.

The targets are alternative values of one blocker permutation variable.  The
support-disjoint family is a dispersion record across alternatives; it is not
claimed to be simultaneously activated.

### Proof

If at least half the targets have empty residual, conclusion 1 holds.  Otherwise
`|U_+|>u/2`.  Apply AC3aj to the retained rank-at-most-two residual scopes.
Either one residual variable has target degree greater than `Delta`, or a
maximal disjoint residual family has size at least

\[
\left\lceil\frac{|U_+|}{2\Delta}\right\rceil
\ge
\left\lceil\frac{u}{4\Delta}\right\rceil.
\]

Current alignment of the residual literal is AC3jg. QED.

## AC3jl -- owner-resource refinement of the target fan -- PROVED

Combine AC3jj and AC3jk.  Every blocker Hall failure returns one exact centre,
one unary role and one of the following finite records.

1. At least `ceil(u/2)` unconditional one-cell exclusions.
2. One current residual literal paired with more than `Delta` distinct blocker
   targets.
3. At least `ceil(u/(4 Delta))` target blockers with support-disjoint residual
   arms.
4. One owner token shared by more than `D` target values.
5. At least `ceil(u/D)` distinct owner tokens attached to the same centre and
   role.

When the owner is a charging current resource, records 4 and 5 are respectively
the same-token and role-pure resource-star interfaces of AC3j--AC3l.  A
terminal carry/BDA/RI owner leaves through its named occurrence gate.  A
separable phase owner enters AC3p--AC3u.  An unowned exact check remains in
records 1--3 and is never assigned payment without a charging theorem.

### Proof

AC3jj supplies the owner dichotomy, while AC3jk independently supplies the
residual-scope trichotomy.  Retain both labels and report the first applicable
record in the displayed order.  The routes for the declared owner classes are
their definitions in AC3jh. QED.

## AC3jm -- the missing-host obstruction is a literal star -- PROVED

After AC3iu--AC3jc and AC3jd--AC3jl, a nonrepairable projected active matching
cannot return an unstructured blocker-host defect.  It exposes:

- a blocker row or inverse blocker column;
- at least `floor(n/2)` genuinely missing alternative cells at that centre;
- one role-pure subfan of size at least
  `ceil(floor(n/2)/R_un)`;
- exact activated hard checks with current-aligned residual rank at most two;
- and the owner-resource/refined residual alternatives of AC3jl.

Thus the remaining frontier is not Hall geometry or host-state drift.  It is
installation/payment of the explicit common-residual fan, support-disjoint
residual blockers, same-owner fan, many-owner star, or unconditional literal
stock, followed by outer arithmetic/context and envelope-epoch termination.

## Finite check

`scripts/verify_ac_hall_cut_target_fan.py` exhausts every Hall-cut defect subset
meeting the AC3iz lower bound through side seven, checks the sharp row/column
centre degree, exhausts rank-at-most-two residual families through five targets
and verifies every role, owner and threshold inequality above.