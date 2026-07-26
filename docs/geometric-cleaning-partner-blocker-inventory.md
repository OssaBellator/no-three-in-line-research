# Explicit partner-blocker inventories for rectangle banks

**Branch:** `research/geometric-cleaning`

GC1a proves that separate blocker densities add, but it leaves each density as a
geometric input.  GC3j--GC3l compute the exact assignment incidence of physical
cells and non-axis lines.  Applying those bounds target by target gives a concrete
GC1 partner-loss inventory and a direct sufficient condition for the spread
injection of L1.

This note does not prove that the physical support or line inventories are small.
It identifies the exact quantities which must be bounded.  A global context
predicate which directly forbids many partner values remains visible as an
explicit residual set rather than being hidden inside a physical support count.

## One-target partner roles

Fix a target

\[
b=(r_b,c_b)
\]

and a partner pool `P` of size `p` in the same permutation layer.  For
`u=(r_u,c_u) in P`, the rectangle assignment inserts

\[
x(b,u)=(r_b,c_u),
\qquad
y(b,u)=(r_u,c_b).
\]

Let `Q_b` be an exact set of physical cells whose occurrence in the rectangle
support makes the assignment inadmissible.  It may combine opposite-layer
collision cells, installed-block support, active-core support and other exact
cell-local blockers.

## GC1c -- physical support blocks an explicit number of partners -- PROVED

The number of partners `u in P` satisfying

\[
\{b,u,x(b,u),y(b,u)\}\cap Q_b\ne\varnothing
\]

is at most

\[
\boxed{
p\mathbf1_{b\in Q_b}
+|P\cap Q_b|
+2|Q_b|.
}
\]

In particular, when the certified target itself is not physically forbidden,

\[
\boxed{
|I_{\rm cell}(b)|
\le
|P\cap Q_b|+2|Q_b|.
}
\]

If `Q_b` is disjoint from both the target and the current partner pool, then

\[
\boxed{|I_{\rm cell}(b)|\le2|Q_b|.}
\]

### Proof

The target role contributes all `p` partners only when `b in Q_b`.  Each support
cell which is itself a current partner excludes at most that one partner value.
For a fixed support cell `z`, the equation `x(b,u)=z` determines at most one
partner column and hence one partner; similarly `y(b,u)=z` determines at most one
partner row.  Sum these role incidences over `Q_b`.  Multiple incidences of one
assignment only overcount. QED.

The estimate is intentionally support-sensitive.  Saying only that every block
has bounded size is insufficient when linearly many disjoint blocks cover the
pool, as shown by GC1-wall.

## Exact high-line blockers

Let `L_b` be a finite set of exact non-axis grid lines.  A partner is line-blocked
when at least one of its two prospective cross-cells lies on one of those lines.
Rows and columns are excluded because permutation preservation handles them
exactly and they are not high-line defects.

## GC1d -- exact line inventory costs at most two partners per line -- PROVED

The line-blocked partner set satisfies

\[
\boxed{
|I_{\rm line}(b)|
\le
2|\mathcal L_b|.
}
\]

### Proof

GC3l gives at most two partners for one fixed target and one exact non-axis line:
one whose first cross-cell lies on the line and one whose second cross-cell lies
on it.  Take the union over `L_b`. QED.

The same partner may be blocked by several lines; union counting only lowers the
true cardinality.

## Global residual blockers

Let `J_b subseteq P` be the exact partner values forbidden by predicates not
represented by `Q_b` or `L_b`.  Examples include a global arithmetic context,
discretionary candidate filter or a nonlocal protected contract.  Its cost is
retained exactly as `|J_b|`.

## GC1e -- explicit per-target admissibility bound -- PROVED

Assume every inadmissible partner for target `b` is blocked by at least one of:

1. physical rectangle-support intersection with `Q_b`;
2. a prospective cross-cell on one line in `L_b`;
3. direct membership in `J_b`.

Then

\[
\boxed{
|I(b)|
\le
p\mathbf1_{b\in Q_b}
+|P\cap Q_b|
+2|Q_b|
+2|\mathcal L_b|
+|J_b|.
}
\]

For a certified target with `b notin Q_b`, define

\[
D_b
=
|P\cap Q_b|
+2|Q_b|
+2|\mathcal L_b|
+|J_b|.
\]

Then its admissible degree satisfies

\[
\boxed{d_\Gamma(b)\ge p-D_b.}
\]

If `D_b<=delta p` for every target in a batch, then GC1a holds with this
`delta` and the common pool `P`.

### Proof

GC1c bounds the physical-support blocker set, GC1d bounds the line blocker set,
and the residual set has cardinality `|J_b|`.  Their union contains every
inadmissible partner by hypothesis, so the union bound gives the first display.
The remaining statements are rearrangements. QED.

## GC1f -- direct spread-bank entry criterion -- PROVED

Let the target batch have size `t` and assume

\[
D_b\le\delta p
\quad(b\in B),
\qquad
t\le\beta p,
\qquad
delta+beta<1.
\]

Then the admissibility graph has a distribution on injections covering all
targets such that every compatible set of `r` prescribed assignments has
probability at most

\[
\boxed{
\left(\frac Kp\right)^r,
\qquad
K=(1-\delta-\beta)^{-1}.
}
\]

Thus the quantities in GC1e feed the L1 spread bank and the AC5 event audit
directly.

### Proof

GC1e gives `d_Gamma(b)>=(1-delta)p` for every target.  Apply L1: expose targets
sequentially and choose uniformly from unused admissible partners.  At every step
at least `(1-delta-beta)p=p/K` choices remain, so prescribed compatible choices
have probability at most `(K/p)^r`. QED.

## Pool restriction

If a later step retains a pool `P' subseteq P` of size at least `rho p` and
creates no new blocker on a retained partner, GC1b changes the relative blocker
density from `delta` to at most `delta/rho`.  The new L1 constant is therefore

\[
K'
=
\left(1-\frac\delta\rho-\frac{t}{|P'|}\right)^{-1}
\]

whenever the denominator is positive.  New blockers must instead enter the GC3
cause inventory.

## Corrected GC1 frontier

For each target it is now enough to bound four explicit quantities:

- current partners physically contained in `Q_b`;
- the total forbidden physical support size `|Q_b|`;
- the number of exact dangerous non-axis lines `|L_b|`;
- the global residual partner set `|J_b|`.

The first three have exact rectangle-incidence coefficients `1,2,2`.  Any failure
of positive partner density must therefore expose a large physical support, many
exact dangerous lines, or one large global residual predicate.  Those outcomes
match the installed-wall obstruction, GC2's pair-shadow/line bank, and the
alternating-core context router respectively.

## Finite check

`scripts/verify_geometric_partner_blocker_inventory.py` exhausts permutation
layers through order six, every target and partner pool, physical blocker sets of
rank at most three and every family of up to three non-axis lines.  It verifies
GC1c--GC1e and the sequential choice lower bound used by GC1f.
