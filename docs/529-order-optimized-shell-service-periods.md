# Order-optimized shell service periods

`docs/523` chooses the best cyclic phase of a fixed shell period. The service
multiset itself may have many different cyclic orders. This chapter optimizes
the order and returns the minimum startup reserve before repetition begins.

A period contains `m_j` copies of coordinate service action `e_j`, with total
length `p=sum_j m_j` and target rate `r_j=m_j/p`. For a period word `sigma`, let
`N_j(t)` be the number of `j`-services in its first `t` slots.

## 1. Exact startup buffer for one word

### Theorem PP3cln -- PROVED / PERIOD-WORD DEFICIT FORMULA

The componentwise minimum startup buffer making every prefix feasible is

```text
b_j(sigma)=max_(0<=t<=p) (t r_j-N_j(t)).
```

The same buffer makes every prefix of the infinitely repeated word feasible.

#### Proof

At prefix `t`, the account is `b_j+N_j(t)-tr_j`, so the displayed maximum is
necessary and sufficient during the first period. A complete period has zero
net drift in every coordinate. Every later prefix is therefore a full number
of zero-drift periods plus one certified first-period prefix. ∎

## 2. Exact order optimization

### Theorem PP3clo -- PROVED / MULTISET BUFFER DYNAMIC PROGRAM

The Pareto set of attainable startup buffers is computable by a finite dynamic
program on used multiplicity vectors. At state `n=(n_1,...,n_d)`, the current
deficit is

```text
Delta(n)=|n| r-n.
```

Appending one action updates a predecessor buffer by componentwise maximum with
`Delta(n)`. Pareto pruning at each multiplicity state is exact, and stored
predecessors reconstruct every optimal word.

#### Proof

The current deficit depends only on the used multiplicities, while the largest
deficit seen so far is the componentwise maximum accumulated along the path.
Future continuations add the same deficit increments to states with the same
multiplicity vector, so componentwise dominance is preserved and pruning is
safe. ∎

## 3. All-length overhead certificate

### Theorem PP3clp -- PROVED / OPTIMAL PERIODIC SHELL RESERVE

For any nonnegative reserve-price vector `c`, minimizing `c dot b(sigma)` over
the finite Pareto set gives the exact least startup cost among all orders of the
service multiset. Repeating an optimal word for `N` slots has average reserve
overhead `(c dot b)/N`, and exhaustive lower layers of the dynamic program
certify optimality.

#### Proof

`PP3cln` identifies the exact reserve of each word, and `PP3clo` enumerates its
undominated possibilities. The reserve is paid once, so division by the
execution length gives the average overhead. ∎

## 4. Stored exact fixture

The audit `scripts/check_order_optimized_shell_periods.py` orders the multiset

```text
A,A,B,B,C
```

with target `(2/5,2/5,1/5)`. All 30 distinct period words are checked. The
minimum `l_1` startup buffer is `6/5`, attained by ten words. The
lexicographically first optimum is

```text
ABABC
```

with buffer `(0,2/5,4/5)`. Repetition is verified through 200 prefixes.

## 5. Prime-patching consequence

Shell startup loss is now optimized over the entire period design rather than
accepted from an arbitrary word or phase. The result is a finite exact reserve
certificate with `O(1/N)` average cost.
