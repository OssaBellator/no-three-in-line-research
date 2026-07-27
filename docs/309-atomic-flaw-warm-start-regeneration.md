# Atomic flaw warm starts and faster total-variation regeneration

The worst-case pointwise regeneration theorem in `docs/308` starts from an
arbitrary signed Hamilton state and therefore pays `log |Omega_m|=Theta(m log
m)`.  A targeted deletion output is much warmer than an arbitrary point mass.
This chapter computes its exact density and removes that extra factor for
total-variation restoration.

The result does not improve the pointwise charge bound from PP3bkh.  It gives a
faster approximate-regeneration interface for coupling, recurrence, and
warm-start flaw-walk arguments.

## 1. Atomic Hamilton flaws

An atomic bad-triple flaw records:

1. the three selected collinear cells; and
2. the signed pair assignments owning those cells.

By PP3bjy, it has either two or three owners.  In a Hamilton pair cycle, any
proper subset of two or three cycle edges is a directed path forest.

### Proposition PP3bki -- PROVED

Under the uniform signed Hamilton measure, every compatible atomic flaw has
probability

```text
two owners:   p_2(m) = 1/[4(m-1)_2],
three owners: p_3(m) = 1/[8(m-1)_3].
```

#### Proof

A two-owner atomic flaw fixes two signed nonloop pair assignments.  Their
unsigned edges form a directed path forest, so PP3bjc with `r=2` gives

```text
1/[2^2(m-1)_2].
```

Likewise, a three-owner flaw fixes three signed cycle edges.  Since `m>=4`,
those three edges cannot form the complete Hamilton cycle and hence form a path
forest.  PP3bjc with `r=3` gives the second formula. ∎

## 2. Exact deletion images

For a two-owner flaw, choose either owner uniformly and flip its orientation.
For a three-owner flaw, apply the successor rotation and choose the three fresh
signs uniformly.

### Proposition PP3bkj -- PROVED / EXACT WARMNESS

For a fixed atomic flaw `A`:

1. every deletion output lies outside `A`;
2. the labelled deletion map is injective;
3. the two-owner deletion output is uniform on `2|A|` states;
4. the three-owner deletion output is uniform on `8|A|` states.

Consequently the output density relative to the uniform measure is bounded
exactly by

```text
M_2(m) = 1/[2p_2(m)] = 2(m-1)(m-2),
M_3(m) = 1/[8p_3(m)] = (m-1)(m-2)(m-3).
```

#### Proof

Guaranteed deletion is PP3bjz in the two-owner case and PP3bjk in the
three-owner case.

For two owners, fix the deletion label specifying which owner is flipped.  The
output uniquely determines the input by applying the same involution.  Outputs
from the two different labels cannot coincide: such a common output would have
to agree with the flaw signs at each owner for one inverse and disagree at the
same owner for the other inverse.

For three owners, the output and the fixed source triple uniquely determine the
inverse successor rotation.  The atomic flaw fixes the old three signs, while
the output records the fresh three signs.  Thus the labelled input is unique.

A uniform input on `A` and a uniform deletion label therefore give a uniform
distribution on the displayed number of distinct outputs.  Divide the point
mass `1/[q|A|]` by the uniform state mass `1/|Omega_m|`, using
`p_r=|A|/|Omega_m|`. ∎

The exact finite audit through `m=6` is run by

```bash
python scripts/check_hamilton_atomic_flaw_warmness.py \
  experiments/hamilton-atomic-flaw-warmness-audit.json
```

It checks `10,416` atomic flaws, every cylinder size, every deletion image, and
maximum output multiplicity one.

## 3. Warm-start spectral contraction

Let `K_m` be the lazy reversible combined chain from PP3bkd and write

```text
lambda_m = gap(K_m) = Omega(m^-5).
```

A distribution `nu` is `M`-warm relative to `mu_m` when

```text
nu(x) <= M mu_m(x)
```

for every state.

### Theorem PP3bkk -- PROVED

If `nu` is `M`-warm, then

```text
|| nu K_m^t - mu_m ||_TV
 <= (1/2) sqrt(M-1) exp(-lambda_m t).
```

#### Proof

Put `f=nu/mu_m`.  Warmness and `E_mu f=1` give

```text
chi^2(nu||mu_m)
 = E_mu[(f-1)^2]
 = E_mu[f^2]-1
 <= M E_mu[f]-1
 = M-1.
```

Reversibility and the spectral gap contract the mean-zero density in `L^2`:

```text
||K_m^t(f-1)||_2 <= (1-lambda_m)^t ||f-1||_2.
```

Finally `TV <= (1/2)L^1 <= (1/2)L^2` and
`(1-lambda_m)^t<=exp(-lambda_m t)`. ∎

## 4. Faster delete-then-mix regeneration

### Corollary PP3bkl -- PROVED / WARM-START REGENERATION

After deleting one atomic flaw, total-variation distance at most `epsilon` from
the uniform signed Hamilton measure is reached once

```text
t >= lambda_m^(-1)
     [ (1/2)log(M_r(m)-1) + log(1/(2epsilon)) ].
```

For either owner count this is

```text
O(m^5[log m + log(1/epsilon)]).
```

In particular, choosing `epsilon=p_r(m)` gives regeneration in

```text
O(m^5 log m)
```

steps and makes the probability that the deleted flaw has recurred at most

```text
2p_r(m).
```

#### Proof

Apply PP3bkk with the exact warmness from PP3bkj.  Both warmness values are
polynomial in `m`, so their logarithms are `O(log m)`.  Total variation controls
the probability of every event, including recurrence of the deleted flaw:

```text
Pr(A after mixing) <= mu_m(A)+epsilon.
```

Set `epsilon=p_r(m)`. ∎

## 5. Revised warm-start frontier

The delete-then-mix mechanism now has two quantitative forms:

1. worst-case `L-infinity` regeneration and near-optimal pointwise charge in
   `O(m^6 log m)` steps by PP3bkh;
2. atomic-deletion warm-start total-variation regeneration in `O(m^5 log m)`
   steps by PP3bkl.

The remaining challenge is to avoid paying even this polynomial mixing cost
after every flaw.  Natural next targets are:

1. prove that a sequence of local deletions remains polynomially warm;
2. interleave only enough unconditioned steps to control accumulated density;
3. formulate a witness-sequence theorem tolerating total-variation rather than
   pointwise regeneration;
4. exploit the exact injective deletion images in a partial-rejection analysis.

No asymptotic seed existence or termination theorem is claimed.
