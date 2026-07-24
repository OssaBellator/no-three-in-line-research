# Mixed-radix product constructions

This chapter develops
[`tracks/all-n-product-construction.md`](../tracks/all-n-product-construction.md).
It completes the saturation task, classifies every cross-block collinearity by
an exact determinant identity, and refutes independent cycle phases as a
universal closure mechanism. It does **not** prove multiplicative closure.

All grids are zero-indexed. Write saturated factor configurations as

\[
S_m=\{(i,\sigma_r(i)):i\in[m],\ r\in\{0,1\}\},
\qquad
S_n=\{(u,\tau_s(u)):u\in[n],\ s\in\{0,1\}\}.
\]

The two permutations in each factor are pointwise disjoint.

## 1. Independent cycle-phase encoding

Let `pi=tau_1^{-1} tau_0` and write `C(u)` for the orbit of `u`. For every
output layer `r`, coarse row `i`, and orbit `C`, choose
`epsilon_{r,i,C} in {0,1}`. Define

\[
\boxed{
\Pi_r(ni+u)=n\sigma_r(i)+\tau_{\varepsilon_{r,i,C(u)}}(u).
}
\]

Let `P_{m,n}(epsilon)` be the union of the two graphs of `Pi_0,Pi_1`.

### Theorem PX1 — PROVED

Each `Pi_r` is a permutation of `[mn]`; the two graphs are cell-disjoint.
Therefore the product has exactly `2mn` cells and two points in every row and
column. It is constructible in `O(mn)` operations once the phases are given.

### Proof

Fix `r` and a target coarse column `j`; then `i=sigma_r^{-1}(j)` is unique. For
an orbit `C` of `pi`,

\[
\tau_0(C)=\tau_1(\pi(C))=\tau_1(C).
\]

Thus either restriction `tau_0|_C` or `tau_1|_C` bijects `C` to the same
right-vertex set. Choosing one restriction independently on every orbit gives
a permutation of `[n]`, hence `Pi_r` is a permutation. The two outputs in row
`ni+u` have distinct coarse digits `sigma_0(i),sigma_1(i)`, proving
disjointness. \(\square\)

If `pi` has `c` orbits, the family has `2^(2mc)` states.

## 2. Exact mixed-radix determinant

For encoded points

\[
P_t=(ni_t+u_t,nj_t+v_t),\qquad t=0,1,2,
\]

put

\[
\Delta_c=\det((i_0,j_0),(i_1,j_1),(i_2,j_2)),
\quad
\Delta_f=\det((u_0,v_0),(u_1,v_1),(u_2,v_2)),
\]

\[
\begin{aligned}
M={}&(i_1-i_0)(v_2-v_0)+(u_1-u_0)(j_2-j_0)\\
&-(j_1-j_0)(u_2-u_0)-(v_1-v_0)(i_2-i_0).
\end{aligned}
\]

### Theorem PX2 — PROVED

\[
\boxed{\det(P_0,P_1,P_2)=n^2\Delta_c+nM+\Delta_f.}
\]

A collinear triple satisfies

\[
\Delta_f=n\kappa,\qquad |\kappa|\le n-2,
\qquad
\boxed{n\Delta_c+M+\kappa=0.}
\]

### Proof

Expand after substituting `X_t=ni_t+u_t`, `Y_t=nj_t+v_t`. The coarse,
mixed, and fine terms are respectively `n^2 Delta_c`, `nM`, and `Delta_f`.
For a zero determinant, reduction modulo `n` makes `Delta_f` a multiple of
`n`. Since three points in `[n]^2` have
`|Delta_f| <= (n-1)^2 < n^2`, write `Delta_f=n kappa` with
`|kappa|<=n-2`, then divide by `n`. \(\square\)

## 3. Four cross-block types

Let `c` and `f` count distinct coarse and fine points in a product triple.

### Theorem PX3 — PROVED

If both factors are no-three, every bad product triple has one of:

| Type | Exact resonance |
|---|---|
| `(2,2)` | `Delta_c=Delta_f=0`, `M=0` |
| `(2,3)` | `Delta_c=0`, `Delta_f=n kappa != 0`, `M+kappa=0` |
| `(3,2)` | `Delta_c != 0`, `Delta_f=0`, `n Delta_c+M=0` |
| `(3,3)` | `Delta_c != 0`, `Delta_f=n kappa != 0`, `n Delta_c+M+kappa=0` |

Here `|kappa|<=n-2`, so `(2,3)` is impossible for `n=2`.

### Proof

If `c=1`, collinearity reduces to a forbidden fine triple; similarly `f=1`
reduces to a forbidden coarse triple. Thus `c,f>=2`. Two distinct projected
points give zero projected determinant because one point repeats; three give a
nonzero determinant by the factor no-three property. Substitute in PX2.
\(\square\)

PX2–PX3 finish the classification portion of PC2. Eliminating the four
resonances remains open.

## 4. Product-compatible repair

### Theorem PX4 — PROVED

Toggling one `epsilon_{r,i,C}` removes and inserts exactly `|C|` cells, preserves
every row and column, is supported on `(i,sigma_r(i))`, and keeps both factor
projections inside `S_m,S_n`.

### Proof

The toggle replaces `tau_s(u)` by `tau_{1-s}(u)` for `u in C`. Since
`tau_0(C)=tau_1(C)`, the affected fine-column set is unchanged. PX1 preserves
global saturation; the other output layer lies in the distinct coarse column
`sigma_{1-r}(i)`. \(\square\)

This closes the row-column and factor-protection parts of PC6. Carry-signature
multiplicity remains open.

## 5. Independent phases are insufficient

### Claim PX5 — REFUTED

Take

\[
\sigma_0=(0,1),\quad\sigma_1=(1,0),
\qquad
\tau_0=(0,2,1),\quad\tau_1=(1,0,2).
\]

Both factor unions are saturated and no-three. The fine transition is one
3-cycle, so a state is four bits
`(epsilon_{0,0},epsilon_{0,1},epsilon_{1,0},epsilon_{1,1})`. Every state has a
line; witnesses are:

| States | Witness |
|---|---|
| `0000,0001,0100,0101` | `(0,0),(1,2),(2,4)` |
| `0010,0110` | `(0,0),(2,1),(4,2)` |
| `0011` | `(1,2),(3,3),(5,4)` |
| `0111` | `(3,4),(4,3),(2,5)` |
| `1000` | `(3,3),(1,5),(2,4)` |
| `1001` | `(1,0),(3,1),(5,2)` |
| `1010,1011` | `(0,1),(1,3),(2,5)` |
| `1100,1101,1110,1111` | `(0,1),(2,2),(4,3)` |

Thus independent cycle phases in the raw mixed-radix lift do not prove PC3.

## 6. Verification and status

Run:

```bash
python scripts/verify_product_construction.py
python scripts/verify_product_construction.py --include-four
```

The exhaustive finite counts are:

| `(m,n)` | States | No-three products |
|---|---:|---:|
| `(2,2)` | 64 | 20 |
| `(2,3)` | 128 | 0 |
| `(3,2)` | 512 | 0 |
| `(3,3)` | 1024 | 0 |
| `(2,4)` | 18560 | 0 |
| `(4,2)` | 20480 | 16 |

The first four run by default; `--include-four` adds the last two. These are
finite checks, not an asymptotic theorem.

- **PC1 complete:** PX1.
- **PC2 partial:** PX2–PX3; resonance elimination open.
- **PC3 open:** independent cycle phases refuted by PX5.
- **PC4–PC5 open:** no multiplicative closure or arithmetic coverage.
- **PC6 partial:** PX4; carry-signature bounds open.
