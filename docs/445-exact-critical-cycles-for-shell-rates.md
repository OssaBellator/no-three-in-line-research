# Exact critical cycles for shell rates

`docs/439` brackets the optimal shell contraction rate by rational oracle calls.
When the finite shell graph is fixed, the exact optimum is an algebraic number
determined by one simple cycle.  This chapter gives a radical-free certificate
and a rational robustness test.

## 1. Exact comparison without radicals

For a simple directed cycle `C`, let `P_C` be its rational edge-product and
`ell_C` its length.  Its geometric rate is `P_C^(1/ell_C)`.

### Theorem PP3cbv -- PROVED / CROSS-POWER CRITICAL-CYCLE SELECTION

Two cycle rates satisfy

```text
P_C^(1/ell_C) >= P_D^(1/ell_D)
```

exactly when

```text
P_C^(ell_D) >= P_D^(ell_C).
```

Consequently a critical cycle can be selected using rational arithmetic only.

#### Proof

Raise both nonnegative quantities to the positive integer power
`ell_Cell_D`. ∎

## 2. Algebraic optimum certificate

### Theorem PP3cbw -- PROVED / CRITICAL POLYNOMIAL CERTIFICATE

Let `C_*` be a simple cycle such that

```text
P_D^(ell_*) <= P_*^(ell_D)
```

for every simple cycle `D`.  Then the optimal shell rate `mu` is the unique
positive root of

```text
x^(ell_*)-P_*=0.
```

The cycle, its product, and the finite cross-power inequalities form an exact
algebraic certificate for `mu`.

#### Proof

Every closed walk decomposes into simple cycles, so its geometric mean is at
most the largest simple-cycle mean.  The selected cycle attains that maximum.
Its positive geometric mean is exactly the positive root of the displayed
polynomial. ∎

## 3. Rational robustness margin

Suppose every edge weight may change by a multiplicative factor in
`[Gamma^(-1),Gamma]`.

### Theorem PP3cbx -- PROVED / UNIQUE-CYCLE PERTURBATION RESERVE

A critical cycle `C_*` remains uniquely critical throughout that uncertainty if
for every other simple cycle `D`,

```text
P_*^(ell_D)
 >P_D^(ell_*) Gamma^(2 ell_* ell_D).
```

#### Proof

In the worst case, every edge of `C_*` shrinks by `Gamma^(-1)` while every edge
of `D` grows by `Gamma`.  Comparing the two perturbed geometric means and
clearing roots gives exactly the displayed inequality. ∎

## 4. Exact diagnostic

Run

```bash
python scripts/check_exact_critical_shell_cycles.py
```

The script enumerates all five simple cycles of a rational four-state shell
graph.  It certifies the unique critical cycle `(0,1)`, exact polynomial
`x^2-3/5`, and rational perturbation factor `Gamma=1001/1000`.

The next theorem identifier after this chapter is `PP3cby`.
