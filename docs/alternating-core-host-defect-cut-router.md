# Blocker Hall cuts and quantitative missing-host ancestry

**Branch:** `research/alternating-core-chain`

AC3iu--AC3iy reduce fixed-mask state-derived host drift to a blocker exchange
digraph.  A repairable projection enters an executable paid menu.  A failed
projection has a canonical minimal Hall core.  This note extracts the actual
base-host defect hidden in that Hall core.

The key count is sharp.  A deficient core of size `m` has a destination
complement of size `n-m+1`.  Every cell in the corresponding rectangular cut is
absent from the exchange graph.  The projected active permutation can account
for only one cell in each selected row and destination column, and the protected
pivot accounts for at most one further cell.  At least `n-2` cut cells are
therefore genuinely absent from the blocker base host.

## Hall-cut notation

Retain the current blocker

\[
O=\{(c,\rho_c):c\in[n]\},
\]

one projected active matching `P`, protected pivot `e`, blocker base host `B`
and exchange digraph `D_P` from AC3iv.

Assume `D_P` has no cycle cover.  Let `X` be the canonical inclusion-minimal
Hall-deficient source set from AC3ix and put

\[
m=|X|.
\]

Write

\[
Y=N_{D_P}(X)
\]

and define the destination complement

\[
Z=[n]\setminus Y.
\]

For the singleton dead-row case AC3ix gives `|Y|=0`.  Otherwise
`|Y|=m-1`.  In both cases,

\[
\boxed{|Z|=n-m+1.}
\]

The physical Hall cut is

\[
\mathcal Q(X)
=
\{(b,\rho_a):a\in X,\ b\in Z\}.
\]

Every cell in this cut is absent from
`B setminus (P union {e})`.

## AC3iz -- every failed blocker repair exposes `n-2` missing host cells -- PROVED

Define the genuine base-host defect set

\[
\mathcal H(X)
=
\mathcal Q(X)\setminus(P\cup\{e\})
\setminus B.
\]

Equivalently, `mathcal H(X)` consists of Hall-cut cells which are neither
occupied by the projected active permutation nor equal to the protected pivot,
and which are absent from the blocker base host.

Then

\[
\boxed{
|\mathcal H(X)|
\ge
m(n-m+1)-\min\{m,n-m+1\}-1.
}
\]

In particular, for every `n>=3`,

\[
\boxed{
|\mathcal H(X)|\ge n-2.
}
\]

The lower bound `n-2` is sharp at the endpoint core sizes `m=1` and `m=n`.

### Proof

The Hall cut contains

\[
|\mathcal Q(X)|=m|Z|=m(n-m+1)
\]

cells.  Because `P` is a permutation, its cells in the cut use distinct
selected rows and distinct destination columns.  Hence

\[
|P\cap\mathcal Q(X)|
\le
\min\{m,|Z|\}
=
\min\{m,n-m+1\}.
\]

The pivot `e` accounts for at most one additional cut cell and is not in `P`.
Every remaining cut cell is absent from `D_P`; by the exchange-graph
definition it must therefore be absent from `B`.  This proves the first box.

Put `s=n-m+1`, so `m+s=n+1`.  The quantity

\[
ms-\min\{m,s\}-1
\]

is minimized when `m=1` or `s=1`, where it equals `n-2`; moving both variables
away from an endpoint only increases the product after subtracting the smaller
variable. QED.

### Complete-host consistency

When `B=[n] x [n]` and `n>=3`, the set `mathcal H(X)` is empty, contradicting
AC3iz.  Thus the theorem recovers the complete-host repair corollary of AC3iv
from Hall-cut counting alone.

## AC3ja -- weighted missing-cell concentration -- PROVED

Let `mathcal F` be a finite family of distinct nonrepairable projected
matchings at one fixed current state, pivot and blocker base host.  Give
`P in mathcal F` a nonnegative historical/profile weight `w(P)` and put

\[
V=\sum_{P\in\mathcal F}w(P).
\]

Choose the canonical Hall core and defect set `mathcal H_P` for every
projection.  Define the missing-cell incidence load

\[
L(z)
=
\sum_{P:z\in\mathcal H_P}w(P),
\qquad z\in[n]^2\setminus B.
\]

