# Canonical minimax codes for unequal corridor banks

`docs/432` reduces variable-length corridor scheduling to a Kraft feasibility
test at a proposed risk.  This chapter identifies the finite candidate set and
shows that optimal code lengths may be ordered canonically by bank risk.

Let bank `i` have conditioned base load `rho_i>0`.  One binary schedule symbol
retains at least a fraction `p`, with `0<p<1`.  A codeword of length `ell_i`
therefore contributes risk `rho_i p^(-ell_i)`.

## 1. Monotone optimal lengths

### Proposition PP3cba -- PROVED / HEAVIER BANKS GET SHORTER CODES

If `rho_i>=rho_j`, there is an optimal prefix code with

```text
ell_i<=ell_j.
```

#### Proof

If instead `ell_i>ell_j`, swap the two codewords.  Before the swap, the two
risks are `rho_i p^(-ell_i)` and `rho_j p^(-ell_j)`.  After the swap they are
`rho_i p^(-ell_j)` and `rho_j p^(-ell_i)`.  Since `rho_i>=rho_j` and
`p^(-ell_i)>=p^(-ell_j)`, the larger of the two risks cannot increase.  Repeated
inversions produce a monotone optimum. ∎

## 2. Finite candidate risks

### Theorem PP3cbb -- PROVED / FINITE MINIMAX CORRIDOR SEARCH

For `K>=2` banks, an optimal binary prefix code has maximum length at most
`K-1`.  Its optimum risk belongs to

```text
C={rho_i p^(-ell):1<=i<=K, 1<=ell<=K-1}.
```

The exact optimum is the smallest `R in C` for which the Kraft test of
`PP3caj` succeeds.

#### Proof

As in `PP3cat`, remove unary internal vertices from an optimal prefix tree; a
leaf at depth `d` forces at least `d+1` leaves, hence `d<=K-1`.  The maximum
risk equals one class risk and therefore lies in `C`.  Feasibility is exactly
`PP3caj`. ∎

## 3. Canonical certificate

### Theorem PP3cbc -- PROVED / SORTED-LENGTH CERTIFICATE

After sorting

```text
rho_1<=rho_2<=...<=rho_K,
```

it is enough to inspect nonincreasing length vectors

```text
ell_1>=ell_2>=...>=ell_K
```

with `1<=ell_i<=K-1` and `sum_i 2^(-ell_i)<=1`.  The best such vector is a
complete exact certificate of the global optimum.

#### Proof

`PP3cba` supplies an optimum with the displayed order, and `PP3cbb` supplies the
depth bound.  Every remaining vector is a realizable prefix-length multiset by
Kraft--McMillan. ∎

This converts corridor scheduling into a small monotone integer search rather
than a search over codewords or word kernels.

## 4. Exact diagnostic

Run

```bash
python scripts/check_canonical_corridor_codes.py
```

The script exhausts every monotone binary length vector for seven unequal banks,
checks the finite candidate algorithm, and records a sharp rational optimum.
