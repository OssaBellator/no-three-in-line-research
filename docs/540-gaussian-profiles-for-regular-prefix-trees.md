# Gaussian profiles for regular prefix trees

`docs/534` gives exact unary/binary profile coefficients for legal prefix trees.
This chapter identifies the typical branching profile and its fluctuation scale.
The result turns an exact coefficient table into a probabilistic concentration
certificate for large legal marker-code families.

For the language avoiding `000`, mark binary nodes by `u`.  The bivariate
ordered-tree series is

```text
T(z,u)=z(1+T(z,u)+u T(z,u)^2).
```

Let `J_n` be the number of binary nodes in a uniformly chosen legal tree with
`n` leaves.

## 1. Moving dominant singularity

### Theorem PP3cmu -- PROVED / LEGAL-TREE QUASI-POWERS LAW

Near `u=1`, the dominant singularity is

```text
rho(u)=1/(1+2 sqrt(u)).
```

Consequently

```text
E J_n=n/3+O(1),
Var(J_n)=n/18+O(1),
```

and `(J_n-n/3)/sqrt(n/18)` converges in distribution to the standard normal law.

#### Proof

The smooth implicit schema becomes singular when
`1=T derivative_T(1+T+uT^2)`, giving `T=u^(-1/2)` and the displayed `rho(u)`.
The coefficient ratio

```text
[z^n]T(z,u)/[z^n]T(z,1)
```

has quasi-power exponential term `(rho(1)/rho(u))^n`.  Differentiating
`log((1+2 exp(t/2))/3)` at `t=0` gives mean coefficient `1/3` and variance
coefficient `1/18`.  The analytic quasi-powers theorem gives asymptotic
normality. ∎

## 2. Local central profile

### Theorem PP3cmv -- PROVED / LEGAL-TREE LOCAL GAUSSIAN PROFILE

Uniformly for integers `j=n/3+O(sqrt(n))`,

```text
P(J_n=j)=
(1/sqrt(2 pi n/18))
exp(-(j-n/3)^2/(2n/18)) (1+o(1)).
```

In particular, every fixed multiple of `sqrt(n)` captures a limiting Gaussian
fraction of the legal code family.

#### Proof

The bivariate algebraic function is analytic in a complex neighborhood of the
positive critical point and has an aperiodic square-root singularity.  Fourier
inversion of the uniform quasi-powers expansion gives the local limit theorem. ∎

## 3. Exact finite profile oracle

### Theorem PP3cmw -- PROVED / PROFILE MOMENT AND MODE CERTIFICATE

The exact coefficient with `j` binary nodes and
`a=n-1-2j` unary nodes is

```text
c_(n,j)=(n-1)!/(a! j! (j+1)!).
```

The ratio

```text
c_(n,j+1)/c_(n,j)=a(a-1)/((j+1)(j+2))
```

proves unimodality and locates every finite mode.  Exact sums of `j c_(n,j)` and
`j^2 c_(n,j)` certify the finite mean and variance.

#### Proof

The coefficient formula is the Lagrange coefficient from `docs/534`.  Dividing
successive terms gives the ratio; it decreases through one, proving unimodality.
The moment statements are finite integer sums. ∎

## 4. Stored exact fixture

The audit `scripts/check_regular_prefix_profile_clt.py` checks every profile
through 200 leaves.  At 30 leaves the two modes are nine and ten, each with count
`168212023980`.  At 200 leaves,

```text
E J_200 / 200  = 0.3304190104...,
Var(J_200)/200 = 0.0556932696...,
```

and the exact two-standard-deviation window contains approximately
`0.94950416` of all legal trees.

## 5. Prime-patching consequence

Large regular-language marker-code families are not merely exponentially
numerous: almost all legal trees have a predictable branching density with
`sqrt(n)` fluctuations.  This supports typical-case resource sizing while the
exact coefficient oracle still certifies every exceptional finite profile.
