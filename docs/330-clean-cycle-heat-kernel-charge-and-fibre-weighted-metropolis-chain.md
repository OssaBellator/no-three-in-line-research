# Clean-cycle heat-kernel charge and a fibre-weighted Metropolis chain

`docs/324` expresses optimal merged fibre charge as a weighted Hall transport
problem.  This chapter gives the dynamic version: after a reversible walk on
clean Hamilton cycles, the exact merged charge is the `L^infinity` norm of a
heat-evolved source density.

The result isolates a canonical clean-cycle mixing problem.  No spectral gap,
logarithmic mixing bound, flaw-walk termination theorem, or asymptotic seed is
claimed.

## 1. The fibre-weighted clean-cycle measure

Let `Omega_cl` be the set of Hamilton cycles whose parity systems are
satisfiable.  For `rho in Omega_cl`, write

```text
c(rho) = number of parity components,
v(rho) = 2^c(rho).
```

Thus `v(rho)` is exactly the number of clean orientations above `rho`.  Put

```text
V = sum_(rho in Omega_cl) v(rho),
pi(rho)=v(rho)/V.
```

The probability measure `pi` is the cycle marginal of the uniform measure on
all parity-clean signed Hamilton states.

Two clean cycles are adjacent when one is obtained from the other by a
three-source successor rotation and the target parity system remains
satisfiable.  The adjacency relation is undirected because every fixed-source
successor rotation is an involution.

## 2. A canonical reversible clean-cycle kernel

Let

```text
D = C(m,3).
```

For adjacent clean cycles `rho` and `eta`, define

```text
K(rho,eta)
 = [1/(2D)] min(1,v(eta)/v(rho)).
```

Put the remaining row mass on the holding transition.

### Proposition PP3bnv -- PROVED / FIBRE-WEIGHTED METROPOLIS KERNEL

The kernel `K` is stochastic, at least one-half lazy, supported on clean
successor rotations, and reversible with stationary distribution `pi`.

If the clean induced rotation graph is connected, then `K` is irreducible.

#### Proof

There are at most `D` possible source triples, and every off-diagonal transition
has probability at most `1/(2D)`.  Hence the total off-diagonal row mass is at
most one half, so the holding probability is nonnegative and at least one half.

For adjacent cycles,

```text
v(rho)K(rho,eta)
 = [1/(2D)] min(v(rho),v(eta))
 = v(eta)K(eta,rho).
```

Dividing by `V` gives detailed balance with `pi`.  Support and irreducibility are
immediate from the definition and connectedness. ∎

The exact audits in `docs/320` and `docs/329` verify connectedness through
`m=10`, including the first clean parity graphs of positive cyclomatic rank.

## 3. Source density of one atomic flaw

Fix an atomic three-owner flaw `A`.  For a clean source cycle `rho`, let

```text
r_A(rho)
 = number of parity components met by the three owners of A.
```

If the prescribed signed owner assignments of `A` are compatible with the clean
fibre over `rho`, then the number of clean source orientations containing `A` is

```text
w_A(rho)=2^(c(rho)-r_A(rho));
```

otherwise put `w_A(rho)=0`.  Define the fibre-relative source density

```text
f_A(rho)=w_A(rho)/v(rho).
```

Thus, on compatible source cycles,

```text
f_A(rho)=2^(-r_A(rho)).
```

In particular `0<=f_A<=1/2`, and `f_A=1/8` when the three owners lie in three
distinct parity components.

## 4. Exact heat-kernel formula for merged charge

Consider the following action on clean signed source states containing `A`:

1. retain only the source Hamilton cycle `rho`;
2. run `t` steps of the clean-cycle kernel `K`, obtaining `eta`;
3. choose a uniformly random clean orientation in the fibre over `eta`.

### Theorem PP3bnw -- PROVED / EXACT HEAT-KERNEL CHARGE

For every clean signed output state over target cycle `eta`, the total incoming
transition mass from all clean source states containing `A` is exactly

```text
(K^t f_A)(eta).
```

Consequently the action charge is

```text
gamma_A(t)=||K^t f_A||_infinity.
```

#### Proof

Before using reversibility, the output column over `eta` has mass

