# Bank-ready audit for two-target terminal secants

**Branch:** `research/rational-inverse-expansion`

RI5bd--RI5bg close the bank-ready one-target terminal branch.  This note closes
the corresponding two-target expectation whenever the two prescribed target
cells occupy distinct source and target cosets of one installed I6 block.
Repeated-coset prescriptions are deliberately routed to their actual lower-rank
correlation law rather than charged as rank two.

Let

\[
X=\bigcup_{\alpha=1}^m u_\alpha H,
\qquad |H|=h,
\]

and use the uniform I6 state bank `M_(sigma,t)`.

## RI5bh -- exact rank-two I6 cylinder law -- PROVED

Fix two distinct source cosets `alpha_1,alpha_2`, two distinct target row cosets
`beta_1,beta_2`, and two within-coset shifts `s_1,s_2`.  The compatible
prescription

\[
\sigma(\alpha_i)=\beta_i,
\qquad t_{\alpha_i}=s_i,
\qquad i=1,2,
\]

occurs in exactly

\[
(m-2)!h^{m-2}
\]

of the `m!h^m` I6 states.  Hence

\[
\boxed{\Pr(T)=\frac1{(m)_2h^2}.}
\]

### Proof

The prescription fixes two distinct values of the permutation and two shift
coordinates.  The remaining `m-2` permutation images and `m-2` shifts are free.
QED.

## Two-target secant records

A bank-ready two-target record consists of one state-independent context cell
and two prescribed target-hyperbola cells.  The target pair determines its
unordered source-column pair and therefore its exact hyperbola secant.  The
record is rank two precisely when its two prescriptions use distinct source
cosets and distinct target row cosets.

## RI5bi -- exact weighted two-target collateral -- PROVED

Let `T_2` be any weighted multiset of bank-ready rank-two secant records, with
nonnegative costs `c(T)`, and put

\[
Q_2=\sum_{T\in T_2}c(T).
\]

For a uniform I6 state, the expected total two-target collateral is exactly

\[
\boxed{\frac{Q_2}{(m)_2h^2}.}
\]

No independence between records is required.

### Proof

Every record indicator has expectation `1/((m)_2h^2)` by RI5bh.  Sum the
weighted indicators and use linearity of expectation. QED.

## RI5bj -- secant-address injectivity -- PROVED

On the nondegenerate target hyperbola `xy=a`, two distinct target cells

\[
(x,a/x),\qquad(y,a/y)
\]

determine the secant

\[
xyR+aX=a(x+y).
\]

The secant determines the unordered pair `{x,y}` uniquely.  Consequently one
fixed secant address contributes at most one unordered target pair before the
finite component/profile decoration split.

### Proof

The target columns are the two roots of

\[
Z^2-(x+y)Z+xy=0.
\]

The secant coefficients determine their sum and product, hence the unordered
root pair. QED.

## RI5bk -- complete bank-ready terminal comparison -- PROVED UNDER THE
## PHYSICAL BLOCK HYPOTHESES

Let `W` be paid fixed-edge weight, `F` state-independent collateral, `Q_1` the
complete bank-ready one-target weight, `Q_2` the complete bank-ready rank-two
secant weight, and `C_3` the exact expected contribution of every remaining
rank-three prescription.  If

\[
\boxed{
\left(1-\frac1{mh}\right)W
>
F+\frac{Q_1}{mh}+\frac{Q_2}{(m)_2h^2}+C_3,
}
\]

then one I6 state strictly improves the paid potential.

### Proof

Use RI5a for expected paid destruction, RI5be for the one-target term, RI5bi for
the two-target term, and the actual cylinder law for `C_3`.  Positive expected
net gain yields one improving state. QED.

## Rank-collapse and physical audit

A two-cell prescription with a repeated source coset or repeated target row
coset is not assigned the rank-two probability.  It is either incompatible or
belongs to a lower-rank correlated cylinder and must be evaluated with its
actual source-coset prescription.  Every retained record must carry physical
source cosets, target row cosets, shifts, scale and owner fields.

Thus the entire bank-ready one-target/two-target terminal interaction audit is
closed.  The remaining RI6 interaction frontier is rank-three collateral,
non-bank-ready physical lifts, arithmetic owner payment and replenishable
source recurrence.

## Finite check

`scripts/verify_ri_two_target_bank_audit.py` enumerates small I6 banks, verifies
the exact rank-two count and weighted expectation, checks repeated-coset rank
collapse, and verifies secant-address injectivity over small prime fields.
