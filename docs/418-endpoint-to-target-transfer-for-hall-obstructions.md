# Endpoint-to-target transfer for Hall obstructions

`docs/412` converts a failed finite-depth Hall certificate into many distinct
raw-congestion sources unless the backward walks merge heavily. Raw congestion
itself is a capacity-weighted average of target multiplicity. This chapter
pushes the obstruction one step further: endpoint mass on bad sources becomes
positive mass on highly reused targets.

The statements are general. They do not classify the resulting targets in the
prime-patching transport graph.

## 1. The endpoint-target sampling law

Fix a source subset `U`, target capacities `v(y)>0`, and

```text
D(x)=sum_(y in N(x)) v(y),
n_U(y)=#{x in U:y in N(x)}.
```

The raw source ratio is

```text
r_0(x)=sum_(y in N(x)) v(y)n_U(y)/D(x).
```

Let `mu` be any probability distribution on `U`. Sample `X~mu`, then sample a
target from `N(X)` by

```text
P(Y=y|X=x)=v(y)/D(x).
```

### Proposition PP3bys -- PROVED / EXACT ENDPOINT-TARGET EXPECTATION

The sampling law satisfies

```text
E[n_U(Y)|X=x]=r_0(x)
```

and therefore

```text
E[n_U(Y)]=sum_x mu(x)r_0(x).
```

#### Proof

Expand the conditional expectation using the target sampling probabilities.
Averaging over `X` gives the second identity. ∎

Thus the final step of a backward Hall walk may be followed by one capacity-
weighted incidence to obtain a literal target-column obstruction.

## 2. Threshold transfer

Let

```text
H_theta={x:r_0(x)>theta}
```

and suppose `mu(H_theta)>=p`. Condition `mu` on `H_theta` and use the target law
above. Put

```text
M=max_y n_U(y).
```

### Theorem PP3byt -- PROVED / HIGH-TARGET MASS FROM HIGH ENDPOINTS

For every `phi<theta<=M`, the conditional target law satisfies

```text
P(n_U(Y)>phi | X in H_theta)
 >=(theta-phi)/(M-phi).
```

Under the original unconditioned law,

```text
P(X in H_theta and n_U(Y)>phi)
 >=p(theta-phi)/(M-phi).
```

In particular, some target reached from a high endpoint has multiplicity
strictly greater than `theta`.

#### Proof

Conditioned on `H_theta`, the expectation of `n_U(Y)` is greater than `theta` by
`PP3bys`. If `a` is the probability of the event `n_U(Y)>phi`, then

```text
E[n_U(Y)]<=phi(1-a)+Ma.
```

Rearranging gives the first bound. Multiply by `p` for the joint event. The
last statement follows directly from an average greater than `theta`. ∎

## 3. Distinct target localization

Let `nu` be the subprobability measure on targets defined by

```text
nu(y)=P(X in H_theta,Y=y,n_U(y)>phi).
```

Write

```text
m=sum_y nu(y),
chi_T=sum_y nu(y)^2,
beta_T=max_y nu(y).
```

### Theorem PP3byu -- PROVED / TARGET-HUB COUNT OR TARGET MERGING

The number of targets with positive `nu`-mass obeys

```text
|supp(nu)|>=m^2/chi_T
```

and

```text
|supp(nu)|>=m/beta_T.
```

Combining with `PP3byt`, one may take

```text
m>=p(theta-phi)/(M-phi).
```

Hence a persistent Hall obstruction has one of two target-side forms:

1. many distinct targets of multiplicity greater than `phi`; or
2. a large collision atom or collision energy concentrated on a few such
   targets.

#### Proof

Cauchy--Schwarz gives

```text
m^2<=(number of positive atoms) chi_T.
```

Also `m<=|supp(nu)| beta_T`. Insert the mass lower bound from `PP3byt`. ∎

## 4. Revised Hall frontier

The finite-depth obstruction chain is now

```text
failed Collatz ratio
 -> backward bad endpoints
 -> many raw-congestion sources or path merging
 -> many high-multiplicity targets or target merging.
```

The remaining geometric audit can therefore focus on bounded-depth source paths
feeding a small target hub, or on a dispersed family of high-multiplicity target
columns.

## 5. Exact diagnostic

Run

```bash
python scripts/check_hall_endpoint_target_transfer.py
```

The checker uses exact rational capacities and an exact endpoint law to verify
the expectation, threshold transfer, and target collision bounds.

The next theorem identifier after this chapter is `PP3byv`.
