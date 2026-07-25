# Paid residual-matching selection

PP3qj closes diffuse rectangle-dependent shadow provided the fixed residual
matching contributes less than the rectangle removal credit.  That residual
matching need not be chosen arbitrarily.  The superregular spread theorem allows
source validity and low residual shadow cost to be imposed simultaneously by the
same paid first moment used in PP3io.

## 1. Residual host data

Reserve a cross-safe rectangle subbank \(H\) of size \(h\), and let the remaining
balanced endpoint host have side size \(q_0\).  Assume it is superregular with
fixed positive density, as in PP3ov.

Let:

- \(P_0\) be the number of compatible residual edge pairs whose cells are
  collinear with one fixed retained point;
- \(Q_0\) be the number of residual three-edge matchings whose cells are
  collinear;
- \(A_0\) be the total residual unary shadow weight, summed over one residual
  matching edge and one fixed retained point;
- \(B_0\) be the total residual binary shadow weight over compatible residual
  edge pairs.

All weights are nonnegative and exclude rectangle-state contributions, which are
handled separately by PP3qh--PP3qm.

Let \(R_H>0\) be the removal credit allocated to the rectangle owners.  By
PP3pn,

\[
 R_H\ge h.
\]

## 2. Joint source-valid and paid first moment

### Theorem PP3qn -- PROVED FROM SR1

There is a constant \(K\), depending only on the residual superregularity
parameters, such that the following holds for sufficiently large \(q_0\).
If

\[
 K^2\frac{P_0}{q_0^2}
 +
 K^3\frac{Q_0}{q_0^3}
 +
 \frac1{R_H}
 \left(
 K\frac{A_0}{q_0}
 +
 K^2\frac{B_0}{q_0^2}
 \right)
 <1,
\]

then the residual host has a perfect matching \(M_0\) such that:

1. the retained fixed configuration together with \(M_0\) is no-three-in-line;
2. the residual insertion-shadow base cost satisfies
   
   \[
   C_0(M_0)<R_H.
   \]

#### Proof

Choose a uniform random perfect matching of the residual superregular host.  SR1
bounds every prescribed matching cylinder of rank \(r\le3\) by

\[
 \left(\frac K{q_0}\right)^r.
\]

Let \(X\) count the selected anchored-pair and collinear-triple source-invalid
patterns.  Then

\[
 \mathbb EX
 \le
 K^2\frac{P_0}{q_0^2}
 +
 K^3\frac{Q_0}{q_0^3}.
\]

The expected residual shadow cost is at most

\[
 \mathbb EC_0
 \le
 K\frac{A_0}{q_0}
 +
 K^2\frac{B_0}{q_0^2}.
\]

The displayed hypothesis gives

\[
 \mathbb E\left(X+\frac{C_0}{R_H}\right)<1.
\]

Some matching makes this random variable below one.  Since \(X\) is a
nonnegative integer, \(X=0\), and then \(C_0<R_H\). ∎

This is PP3io applied only to the residual matching, with the rectangle credit
reserved for the later local-state choice.

## 3. Adaptive-preparation simplification

### Corollary PP3qo -- PROVED

After the adaptive preparation PP3nr and reservation of a fixed small fraction
of endpoint resources, one has

\[
 \frac{P_0}{q_0^2}
 +
 \frac{Q_0}{q_0^3}
 =o(1).
\]

Consequently PP3qn applies whenever

\[
 K\frac{A_0}{q_0}
 +
 K^2\frac{B_0}{q_0^2}
 <(1-o(1))R_H.
\]

If, more strongly,

\[
 K\frac{A_0}{q_0}
 +
 K^2\frac{B_0}{q_0^2}
 =o(h),
\]

then the residual matching may be chosen source-valid with

\[
 C_0=o(h).
\]

#### Proof

Reservation can only decrease the source-pattern populations, while
\(q_0=\Theta(q)\) changes the normalized expressions by constant factors.
PP3nr and PP3jl make their sum \(o(1)\).  This proves the first sufficient
condition by substitution into PP3qn.

For the final assertion, write

\[
 \alpha_m=\mathbb EX=o(1)
\]

and

\[
 \beta_m=\frac{\mathbb EC_0}{h}=o(1).
\]

Choose any positive sequence

\[
 \epsilon_m\longrightarrow0
\]

such that

\[
 \frac{\beta_m}{\epsilon_m}\longrightarrow0;
\]

for example \(\epsilon_m=\sqrt{\beta_m}\) when \(eta_m>0\).  Then

\[
 \mathbb E\left(
 X+\frac{C_0}{\epsilon_mh}
 \right)
 \le
 \alpha_m+\frac{\beta_m}{\epsilon_m}
 =o(1).
\]

For all sufficiently large instances this expectation is below one.  Some
matching therefore has \(X=0\) and

\[
 C_0<\epsilon_mh=o(h).
\]

∎

## 4. Completion with a cleaned cross subbank

### Corollary PP3qp -- PROVED

Assume:

1. the residual expected shadow expression in PP3qo is \(o(h)\);
2. the all-cross rectangle family contains a subbank \(J\) of size
   \(h\to\infty\) whose rectangle-dependent insertion cost is \(o(h)\), as in
   PP3ql;
3. the all-cross state is geometrically valid on \(J\).

Then a source-valid residual matching and all-cross rectangle state exist whose
total insertion cost is \(o(h)\), while their designated owner removal credit is
at least \(h\).  Hence the combined trade is strictly improving.

#### Proof

Choose the residual matching with base cost \(o(h)\) by PP3qo.  Choose the
rectangle subbank with variable-dependent cost \(o(h)\) by PP3ql.  The sum is
\(o(h)<h\le R_H\), and geometric validity is PP3pp or PP3qg.  Apply PP3op. ∎

## 5. Exact residual weighted obstruction

### Corollary PP3qq -- PROVED

If the residual matching cannot be made cheap relative to a rectangle bank of
credit \(R_H\), then at least one of the following normalized quantities is
bounded away from zero at that credit scale:

1. anchored-pair source mass \(P_0/q_0^2\);
2. inserted-triple source mass \(Q_0/q_0^3\);
3. residual unary shadow expectation \(A_0/q_0\) divided by \(R_H\);
4. residual binary shadow expectation \(B_0/q_0^2\) divided by \(R_H\).

Under adaptive source preparation the first two vanish, so only residual unary
or binary weighted shadow can remain.

#### Proof

Negate the sufficient inequality of PP3qn and use PP3qo. ∎

### Corollary PP3qr -- PROVED

In the superregular common-line branch, diffuse geometry and diffuse paid cost
are now both closed.  Failure requires one of:

- a cross-conflict line or pencil from PP3px--PP3qc;
- linear unary or quadratic binary all-cross support from PP3qk;
- residual unary or binary weighted shadow at the rectangle-credit scale;
- a credit-poor homogeneous signature from PP3qg;
- a local signed contradiction.

The fixed residual matching is no longer an uncontrolled source of cost.