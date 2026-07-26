# Prime seeds through relative permutations and maximal grid lines

The prime-minus-one seed CSP uses two edge-disjoint permutations and one
constraint for every Euclidean collinear triple.  Two exact reductions make the
remaining global problem smaller and more structured.

First, the two layers are equivalently one permutation `sigma` together with a
fixed-point-free relative permutation `pi`.  The cycles of `pi` are exactly the
alternating components of the saturated row--column incidence graph.  Second,
all triple inequalities on one geometric line are equivalent to one maximal-line
occupancy inequality.

These reductions preserve the full Euclidean problem.  They do not prove that a
feasible pair exists for all sufficiently large primes.

## 1. Relative-permutation normal form

Let `sigma,tau` be permutations of `[n]` and define

```text
pi = sigma^(-1) o tau.
```

Equivalently,

```text
tau = sigma o pi.
```

### Proposition PP3bcv -- PROVED

The two permutation graphs are edge-disjoint if and only if `pi` is a
derangement:

```text
pi(x) != x
```

for every column `x`.  Thus every saturated seed state is represented uniquely
by a pair `(sigma,pi)` with `sigma` a permutation and `pi` a derangement.

#### Proof

The two selected cells in column `x` coincide exactly when

```text
sigma(x)=tau(x)=sigma(pi(x)).
```

Since `sigma` is injective, this is equivalent to `pi(x)=x`.  The formula
`pi=sigma^(-1)o tau` is unique. ∎

## 2. Alternating components are relative cycles

### Proposition PP3bcw -- PROVED

If `pi` has cycle lengths

```text
lambda_1,...,lambda_k,
```

then the bipartite row--column incidence graph of the saturated state has
alternating cycle components of lengths

```text
2 lambda_1,...,2 lambda_k.
```

#### Proof

Starting at column `x`, traverse the `tau` edge to row
`sigma(pi(x))`, then traverse the `sigma` edge backwards to column `pi(x)`.
Two incidence edges therefore apply one step of `pi`.  A `lambda`-cycle of
`pi` gives one alternating incidence cycle of length `2lambda`, and every
incidence component arises this way. ∎

This makes connected saturated seeds equivalent to relative permutations that
are single `n`-cycles.

## 3. Basic symmetry of the relative cycle type

### Proposition PP3bcx -- PROVED

1. Swapping the two permutation layers replaces `pi` by `pi^(-1)`.
2. Transposing the board replaces the relative permutation by a conjugate of
   `pi^(-1)`.

Consequently the partition of `n` into relative cycle lengths is invariant under
layer swap and board transpose.

#### Proof

After layer swap the relative permutation is

```text
tau^(-1) o sigma = pi^(-1).
```

After transpose the layers become `sigma^(-1),tau^(-1)`, whose relative
permutation is

```text
sigma o tau^(-1)
= sigma o pi^(-1) o sigma^(-1).
```

Inverse and conjugacy preserve cycle lengths. ∎

The cycle partition is therefore a useful exact certificate statistic and a
natural way to divide finite searches.

## 4. Maximal-line compression

For a maximal Euclidean line `L` meeting `[n]^2` in at least three grid cells,
write

```text
u(L)=|S cap L|.
```

### Proposition PP3bcy -- PROVED

A saturated two-permutation state `S` is no-three-in-line if and only if

```text
u(L) <= 2
```

for every maximal grid line `L` containing at least three board cells.

#### Proof

If one maximal line contains three selected cells, those cells form a forbidden
triple.  Conversely every collinear triple lies on one unique maximal line, so
a forbidden triple violates its line inequality. ∎

One maximal-line inequality replaces all triple inequalities supported on that
line.

## 5. Exact primitive-direction enumeration

Choose one orientation for every primitive integer vector

```text
v=(a,b), gcd(|a|,|b|)=1,
a>0 or (a=0 and b>0).
```

For a board cell `z`, call it a start for `v` when `z-v` lies outside the board.

### Proposition PP3bcz -- PROVED

The sets

```text
L(z,v)={z+kv in [n]^2 : k>=0}
```

with `z` a start and `|L(z,v)|>=3` enumerate every maximal grid line exactly
once.

#### Proof

