# Automaton-constrained switching for Hall transfers

`docs/532` controls arbitrary switching by one common Dobrushin coefficient.
Many Hall gadgets have additional local switching rules, and those rules can
improve the sharp mixing horizon.  This chapter records an exact finite-automaton
certificate.

Let `Q` be a finite automaton whose labeled edges choose stochastic Hall transfer
kernels `K_e`.  All kernels preserve the same stationary syndrome distribution
`pi`.  Let `tau_e` be any certified contraction factor on the zero-mass
subspace, for example a Dobrushin coefficient.

## 1. Max-product automaton envelope

### Theorem PP3cmo -- PROVED / AUTOMATON-SWITCHED HALL ENVELOPE

For an allowed path `e_1...e_n`,

```text
||nu K_(e_1)...K_(e_n)-pi|| <=
||nu-pi|| product_t tau_(e_t).
```

The worst certified length-`n` envelope is the maximum path product in the
finite weighted automaton.  It is computed exactly by max-product dynamic
programming on `(time,automaton state)`.

#### Proof

Apply the one-step contraction inequality successively.  The automaton contains
exactly the legal kernel words, so maximizing the resulting scalar product over
its paths gives the stated envelope. ∎

## 2. Critical switching cycles

### Theorem PP3cmp -- PROVED / CONSTRAINED JOINT CONTRACTION RATE

Let

```text
rho=max_C (product_(e in C) tau_e)^(1/|C|),
```

where `C` ranges over directed cycles of the switching automaton.  Then the
worst path product is at most `C_0 rho^n` for a finite rational prefactor `C_0`.
If `rho<1`, every allowed switching sequence mixes exponentially.  A maximum
cycle-mean computation in logarithmic weights, or an exact multiplicative cycle
comparison, certifies `rho`.

#### Proof

Delete repeated automaton states from a path.  The remaining simple prefix and
suffix have bounded length, while each deleted cycle contributes at most its
geometric-mean bound.  The finite acyclic remainder is absorbed into `C_0`. ∎

## 3. Reverse-load stopping rule

### Theorem PP3cmq -- PROVED / AUTOMATON HALL HORIZON

If a certified syndrome deviation after `n` blocks is `epsilon_n`, then the
largest syndrome probability is at most

```text
max_s pi_s+epsilon_n.
```

With residual Hall degree `d`, the reverse load is at most this quantity divided
by `d`.  The first `n` whose max-product envelope meets a target is therefore a
finite switch-aware mixing horizon.

#### Proof

The deviation bound controls every syndrome coordinate.  Hall expansion divides
the compatible colors among at least `d` targets. ∎

## 4. Stored exact fixture

The audit `scripts/check_automaton_switched_hall_products.py` uses two symmetric
binary syndrome kernels with exact contraction factors

```text
A: 1/2,
B: 3/4,
```

and forbids the automaton word `BB`.  Every legal word through length 20 is
multiplied exactly.  The worst word alternates the two kernels, seven blocks
still have deviation `81/4096`, and eight blocks have deviation `81/8192`.
Thus eight is the sharp one-percent horizon.  At Hall degree 20 the certified
load is `4177/163840`.

## 5. Prime-patching consequence

Localized Hall transport can now exploit admissible gadget-switching rules
without reverting to the pessimistic unconstrained joint bound.  The certificate
is finite, exact, and directly returns both the adversarial switching word and
the first safe block depth.
