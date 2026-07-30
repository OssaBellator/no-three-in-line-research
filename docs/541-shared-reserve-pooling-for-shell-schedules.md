# Shared reserve pooling for shell schedules

`docs/535` synchronizes several shell periods and optimizes their phase pair.
When components draw on a common reserve pool, summing their separate startup
buffers can be unnecessarily expensive.  This chapter gives the exact pooled
buffer and a finite phase-sharing oracle.

Component `k` has a zero-sum periodic residual word
`d^(k)_1,...,d^(k)_T` in a common resource space.  A nonnegative pooling map `P`
converts component residuals into shared reserve coordinates.

## 1. Exact pooled startup buffer

### Theorem PP3cmx -- PROVED / SHARED SHELL BUFFER FORMULA

For fixed component phases, define the pooled prefix residual

```text
S_t=P sum_k sum_(s<=t) d^(k)_s.
```

The coordinatewise minimum startup buffer is

```text
b_j=max_t (-S_(t,j))_+.
```

With this buffer every pooled prefix is feasible, and decreasing any positive
coordinate of `b` violates the prefix attaining its minimum.

#### Proof

Feasibility requires `b+S_t>=0` for every `t`, which is equivalent to the stated
coordinatewise inequalities.  Taking their maximum is sufficient and necessary. ∎

## 2. Pooling never costs more than separation

### Theorem PP3cmy -- PROVED / RESERVE-SHARING DOMINATION

Let `b^(k)` be the minimum startup buffer of component `k` before pooling.  Then

```text
b_pool <= sum_k P b^(k)
```

coordinatewise.  The inequality can be strict, including complete cancellation
to zero pooled reserve.

#### Proof

For each coordinate, the minimum of a sum of prefix processes is at least the
sum of their separate minima.  Negating and applying the nonnegative map gives
the inequality. ∎

## 3. Finite phase-torus optimization

### Theorem PP3cmz -- PROVED / SHARED-RESERVE PHASE ORACLE

For finitely many finite periodic components, the Pareto-minimal pooled startup
buffers are obtained by exact enumeration of the finite phase torus.  Storing a
phase tuple and the prefix attaining each active buffer coordinate is a complete
feasibility and optimality certificate.

#### Proof

There are finitely many phase tuples.  `PP3cmx` computes the unique minimal
buffer for each tuple.  Pareto pruning is exact, and the stored minimum-prefix
witness prevents any coordinate reduction. ∎

## 4. Stored exact fixture

The audit `scripts/check_shared_shell_reserves.py` uses two period-three
components

```text
X=((1,-1),(0,0),(-1,1)),
Y=((-1,1),(0,0),(1,-1)).
```

Each component separately needs `l_1` reserve one.  All nine phase pairs are
checked.  Three aligned pairs cancel slot by slot, reducing the pooled startup
reserve from two to zero.  One hundred repeated periods are checked with zero
pooled deficit.

## 5. Prime-patching consequence

Shell components no longer need independent worst-case reserves.  Their phase
choices can be coordinated so that one component's temporary surplus protects
another's deficit, with an exact finite certificate for the shared buffer.
