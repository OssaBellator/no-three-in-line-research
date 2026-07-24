# Primitive-parameter spacing inside tangent cells

CMR11 used the shorter coordinate interval to improve the modular Hensel root
count. Parameterizing the exact primitive line removes the remaining small
coefficient and gives a sharper bound.

Use the odd-prime top-stratum notation

\[
M=p^m,
\qquad
Au+Bw=C_h,
\qquad
p\nmid AB,
\]

with primitive coefficients

\[
\gcd(A,B)=1.
\]

Put

\[
H=\max(|A|,|B|),
\qquad
\Delta=C_h^2-4ABc_h.
\]

## 1. Parameter spacing

Any two integer points on the exact line differ by

\[
(u'-u,w'-w)=(Bs,-As)
\]

for an integer parameter `s`.

### Theorem CMR30 — PROVED

1. Suppose

   \[
   v_p(\Delta)=2t<m
   \]

   and the residual unit is a quadratic residue modulo `p`. Then the exact
   top-stratum population is at most

   \[
   2\left(
   1+
   \left\lfloor
   \frac{M-1}{H p^{m-t}}
   \right\rfloor
   \right)
   \le
   2\left(1+\left\lfloor\frac{p^t}{H}\right\rfloor\right).
   \]
2. If

   \[
   \Delta\equiv0\pmod M,
   \]

   the top population is at most

   \[
   1+
   \left\lfloor
   \frac{M-1}{H p^{\lceil m/2\rceil}}
   \right\rfloor
   \le
   1+\left\lfloor\frac{p^{\lfloor m/2\rfloor}}{H}\right\rfloor.
   \]
3. The odd-valuation and nonsquare cases have no top points.

The full line intersection is bounded by the displayed top contribution plus
`2h`, where `h` is the top valuation from CMR3.

### Proof

In the two-root case, the possible `u` coordinates form two classes modulo

\[
q=p^{m-t}.
\]

The same is true of the `w` coordinates. If two exact points belong to the
same root branch, then both coordinate differences are divisible by `q`.
Since

\[
(u'-u,w'-w)=(Bs,-As)
\]

and `p` divides neither `A` nor `B`, it follows that

\[
q\mid s.
\]

The box restrictions \(0\le u,w<M\) imply

\[
|B|\,|s|\le M-1,
\qquad
|A|\,|s|\le M-1.
\]

Thus all feasible parameters lie in an interval of diameter at most

\[
(M-1)/H.
\]

One residue class modulo `q` meets that interval in at most

\[
1+\left\lfloor\frac{M-1}{Hq}\right\rfloor
\]

integers. There are two branches. The zero-discriminant case has one branch
with

\[
q=p^{\lceil m/2\rceil}.
\]

The final inequalities use \(M/q=p^t\), respectively
\(M/q=p^{\lfloor m/2\rfloor}\). ∎

## 2. Concentration consequence

A two-branch tangent cell with at least `s>2` points forces

\[
H
\le
\frac{p^t}{s/2-1}.
\]

A zero-discriminant cell with at least `s>1` points forces

\[
H
\le
\frac{p^{\lfloor m/2\rfloor}}{s-1}.
\]

Hence a large exact tangent cell is simultaneously:

- highly singular `p`-adically;
- supported on a primitive direction with small coefficients.

This is the desired divisor-sensitive exact-real improvement. It does not yet
prove a constant line cap, because small-coefficient singular lines remain.
The next counting theorem should sum those exceptional directions by height
rather than applying a global maximum occupancy.

The checks are in
[`scripts/verify_prime_power_tangent_parameter.py`](../scripts/verify_prime_power_tangent_parameter.py).
