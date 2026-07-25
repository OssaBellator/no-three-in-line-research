# Fixed heavy conflict lines are absorbed outside the protected core or force a large core

CMR564--CMR570 convert static canonical collateral into fixed low-height heavy
lines, secant stars, matching walls, heavy prefixes, or dispersed carry cells.
CMR599--CMR604 ensure that every such line has one protected-selector owner.
This chapter executes the heavy single-line branch directly.

A nonaxis line is itself a partial matching: it contains at most one cell in
every source row and target column.  At a protected state of size `k`, at most
`2k` cells of that line can touch protected vertices.  Every other line cell is
simultaneously compatible with the complete protected matching and may be
inserted into the canonical forbidden matching in one batch.  The resulting
line-clean cylinder avoids those cells at zero residual restoration cost.

Thus a line with `r` relevant cells either grows the protected matching by at
least `r-2k`, or the protected core already has size at least `r/2`.  After the
absorption, at most `2k` cells of the line remain potentially allowed, giving
exact binomial caps on all residual rank-zero and rank-one atoms supported by
that line.

Fix one canonical protected selector state on a residual board of side `n`.
Let

\[
P
\]

be its protected partial matching and put

\[
k=|P|.
\]

Let `K` be any nonaxis real line and let

\[
X_K
\]

be a set of `r` residual board cells on `K`.  In applications, `X_K` is the set
of canonical allowed cells involved in the fixed heavy-line profile.

## 1. Protected vertices meet few cells of one line

### Theorem CMR605 — PROVED

The number of cells of `X_K` incident with a protected source or target vertex
satisfies

\[
\boxed{
|\{x\in X_K:x\cap V(P)\ne\varnothing\}|
\le
2k.
}
\]

Consequently the free line-cell set

\[
X_K^\circ
=
\{x\in X_K:x\cap V(P)=\varnothing\}
\]

satisfies

\[
\boxed{
|X_K^\circ|
\ge
\max\{0,r-2k\}.
}
\]

### Proof

A nonaxis line meets each source row and each target column in at most one cell.
Every protected matching edge contributes one protected source vertex and one
protected target vertex.  Therefore its two endpoints can account for at most
two cells of `K`.  Sum over the `k` protected edges. ∎

The estimate is a union bound; a line cell meeting two protected endpoints is
counted twice and can only improve the conclusion.

## 2. All free line cells absorb simultaneously

### Theorem CMR606 — PROVED

The set

\[
P\cup X_K^\circ
\]

is a partial matching.  It has a canonical perfect-matching extension

\[
F_{P,K}
\]

and the exact derangement cylinder

\[
\mathcal D_{P,K}
=
\{\delta\in\operatorname{PM}(K_{n,n}):
\delta\cap F_{P,K}=\varnothing\}
\]

has size

\[
\boxed{|\mathcal D_{P,K}|=D_n.}
\]

Every state in this cylinder avoids every cell of `X_K^\circ` at zero residual
restoration cost.

### Proof

Cells on one nonaxis line use distinct source and target vertices, so
`X_K^\circ` is a partial matching.  Its endpoints avoid `V(P)` by definition,
so its union with `P` is also a partial matching.  Apply the canonical extension
CMR571. ∎

This is bulk protected absorption specialized to one geometric line.

## 3. Exact post-absorption line caps

Let

\[
Y_K
=
X_K\setminus X_K^\circ
\]

be the cells of the line touching the old protected core.  Thus `|Y_K|<=2k`.

### Theorem CMR607 — PROVED

After passing to the cylinder `\mathcal D_{P,K}`:

1. the number of possible rank-zero candidate triples supported on `K` and
   using cells from `X_K` is at most
   \[
   \boxed{
   \binom{|Y_K|}{3}
   \le
   \binom{2k}{3};
   }
   \]
2. for any fixed paid endpoint `z\in K`, the number of possible rank-one
   candidate triples through `z` and using two cells from `X_K` is at most
   \[
   \boxed{
   \binom{|Y_K|}{2}
   \le
   \binom{2k}{2}.
   }
   \]

Binomial coefficients with upper argument below the lower one are zero.

### Proof

Every free line cell belongs to the new forbidden matching and is absent from
every cylinder state.  Any surviving atom supported on `K` must therefore use
only cells of `Y_K`.  Choose three such cells for rank zero or two for rank one.
∎

