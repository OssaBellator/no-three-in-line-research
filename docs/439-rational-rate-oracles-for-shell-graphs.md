# Rational rate oracles and robust brackets for shell graphs

`docs/433` gives a multiplicative Bellman--Ford procedure at one proposed shell
rate.  This chapter packages that procedure as an exact rational decision
oracle, shows how to isolate the optimal cycle rate without taking roots, and
records a simple perturbation reserve.

Let a finite directed shell graph have positive rational edge multipliers
`p_e`.  Write

```text
mu=max_C (product_(e in C) p_e)^(1/|C|),
```

where the maximum is over directed cycles.

## 1. Exact rational decision

### Theorem PP3cbd -- PROVED / RATIONAL SHELL-RATE ORACLE

For every positive rational `q`, `|V|` rounds of multiplicative Bellman--Ford
using normalized weights `p_e/q` decide exactly whether `mu<=q`.

If yes, the algorithm returns a positive rational potential `a` satisfying

```text
p_(uv) a(v)<=q a(u)
```

on every edge.  If no, predecessor tracing returns a simple directed cycle `C`
with the exact rational inequality

```text
product_(e in C) p_e>q^|C|.
```

#### Proof

This is `PP3cal--PP3can`, noting that all path products and comparisons remain
rational; no logarithms or algebraic roots are required. ∎

## 2. Exact rational bracketing

### Theorem PP3cbe -- PROVED / MONOTONE RATE BRACKETS

Suppose the oracle fails at rational `q_-` and succeeds at rational `q_+`, with
`q_-<q_+`.  Then

```text
q_-<mu<=q_+.
```

Applying the oracle successively at rational mediants or dyadic midpoints yields
an arbitrarily narrow exact rational bracket.  Every lower endpoint is certified
by an explicit cycle and every upper endpoint by a rational potential.

#### Proof

Cycle feasibility is monotone in `q`.  Failure gives `mu>q_-`; success gives
`mu<=q_+`.  Repeating preserves the invariant. ∎

## 3. Multiplicative perturbation reserve

### Proposition PP3cbf -- PROVED / ROBUST SHELL POTENTIAL

If `a` certifies rate `q` for weights `p_e` and perturbed multipliers satisfy

```text
tilde p_e<=gamma p_e
```

for every edge, then the same potential certifies rate `gamma q`.  In
particular, contraction survives whenever

```text
gamma q<1.
```

#### Proof

Multiply every certified edge inequality by `gamma`. ∎

Thus a rational upper-rate certificate automatically carries a quantitative
multiplicative error budget.

## 4. Revised shell frontier

A finite shell quotient now has an exact yes/no oracle, an explicit interval
certificate for its optimal cycle rate, and a robust reserve for geometric
estimation error.  The remaining task is to construct a quotient whose edge
multipliers are valid upper bounds for the actual clean-macro transitions.

## 5. Exact diagnostic

Run

```bash
python scripts/check_rational_shell_rate_oracle.py
```

The stored rational graph is certified to have optimal rate in
`(763/1000,191/250]`; the lower endpoint returns an expansive three-cycle and the
upper endpoint returns a nonconstant rational potential.
