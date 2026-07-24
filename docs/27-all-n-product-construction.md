# Mixed-radix product constructions

This chapter develops the product/composition branch in
[`tracks/all-n-product-construction.md`](../tracks/all-n-product-construction.md).
It solves the saturation part of the product problem, gives an exact
coarse/fine determinant classification for every bad triple, and records a
minimal obstruction to the simplest phase strategy.

The results here do **not** prove multiplicative closure for no-three-in-line
configurations. The remaining issue is the elimination of the explicit mixed
resonance equations below.

Throughout, grids are zero-indexed:

\[
[k]=\{0,1,\ldots,k-1\}.
\]

## 1. Factor configurations and alternating cycles

Let

\[
S_m=\{(i,\sigma_r(i)):i\in[m],\ r\in\{0,1\}\}
\]

and

\[
S_n=\{(u,\tau_s(u)):u\in[n],\ s\in\{0,1\}\}
\]

be saturated configurations, written as two permutation layers. Thus
`σ_0,σ_1` are permutations of `[m]`, `τ_0,τ_1` are permutations of `[n]`, and

\[
\sigma_0(i)\ne\sigma_1(i),
\qquad
\tau_0(u)\ne\tau_1(u)
\]

for every `i,u`.

Define

\[
\pi=\tau_1^{-1}\tau_0.
\]

The orbits of `π` are the left-vertex sets of the alternating cycles in the
bipartite union of the two fine permutation matchings. Write `C(u)` for the
orbit containing `u`.

For every coarse row `i` and every orbit `C`, choose a phase bit

\[
\varepsilon_{i,C}\in\{0,1\}.
\]

For `r in {0,1}`, define a flattened permutation candidate by

\[
\boxed{
\Pi_r(ni+u)
=
 n\sigma_r(i)
 +
 \tau_{r\oplus\varepsilon_{i,C(u)}}(u).
}
\]

The corresponding product set is

\[
P_{m,n}(\varepsilon)
=
\{(x,\Pi_r(x)):x\in[mn],\ r\in\{0,1\}\}.
\]

This includes the constant tensor choices, coarse-row phase choices, and
independent phase choices on every alternating fine cycle.

## 2. Saturation is closed under cycle phases

### Theorem PX1 — PROVED

For every phase array `ε`, each `Π_r` is a permutation of `[mn]`. The two
permutation graphs are cell-disjoint. Consequently,
`P_{m,n}(ε)` consists of exactly `2mn` cells and has exactly two points in every
row and every column.

The coordinates can be constructed in `O(mn)` arithmetic operations once the
factor permutations and phase bits are given.

### Proof

Fix `r` and a target coarse column `j`. Since `σ_r` is a permutation, there is
a unique coarse row

\[
i=\sigma_r^{-1}(j).
\]

It remains to show that

\[
\rho_i(u)=\tau_{r\oplus\varepsilon_{i,C(u)}}(u)
\]

is a permutation of `[n]`.

Let `C` be one orbit of `π`. Since `π(C)=C`,

\[
\tau_0(C)
=
\tau_1(\pi(C))
=
\tau_1(C).
\]

Thus the two restrictions `τ_0|_C` and `τ_1|_C` are bijections from `C` onto
the same right-vertex set. On each orbit, `ρ_i` chooses one of these two
bijections in its entirety. Distinct orbits have disjoint image sets because
`τ_1` is a permutation. Hence `ρ_i` is a permutation of `[n]`.

Therefore `Π_r` is a permutation of `[mn]`. For a fixed input `ni+u`, the two
outputs have coarse digits `σ_0(i)` and `σ_1(i)`, which are distinct. Hence the
two cells in that row are distinct. The two permutation graphs are therefore
edge-disjoint, proving the row and column counts. The displayed formula gives
the stated construction time. \(\square\)

### Remark

If `π` has `c` orbits, this family contains exactly

\[
2^{mc}
\]

phase states. Saturation alone therefore leaves a large but structured repair
space.

## 3. Exact determinant and carry normal form

Take three encoded points

\[
P_t=(ni_t+u_t,nj_t+v_t),
\qquad t=0,1,2,
\]

where `(i_t,j_t) in S_m` and `(u_t,v_t) in S_n`.

