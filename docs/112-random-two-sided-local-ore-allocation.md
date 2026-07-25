# Random two-sided local Ore allocation

The deterministic two-sided theorem PP3mq requires global row and column
nondegrees whose thresholds sum to at most the local macro width \(W\). Random
balanced ownership gives a softer alternative: a global nondegree is sampled
down by the factor \(W/T=1/M\) inside each macro.

The resulting endpoint uses a per-macro complementary-degree condition and
independent random balanced partitions of the two numerical label sets.

## 1. Balanced hypergeometric counts

Let a uniformly random balanced map partition a \(T=MW\) element set into
\(M\) labelled classes of size \(W\). For a fixed subset \(D\) and class \(i\),
put

\[
X_i(D)=|D\cap\mathcal C_i|.
\]

### Lemma PP3na -- PROVED FROM HOEFFDING'S INEQUALITY FOR SAMPLING WITHOUT REPLACEMENT

For every \(t>0\),

\[
\boxed{
\Pr\left(
X_i(D)>
\frac{W|D|}{T}+t
\right)
\le
\exp\left(-\frac{2t^2}{W}\right).
}
\]

#### Proof

The class \(\mathcal C_i\) is a uniform \(W\)-subset of the ground set, so
\(X_i(D)\) is hypergeometric with mean \(W|D|/T\). Apply the standard Hoeffding
upper-tail inequality for sampling without replacement. ∎

## 2. Random local complementary-degree theorem

For macro \(i\), write

\[
\overline d_i(A)=T-\deg_{J_i}(A),
\qquad
\overline e_i(B)=T-\deg_{J_i}(B).
\]

Choose independent uniformly random balanced partitions

\[
\mathcal A=\dot\bigcup_i\mathcal A_i,
\qquad
\mathcal B=\dot\bigcup_i\mathcal B_i,
\]

with every class of size \(W\).

### Theorem PP3nb -- PROVED

Let \(h,t>0\) satisfy

\[
\boxed{2t\le\frac{Wh}{T}}
\]

and

\[
\boxed{
2MT\exp\left(-\frac{2t^2}{W}\right)<1.
}
\]

Assume that every macro nonedge \((A,B)\notin J_i\) satisfies

\[
\boxed{
\overline d_i(A)+\overline e_i(B)
\le
T-h.
}
\]

Then there are balanced partitions for which every induced graph

\[
J_i[\mathcal A_i,\mathcal B_i]
\]

contains a perfect matching. The union of the local matchings uses every
movement and refill label exactly once.

For the controller-aware compatibility graphs, the full patch follows from
PP3ho and PP3hq.

#### Proof

For fixed \(i,A\), the number of nonneighbors of \(A\) that land in
\(\mathcal B_i\) is at most

\[
\frac{W\overline d_i(A)}T+t
\]

except with probability at most \(\exp(-2t^2/W)\), by PP3na. The transposed
statement holds for every fixed \(i,B\) and the random movement partition.

There are \(MT\) row counts and \(MT\) column counts. The second displayed
hypothesis and a union bound give balanced partitions for which all bounds hold
simultaneously.

Fix a macro and a nonedge \((A,B)\) of its induced graph. Its two induced
nondegrees have sum at most

\[
\frac WT
\bigl(
\overline d_i(A)+\overline e_i(B)
\bigr)
+2t
\le
W-\frac{Wh}{T}+2t
\le W.
\]

Therefore its induced endpoint-degree sum is at least \(W\). Apply PP3gj to each
induced balanced graph. ∎

## 3. Explicit asymptotic slack

### Corollary PP3nc -- PROVED

It is sufficient to take

\[
\boxed{
t=\sqrt{W\log(4MT)}}
\]

and

\[
\boxed{
h=2T\sqrt{\frac{\log(4MT)}W}.}
\]

For all sufficiently large \(T\), the probability condition in PP3nb holds and
\(h=o(T)\) whenever \(W\to\infty\).

At the slab-optimal exponents,

\[
T=m^{21/40+o(1)},
\qquad
W=m^{19/40+o(1)},
\]

so

\[
\boxed{
h=m^{23/80+o(1)}.}
\]

#### Proof

The first condition of PP3nb holds with equality. Also

\[
2MT\exp\left(-\frac{2t^2}{W}\right)
=
2MT\,(4MT)^{-2}
<1.
\]

Finally,

\[
\frac hT
=
2\sqrt{\frac{\log(4MT)}W}
=o(1).
\]

The exponent is

\[
\frac{21}{40}-\frac{19}{80}=\frac{23}{80}.
\]

∎

This slack is larger than the \(m^{21/80+o(1)}\) fluctuation in the one-sided
random ownership theorem by the factor \(\sqrt M=m^{1/40+o(1)}\), but remains
sublinear in \(T\).

## 4. Controller-defect score form

### Corollary PP3nd -- PROVED

Let \(\rho_i(A)\) and \(\chi_i(B)\) be the controller-defect nondegree upper
bounds from PP3ly. If every incompatible triple satisfies

\[
\boxed{
\rho_i(A)+\chi_i(B)
\le
T-h,
}
\]

with \(h\) satisfying PP3nb, then random two-sided ownership gives the complete
controller-aware allocation and full patch.

#### Proof

The true row and column nondegrees are bounded by \(\rho_i(A)\) and
\(\chi_i(B)\). Apply PP3nb. ∎

## 5. Revised direct-allocation alternatives

### Corollary PP3ne -- PROVED

The controller-aware allocation is complete under any one of the following
independent deterministic or probabilistic interfaces.

1. One-sided ownership bottleneck versus refill slack: PP3mx.
2. Deterministic two-sided ownership at local thresholds: PP3mr.
3. Random two-sided ownership from per-macro complementary degree: PP3nd.
4. Random one-sided ownership from average refill complementary degree: PP3lz.

If all four fail, the remaining numerical obstruction simultaneously contains:

- a one-sided ownership Hall/slack gap;
- failure of local-scale two-sided thresholds;
- a macro nonedge with large complementary defect score
  \(\rho_i(A)+\chi_i(B)>T-h\);
- and an average-refill complementary score failure
  \(\rho_i(A)+\kappa(B)>T-h'\).

Thus no single abstract density condition remains. Direct failure must survive
four allocation architectures with different averaging and routing mechanisms.