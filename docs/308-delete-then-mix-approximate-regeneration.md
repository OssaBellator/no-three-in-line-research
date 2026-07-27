# Delete-then-mix approximate regeneration for Hamilton flaws

The targeted moves from `docs/307` delete every present bad triple but cannot be
exact resampling oracles, by `docs/306`.  This chapter replaces exact one-step
restoration by a quantitative two-phase mechanism:

```text
delete the selected flaw, then run the reversible unconditioned chain.
```

The unconditioned chain has a polynomial spectral-gap lower bound.  After a
polynomial number of mixing steps, the output distribution is pointwise close
to the uniform signed Hamilton measure, and the standard flaw charge is within
a factor `1+epsilon` of the original flaw probability.

This is an approximate-regeneration interface, not a termination theorem.

## 1. A balanced lazy combined chain

Let `Omega_m` be the signed Hamilton state space.  Its size is

```text
N_m = 2^m (m-1)!.
```

Define `K_m` by the following one-step rule:

```text
probability 1/2: stay;
probability 1/4: choose one source uniformly and flip its orientation;
probability 1/4: choose one source triple uniformly, rotate successors,
                 and choose the three new signs uniformly.
```

### Proposition PP3bkd -- PROVED

`K_m` is lazy, irreducible, symmetric, and reversible for the uniform measure
`mu_m` on `Omega_m`.

#### Proof

The holding step gives laziness.  Every orientation flip is its own inverse.
Every successor rotation is inverted by the same source triple, and each old
three-bit pattern is one of the eight equally likely reverse choices.  Thus
transition probabilities are symmetric.

Irreducibility follows from PP3bkb: rotations connect all Hamilton cycles and
orientation flips connect all sign vectors over a fixed cycle.  Symmetry gives
uniform stationarity and reversibility. ∎

## 2. Adjacent transpositions form a comparison subchain

Anchor vertex zero in the Hamilton cycle.  The other `m-1` vertices form a
linear order.  Let `Q_m` be the lazy product-reference chain:

```text
probability 1/2: stay;
probability 1/4: flip a uniformly random sign bit;
probability 1/4: swap a uniformly random adjacent pair in the anchored order,
                 leaving all sign bits unchanged.
```

There are `m-2` adjacent swaps.

### Proposition PP3bke -- PROVED / SPECTRAL COMPARISON

Every adjacent-transposition edge of `Q_m` is a successor-rotation edge of
`K_m` with the three new signs chosen equal to their old values.  For every real
function `f` on `Omega_m`, their Dirichlet forms satisfy

```text
E_K(f,f) >= c_m E_Q(f,f),

c_m = (m-2)/[8 C(m,3)] = 3/[4m(m-1)].
```

Consequently

```text
gap(K_m) >= c_m gap(Q_m).
```

#### Proof

Suppose the anchored cyclic order contains

```text
... a, x, y, z ... .
```

The successor rotation on sources `{a,x,y}` changes the segment to

```text
... a, y, x, z ...,
```

so it performs the adjacent transposition of `x,y`.  Choosing the three fresh
signs equal to the old signs gives exactly the corresponding `Q_m` edge.

A sign-flip edge has probability `1/(4m)` in both chains.  An adjacent edge has
probability `1/[4(m-2)]` in `Q_m` and probability

```text
1/[4 C(m,3) 8]
```

in `K_m`.  Their ratio is `c_m`.  Summing squared edge differences proves the
Dirichlet inequality.  The variational characterization of spectral gap gives
the final statement. ∎

The adjacent-transposition embedding is exhaustively checked through `m=8` by

```bash
python scripts/check_hamilton_adjacent_transposition_embedding.py \
  experiments/hamilton-adjacent-transposition-embedding-audit.json
```

covering `34,404` adjacent swaps.

## 3. A polynomial spectral gap

The sign-flip chain on the `m`-cube has gap `2/m`.  The adjacent-transposition
shuffle on `m-1` labelled positions is the interchange process on a path.  By
the Caputo--Liggett--Richthammer theorem proving Aldous' spectral-gap
conjecture, its gap equals the one-particle path gap.  For the discrete chain
that chooses one of the `m-2` adjacent edges uniformly, this is

```text
lambda_AT(m) = 2[1-cos(pi/(m-1))]/(m-2).
```

