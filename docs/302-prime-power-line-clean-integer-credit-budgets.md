# The three line-clean rows have exact integer credit budgets

CMR1534--CMR1557 give three host-uniform line-clean coefficients and
CMR1566--CMR1573 show that rooted trace recurrence uses only the strong or
singleton class.  The remaining comparison with destroyed target load is
rational but has a common rank denominator.  Clearing it once gives a single
integer slack test for every class, including unavailable-edge penalties.

This is useful both mathematically and computationally.  Finite searches no
longer need floating-point comparisons, and a line-clean row can be inserted
directly into the strict integer certificate format of CMR1270--CMR1277.

Fix response side `d>=4`.  Let

\[
V_1,V_2,V_3\in\mathbb Z_{\ge0}
\]

be the corrected off-line candidate counts of residual ranks one, two and three.
Let `b>=0` be the number of unavailable allowed response edges, let `m>=0` be the
current integer potential, and let

\[
D=D_S(e)\in\mathbb Z_{\ge0}
\]

be the destroyed target load.

## 1. One common weighted candidate count

Define

\[
\boxed{
W_d(V_1,V_2,V_3;b,m)
=
(d-1)(d-2)V_1
+(d-2)V_2
+V_3
+(m+1)b(d-1)(d-2).
}
\]

### Theorem CMR1590 -- PROVED

The complete line-clean collateral-plus-availability bracket is

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

Multiply each summand by

\[
(d)_3=d(d-1)(d-2).
\]

The four resulting integer numerators are exactly the four terms in `W_d`. ∎

Thus rank one costs `(d-1)(d-2)` integer units, rank two costs `d-2`, rank three
costs one, and every unavailable edge costs `(m+1)(d-1)(d-2)`.

## 2. Generic rational factor form

Write the applicable line-clean factor as a positive rational number

\[
q=\frac uv
\]

with positive integers `u,v`.  Its permanent coefficient is

\[
\kappa(q)=\left(\frac d q\right)^d
=
\left(\frac{dv}{u}\right)^d.
\]

### Theorem CMR1591 -- PROVED

The strict line-clean improvement inequality

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

is equivalent to the strict integer inequality

\[
\boxed{
(dv)^d W_d
<
D u^d d(d-1)(d-2).
}
\]

### Proof

Use CMR1590, substitute `kappa(q)=(dv/u)^d`, and multiply by the positive
integer `u^d(d)_3`. ∎

No approximation enters this equivalence.

## 3. The three exact class inequalities

Use the class data

\[
(u_{\rm str},v_{\rm str})=(d-2,1),
\]

\[
(u_{\rm sing},v_{\rm sing})=((d-1)(d-3),d-2),
\]

\[
(u_{\rm ov},v_{\rm ov})=(d-3,1).
\]

### Theorem CMR1592 -- PROVED

The three line-clean rows improve whenever, respectively,

### Strong class

\[
\boxed{
 d^d W_d
<
D(d-2)^d d(d-1)(d-2).
}
\]

### Singleton class

\[
\boxed{
 [d(d-2)]^d W_d
<
D[(d-1)(d-3)]^d d(d-1)(d-2).
}
\]

### Endpoint-overlap class

\[
\boxed{
 d^d W_d
<
D(d-3)^d d(d-1)(d-2).
}
\]

These are exactly the CMR1547, CMR1555 and CMR1540 strict-improvement tests,
not merely sufficient relaxations.

### Proof

Insert the three pairs `(u,v)` into CMR1591. ∎

For a rooted-target trace, only the first two tests are needed by CMR1569--CMR1570.

## 4. Exact integer candidate budget

For one class `(u,v)` and destroyed load `D`, define

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

The line-clean row improves if and only if

\[
\boxed{W_d\le B_{d,u,v}(D).}
\]

When `D=0`, the budget is negative and no strict destruction comparison is
possible.  For `D>=1`, the budget is an explicit nonnegative or negative integer
which can be tested without rational arithmetic.

### Proof

CMR1591 has the form `A W_d < R` with positive integer `A=(dv)^d` and integer
`R=D u^d d(d-1)(d-2)`.  For integer `W_d`, this is equivalent to

\[
W_d\le\left\lfloor\frac{R-1}{A}\right\rfloor.
\]

∎

## 5. Rank-pure automatic ranges

Assume `b=0`.  For a fixed class budget `B=B_{d,u,v}(D)`, define

\[
B_1=\left\lfloor\frac{B}{(d-1)(d-2)}\right\rfloor,
\qquad
B_2=\left\lfloor\frac{B}{d-2}\right\rfloor,
\qquad
B_3=B.
\]

### Theorem CMR1594 -- PROVED

If only one residual rank is present, strict improvement is automatic in the
following exact ranges:

1. rank one only and `V_1<=B_1`;
2. rank two only and `V_2<=B_2`;
3. rank three only and `V_3<=B_3`.

Each threshold is maximal for the corresponding rank-pure integer envelope.

### Proof

In the three rank-pure cases, `W_d` equals the corresponding rank cost times
`V_r`.  Apply CMR1593.  Increasing `V_r` by one beyond the floor makes `W_d>B`,
so the threshold is maximal. ∎

This closes a nonempty finite geometric range whenever the corresponding budget
is nonnegative.

## 6. Availability consumes the same budget

Put

\[
C_b=(m+1)(d-1)(d-2).
\]

### Theorem CMR1595 -- PROVED

For fixed candidate counts and class budget `B`, the largest unavailable-edge
count allowed by the uniform criterion is

\[
\boxed{
 b_{\max}
=
\left\lfloor
\frac{B-igl[(d-1)(d-2)V_1+(d-2)V_2+V_3\bigr]}{C_b}
\right\rfloor,
}
\]

provided the numerator is nonnegative.  If it is negative, even the unrestricted
candidate row exceeds the uniform budget.

### Proof

Solve `W_d<=B` for the integer `b`. ∎

Thus restricted-host feasibility and new collateral draw from one common exact
integer reserve.

## 7. Integer slack certificate

Define the class slack

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

The integer `mathfrak S` is additive under any partition of the weighted
candidate count `W_d` into exact owner, line-height, prefix, carry or component-
rook classes, provided all parts use the same response coefficient class.

### Proof

The first assertion is CMR1591.  The second follows from linearity of `W_d` in
all candidate and unavailable-edge counts. ∎

For mixed coefficient classes one retains separate slacks; they must not be
merged using the strongest coefficient unless the response policy actually lies
in that class.

## 8. Integer-budget endpoint

### Corollary CMR1597 -- PROVED

Every strong, singleton or endpoint-overlap line-clean row now has:

1. one common integer weighted candidate count `W_d`;
2. one exact class-specific strict integer inequality;
3. one maximal integer collateral budget `B_{d,u,v}(D)`;
4. exact rank-pure automatic ranges;
5. an exact unavailable-edge budget; and
6. one positive integer slack suitable for independent certificate checking.

The remaining geometric task is to bound `V_1,V_2,V_3` and `b` by inherited
owner, line-height, token, prefix and carry classes strongly enough to make the
appropriate slack positive.  Rooted traces need only the strong and singleton
budgets.  No all-`n` theorem is claimed.

Rational-versus-integer equivalence, all three class formulae, maximal budgets,
rank-pure ranges, unavailable-edge caps and slack arithmetic are checked in
[`scripts/verify_prime_power_line_clean_integer_budgets.py`](../scripts/verify_prime_power_line_clean_integer_budgets.py).
