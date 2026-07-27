# Edge-disjoint swapped-quarter-turn states retain a logarithmic first-moment barrier

The signed orbit model removes duplicate orbit blocks at only constant-factor
cost by PP3bfp.  It is therefore natural to ask whether a uniformly random
*edge-disjoint* signed permutation might already have a small enough line
defect for a direct first-moment proof.

It does not.  Even after conditioning on edge-disjointness, one permutation
layer alone contains `Theta(n log n)` expected generic collinear triples.  Thus
the quarter-turn reduction compresses the state space but does not make the
uniform measure first-moment feasible.

This is a barrier for one natural probability measure.  Nonuniform signed
cycle covers, correlated cycle-parity choices, stronger local-lemma methods,
and constructive repair remain possible.

## 1. Generic collinear triples

Write `n=2m`.  A board coordinate belongs to one reversal pair under

```text
J(x)=n-1-x.
```

Call a nonaxis collinear triple of board cells *generic* when:

1. its three columns lie in distinct reversal pairs;
2. its three rows lie in distinct reversal pairs; and
3. the three induced source-pair to target-pair assignments contain no directed
   two-cycle.

### Proposition PP3bga -- PROVED

The number `G_n` of generic nonaxis collinear triples satisfies

```text
G_n=Theta(n^4 log n).
```

#### Proof

The total number of nonaxis collinear triples is `Theta(n^4 log n)` by
PP3bdg.

Triples with two columns in one reversal pair are `O(n^4)`: choose which two
points form the pair, their reversal-paired columns, their two rows, and the
third column; collinearity determines the third row at most once.  The same
bound applies to two rows in one reversal pair.

For a directed pair-level two-cycle, choose the two pair indices and the finite
coordinate bits specifying the first two cells, then choose the third column;
again collinearity determines its row at most once.  This contributes only
`O(n^3)` triples.

Removing these exceptional families leaves

```text
Theta(n^4 log n)-O(n^4)=Theta(n^4 log n).
```

∎

## 2. Uniform edge-disjoint signed states

Choose uniformly from all ordered signed permutations `(rho,e)` whose forced
swapped layers are edge-disjoint.  Their number is `D_m` from PP3bfp, with

```text
D_m/(2^m m!) -> exp(-1/4).
```

Fix one generic triple `T` and ask that all three cells lie in the first layer
`P_sigma`.

### Proposition PP3bgb -- PROVED

For all sufficiently large `m`, uniformly over generic triples `T`,

```text
1/[32(m)_3]
<= Pr(T subset P_sigma)
<= 1/[4(m)_3].
```

In particular,

```text
Pr(T subset P_sigma)=Theta(m^(-3)).
```

#### Proof

The generic conditions make the three source pair indices distinct, the three
target pair indices distinct, and the prescribed signed edges free of a fixed
directed two-cycle.  Thus the event fixes exactly three signed pair assignments.

There are at most

```text
2^(m-3)(m-3)!
```

completions before edge-disjointness is imposed.

For a lower bound, choose a uniformly random bijection between the remaining
`m-3` sources and targets.  Let `Z` count:

1. directed two-cycles entirely among the remaining vertices; and
2. reverse edges completing a two-cycle with one of the three fixed edges.

The expected number of internal two-cycles is at most `1/2`.  Each fixed edge
creates at most one reverse-edge event, of probability `1/(m-3)`.  Hence

```text
E Z <= 1/2 + 3/(m-3).
```

For all sufficiently large `m`, this is at most `3/4`.  Markov's inequality
gives

```text
Pr(Z=0)>=1/4.
```

When `Z=0`, the pair permutation has no two-cycle involving a remaining edge,
so every choice of the remaining orientation bits is edge-disjoint.  Therefore
the triple event has at least

```text
(1/4) 2^(m-3)(m-3)!
```

valid completions.

Use `D_m<=2^m m!` for the lower probability bound.  By PP3bfp, for all
sufficiently large `m` one also has `D_m>=(1/2)2^m m!`; use this with the crude
completion upper bound for the upper probability bound. ∎

The constants are intentionally elementary.  Their exact values are not
important; the uniform `m^(-3)` scale is.

## 3. Expected same-layer defects

Let `Y_m` be the number of generic collinear triples contained in the first
permutation layer of a uniformly random edge-disjoint swapped state.

### Theorem PP3bgc -- PROVED

Uniformly for the edge-disjoint swapped measure,

```text
E Y_m=Theta(n log n).
```

Consequently the expected number of forbidden triples in the full two-layer
state is at least `Omega(n log n)`.

#### Proof

Sum the cylinder probabilities of PP3bgb over the `G_n` generic triples from
PP3bga.  Since `m=n/2`,

```text
G_n/(m)_3
=Theta(n^4 log n / n^3)
=Theta(n log n).
```

Every first-layer collinear triple remains selected in the full union, so the
full defect count dominates `Y_m`. ∎

### Corollary PP3bgd -- PROVED

The direct unconditioned first-moment argument cannot establish existence in
the uniform edge-disjoint swapped-quarter-turn model.

#### Proof

A first-moment existence proof based on the total number of bad triples would
require expectation below one.  PP3bgc gives expectation growing at least as a
positive constant times `n log n`. ∎

This does not imply that a typical state is far from repair, nor does it rule
out a weighted measure designed to suppress the generic cylinders.

## 4. Exhaustive finite diagnostic

### Proposition PP3bge -- VERIFIED FINITELY

Exhaustive enumeration of every ordered edge-disjoint signed permutation for
`2<=m<=6` checks `39,222` states and `8,271,144` exact first-layer determinants.
The exact mean numbers of collinear triples in `P_sigma` are:

| `m` | `n` | edge-disjoint states | exact mean | decimal mean |
|---:|---:|---:|---:|---:|
| 2 | 4 | 6 | `4/3` | 1.333333 |
| 3 | 6 | 36 | `20/9` | 2.222222 |
| 4 | 8 | 300 | `74/25` | 2.960000 |
| 5 | 10 | 3,000 | `1354/375` | 3.610667 |
| 6 | 12 | 35,880 | `21131/4485` | 4.711483 |

#### Verification

Run

```bash
python scripts/check_swapped_edge_disjoint_first_moment.py \
  experiments/swapped-edge-disjoint-first-moment-example.json
```

For each state the checker constructs `sigma`, tests every triple of its `2m`
points by an exact integer determinant, and verifies the state count against
the coefficient of `exp(-z^2)/(1-2z)`. ∎

## 5. Revised probabilistic frontier

### Corollary PP3bgf -- PROVED / FINITE DIAGNOSTIC RECORDED

The two most direct uniform probabilistic routes are now blocked at both levels:

1. unrestricted fixed-relative permutations have `Theta(n log n)` expected bad
   triples by PP3bdh; and
2. edge-disjoint swapped-quarter-turn signed permutations retain
   `Theta(n log n)` expected generic first-layer triples by PP3bgc.

A probabilistic proof inside the orbit CSP must therefore bias the signed cycle
cover toward geometrically sparse line profiles, use a stronger dependency or
cluster criterion, or combine sampling with a distributed repair mechanism.

The signed-orbit asymptotic theorem, the unrestricted prime-minus-one seed
theorem, and the no-three-in-line conjecture remain unproved.
