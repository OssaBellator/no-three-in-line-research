# Walsh acceleration for binary Hall syndromes

`docs/490` and `docs/496` compute Hall-color lists by syndrome dynamic
programming and sparse half joins.  When many binary marker blocks repeat, the
remaining operation is convolution on the syndrome group.  This chapter
diagonalizes that convolution exactly with the Walsh--Hadamard transform.

Let the outer parity-check rank be `r`, so syndromes form `F_2^r`.  Block `j`
permits a finite set `A_j` of syndrome increments.  A compatible block choice
has total syndrome equal to the xor of its increments.

## 1. Syndrome convolution

### Theorem PP3cik -- PROVED / GROUP-ALGEBRA LIST COUNT

The exact number of compatible block choices with terminal syndrome `s` is

```text
N(s) = (1_(A_1) * ... * 1_(A_m))(s),
```

where `*` is xor convolution on `F_2^r`.

#### Proof

Expanding the convolution sums one unit for every tuple
`(a_1,...,a_m)` with `a_j in A_j` and xor `a_1 xor ... xor a_m=s`.  These are
exactly the compatible block choices. ∎

## 2. Exact Walsh diagonalization

### Theorem PP3cil -- PROVED / CHARACTER-PRODUCT FORMULA

For `xi in F_2^r`, define

```text
hat f(xi)=sum_s (-1)^(xi dot s) f(s).
```

Then

```text
N(s)=2^(-r) sum_xi (-1)^(xi dot s)
      product_j hat(1_(A_j))(xi).
```

Repeated identical blocks therefore require only powering their integer Walsh
spectrum, followed by one inverse transform.

#### Proof

Walsh characters diagonalize xor convolution:
`hat(f*g)=hat f hat g`.  Applying this identity to `PP3cik` and using the exact
inverse Walsh formula gives the result.  All intermediate values are integers,
and the final numerator is divisible by `2^r`. ∎

## 3. Reconstruction and reverse load

### Theorem PP3cim -- PROVED / WALSH COUNT WITH WITNESS RECOVERY

The transform gives the exact surviving Hall-color list size.  One compatible
choice can be reconstructed by a prefix table or divide-and-conquer split.  If
every compatible color contributes reverse load at most `1/d`, the observed
load is exactly bounded by `N(s)/d`.  Any failed claim localizes to one transform
coefficient, inverse-divisibility check, or reconstructed increment tuple.

#### Proof

The count statement is `PP3cil`.  A nonzero prefix count always has a predecessor
increment with nonzero previous count, so backtracking reconstructs a tuple.
The load bound is additive over the surviving compatible colors. ∎

## 4. Stored exact fixture

The audit `scripts/check_walsh_hall_syndrome_convolution.py` has rank four and
twelve repeated blocks of two types.  It counts `1,049,760,000` compatible block
assignments.  The zero-syndrome list has size `65,622,784`, equal to the maximum
syndrome count.  Direct dynamic programming and the exact Walsh formula agree
on all sixteen syndromes, and the script reconstructs a tuple for syndrome
seven.

## 5. Prime-patching consequence

Long repeated Hall-tag patterns can now be evaluated by integer spectral powers
on a fixed `2^r`-state transform, rather than by scanning colors or advancing a
large block-by-block list table.
