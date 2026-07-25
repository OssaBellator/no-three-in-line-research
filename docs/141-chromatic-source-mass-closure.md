# Chromatic source-mass closure

PP3sy selects one unary-independent colour class using the global objective

\[
K^2\frac{kP}{H^2}
+
K^3\frac{k^2Q}{H^3}
+
K\frac{kA}{H^2}
+
K^2\frac{k^2B}{H^3}.
\]

The first two terms are source-validity terms.  The two-scale endpoint estimates
PP3jl are strong enough to absorb the extra chromatic factors \(k\) and \(k^2\)
when the secondary bank exponent is chosen below \(1/60\).  Thus the global paid
frontier reduces to controller-shadow weight.

## 1. Quantitative secondary scale

Let the original resource bank have size

\[
Q_0=\Omega(m^{21/40}).
\]

Fix

\[
0<\kappa<\frac1{60}
\]

and choose the adaptive secondary bank size

\[
q\le m^\kappa,
\qquad
q\longrightarrow\infty,
\]

as in PP3nq, with any additional slowing needed to make the unary-density
condition hold.

After PP3nr, write \(q'=(1-o(1))q\).  Let the extracted rectangle bank have size

\[
H\ge c q'
\]

for a fixed \(c>0\), as supplied by the linear rectangle extraction PP3ok.

Let \(k\) be the equitable-colouring count of PP3sv.  Always

\[
1\le k\le H.
\]

## 2. Anchored-pair term

Let \(P\) be the total remaining support-rank-four anchored-pair count on the
secondary endpoint resources.

### Proposition PP3tb -- PROVED

One has

\[
\frac{kP}{H^2}=o(1).
\]

#### Proof

PP3jj--PP3jl give

\[
\frac{P}{q^2}
=
O\left(
\frac{mD_mq^2}{Q_0^2}
\right)
=
m^{-1/20+2\kappa+o(1)}.
\]

Since \(k\le H\) and \(H=\Theta(q)\) up to fixed constants,

\[
\frac{kP}{H^2}
\le
\frac{P}{H}
=
O\left(
q\frac{P}{q^2}
\right)
=
m^{-1/20+3\kappa+o(1)}
=o(1)
\]

because \(3\kappa<1/20\). ∎

The divisor factor \(D_m=m^{o(1)}\) is absorbed in the final exponent.

## 3. Inserted-triple term

Let

\[
Q=Q_4+Q_5+Q_6
\]

be the total remaining inserted collinear-triple count, separated by endpoint-
index support rank as in PP3jk.

### Proposition PP3tc -- PROVED

One has

\[
\frac{k^2Q}{H^3}=o(1).
\]

#### Proof

The random subbank estimates PP3jl give

\[
Q_4=O\left(\frac{q^4}{Q_0}\right),
\qquad
Q_5=O\left(\frac{q^5}{Q_0}\right),
\qquad
Q_6=O\left(\frac{q^6}{Q_0}\right).
\]

Since \(k\le H\),

\[
\frac{k^2Q}{H^3}
\le
\frac QH.
\]

Using \(H=\Omega(q)\), the three contributions are bounded by

\[
O\left(
\frac{q^3}{Q_0}
+
\frac{q^4}{Q_0}
+
\frac{q^5}{Q_0}
\right).
\]

The largest term has exponent

\[
5\kappa-\frac{21}{40}<0,
\]

indeed with substantial slack for \(\kappa<1/60\).  Hence the sum is \(o(1)\). ∎

Deleting endpoints or pruning rectangle resources can only decrease these
pattern counts.

## 4. Source-validity part of the chromatic objective

### Corollary PP3td -- PROVED

At the scale \(\kappa<1/60\),

\[
K^2\frac{kP}{H^2}
+
K^3\frac{k^2Q}{H^3}
=o(1)
\]

for every equitable-colouring count \(1\le k\le H\).

#### Proof

The spread constant \(K\) is fixed.  Apply PP3tb and PP3tc. ∎

Thus even the worst possible sublinear-unary chromatic complexity does not
consume a positive part of the paid budget through source-invalid pairs or
triples.

## 5. Pure shadow-weight completion criterion

### Theorem PP3te -- PROVED

Under the preceding hypotheses, a source-admissible strict paid cross-block state
exists whenever

\[
K\frac{kA}{H^2}
+
K^2\frac{k^2B}{H^3}
<1-o(1).
\]

In particular it is sufficient that

\[
kA=o(H^2)
\]

and

\[
k^2B=o(H^3).
\]

#### Proof

Insert PP3td into the global paid criterion PP3sy. ∎

The quantities \(A,B\) are the complete unary and binary controller-shadow
weights of candidate cells supported inside the rectangle bank.  Direct
designated recapture has already been excluded from the cross states.

## 6. Revised chromatic weighted endpoint

### Corollary PP3tf -- PROVED

For zero-density hard-unary support and secondary exponent
\(\kappa<1/60\), failure of the superregular cross-block conversion forces

\[
kA=\Omega(H^2)
\]

or

\[
k^2B=\Omega(H^3).
\]

Source-invalid anchored-pair and inserted-triple mass are no longer part of the
chromatically normalized frontier.

#### Proof

Negate PP3te. ∎

The remaining rectangle obstruction is therefore purely controller-shadow
collateral: unary weight at scale \(H^2/k\) or binary weight at scale
\(H^3/k^2\), together with the separate positive-density hard-unary branch.