# Geometric fibre occupancy moments give finite background-height certificates

CMR1814--CMR1821 attach to every exact geometric response host `G` the line
occupancy capacity

\[
\tau_G(\ell)=\max_{Q\in\operatorname{PM}(G)}|Q\cap\ell|.
\]

The full table has one entry for every nonaxis real grid line.  This chapter
compresses that table into three host moments and executes the compression on all
740 raw side-four and side-five hosts.  The moments give immediate certificates
whenever the background line heights are controlled uniformly, while an exact
height-layer identity retains the sharper nonuniform profile.

For `r=1,2,3`, define

\[
M_r(G)=\sum_\ell \binom{\tau_G(\ell)}r,
\]

where the sum ranges over nonaxis real lines containing at least two cells of the
ambient standard grid.

## 1. Occupancy moments

### Theorem CMR1830 -- PROVED

For every background set `B`, with

\[
h_\ell=|B\cap\ell|,
\]

the deterministic line-capacity row of CMR1816 is

\[
\mathcal C_G(B)
=
\sum_\ell
\left[
 \tau_G(\ell)\binom{h_\ell}{2}
 +\binom{\tau_G(\ell)}2h_\ell
 +\binom{\tau_G(\ell)}3
\right].
\]

Its three coefficient sums are exactly `M_1(G)`, `M_2(G)` and `M_3(G)`.

### Proof

This is the definition of the three moments after grouping the rank-one,
rank-two and rank-three terms of the line-capacity row. ∎

The moments are integers and depend only on the embedded response host.

## 2. Uniform background-height compiler

### Theorem CMR1831 -- PROVED

Suppose every relevant nonaxis background line has load at most `H`.  Then

\[
\boxed{
\mathcal C_G(B)
\le
\binom H2 M_1(G)+H M_2(G)+M_3(G).
}
\]

Consequently every corrected genuinely new geometric row is bounded by the same
quantity.

### Proof

For every line, `h_ell<=H`, so

\[
\binom{h_\ell}{2}\le\binom H2
\qquad\text{and}\qquad
h_\ell\le H.
\]

Multiply by the nonnegative occupancy coefficients, sum, and use CMR1816 for the
corrected row. ∎

For a triple-free background one may take `H=2`, giving the particularly simple
host score

\[
\boxed{E_2(G)=M_1(G)+2M_2(G)+M_3(G).}
\]

No response probability law enters this bound.

## 3. Exact height-layer identity

For every integer `s>=1`, put

\[
\mathcal L_s(B)=\{\ell:h_\ell\ge s\}.
\]

### Theorem CMR1832 -- PROVED

The complete line-capacity row has the exact expansion

\[
\boxed{
\mathcal C_G(B)
=
M_3(G)
+
\sum_{s\ge2}(s-1)
\sum_{\ell\in\mathcal L_s(B)}\tau_G(\ell)
+
\sum_{s\ge1}
\sum_{\ell\in\mathcal L_s(B)}
\binom{\tau_G(\ell)}2.
}
\]

Only finitely many terms are nonzero.

### Proof

Use the elementary layer identities

\[
\binom h2=\sum_{s=2}^h(s-1)
\qquad\text{and}\qquad
h=\sum_{s=1}^h1
\]

inside the definition of `C_G(B)` and interchange the finite sums. ∎

Thus the exact background dependence is a finite dot product between nested
background-line superlevels and precomputed host occupancies.

## 4. Maximum line occupancy through side five

### Theorem CMR1833 -- PROVED

Across the corrected raw geometric hosts, the maximum line occupancy has the
following distribution.

### Side four

\[
\boxed{
37\text{ hosts with maximum }2,
\quad
14\text{ with maximum }3,
\quad
35\text{ with maximum }4.
}
\]

### Side five

\[
\boxed{
379\text{ hosts with maximum }3,
\quad
275\text{ with maximum }4.
}
\]

In particular no executable side-five host permits a response matching with five
collinear selected cells.

### Proof

Enumerate the 86 side-four and 654 side-five raw hosts of CMR1800.  For every
nonaxis grid line, maximize its zero-one indicator score over the exact response
matchings, then take the largest capacity in the host. ∎

The side-four maximum-two class is exactly the 37 triple-free hosts of CMR1808.

## 5. Exact third-moment distributions

### Theorem CMR1834 -- PROVED

The rank-three occupancy moment

\[
M_3(G)=\sum_\ell\binom{\tau_G(\ell)}3
\]

