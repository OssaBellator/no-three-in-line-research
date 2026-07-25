# Core-aware local Ore completion

PP3vt bounds the actual same-slot anchor mass of every assignment crossing the
canonical movement deficiency core. The refill side has the transposed bound.
Combining those bottlenecks with the controller-defect degree estimates PP3ly
gives a direct local Ore theorem.

Thus a sublinear anchor deficiency completes whenever its per-crossing weight
fits inside the existing controller-degree slack. Failure has a quantitative
certificate: one canonical core carries enough slot-expanded energy per crossing
to consume that slack.

## 1. Balanced ownership caps

Choose balanced movement and refill ownerships by PP3vj and complete their
canonical cores by PP3vt.

Let

```text
d_U, E_U = movement core deficiency and slot-expanded energy,
d_V, E_V = refill core deficiency and slot-expanded energy.
```

Use the convention `E_U/d_U=0` when `d_U=0`, and similarly on the refill side.
Define

$$
U_cap = max(u, E_U/d_U),
$$

$$
V_cap = max(u, E_V/d_V).
$$

Then every movement label owned by macro `i` satisfies `U_i(A) <= U_cap`, and
every owned refill label satisfies `V_i(B) <= V_cap`.

For macro `i`, put

```text
alpha_i = maximum a_i(A) over its owned movement labels,
beta_i  = maximum b_i(B) over its owned refill labels,
DA_i    = (1-gamma)R-alpha_i,
DB_i    = (1-gamma)R-beta_i.
```

## 2. Uniform owned-label nondegree bounds

### Proposition PP3vx -- PROVED

If `DA_i>0` and `DB_i>0`, then every owned movement label in macro `i` has global
refill nondegree at most

$$
r_i = (B_i+U_cap)/DA_i,
$$

and every owned refill label has global movement nondegree at most

$$
s_i = (A_i+V_cap)/DB_i.
$$

The nondegrees inside the induced `W by W` owned-label compatibility graph are
bounded by the same quantities.

#### Proof

Apply PP3ly and use `a_i(A) <= alpha_i`, `U_i(A) <= U_cap`, and the analogous
refill inequalities. Restricting the opposite label set from `T` labels to its
`W` owned labels cannot increase the number of nonneighbours. ∎

## 3. Core-aware local Ore theorem

### Theorem PP3vy -- PROVED

Suppose for every macro `i`:

```text
DA_i > 0,
DB_i > 0,
r_i+s_i <= W.
```

Then every induced owned-label compatibility graph has a perfect matching.
Their union gives a saturation-compatible controller-aware global allocation,
and the prime-gap-scale patch follows from PP3hq.

#### Proof

For any nonedge between an owned movement label and an owned refill label, the
sum of their nondegrees in the induced `W by W` graph is at most `r_i+s_i`, hence
at most `W`. The bipartite Ore theorem gives a perfect matching in each macro.
The ownerships use every numerical label exactly once. ∎

This theorem allows anchor-threshold violations; only their actual bottleneck
weights enter.

## 4. Baseline controller slack

Define the baseline anchor-threshold scores

$$
r_i^0 = (B_i+u)/DA_i,
$$

$$
s_i^0 = (A_i+u)/DB_i.
$$

Suppose

$$
r_i^0+s_i^0 <= W-h_i
$$

for some local slack `h_i>0`.

### Proposition PP3vz -- PROVED

Macro `i` satisfies the core-aware Ore condition whenever

$$
(U_cap-u)/DA_i + (V_cap-u)/DB_i <= h_i.
$$

#### Proof

Subtract the baseline score sum from `r_i+s_i`. The increase is exactly the left
side of the displayed inequality. ∎

Thus the exceptional-core weights pay only for the amount by which they exceed
the original anchor threshold.

## 5. Energy certificate when slack is consumed

### Corollary PP3wa -- PROVED

Assume the baseline slack inequality at macro `i`, but the core-aware Ore
condition fails there. Then at least one of the following holds:

1. the movement core satisfies
   
   $$
   E_U/d_U > u + h_i DA_i/2;
   $$
2. the refill core satisfies
   
   $$
   E_V/d_V > u + h_i DB_i/2.
   $$

The relevant alternative is ignored when its deficiency is zero.

#### Proof

Failure and PP3vz give

$$
(U_cap-u)/DA_i + (V_cap-u)/DB_i > h_i.
$$

At least one summand exceeds `h_i/2`. Substitute the definitions of `U_cap` and
`V_cap`. ∎

Equivalently, one slot-expanded canonical core has total energy at least its
number of necessary crossings times the displayed local threshold.

## 6. Revised direct-allocation endpoint

### Corollary PP3wb -- PROVED

After the anchor-deficiency reduction, the direct allocation route has the
following exact dichotomy.

1. The movement and refill core bottlenecks fit inside every macro's baseline
   controller slack, and PP3vy completes the full global allocation.
2. Some macro has a nonpositive controller denominator, insufficient baseline
   slack, or one canonical movement/refill core has energy per necessary crossing
   large enough to consume that slack as in PP3wa.

Therefore the remaining direct obstruction is no longer a Hall deficiency or a
count of exceptional labels. It is a concrete interaction between:

- controller defect denominators and aggregate masses;
- local Ore slack;
- slot-expanded anchor energy in one canonical deficient core.