The bounds ignore compatibility and current availability, so they are safe
upper caps.

## 4. Quantitative atom destruction

Suppose the old canonical profile contains `T_0(K)` rank-zero atoms or
`T_1(z,K)` rank-one atoms on the line.

### Theorem CMR608 — PROVED

The line absorption removes at least

\[
\boxed{
\max\left\{0,
T_0(K)-\binom{2k}{3}
\right\}
}
\]

rank-zero line atoms and at least

\[
\boxed{
\max\left\{0,
T_1(z,K)-\binom{2k}{2}
\right\}
}
\]

rank-one line atoms from the canonical allowed profile.

At the same time, protected matching size grows by exactly

\[
|X_K^\circ|
\ge
\max\{0,r-2k\}.
\]

### Proof

CMR607 bounds the number of atoms that can remain after absorption.  Subtract
those caps from the old atom counts.  The protected-size statement is CMR605--
CMR606. ∎

Thus heavy-line execution has two simultaneous monotone effects: it enlarges
the protected forbidden matching and reduces the line's conflict profile.

## 5. Finite total heavy-line growth

Consider any monotone sequence of line absorptions in which every newly
absorbed line-cell set is disjoint from the current protected matching.  Let
`k_0` be the initial protected size and let `g_i` be the number of new cells
absorbed at step `i`.

### Theorem CMR609 — PROVED

One has

\[
\boxed{
\sum_i g_i
\le
n-k_0.
}
\]

Consequently, the number of line-execution steps satisfying

\[
g_i\ge G
\]

is at most

\[
\boxed{
\left\lfloor\frac{n-k_0}{G}\right\rfloor
}
\]

for every integer `G>=1`.

### Proof

Every step adds `g_i` new edges to one protected partial matching.  The final
protected matching has size `k_0+sum_i g_i` and cannot exceed `n`. ∎

Repeated heavy lines cannot draw indefinitely on fresh compatible line cells.

## 6. Heavy-line execution endpoint

Let

\[
\rho_2(A)
=
\min\{r\ge2:\binom r2\ge A\},
\qquad
\rho_3(A)
=
\min\{r\ge3:\binom r3\ge A\}.
\]

### Corollary CMR610 — PROVED

At a protected state of size `k`:

1. a rank-one line supporting `A` atoms either
   - grows the protected matching by at least
     \[
     \boxed{
     \max\{0,\rho_2(A)-2k\}
     }
     \]
     line cells, or
   - certifies
     \[
     \boxed{k\ge\rho_2(A)/2;}
     \]
2. a rank-zero line supporting `A` atoms either
   - grows the protected matching by at least
     \[
     \boxed{
     \max\{0,\rho_3(A)-2k\}
     }
     \]
     line cells, or
   - certifies
     \[
     \boxed{k\ge\rho_3(A)/2.}
     \]

After execution, the surviving line atoms obey the caps of CMR607.  The line's
primitive height also obeys the CMR567 bound in terms of its original involved
cell count.

### Proof

CMR559 gives at least `rho_2(A)` or `rho_3(A)` involved line cells.  Apply
CMR605--CMR608.  If the corresponding free-cell lower bound is zero, then the
involved cell count is at most `2k`, giving the core-size alternative. ∎

## 7. Revised frontier

The fixed heavy-line branch now has a direct monotone execution.

- All line cells outside the protected core absorb simultaneously.
- Total fresh line absorption is bounded by residual matching capacity.
- If little can be absorbed, the protected core is already large relative to
  the heavy-line occupancy.
- Post-absorption line collateral has explicit binomial caps.

The remaining fixed-certificate branches are repeated-cell secant stars,
matching-vertex walls, heavy/dispersed prefix cells, and persistent unavailable
cores after absorption capacity becomes large or exhausted.  Their expected
payments remain protected-reserve depletion, full-token return, deletion
ancestry, strict potential decrease, or envelope expansion.

No all-`n` theorem is claimed.  Protected-line incidence, simultaneous
absorption, residual atom caps, monotone growth, and heavy-line threshold
arithmetic are checked in
[`scripts/verify_prime_power_heavy_line_absorption.py`](../scripts/verify_prime_power_heavy_line_absorption.py).
