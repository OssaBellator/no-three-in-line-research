# Summing the singular same-stratum collision class

CMR47 isolates one potentially singular carry class in the critical stratum
`r=t`. Its total Hensel multiplicity can nevertheless be summed directly.

Retain the notation

\[
M=p^{k-t},
\qquad
a=p^tA,
\qquad d\mid A,
\]

and work in the same-stratum cell

\[
v_p(x)=v_p(x+a)=t.
\]

For a divisor collision, CMR47 gives

\[
dm\,u(u+A)+Ac_t\equiv0\pmod M,
\]

where

\[
0<|m|<M/d,
\qquad p\nmid m.
\]

After division by `dm`, the discriminant is

\[
\Delta_m
=A^2-4Ac_t(dm)^{-1}.
\]

Since `A,d,m,c_t` are units,

\[
v_p(\Delta_m)
=
v_p(dmA-4c_t).
\]

## 1. Layer-cake bound

### Theorem CMR50 — PROVED

The total number of possible critical same-stratum parameters `u` over all
signed carry values `m` is less than

\[
\frac{6M}d+2\sqrt M.
\]

Consequently the actual number of divisor collisions in the critical stratum
`r=t` satisfies the same bound.

### Proof

Put

\[
e=k-t,
\qquad
E=\lfloor e/2\rfloor,
\qquad
R=M/d.
\]

For one fixed `m`, the odd-prime square-root classification bounds the number
of roots by

\[
2p^{\min(\lfloor v_p(dmA-4c_t)/2\rfloor,E)}.
\]

Let

\[
W(m)=p^{\min(\lfloor v_p(dmA-4c_t)/2\rfloor,E)}.
\]

Use the exact layer decomposition

\[
W(m)
=
1+
\sum_{s=1}^{E}
(p^s-p^{s-1})
\mathbf1_{p^{2s}\mid dmA-4c_t}.
\]

There are fewer than `2R` signed integers with `0<|m|<R`. For each `s`, the
linear congruence

\[
dmA\equiv4c_t\pmod {p^{2s}}
\]

selects one residue class modulo `p^(2s)`, because `dA` is a unit. That class
meets the interval `(-R,R)` in at most

\[
1+\frac{2R}{p^{2s}}
\]

integers. Therefore

\[
\begin{aligned}
\sum_m W(m)
&<2R
+
\sum_{s=1}^{E}(p^s-p^{s-1})
+
2R\sum_{s=1}^{E}
\frac{p^s-p^{s-1}}{p^{2s}}\\
&\le
2R+\sqrt M+\frac{2R}{p}.
\end{aligned}
\]

Multiplying by the root-count factor `2` gives

\[
\sum_m\#\{u\text{ roots for }m\}
<
4R+2\sqrt M+\frac{4R}{p}
<
6R+2\sqrt M
\]

for odd `p`. Every actual collision supplies one of the counted pairs `(m,u)`,
so the same bound holds for collisions. ∎

## 2. Complete same-stratum bound

### Corollary CMR51 — PROVED

For every positive difference `a` and every divisor `d` of its reduced part
`A`, the total number of same-stratum divisor collisions is less than

\[
\frac{12N}d+2\sqrt N.
\]

### Proof

CMR48 bounds all lower same-stratum cells `r<t` by less than `6N/d` in total.
CMR50 bounds the critical cell by

\[
6M/d+2\sqrt M
\le
6N/d+2\sqrt N.
\]

Add the two estimates. ∎

## 3. Remaining deterministic mass

The deterministic divisor-collision problem is now reduced to cross-stratum
pairs. Those pairs already satisfy the single residue condition

\[
dmA\equiv c_t\pmod p
\]

from CMR49. Proving an `O(polylog(N)N/d)` bound for that cross-stratum class
would complete the CMR46 hypothesis up to the explicit square-root boundary
term in CMR51.

The checker is
[`scripts/verify_prime_power_singular_collision_sum.py`](../scripts/verify_prime_power_singular_collision_sum.py).
