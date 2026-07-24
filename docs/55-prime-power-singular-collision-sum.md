# Summing the singular same-stratum collision class

CMR58 isolates one potentially singular carry class in the critical stratum
`r=t`. Its total Hensel multiplicity can be summed directly.

Retain

\[
M=p^{k-t},
\qquad a=p^tA,
\qquad d\mid A,
\]

and work in the same-stratum cell \(v_p(x)=v_p(x+a)=t\). For a divisor
collision, CMR58 gives

\[
dm\,u(u+A)+Ac_t\equiv0\pmod M,
\]

where \(0<|m|<M/d\) and \(p\nmid m\). After division by `dm`, the
discriminant is

\[
\Delta_m=A^2-4Ac_t(dm)^{-1},
\]

and, since all displayed factors are units,

\[
v_p(\Delta_m)=v_p(dmA-4c_t).
\]

## Layer-cake bound

### Theorem CMR61 — PROVED

The total number of possible critical same-stratum parameters `u` over all
signed carries `m` is less than

\[
\frac{6M}d+2\sqrt M.
\]

The actual number of divisor collisions satisfies the same bound.

### Proof

Put \(e=k-t\), \(E=\lfloor e/2\rfloor\), and \(R=M/d\). For one fixed `m`,
the odd-prime square-root classification bounds the roots by

\[
2p^{\min(\lfloor v_p(dmA-4c_t)/2\rfloor,E)}.
\]

For

\[
W(m)=p^{\min(\lfloor v_p(dmA-4c_t)/2\rfloor,E)},
\]

use the exact layer decomposition

\[
W(m)=1+
\sum_{s=1}^{E}(p^s-p^{s-1})
\mathbf1_{p^{2s}\mid dmA-4c_t}.
\]

There are fewer than `2R` possible signed carries. For fixed `s`, the linear
congruence

\[
dmA\equiv4c_t\pmod {p^{2s}}
\]

selects one residue class, which meets `(-R,R)` in at most
\(1+2R/p^{2s}\) integers. Therefore

\[
\sum_mW(m)
<2R+\sqrt M+rac{2R}{p}.
\]

Multiplying by the root-count factor `2` gives the result for odd `p`. ∎

### Corollary CMR62 — PROVED

For every positive difference `a` and every divisor `d` of its reduced part,
the total number of same-stratum divisor collisions is less than

\[
\frac{12N}d+2\sqrt N.
\]

### Proof

CMR59 bounds all lower same-stratum cells by less than `6N/d`. CMR61 bounds the
critical cell by \(6M/d+2\sqrt M\), which is at most
\(6N/d+2\sqrt N\). ∎

The remaining deterministic mass is cross-stratum and is summed in CMR63–66.

The checker is
[`scripts/verify_prime_power_singular_collision_sum.py`](../scripts/verify_prime_power_singular_collision_sum.py).
