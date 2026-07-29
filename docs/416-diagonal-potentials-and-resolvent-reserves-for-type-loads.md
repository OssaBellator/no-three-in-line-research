# Diagonal potentials and resolvent reserves for type loads

`docs/410` replaces scalar stage loads by nonnegative type-transition matrices
and closes repeated procedures when the spectral radius is below one.  This
chapter gives an equivalent positive-potential certificate, an explicit bound
for arbitrarily many repetitions, and a perturbation reserve for omitted or
exceptional transitions.

The statements are general.  They do not yet construct the prime-patching type
matrix.

## 1. Positive diagonal type potentials

Let `M` be a finite nonnegative square matrix.  For a positive type potential
`a`, define

```text
q_a(M)=max_i (Ma)_i/a_i.
```

### Theorem PP3byl -- PROVED / DIAGONAL TYPE-POTENTIAL BOUND

For every positive `a`,

```text
rho(M)<=q_a(M).
```

Moreover

```text
rho(M)=inf_(a>0) q_a(M).
```

#### Proof

The inequality is the Collatz--Wielandt bound.  For an irreducible matrix, a
positive Perron vector attains equality.  For a reducible matrix, apply the
irreducible result to its maximal Perron block and approximate zero coordinates
by positive epsilon entries, or equivalently apply Collatz--Wielandt to
`M+epsilon 11^T` and let `epsilon` decrease to zero. ∎

Thus type-dependent weights can certify contraction without computing an exact
eigenvector.

## 2. Exact strict-contraction criterion

### Theorem PP3bym -- PROVED / POSITIVE SUPERSOLUTION CHARACTERIZATION

The following are equivalent:

1. `rho(M)<1`;
2. there are `a>0` and `q<1` such that

   ```text
   Ma<=q a;
   ```

3. there is `a>0` such that

   ```text
   Ma<a
   ```

   coordinatewise.

#### Proof

Condition 2 implies 1 by `PP3byl`, and condition 2 implies 3.  Condition 3 gives
condition 2 by taking

```text
q=max_i (Ma)_i/a_i<1.
```

Finally, if `rho(M)<1`, the Neumann series converges and

```text
a=(I-M)^(-1) 1=sum_(t>=0) M^t 1
```

is positive.  It satisfies

```text
Ma=a-1<a.
```

∎

The vector `a` is a type budget: one stage consumes a strict fraction of that
budget in every coordinate.

## 3. Arbitrary repetition and inhomogeneous input

### Theorem PP3byn -- PROVED / TYPE-LOAD RESOLVENT BOUND

Suppose

```text
Ma<=q a
```

for some `a>0` and `0<=q<1`.  If a nonnegative input vector `b` satisfies

```text
b<=beta a,
```

then for every `n>=0`,

```text
sum_(t=0)^n M^t b
 <=beta (1-q^(n+1))/(1-q) a,
```

and hence

```text
sum_(t=0)^infinity M^t b
 <=beta a/(1-q).
```

#### Proof

Induction gives

```text
M^t b<=beta M^t a<=beta q^t a.
```

Sum the geometric series coordinatewise. ∎

This bounds not only one composed repair trajectory but the total reverse load
of all possible repetition depths under one common type envelope.

## 4. Perturbation reserve

### Corollary PP3byo -- PROVED / ROBUST TYPE-MATRIX CONTRACTION

Assume

```text
Ma<=q a,
Na<=epsilon a
```

for nonnegative matrices `M,N`.  Then

```text
(M+N)a<=(q+epsilon)a.
```

If

```text
q+epsilon<1,
```

then `rho(M+N)<1`, and every input `b<=beta a` obeys

```text
sum_(t>=0)(M+N)^t b
 <=beta a/[1-q-epsilon].
```

#### Proof

Add the two potential inequalities and apply `PP3byl`, `PP3bym`, and
`PP3byn` with `q+epsilon`. ∎

Thus rare exceptional type transitions need not be removed completely.  They
may be retained whenever their potential-weighted load fits inside the
spectral reserve of the main typed kernel.

## 5. Finite diagnostic

Run

```bash
python scripts/check_type_matrix_potential_resolvent.py
```

The checker uses exact rational matrices to verify diagonal potential bounds,
strict supersolutions, finite resolvent sums, and perturbation reserves.  It
also compares the matrix certificate with direct enumeration of all typed paths
through twelve stages.

The next theorem identifier after this chapter is `PP3byp`.
