# Full product-host selection and carry multiplicity

This chapter continues
[`docs/27-all-n-product-construction.md`](27-all-n-product-construction.md).
It enlarges the cycle-phase family to every degree-two state in the full
factor-product host, gives an exact 3-CNF formulation, proves repair-state
connectivity, and bounds fixed carry levels. It does **not** prove
multiplicative closure.

Use the notation and four radix orientations of Chapter 27. For one orientation
`theta`, let

\[
\mathcal H^\theta_{m,n}
=
\{F_\theta(c,f):c\in S_m,\ f\in S_n\}.
\]

By PX6 this host has `4mn` cells and line cap `4 min(m,n)`.

## 1. Full product-host two-factor selection

The cycle-phase family uses only a small subset of the host. A general
factor-compatible state selects

\[
Q\subseteq\mathcal H^\theta_{m,n}
\]

with degree exactly two at every scalar row and every scalar column.

### Theorem PX9 — PROVED

The factor-product host is a simple four-regular bipartite graph between the
`mn` scalar rows and `mn` scalar columns. Every degree-two spanning subgraph
`Q` has exactly `2mn` cells, is saturated, and decomposes in linear time into
two cell-disjoint permutation layers. Every selected cell retains its coarse
projection in `S_m` and fine projection in `S_n`.

### Proof

Decode one scalar row as `(i,u)`. There are two choices

\[
j\in\{\sigma_0(i),\sigma_1(i)\}
\]

and independently two choices

\[
v\in\{\tau_0(u),\tau_1(u)\}.
\]

Pointwise disjointness in both factors makes the resulting four scalar columns
distinct. Reversing rows and columns proves degree four on the column side.

A spanning degree-two bipartite graph is a disjoint union of even cycles.
Alternately colour the edges of every cycle. Each colour meets every row and
column exactly once, so its edges form a perfect matching and hence a
permutation layer. Host membership gives the projection claim. `square`

The cycle-phase states of PX1 are degree-two host states, but not conversely.

## 2. Exact full-selector width-three CNF

For every host cell `e`, introduce a Boolean variable `x_e` indicating whether
that cell is selected.

### Theorem PX10 — PROVED

Existence of a no-three degree-two state in
`H^theta_{m,n}` is equivalent to satisfiability of an explicit width-three CNF
with `4mn` variables and

\[
16mn+T(\mathcal H^\theta_{m,n})
\]

clauses before duplicate removal. Consequently PX6a gives the bound

\[
\boxed{
16mn+
\frac13\binom{4mn}{2}
\bigl(4\min(m,n)-2\bigr).
}
\]

### Construction and proof

Each scalar row or column has four incident host cells. For each of its four
three-element subsets `A`, add both clauses

\[
\bigvee_{e\in A}x_e,
\qquad
\bigvee_{e\in A}\neg x_e.
\]

The positive clauses forbid degree zero or one. The negative clauses forbid
degree three or four. Thus the eight clauses enforce degree exactly two.
There are `2mn` row/column vertices, producing `16mn` clauses.

For every real-collinear host triple `{e,f,g}`, add

\[
\neg x_e\vee\neg x_f\vee\neg x_g.
\]

The satisfying assignments are exactly the no-three degree-two host states.
The clause count follows, followed by PX6a. `square`

The verifier constructs this CNF and, for every `2 x 2` orientation, checks by
complete truth-table enumeration that its model count equals the direct
row-degree search count: eleven models for each fixed canonical factor pair.

## 3. Alternating-cycle repair connectivity

### Theorem PX11 — PROVED

Let `Q,Q'` be two degree-two states in the same product host. Their symmetric
difference decomposes into edge-disjoint even cycles whose edges alternate
between `Q minus Q'` and `Q' minus Q`. Toggling these cycles one at a time
transforms `Q` into `Q'`. Every intermediate state remains degree two at every
row and column and remains factor-compatible.

### Proof

Colour edges of `Q minus Q'` red and edges of `Q' minus Q` blue. At every row
or column vertex, the red and blue degrees are equal because both states have
degree two there. Pair red and blue half-edges locally. Following paired
half-edges decomposes the symmetric difference into alternating even cycles.
On one cycle, replacing red edges by blue edges preserves every incident
vertex degree. All other vertices are unchanged, and all edges remain in the
host. Repeat over the cycles. `square`

This closes the connectivity and executable-trade part of PC6 for the entire
product-compatible state space. It does not give a monotone collinearity
potential.

## 4. Fixed-area carry multiplicity

For a finite no-three set `S` in the integer plane and an integer `D`, write

