# Static selector line banks splice into secant stars or linear conflict packings

CMR558--CMR563 convert every static canonical collateral profile into a heavy
line or a large bank of distinct conflict lines.  The distinct-line branches
already have strong intersection geometry: two different real lines cannot
share two grid cells.

For rank one, every line passes through the same paid endpoint.  Choosing one
conflict on each line therefore gives a repeated-cell secant star whose outside
pairs are automatically cell-disjoint.

For rank zero, choosing one conflict on each line gives a linear three-uniform
set system.  A degree split yields either a repeated-cell secant star or a
large pairwise cell-disjoint conflict packing.

## 1. Distinct rank-one secants are an exact secant star

Fix a paid endpoint `z` and distinct nonaxis lines

\[
H_1,\ldots,H_A
\]

through `z`.  For each `i`, choose one rank-one conflict

\[
C_i=\{z,a_i,b_i\}
\]

supported on `H_i`.

### Theorem CMR564 — PROVED

For distinct `i,j`,

\[
\boxed{
\{a_i,b_i\}\cap\{a_j,b_j\}=\varnothing.
}
\]

Consequently

\[
\boxed{
\{C_1,\ldots,C_A\}
}
\]

is a repeated-cell secant star centred at `z` with `A` pairwise cell-disjoint
outside pairs, exactly in the sense of CMR390 and CMR487.

### Proof

If two outside pairs shared a cell `w`, then both supporting lines would contain
the two distinct points `z,w`.  Uniqueness of the real line through two points
would give `H_i=H_j`, contradiction. ∎

Thus the dispersed rank-one branch of CMR562 is already an existing geometric
endpoint, with no further extraction loss.

## 2. Distinct rank-zero lines form a linear triple system

Let

\[
H_1,\ldots,H_A
\]

be distinct nonaxis lines, and choose one rank-zero conflict triple

\[
C_i\subseteq H_i
\]

from each line.

### Theorem CMR565 — PROVED

The family

\[
\mathcal C=\{C_1,\ldots,C_A\}
\]

is a linear three-uniform set system:

\[
\boxed{
i\ne j
\quad\Longrightarrow\quad
|C_i\cap C_j|\le1.
}
\]

If one cell `z` belongs to `R` members of `\mathcal C`, then those `R`
conflicts form a repeated-cell secant star centred at `z`, and their outside
pairs are pairwise cell-disjoint.

### Proof

Two distinct real lines share at most one point, proving linearity.

For conflicts containing `z`, if two outside pairs shared another cell `w`,
their lines would both contain `z,w` and hence would be equal. ∎

The same repeated-cell geometry therefore appears whenever line incidence
concentrates at one residual cell.

## 3. Fan-or-packing extraction

For a grid cell `x`, define its conflict degree

\[
d_{\mathcal C}(x)
=
|\{C\in\mathcal C:x\in C\}|.
\]

### Theorem CMR566 — PROVED

Fix an integer threshold

\[
R\ge2.
\]

At least one of the following holds.

1. **Repeated-cell secant star.**  Some cell belongs to at least `R` conflicts.
2. **Cell-disjoint conflict packing.**  The family contains at least
   \[
   \boxed{
   \left\lceil
   \frac{A}{3(R-1)}
   \right\rceil
   }
   \]
   pairwise cell-disjoint rank-zero conflicts on distinct lines.

### Proof

If the first branch fails, every cell has degree at most `R-1`.

Greedily choose a conflict and delete every conflict meeting it.  A chosen
triple has three cells, and each cell belongs to at most `R-1` remaining
conflicts.  Thus one greedy step deletes at most `3(R-1)` conflicts.  Continuing
until none remain selects at least the displayed number. ∎

The proof needs only bounded cell incidence; linearity identifies the
concentration branch as a genuine secant star.

## 4. Square-root distinct-line endpoint

### Corollary CMR567 — PROVED

Put

\[
R(A)=\max\{2,\lceil\sqrt A\rceil\}.
\]

Every bank of `A` distinct rank-zero conflict lines contains either

\[
\boxed{
\text{a repeated-cell secant star of size at least }R(A)
}
\]

or at least

\[
\boxed{
\left\lceil
\frac{A}{3(R(A)-1)}
\right\rceil
}
\]

pairwise cell-disjoint rank-zero conflicts on distinct lines.

In particular, the packing size is of order `\sqrt A`, while the star branch
has size at least `\sqrt A`.

### Proof

Apply CMR566 with the displayed threshold. ∎

No claim is made that cell-disjoint triples are simultaneously compatible in
one perfect matching; they are a geometric certificate packing with disjoint
edge support.

## 5. Static-selector splice

### Corollary CMR568 — PROVED

Every static canonical selector profile reaches at least one of the following
existing or sharply defined endpoints.

1. A heavy rank-zero residual line.
2. A heavy rank-one secant line through a paid endpoint.
3. A repeated-cell secant star with pairwise cell-disjoint outside pairs.
4. A pairwise cell-disjoint packing of rank-zero conflict triples on distinct
   lines.

More quantitatively:

- in the dispersed rank-one branch, the secant-star size is at least
  \[
  \boxed{
  \left\lfloor
  \sqrt{\frac{c_q}{4}(n)_2}
  \right\rfloor;
  }
  \]
- in the dispersed rank-zero branch, first take
  \[
  A\ge
  \left\lfloor
  \sqrt{\frac{c_q}{2}(n)_3}
  \right\rfloor
  \]
  distinct lines from CMR561, then apply CMR567.

### Proof

The heavy branches are CMR561--CMR562.  Apply CMR564 to the dispersed rank-one
branch.  Apply CMR565--CMR567 to the dispersed rank-zero branch. ∎

## 6. Revised frontier

The static canonical-collateral branch has now been spliced to established
geometry.

- The dispersed rank-one branch is exactly the repeated-cell secant-star
  endpoint already used by CMR390, CMR487, the paid mixed-ratio route, and the
  carry/token machinery.
- The dispersed rank-zero branch is either the same secant-star geometry or a
  disjoint-support line-certificate packing.
- Only the heavy single-line branches and the execution/payment of the
  rank-zero disjoint-support packing require additional quantitative work.
- The dynamic persistent canonical blocker from CMR557 remains the parallel
  availability branch.

The next strict theorem should attach the secant-star size from CMR568 to the
strongest existing mixed-ratio/carry thresholds and attach the rank-zero
packing to protected-line reserve depletion, conflict-free selection, or
deletion ancestry.

No all-`n` theorem is claimed.  Linearity, outside-pair disjointness, greedy
packing bounds, and square-root arithmetic are checked in
[`scripts/verify_prime_power_static_line_bank_splice.py`](../scripts/verify_prime_power_static_line_bank_splice.py).
