# Witness-line survivor congestion and the rich-line barrier

The line-supported cover PP3lo deletes all but one allowed endpoint cell on each
witness line.  This has congestion one for a single line, but a linear bank of
linear-rich **distinct geometric lines** behaves differently.

Repeated typed witnesses on the same geometric line must first be merged: one
deletion set covers all conflicts assigned to that line.  The barrier below
concerns the number of distinct geometric traces after this merging.

## 1. Survivor covers

Let

\[
G_0=(L,R;E),
\qquad |L|=|R|=q,
\]

and let \(\mathcal L\) be a family of distinct nonaxis geometric lines.  For
\(\lambda\in\mathcal L\), let

\[
P_\lambda=P_E(\lambda)
\]

be its nonempty allowed trace.  By PP3lm, every trace is a matching in the
endpoint-resource graph.

Choose one survivor \(s_\lambda\in P_\lambda\), put

\[
D_\lambda=P_\lambda\setminus\{s_\lambda\},
\]

and define the simple unary cover

\[
C_s=\bigcup_{\lambda\in\mathcal L}D_\lambda.
\]

## 2. Exact multiplicity-load conservation

For a resource \(v\in L\cup R\), define

\[
M_s(v)
=
|\{\lambda:
P_\lambda\text{ contains a cell incident with }v,
\ s_\lambda\text{ is not incident with }v\}|.
\]

### Proposition PP3lr -- PROVED

For every survivor choice,

\[
\boxed{
\sum_{v\in L\cup R}M_s(v)
=
2\sum_{\lambda\in\mathcal L}(|P_\lambda|-1).
}
\]

Consequently

\[
\boxed{
\max_vM_s(v)
\ge
\frac1q
\sum_{\lambda\in\mathcal L}(|P_\lambda|-1).
}
\]

#### Proof

On one trace, every deleted cell uses two resources and distinct deleted cells
use distinct resources on each side.  Thus the trace contributes exactly
\(2(|P_\lambda|-1)\) to the total multiplicity load.  Sum and average over the
\(2q\) resources. ∎

This controls the multiplicity estimate.  A geometric union bound is needed for
the actual simple cover because deletions from different lines may overlap.

## 3. Geometric union lower bound

Put

\[
r=|\mathcal L|,
\qquad
S=\sum_{\lambda\in\mathcal L}(|P_\lambda|-1).
\]

For a cell \(a\), let

\[
m(a)=|\{\lambda:a\in D_\lambda\}|.
\]

Distinct geometric lines meet in at most one point, so

\[
\sum_a\binom{m(a)}2
\le
\binom r2.
\]

### Theorem PP3ls -- PROVED

Every survivor cover satisfies

\[
\boxed{
|C_s|
\ge
\frac{S^2}{S+r(r-1)}.
}
\]

Hence

\[
\boxed{
\Delta(C_s)
\ge
\frac1q\frac{S^2}{S+r(r-1)}.
}
\]

#### Proof

One has

\[
\sum_a m(a)=S
\]

and

\[
\sum_a m(a)^2
=
S+2\sum_a\binom{m(a)}2
\le
S+r(r-1).
\]

Cauchy--Schwarz gives

\[
S^2
\le
|C_s|\sum_a m(a)^2.
\]

Finally, the bipartite graph \(C_s\) has average resource degree
\(|C_s|/q\). ∎

### Corollary PP3lt -- PROVED

Fix constants \(\alpha,\beta>0\).  If

\[
r\ge\beta q
\]

and every trace has

\[
|P_\lambda|\ge\alpha q,
\]

then

\[
\boxed{
\Delta(C_s)
\ge
\left(
\frac{\alpha^2\beta}{\alpha+\beta}-o(1)
\right)q.
}
\]

#### Proof

Use

\[
S\ge r(\alpha q-1)
\]

in PP3ls.  The resulting asymptotic lower bound is increasing in \(r/q\), so its
minimum under \(r/q\ge\beta\) occurs at \(\beta\). ∎

Therefore a linear number of distinct geometric lines with linear traces cannot
be absorbed by the one-survivor deletion pattern at sublinear congestion.

For the PP3kp recapture alternative this gives a dichotomy:

1. linearly many typed designated witnesses collapse onto few geometric lines,
   producing a repeated-line credit concentration; or
2. linearly many distinct geometric designated lines remain, and PP3lt rules out
   naive unary survivor covering.

The second case requires owner-line reassignment or another genuine trade.

## 4. Fractional survivor allocation

Choose variables \(x_{\lambda,a}\ge0\) satisfying

\[
\sum_{a\in P_\lambda}x_{\lambda,a}=1.
\]

For a resource \(v\), let \(a_\lambda(v)\) be the unique trace cell incident with
\(v\), when it exists, and define

\[
\ell_x(v)
=
\sum_{\lambda:v\in P_\lambda}
\left(1-x_{\lambda,a_\lambda(v)}\right).
\]

Put

\[
\sigma^*(\mathcal L)=\min_x\max_v\ell_x(v).
\]

### Theorem PP3lu -- PROVED

The fractional survivor congestion has the exact dual

\[
\boxed{
\sigma^*(\mathcal L)
=
\max_y
\left[
\sum_vd_{\mathcal L}(v)y_v
-
\sum_{\lambda\in\mathcal L}
\max_{a\in P_\lambda}
\bigl(y_{\ell(a)}+y_{r(a)}\bigr)
\right],
}
\]

where \(y_v\ge0\) and

\[
\sum_vy_v\le1.
\]

#### Proof

Write the primal resource constraints as

\[
t+
\sum_{\lambda:v\in P_\lambda}
 x_{\lambda,a_\lambda(v)}
\ge
d_{\mathcal L}(v).
\]

Dual resource variables are nonnegative and the survivor equalities have free
dual variables.  The variable \(t\) gives \(\sum_vy_v\le1\), while a trace cell
\(a\in P_\lambda\) gives

\[
y_{\ell(a)}+y_{r(a)}+\alpha_\lambda\le0.
\]

Optimizing \(\alpha_\lambda\) yields the displayed objective. ∎

## 5. Randomized rounding

### Theorem PP3lv -- PROVED

There is an integral survivor choice satisfying

\[
\boxed{
\max_vM_s(v)
\le
\sigma^*(\mathcal L)
+4\sqrt{(\sigma^*(\mathcal L)+1)\log(2q)}
+4\log(2q).
}
\]

Thus \(\sigma^*(\mathcal L)=o(q)\) gives a simple unary cover of congestion
\(o(q)\).

#### Proof

Choose each line's survivor independently according to an optimal fractional
solution.  For fixed \(v\), \(M_s(v)\) is a Bernoulli sum of expectation at most
\(\sigma^*(\mathcal L)\).  Bernstein's inequality and a union bound over the
\(2q\) resources give the stated bound.  Simple cover degree is at most
multiplicity load. ∎

## 6. Revised endpoint

### Corollary PP3lw -- PROVED

The full-trace survivor route has three exact regimes.

1. \(\sigma^*(\mathcal L)=o(q)\): survivor rounding gives a low-congestion unary
   cover, after which PP3lc or PP3ld applies.
2. \(\sigma^*(\mathcal L)\ge\rho q\) along a subsequence: PP3lu supplies a unit
   resource-price vector with linear unavoidable deletion price.
3. A linear bank of linear-rich distinct lines automatically lies in regime 2 by
   PP3lt.

Hence one-line absorption closes sparse total trace volume.  It cannot close the
second-generation grid-rich pencil.  The unresolved conversion must move the
owner lines, use a rectangle/tomographic trade, or exploit a substantially more
economical conflict cover than deleting almost the whole trace.