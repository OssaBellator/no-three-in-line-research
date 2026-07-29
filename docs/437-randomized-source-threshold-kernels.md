# Randomized source-adaptive multiplicity thresholds

`docs/431` permits a different multiplicity threshold at every source.  A
single deterministic threshold assignment need not be optimal.  This chapter
allows each source to randomize among its retained-action kernels and gives an
exact linear-program dual.

## 1. Mixed threshold kernels

For source `x`, let `H_x` be its finite set of admissible thresholds.  Threshold
`h` retains a nonempty target set `N_h(x)` of size `d_h(x)`.  Choose probabilities
`alpha_(x,h)` with

```text
sum_(h in H_x) alpha_(x,h)=1.
```

The resulting kernel is

```text
P(x,y)=sum_(h:y in N_h(x)) alpha_(x,h)/d_h(x).
```

### Theorem PP3cax -- PROVED / EXACT MIXED-THRESHOLD LOAD

The reverse load of the mixed kernel is exactly

```text
lambda(alpha)
 =max_y sum_x sum_(h:y in N_h(x)) alpha_(x,h)/d_h(x).
```

#### Proof

The displayed expression is precisely the column sum of the stochastic kernel
`P`. ∎

## 2. Dual target-price certificate

Let `Delta(Y)` be the probability simplex on targets.  For `z in Delta(Y)`,
define the cheapest expected target price available to source `x` by

```text
c_x(z)=min_(h in H_x)
       [sum_(y in N_h(x)) z_y]/d_h(x).
```

### Theorem PP3cay -- PROVED / MIXED-THRESHOLD MINIMAX DUALITY

The optimal mixed load satisfies

```text
min_alpha lambda(alpha)
 =max_(z in Delta(Y)) sum_x c_x(z).
```

#### Proof

Write the primal linear program with variables `alpha_(x,h)` and `rho`:
minimize `rho`, impose one simplex equality per source, and require every target
column to be at most `rho`.  Its dual chooses nonnegative target prices summing
to one.  Minimizing the priced cost separately over the threshold simplex of
each source gives `c_x(z)`.  Finite-dimensional linear-program duality gives
equality. ∎

A target-price distribution therefore certifies that no randomized threshold
rule can do better.

## 3. Sparse optimal randomization

### Theorem PP3caz -- PROVED / SPARSE MIXED-THRESHOLD SUPPORT

There is an optimal solution using at most

```text
|X|+|Y|-1
```

positive threshold probabilities.  Equivalently, at most `|Y|-1` threshold
choices beyond one per source are needed.

#### Proof

Take an optimal basic feasible solution of the primal program.  There are
`|X|` source equalities and at most `|Y|` active column inequalities.  Including
the positive variable `rho`, at most `|X|+|Y|` basic variables can be positive.
The claimed bound on positive `alpha` variables follows. ∎

Thus randomized stripping remains finitely auditable even when every source has
many candidate thresholds.

## 4. Revised direct-clean frontier

The deterministic threshold search is replaced by an exact primal--dual
certificate.  Success gives a sparse mixed repair kernel; failure gives target
prices showing that every source is forced to spend too much probability on an
overloaded target region.

## 5. Exact diagnostic

Run

```bash
python scripts/check_randomized_source_thresholds.py
```

The stored three-source example has deterministic optimum `5/6` but mixed
optimum `3/5`.  Uniform target prices certify the latter exactly.
