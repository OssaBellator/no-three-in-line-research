# Witness-line survivor congestion and the rich-line barrier

The line-supported cover PP3lo deletes all but one allowed endpoint cell on each
witness line.  That construction has congestion one for a single line, but a
linear bank of linear-rich **distinct geometric lines** behaves differently.
This chapter records the exact load conservation, a geometric union lower bound,
and the fractional survivor-allocation problem.

The conclusion is corrective: rich Hall-derived line banks cannot in general be
absorbed by applying the one-line cover independently.  They require the
owner-line reconfiguration energy of PP3lg--PP3ll or another genuine trade.

## 1. Distinct traces and survivor covers

Let

\[
 G_0=(L,R;E),
 \qquad |L|=|R|=q,
\]

be an endpoint host.  Let \(\mathcal L\) be a family of distinct nonaxis
geometric lines.  For \(\lambda\in\mathcal L\), let

\[
 P_\lambda=P_E(\lambda)
\]

be its nonempty allowed endpoint trace.  By PP3lm, every \(P_\lambda\) is a
matching in the resource bipartite graph.

Choose one survivor

\[
 s_\lambda\in P_\lambda
\]

and delete

\[
 D_\lambda=P_\lambda\setminus\{s_\lambda\}.
\]

The resulting simple unary cover is

\[
 C_s=\bigcup_{\lambda\in\mathcal L}D_\lambda.
\]

Repeated typed witnesses on the same geometric line should be merged before this
construction, because one deletion set covers all conflicts assigned to that
line.

## 2. Exact multiplicity-load conservation

For an endpoint resource \(v\in L\cup R\), define the line-multiplicity deletion
load

\[
 M_s(v)
 =
 |\{\lambda\in\mathcal L:
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
 \max_v M_s(v)
 \ge
 \frac1q
 \sum_{\lambda\in\mathcal L}(|P_\lambda|-1).
 }
\]

#### Proof

On one line, every deleted trace cell uses two endpoint resources, and the trace
is a matching.  Hence that line contributes exactly \(2(|P_\lambda|-1)\) to the
sum of multiplicity loads.  Sum over the lines and average over the \(2q\)
resources. ∎

This is a barrier for the **multiplicity estimate** in PP3lo.  Distinct line
deletions can overlap as cells, so a geometric union estimate is also needed for
the actual simple cover.

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

Distinct geometric lines meet in at most one point.  Therefore

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

Hence its endpoint-resource congestion obeys

