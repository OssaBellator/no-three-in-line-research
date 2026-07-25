# Width-three seven-hole signatures have exact displacement variance

CMR288--CMR290 encode a sharp width-three Hall blocker by three seven-element
hole sets and first/second moment constraints.  The second-moment inequality is
actually an exact identity: the hole defect equals the full squared row-
displacement energy of the retained lines.  This gives a sharp dichotomy.
Either the retained directions have a positive integer variance of size at
least linear in the block, or all retained lines are parallel and their row
shifts belong to one absolute finite list.

Let

\[
x_1<x_2<x_3,
\qquad
d_1=x_2-x_1,
\qquad
d_2=x_3-x_2,
\qquad
D=d_1+d_2.
\]

Retain the `n=t-9` disjoint full triples from CMR288 and write their row
coordinates as

\[
(a_{1,j},a_{2,j},a_{3,j}),
\qquad 1\le j\le n.
\]

Put

\[
\delta_j=a_{3,j}-a_{1,j}.
\]

Let `C` be the common large Hall-side row set and let

\[
R_i=C\setminus\{a_{i,j}:1\le j\le n\}.
\]

Thus `|R_i|=7`.  Define the hole moments

\[
M_i=\sum_{r\in R_i}r,
\qquad
Q_i=\sum_{r\in R_i}r^2.
\]

## 1. Exact first and second displacement moments

### Theorem CMR298 — PROVED

The retained lines satisfy

\[
\boxed{
\sum_{j=1}^{n}\delta_j=M_1-M_3
}
\]

and

\[
\boxed{
D^2Q_2-d_2D Q_1-d_1D Q_3
=
 d_1d_2\sum_{j=1}^{n}\delta_j^2.
}
\]

In particular the left side of the second identity is a nonnegative multiple
of `d_1d_2`.

### Proof

Collinearity on the three fixed source slices is exactly

\[
D a_{2,j}=d_2a_{1,j}+d_1a_{3,j}.
\]

The first displayed identity follows directly from

\[
\sum_j\delta_j
=
\sum_j a_{3,j}-\sum_j a_{1,j}
=
\left(\sum_{c\in C}c-M_3\right)
-
\left(\sum_{c\in C}c-M_1\right).
\]

For one retained line, the affine square gap is

\[
\frac{d_2}{D}a_{1,j}^2
+
\frac{d_1}{D}a_{3,j}^2
-
a_{2,j}^2
=
\frac{d_1d_2}{D^2}\delta_j^2.
\]

Sum over `j`.  Replacing each used-set second moment by the full moment of `C`
minus `Q_i` cancels the full moment because `d_1+d_2=D`.  Multiplication by
`D^2` gives the result. ∎

## 2. Exact integer variance

### Theorem CMR299 — PROVED

Define

\[
\mathcal V
=
 n\frac{D^2Q_2-d_2D Q_1-d_1D Q_3}{d_1d_2}
-
(M_1-M_3)^2.
\]

Then

\[
\boxed{
\mathcal V
=
\sum_{1\le j<k\le n}(\delta_j-\delta_k)^2.
}
\]

Consequently:

1. `mathcal V=0` if and only if all retained lines are parallel;
2. if the retained lines are not all parallel and `n>=2`, then
   \[
   \boxed{\mathcal V\ge n-1=t-10.}
   \]

### Proof

CMR298 identifies the first two power sums of the integer sequence
`delta_1,...,delta_n`.  The standard variance identity gives

\[
n\sum_j\delta_j^2-\left(\sum_j\delta_j\right)^2
=
\sum_{j<k}(\delta_j-\delta_k)^2.
\]

The right side vanishes exactly when all displacements are equal, which is
exactly parallelism because the outer source displacement `D` is fixed.

If the integers are not all equal, separate one value class of size `q` from
its complement.  Every cross pair differs by at least one, so the sum is at
least

\[
q(n-q)\ge n-1.
\]

This proves the lower bound. ∎

## 3. Parallel families have bounded shifts

### Theorem CMR300 — PROVED

Assume `mathcal V=0`.  Then there are nonzero integers `r_12,r_23` of one common
sign such that every retained line has

\[
a_{2,j}=a_{1,j}+r_{12},
\qquad
a_{3,j}=a_{2,j}+r_{23}.
\]

They satisfy

\[
\boxed{
d_2r_{12}=d_1r_{23}
}
\]

and

\[
\boxed{
1\le |r_{12}|,
\qquad
1\le |r_{23}|,
\qquad
|r_{12}|+|r_{23}|\le9.
}
\]

Hence there are at most `72` signed ordered shift pairs, independently of `t`.

### Proof

When `mathcal V=0`, all outer displacements equal one integer `delta`.  The
collinearity equation gives the constant shifts

\[
r_{12}=\frac{d_1\delta}{D},
\qquad
r_{23}=\frac{d_2\delta}{D}.
\]

They are integers because every retained middle row is integral, and they obey
the displayed cross-product identity.  Since `d_1,d_2` are positive, the two
shifts have the sign of `delta`.

Let `U_i=C\setminus R_i`.  Then

\[
U_2=U_1+r_{12},
\qquad
U_3=U_2+r_{23},
\qquad
|U_i|=t-9.
\]

If a set of `t-9` distinct integers and its translate by `r` both lie in
`[0,t-1]`, then `|r|<=9`: for `r>0`, the original set lies in an interval of
`t-r` integers, and the negative case is symmetric.  Apply this to
`r_12`, `r_23`, and `r_12+r_23`.  Compatibility of a matching triple forces all
three row coordinates to be distinct, so both adjacent shifts are nonzero.
Their common sign gives

\[
|r_{12}|+|r_{23}|
=
|r_{12}+r_{23}|
\le9.
\]

There are `36` positive ordered pairs with positive sum at most nine and the
same number of negative pairs. ∎

## 4. Prime-power consequence of the parallel case

### Corollary CMR301 — PROVED

Let the parent block have prime base `p>=11`.  In the parallel alternative of
CMR300,

\[
\boxed{v_p(d_1)=v_p(d_2).}
\]

For `p=5` or `p=7`, every failure of this equality is contained in the same
finite list of at most `72` shift pairs from CMR300.

### Proof

For `p>=11`, every nonzero integer of absolute value at most nine is a `p`-adic
unit.  Taking `p`-adic valuations in

\[
d_2r_{12}=d_1r_{23}
\]

therefore gives equality of the two source-gap valuations.  At primes five and
seven, only shift pairs containing a multiple of the prime can change the
valuation balance, and all such pairs lie in the finite CMR300 list. ∎

## 5. Revised width-three charging target

A large width-three blocker now has one of two explicit explanations.

1. **Dispersed directions.**  The seven holes carry the positive integer defect
   \[
   \mathcal V\ge t-10.
   \]
   This is a line-direction dispersion quantity determined entirely by the
   constant-size hole signature.
2. **Bounded parallelism.**  All retained lines use one of `72` signed shift
   pairs.  For prime base at least eleven the adjacent source gaps have equal
   valuation, placing the family in one fixed p-adic cluster type.

The remaining global theorem must prove that the variance defect or one bounded
parallel type is paid only boundedly often under envelope repairs.  This chapter
does not claim that final no-return statement.

No all-`n` theorem is claimed here.  The moment identities, variance gap,
parallel-shift classification, and prime-power valuation consequence are checked
in
[`scripts/verify_prime_power_width_three_variance.py`](../scripts/verify_prime_power_width_three_variance.py).
