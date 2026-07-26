# Subunit paid-pair selectors splice into the return row

CMR1518--CMR1525 compress repeated-token recurrence to a return row, one
persistent paid-pair selector, or one fixed trace incidence.  The selector row
still appears to be independent because CMR1522 records only the alternative

\[
A_L+\frac2Q+\frac{|B_L|}{Q(n-1)}\ge1.
\]

The threshold `Q` is free.  Optimising it shows that every selector with
candidate-only expectation strictly below one has a candidate-free completion
with an explicit finite restoration cap.  The restored edges are exactly return
incidences.  After first restoration labels are made monotone, a subunit
selector has no diagonal selector offspring: it is a bounded splice into the
return row.

This does not prove the return row subcritical and does not handle the critical
candidate regime `A_L>=1`.  It removes the separate selector coefficient in the
subunit regime and gives the exact two-row inequality which remains.

Fix one CMR1522 paid-pair selector on a residual board of side `n>=2`.  Write

\[
A=A_L,
\qquad
B=|B_L|,
\qquad
C=2+\frac{B}{n-1}.
\]

The deterministic surcharge two is already included in `C`.

## 1. Exact optimal integer threshold

Assume

\[
0\le A<1.
\]

Define

\[
\boxed{
Q_*(A,B,n)
=
\left\lfloor
\frac{2+B/(n-1)}{1-A}
\right\rfloor+1
}
\]

and

\[
\boxed{T_*(A,B,n)=Q_*(A,B,n)-1.}
\]

### Theorem CMR1558 -- PROVED

`Q_*` is the least positive integer satisfying

\[
\boxed{
A+\frac2{Q_*}+\frac{B}{Q_*(n-1)}<1.
}
\]

Equivalently,

\[
\boxed{A+\frac{C}{Q_*}<1.}
\]

If `Q_*>1`, then

\[
A+\frac{C}{Q_*-1}\ge1.
\]

### Proof

The strict inequality is equivalent to

\[
Q>\frac{C}{1-A}.
\]

The least integer strictly larger than a nonnegative real number `x` is
`floor(x)+1`.  This gives `Q_*` and the minimality statement. ∎

## 2. Candidate-free execution with bounded restoration

### Theorem CMR1559 -- PROVED

CMR531 supplies a line-clean completion `delta` satisfying

\[
\boxed{X_L(\delta)=0}
\]

and

\[
\boxed{
T_Z(\delta)<Q_*,
\qquad
T_Z(\delta)\le T_*.
}
\]

Thus a subunit paid-pair selector is executable with no candidate-only
collateral and at most

\[
\boxed{
\left\lfloor
\frac{2+B/(n-1)}{1-A}
\right\rfloor
}
\]

restored edges, including the two fixed paid-pair edges.

### Proof

CMR1558 makes the obstruction inequality in CMR1522 false at `Q=Q_*`.
Therefore CMR531 gives the candidate-free branch with `T_Z(delta)<Q_*`.
The restoration count is an integer, hence at most `Q_*-1=T_*`. ∎

The conclusion is pointwise for the exact selector host.  It does not replace
`A_L` by a coarse estimate unless that estimate is also strictly below one.

## 3. First restoration labels are finite

Consider a sequence of selector executions inside one fixed physical board and
one fixed envelope epoch.  Label a restoration incidence `(j,f)` **first** when
edge `f` has not been restored in any earlier selected execution of the epoch;
otherwise label it **repeated**.  Let

\[
N_{\rm first},
\qquad
N_{\rm rep},
\qquad
N_{\rm tot}
\]

be the corresponding incidence counts.

### Theorem CMR1560 -- PROVED

One has

\[
\boxed{
N_{\rm tot}=N_{\rm first}+N_{\rm rep},
\qquad
N_{\rm first}\le n^2.
}
\]

If the exact response-edge universe is used instead of the complete physical
board, the sharper bound is its cardinality; for the extension-free host this is
`n^2-n-1`.

After adjoining the monotone set of already restored physical labels to the
refined state, every first restoration is a strict finite-resource transition.
Only repeated restoration incidences remain in the return row.

### Proof

Every restoration incidence is uniquely first or repeated.  A physical board
of side `n` has `n^2` edge labels, and each label is first at most once.  Adding
a new label strictly enlarges a finite monotone set, exactly as the token and
private-edge coordinates in CMR1491. ∎

This is a bookkeeping refinement, not a claim that restoration itself is free.
Repeated restoration is precisely the unresolved return currency.

## 4. Exact subunit selector row

Refine the recurrent quotient by the monotone first-restoration label set.  Use
`R` for the repeated-return class and `S` for one fixed paid-pair selector class.

### Theorem CMR1561 -- PROVED

For an exact selector state with `A_L<1`, there is a deterministic response row
with

1. zero candidate-only selector offspring;
2. at most `T_*(A_L,|B_L|,n)` restoration incidences;
3. every first restoration on a strict finite-resource arc;
4. every remaining restoration incidence assigned to the repeated-return row.

