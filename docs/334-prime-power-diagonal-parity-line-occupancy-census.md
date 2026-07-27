# Diagonal parity controls the longest response lines

The line-occupancy compiler of CMR1814--CMR1837 treats every nonaxis real grid
line separately.  The longest such lines have an additional exact structure.
They are only the two diagonals of the square, and the forbidden identity matching
interacts with the anti-diagonal differently according to the parity of the side.

This chapter proves the all-side parity law and records the exact line-length /
occupancy census on all 740 raw side-four and side-five hosts.

Let

\[
\Omega_d=\{0,\ldots,d-1\}^2.
\]

Write

\[
\Delta_d=\{(i,i):0\le i<d\}
\]

for the main diagonal and

\[
\bar\Delta_d=\{(i,d-1-i):0\le i<d\}
\]

for the anti-diagonal.  The normalized response host forbids every edge of
`Delta_d` and the target `(0,1)`.

## 1. Classification of full-length nonaxis lines

### Theorem CMR1846 -- PROVED

A nonaxis real line contains `d` cells of `Omega_d` if and only if it is
`Delta_d` or `bar Delta_d`.

### Proof

Let the primitive integer step between consecutive grid points on the line be
`(a,b)`.  A line containing `d` grid cells has total displacement

\[
(d-1)(a,b)
\]

inside a box of coordinate width `d-1`.  Hence `|a|<=1` and `|b|<=1`.  The line
is nonaxis, so both coordinates are nonzero.  Up to reversing orientation the
step is `(1,1)` or `(1,-1)`, giving the two diagonals.  Both diagonals contain
exactly `d` cells. ∎

Thus no other direction can carry a full response matching.

## 2. Main-diagonal capacity

### Theorem CMR1847 -- PROVED

For every normalized response host and every deletion trace,

\[
\boxed{\tau_G(\Delta_d)=0.}
\]

### Proof

Every main-diagonal cell belongs to the forbidden opposite matching. ∎

The main diagonal contributes no rank-one, rank-two or rank-three response term.

## 3. Even anti-diagonal law

Assume `d>=4` is even.

### Theorem CMR1848 -- PROVED

The undeleted normalized host contains the complete anti-diagonal perfect
matching.  For a raw deletion trace `X`,

\[
\boxed{
\tau_{G_X}(\bar\Delta_d)=d
\quad\Longleftrightarrow\quad
X\cap\bar\Delta_d=\varnothing.
}
\]

### Proof

When `d` is even, the two diagonals are disjoint, so every anti-diagonal edge
avoids the forbidden identity matching.  The target `(0,1)` is not on the
anti-diagonal for `d>=4`.  Hence the complete anti-diagonal is an allowed perfect
matching exactly when no deletion removes one of its edges.  A matching selecting
`d` cells from a `d`-cell line must be that complete anti-diagonal. ∎

Deletion can lower the anti-diagonal capacity, but no parity obstruction exists
before deletion.

## 4. Odd anti-diagonal law

Assume `d=2c+1` is odd.

### Theorem CMR1849 -- PROVED

Every normalized response host satisfies

\[
\boxed{
\tau_G(\bar\Delta_d)\le d-2.
}
\]

### Proof

The central anti-diagonal cell `(c,c)` lies on the forbidden identity matching.
If a perfect matching selected all other `d-1` anti-diagonal edges, those edges
would use every row and column except row `c` and column `c`.  The final edge
would be forced to be `(c,c)`, which is forbidden.  Therefore at least two
anti-diagonal positions are absent. ∎

This improves the trivial line-length bound by two on every odd side.

### Theorem CMR1850 -- PROVED

For every odd `d>=5`, the undeleted normalized host attains the bound:

\[
\boxed{
\tau_{H_d}(\bar\Delta_d)=d-2.
}
\]

### Proof

Choose any index `i!=c`.  Retain every anti-diagonal edge except those in rows
`c` and `i`, then add

