# Scale-summed collateral for old-cell-clean joint parent banks

CMR156 introduces nine split-rank certificate classes. The single-layer classes
are contained in the prefix quantities already controlled by CMR89--CMR92. This
chapter proves geometry-free quadratic bounds for the two genuinely new
cross-layer classes and then sums the complete ordered joint-parent collateral.

Retain one nontrivial prefix scale

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
blocks, let

\[
X_a=S\setminus(A_{a,0}\cup A_{a,1}),
\qquad
|X_a|=2N-2t,
\]

and use the split counts from CMR156. Each candidate-board rectangle has `t`
columns and `t` rows, and its old-cell-clean candidate set has size at most
`t(t-1)`.

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

Fix one joint block. Choose the fixed outside point `P` in `X_a`, then choose
the candidate cell `z_0` in the first layer board. The line through `P,z_0`
meets the second layer's `t`-column rectangle in at most `t` grid cells. Hence

\[
T_{1,1}(a)
\le
(2N-2t)\,t(t-1)\,t.
\]

Divide by `t^2` and sum the `m` blocks. Since `mt=N`,

\[
m(2N-2t)(t-1)<2mNt=2N^2.
\]

Conditional forbidden cells and cross-layer collisions only reduce the true
count. ∎

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

For `T_{2,1}`, choose an ordered first candidate cell in the layer-zero board.
There are at most `t(t-1)` choices. A compatible second layer-zero cell uses a
different column and row, giving at most `(t-1)^2` choices. Their line meets
the layer-one rectangle in at most `t` cells.

Every certificate is counted twice by the ordering of its two layer-zero cells,
so

\[
T_{2,1}(a)
\le
\frac{t^2(t-1)^3}{2}.
\]

After division by

\[
(t)_2t=t^2(t-1),
\]

this contributes at most `(t-1)^2/2`. The same estimate holds for `T_{1,2}`.
Summing the two classes and the `m` blocks gives `m(t-1)^2`. Finally,

\[
m(t-1)^2<mt^2=Nt=\frac{N^2}{m}\le\frac{N^2}{p}.
\]

∎

## 3. Choosing the better order

For one joint block, collect all normalized same-layer terms into

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

If layer zero is moved first, their CMR156 weight is `72A_0+700A_1`; reversing
the order gives `700A_0+72A_1`.

### Theorem CMR159 — PROVED

For every joint block, one of the two orders satisfies

\[
\boxed{
\text{same-layer weighted collateral}
\le
386(A_0+A_1).
}
\]

The cross-layer weights are independent of the order and equal `72*700=50400`.
Therefore the optimized expected collateral at scale `s` is at most

\[
\boxed{
386\sum_{a,\ell}
\left(
\frac{T_1(A_{a,\ell})}{t}
+
\frac{T_2(A_{a,\ell})}{(t)_2}
+
\frac{T_3(A_{a,\ell})}{(t)_3}
\right)
+
50400\sum_a
\left(
\frac{T_{1,1}(a)}{t^2}
+
\frac{T_{2,1}(a)+T_{1,2}(a)}{(t)_2t}
\right).
}
\]

### Proof

For nonnegative `A_0,A_1`,

\[
\min(72A_0+700A_1,700A_0+72A_1)
=
72(A_0+A_1)+628\min(A_0,A_1)
\le
386(A_0+A_1).
\]

The candidate universes of the old-cell-clean layer boards are subsets of the
corresponding one-layer prefix candidate universes. Hence their same-layer
counts are bounded by the displayed CMR89--CMR91 quantities. CMR156 gives the
cross coefficient. ∎

## 4. Balanced recursive all-scale endpoint

### Theorem CMR160 — PROVED

For the corrected balanced recursive bank at a fixed prime
`p=1 mod 4`, the expected optimized old-cell-clean joint-parent collateral over
all nontrivial scales is less than

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

In particular, some saturated recursive state has total ordered joint-parent
collateral

\[
O_p(N^2\log^2N).
\]

The same conclusion holds for the prime-seven balanced bank after replacing the
one-scale rank-one expectation by its CMR122 first-separation bound.

### Proof

CMR89 gives

\[
\mathbb E\sum_{a,\ell}\frac{T_1(A_{a,\ell})}{t}
<
(12s+p-1)N^2.
\]

CMR90--CMR91 give

\[
\sum_{a,\ell}
\left(
\frac{T_2}{(t)_2}+
\frac{T_3}{(t)_3}
\right)
<
\left(2+\frac1{3p}\right)N^2.
\]

CMR157--CMR158 give cross total below

\[
\left(2+\frac1p\right)N^2.
\]

Insert these in CMR159 and sum `s=1,...,k-1`, using

\[
\sum_{s=1}^{k-1}12s=6k(k-1).
\]

The prime-seven proof uses the same deterministic higher-rank estimates and its
balanced one-cell and first-separation laws. ∎

## 5. Fine-to-coarse stability

### Theorem CMR161 — PROVED

An old-cell-clean joint repair inside a scale-`s` prefix block preserves both
layer quotient states modulo `p^r` for every `r<=s`. Consequently it preserves
all unprocessed coarser modular syndromes, quotient-incidence energies, and
coarser block row sets.

A fine-to-coarse sweep of ordered joint-parent repairs therefore retains the
initial balanced quotient charges used in CMR160.

### Proof

Each stage permutes only the existing rows of one layer-prefix block. Those rows
have one common residue modulo `p^s`, hence also modulo every `p^r` with `r<=s`.
The statement is CMR93 applied successively to the two layer rematchings. ∎

## 6. Remaining inherited-escape issue

The ordered joint parent bank now has

- exact target destruction;
- fixed-rank spread;
- quadratic cross-layer higher-rank collateral;
- `O_p(N^2 log^2 N)` total balanced collateral;
- fine-to-coarse quotient stability.

Thus the parent-bank mechanism itself introduces no new asymptotic obstruction.
The unresolved step is local-to-global selection: assign terminal four-core
traps to ancestor blocks so that the available target load dominates the
CMR159 collateral without repeatedly consuming the same quotient or
reverse-scale budget.

No all-`n` theorem is claimed here. The cross-rank counting inequalities and
scale sums are checked in
[`scripts/verify_prime_power_joint_parent_collateral.py`](../scripts/verify_prime_power_joint_parent_collateral.py).
