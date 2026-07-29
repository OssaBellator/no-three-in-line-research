# Quantized cycle mixtures for marker flows

`docs/501` realizes a rational stationary marker flow by one Euler circuit.  A
controller selected from a real or high-denominator optimization also needs a
finite-period approximation whose error can be read directly from its cycle
mixture.  This chapter gives that approximation when the selected cycles share a
common return state.

Let `C_1,...,C_m` be directed marker cycles based at one state `o`.  Cycle `C_i`
has length `ell_i>=1` and nonnegative rational total observable vector `a_i`.
For a cycle-count mixture `lambda` in the simplex, define

```text
D(lambda)=sum_i lambda_i ell_i,
R(lambda)=sum_i lambda_i a_i / D(lambda).
```

## 1. Largest-remainder cycle quantization

### Theorem PP3ciz -- PROVED / FINITE CYCLE-MIXTURE REALIZATION

For every integer `K>=1`, there are integers `k_i>=0` such that

```text
sum_i k_i=K,
|k_i/K-lambda_i|<1/K
```

for every `i`.  Concatenating `k_i` copies of each based cycle gives one closed
periodic marker walk of length `sum_i k_i ell_i` and exact average vector
`R(k/K)`.

#### Proof

Set `k_i=floor(K lambda_i)` and distribute the remaining units to the largest
fractional parts.  The counts sum to `K`, and every coordinate differs from its
ideal count by less than one.  All cycles begin and end at `o`, so their copies
may be concatenated in any order.  Totals and lengths add, giving exactly the
stated average. ∎

## 2. Exact rational rate error

### Theorem PP3cja -- PROVED / CYCLE-RATIO ERROR CERTIFICATE

Let `p_i=k_i/K`, `D_0=D(lambda)`, and `D_1=D(p)`.  For every coordinate `j`,

```text
|R_j(p)-R_j(lambda)|
 <= [|sum_i (p_i-lambda_i)a_(i,j)| D_0
     + |sum_i lambda_i a_(i,j)| |D_1-D_0|]
    /(D_0 D_1).
```

In particular, the right side is an explicit `O(1/K)` rational certificate
computed from the finite cycle table.

#### Proof

Write the two averages as `N_1/D_1` and `N_0/D_0`.  The identity

```text
N_1/D_1-N_0/D_0
 = [(N_1-N_0)D_0+N_0(D_0-D_1)]/(D_0D_1)
```

followed by the triangle inequality proves the bound.  The largest-remainder
construction makes every mixture-coordinate error less than `1/K`, so both
numerator errors are `O(1/K)`. ∎

## 3. Finite implementation audit

### Theorem PP3cjb -- PROVED / QUANTIZED FLOW-WALK WITNESS

A proposed quantized cycle implementation has a finite exact audit: check the
integer cycle counts, the common base state, the concatenated period length,
every observable total, and the bound in `PP3cja`.  Failure returns one count,
cycle endpoint, total, or rational inequality.

#### Proof

All objects are finite integer or rational data.  The listed checks are exactly
the hypotheses and conclusions of `PP3ciz--PP3cja`. ∎

## 4. Stored exact fixture

The audit `scripts/check_quantized_marker_cycle_mixtures.py` uses three based
cycles of lengths `2,3,4` carrying actions `A,B,C`.  Its target cycle-count
mixture is

```text
(7/20,1/3,19/60),
```

with target action rate `(21/89,30/89,38/89)`.  Denominator `K=17` gives cycle
counts `(6,6,5)`, period `50`, and rate `(6/25,9/25,2/5)`.  Denominator `60`
gives exact counts `(21,20,19)` and exact period `178`.  The script audits every
`K<=120` against the rational error certificate.

## 5. Prime-patching consequence

A marker-flow optimization no longer needs to return an immediately integral
Euler flow.  A finite cycle decomposition can be rounded to a deterministic
periodic controller with explicit rate loss, while rational mixtures become
exact at a finite denominator.
