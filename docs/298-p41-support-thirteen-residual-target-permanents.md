# Exact p=41 support-thirteen residual target permanents

The support-thirteen frontier at `p=41` contains `75,140` owner-feasible
supports by PP3bhp.  For a fixed support, PP3bhj identifies target repairs with
derangements.  Before branching over all such derangements, one can test each
possible source-to-old-target edge against the unchanged orbit blocks and the
residual line capacities.

This chapter packages those one-edge tests into a small matrix and computes its
permanent exactly for every owner-feasible support.

The resulting census does not enforce interactions between two changed orbit
blocks.  It is therefore an exact outer relaxation of the repair problem, not a
repair count.

## 1. Residual target matrix

Fix an exact support `A` of size `k`.  Remove the old orbit blocks owned by `A`
and retain every old block outside `A`.  Index both rows and columns by `A`.
For `s,u in A`, let

```text
W_A(s,u)
```

be the number of canonical orientations of the signed edge from source `s` to
the old target `rho(u)` that:

1. do not duplicate any retained orbit block; and
2. individually fit every residual maximal-line capacity.

Set `W_A(s,s)=0`, because exact support forbids the old target assignment.  Let
`M_A` be the binary support matrix of `W_A`.

### Proposition PP3bhx -- PROVED

Every valid repair with support `A` selects a permutation matrix contained in
`M_A`.  Equivalently, its target derangement is counted by

```text
per(M_A).
```

#### Proof

By PP3bhj, a repair target map is a derangement `g_A` and sends source `s` to
`rho(g_A(s))`.  Its chosen orientation must avoid every retained orbit and must
fit the residual line capacities before any other changed block is added.
Therefore `M_A(s,g_A(s))=1` for every source.  Since `g_A` is a permutation, the
selected entries form one permutation matrix contained in `M_A`. ∎

The converse need not hold: two selected changed blocks may duplicate each
other or jointly overload a line.

## 2. Binary and weighted permanents

### Proposition PP3bhy -- PROVED

For a fixed support `A`:

1. `per(M_A)` is exactly the number of target derangements surviving every
   one-edge residual test;
2. `per(W_A)` is exactly the number of target/orientation selections surviving
   every one-edge residual test, with no interaction test between changed
   blocks.

#### Proof

A permanent sums over all permutations of the columns.  The zero diagonal
removes fixed points, so every nonzero term of `per(M_A)` is a derangement.
The product of binary entries is one exactly when all selected target edges
pass the individual test.

For `W_A`, the selected entry contributes the number of individually legal
orientations on that target edge.  Multiplying over sources counts all choices
of one such orientation per selected target edge, and summing over target
permutations gives the claim. ∎

Both permanents can be computed by subset dynamic programming in

```text
O(k 2^k)
```

arithmetic operations.  At `k=13` this is small enough to audit every support.

## 3. Permanent-zero supports

### Corollary PP3bhz -- PROVED

If `per(M_A)=0`, then no repair exists on support `A`.

#### Proof

PP3bhx gives a necessary permutation matrix contained in `M_A`.  A zero
permanent means no such permutation exists. ∎

This is the cycle-first form of the initial Hall obstruction.  It is stronger
than checking that every source has a nonempty domain, because it also detects
collective target shortages.

## 4. Exact all-support p=41 census

### Theorem PP3bia -- VERIFIED FINITELY

For all `75,140` owner-feasible supports of size thirteen in the audited
`p=41` near-state, the exact census is

```text
zero binary permanent                           8
positive binary permanent                  75,132
minimum positive permanent                  6,270
maximum permanent                     779,891,623
total binary permanent              2,356,482,881,132
total weighted permanent          178,613,770,154,696
```

The eight zero-permanent supports are:

```text
{1,2,3,4,5,6,8,9,10,11,13,17,18}
{1,2,3,4,5,7,9,10,13,17,18,19,20}
{1,2,3,4,6,8,9,10,11,13,17,18,19}
{1,2,4,5,6,7,10,12,13,16,18,19,20}
{1,2,4,6,8,9,10,13,14,17,18,19,20}
{1,3,4,5,6,7,8,9,10,11,12,17,18}
{1,3,4,5,6,7,9,10,12,13,14,18,19}
{1,3,4,5,6,9,10,11,13,14,16,18,19}.
```

The minimum positive permanent occurs at

```text
{1,2,4,5,6,8,9,10,14,17,18,19,20},
```

and the maximum at

```text
{1,3,5,6,7,9,11,14,15,16,17,18,19}.
```

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_p41_support13_residual_target_permanents.cpp \
  -o /tmp/check_p41_support13_permanents
/tmp/check_p41_support13_permanents
```

The checker reconstructs all `108190` maximal nonaxis lines, every canonical
signed orbit option, every owner-feasible support, both residual matrices, and
both permanents by exact integer dynamic programming. ∎

## 5. Exact outer-space reduction

The owner-filtered target space has size

```text
75,140 * !13 = 172,130,180,910,480.
```

### Corollary PP3bib -- VERIFIED FINITELY

The exact fraction surviving all one-edge residual target tests is

```text
2,356,482,881,132 / 172,130,180,910,480
= 0.013690120283772545....
```

Thus the binary residual matrix removes a factor

```text
73.0453771969...
```

from the target-derangement outer space.

Using the crude orientation upper bound `2^13` on every target map, the weighted
signed survival fraction is

```text
178,613,770,154,696
/
(172,130,180,910,480 * 2^13)
= 0.00012666830781364404....
```

#### Proof

Substitute the exact totals from PP3bia and the subfactorial count from PP3bhq.
∎

The weighted permanent averages about `75.7968` individually legal orientation
selections per surviving target map.  These selections still require duplicate
checks and joint line-capacity propagation.

## 6. Relation to the sampled diagnostic

The uniform-derangement trial stream PP3bhu observed initial survival fraction

```text
6589/484660 = 0.0135950976....
```

The exact all-support fraction PP3bib is `0.0136901203...`.  Their proximity is
a consistency check on the sampler, not an independence theorem or a bound on
sampling error.

The single-cycle sample is not governed by the full permanent because it
conditions on one cycle type.

## 7. Revised branch-and-cut frontier

### Corollary PP3bic -- PROVED / FINITE CENSUS RECORDED

A complete support-thirteen solver may now use the exact hierarchy

```text
weighted owner-cover support,
zero-permanent rejection,
target derangement inside M_A,
orientation selection inside W_A,
changed-orbit duplicate propagation,
and joint maximal-line capacities.
```

Only eight supports are eliminated outright by the permanent-zero cut, but the
binary matrices remove more than `98.63%` of target derangements in aggregate.
The main unresolved work is therefore not support selection; it is structured
enumeration of the remaining `2.356` trillion target maps together with their
changed-block interactions.

No support-thirteen repair is claimed.  The `p=41` seed, the asymptotic
prime-minus-one seed theorem, and the no-three-in-line conjecture remain open.