```text
[1/v(eta)] sum_rho w_A(rho) K^t(rho,eta).
```

By detailed balance,

```text
v(rho)K^t(rho,eta)=v(eta)K^t(eta,rho).
```

Substitute `w_A(rho)=v(rho)f_A(rho)` into the column sum.  The factors
`v(eta)` cancel, leaving

```text
sum_rho K^t(eta,rho) f_A(rho)
 = (K^t f_A)(eta).
```

Taking the largest output column proves the charge identity. ∎

At `t=1`, optimizing over supported kernels recovers the weighted transport
viewpoint of `docs/324`.  For a fixed reversible kernel, all label merging is
already included in the heat operator.

## 5. Spectral and pointwise charge bounds

Write

```text
mu_cl(A)=sum_rho pi(rho)f_A(rho)
        =[sum_rho w_A(rho)]/V,
```

the probability of `A` under the uniform parity-clean signed measure.

Let `g` be the spectral gap of the lazy reversible kernel `K`, and let

```text
pi_min=min_rho pi(rho).
```

### Corollary PP3bnx -- PROVED / SPECTRAL CHARGE REDUCTION

For every `t>=0`,

```text
gamma_A(t)
 <= mu_cl(A)
    +(1-g)^t ||f_A-mu_cl(A)||_(2,pi)/sqrt(pi_min).
```

Moreover,

```text
||f_A||_(2,pi)^2 <= mu_cl(A)/2,
```

so the weaker explicit bound

```text
gamma_A(t)
 <= mu_cl(A)
    +(1-g)^t sqrt(mu_cl(A)/(2 pi_min))
```

also holds.

#### Proof

Lazy reversibility makes the nonconstant `L^2(pi)` operator norm of `K` at most
`1-g`.  Hence

```text
||K^t f_A-mu_cl(A)||_(2,pi)
 <= (1-g)^t ||f_A-mu_cl(A)||_(2,pi).
```

For any target cycle `eta`, point evaluation is bounded by the `L^2(pi)` norm
divided by `sqrt(pi(eta))`, which is at most division by `sqrt(pi_min)`.  Combine
this with PP3bnw.

Finally `0<=f_A<=1/2`, so `f_A^2<=f_A/2`.  Averaging under `pi` gives the second
claim. ∎

### Corollary PP3bny -- PROVED / POINTWISE MIXING ENDPOINT

If, for some `t` and `epsilon>=0`,

```text
K^t(rho,eta) <= (1+epsilon) pi(eta)
```

for every pair of clean cycles, then

```text
gamma_A(t) <= (1+epsilon) mu_cl(A).
```

#### Proof

Use the pre-reversibility column formula:

```text
[1/v(eta)] sum_rho w_A(rho)K^t(rho,eta)
 <= [(1+epsilon)pi(eta)/v(eta)] sum_rho w_A(rho)
 = (1+epsilon)mu_cl(A).
```

Take the largest output column. ∎

Thus pointwise mixing reaches the clean stationary flaw scale with no extra
label-merging loss.

## 6. Revised charge frontier

The weighted Hall and mixing formulations are now unified:

```text
one-step optimized transport:
  gamma_A^*=max_U w_A(U)/v(N(U));

t-step reversible clean walk:
  gamma_A(t)=||K^t f_A||_infinity.
```

The remaining problem is no longer the sign fibre or bookkeeping of rotation
labels.  It is a quantitative mixing theorem for the fibre-weighted clean-cycle
chain.  Concrete targets are:

1. prove a polynomial spectral gap for `K` on the asymptotically relevant clean
   component;
2. obtain a log-Sobolev, evolving-set, or direct pointwise estimate strong enough
   in the `t=Theta(log m)` trajectory window;
3. compare the stationary clean flaw probability `mu_cl(A)` with the uniform
   Hamilton atomic probability `Theta(m^-3)`;
4. prove that pair-safe clean preprocessing lands in a warm distribution for
   `pi`;
5. combine heat-kernel charge reduction with a signed-state implementation whose
   geometric light cone remains controlled.

The canonical kernel is verified to be irreducible only in the finite range
where clean connectivity has been audited.  No asymptotic gap or seed theorem is
proved here.
