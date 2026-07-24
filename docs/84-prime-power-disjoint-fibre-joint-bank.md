# Disjoint-fibre joint parent banks

CMR154--CMR161 construct a general old-cell-clean ordered bank. The recursive
prime-power states have extra structure above the root: corresponding layer
blocks occupy disjoint row-prefix fibres. This turns the joint parent bank into
a product of two independent derangement banks and improves every constant.

## 1. Persistent disjoint row fibres

### Theorem CMR162 — PROVED

In each of the following balanced recursive constructions,

1. the completed-reciprocal bank at `p=1 mod 4`;
2. the non-reciprocal prime-seven bank;

the two layer row sets over every nonroot column-prefix block are disjoint.

This property is preserved by every one-layer prefix rematching, every
recursive-compatible node repair, and every joint repair which reuses the two
existing row sets.

### Proof

At the root, the two local maps are distinct at every input.

For the reciprocal law they use a common coefficient and distinct shifts, so
their output digits differ by one fixed nonzero residue. For the prime-seven
law, distinct maps from the grid factorization use different cells in every
column.

Hence, after the first root digit, the two layer points above one column prefix
have different row prefixes. All descendants lie in those two disjoint row
fibres. Independent child maps cannot change the earlier row digit.

A prefix or joint rematching permutes only the existing rows inside each layer
block. CMR93 therefore preserves both row sets and their disjointness. A
recursive-compatible node repair rigidly translates child fibres inside their
already distinct parent row prefixes and also preserves disjointness. ∎

## 2. One-layer derangement spread

Let `D_t` be the permutations of a `t` by `t` board avoiding one fixed perfect
matching.

### Theorem CMR163 — PROVED

For every `t>=2`,

\[
\boxed{
|D_t|
\ge
\frac{t!}{4}.
}
\]

If `Q` is a compatible rank-`r` prescription and `pi` is uniform on `D_t`,

\[
\boxed{
\Pr(Q\subseteq\pi)
\le
\frac4{(t)_r}.
}
\]

### Proof

The allowed bipartite graph is `(t-1)`-regular. Divide its adjacency matrix by
`t-1`; the result is doubly stochastic. The van der Waerden permanent theorem
gives

\[
|D_t|
\ge
(t-1)^t\frac{t!}{t^t}
=
\left(1-\frac1t\right)^t t!.
\]

The factor `(1-1/t)^t` is increasing for `t>=2` and equals `1/4` at `t=2`.
At most `(t-r)!` permutations contain `Q`; divide by `t!/4`. ∎

## 3. Independent old-cell-clean joint bank

Fix a nonroot column-prefix block of size `t`. Let its two inherited layer row
sets be `R_0,R_1`. By CMR162 they are disjoint.

Independently rematch each layer to its existing rows while forbidding its old
matching.

### Theorem CMR164 — PROVED

The disjoint-fibre joint bank contains at least

\[
\boxed{
\frac{(t!)^2}{16}
}
\]

states. Every state

- preserves both permutation layers and saturation;
- is automatically cross-layer disjoint because `R_0 cap R_1` is empty;
- avoids every old cell of both layer blocks.

For compatible prescriptions of ranks `r_0,r_1`,

\[
\boxed{
\Pr(Q_0\cup Q_1\text{ is selected})
\le
\frac{4^{\mathbf1_{r_0>0}+\mathbf1_{r_1>0}}}
{(t)_{r_0}(t)_{r_1}}.
}
\]

### Proof

Apply CMR163 independently in the two layer boards. A cell from one old layer
has a row outside the other layer's row set, so it cannot be reoccupied by the
other layer. Thus moving both own diagonals removes every old geometric cell.
∎

Put `A=A_0 union A_1` and `X=S\setminus A`. Every old triple touching `A` is
destroyed, so the exact target load is

\[
D(A)=\Phi(S)-\Phi(X).
\]

## 4. Split-rank collateral with constants four and sixteen

### Theorem CMR165 — PROVED

With the split counts of CMR156, a random disjoint-fibre joint state satisfies

\[
\boxed{
\begin{aligned}
\mathbb E[\Phi(S_{\pi_0,\pi_1})-\Phi(X)]
\le{}&
\frac4t(T_{1,0}+T_{0,1})\\
&+
\frac4{(t)_2}(T_{2,0}+T_{0,2})
+
\frac{16}{t^2}T_{1,1}\\
&+
\frac4{(t)_3}(T_{3,0}+T_{0,3})\\
&+
\frac{16}{(t)_2t}(T_{2,1}+T_{1,2}).
\end{aligned}
}
\]

