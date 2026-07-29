# Critical-cycle stability cones

`docs/445` identifies the exact shell rate from a unique critical cycle. This
chapter describes the complete multiplicative perturbation region in which that
cycle remains critical and records the exact local sensitivity of the rate.

## 1. Multiplicative perturbations

For a simple cycle `C`, let `P_C` be its baseline edge product, `ell_C` its
length, and

```text
Gamma_C=product_(e in C) gamma_e
```

for positive edge multipliers `gamma_e`. Fix a baseline critical cycle `C_*`.

### Theorem PP3ccn -- PROVED / STABILITY-CONE CERTIFICATE

The cycle `C_*` remains critical after perturbation exactly when, for every
simple cycle `C`,

```text
(P_* Gamma_*)^(ell_C)>=(P_C Gamma_C)^(ell_*).
```

Strict inequalities for all competitors certify uniqueness.

#### Proof

The displayed cross-power comparison is equivalent to comparing the two
positive geometric means, with no extraction of radicals. Imposing it against
every simple cycle is exactly the definition of criticality. ∎

## 2. One-edge margins

Let only one edge `f` be multiplied by `gamma`, and let `m_C(f)` be its
multiplicity in cycle `C`.

### Theorem PP3cco -- PROVED / EXACT ONE-EDGE THRESHOLD

For every competitor `C`, the admissible factors satisfy

```text
gamma^(m_*(f) ell_C-m_C(f) ell_*)
 >= P_C^(ell_*)/P_*^(ell_C).
```

Thus the complete one-edge stability interval is the intersection of finitely
many exact algebraic lower and upper bounds. Every endpoint is certified by a
specific tying cycle.

#### Proof

Substitute the one-edge perturbation into `PP3ccn` and collect the integer power
of `gamma`. ∎

## 3. Local rate sensitivity

### Theorem PP3ccp -- PROVED / LOGARITHMIC CRITICAL-CYCLE GRADIENT

Inside the strict stability cone,

```text
log mu=(log P_*+sum_(e in C_*) log gamma_e)/ell_*,
```

so

```text
d log(mu)/d log(gamma_e)=m_*(e)/ell_*.
```

Edges outside the critical cycle have zero local sensitivity until a stability
wall is reached.

#### Proof

Within the strict cone the maximizing cycle does not change, so the rate is its
perturbed geometric mean. Differentiate the displayed identity. ∎

## Frontier consequence

The shell frontier now has a finite exact robustness polyhedron in logarithmic
coordinates. Every loss of the current rate certificate is localized to the
first competitor cycle whose cross-power inequality becomes tight.