Any line through two integer grid points has a unique primitive direction up to
sign.  The orientation rule chooses one sign.  Moving backwards along that
primitive direction from any point of the line reaches a unique first board
cell `z`; this is the unique start.  Advancing from `z` lists every board point
on the maximal line. ∎

Thus the compressed constraints can be generated without enumerating board-cell
triples.

## 6. Fixed-relative-permutation CSP

Fix one derangement `pi` of `[n]`.  Introduce binary variables

```text
y_(x,r)=1 iff sigma(x)=r.
```

### Theorem PP3bda -- PROVED

For fixed `pi`, seed feasibility is equivalent to the following one-permutation
CSP.

1. `y` is a permutation matrix.
2. For every maximal grid line `L`,

   ```text
   sum_((x,r) in L) [y_(x,r)+y_(pi(x),r)] <= 2.
   ```

A feasible `y` decodes as

```text
sigma(x)=r where y_(x,r)=1,
tau(x)=sigma(pi(x)).
```

The unrestricted prime-minus-one seed problem is feasible exactly when this
fixed-`pi` CSP is feasible for at least one derangement `pi`.

#### Proof

For a fixed cell `(x,r)`, the first layer selects it when `y_(x,r)=1`; the
second layer selects it when

```text
tau(x)=r
iff sigma(pi(x))=r
iff y_(pi(x),r)=1.
```

Because `pi(x)!=x` and `sigma` is a permutation, the two terms cannot both be
one.  Summing them over `L` gives the occupancy `u(L)`.  Apply PP3bcy and the
relative normal form PP3bcv. ∎

For a selected cycle type, finite search may enumerate relative derangements of
that type and solve only one permutation matrix at a time.

## 7. Affine permutation layers cannot be seeds

### Proposition PP3bdb -- PROVED

Let `n>=3`.  If a real affine map

```text
f(x)=ax+b
```

permutes `[n]`, then `f` is either

```text
f(x)=x
```

or

```text
f(x)=n+1-x.
```

Its permutation graph contains `n` collinear points.  Therefore neither layer of
a no-three seed on `[n]^2` can be an affine permutation graph.

#### Proof

An affine bijection of the ordered finite interval is monotone.  If increasing,
it sends the minimum and maximum to themselves, forcing `a=1,b=0`.  If
decreasing, it swaps the endpoints, forcing `a=-1,b=n+1`.  In both cases the
entire graph lies on one line, which contains at least three selected points
when `n>=3`. ∎

In particular, a modular affine-plane construction does not become a Euclidean
prime-minus-one seed merely by restricting its coordinates to integer
representatives.  A successful permutation layer must be genuinely nonlinear
in the Euclidean grid.

## 8. Stored relative cycle types

### Proposition PP3bdc -- VERIFIED FINITELY

The stored exact seed certificates have relative cycle partitions:

```text
p=3:  [2]
p=5:  [2,2]
p=7:  [6]
p=11: [10]
p=13: [4,4,2,2].
```

Thus the `p=7` and `p=11` examples have connected alternating incidence graphs,
while the `p=5` and `p=13` examples have multiple alternating components.

#### Verification

Run the diagnostic below.  It reconstructs `pi`, verifies that it is a
derangement, computes its cycles, and checks every compressed maximal-line
constraint.  The `p=13` certificate checks `898` maximal lines and has maximum
selected occupancy two. ∎

## 9. Revised global seed frontier

### Corollary PP3bdd -- PROVED AS AN EQUIVALENCE

For every prime `p`, with `n=p-1`, prime-minus-one seed feasibility is equivalent
to finding:

1. a derangement `pi` of `[n]`; and
2. a permutation matrix `y` satisfying the maximal-line system of PP3bda.

The remaining asymptotic theorem is that such a pair exists for every
sufficiently large prime.  The relative-cycle and line-compression reductions do
not prove that theorem.  The no-three-in-line conjecture remains unproved.

## 10. Finite diagnostic

Run

```bash
python scripts/check_prime_seed_relative_cycles.py \
  experiments/prime-seed-relative-cycle-example.json
```

The checker computes the relative derangement, relative cycle lengths,
alternating incidence-component lengths, exact reconstruction of `tau`, the
number of maximal grid lines with at least three cells, maximum selected
occupancy on one such line, and whether the compressed line system is
satisfied.
