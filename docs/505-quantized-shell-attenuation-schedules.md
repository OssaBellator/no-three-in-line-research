# Quantized shell attenuation schedules

`docs/493` and `docs/499` describe rational parametric shell attenuations.  A
geometric construction may only apply attenuation in integer multiples of a
fixed quantum.  This chapter converts rational cycle-cover solutions into
finite quantized schedules with one-sided feasibility and explicit cost loss.

Consider

```text
minimize c dot x
subject to A x >= Delta,  x>=0,
```

with `A,c,Delta` nonnegative and rational.  For denominator `M`, set

```text
u_M(x)_e = ceil(M x_e)/M.
```

## 1. Feasible upward quantization

### Theorem PP3cit -- PROVED / CYCLE-SAFE CEILING ROUNDING

If `x` satisfies every shell cycle constraint, then `u_M(x)` also satisfies
every constraint.

#### Proof

Coordinatewise `u_M(x)>=x`.  Since `A>=0`,
`A u_M(x)>=A x>=Delta`. ∎

## 2. Quantized cost guarantee

### Theorem PP3ciu -- PROVED / ADDITIVE GRID OVERHEAD

The rounded schedule satisfies

```text
0 <= c dot u_M(x)-c dot x < ||c||_1/M.
```

If upper edge caps are present, the same conclusion holds whenever each cap has
at least `1/M` slack on every rounded coordinate.

#### Proof

Each coordinate increases by less than `1/M`; multiply by `c_e` and sum.  The
cap statement is immediate. ∎

## 3. Exact integer covering certificate

### Theorem PP3civ -- PROVED / FINITE QUANTIZED SHELL ORACLE

The optimal denominator-`M` schedule is the integer covering problem

```text
minimize c dot z
subject to A z >= M Delta,  z in Z_+^E,
```

scaled by `1/M`.  Exact branch-and-bound, together with the rational LP
relaxation, gives a finite optimality certificate.  If `M` clears the
denominators of a rational continuous optimum, quantization has zero loss.

#### Proof

Substituting `x=z/M` gives the displayed integer system.  Finite exact integer
optimization is complete on any bounded cost sublevel.  Denominator divisibility
makes the continuous optimum an integer-grid point. ∎

## 4. Stored exact fixture

The audit `scripts/check_quantized_shell_attenuation.py` uses the triangle cycle
constraints

```text
x+y>=1/2,  y+z>=2/3,  z+x>=5/6.
```

The continuous optimum is `(1/3,1/6,1/2)` of cost one.  At denominator four,
ceiling rounding gives `(1/2,1/4,1/2)` and exact grid optimum `5/4`.
Denominator six realizes the continuous optimum exactly.  Denominators through
twenty are audited.

## 5. Prime-patching consequence

Rational shell repairs now translate into a bounded number of discrete geometric
attenuation operations.  Every cycle inequality remains valid, while the total
extra shell cost is explicitly controlled by the chosen denominator.
