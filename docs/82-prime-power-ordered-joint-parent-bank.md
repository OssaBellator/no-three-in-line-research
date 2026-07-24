# Ordered joint parent banks and split-rank collateral

The exact prime-five and prime-seven escapes require a larger move than the
terminal four-board: rematch one complete inherited layer block and then rematch
the other against the new first layer. This chapter constructs that ordered
joint bank at every block size and gives its exact split-rank collateral bound.

## 1. The 72-spread bound extends to every size at least four

CMR110 proves the degree-two forbidden-board estimate for `t>=7`, while CMR128
proves existence for `t>=4`. The same quantitative constant in fact holds over
the entire range.

### Theorem CMR153 — PROVED

Let `F` be a forbidden subset of a `t` by `t` matching board with row and column
degree at most two. For every `t>=4`,

\[
|\Omega(F)|\ge\frac{t!}{72}.
\]

If `Q` is a compatible partial matching of `r` nonforbidden cells and `pi` is
uniform on `Omega(F)`, then

\[
\Pr(Q\subseteq\pi)
\le
\frac{72}{(t)_r}.
\]

### Proof

For `t>=7` this is CMR110. It remains to check `t=4,5,6`.

A bipartite forbidden graph of maximum degree two is the union of two partial
matchings. Extend both partial matchings to perfect matchings. Adding forbidden
cells can only decrease the allowed set, so it suffices to consider the union
of two complete matchings. Normalize the first to the identity and enumerate
the relative second permutation.

The exact minimum allowed-state counts are

\[
2,\qquad12,\qquad80
\]

at `t=4,5,6`, respectively. These exceed

\[
\frac{4!}{72},
\qquad
\frac{5!}{72},
\qquad
\frac{6!}{72}.
\]

For the cylinder estimate, at most `(t-r)!` permutations contain `Q`; divide by
`t!/72`. ∎

The size-three obstruction from CMR128 shows that `t=4` remains the sharp
universal threshold.

## 2. Ordered rematching of two inherited layer blocks

Fix one column block `C` of size `t>=4` in a saturated state. Let `A_0` and
`A_1` be the points of the two permutation layers in those columns. Each has
`t` points and carries one set of `t` rows.

Construct an ordered state as follows.

1. Uniformly rematch `A_0` to its existing rows while avoiding its old cells and
   the current cells of layer one.
2. Conditional on the first matching, uniformly rematch `A_1` to its existing
   rows while avoiding its old cells and the new cells of layer zero.

At both stages the forbidden board has row and column degree at most two.

### Theorem CMR154 — PROVED

The ordered joint bank is nonempty and contains at least

\[
\left(\frac{t!}{72}\right)^2
\]

ordered states.

Every state preserves both permutation layers, exact saturation, and layer
disjointness, and moves every point of `A_0 union A_1`.

Let `Q_0,Q_1` be compatible prescribed cells in the two layer boards, with

\[
|Q_0|=r_0,
\qquad
|Q_1|=r_1.
\]

Under the sequential uniform law,

\[
\boxed{
\Pr(Q_0\cup Q_1\text{ is selected})
\le
\frac{72^{\mathbf 1_{r_0>0}+\mathbf 1_{r_1>0}}}
{(t)_{r_0}(t)_{r_1}}.
}
\]

Here `(t)_0=1`. If a prescription conflicts with the random first matching,
its conditional probability is zero.

### Proof

CMR153 gives at least `t!/72` first-stage states. For every first-stage state,
the second forbidden board again has degree at most two, so it has at least
`t!/72` states. This proves the state count and all structural assertions.

Expose the first matching. Its prescription probability is at most
`72/(t)_{r_0}` when `r_0>0`. Conditional on any exposed first matching, the
second prescription is either forbidden or has probability at most
`72/(t)_{r_1}`. Multiply the bounds. ∎

## 3. Exact target destruction

Put

\[
A=A_0\cup A_1,
\qquad
X=S\setminus A.
\]

### Theorem CMR155 — PROVED

Every old real triple touching `A` is absent from every ordered joint state.
Thus the exact destroyed population is

\[
D(A)=\Phi(S)-\Phi(X).
\]

In particular, the bank destroys every inherited four-core target whose chosen
moved endpoint lies in `A`.

### Proof

Every old cell of both layer blocks is forbidden at its corresponding stage.
Hence no old point of `A` survives. A triple touching `A` therefore loses at
least one cell. Triples wholly in `X` are unchanged. ∎

## 4. Split-rank collateral identity

For nonnegative integers `r_0,r_1` with

\[
1\le r_0+r_1\le3,
\]

let `T_{r_0,r_1}` count real-collinear candidate certificates consisting of

- exactly `r_0` mutually compatible cells from the layer-zero board;
- exactly `r_1` mutually compatible cells from the layer-one board;
- exactly `3-r_0-r_1` fixed points of `X`;

with the two board prescriptions also cell-disjoint. Candidate certificates
which become forbidden after the first exposure are harmless overcounts.

### Theorem CMR156 — PROVED

For a sequentially random ordered joint state `S_{pi_0,pi_1}`,

\[
\boxed{
\begin{aligned}
\mathbb E\bigl[\Phi(S_{\pi_0,\pi_1})-\Phi(X)\bigr]
\le{}&
\frac{72}{t}\bigl(T_{1,0}+T_{0,1}\bigr)\\
&+\frac{72}{(t)_2}\bigl(T_{2,0}+T_{0,2}\bigr)
+\frac{72^2}{t^2}T_{1,1}\\
&+\frac{72}{(t)_3}\bigl(T_{3,0}+T_{0,3}\bigr)\\
&+\frac{72^2}{(t)_2t}
\bigl(T_{2,1}+T_{1,2}\bigr).
\end{aligned}
}
\]

Consequently, if the right side is strictly below `D(A)`, some ordered joint
parent state lowers the triple potential.

More generally, relative to a fixed global baseline `S_0`, if the parent excess
is `e` and no joint state improves `S_0`, then the displayed weighted sum is at
least

\[
D(A)-e.
\]

### Proof

Every new triple has one of the nine displayed split ranks. Apply CMR154 to its
prescribed cells and sum by linearity of expectation. CMR155 gives

\[
\Phi(S_{\pi_0,\pi_1})-\Phi(S)
=
-D(A)+\bigl(\Phi(S_{\pi_0,\pi_1})-\Phi(X)\bigr).
\]

A negative expectation yields an improving state. For the global-baseline
version, use the identity from CMR123:

\[
\Phi(S_{\pi_0,\pi_1})-\Phi(X)
=
\bigl(\Phi(S_{\pi_0,\pi_1})-\Phi(S_0)\bigr)-e+D(A).
\]

The first term is nonnegative under global nonimprovement. ∎

## 5. Remaining joint-parent theorem

CMR156 supplies the exact bank and the exact collateral expression suggested by
the `p=5` and `p=7` escape censuses. The remaining work is no longer to invent
a larger move. It is to control the five split-rank sums using the inherited
prefix geometry.

A sufficient theorem would show that, for the smallest ancestor block of every
terminal four-core trap, the CMR156 right side is paid by

1. the ancestor's quotient modular syndrome;
2. its primitive carry-direction cells;
3. the coarse target load which created the terminal core; or
4. a reverse-scale account for fine triples recreated by the joint move.

This would convert the exact finite parent escapes into a general inherited
escape theorem.

No all-`n` theorem is claimed here. The small-size state counts and joint
cylinder arithmetic are checked in
[`scripts/verify_prime_power_ordered_joint_parent.py`](../scripts/verify_prime_power_ordered_joint_parent.py).
