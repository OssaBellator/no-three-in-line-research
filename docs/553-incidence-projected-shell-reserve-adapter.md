# Incidence-projected shell reserve adapter

The shell row in `docs/543--548` is expressed in a small common resource space,
while the geometric construction has a larger coupled shell-incidence system.
This chapter gives a finite projection adapter and a certificate for exact pooled
startup reserves.

Let component residuals be `d^(k)(t) in Q^r`.  A nonnegative incidence matrix
`H in Q_>=0^(m by r)` maps them to physical shell resources.

## 1. Incidence projection commutes with scheduling

### Theorem PP3coh -- PROVED / SHELL INCIDENCE-PROJECTION ADAPTER

For fixed component phases, put

```text
u(t)=H sum_k d^(k)(t).
```

Every physical prefix residual equals `H` applied to the corresponding aggregate
component prefix.  Hence a finite phase word in component coordinates determines
the complete physical shell trajectory exactly.

#### Proof

Matrix multiplication is linear and commutes with finite summation over
components and time. ∎

## 2. Exact physical reserve and dual witnesses

### Theorem PP3coi -- PROVED / PHYSICAL SHELL BUFFER CERTIFICATE

For a zero-sum physical supercycle `u(1),...,u(L)`, the coordinatewise least
startup reserve is

```text
b_j=max_(0<=t<=L) (-sum_(s<=t) u_j(s))_+.
```

A certificate consists of the phase tuple, the physical prefix table, and for
every positive coordinate `b_j` a prefix attaining `-b_j`.  This certificate is
both feasible and coordinatewise minimal.

#### Proof

The physical reserve after each prefix is `b` plus that prefix residual.  The
displayed coordinatewise maximum is therefore necessary and sufficient, and an
attaining prefix witnesses necessity. ∎

## 3. Ledger overhead after projection

### Theorem PP3coj -- PROVED / SHELL ROW FROM PHYSICAL RESERVE

Let `p in Q_>=0^m` be the physical reserve-price vector and let a finite
interface seam cost at most `gamma`.  Repeating the certified zero-sum
supercycle for `N` slots contributes shell-row overhead at most

```text
(p dot b+gamma)/N.
```

In particular, if one phase tuple has `b=0`, the shell row is at most `gamma/N`
for every truncation.

#### Proof

Complete supercycles have zero residual.  One final prefix is protected by `b`,
and the only nonperiodic term is the declared seam.  Divide the bounded startup
cost by `N`. ∎

## 4. Stored exact fixture

The audit `scripts/check_shell_incidence_adapter.py` uses the opposite period-three
component words from `docs/541` and the physical incidence map

```text
H=((1,0),(0,1),(1,1)).
```

All nine phase pairs are enumerated.  Exactly three aligned pairs have zero
physical residual in every slot and hence zero startup reserve in all three
physical resources.  With one unit of seam price, the derived shell row is

```text
1/N<=1/40
```

for every `N>=40`.  One hundred repeated periods are checked prefix by prefix.

## 5. Prime-patching consequence

The shell realization problem is reduced to writing the actual coupled shell
incidence matrix and the finite component residual words.  Once these are
specified, phase optimization and reserve verification occur directly in the
physical resource coordinates.  The stored incidence matrix is an interface
fixture, not yet the actual shell-incidence system of the prime patch.