Consequently the recurrent part of the selector row is componentwise dominated
by

\[
\boxed{(T_*,0)}
\]

in the ordered columns `(R,S)`.

### Proof

Choose the completion from CMR1559.  Its candidate count is zero, so no new
candidate credit remains in the selector coordinate.  Split its at most `T_*`
restorations by CMR1560.  First labels are strict resource transitions; repeated
labels are return incidences. ∎

The response may create structural or later-owner offspring, but those are
already off-diagonal under CMR1491 and the owner DAG.

## 5. Exact two-row spectral criterion

Suppose the unresolved repeated-return row has recurrent offspring bounds

\[
(\alpha,\beta)
\]

in columns `(R,S)`, where `alpha,beta>=0`.  Let one uniform selector cap be the
nonnegative integer `T`.  The recurrent two-row upper block is

\[
\boxed{
M=
\begin{pmatrix}
\alpha&\beta\\
T&0
\end{pmatrix}.
}
\]

### Theorem CMR1562 -- PROVED

The following are equivalent.

1. There is a positive vector `v` with `Mv<v`.
2. `rho(M)<1`.
3. One scalar strict inequality holds:
   \[
   \boxed{\alpha+\beta T<1.}
   \]

### Proof

Scale the return weight to one and write the selector weight as `x>0`.  The two
row inequalities are

\[
\alpha+\beta x<1,
\qquad
T<x.
\]

If `beta>0`, such an `x` exists exactly when

\[
T<\frac{1-\alpha}{\beta},
\]

which is the displayed condition.  If `beta=0`, the condition becomes
`alpha<1`; then any `x>T` works.  A finite nonnegative matrix has a positive
strict Lyapunov vector exactly when its spectral radius is below one. ∎

Equivalently, the positive root of

\[
\lambda^2-\alpha\lambda-\beta T=0
\]

is below one exactly under the same condition.

## 6. Rational and integer certificate form

### Theorem CMR1563 -- PROVED

Assume

\[
\alpha=\frac aD,
\qquad
\beta=\frac bD
\]

with integers `D>0` and `a,b>=0`.  The exact two-row condition is the strict
integer inequality

\[
\boxed{a+bT<D.}
\]

When `b>0`, one valid rational selector weight is any number strictly between

\[
T
\qquad\text{and}\qquad
\frac{D-a}{b};
\]

for example their midpoint.  When `b=0`, use any rational weight greater than
`T`.

### Proof

Clear the common denominator in CMR1562.  The displayed interval is nonempty
exactly when `a+bT<D`, and its endpoints give the two row inequalities. ∎

Thus the selector splice is compatible with the exact integer-certificate
format of CMR1332.

## 7. Host-uniform gap specialization

Fix a rational gap `eta` with

\[
0<\eta\le1
\]

and an unavailable-edge cap `B_0>=0`.

### Theorem CMR1564 -- PROVED

Every selector satisfying

\[
A_L\le1-\eta,
\qquad
|B_L|\le B_0
\]

has the uniform restoration cap

\[
\boxed{
T_*(A_L,|B_L|,n)
\le
T_{\eta,B_0}(n)
:=
\left\lfloor
\frac{2+B_0/(n-1)}{\eta}
\right\rfloor.
}
\]

Hence one coarse subunit selector class has recurrent row `(T_{eta,B_0}(n),0)`.
Its coupling with a return row `(alpha,beta)` is subcritical whenever

\[
\boxed{
\alpha+
\beta T_{\eta,B_0}(n)
<1.
}
\]

### Proof

The hypotheses give `1-A_L>=eta` and
`2+|B_L|/(n-1)<=2+B_0/(n-1)`.  Apply monotonicity to the floor formula in
CMR1559, then use CMR1562. ∎

The complementary branch `A_L>1-eta` has explicit candidate-only pressure.  It
must be treated by the line, height, prefix, carry or exact rook-profile rows;
it is not hidden inside restoration accounting.

## 8. Selector-return endpoint

### Corollary CMR1565 -- PROVED

The persistent paid-pair selector is no longer an undifferentiated recurrent
row.

1. For every exact host with `A_L<1`, the selector has zero candidate self-row
   and an explicit finite splice into repeated edge return.
2. First restoration labels are finite off-diagonal resources.
3. Under a uniform gap `A_L<=1-eta`, the selector-to-return coefficient is the
   explicit integer `T_{eta,B_0}(n)`.
4. Coupling to one return row reduces exactly to
   \[
   \alpha+\beta T<1.
   \]
5. Only the critical candidate regime `A_L>=1`, or a chosen near-critical band
   `A_L>1-eta`, requires an independent geometric candidate coefficient.

This does not prove the return coefficient or the critical candidate row
subcritical.  It replaces the subunit selector frontier by one exact return
splice and one strict integer inequality.

Threshold minimality, restoration-label accounting, uniform-gap caps and the
exact two-row criterion are checked in
[`scripts/verify_prime_power_paid_pair_selector_return_splice.py`](../scripts/verify_prime_power_paid_pair_selector_return_splice.py).
