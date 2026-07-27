# The three line-clean rows have exact integer credit budgets

CMR1534--CMR1557 give three host-uniform line-clean coefficients, and
CMR1566--CMR1573 show that rooted trace recurrence uses only the strong or
singleton class.  Their destroyed-credit comparisons share one rank
denominator, so every class admits an exact integer slack test, including the
unavailable-edge penalty.

Fix response side `d>=4`.  Let `V_1,V_2,V_3` be the corrected off-line candidate
counts of residual ranks one, two and three.  Let `b>=0` be the number of
unavailable allowed response edges, `m>=0` the current integer potential, and

\[
D=D_S(e)\in\mathbb Z_{\ge0}
\]

be the destroyed target load.

## 1. One common weighted candidate count

Define

\[
\boxed{
W_d
=
(d-1)(d-2)V_1
+(d-2)V_2
+V_3
+(m+1)b(d-1)(d-2).
}
\]

### Theorem CMR1590 -- PROVED

\[
\boxed{
\frac{V_1}{d}
+
\frac{V_2}{(d)_2}
+
\frac{V_3}{(d)_3}
+
\frac{(m+1)b}{d}
=
\frac{W_d}{(d)_3}.
}
\]

### Proof

Multiply by `(d)_3=d(d-1)(d-2)`.  The four resulting integer numerators are the
four terms in `W_d`. ∎

Thus rank one costs `(d-1)(d-2)` units, rank two costs `d-2`, rank three costs
one, and every unavailable edge costs `(m+1)(d-1)(d-2)`.

## 2. Generic rational factor form

Write the applicable line-clean fractional factor as

\[
q=\frac uv
\]

with positive integers `u,v`.  Its permanent coefficient is

\[
\kappa(q)=\left(\frac dq\right)^d
=\left(\frac{dv}{u}\right)^d.
\]

### Theorem CMR1591 -- PROVED

The strict improvement inequality

\[
\kappa(q)
\left[
\frac{V_1}{d}
+
\frac{V_2}{(d)_2}
+
\frac{V_3}{(d)_3}
+
\frac{(m+1)b}{d}
\right]
<D
\]

is equivalent to

\[
\boxed{
(dv)^dW_d
<
D u^d d(d-1)(d-2).
}
\]

### Proof

Substitute CMR1590 and clear the positive denominator `u^d(d)_3`. ∎

No approximation enters this equivalence.

## 3. The three exact class inequalities

Use

\[
(u_{\rm str},v_{\rm str})=(d-2,1),
\]

\[
(u_{\rm sing},v_{\rm sing})=((d-1)(d-3),d-2),
\]

and

\[
(u_{\rm ov},v_{\rm ov})=(d-3,1).
\]

### Theorem CMR1592 -- PROVED

The exact strict tests are:

### Strong class

\[
\boxed{
 d^dW_d
<
D(d-2)^d d(d-1)(d-2).
}
\]

### Singleton class

\[
\boxed{
[d(d-2)]^dW_d
<
D[(d-1)(d-3)]^d d(d-1)(d-2).
}
\]

### Endpoint-overlap class

\[
\boxed{
 d^dW_d
<
D(d-3)^d d(d-1)(d-2).
}
\]

### Proof

Insert the three pairs `(u,v)` into CMR1591. ∎

For a rooted-target trace, only the first two tests are needed.

## 4. Exact integer candidate budget

For one class `(u,v)`, define

\[
\boxed{
B_{d,u,v}(D)
=
\left\lfloor
\frac{D u^d d(d-1)(d-2)-1}{(dv)^d}
\right\rfloor.
}
\]

### Theorem CMR1593 -- PROVED

The uniform line-clean row improves if and only if

\[
\boxed{W_d\le B_{d,u,v}(D).}
\]

### Proof

CMR1591 has the integer form `AW_d<R`.  For integer `W_d`, this is equivalent to
`W_d<=floor((R-1)/A)`. ∎

When `D=0`, the budget is negative and no strict destruction comparison is
possible.

## 5. Rank-pure automatic ranges

Assume `b=0` and put `B=B_{d,u,v}(D)`.  Define

\[
B_1=\left\lfloor\frac{B}{(d-1)(d-2)}\right\rfloor,
\qquad
B_2=\left\lfloor\frac{B}{d-2}\right\rfloor,
\qquad
B_3=B.
\]

### Theorem CMR1594 -- PROVED

If only one residual rank is present, strict improvement is automatic exactly in
the following maximal integer ranges:

1. rank one only and `V_1<=B_1`;
2. rank two only and `V_2<=B_2`;
3. rank three only and `V_3<=B_3`.

### Proof

In each rank-pure case, `W_d` is the rank cost times `V_r`.  Apply CMR1593 and
the defining floor. ∎

## 6. Availability consumes the same budget

Let

\[
W_d^{\rm cand}
=(d-1)(d-2)V_1+(d-2)V_2+V_3
\]

and

\[
C_b=(m+1)(d-1)(d-2).
\]

### Theorem CMR1595 -- PROVED

Provided `B-W_d^{cand}>=0`, the largest unavailable-edge count allowed by the
uniform criterion is

\[
\boxed{
 b_{\max}
=
\left\lfloor
\frac{B-W_d^{\rm cand}}{C_b}
\right\rfloor.
}
\]

If `B-W_d^{cand}<0`, even the unrestricted candidate row exceeds the uniform
budget.

### Proof

The condition `W_d<=B` is `W_d^{cand}+C_bb<=B`.  Solve for integer `b`. ∎

Thus restricted-host feasibility and new collateral draw from one exact integer
reserve.

## 7. Integer slack certificate

Define

\[
\boxed{
\mathfrak S_{d,u,v}
=
D u^d d(d-1)(d-2)
-(dv)^dW_d.
}
\]

### Theorem CMR1596 -- PROVED

The uniform line-clean response is a strict improvement exactly when

\[
\boxed{\mathfrak S_{d,u,v}>0.}
\]

The slack is additive under any partition of `W_d` into exact owner,
line-height, prefix, carry or component-rook classes, provided all parts use the
same coefficient class.

### Proof

The first statement is CMR1591.  The second follows from linearity of `W_d`. ∎

Mixed coefficient classes retain separate slacks; they may not be merged using a
stronger coefficient unless the chosen response policy belongs to that class.

## 8. Integer-budget endpoint

### Corollary CMR1597 -- PROVED

Every strong, singleton or endpoint-overlap line-clean row now has:

1. one common integer weighted count `W_d`;
2. one exact class-specific strict integer inequality;
3. one maximal collateral budget `B_{d,u,v}(D)`;
4. exact rank-pure automatic ranges;
5. an exact unavailable-edge budget; and
6. one positive integer slack suitable for independent certificate checking.

The remaining geometric task is to bound `V_1,V_2,V_3` and `b` by inherited
owner, line-height, token, prefix and carry classes strongly enough to make the
applicable slack positive.  Rooted traces need only the strong and singleton
budgets.  No all-`n` theorem is claimed.

Rational-versus-integer equivalence, all three class formulae, maximal budgets,
rank-pure ranges, unavailable-edge caps and slack arithmetic are checked in
[`scripts/verify_prime_power_line_clean_integer_budgets.py`](../scripts/verify_prime_power_line_clean_integer_budgets.py).
