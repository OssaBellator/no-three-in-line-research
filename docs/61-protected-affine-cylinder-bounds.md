# Protected affine cylinder bounds and the rank-two barrier

PX92--PX93 add independent row and column affine parameters inside every
protected coset.  This chapter computes the exact local cylinder probabilities.
The bank has the desired spread through rank two, but no further: two prescribed
indices determine the complete local affine state.

This identifies the next necessary enlargement.  A protected all-rank spread
distribution must use nonlinear local permutations or combine several affine
charts.

Assume the subgroup order is a prime `ell`.  Fix one coset and identify it with
`F_ell`.  Let

\[
M\subseteq(\mathbb F_\ell^*)^2
\]

be the admissible slope-pair set from PX93.  Choose

\[
(A,G)\in M,
\qquad
(\sigma,\delta)\in\mathbb F_\ell^2
\]

uniformly.  The local row and column labels are

\[
P(x)=Ax+\sigma,
\qquad
\Phi(x)=Gx+\delta.
\]

The harmless fixed coset representatives, global multiplier `m`, and global
column shift are omitted from the formulas; they are bijections and do not
change cylinder probabilities.

## Theorem PX94 -- PROVED

The protected affine local measure has the following exact cylinder laws.

1. For one index `x` and arbitrary targets `y,z`,

   \[
   \Pr(P(x)=y,\Phi(x)=z)=\frac1{\ell^2}.
   \]

2. For distinct indices `x_1,x_2` and arbitrary row and column targets
   `y_1,y_2,z_1,z_2`, the joint probability is either zero or

   \[
   \boxed{
   \frac1{|M|\ell^2}.
   }
   \]

3. Local states in distinct additive cosets are independent, so cylinder
   probabilities multiply over cosets.

Using PX93, every nonzero two-index cylinder therefore satisfies

\[
\Pr(\text{cylinder})
\le
\frac1{\ell^2(\ell-1-|D|)^2}.
\]

### Proof

Fix `(A,G)`.  For prescribed one-point targets, there is exactly one shift

\[
\sigma=y-Ax
\]

and exactly one shift

\[
\delta=z-Gx.
\]

Thus every admissible slope pair contributes one local state, giving probability
`|M|/(|M|ell^2)=ell^(-2)`.

For two distinct indices, subtraction gives

\[
A=(y_1-y_2)(x_1-x_2)^{-1},
\]

\[
G=(z_1-z_2)(x_1-x_2)^{-1}.
\]

The shifts are then uniquely determined.  If this slope pair is not in `M`, the
probability is zero; otherwise exactly one of the `|M|ell^2` local states
realizes the cylinder.  Independence across cosets is built into PX92.  The
last inequality is PX93. \(\square\)

For `ell` large compared with `|D|`, the two-index probability is
`O(ell^(-4))`, matching the scale of two independent random permutations.

## Theorem PX95 -- PROVED

The affine protected bank does not have all-rank permutation spread.  For every
admissible slope pair and every three distinct indices

\[
x_1,x_2,x_3,
\]

there are target images for which the three-index cylinder has probability

\[
\boxed{
\frac1{|M|\ell^2},
}
\]

exactly the same as its two-index subcylinder.

Consequently, when `|M|=Theta(ell^2)`, some three-index cylinders have
probability `Theta(ell^(-4))` rather than the `Theta(ell^(-6))` scale of two
independent uniform permutations.

### Proof

Choose any admissible local state `(A,G,sigma,delta)` and prescribe

\[
y_i=Ax_i+\sigma,
\qquad
z_i=Gx_i+\delta
\]

for `i=1,2,3`.  The first two prescribed pairs already determine all four affine
parameters uniquely, and the third pair is automatically satisfied.  Hence
exactly one local state realizes the three-index cylinder, just as for the
first two indices. \(\square\)

## 3. Consequence for certificate loads

The rank-two law is enough to control events using at most two distinct indices
from one coset.  It cannot give the extra probability factor needed for a
collinearity certificate involving three independently placed indices in the
same coset.

This explains structurally why adding affine slopes improves the translation
bank but does not automatically solve PX90.  The next protected entropy source
must have genuine rank-three variation.  Natural candidates are:

1. arbitrary or highly spread permutations inside each additive coset subject
   to the protected line-coordinate constraints;
2. piecewise-affine maps with at least three independently chosen pieces;
3. mixtures of affine charts whose chart variable is not determined by two
   point images;
4. a repair theorem which first eliminates all same-coset three-index
   certificates, leaving only the rank-two regime.

## 4. First example

For the `Z_25` diagonal-protected bank,

\[
ell=5,
\qquad
|M|=4.
\]

Every nonzero two-index joint row/column cylinder has probability

\[
\frac1{4\cdot25}=\frac1{100}.
\]

Some three-index cylinders also have probability `1/100`.  By contrast, the
uniform two-permutation scale for three distinct images would be

\[
\frac1{(5)_3^2}=\frac1{3600}.
\]

Thus the finite example already displays the full rank-two obstruction.

## 5. Verification

Run

```bash
python scripts/verify_product_protected_affine_cylinders.py
```

The verifier exhausts every local state for prime orders five, seven, and eleven,
checks all one- and two-index cylinder populations, and exhibits three-index
cylinders with the same probability as their two-index restrictions.