The current-potential and fixed-global-baseline improvement criteria from
CMR156 hold with this right side.

### Proof

Apply the independent cylinder law from CMR164 to each candidate certificate
and sum by split rank. Exact old-cell exclusion gives the same potential
identity as CMR156. ∎

## 5. Scale sums for balanced reciprocal banks

### Theorem CMR166 — PROVED

For every fixed prime `p=1 mod 4`, including `p=5`, the expected total
disjoint-fibre joint-parent collateral over all nontrivial scales is less than

\[
\boxed{
\begin{aligned}
&4\left[
6k(k-1)
+
\left(p+1+\frac1{3p}\right)(k-1)
\right]N^2\\
&\qquad+
16\left(2+\frac1p\right)(k-1)N^2.
\end{aligned}
}
\]

Hence some saturated recursive state has total nonroot joint-parent collateral

\[
O_p(N^2\log^2N).
\]

### Proof

At scale `s`, CMR89 bounds the expected rank-one sum by

\[
(12s+p-1)N^2.
\]

CMR90--CMR91 bound the same-layer higher ranks by

\[
\left(2+\frac1{3p}\right)N^2,
\]

and CMR157--CMR158 bound the cross ranks by

\[
\left(2+\frac1p\right)N^2.
\]

Multiply the same-layer classes by `4`, the cross classes by `16`, and sum
`12s` over `s=1,...,k-1`. CMR162 supplies the disjoint-fibre hypothesis at every
such scale. ∎

## 6. Prime-seven quotient and joint-parent sum

The CMR122 modular estimate supplies the missing prime-seven quotient input.
At quotient modulus `m=7^s`, the expected number of modular-zero triples with
three distinct columns is below

\[
\left(
\frac{36}{7}(s-1)+\frac{29}{9}
\right)m^2.
\]

Adding the fewer than `2m^2` vertical-pair triples and applying CMR86 gives the
rank-one prefix estimate

\[
\mathbb E
\sum_{a,\ell}
\frac{T_1(A_{s,a,\ell})}{t}
<
\left(
\frac{108}{7}(s-1)+\frac{53}{3}
\right)N^2.
\]

### Theorem CMR167 — PROVED

For the balanced prime-seven recursive bank, the expected total disjoint-fibre
joint-parent collateral over all nontrivial scales is less than

\[
\boxed{
\frac{(216k+360)(k-1)}7N^2.
}
\]

In particular it is `O(N^2 log^2 N)`.

### Proof

The displayed rank-one estimate follows from CMR85--CMR87 exactly as in CMR88.
At one scale, add the deterministic higher-rank bounds

\[
2+\frac1{21}
\]

and the cross bounds

\[
2+\frac17,
\]

then use CMR165. The resulting coefficient is

\[
4\left(
\frac{108}{7}(s-1)+\frac{53}{3}+2+\frac1{21}
\right)
+
16\left(2+\frac17\right)
=
\frac{432s+360}{7}.
\]

Summing `s=1,...,k-1` gives the theorem. ∎

## 7. Stability and the root boundary

### Theorem CMR168 — PROVED

Disjoint-fibre joint repairs preserve every unprocessed coarser quotient state
and charge, by CMR93 applied independently to the two layer rematchings.

Thus CMR166--CMR167 remain valid during a fine-to-coarse sweep.

The only block without disjoint row fibres is the root block. It is handled by

- the exact `p=5` and `p=7` parent escapes CMR147 and CMR151 at exponent one;
- the general old-cell-clean ordered bank CMR155 whenever the root size
  `N>=13`.

### Proof

The stability statement is identical to CMR161. The root alternatives are the
cited theorems. ∎

## 8. Revised remaining theorem

Every inherited ancestor block now has an executable old-cell-clean joint bank:

- nonroot blocks use the independent disjoint-fibre bank;
- large root blocks use the degree-three ordered bank;
- the two exceptional balanced roots `p=5,7` have exact escape certificates.

Their total balanced collateral is quadratic-polylogarithmic and stable under a
fine-to-coarse sweep. The remaining issue is a packing theorem: choose ancestor
blocks for terminal four-core traps so that their destroyed target populations
dominate the available joint-parent collateral without overlapping the same
trap or reverse-scale charge too many times.

No all-`n` theorem is claimed here. The derangement constants, prime-seven
coefficient, and all-scale sums are checked in
[`scripts/verify_prime_power_disjoint_fibre_joint.py`](../scripts/verify_prime_power_disjoint_fibre_joint.py).
