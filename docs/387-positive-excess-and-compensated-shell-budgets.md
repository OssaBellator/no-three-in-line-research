# Positive-excess and compensated shell budgets

`docs/382` proves that adjacent-shell reverse-column norms multiply, and
`docs/384` uses the exact terminal factor to permit a common `6/5` bound on each
nonterminal shell.  This chapter gives an amortized alternative: only the total
positive excess above one must fit inside the terminal reserve.  Contractive
nonterminal shells can also be credited through the exact product.

No nonterminal shell norm is audited here, and no asymptotic shell-depth theorem
is claimed.

## 1. Total positive-excess bound

Let `tau<1` be the terminal-shell norm and let

```text
kappa_1,...,kappa_r
```

be the earlier adjacent-shell norms.  Define

```text
delta_j = max(kappa_j-1,0),
S       = sum_j delta_j.
```

### Proposition PP3bux -- PROVED / POSITIVE-EXCESS SHELL BUDGET

If `S<1`, then

```text
product_j kappa_j
 <= product_j (1+delta_j)
 <= 1/(1-S).
```

Consequently the complete clean-macro norm is at most

```text
tau/(1-S),
```

and contracts whenever

```text
S < 1-tau.
```

#### Proof

The first inequality is immediate.  Expanding the second product into elementary
symmetric sums, every term of degree `q` is bounded by the corresponding part of
`S^q`; hence

```text
product_j(1+delta_j)
 <= sum_(q>=0) S^q
 = 1/(1-S).
```

Multiplying by the terminal factor and comparing with one proves the criterion.
∎

This condition allows an individual shell to exceed the equal-factor ceiling,
provided the total positive excess remains controlled.

## 2. A common exact two-fifths reserve through `m=10`

The exact terminal factors `tau_m` from `PP3bsc` are all strictly below `3/5`.

### Theorem PP3buy -- PROVED / VERIFIED FINITELY / COMMON AMORTIZED RESERVE

At each audited size `m=8,9,10`, the complete clean-macro trajectory would
contract under the single condition

```text
sum_(nonterminal shells j) max(kappa_j-1,0) <= 2/5.
```

Indeed `1-S>=3/5`, so `PP3bux` gives the exact bounds

```text
m=8:
  1468416446839930521721999
  ----------------------------------------------
  2273964204443332048838190
  = 0.6457517862...;

m=9:
  406616023430754819367780545483294984597292560691
  ------------------------------------------------------------
  425366276354450702988928044497989625380630417920
  = 0.9559197473...;

m=10:
  5252950050653541320261353842660696885393101
  -------------------------------------------------
  20306308933242301464426314855319785920160640
  = 0.2586856167....
```

All are strictly below one.  The exact margins are recorded in the accompanying
machine ledger.

#### Proof

Use `S<=2/5` in `PP3bux`, obtaining a factor at most `5/3` for the nonterminal
product.  Multiply each exact terminal factor by `5/3` and reduce.  Exact cross
multiplication gives the three displayed strict inequalities. ∎

This is more flexible than a uniform per-shell rule but more conservative than
the exact product reserve.  For example one shell may carry nearly all of the
`2/5` excess while the others contract or stay below one.

## 3. Exact compensation by contractive shells

Partition the earlier shells into

```text
E = {j : kappa_j > 1},
C = {j : kappa_j < 1}.
```

### Corollary PP3buz -- PROVED / CONTRACTIVE-SHELL CREDIT

Write

```text
A = product_(j in E) kappa_j,
Cprod = product_(j in C) kappa_j.
```

The complete trajectory contracts exactly whenever

```text
tau A Cprod < 1.
```

Equivalently, the admissible expansion product is

```text
A < 1/(tau Cprod).
```

Thus every contractive nonterminal shell enlarges the terminal-only expansion
reserve by the multiplicative factor `1/Cprod`.  In logarithmic form the same
criterion is

```text
sum_j log(kappa_j) < -log(tau).
```

#### Proof

This is the shell-product theorem with the factors grouped above and below one.
All factors are nonnegative; zero gives immediate contraction, and otherwise
logs preserve the product comparison. ∎

## 4. Revised all-shell frontier

There are now three nested audit targets.

1. **Exact product:** prove `product kappa_j < 1/tau`.
2. **Amortized excess:** prove total positive excess below `1-tau`, or uniformly
   below `2/5` in the audited range.
3. **Simple local ceiling:** prove each nonterminal shell is at most `6/5`, as in
   `docs/384`.

The first can exploit strong contraction on some boundaries, the second permits
uneven expansion without tracking all products, and the third is easiest to
state.  Any one, together with a shell-depth bound and adjacent-fibre control,
would close the analytic clean-macro trajectory.

Verify the exact finite arithmetic with

```bash
python scripts/verify_terminal_shell_positive_excess_reserve.py .
```

The next theorem identifier after this chapter is `PP3bva`.
