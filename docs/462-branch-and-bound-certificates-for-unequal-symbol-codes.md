# Branch-and-bound certificates for unequal-symbol codes

`docs/450` gives an exact `O(3^K)` subset dynamic program for unequal symbol
survivals, and `docs/456` adds a generalized Kraft lower bound.  This chapter
turns that lower bound into a checkable branch-and-bound proof of optimality.

For a bank subset `S`, let `V(S)` denote the optimal subtree risk and let `L(S)`
be any certified lower bound, such as

```text
L(S)=(sum_(i in S) rho_i^theta)^(1/theta),
p_0^theta+p_1^theta=1.
```

## 1. Split pruning

### Theorem PP3cdu -- PROVED / SAFE SPLIT LOWER BOUND

For a proposed split `S=A disjoint_union B`, every orientation has risk at least

```text
min(max(L(A)/p_0,L(B)/p_1),
    max(L(A)/p_1,L(B)/p_0)).
```

If this quantity is at least the best complete risk already found for `S`, the
split may be discarded without changing `V(S)`.

#### Proof

Replace the unknown exact child values in the subset recurrence by their lower
bounds.  Monotonicity of division and maximum gives a lower bound for each
orientation.  A split whose lower bound is no better than the incumbent cannot
improve it. ∎

## 2. Finite optimality certificate

### Theorem PP3cdv -- PROVED / BRANCH-AND-BOUND PROOF TREE

An exact optimality certificate consists of, for every visited subset:

1. one evaluated split attaining its recorded value, and
2. for every unevaluated split, a lower-bound value at least that recorded
   incumbent.

Checking these inequalities bottom-up proves the root value exactly.

#### Proof

Induct on subset size.  Singleton values are exact.  At a larger subset, the
attaining split supplies an upper bound equal to the recorded value.  Every
other split is either evaluated and no smaller, or pruned by a certified lower
bound no smaller.  Hence the recorded value equals the minimum recurrence. ∎

The certificate records why a split was omitted, rather than merely reporting
that a search program skipped it.

## 3. Exact finite search

### Theorem PP3cdw -- PROVED / MEMOIZED PRUNED SUBSET ORACLE

Ordering splits by their certified lower bound, evaluating them recursively, and
memoizing subset values returns the same exact optimum as the full subset
dynamic program.  It visits at most `2^K-1` subset states and examines at most
the full `O(3^K)` collection of unordered splits, while every pruning step is
independently checkable by `PP3cdu`.

#### Proof

`PP3cdu` preserves the minimum at each state.  Memoization only reuses an
already proved exact subset value.  The finite state and split counts give
termination and the stated worst-case bounds. ∎

## 4. Exact audit

Run

```bash
python scripts/check_branch_and_bound_unequal_codes.py
```

For seven banks and survivals `(1/3,2/3)`, the exact optimum is `27/64`.  The
certificate visits 76 of 127 possible nonempty subsets, evaluates 143 splits,
and safely prunes 236.  A separate full recurrence checks the same optimum over
all 966 subset partitions.
