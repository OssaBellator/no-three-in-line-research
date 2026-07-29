# Conservative matrix rounding for threshold schedules

`docs/503` floors a downward-closed threshold design coordinatewise.  Some
prime-patching schedules must also preserve exact source totals and exact global
action totals.  This chapter uses bipartite integral flow to round a rational
matrix while conserving both margins.

Let `P=(p_ij)` be a nonnegative rational matrix.  Fix an integer `M` such that
all scaled row sums and column sums of `MP` are integers.

## 1. Two-margin rounding

### Theorem PP3cjf -- PROVED / CONSERVATIVE MATRIX ROUNDING

There is a nonnegative integer matrix `N` satisfying

```text
sum_j N_ij = M sum_j p_ij,
sum_i N_ij = M sum_i p_ij,
|N_ij/M-p_ij|<1/M
```

for every entry.

#### Proof

Let `F_ij=floor(Mp_ij)` and `R_ij=Mp_ij-F_ij`.  The row and column deficits of
`F` are integers, and `R` itself is a feasible fractional bipartite flow between
those deficits using only entries with `R_ij>0` and unit edge capacities.
Bipartite network integrality gives a `0--1` flow `Z` with the same deficits.
Set `N=F+Z`.  The margins are exact.  On a fractional entry,
`|Z_ij-R_ij|<1`; on an integral entry both are zero.  Divide by `M`. ∎

## 2. Quotienting additive load potentials

### Theorem PP3cjg -- PROVED / ROW--COLUMN POTENTIAL ERROR BOUND

Let `Delta=N/M-P`.  For every coefficient matrix `A` and arbitrary row and
column potentials `r_i,s_j`,

```text
sum_ij Delta_ij(r_i+s_j)=0
```

and therefore

```text
|sum_ij Delta_ij A_ij|
 < (1/M) sum_ij |A_ij-r_i-s_j|.
```

#### Proof

Every row and column sum of `Delta` is zero by `PP3cjf`, so additive row and
column potentials vanish exactly.  Replace `A` by its residual after subtracting
those potentials, use `|Delta_ij|<1/M`, and apply the triangle inequality. ∎

## 3. Finite residual matching audit

### Theorem PP3cjh -- PROVED / ROUNDING-MATCHING CERTIFICATE

A conservative rounding is certified by the floor matrix and one integral
bipartite residual flow.  Verification checks residual support, row deficits,
column deficits, entry errors, and the final margins.  Any failure returns one
entry, row, column, or deficient residual cut.

#### Proof

These are exactly the finite conditions in the integral-flow proof of
`PP3cjf`. ∎

## 4. Stored exact fixture

The audit `scripts/check_conservative_matrix_rounding.py` uses

```text
P = [5/12  1/4  1/6  1/6]
    [1/3   1/6  1/4  1/4]
    [1/4   1/3  1/3  1/12]
```

at denominator `M=4`.  The exact row totals are `(4,4,4)` and column totals are
`(4,3,3,2)`.  Among the `2^8` residual choices, exactly three are conservative;
the canonical one is

```text
[1 1 1 1]
[2 0 1 1]
[1 2 1 0].
```

The script also verifies a structured load bound after quotienting explicit row
and column potentials.

## 5. Prime-patching consequence

Threshold randomization can now be converted to a finite schedule without
changing either the number of uses at each source or the global inventory of
each action.  Load error depends only on the genuinely non-additive part of the
kernel.