\[
 \boxed{
 \Delta(C_s)
 \ge
 \frac1q\,
 \frac{S^2}{S+r(r-1)}.
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
 =
 \left(\sum_{a\in C_s}m(a)\right)^2
 \le
 |C_s|\sum_a m(a)^2.
\]

This proves the union bound.  The bipartite graph \(C_s\) has \(2|C_s|\)
resource incidences on \(2q\) resources, so its maximum degree is at least
\(|C_s|/q\). ∎

### Corollary PP3lt -- PROVED

Fix constants \(\alpha,\beta>0\).  Suppose

\[
 r\ge\beta q
\]

and every allowed trace satisfies

\[
 |P_\lambda|\ge\alpha q.
\]

Then every one-survivor line cover has

\[
 \Delta(C_s)
 \ge
 \left(
 \frac{\alpha^2\beta}{\alpha+\beta}
 -o(1)
 \right)q.
\]

#### Proof

Here

\[
 S\ge r(\alpha q-1).
\]

Substitute this and \(r\ge\beta q\) into PP3ls and divide by \(q\). ∎

Thus a linear bank of linear-rich distinct lines necessarily creates linear
unary congestion under the PP3ln deletion pattern.  In particular, the rich
recapture bank of PP3kp cannot be completed merely by deleting all but one cell
from each designated line.

## 4. Fractional survivor allocation

The exact obstruction can be expressed as a fractional assignment problem.  For
every \(\lambda\in\mathcal L\) and \(a\in P_\lambda\), choose
\(x_{\lambda,a}\ge0\) with

\[
 \sum_{a\in P_\lambda}x_{\lambda,a}=1.
\]

For a resource \(v\), let \(a_\lambda(v)\) denote the unique trace cell incident
with \(v\), when it exists.  Define the fractional deletion load

\[
 \ell_x(v)
 =
 \sum_{\lambda:v\in P_\lambda}
 \left(1-x_{\lambda,a_\lambda(v)}\right).
\]

Put

\[
 \sigma^*(\mathcal L)
 =
 \min_x\max_v\ell_x(v).
\]

### Theorem PP3lu -- PROVED

The fractional survivor congestion has the exact dual form

\[
 \boxed{
 \sigma^*(\mathcal L)
 =
 \max_y
 \left[
 \sum_{v}d_{\mathcal L}(v)y_v
 -
 \sum_{\lambda\in\mathcal L}
 \max_{a\in P_\lambda}
 \bigl(y_{\ell(a)}+y_{r(a)}\bigr)
 \right],
 }
\]

where the maximum is over nonnegative resource prices satisfying

\[
 \sum_v y_v\le1.
\]

#### Proof

Write the primal constraints as

\[
 t+
 \sum_{\lambda:v\in P_\lambda}
 x_{\lambda,a_\lambda(v)}
 \ge
 d_{\mathcal L}(v).
\]

Use nonnegative dual variables \(y_v\) for these inequalities and a free variable
\(\alpha_\lambda\) for each survivor equality.  The variable \(t\) gives
\(\sum_vy_v\le1\).  For a trace cell \(a\in P_\lambda\), dual feasibility is

\[
 y_{\ell(a)}+y_{r(a)}+\alpha_\lambda\le0.
\]

At the optimum,

\[
 \alpha_\lambda
 =
 -\max_{a\in P_\lambda}
 \bigl(y_{\ell(a)}+y_{r(a)}\bigr).
\]

Substitution gives the displayed objective.  Finite-dimensional linear
programming duality completes the proof. ∎

The dual measures resource price that cannot be protected by choosing one cell
on each trace.

## 5. Randomized rounding

### Theorem PP3lv -- PROVED

There is an integral survivor choice satisfying

\[
 \boxed{
 \max_v M_s(v)
 \le
 \sigma^*(\mathcal L)
 +4\sqrt{(\sigma^*(\mathcal L)+1)\log(2q)}
 +4\log(2q).
 }
\]

Consequently, if

\[
 \sigma^*(\mathcal L)=o(q),
\]

then the PP3lo survivor cover has multiplicity congestion \(o(q)\), and therefore
simple resource congestion \(o(q)\).

#### Proof

Take an optimal fractional solution and choose the survivor on each line
independently according to \(x_{\lambda,\cdot}\).  For a fixed resource \(v\),
\(M_s(v)\) is a sum of independent Bernoulli variables with expectation at most
\(\sigma^*(\mathcal L)\).  Bernstein's inequality and a union bound over the
\(2q\) resources give the displayed bound with positive probability.  The final
statement follows because the additive term is \(o(q)\) whenever
\(\sigma^*(\mathcal L)=o(q)\). ∎

## 6. Revised witness-line endpoint

### Corollary PP3lw -- PROVED

The full-trace line-cover route has the following exact alternatives.

1. \(\sigma^*(\mathcal L)=o(q)\).  Then survivor rounding gives a unary cover of
   congestion \(o(q)\), after which PP3lc or PP3ld applies.
2. \(\sigma^*(\mathcal L)\ge\rho q\) along a subsequence.  Then PP3lu supplies a
   unit resource-price vector for which a linear amount of line-incidence price
   remains unprotected after the best survivor on every trace.
3. If there are \(\Omega(q)\) distinct lines with \(\Omega(q)\)-sized traces,
   PP3lt already forces the second regime.

Therefore one-line unary absorption closes sparse total trace volume, but it
cannot close the second-generation grid-rich pencil.  The latter must be attacked
by owner-line reassignment, a rectangle/tomographic trade, or a more economical
conflict cover that does not delete almost the whole trace.

This chapter also corrects the scope of PP3lp: low witness-line overlap is a
sufficient endpoint, not a mechanism capable of absorbing every linear bank of
linear-rich lines.