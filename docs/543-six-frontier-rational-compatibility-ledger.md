# Six-frontier rational compatibility ledger

The preceding six chapters produce independently auditable certificates for
boundary markers, Hall transport, threshold cycles, prefix trees, shell reserves,
and interaction optimization.  This chapter puts those outputs into one typed
ledger.  The purpose is not to assert geometric realizability; it is to make all
period, denominator, and strict-slack obligations visible in one finite object.

A ledger row records a rational loss `ell_i`, a state period `p_i`, a denominator
`d_i`, and a certified perturbation allowance `eta_i`.

## 1. Common period and denominator

### Theorem PP3cnd -- PROVED / RATIONAL LEDGER NORMAL FORM

For finitely many rational ledger rows, let

```text
L=lcm_i p_i,
D=lcm_i d_i.
```

Then every state obligation is represented by one of the `L` combined residue
states, and every loss inequality becomes an integer inequality after
multiplication by `D`.  Thus compatibility of the displayed ledger is a finite
residue table together with exact integer arithmetic.

#### Proof

A side length determines each local state by reduction modulo `p_i`; the Chinese
remainder map into the product factors through reduction modulo their least
common multiple `L`.  Every rational whose denominator divides some `d_i`
becomes integral after multiplication by `D`. ∎

## 2. Strict additive composition

### Theorem PP3cne -- PROVED / LEDGER SLACK COMPOSITION

Suppose the global admissible loss is `M`, the certified base losses are
`ell_i`, and implementation perturbations satisfy `0<=delta_i<=eta_i`.  If

```text
sum_i ell_i + sum_i eta_i < M,
```

then every simultaneous implementation respecting the row interfaces remains
strictly feasible.  The residual margin is exactly

```text
sigma=M-sum_i ell_i-sum_i eta_i.
```

#### Proof

Add the rowwise inequalities.  No cancellation is assumed, so the bound is valid
for every compatible realization.  Strict positivity of `sigma` gives the
claimed margin. ∎

## 3. Stored six-row fixture

### Theorem PP3cnf -- PROVED / PRIME-PATCHING LEDGER FIXTURE

The exact fixture is

| Frontier | Period | Denominator | Base loss | Perturbation cap |
|---|---:|---:|---:|---:|
| boundary | 3 | 120 | `7/120` | `1/960` |
| Hall | 8 | 160 | `9/160` | `1/960` |
| threshold | 12 | 24 | `1/24` | `1/1920` |
| prefix | 2 | 32 | `1/32` | `1/1920` |
| shell | 3 | 40 | `1/40` | `1/1920` |
| interaction | 2 | 48 | `1/48` | `1/1920` |

It has

```text
L=24,
D=480,
sum_i ell_i=112/480=7/30,
M=120/480=1/4,
base slack=8/480=1/60,
sum_i eta_i=1/240,
robust slack=1/80.
```

#### Proof

The least common multiples are direct.  Scaling the six losses by 480 gives
`28,27,20,15,12,10`, whose sum is 112.  The perturbation caps sum to `1/240`, so
`1/4-7/30-1/240=1/80`. ∎

## 4. Stored exact audit

The audit `scripts/check_six_frontier_parameter_ledger.py` reconstructs the
least common multiples, all scaled integer losses, the 24 combined residue
states, and both strict margins using `Fraction` arithmetic.

## 5. Prime-patching consequence

Any proposed global closure can now be checked against one explicit interface:
which row consumes which margin, which residue or phase it requires, and how much
unmodelled perturbation it is allowed.  The ledger deliberately does not prove
that the geometric prime-patching construction realizes these six rows; that is
the remaining conversion problem.
