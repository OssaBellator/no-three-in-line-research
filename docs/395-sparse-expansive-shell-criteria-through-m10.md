# Sparse expansive-shell criteria through `m=10`

`docs/390` converts total positive shell excess into a product bound using the
number of nonterminal boundaries. This chapter gives a complementary criterion:
only count the boundaries whose reverse-column norm exceeds one by a specified
factor.

No nonterminal shell norm is audited here, and no asymptotic bound on the number
of expansive boundaries is proved.

## 1. Counting bad shell boundaries

Let `tau<1` be the terminal-shell norm and let `kappa_1,...,kappa_r` be the
nonterminal adjacent-shell norms.

### Proposition PP3bvv -- PROVED / SPARSE EXPANSIVE-SHELL PRODUCT

Suppose at most `q` nonterminal boundaries have norm greater than one, every such
boundary has norm at most `B>=1`, and all remaining boundaries have norm at most
one. Then

```text
kappa_total <= tau B^q.
```

In particular, the complete trajectory contracts whenever

```text
tau B^q<1.
```

#### Proof

Apply the shell-product theorem `PP3buj`. At most `q` factors contribute more
than one, each by at most `B`; every other factor can be discarded from an upper
bound. ∎

This criterion is independent of the total shell horizon once the number of
expansive boundaries is controlled.

## 2. Exact audited strong-shell allowances

Insert the exact terminal factors and the audited nonterminal boundary counts
`2,3,4`.

### Theorem PP3bvw -- PROVED / VERIFIED FINITELY / STRONG-SHELL COUNT PROFILE

For a strong-shell ceiling `B=3/2`, contraction is guaranteed under

```text
m=8:  at most 2 expansive boundaries,
m=9:  at most 1 expansive boundary,
m=10: at most 4 expansive boundaries.
```

The corresponding exact bounds are

```text
m=8:
  1468416446839930521721999
  /1684417929217282999139400
  =0.8717649114...;

m=9:
  406616023430754819367780545483294984597292560691
  /472629195949389669987697827219988472645144908800
  =0.8603277726...;

m=10:
  47276550455881871882352184583946271968537909
  /60166841283680893227929821793540106430105600
  =0.7857575609....
```

At `m=9`, two `3/2`-expansive boundaries would give

```text
1.2904916589...>1,
```

so the one-boundary allowance is sharp using only `tau_9`, `B=3/2`, and the bad-
boundary count.

For a doubling ceiling `B=2`, the guaranteed counts are

```text
m=8:  at most 1 doubling boundary,
m=9:  no doubling boundary,
m=10: at most 2 doubling boundaries.
```

The exact accepted and first rejected products are stored in the machine ledger.

#### Verification

The verifier reads the exact terminal factors, enumerates all possible bad-shell
counts up to the audited horizon, and checks the largest accepted count and the
first rejected count by exact `Fraction` arithmetic. ∎

## 3. Horizon-free structural consequence

### Corollary PP3bvx -- PROVED / BOUNDED-BAD-SHELL REDUCTION

Suppose a family of clean-macro trajectories has terminal factors

```text
tau_m<=tau_0<1.
```

If every trajectory has at most `q_0` expansive nonterminal boundaries, each of
norm at most `B`, while all other boundaries contract, then the entire family has
uniform reverse-column norm at most

```text
tau_0 B^(q_0).
```

Thus a uniform contraction theorem follows from

```text
tau_0 B^(q_0)<1,
```

even when the total cycle-minimum depth grows.

#### Proof

Apply `PP3bvv` with the uniform constants. ∎

The all-shell frontier now has two complementary geometric routes:

1. control total positive excess as in `docs/390`; or
2. show that only boundedly many shell boundaries are expansive and bound their
   individual severity.

The latter may be more natural if a decreasing invariant forces most shell
transitions to be contractive but permits a few exceptional gates.

Verify with

```bash
python scripts/verify_terminal_sparse_expansive_shells.py .
```

The next theorem identifier after this chapter is `PP3bvy`.