Reference: P. Caputo, T. M. Liggett, and T. Richthammer, *Proof of Aldous'
spectral gap conjecture*, Journal of the American Mathematical Society 23
(2010), arXiv:0906.1238.

### Theorem PP3bkf -- PROVED

The reference chain satisfies

```text
gap(Q_m)
 = (1/4) min(2/m, lambda_AT(m)).
```

Therefore

```text
gap(K_m)
 >= [3/(16m(m-1))] min(2/m, lambda_AT(m))
 = Omega(m^-5).
```

#### Proof

`Q_m` is the sum of commuting kernels on the permutation and sign coordinates:

```text
Q_m = (1/2)I + (1/4)H_m + (1/4)A_m.
```

Tensor-product eigenfunctions show that its smallest nonzero spectral
difference is one quarter of the smaller component gap.  Apply PP3bke and the
displayed component gaps.  Since

```text
1-cos(pi/(m-1)) = Theta(m^-2),
```

`lambda_AT(m)=Theta(m^-3)`, and multiplication by `c_m=Theta(m^-2)` gives the
stated polynomial bound. ∎

The constants are deliberately explicit but not optimized.

## 4. Pointwise mixing

### Corollary PP3bkg -- PROVED

For every `0<epsilon<1`, if

```text
t >= gap(K_m)^(-1) [log N_m + log(1/epsilon)],
```

then uniformly for all states `x,y`,

```text
| K_m^t(x,y)/mu_m(y) - 1 | <= epsilon.
```

In particular, the required number of steps is

```text
O(m^6 log m + m^5 log(1/epsilon)).
```

#### Proof

For a lazy reversible chain with uniform stationary measure and spectral gap
`lambda`, the spectral expansion gives

```text
|K^t(x,y)/mu(y)-1| <= N_m (1-lambda)^t
                    <= N_m exp(-lambda t).
```

The displayed choice of `t` makes the right side at most `epsilon`.  Use
`log N_m=O(m log m)` and PP3bkf. ∎

## 5. Delete, then approximately regenerate

Let `A` be any bad-triple flaw.  Let `R_A` be any row-stochastic targeted kernel
that deletes `A` using the complete flaw rule from PP3bka: an orientation flip
for a two-owner flaw or a successor rotation for a three-owner flaw.

Define

```text
S_A = R_A K_m^t.
```

### Theorem PP3bkh -- PROVED / APPROXIMATE RESAMPLING

For `t` as in PP3bkg, an input distributed as `mu_m` conditioned on `A`, followed
by `S_A`, produces a distribution `nu_A` satisfying

```text
1-epsilon <= nu_A(y)/mu_m(y) <= 1+epsilon
```

for every state `y`.

Moreover, the standard uniform-measure flaw charge

```text
gamma_A
 = max_y sum_(x in A) S_A(x,y)
```

satisfies

```text
gamma_A <= (1+epsilon) mu_m(A).
```

#### Proof

After the deletion step, the state has some probability distribution `eta`.
PP3bkg applies uniformly to every starting state, so averaging its upper and
lower pointwise bounds against `eta` gives the displayed density comparison.

For the charge, PP3bkg gives

```text
K_m^t(z,y) <= (1+epsilon)/N_m
```

for all `z,y`.  Hence

```text
sum_(x in A) sum_z R_A(x,z)K_m^t(z,y)
 <= |A|(1+epsilon)/N_m
 = (1+epsilon)mu_m(A).
```

Take the maximum over `y`. ∎

Unlike an exact resampling oracle, the mixed output may contain `A` again, with
probability close to its stationary probability.  This recurrence is necessary
by PP3bju.

## 6. Revised resampling frontier

The oracle obstruction is no longer absolute.  Exact immediate restoration is
impossible, but targeted deletion followed by polynomial mixing gives
pointwise approximate restoration and near-optimal charges.

The remaining tasks are now sharper:

1. replace the static coordinate-overlap graph by a smaller causal or witness
   graph for delete-then-mix actions;
2. quantify how much mixing is actually needed between targeted deletions;
3. prove a flaw-walk or partial-rejection criterion using charges close to
   `mu_m(A)`;
4. exploit warm starts so that full worst-case `L-infinity` mixing is not paid
   after every deletion.

The coordinate-clique barrier from `docs/305` still defeats any analysis that
keeps all coordinate-sharing adjacencies.  The present theorem supplies a
regeneration mechanism, not the missing sparse causality theorem.  The
asymptotic seed theorem remains open.