For three planar points, write `det(A_0,A_1,A_2)` for the affine determinant.
Define

\[
\Delta_c
=
\det((i_0,j_0),(i_1,j_1),(i_2,j_2)),
\]

\[
\Delta_f
=
\det((u_0,v_0),(u_1,v_1),(u_2,v_2)),
\]

and

\[
\begin{aligned}
M={}&(i_1-i_0)(v_2-v_0)+(u_1-u_0)(j_2-j_0)\\
&-(j_1-j_0)(u_2-u_0)-(v_1-v_0)(i_2-i_0).
\end{aligned}
\]

### Theorem PX2 — PROVED

The flattened determinant is exactly

\[
\boxed{
\det(P_0,P_1,P_2)
=
n^2\Delta_c+nM+\Delta_f.
}
\]

In particular, a real collinear triple must satisfy

\[
\Delta_f=n\kappa,
\qquad
|\kappa|\le n-2,
\]

and then its exact mixed carry equation is

\[
\boxed{
n\Delta_c+M+\kappa=0.
}
\]

### Proof

Expand the determinant after substituting

\[
X_t=ni_t+u_t,
\qquad
Y_t=nj_t+v_t.
\]

The terms using two coarse differences give `n^2 Δ_c`; the terms using one
coarse and one fine difference give `nM`; and the terms using two fine
differences give `Δ_f`.

If the flattened determinant vanishes, reduction modulo `n` gives
`Δ_f = 0 mod n`. Three points in the square `[n]^2` satisfy

\[
|\Delta_f|\le(n-1)^2<n^2.
\]

Therefore `Δ_f=nκ` with

\[
|\kappa|
\le
\left\lfloor\frac{(n-1)^2}{n}\right\rfloor
=n-2.
\]

Dividing the determinant identity by `n` gives the mixed carry equation.
\(\square\)

### Consequences

- A triple with `Δ_f` not divisible by `n` cannot be collinear after
  flattening.
- Lexicographic flattening does not automatically separate scales: the mixed
  term `M` can cancel both the coarse determinant and the fine carry.
- A triple lying entirely in one coarse block is collinear exactly when its
  three fine points are collinear.
- A triple whose three points share one fine point is collinear exactly when
  its three coarse points are collinear.

The last two cases are therefore excluded when the factor configurations are
no-three.

## 4. Four exact cross-block types

For a product triple, let `c` be the number of distinct coarse points
`(i_t,j_t)` and let `f` be the number of distinct fine points `(u_t,v_t)`.

### Theorem PX3 — PROVED

Assume both factor configurations are no-three. Every collinear triple in the
flattened product has

\[
(c,f)\in\{(2,2),(2,3),(3,2),(3,3)\}.
\]

Moreover the four types satisfy the following exact equations.

| Type | Determinants | Required resonance |
|---|---|---|
| `(2,2)` | `Δ_c=Δ_f=0` | `M=0` |
| `(2,3)` | `Δ_c=0`, `Δ_f=nκ != 0` | `M+κ=0` |
| `(3,2)` | `Δ_c != 0`, `Δ_f=0` | `nΔ_c+M=0` |
| `(3,3)` | `Δ_c != 0`, `Δ_f=nκ != 0` | `nΔ_c+M+κ=0` |

Here `|κ| <= n-2`. In particular, type `(2,3)` is impossible when `n=2`.

### Proof

If `c=1`, all three points lie in one coarse block, so Theorem PX2 reduces
collinearity to `Δ_f=0`. The three fine points are distinct cells of `S_n`,
contradicting the no-three property. Thus `c>=2`. The same argument with the
roles reversed gives `f>=2`.

If `c=2`, two coarse points coincide, so `Δ_c=0`. If `c=3`, the three coarse
points are distinct points of `S_m`, so the no-three property gives
`Δ_c != 0`. The analogous statements hold for `f` and `Δ_f`. Substitution in
Theorem PX2 gives the four equations. \(\square\)

This is the exact cross-block classification requested by PC2. What remains
open is a phase or offset theorem that rules out all four resonance types.

## 5. Cycle-bit flips are executable repair trades

### Theorem PX4 — PROVED

Toggle one phase bit `ε_{i,C}` and leave all other bits fixed. The resulting
change:

1. removes exactly `2|C|` cells and inserts exactly `2|C|` cells;
2. preserves every row sum and every column sum exactly;
3. is supported on the two coarse blocks
   `(i,σ_0(i))` and `(i,σ_1(i))`;
4. keeps every fine cell inside `S_n` and every coarse cell inside `S_m`.

Hence the toggle is an executable binary row-column-preserving trade, and it
cannot create a forbidden triple internal to either factor projection.

### Proof

For each outer layer `r`, the toggle replaces `τ_s(u)` by `τ_{1-s}(u)` for all
`u in C`. Pointwise disjointness of the two fine layers makes all removed and
inserted cells distinct. There are `|C|` replacements in each of the two outer
layers.

Theorem PX1 applies before and after the toggle, so global row and column sums
are unchanged. More locally, `τ_0(C)=τ_1(C)`, so the set of fine columns used
inside each affected coarse column block is unchanged. The coarse coordinates
are fixed, and each inserted fine coordinate is still a point of one of the
two factor permutation layers. \(\square\)

This proves the row-column and factor-protection parts of PC6 for cycle-phase
repairs. Bounded multiplicity of the mixed carry signatures remains open.

## 6. Cycle phases alone do not give product closure

The next statement is deliberately negative.

### Claim PX5 — REFUTED

> For every pair of saturated no-three factor configurations, some cycle-phase
> state produces a no-three product.

### Counterexample

Take the outer side `m=2` with

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0),
\]

and the inner side `n=3` with

\[
\tau_0=(0,2,1),
\qquad
\tau_1=(1,0,2).
\]

Both unions are saturated and no-three. The permutation
`τ_1^{-1}τ_0` is one 3-cycle, so a cycle-phase state is only a pair of bits
`(ε_0,ε_1)`. Every one of the four states contains the displayed collinear
triple:

| `(ε_0,ε_1)` | Collinear triple |
|---|---|
| `(0,0)` | `(1,2), (3,3), (5,4)` |
| `(0,1)` | `(0,0), (2,1), (4,2)` |
| `(1,0)` | `(1,0), (3,1), (5,2)` |
| `(1,1)` | `(0,1), (2,2), (4,3)` |

Each line has horizontal step `2` and vertical step `1`. Thus even the full
cycle-wise phase freedom can be trapped by a rational coarse/fine resonance.

A still simpler warning is the diagonal `2x2` tensor state, which contains
`(0,0),(1,1),(2,2),(3,3)`.

## 7. Finite verification

Run

```bash
python scripts/verify_product_construction.py
python scripts/verify_product_construction.py --include-four
```

The default check exhausts all ordered saturated no-three permutation-pair
factors for `(m,n)` equal to `2x2`, `2x3`, `3x2`, and `3x3`, together with all
cycle-phase states. It verifies PX1 and PX2 on every state and every point
triple.

The extended check also exhausts `2x4`, `3x4`, `4x2`, and `4x3`. The observed
numbers of no-three products are:

| `(m,n)` | Phase states checked | No-three products |
|---|---:|---:|
| `(2,2)` | 16 | 12 |
| `(2,3)` | 32 | 0 |
| `(3,2)` | 64 | 0 |
| `(3,3)` | 128 | 0 |
| `(2,4)` | 1184 | 0 |
| `(3,4)` | 9344 | 0 |
| `(4,2)` | 1280 | 0 |
| `(4,3)` | 2560 | 0 |

These counts are finite evidence, not an asymptotic theorem. They show that a
successful PC3 theorem must use more than independent cycle phases in the
unmodified mixed-radix lift, or must combine those phases with a stronger
offset, digit, or repair mechanism.

## 8. Track status after these results

- **PC1: complete.** PX1 gives an explicit `O(mn)` saturated product encoding
  with two permutation layers.
- **PC2: partially complete.** PX2 and PX3 give the exact determinant, carry
  normal form, and four cross-block types. Elimination of the four resonance
  equations is open.
- **PC3: open, with one candidate refuted.** PX5 rules out cycle phases alone.
- **PC4: open.** No no-three multiplicative closure theorem is proved.
- **PC5: open.** No arithmetic coverage follows without PC4.
- **PC6: partially complete.** PX4 gives exact product-compatible binary trades
  and factor-projection protection; carry-signature bounds are open.
