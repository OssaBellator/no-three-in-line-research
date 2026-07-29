# Phase-optimized startup buffers for shell periods

`docs/517` computes the startup buffer of one fixed shell word.  A periodic word
also has finitely many cyclic phases, and choosing the phase can change which
cycle constraints require initial slack.

Let a period have service vectors `s_0,...,s_{L-1}` and average target

```text
tau=(s_0+...+s_{L-1})/L.
```

All inequalities are coordinatewise.

## 1. Exact buffer for one phase

### Theorem PP3ckv -- PROVED / PHASE PREFIX-DEFICIT FORMULA

For phase `p`, write the cyclic period as `s^(p)_1,...,s^(p)_L`.  Its least
coordinatewise startup buffer is

```text
b_j(p)=max_(1<=k<=L)
       (k tau_j-sum_(t=1)^k s^(p)_(t,j))_+.
```

With this buffer, infinite repetition of the phased period satisfies every shell
service inequality at every prefix.  No smaller buffer works for that phase.

#### Proof

The displayed maximum is necessary at the prefix attaining it.  During repeated
periods, complete periods have zero net deficit, so every prefix deficit equals a
prefix deficit inside one period.  The maximum therefore suffices. ∎

## 2. Exact phase optimization

### Theorem PP3ckw -- PROVED / FINITE BUFFER PARETO SCAN

The complete set of phase-minimal buffers is obtained by evaluating the `L`
vectors `b(p)` and Pareto-pruning them.  For any nonnegative buffer price `w`, the
minimum startup cost is

```text
min_p w dot b(p).
```

For one scalar constraint, some phase has zero buffer; for several constraints a
zero-buffer phase need not exist.

#### Proof

There are only `L` phases and `PP3ckv` gives the unique least buffer of each.
Weighted optimization is therefore finite.  In the scalar case, rotate a
zero-sum increment word immediately after a minimum partial sum; every subsequent
partial sum is nonnegative.  Different coordinates can require incompatible
rotations. ∎

## 3. All-length truncation

### Theorem PP3ckx -- PROVED / PHASED ALL-PREFIX SHELL CERTIFICATE

Truncating the infinite phased word after any length `N` preserves feasibility
with the same startup buffer.  Its average startup overhead is exactly
`w dot b(p)/N`, and the service-rate error is bounded by one fixed period divided
by `N`.

#### Proof

Every truncation is a prefix already covered by `PP3ckv`.  The buffer is paid
once, while total length grows.  Only the incomplete final period contributes a
rate discrepancy. ∎

## 4. Stored exact fixture

The audit `scripts/check_phase_optimized_shell_buffers.py` uses the three unit
service vectors and target `(1/3,1/3,1/3)`.  The three phases have buffers

```text
(0,1/3,2/3), (2/3,0,1/3), (1/3,2/3,0).
```

Every phase has minimum `l_1` buffer one, and no zero-buffer phase exists.  The
audit checks every prefix through length 100 for every phase.

## 5. Prime-patching consequence

Periodic shell repairs can now choose their cyclic origin optimally.  The needed
startup reserve is a finite exact phase calculation, and its contribution to a
long construction vanishes as `O(1/N)`.
