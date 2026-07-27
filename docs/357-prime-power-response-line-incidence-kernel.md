# Exact line-incidence kernel for every side-four/five response

The canonical raw-host catalogue contains 9,260 response occurrences. This chapter
precomputes the exact affine-line geometry of every one of them. The resulting kernel
is the reusable bridge from a raw response permutation to arbitrary background
rank-two and rank-three witness counts.

For a response `Q`, let

\[
\mathcal L(Q)=\{L:|Q\cap L|\ge2\},
\qquad r_Q(L)=|Q\cap L|.
\]

Every line is stored in primitive normalized integer form `ax+by+c=0`.

## 1. Canonical response-line records

### Theorem CMR2030 -- PROVED

Every unordered response pair determines exactly one normalized line. Grouping equal
lines yields a unique ordered record containing

\[
L,\quad r_Q(L),\quad\binom{r_Q(L)}2,\quad\binom{r_Q(L)}3.
\]

### Proof

Two distinct integer points determine one affine line. Divide the integer coefficient
triple by its gcd and fix the sign by the first nonzero coefficient. This gives one
canonical representative. Grouping pair supports by this representative is unique. ∎

## 2. Exact rank-two kernel

For a background `B`, put `h_B(L)=|B\cap L|`.

### Theorem CMR2031 -- PROVED

The number of post-response triples with exactly two response points is

\[
\boxed{
W_2(Q;B)=\sum_{L\in\mathcal L(Q)}\binom{r_Q(L)}2h_B(L).
}
\]

### Proof

A rank-two triple is one response pair and one background point on the pair's line.
A line containing `r` response points contributes one triple for each of its
`binom(r,2)` response pairs and each of its `h_B(L)` background points. Distinct
response pairs determine their unique line, so there is no double counting. ∎

## 3. Exact rank-three kernel

### Theorem CMR2032 -- PROVED

The literal rank-three response count is

\[
\boxed{
W_3(Q)=\sum_{L\in\mathcal L(Q)}\binom{r_Q(L)}3.
}
\]

### Proof

Every collinear response triple lies on one unique line. A line containing `r`
response points contributes exactly `binom(r,3)` triples. ∎

## 4. Rank-one point kernel

For a response point `q`, let `p_B(q)` be the number of unordered background pairs
collinear with `q`.

### Theorem CMR2033 -- PROVED

The rank-one count is

\[
\boxed{W_1(Q;B)=\sum_{q\in Q}p_B(q).}
\]

Thus the response points together with the line kernel determine all three primitive
ranks for every supplied background.

### Proof

A rank-one triple has a unique response point and a unique unordered background pair.
Sum the pair count over response points. ∎

## 5. Complete kernel census

### Theorem CMR2034 -- PROVED

Across all 740 hosts the kernel contains

\[
\boxed{9,260\text{ responses and }79,736\text{ line records}.}
\]

The sum of all rank-three response occurrences is 6,485. There are 39 distinct
coordinate-labelled response geometries.

The maximum line-occupancy distribution is

\[
\boxed{[[2,4253],[3,4697],[4,310]].}
\]

### Proof

Reconstruct every response from the canonical catalogue, build its normalized line
records, and sum the stored multiplicities. The rank-three sum agrees independently
with the catalogue numerator total. ∎

## 6. Seven exact occupancy profiles

### Theorem CMR2035 -- PROVED

Only seven line-occupancy profiles occur:

| side | sorted occupancies `r_Q(L)` | response occurrences |
|---:|---|---:|
| 4 | `2,2,2,2,2,2` | 137 |
| 4 | `2,2,2,3` | 34 |
| 4 | `4` | 35 |
| 5 | `2,2,2,2,2,2,2,2,2,2` | 4,116 |
| 5 | `2,2,2,2,2,2,2,3` | 4,115 |
| 5 | `2,2,2,2,3,3` | 548 |
| 5 | `2,2,2,2,4` | 275 |

### Proof

Sort the occupancies in every canonical response-line record and tabulate. The counts
sum to 9,260. ∎

## 7. Exact background response score

Define

\[
N_B(Q)=W_1(Q;B)+W_2(Q;B)+W_3(Q).
\]

### Theorem CMR2036 -- PROVED

For every canonical response and every finite background disjoint from the response
grid, the point list and line-incidence kernel compute `N_B(Q)` exactly. No geometric
upper bound or matching average is used.

### Proof

Apply CMR2031--CMR2033 and add the three disjoint response-rank classes. ∎

## 8. Executable endpoint

### Corollary CMR2037 -- PROVED

`scripts/check_prime_power_response_line_incidence_kernel.py` builds and validates the
complete kernel, verifies the rank-three total against the canonical catalogue, and
provides the exact rank-two evaluator used by downstream background selectors.

The fixed kernel digest is

\[
\texttt{b591356b800b44ae1a20c9f57cdad0782aecc43ca0a2ee699c4c0337d3010697}.
\]

The built-in mutation suite rejects ten independently corrupted kernels.