\[
(c,d-1-i)
\qquad\text{and}\qquad
(i,c).
\]

These two edges use the two remaining rows and columns, avoid the identity
matching, and avoid the target `(0,1)` when `d>=5`.  The resulting perfect
matching contains exactly `d-2` anti-diagonal edges.  Combine with CMR1849. ∎

## 5. Exact line-length occupancy census

For every raw host and every nonaxis grid line, record the pair

\[
(|\ell\cap\Omega_d|,\tau_G(\ell)).
\]

### Theorem CMR1851 -- PROVED

The exact side-four host-line counts are:

| line length | occupancy 0 | occupancy 1 | occupancy 2 | occupancy 3 | occupancy 4 |
|---:|---:|---:|---:|---:|---:|
| 2 | 1278 | 2148 | 702 | 0 | 0 |
| 3 | 45 | 195 | 70 | 34 | 0 |
| 4 | 97 | 0 | 40 | 0 | 35 |

The exact side-five counts are:

| line length | occupancy 0 | occupancy 1 | occupancy 2 | occupancy 3 | occupancy 4 | occupancy 5 |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 7345 | 36691 | 26596 | 0 | 0 | 0 |
| 3 | 311 | 3147 | 5407 | 1599 | 0 | 0 |
| 4 | 7 | 145 | 1033 | 1156 | 275 | 0 |
| 5 | 655 | 34 | 67 | 552 | 0 | 0 |

### Proof

Enumerate every raw host, every nonaxis line and every response matching.  The
capacity is the maximum line occupancy over the response list.  The side-four
counts sum to `86*54`, and the side-five counts sum to `654*130`. ∎

The zero entries are exact structural exclusions, not omitted cases.

## 6. Exact anti-diagonal distributions through side five

### Theorem CMR1852 -- PROVED

After removing the identically zero main-diagonal contribution from the
full-length rows of CMR1851, the anti-diagonal capacities are:

### Side four

| anti-diagonal capacity | 0 | 2 | 4 |
|---:|---:|---:|---:|
| raw hosts | 11 | 40 | 35 |

### Side five

| anti-diagonal capacity | 0 | 1 | 2 | 3 |
|---:|---:|---:|---:|---:|
| raw hosts | 1 | 34 | 67 | 552 |

### Proof

Each side has exactly two full-length nonaxis lines.  One is the main diagonal,
which contributes one zero-capacity line in every host by CMR1847.  Subtract
those 86 or 654 entries from the length-`d` rows of CMR1851. ∎

For side five, the absence of capacities four and five is the odd parity law
CMR1849.  For side four, the capacity-four hosts are exactly the deletion traces
which avoid the anti-diagonal.

## 7. Rank-three and line-energy consequences

### Theorem CMR1853 -- PROVED

The longest-line contribution to every geometric certificate may be treated as
follows.

1. The main diagonal is deleted permanently.
2. On even side, the anti-diagonal has full capacity precisely when its trace is
   untouched.
3. On odd side, its capacity is at most `d-2`, with equality already in the
   undeleted host for `d>=5`.
4. Through side five the exact anti-diagonal capacity is one integer table entry
   per raw host.
5. In the occupancy-moment or line-capacity row, the full-length contribution is
   therefore known without solving a new assignment.
6. Shorter lines retain their exact capacities from the finite census and may be
   combined with exact rank-three numerators or nested assignments.

This parity law does not certify the remaining background-dependent rows by
itself.  It removes the only possible length-`d` directions from the unresolved
assignment search and gives an exact longest-line coefficient for every current
side-four/five fibre.

Full-line classification, even/odd constructions, permutation checks through
side eight, and all 89,664 raw host-line capacities are checked in
[`scripts/verify_prime_power_diagonal_parity_line_occupancy.py`](../scripts/verify_prime_power_diagonal_parity_line_occupancy.py).
