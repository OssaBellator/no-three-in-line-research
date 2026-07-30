# Cyclic discrepancy of threshold permutation layers

`docs/527` orders a finite set of collision-free threshold layers to control
prefix loads from one chosen starting phase. Repeated use also requires control
from every cyclic phase and over every contiguous time window. The correct
finite invariant is the coordinate diameter of the cyclic prefix path.

After quotienting additive source-plus-action potentials, let layer `i` have a
rational resource vector `z_i` and assume `sum_i z_i=0`.

## 1. Prefix-range identity

### Theorem PP3clz -- PROVED / CYCLIC WINDOW DISCREPANCY

For a cyclic order `sigma`, define

```text
p_0=0,
p_k=sum_(t<k) z_(sigma(t)).
```

The largest absolute discrepancy in coordinate `j` over every contiguous
subword of the cyclic period is exactly

```text
max_k p_k(j)-min_k p_k(j).
```

Hence the worst `l_infinity` cyclic-window discrepancy is the maximum coordinate
range of the prefix path.

#### Proof

Every cyclic interval sum is a difference of two prefix vectors; an interval
crossing the period boundary uses the zero total sum to obtain the same form.
The largest possible difference in one coordinate is its maximum prefix minus
its minimum prefix, and both extrema define an interval attaining it. ∎

## 2. Exact cyclic sequencing oracle

### Theorem PP3cma -- PROVED / FINITE CYCLIC LAYER OPTIMIZATION

The minimum cyclic-window discrepancy is an exact finite optimization problem.
Enumeration over permutations, or a subset dynamic program storing current
prefix, coordinate minima, and coordinate maxima, returns an optimal cyclic
order and a matching lower certificate. Orders differing only by rotation may
be quotient-canonicalized.

#### Proof

There are finitely many layer orders, and `PP3clz` evaluates each by rational
arithmetic. The subset state contains all information needed when one layer is
appended. Exhaustion proves optimality; canonical rotation removes only copies
of the same cycle. ∎

## 3. Repeated all-window execution

### Theorem PP3cmb -- PROVED / PERIODIC THRESHOLD WINDOW CERTIFICATE

Repeating an optimal zero-sum cyclic order preserves the same discrepancy bound
for every contiguous interval of arbitrary length. Full periods contribute
zero, and the remaining interval is contained in one cyclic period. The stored
order therefore gives a phase-independent transient certificate.

#### Proof

Delete all complete periods from an interval. The residual sum is a cyclic
subword sum, bounded by `PP3clz`. ∎

## 4. Stored exact fixture

The audit `scripts/check_cyclic_threshold_layer_discrepancy.py` uses six quotient
vectors

```text
A=(2,0), B=(-2,0), C=(0,-2),
D=(1,2), E=(1,-1), F=(-2,1).
```

Among all `720` linear orders, exactly `48` attain minimum cyclic
`l_infinity` discrepancy two. They form eight cyclic rotation classes. The
lexicographically first optimum is `ABCDEF`, whose prefix path is

```text
(0,0),(2,0),(0,0),(0,-2),(1,0),(2,-1),(0,0).
```

The audit also checks every window of length at most sixty in fifty repeated
periods.

## 5. Prime-patching consequence

Collision-free threshold layers now have a phase-independent implementation.
No geometric subinterval sees more resource drift than the exact finite cyclic
prefix-range certificate.