has the following exact distributions.

### Side four

| `M_3(G)` | 0 | 1 | 4 | 5 |
|---:|---:|---:|---:|---:|
| raw hosts | 37 | 14 | 15 | 20 |

### Side five

| `M_3(G)` | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10 | 11 | 12 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| raw hosts | 1 | 4 | 30 | 63 | 128 | 126 | 64 | 54 | 94 | 62 | 22 | 6 |

### Proof

Compute every line capacity and sum its third binomial coefficient.  The counts
sum to 86 and 654. ∎

`M_3` is an upper linewise certificate.  The exact uniform numerator table of
CMR1809--CMR1810 is usually smaller because different line maxima need not occur
in one response.

## 6. Side-four denominator table

### Theorem CMR1835 -- PROVED

For each side-four response denominator `Z`, the table gives the number of raw
hosts and the exact maxima of `M_1`, `M_2`, `M_3` and the triple-free-background
score `E_2`.

| `Z` | hosts | max `M_1` | max `M_2` | max `M_3` | max `E_2` |
|---:|---:|---:|---:|---:|---:|
| 1 | 14 | 32 | 6 | 4 | 44 |
| 2 | 40 | 53 | 12 | 5 | 78 |
| 3 | 20 | 62 | 17 | 5 | 98 |
| 4 | 9 | 69 | 22 | 5 | 116 |
| 5 | 2 | 70 | 25 | 5 | 125 |
| 6 | 1 | 77 | 30 | 5 | 142 |

Every displayed maximum is taken over the exact coordinate-labelled hosts with
that denominator.

### Proof

Group the 86 raw hosts by their perfect-matching count and maximize the four
integer host scores. ∎

## 7. Side-five denominator table

### Theorem CMR1836 -- PROVED

For side five the corresponding table is:

| `Z` | hosts | max `M_1` | max `M_2` | max `M_3` | max `E_2` |
|---:|---:|---:|---:|---:|---:|
| 8 | 21 | 163 | 57 | 9 | 280 |
| 9 | 18 | 163 | 57 | 9 | 280 |
| 10 | 93 | 174 | 64 | 10 | 307 |
| 11 | 48 | 178 | 70 | 10 | 325 |
| 12 | 104 | 181 | 70 | 11 | 323 |
| 13 | 30 | 185 | 75 | 10 | 340 |
| 14 | 111 | 189 | 77 | 11 | 351 |
| 15 | 50 | 191 | 81 | 11 | 361 |
| 16 | 63 | 194 | 84 | 11 | 371 |
| 17 | 12 | 195 | 83 | 11 | 371 |
| 18 | 24 | 198 | 84 | 12 | 373 |
| 19 | 15 | 200 | 89 | 11 | 388 |
| 20 | 45 | 203 | 91 | 12 | 395 |
| 22 | 6 | 205 | 90 | 12 | 396 |
| 24 | 1 | 201 | 84 | 7 | 376 |
| 25 | 6 | 212 | 97 | 12 | 417 |
| 26 | 6 | 212 | 97 | 11 | 417 |
| 33 | 1 | 220 | 104 | 12 | 440 |

### Proof

Group the 654 raw hosts by denominator and maximize the four integer host scores.
The host counts agree with the expanded denominator census. ∎

The `E_2` maximum is computed hostwise; it is not obtained by adding three
independently attained moment maxima.

## 8. Occupancy-moment endpoint

### Corollary CMR1837 -- PROVED

The background-dependent geometric frontier now has the following finite host
compiler through side five.

1. Every raw host has a complete line-capacity table and three integer moments.
2. A uniform background-height cap `H` gives the immediate certificate
   `C(H,2)M_1+HM_2+M_3`.
3. Nonuniform heights enter through the exact nested-superlevel identity of
   CMR1832.
4. Triple-free backgrounds use the precomputed integer score `E_2`.
5. Exact rank-three numerators, nested assignments and exact marginal rows may
   replace any coarser moment term.
6. The moment tables do not erase line, owner or provenance labels in an exact
   quotient; they are upper certificates for a stated background-height class.

No all-`n` conclusion is claimed.  The remaining geometric work is to attach the
actual background-height and provenance classes to these finite host signatures.

All raw-host counts, line capacities, moment tables, uniform-height inequalities
and exact height-layer identities are checked in
[`scripts/verify_prime_power_geometric_fibre_occupancy_moments.py`](../scripts/verify_prime_power_geometric_fibre_occupancy_moments.py).
