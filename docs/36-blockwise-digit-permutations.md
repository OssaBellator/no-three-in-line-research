# Blockwise digit permutations and a side-ten product witness

This chapter enlarges the global radix maps from Chapters 27--35 without
changing the ambient `mn x mn` grid. Fine digits may be permuted independently
inside each coarse row block and each coarse column block.

The enlargement preserves the four-regular factor-product host, but it is
strictly stronger geometrically: one blockwise reversal removes the quantified
`2 x 5` obstruction and gives an exact saturated no-three configuration at side
ten.

## 1. Locally permuted mixed-radix coordinates

For each coarse row `i in [m]`, choose a permutation

\[
\alpha_i\in\operatorname{Sym}([n]),
\]

and for each coarse column `j in [m]`, choose

\[
\beta_j\in\operatorname{Sym}([n]).
\]

Define

\[
X_c^\alpha(i,u)=ni+\alpha_i(u),
\qquad
X_f^\alpha(i,u)=m\alpha_i(u)+i,
\]

and

\[
Y_c^\beta(j,v)=nj+\beta_j(v),
\qquad
Y_f^\beta(j,v)=m\beta_j(v)+j.
\]

For an orientation `theta in {cc,cf,fc,ff}`, flatten one factor-product cell
`(i,j,u,v)` as

\[
F_{\theta,\alpha,\beta}(i,j,u,v)
=
\left(
X_{\theta_x}^\alpha(i,u),
Y_{\theta_y}^\beta(j,v)
\right).
\]

Let

\[
\mathcal H^{\theta,\alpha,\beta}_{m,n}
=
\left\{
F_{\theta,\alpha,\beta}(i,\sigma_r(i),u,\tau_s(u)):
 r,s\in\{0,1\}
\right\}.
\]

## Theorem PX24 — PROVED

For arbitrary blockwise digit permutations `alpha_i,beta_j` and every global
orientation `theta`, the locally permuted factor-product host is a simple
four-regular bipartite graph on the `mn` scalar rows and `mn` scalar columns.
Consequently, every spanning degree-two subgraph:

- has exactly `2mn` cells;
- has exactly two cells in every scalar row and column;
- decomposes in linear time into two cell-disjoint permutation layers;
- retains both factor projections.

### Proof

Both maps

\[
(i,u)\mapsto X_{\theta_x}^\alpha(i,u),
\qquad
(j,v)\mapsto Y_{\theta_y}^\beta(j,v)
\]

are bijections onto `[mn]`. In coarse-major mode, the coarse block is recovered
by integer division and the fine digit is inverted through the corresponding
local permutation. In fine-major mode, the coarse index is recovered modulo
`m`, followed again by inversion of the local permutation.

For one decoded row pair `(i,u)`, the two outer layers give two distinct coarse
columns and the two inner layers give two distinct fine columns. Hence the four
factor-layer products give four distinct scalar columns.

Conversely, fix a decoded column pair `(j,v)`. For each outer layer there is a
unique `i=sigma_r^{-1}(j)`, and for each inner layer there is a unique
`u=tau_s^{-1}(v)`. Thus exactly four host cells meet the scalar column.

The degree-two and permutation-layer conclusions now follow exactly as in PX9:
a spanning two-regular bipartite graph is a disjoint union of even cycles, whose
alternating edge colours are two perfect matchings. \(\square\)

The exact full-selector width-three CNF from PX10 applies without change after
the locally permuted host cells are constructed.

## 2. A parity-reflection subfamily

Take `m=2` and the saturated outer factor

\[
\sigma_0=(0,1),
\qquad
\sigma_1=(1,0).
\]

Let

\[
\alpha_0=\beta_0=\operatorname{id},
\qquad
\alpha_1(u)=\beta_1(u)=n-1-u,
\]

and use the `ff` orientation. Select both outer layers but only one fine
permutation `tau`. The resulting point set is

\[
\boxed{
R_n(\tau)=
\left\{
(x,y):
 x\in\{2u,2n-1-2u\},
 y\in\{2\tau(u),2n-1-2\tau(u)\},
 u\in[n]
\right\}.
}
\]

### Corollary PX24a — PROVED

For every permutation `tau` of `[n]`, `R_n(tau)` is a saturated configuration
of `4n` points in the `2n x 2n` grid.

### Proof

Every even scalar row is `2u` for a unique `u`, and every odd scalar row is
`2n-1-2u` for a unique `u`; each contains the two displayed column choices.
Because `tau` is a permutation, the same statement holds for columns. \(\square\)

## 3. Exact side-ten witness

Use the side-five factor pair

\[
\tau_0=(0,2,1,4,3),
\qquad
\tau_1=(2,4,0,3,1).
\]

Apply the parity-reflection construction to `tau=tau_1`. Alternating-cycle
colouring gives the two permutation layers

\[
\pi_0=(4,2,1,3,0,9,6,8,7,5),
\]

\[
\pi_1=(5,7,8,6,9,0,3,1,2,4).
\]

### Theorem PX25 — PROVED

The union of the graphs of `pi_0,pi_1` is a saturated no-three configuration of
20 points in `[10]^2`. Every cell belongs to the locally reversed `2 x 5`
factor-product host above.

### Proof

Permutation and host membership are direct from the displayed construction.
The verifier checks all

\[
\binom{20}{3}=1140
\]

integer determinants and finds none equal to zero. This is an exact finite
certificate. \(\square\)

Thus the positive defect gap in every **unmodified** `2 x 5` host from PX23 is
not an obstruction to factor-compatible product constructions in the same
ambient side length. Non-global digit maps genuinely add useful geometry.

## 4. Exact finite census of the reflection lift

### Theorem PX26 — PROVED FINITE

Exhausting every permutation `tau in Sym([n])` for `2 <= n <= 8` gives:

| Base side `n` | No-three permutations for `R_n(tau)` | First / unique witness |
|---:|---:|---|
| 2 | 1 | `(1,0)` |
| 3 | 0 | -- |
| 4 | 0 | -- |
| 5 | 1 | `(2,4,0,3,1)` |
| 6 | 0 | -- |
| 7 | 0 | -- |
| 8 | 0 | -- |

The count is literal, not modulo reflection or permutation equivalence.

This refutes the parity-reflection lift as a universal doubling theorem while
retaining its exact side-ten success. More general blockwise permutations and
full degree-two selection remain substantially larger families.

## Verification

Run

```bash
python scripts/verify_product_blockwise_digits.py
```

The script verifies PX24 on the displayed host, checks the side-ten certificate,
and performs the complete reflection-lift census through base side eight using
only the standard library.
