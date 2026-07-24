# Sharp fixed-rank cylinders for nonroot derangement banks

CMR163 uses the uniform constant `4/(t)_r`. Every nonroot recursive block has
size at least the base prime, hence at least five. In that range the exact
derangement density gives substantially better fixed-rank constants.

## 1. Derangement density and one-cell law

Let `D_t` denote the number of derangements of `t` objects.

### Theorem CMR176 — PROVED

For every `t>=5`,

\[
\boxed{
D_t\ge\frac{11}{30}t!.
}
\]

Under the uniform derangement law, every nonfixed prescribed cell has exact
probability

\[
\boxed{
\frac1{t-1}.
}
\]

For every compatible nonfixed rank-`r` prescription, `r=2,3`,

\[
\boxed{
\Pr(Q\subseteq\pi)
\le
\frac{30}{11(t)_r}.
}
\]

### Proof

Inclusion-exclusion gives

\[
\frac{D_t}{t!}
=
\sum_{j=0}^t\frac{(-1)^j}{j!}.
\]

The odd partial sums increase to `e^{-1}` and the even partial sums decrease to
it. At `t=5`, the odd sum is

\[
1-1+\frac12-\frac16+\frac1{24}-\frac1{120}
=
\frac{11}{30}.
\]

Thus every later partial sum is at least `11/30`.

For rank one, symmetry among the `t-1` permitted columns in one row gives exact
probability `1/(t-1)`.

At most `(t-r)!` permutations contain a compatible rank-`r` prescription.
Divide by `(11/30)t!`. ∎

In the normalized form used by prefix collateral,

\[
\frac1{t-1}
=
\frac{t}{t-1}\frac1t
\le
\frac54\frac1t.
\]

## 2. Sharpened independent joint-parent law

### Theorem CMR177 — PROVED

For a nonroot disjoint-fibre joint block of size `t>=5`, a random independent
pair of derangements satisfies

\[
\boxed{
\begin{aligned}
\mathbb E[\Phi(S_{\pi_0,\pi_1})-\Phi(X)]
\le{}&
\frac5{4t}(T_{1,0}+T_{0,1})\\
&+
\frac{30}{11(t)_2}(T_{2,0}+T_{0,2})
+
\frac{25}{16t^2}T_{1,1}\\
&+
\frac{30}{11(t)_3}(T_{3,0}+T_{0,3})\\
&+
\frac{75}{22(t)_2t}(T_{2,1}+T_{1,2}).
\end{aligned}
}
\]

### Proof

Use the rank-one bound `5/(4t)` and the rank-two/rank-three bound
`30/(11(t)_r)` from CMR176 independently in the two layers. A `(1,1)`
certificate receives the product `(5/4)^2=25/16`. A `(2,1)` or `(1,2)`
certificate receives `(30/11)(5/4)=75/22`. Sum by split rank. ∎

## 3. Reciprocal all-scale endpoint

### Theorem CMR178 — PROVED

For every fixed balanced reciprocal prime `p=1 mod 4`, the expected total
nonroot joint-parent collateral is less than

\[
\boxed{
\begin{aligned}
(k-1)N^2\Bigg[{}
&\frac54(6k+p-1)
+
\frac{30}{11}\left(2+\frac1{3p}\right)\\
&+
\frac{25}{8}
+
\frac{75}{22p}
\Bigg].
\end{aligned}
}
\]

This improves CMR166 while preserving the order `O_p(N^2 log^2 N)`.

### Proof

At each scale use

- CMR89 for rank one;
- CMR90--CMR91 for same-layer ranks two and three;
- CMR157 for cross rank `(1,1)`;
- CMR158 for cross ranks `(2,1),(1,2)`.

Apply the coefficients from CMR177 and sum

\[
\sum_{s=1}^{k-1}12s=6k(k-1).
\]

∎

## 4. Prime-seven endpoint

### Theorem CMR179 — PROVED

For the balanced prime-seven recursive bank, the expected total nonroot
joint-parent collateral is less than

\[
\boxed{
\frac{(1620k+2015)(k-1)}{168}N^2.
}
\]

At one scale the coefficient is

\[
\frac{135}{7}s+rac{2015}{168}.
\]

### Proof

Use the prime-seven rank-one estimate from CMR167,

\[
\frac{108}{7}(s-1)+\frac{53}{3},
\]

together with the same higher-rank and cross-rank bounds used there. CMR177
gives

\[
\begin{aligned}
&\frac54\left(\frac{108}{7}(s-1)+\frac{53}{3}\right)
+
\frac{30}{11}\left(2+\frac1{21}\right)\\
&\qquad+
\frac{25}{16}\cdot2
+
\frac{75}{22}\cdot\frac17
=
\frac{135}{7}s+rac{2015}{168}.
\end{aligned}
\]

Sum over `s=1,...,k-1`. ∎

## 5. Sharpened frozen-state ledger

Combining CMR170 with CMR178--CMR179 gives the following explicit endpoints.

### Corollary CMR180 — PROVED

A low-collateral balanced reciprocal state frozen under every nonroot joint
parent bank satisfies

\[
\Phi(S)
<
N^2\left[
\frac54(6k+p-1)
+
\frac{30}{11}\left(2+\frac1{3p}\right)
+
\frac{25}{8}
+
\frac{75}{22p}
\right].
\]

For the prime-seven bank,

\[
\Phi(S)
<
\frac{1620k+2015}{168}N^2.
\]

The remaining gap is qualitative rather than an unbounded cylinder loss: one
must extract a strict target-versus-collateral advantage from first-separation
or carry structure inside one closure envelope epoch.

No all-`n` theorem is claimed here. The derangement density, exact one-cell law,
and scale coefficients are checked in
[`scripts/verify_prime_power_sharp_derangement.py`](../scripts/verify_prime_power_sharp_derangement.py).
