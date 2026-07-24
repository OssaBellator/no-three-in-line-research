# Linear displacement obstruction for completed reciprocals

This chapter closes one of the quantitative CM3 targets negatively for the
valuation-completed reciprocal family. Although these channels are full
nonlinear permutations and have an exact line-intersection calculus, their
same-channel displacement multiplicity is necessarily large.

Let

\[
N=p^k,
\qquad p\text{ odd},
\qquad k\ge2,
\]

and let \(R_{\mathbf c}\) be a completed reciprocal channel. Only the unit
stratum parameter \(c_0\) is relevant below.

## 1. A top-digit translation

Put

\[
a=p^{k-1}=N/p.
\]

For every unit column `x` with

\[
0\le x<N-a,
\]

both `x` and `x+a` remain in the unit stratum. Modulo `N`,

\[
\begin{aligned}
R_{\mathbf c}(x+a)-R_{\mathbf c}(x)
&\equiv
c_0\bigl((x+a)^{-1}-x^{-1}\bigr)\\
&\equiv
-c_0a\,[x(x+a)]^{-1}
\pmod N.
\end{aligned}
\]

Because multiplication by `a=N/p` only retains a coefficient modulo `p`,
and because \(x+a\equiv x\pmod p\), define

\[
q_x\equiv c_0x^{-2}\pmod p,
\qquad 1\le q_x\le p-1.
\]

Then

\[
R_{\mathbf c}(x+a)-R_{\mathbf c}(x)
\equiv -q_xa\pmod N.
\]

## 2. Linear exact displacement multiplicity

### Theorem CMR14 — PROVED

For every odd prime power \(N=p^k\) with \(k\ge2\), and for every choice of
completed-reciprocal parameters, there is an exact lifted displacement vector

\[
(a,d),
\qquad a=p^{k-1},
\]

that occurs for at least

\[
(p-1)p^{k-2}
=
\frac{p-1}{p^2}N
\]

ordered same-channel pairs.

More explicitly, for some \(q\in\{1,\ldots,p-1\}\), one of

\[
(a,-qa)
\qquad\text{or}\qquad
(a,(p-q)a)
\]

has that multiplicity.

### Proof

The map

\[
z\longmapsto c_0z^{-2}
\]

on \(\mathbb F_p^\times\) has image size \((p-1)/2\), and every image value
has exactly two preimages, `z` and `-z`.

The interval

\[
0\le x<N-a
\]

has length

\[
N-a=(p-1)p^{k-1},
\]

which is divisible by `p`. Hence every residue class modulo `p` occurs
exactly

\[
(p-1)p^{k-2}
\]

times in this interval. For each fixed image value `q`, the two corresponding
unit residue classes therefore supply

\[
2(p-1)p^{k-2}
\]

columns `x` with

\[
R_{\mathbf c}(x+a)-R_{\mathbf c}(x)
\equiv-qa\pmod N.
\]

The exact lifted row difference lies strictly between `-N` and `N`. The only
two integers in that range congruent to `-qa` modulo `N=pa` are

\[
-qa
\qquad\text{and}\qquad
(p-q)a.
\]

At least half of the columns belonging to the fixed value `q` choose the same
exact difference. Thus one exact displacement occurs at least
\((p-1)p^{k-2}\) times. ∎

## 3. Consequence for CM3

The completed-reciprocal family cannot satisfy a modulus-independent bounded
displacement hypothesis. For every fixed odd prime base `p`, its maximum
same-channel displacement multiplicity is \(\Omega(N)\).

Therefore the prime-field implication

\[
\text{bounded displacement multiplicity}
\Longrightarrow
\text{small dyadic secant shadow}
\]

cannot be transferred directly to completed reciprocals. Any successful use
of this family must do one of the following:

1. quotient out the top-digit translation classes;
2. charge the repeated vectors to an explicit valuation block or absorber;
3. randomize or vary the unit-stratum parameter by blocks rather than use one
   global completed reciprocal;
4. replace displacement multiplicity by a collision-aware weighted bound.

This obstruction does not refute the line-cap or tangent-cell results. It
shows that the remaining prime-power route needs a structured-collision
repair theorem rather than the exact prime-hyperbola codegree argument.

The finite check is
[`scripts/verify_prime_power_displacement_obstruction.py`](../scripts/verify_prime_power_displacement_obstruction.py).
