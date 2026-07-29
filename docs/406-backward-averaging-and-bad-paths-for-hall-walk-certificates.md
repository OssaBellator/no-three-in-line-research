# Backward averaging and bad paths for Hall walk certificates

`docs/400` defines the canonical overlap-walk potentials

```text
a_(t+1)=K a_t
```

and the decreasing Collatz ratios

```text
c_t=max_x a_(t+1)(x)/a_t(x).
```

This chapter identifies the exact local recursion behind that monotonicity.
Every depth ratio is a convex average of the preceding-depth ratios.  Failed
Hall certificates therefore propagate backwards along an actual overlap path,
and quantitative failure places positive walk mass on raw-congestion sources.

The statements are general.  They do not classify the resulting paths in the
prime-patching overlap graph.

## 1. Exact ratio averaging

Retain the nonnegative normalized overlap matrix `K`, with positive diagonal,
and put

```text
r_t(x)=a_(t+1)(x)/a_t(x).
```

For `t>=1`, define

```text
pi_t(x,x')
 =K(x,x') a_(t-1)(x')/a_t(x).
```

### Theorem PP3bxg -- PROVED / BACKWARD COLLATZ AVERAGING

For every `x` and `t>=1`, the coefficients `pi_t(x,x')` form a probability
distribution on the overlap neighbours of `x`, and

```text
r_t(x)=sum_(x') pi_t(x,x') r_(t-1)(x').
```

Consequently

```text
min_(x':K(x,x')>0) r_(t-1)(x')
 <=r_t(x)
 <=max_(x':K(x,x')>0) r_(t-1)(x').
```

#### Proof

The denominator satisfies

```text
a_t(x)=sum_(x') K(x,x')a_(t-1)(x'),
```

so the `pi_t` are nonnegative and sum to one.  Moreover

```text
r_t(x)
 =a_(t+1)(x)/a_t(x)
 =[sum_(x')K(x,x')a_t(x')]/a_t(x)
 =sum_(x')
   [K(x,x')a_(t-1)(x')/a_t(x)]
   [a_t(x')/a_(t-1)(x')].
```

The second bracket is `r_(t-1)(x')`, proving the identity and the interval
bound. ∎

This gives a local explanation of `c_t<=c_(t-1)`: each new ratio lies in the
convex hull of neighbouring old ratios.

## 2. Bad-path extraction

### Theorem PP3bxh -- PROVED / NESTED OVERLAP-PATH WITNESS

Fix `C`.  If some depth-`t` ratio satisfies

```text
r_t(x_t)>C,
```

then there is an overlap path

```text
x_t,x_(t-1),...,x_0
```

with

```text
K(x_i,x_(i-1))>0
```

and

```text
r_i(x_i)>C
```

for every `0<=i<=t`.

In particular, failure of `c_t<=C` forces a length-`t` path ending at a source
whose raw average target multiplicity obeys

```text
r_0(x_0)>C.
```

#### Proof

By `PP3bxg`, `r_t(x_t)` is an average of the values
`r_(t-1)(x')` over overlap neighbours.  If the average exceeds `C`, at least
one positively weighted neighbour `x_(t-1)` has value exceeding `C`.
Iterate until depth zero. ∎

Thus a persistent finite-depth obstruction is not an arbitrary rooted tree:
it contains a nested chain of bad sources.

## 3. Quantitative endpoint localization

Start at a root `Z_t=x`.  For `i=t,t-1,...,1`, move from `Z_i` to `Z_(i-1)`
using the transition probabilities `pi_i(Z_i,.)`.

### Theorem PP3bxi -- PROVED / RAW-CONGESTION ENDPOINT MASS

The induced inhomogeneous backward walk satisfies

```text
r_t(x)=E_x[r_0(Z_0)].
```

Let

```text
M=max_z r_0(z)
```

and fix `theta<C<=M`.  If `r_t(x)>=C`, then

```text
P_x(r_0(Z_0)>theta)
 >=(C-theta)/(M-theta).
```

Moreover, if `r_t(x)=M`, then every backward path of positive probability ends
at a source with `r_0=M`.  If the overlap graph is connected and
`t` is at least its diameter, then every source has raw ratio `M`.

#### Proof

Iterating the averaging identity in `PP3bxg` gives the expectation formula.
Let

```text
p=P_x(r_0(Z_0)>theta).
```

Since `r_0<=theta` off that event and `r_0<=M` everywhere,

```text
C<=E[r_0(Z_0)]
  <=theta(1-p)+Mp.
```

Rearrangement gives the probability bound.

If the expectation equals the global maximum `M`, every endpoint of positive
probability must itself have value `M`.  Positive diagonals and positive
overlap edges make every path of length at most the diameter reachable after
padding with diagonal steps, yielding the final statement. ∎

Near-maximal depth congestion therefore places a definite fraction of the
backward walk on the raw high-multiplicity set.  Exact non-improvement forces
a flat congestion plateau rather than a hidden spectral phenomenon.

## 4. Revised Hall frontier

A failed depth certificate now returns two increasingly concrete objects:

1. a nested overlap path all of whose level-matched ratios exceed the proposed
   bound;
2. a quantitative endpoint distribution supported substantially on sources
   with large raw average target multiplicity.

The next geometric audit can classify raw-congestion sources and the overlap
paths feeding them, rather than arbitrary Perron vectors.

## 5. Finite diagnostic

The script

```bash
python scripts/check_overlap_walk_backward_averaging.py
```

uses exact rational arithmetic to verify the convex recursion, enumerate all
positive-probability backward paths through depth six, and check the endpoint
expectation and threshold-mass bound.

The next theorem identifier after this chapter is `PP3bxj`.