Then

\[
\boxed{
\sum_z L(z)
\ge
(n-2)V.
}
\]

Consequently one exact missing blocker-host cell satisfies

\[
\boxed{
L(z)
\ge
\frac{n-2}{n^2}V.
}
\]

If the missing-cell universe has size `U_B` rather than the safe bound `n^2`,
the stronger denominator `U_B` may be used.

### Proof

AC3iz gives at least `n-2` defect cells for every weighted projection.
Double-count the weighted projection--defect incidences.  There are at most
`n^2` possible physical cells, so weighted pigeonhole gives the second box.
QED.

Thus a recurrent unrepairable host profile does not remain spread over arbitrary
historical states.  It concentrates quantitatively on one exact cell absent
from the fixed blocker host.

## AC3jb -- missing-reason localization -- PROVED

Suppose every cell `z notin B` carries one canonical reason label

\[
\operatorname{reas}(z)\in\Lambda,
\qquad |\Lambda|\le R.
\]

A reason may record an unavailable-mask token, carry condition, BDA/RI role,
protected support, envelope boundary or one finite exceptional state.

Let

\[
L_\lambda
=
\sum_{\operatorname{reas}(z)=\lambda}L(z).
\]

Then one reason satisfies

\[
\boxed{
L_\lambda
\ge
\frac{n-2}{R}V.
}
\]

For every threshold `beta>0`, that reason class has either:

1. one exact missing cell with load greater than `beta V`; or
2. more than
   \[
   \boxed{
   \frac{n-2}{R\beta}
   }
   \]
   distinct missing cells of positive load.

### Proof

The reason classes partition the missing-cell incidence sum from AC3ja.
Pigeonhole over at most `R` labels.  If no cell exceeds `beta V`, at least the
displayed number of cells is required to carry the selected reason load. QED.

When the selected reason is a charging resource, the first output is a
fixed-resource overload and the second is a role-pure resource star, entering
AC2d and AC3j--AC3l.  A noncharging reason remains one explicit finite
exceptional token; it is not promoted to paid geometry without its stated
interface.

## AC3jc -- quantitative host-drift ancestry router -- PROVED

Inside one fixed arithmetic/context, mask and envelope epoch, apply AC3iu to
project a recurrent target family to one current active matching.

Exactly one of the following occurs.

1. **Repaired execution.**  At least one distinct projection has a blocker cycle
   cover and enters AC3iw.  Improvement or an explicit created-rank/pivot return
   follows.
2. **Fixed missing-host cell.**  The nonrepairable projected weight `V` yields
   one exact cell absent from `B` with incidence load at least
   \[
   \boxed{(n-2)V/n^2}.
   \]
3. **Role-pure missing-resource output.**  With at most `R` canonical missing
   reasons, one reason carries incidence at least
   \[
   \boxed{(n-2)V/R},
   \]
   and AC3jb gives a heavy cell or many distinct cells in that role.
4. **Outer-field change.**  The base host, arithmetic/context, unavailable mask
   or envelope epoch changed and is retained as the genuine outer transition.

Therefore fixed-mask reference-state and opposite-layer drift are reduced to a
quantitative missing-cell ancestry certificate.  The unresolved state-derived
host frontier is no longer a matching-state problem; it is classification and
payment of one exact missing-host reason.

## Consequence

AC3it forces a repeated fixed-mask two-cross profile after polynomially many
state changes.  AC3iu--AC3iy remove historical reference variation and perform
every available blocker completion.  AC3iz--AC3jc now show that failure of all
such completions exposes at least `n-2` genuine missing host cells per
projection and concentrates the historical weight on one cell or one finite
reason class.

The next arithmetic target is to prove that every live missing-host reason is
one of the already paid carry/BDA/RI/protected-resource roles, or to place it in
a bounded exceptional stock.  That is a finite role-realization problem rather
than generic host drift.

## Finite check

`scripts/verify_ac_host_defect_cut_router.py` exhausts every core size,
destination complement and projected-permutation placement through side six,
checks the sharp `n-2` defect bound, weighted missing-cell and reason
pigeonholes, complete-host consistency and all displayed constants.
