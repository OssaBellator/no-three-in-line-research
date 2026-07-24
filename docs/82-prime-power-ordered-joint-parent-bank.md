# Old-cell-clean ordered joint parent banks

The exact prime-five and prime-seven escapes require a larger move than the
terminal four-board: rematch one complete inherited layer block and then rematch
the other against the new first layer.

There is one essential geometric subtlety. It is not enough to move both
**labeled** layers. An old first-layer grid cell could be reoccupied by the new
second layer, so an old target triple might survive geometrically. Exact target
destruction requires the final union to avoid every old cell of both parent
blocks. The second stage therefore has three forbidden matchings.

This chapter constructs the resulting old-cell-clean bank for block size at
least thirteen and gives its split-rank collateral law.

## 1. Degree-two spread down to size four

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

For `t>=7` this is CMR110. A degree-two bipartite forbidden graph is the union
of two partial matchings. Extend them to complete matchings and normalize the
first to the identity. Exact enumeration of the relative second matching gives
minimum allowed-state counts

\[
2,\qquad12,\qquad80
\]

at `t=4,5,6`. Each exceeds `t!/72`. At most `(t-r)!` permutations contain a
fixed compatible rank-`r` prescription, proving the cylinder bound. ∎

## 2. A degree-three spread bank

### Theorem CMR154 — PROVED

Let `F` have row and column degree at most three. For every `t>=13`,

\[
\boxed{
|\Omega(F)|\ge\frac{t!}{700}.
}
\]

For a compatible rank-`r` partial matching `Q` and uniform `pi` in `Omega(F)`,

\[
\boxed{
\Pr(Q\subseteq\pi)
\le
\frac{700}{(t)_r}.
}
\]

### Proof

For each forbidden cell `(i,j)`, let `E_{ij}` be the canonical event
`pi(i)=j` under a uniformly random permutation. Each event has probability
`1/t`. In the lopsided permutation dependency graph, it has at most four
neighbours: at most two further forbidden cells in its row and two in its
column.

Choose

\[
x=\frac2t.
\]

For `t>=13`,

\[
\frac1t
\le
\frac2t\left(1-\frac2t\right)^4,
\]

because `(1-2/13)^4>1/2` and the left factor increases with `t`. The lopsided
local lemma gives

\[
\Pr(\pi\in\Omega(F))
\ge
\left(1-\frac2t\right)^{|F|}
\ge
\left(1-\frac2t\right)^{3t}.
\]

The final expression is increasing for `t>=13`, and at `t=13` it is

\[
\left(\frac{11}{13}\right)^{39}
>
\frac1{700}.
\]

Thus the state count follows. Divide the trivial upper bound `(t-r)!` for
states containing `Q` by `t!/700`. ∎

## 3. The old-cell-clean ordered joint bank

Fix one column block `C` of size `t>=13` in a saturated state. Let `A_0,A_1`
be the two inherited layer blocks in those columns, and let `O` be the union of
their old grid cells.

Construct an ordered state as follows.

1. Rematch `A_0` to its existing rows while avoiding every cell of `O`.
2. Conditional on the first matching, rematch `A_1` to its existing rows while
   avoiding every cell of `O` and every new first-layer cell.

The first forbidden board has degree at most two. The second has degree at most
three: the old layer-zero cells, old layer-one cells, and new layer-zero cells
are three partial matchings in the second board.

### Theorem CMR155 — PROVED

The old-cell-clean ordered joint bank contains at least

\[
\boxed{
\frac{(t!)^2}{72\cdot700}
}
\]

ordered states. Every state preserves both permutation layers, saturation, and
layer disjointness, and its final point set avoids every old cell of `A_0 union
A_1`.

Let `Q_0,Q_1` prescribe `r_0,r_1` compatible cells in the first and second
boards. Under the sequential uniform law,

\[
\boxed{
\Pr(Q_0\cup Q_1\text{ is selected})
\le
\frac{72^{\mathbf1_{r_0>0}}700^{\mathbf1_{r_1>0}}}
{(t)_{r_0}(t)_{r_1}}.
}
\]

### Proof

CMR153 gives at least `t!/72` first-stage states. For every first-stage state,
CMR154 gives at least `t!/700` second-stage states. Both structural claims
follow from the forbidden sets.

Expose the first matching and apply its `72/(t)_{r_0}` cylinder bound.
Conditional on it, the second prescription is either forbidden or has
probability at most `700/(t)_{r_1}`. Multiply. ∎

Put

\[
A=A_0\cup A_1,
\qquad
X=S\setminus A.
\]

Because the final union avoids all old cells of `A`, every old triple touching
`A` is destroyed. Hence the exact target population is

\[
D(A)=\Phi(S)-\Phi(X).
\]

## 4. Split-rank collateral law

For `1<=r_0+r_1<=3`, let `T_{r_0,r_1}` count real-collinear candidate
certificates with exactly `r_0` compatible first-board cells, `r_1` compatible
second-board cells, and `3-r_0-r_1` fixed points of `X`. Overcounting cells which
become conditionally forbidden is harmless.

### Theorem CMR156 — PROVED

For a sequentially random old-cell-clean state,

\[
\boxed{
\begin{aligned}
\mathbb E\bigl[\Phi(S_{\pi_0,\pi_1})-\Phi(X)\bigr]
\le{}&
\frac{72}{t}T_{1,0}
+
\frac{700}{t}T_{0,1}\\
&+
\frac{72}{(t)_2}T_{2,0}
+
\frac{700}{(t)_2}T_{0,2}
+
\frac{72\cdot700}{t^2}T_{1,1}\\
&+
\frac{72}{(t)_3}T_{3,0}
+
\frac{700}{(t)_3}T_{0,3}\\
&+
\frac{72\cdot700}{(t)_2t}
\bigl(T_{2,1}+T_{1,2}\bigr).
\end{aligned}
}
\]

If the right side is below `D(A)`, some ordered joint state lowers the current
triple potential.

Relative to a fixed global baseline `S_0`, if the parent excess is `e` and no
joint state improves `S_0`, the displayed weighted sum is at least

\[
D(A)-e.
\]

### Proof

Every new triple has one of the nine displayed split ranks. Apply CMR155 to its
prescribed cells and sum by linearity of expectation. Exact old-cell exclusion
gives

\[
\Phi(S_{\pi_0,\pi_1})-\Phi(S)
=
-D(A)+\bigl(\Phi(S_{\pi_0,\pi_1})-\Phi(X)\bigr).
\]

The global-baseline statement is the CMR123 identity with the joint block in
place of the endpoint block. ∎

## 5. Exceptional base blocks and remaining theorem

The general bank begins at `t=13`. This covers

- every base block for primes `p>=13`;
- every nonbase ancestor block at `p=5`, since its size is at least `25`;
- every nonbase ancestor block at `p=7`, since its size is at least `49`.

The exceptional base blocks are exactly the cases already handled by exhaustive
certificates:

- CMR147--CMR148 at `p=5`;
- CMR151--CMR152 for the balanced `p=7` root family.

The remaining general theorem is to control the CMR156 split-rank sums by the
ancestor's quotient, carry, and reverse-scale budgets. The new cross-layer
higher-rank terms admit universal quadratic bounds in the next chapter; only
rank-one secant shadows retain arithmetic content.

No all-`n` theorem is claimed here. The finite degree-two counts, the
`1/700` degree-three constant, and the split-rank arithmetic are checked in
[`scripts/verify_prime_power_ordered_joint_parent.py`](../scripts/verify_prime_power_ordered_joint_parent.py).
