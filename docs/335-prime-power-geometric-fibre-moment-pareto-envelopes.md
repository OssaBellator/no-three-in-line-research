# Geometric fibre moment Pareto envelopes compress the shorter-line frontier

CMR1830--CMR1837 attach to every exact side-four/five raw response host the
occupancy moments

\[
M_r(G)=\sum_\ell \binom{\tau_G(\ell)}r,
\qquad r=1,2,3.
\]

For a uniform background line-height cap `H`, the host-only upper score is

\[
F_H(G)
=
\binom H2M_1(G)+HM_2(G)+M_3(G).
\]

This chapter computes the exact denominator-preserving Pareto and integer-height
upper envelopes of these moment triples.  It also records a line-length-stratified
variant for background classes whose height cap depends on the length of the
supporting grid line.

All comparisons below preserve the exact response denominator `Z`; hosts with
different denominators are not identified.

## 1. Moment dominance

For moment triples `m=(m_1,m_2,m_3)` and `m'=(m'_1,m'_2,m'_3)`, write
`m<=m'` when every coordinate is at most the corresponding coordinate of `m'`.

### Theorem CMR1854 -- PROVED

If two exact hosts have the same response denominator and

\[
(M_1(G),M_2(G),M_3(G))
\le
(M_1(G'),M_2(G'),M_3(G')),
\]

then for every integer `H>=0`,

\[
\boxed{F_H(G)\le F_H(G').}
\]

The same domination holds for every nonnegative linear combination of the three
moments.

### Proof

The coefficients `C(H,2)`, `H` and `1` are nonnegative.  Multiply the three
coordinate inequalities by those coefficients and add.  The general statement is
identical. ∎

Thus a denominator class needs only its componentwise maximal moment triples.

## 2. Exact denominator-preserving Pareto compression

### Theorem CMR1855 -- PROVED

The 740 raw geometric hosts compress as follows under moment dominance.

| side | raw hosts | exact response denominators | unique Pareto moment triples |
|---:|---:|---:|---:|
| 4 | 86 | 6 | 11 |
| 5 | 654 | 18 | 58 |

Hence the complete uniform-height host frontier through side five contains only

\[
\boxed{11+58=69}
\]

denominator-preserving Pareto moment triples.

### Proof

Enumerate every raw host, compute its exact denominator and moment triple, group
by denominator, and delete every triple strictly dominated by another triple in
the same group.  Duplicate surviving triples are retained only once. ∎

### Theorem CMR1856 -- PROVED

The exact number of unique Pareto triples in every denominator class is:

### Side four

| `Z` | raw hosts | Pareto triples |
|---:|---:|---:|
| 1 | 14 | 2 |
| 2 | 40 | 3 |
| 3 | 20 | 2 |
| 4 | 9 | 2 |
| 5 | 2 | 1 |
| 6 | 1 | 1 |

### Side five

| `Z` | raw hosts | Pareto triples |
|---:|---:|---:|
| 8 | 21 | 3 |
| 9 | 18 | 3 |
| 10 | 93 | 7 |
| 11 | 48 | 3 |
| 12 | 104 | 9 |
| 13 | 30 | 4 |
| 14 | 111 | 4 |
| 15 | 50 | 4 |
| 16 | 63 | 3 |
| 17 | 12 | 2 |
| 18 | 24 | 4 |
| 19 | 15 | 2 |
| 20 | 45 | 3 |
| 22 | 6 | 2 |
| 24 | 1 | 1 |
| 25 | 6 | 2 |
| 26 | 6 | 1 |
| 33 | 1 | 1 |

The counts sum to 11 and 58 respectively.

## 3. Exact integer-height upper envelopes

A Pareto triple need not maximize `F_H` for any integer `H`.  Call it
**height-active** when it attains the maximum for at least one integer `H>=0` in
its denominator class.

### Theorem CMR1857 -- PROVED

Among the 69 denominator-preserving Pareto triples, exactly

\[
\boxed{11+46=57}
\]

are height-active: every side-four Pareto triple and 46 of the 58 side-five
Pareto triples.

For every denominator there is a terminal triple which maximizes `F_H` for all
sufficiently large integer `H`.  The exact active counts, first terminal heights
and terminal triples `(M_1,M_2,M_3)` are:

### Side four

| `Z` | Pareto | active | terminal from `H` | terminal triple |
|---:|---:|---:|---:|---:|
| 1 | 2 | 2 | 2 | `(32,6,0)` |
| 2 | 3 | 3 | 2 | `(53,12,1)` |
| 3 | 2 | 2 | 3 | `(62,17,1)` |
| 4 | 2 | 2 | 4 | `(69,21,1)` |
| 5 | 1 | 1 | 0 | `(70,25,5)` |
| 6 | 1 | 1 | 0 | `(77,30,5)` |

### Side five

| `Z` | Pareto | active | terminal from `H` | terminal triple |
|---:|---:|---:|---:|---:|
| 8 | 3 | 3 | 4 | `(163,55,4)` |
| 9 | 3 | 3 | 3 | `(163,55,5)` |
| 10 | 7 | 4 | 3 | `(174,64,3)` |
| 11 | 3 | 3 | 1 | `(178,70,7)` |
| 12 | 9 | 6 | 4 | `(181,66,5)` |
| 13 | 4 | 3 | 4 | `(185,72,5)` |
| 14 | 4 | 3 | 3 | `(189,77,7)` |
| 15 | 4 | 3 | 16 | `(191,74,5)` |
| 16 | 3 | 2 | 1 | `(194,84,9)` |
| 17 | 2 | 2 | 6 | `(195,81,9)` |
| 18 | 4 | 3 | 3 | `(198,83,7)` |
| 19 | 2 | 2 | 8 | `(200,86,10)` |
| 20 | 3 | 2 | 1 | `(203,91,10)` |
| 22 | 2 | 2 | 9 | `(205,87,7)` |
| 24 | 1 | 1 | 0 | `(201,84,7)` |
| 25 | 2 | 2 | 1 | `(212,97,11)` |
| 26 | 1 | 1 | 0 | `(212,97,11)` |
| 33 | 1 | 1 | 0 | `(220,104,12)` |

In particular every side-four envelope stabilizes by `H=4`, and every side-five
envelope stabilizes by `H=16`.

### Proof

Evaluate the finitely many quadratic integer scores `F_H` until a candidate
terminal triple dominates every competitor and its one-step score difference is
nonnegative.  If `w` is the candidate and `v` a competitor, then

\[
(F_{H+1}(w)-F_{H+1}(v))-(F_H(w)-F_H(v))
=
H(w_1-v_1)+(w_2-v_2).
\]

When `w_1>=v_1` and the displayed increment is nonnegative at the claimed
terminal height, it remains nonnegative thereafter.  The verifier checks minimality
of every terminal height and records every integer-height maximizer before it. ∎

### Corollary CMR1858 -- PROVED

For a uniform background-height class, exact worst-host testing through side five
needs only the 57 height-active triples.  For `H>=16`, it needs only one terminal
triple per denominator, namely 24 triples in total.

This compression is valid only for the stated moment upper score.  It does not
identify exact geometric rows with different line, owner or provenance labels.

## 4. Line-length-stratified moments

For each grid-line length `L`, define

\[
M_{r,L}(G)
=
\sum_{\ell:\,|\ell\cap\Omega_d|=L}
\binom{\tau_G(\ell)}r.
\]

### Theorem CMR1859 -- PROVED

Suppose every relevant background line of grid length `L` has load at most `H_L`.
Then

\[
\boxed{
\mathcal C_G(B)
\le
\sum_L
\left[
 \binom{H_L}{2}M_{1,L}(G)
 +H_LM_{2,L}(G)
 +M_{3,L}(G)
\right].
}
\]

### Proof

Apply the linewise monotone bound of CMR1815 with `h_ell<=H_L` on every line of
length `L`, then group by line length. ∎

This separates the completed diagonal/full-length data from the remaining shorter
lines.

### Theorem CMR1860 -- PROVED

Under componentwise dominance of the complete length-stratified signature

\[
(M_{r,L})_{r=1,2,3;\,L},
\]

the denominator-preserving raw host tables compress to:

| side | raw hosts | unique Pareto length-stratified signatures |
|---:|---:|---:|
| 4 | 86 | 20 |
| 5 | 654 | 225 |

Thus background classes described only by line-length height caps require at most
245 exact denominator-preserving host signatures through side five.

The per-denominator signature counts are:

### Side four

| `Z` | 1 | 2 | 3 | 4 | 5 | 6 |
|---:|---:|---:|---:|---:|---:|---:|
| signatures | 3 | 8 | 4 | 2 | 2 | 1 |

### Side five

| `Z` | 8 | 9 | 10 | 11 | 12 | 13 | 14 | 15 | 16 | 17 | 18 | 19 | 20 | 22 | 24 | 25 | 26 | 33 |
|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| signatures | 14 | 9 | 36 | 13 | 40 | 16 | 21 | 17 | 18 | 8 | 9 | 4 | 8 | 5 | 1 | 3 | 2 | 1 |

### Proof

Compute the three moments separately on every line-length class, group raw hosts
by exact denominator, and retain the componentwise maximal distinct signatures. ∎

## 5. Pareto-envelope endpoint

### Corollary CMR1861 -- PROVED

The shorter-line host-only frontier through side five now has three exact levels of
compression.

1. The complete embedded table has 740 raw hosts and 89,664 host-line capacities.
2. Uniform background-height classes need 69 Pareto moment triples, of which only
   57 are active for an integer height.
3. Every uniform-height envelope is terminal by `H=16`.
4. Line-length-dependent height classes need 245 Pareto signatures.
5. Exact marginal, nested-assignment and provenance-labelled rows may replace these
   upper signatures whenever they are sharper.
6. None of these compressions merges owner, collision, local-line, interface or CRT
   states in the final exact quotient.

No all-`n` conclusion is claimed.  The remaining use is to attach the actual
background-height and provenance classes to these finite envelope tables.

All raw-host enumerations, Pareto reductions, active-height phases, terminal
certificates and length-stratified signatures are checked in
[`scripts/verify_prime_power_geometric_fibre_moment_pareto_envelopes.py`](../scripts/verify_prime_power_geometric_fibre_moment_pareto_envelopes.py).