\[
N_D(S)
=
\#\{(a,b,c)\in S^3:
 a,b,c\text{ distinct and }\det(a,b,c)=D\}.
\]

### Theorem PX12 — PROVED

If `|S|=s`, then

\[
N_0(S)=0
\]

and, for every nonzero `D`,

\[
\boxed{N_D(S)\le2s(s-1).}
\]

Consequently, for a saturated no-three factor `S_n`,

\[
N_D(S_n)\le4n(2n-1).
\]

In the ordinary `cc` product, fix an ordered coarse projected triple. For each
nonzero fine carry `kappa`, at most

\[
\boxed{4n(2n-1)}
\]

ordered fine projected triples have

\[
\Delta_{uv}=n\kappa.
\]

The analogous coarse determinant-level bound is `4m(2m-1)`.

### Proof

The zero-level statement is the no-three property. For nonzero `D`, choose the
ordered pair `(a,b)`, in `s(s-1)` ways. The equation

\[
\det(a,b,c)=D
\]

places `c` on one real line parallel to `ab`. That line contains at most two
points of `S`, otherwise `S` would contain three collinear points. Thus every
ordered pair admits at most two choices for `c`. Apply this with `s=2n` and
`D=n kappa`. `square`

This gives an arithmetic carry-level multiplicity bound for the
projection-distinct branch of PC6. Simultaneous concentration of the two hybrid
determinants remains open.

## 5. The phase obstruction is not a host obstruction

For the factor pairs used in PX8,

\[
\sigma_0=(0,1),\qquad \sigma_1=(1,0),
\]

\[
\tau_0=(0,2,1),\qquad \tau_1=(1,0,2),
\]

all 64 global-orientation cycle-phase states fail. Nevertheless, in the `cf`
product host the two permutations

\[
\pi_0=(1,5,3,0,4,2),
\qquad
\pi_1=(3,1,5,2,0,4)
\]

form a degree-two host subset with no collinear triple. Thus PX8 is an
obstruction to the phase parameterization, not to the entire product host.

The full selector also gives an exact side-nine certificate from selected
`3 x 3` factors:

\[
\pi_0=(3,6,1,8,0,2,5,7,4),
\]

\[
\pi_1=(4,1,3,6,8,0,7,2,5).
\]

These are finite constructions, not a closure theorem.

## 6. Exact finite census

Run

```bash
python scripts/verify_product_two_factor.py
python scripts/verify_product_two_factor.py --extended
python scripts/verify_product_carry_multiplicity.py
```

Each table entry below is

`successful ordered factor-pair instances / total no-three degree-two models`.

| `(m,n)` | Instances | `cc` | `cf` | `fc` | `ff` |
|---|---:|---:|---:|---:|---:|
| `(2,2)` | 4 | `4 / 44` | `4 / 44` | `4 / 44` | `4 / 44` |
| `(2,3)` | 8 | `0 / 0` | `8 / 16` | `8 / 16` | `0 / 0` |
| `(3,2)` | 8 | `0 / 0` | `8 / 16` | `8 / 16` | `0 / 0` |
| `(3,3)` | 16 | `0 / 0` | `8 / 16` | `8 / 16` | `0 / 0` |
| `(2,4)` | 80 | `0 / 0` | `32 / 64` | `32 / 64` | `40 / 96` |
| `(4,2)` | 80 | `40 / 96` | `32 / 64` | `32 / 64` | `0 / 0` |
| `(2,5)` | 128 | `0 / 0` | `0 / 0` | `0 / 0` | `0 / 0` |
| `(5,2)` | 128 | `0 / 0` | `0 / 0` | `0 / 0` | `0 / 0` |

The full selector strictly enlarges the positive range and repairs the `2 x 3`
and some `3 x 3` instances. However, the exhaustive `2 x 5` and `5 x 2`
zeros show that arbitrary degree-two selection in the four unmodified global
factor-product hosts is not a universal composition rule.

The carry verifier exhausts every ordered saturated no-three permutation pair
through side five and checks PX12 at every signed determinant level.

## 7. Remaining boundary

- PC1 is complete in the full product-host state space.
- PC2 still lacks elimination of simultaneous hybrid resonances.
- PC3 has exact phase and full-selector CNFs, but both unmodified routes have
  finite obstructions.
- PC4 and PC5 still lack an infinite closure class and arithmetic coverage.
- PC6 now has connected executable repair states and fixed-carry concentration;
  the missing result is a monotone or resampling theorem for simultaneous
  hybrid resonances.
