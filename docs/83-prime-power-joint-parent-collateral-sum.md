# Scale-summed collateral for old-cell-clean joint parent banks

CMR156 introduces nine split-rank certificate classes. The single-layer classes
are contained in the prefix quantities already controlled by CMR89--CMR92. This
chapter proves geometry-free quadratic bounds for the two genuinely new
cross-layer classes and then sums the complete ordered joint-parent collateral
on every scale where the degree-three bank exists.

Retain

\[
N=p^k,
\qquad
m=p^s,
\qquad
1\le s<k,
\qquad
 t=N/m.
\]

For each column-prefix block `C_a`, let `A_{a,0},A_{a,1}` be the two layer
blocks and put

\[
X_a=S\setminus(A_{a,0}\cup A_{a,1}),
\qquad
|X_a|=2N-2t.
\]

Each old-cell-clean candidate board has at most `t(t-1)` cells.

## 1. Cross rank two

### Theorem CMR157 — PROVED

At every nontrivial prefix scale,

\[
\boxed{
\sum_{a\bmod m}
\frac{T_{1,1}(a)}{t^2}
\le
m(2N-2t)(t-1)
<
2N^2.
}
\]

### Proof

Fix one block. Choose the fixed outside point `P` in `X_a`, then choose the
candidate cell `z_0` in the first layer board. The line through `P,z_0` meets
the second layer's `t`-column rectangle in at most `t` grid cells. Hence

\[
T_{1,1}(a)
\le
(2N-2t)t(t-1)t.
\]

Divide by `t^2`, sum the `m` blocks, and use `mt=N`. Conditional forbidden cells
and cross-layer collisions only reduce the true count. ∎

## 2. Cross rank three

### Theorem CMR158 — PROVED

At every nontrivial prefix scale,

\[
\boxed{
\sum_{a\bmod m}
\frac{T_{2,1}(a)+T_{1,2}(a)}{(t)_2t}
\le
m(t-1)^2
<
\frac{N^2}{p}.
}
\]

### Proof

For `T_{2,1}`, choose an ordered first candidate cell in the layer-zero board,
then a compatible second cell. There are at most

\[
t(t-1)(t-1)^2
\]

ordered choices. Their line meets the layer-one rectangle in at most `t` cells.
Every certificate is counted twice by the ordering of its two layer-zero cells,
so

\[
T_{2,1}(a)
\le
\frac{t^2(t-1)^3}{2}.
\]

After division by `(t)_2t=t^2(t-1)`, this contributes at most
`(t-1)^2/2`. The same holds for `T_{1,2}`. Sum the `m` blocks and use

\[
m(t-1)^2<mt^2=\frac{N^2}{m}\le\frac{N^2}{p}.
\]

∎

## 3. Choosing the better layer order

For one block define

\[
A_0
=
\frac{T_{1,0}}t+
\frac{T_{2,0}}{(t)_2}+
\frac{T_{3,0}}{(t)_3},
\]

\[
A_1
=
\frac{T_{0,1}}t+
\frac{T_{0,2}}{(t)_2}+
\frac{T_{0,3}}{(t)_3}.
\]

Moving layer zero first gives weight `72A_0+700A_1`; reversing the order gives
`700A_0+72A_1`.

### Theorem CMR159 — PROVED

For every joint block, one order satisfies

\[
\boxed{
\text{same-layer weighted collateral}
\le386(A_0+A_1).
}
\]

The cross-layer weight is `72*700=50400`, independent of the order. Therefore
the optimized scale-`s` collateral is at most

\[
\boxed{
\begin{aligned}
&386\sum_{a,\ell}
\left(
\frac{T_1(A_{a,\ell})}{t}
+
\frac{T_2(A_{a,\ell})}{(t)_2}
+
\frac{T_3(A_{a,\ell})}{(t)_3}
\right)\\
&\quad+
50400\sum_a
\left(
\frac{T_{1,1}(a)}{t^2}
+
\frac{T_{2,1}(a)+T_{1,2}(a)}{(t)_2t}
\right).
\end{aligned}
}
\]

### Proof

For nonnegative `A_0,A_1`,

\[
\min(72A_0+700A_1,700A_0+72A_1)
=
72(A_0+A_1)+628\min(A_0,A_1)
\le386(A_0+A_1).
\]

The old-cell-clean same-layer candidate universes are subsets of the
corresponding one-layer prefix universes. Apply CMR156 to the cross terms. ∎

## 4. Balanced recursive scale sum

### Theorem CMR160 — PROVED

Let `p>=13` be a fixed prime with `p=1 mod 4`. For the corrected balanced
recursive bank, the expected optimized old-cell-clean joint-parent collateral
over all nontrivial scales is less than

\[
\boxed{
\begin{aligned}
&386\left[
6k(k-1)
+
\left(p+1+\frac1{3p}\right)(k-1)
\right]N^2\\
&\qquad+
50400\left(2+\frac1p\right)(k-1)N^2.
\end{aligned}
}
\]

Hence some saturated recursive state has total joint-parent collateral

\[
O_p(N^2\log^2N).
\]

For `p=5`, the same one-scale estimate and the corresponding sum hold for every
scale with `t>=25`, equivalently `s<=k-2`. The bottom `t=5` layer is not covered
by CMR154 and remains a finite-base outside-collateral problem. No prime-seven
all-scale claim is made here; CMR151 handles only the exact root state space.

### Proof

At one scale, CMR89 gives

\[
\mathbb E\sum_{a,\ell}\frac{T_1(A_{a,\ell})}{t}
<
(12s+p-1)N^2.
\]

CMR90--CMR91 give same-layer higher-rank total below

\[
\left(2+\frac1{3p}\right)N^2,
\]

while CMR157--CMR158 give cross total below

\[
\left(2+\frac1p\right)N^2.
\]

Insert these estimates in CMR159 and sum. For `p>=13`, every nontrivial block
has `t>=p>=13`, so CMR154 applies at all scales. For `p=5`, restrict the sum to
`t>=25`. ∎

## 5. Fine-to-coarse stability

### Theorem CMR161 — PROVED

Wherever the old-cell-clean joint bank is defined, a scale-`s` repair preserves
both layer quotient states modulo `p^r` for every `r<=s`. It therefore preserves
all unprocessed coarser modular syndromes, quotient-incidence energies, and
coarser block row sets.

A fine-to-coarse sweep retains the initial balanced quotient charges used in
CMR160.

### Proof

Each stage permutes only the existing rows of one layer-prefix block. Those rows
have one common residue modulo `p^s`, and hence modulo every `p^r` with `r<=s`.
Apply CMR93 successively to the two layer rematchings. ∎

## 6. Remaining inherited-escape issue

The ordered joint parent bank now has

- exact old-cell target destruction;
- fixed-rank spread for `t>=13`;
- quadratic cross-layer higher-rank collateral;
- `O_p(N^2 log^2 N)` total balanced collateral for reciprocal primes `p>=13`;
- fine-to-coarse quotient stability.

Thus the parent mechanism introduces no new asymptotic obstruction on those
scales. The unresolved step is local-to-global selection: assign terminal
four-core traps to ancestor blocks so that their target load dominates the
CMR159 collateral without repeatedly consuming the same quotient or
reverse-scale budget. The exceptional bottom blocks at `p=5` and `p=7` require
separate finite-base collateral control.

No all-`n` theorem is claimed here. The cross-rank inequalities and scale sums
are checked in
[`scripts/verify_prime_power_joint_parent_collateral.py`](../scripts/verify_prime_power_joint_parent_collateral.py).
