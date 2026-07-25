# Diffuse-shadow direct allocation

The defect-score theorem PP3lz converts controller-cell and same-slot anchor
counts into the complementary degree required by the global label matching.  This
chapter gives a clean asymptotic corollary: uniformly diffuse excess shadow is
already enough for direct completion.

The theorem separates the remaining direct obstruction from average density.
Failure must concentrate in a nearly dead label, one macro with large total
excess shadow, or a same-slot anchor row/column.

## 1. Uniform domain margin

Fix constants

\[
 0<\gamma<1,
 \qquad
 0<\delta<1-\gamma.
\]

Say the controller-cell defects have **margin \(\delta\)** when every macro and
label satisfy

\[
 a_i(A),b_i(B)
 \le
 (1-\gamma-\delta)R.
\]

Then every denominator in PP3ly is at least \(\delta R\).

### Proposition PP3mc -- PROVED

Assume margin \(\delta\).  If

\[
 A_i,B_i\le\varepsilon RT
\]

and

\[
 U_i(A)\le\varepsilon RT
\]

for every macro \(i\) and movement label \(A\), then

\[
 \boxed{
 \rho_i(A)
 \le
 \frac{2\varepsilon}{\delta}T.
 }
\]

If additionally

\[
 \frac1M\sum_{j=1}^M V_j(B)
 \le
 \varepsilon RT
\]

for every refill label \(B\), then

\[
 \boxed{
 \kappa(B)
 \le
 \frac{2\varepsilon}{\delta}T.
 }
\]

#### Proof

The margin gives

\[
 (1-\gamma)R-a_i(A)
 \ge
 \delta R.
\]

The numerator of \(\rho_i(A)\) is at most

\[
 B_i+U_i(A)
 \le
 2\varepsilon RT.
\]

Divide.  For \(\kappa(B)\), apply the same denominator bound in every macro and
average

\[
 A_j+V_j(B).
\]

The first terms have average at most \(\varepsilon RT\), and the displayed
anchor hypothesis bounds the second terms. ∎

## 2. Direct completion from diffuse shadow

### Theorem PP3md -- PROVED

Let \(h>0\) satisfy

\[
 T\exp\left(-\frac{h^2}{32T}\right)<1.
\]

Assume the margin and diffuse-mass hypotheses of PP3mc.  If

\[
 \boxed{
 \frac{4\varepsilon}{\delta}T
 \le
 T-h,
 }
\]

then the controller-aware global label allocation exists and PP3hq gives a
saturated no-three patch of width

\[
 \Omega(m^{21/40}).
\]

#### Proof

For every incompatible triple,

\[
 \rho_i(A)+\kappa(B)
 \le
 \frac{4\varepsilon}{\delta}T
 \le
 T-h.
\]

Apply PP3lz. ∎

In particular, with

\[
 h=8\sqrt{T\log T}=o(T),
\]

any fixed \(\delta>0\) and any sequence \(\varepsilon=o(1)\) satisfy the
inequality for all sufficiently large \(T\).

## 3. Excess-potential form

### Corollary PP3me -- PROVED

Under margin \(\delta\), the hypotheses

\[
 \Xi_i=o(RT)
\]

uniformly in \(i\),

\[
 \max_{i,A}U_i(A)=o(RT),
\]

and

\[
 \max_B\frac1M\sum_jV_j(B)=o(RT)
\]

imply direct controller-aware global allocation.

#### Proof

PP3mb gives

\[
 A_i+B_i\le\Xi_i.
\]

Choose \(\varepsilon=o(1)\) dominating the three normalized quantities and apply
PP3md. ∎

Thus a successful dynamic preparation theorem does not need to make every
candidate cell safe.  It only needs:

1. a fixed positive labelwise domain margin;
2. vanishing macro-total excess shadow;
3. vanishing same-slot anchor row and average-column mass.

## 4. Exact remaining direct obstruction

### Corollary PP3mf -- PROVED

If direct allocation still fails along an asymptotic sequence, then at least one
of the following persists along a subsequence.

1. **Nearly dead movement label:** for some fixed \(\delta>0\),
   \[
   a_i(A)>(1-\gamma-\delta)R.
   \]
2. **Nearly dead refill label:**
   \[
   b_i(B)>(1-\gamma-\delta)R.
   \]
3. **Macro excess-shadow concentration:**
   \[
   \Xi_i=\Omega(RT).
   \]
4. **Same-slot anchor row concentration:**
   \[
   U_i(A)=\Omega(RT).
   \]
5. **Same-slot anchor average-column concentration:**
   \[
   \frac1M\sum_jV_j(B)=\Omega(RT).
   \]

#### Proof

If none persists, choose a fixed margin \(\delta>0\) and a common
\(\varepsilon=o(1)\) satisfying PP3me.  The direct allocation then exists, a
contradiction. ∎

This reduces the direct route from an abstract graph-density theorem to five
explicit geometric concentration objects.  The dynamic \(\Xi\)-trades target the
third object.  The first two require labelwise shadow regularisation, while the
last two are governed by the same-edge product equation and divisor-energy
machinery.