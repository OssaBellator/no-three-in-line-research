# Locality--charge endpoint tradeoff for Hamilton flaw actions

`docs/311` proves that immediate deletion causality is only `O(n^2 log n)`, and
`docs/308` proves that sufficiently mixed deletion actions have charge close to
the stationary flaw probability.  These two gains do not occur at the same
endpoint.  This chapter records the exact action charges and the loss of
locality after full mixing.

The result isolates an intermediate-time interpolation problem rather than
claiming a new obstruction to every possible flaw-walk theorem.

## 1. Exact immediate deletion charges

For an atomic flaw `A`, use the uniform-measure action charge

```text
gamma_A(R)
 = max_y sum_(x in A) R(x,y).
```

### Proposition PP3ble -- PROVED

For the uniform labelled deletion kernels from PP3bkj,

```text
two-owner flaw:   gamma_A = 1/2,
three-owner flaw: gamma_A = 1/8.
```

#### Proof

PP3bkj proves that the labelled deletion maps are injective.  Every two-owner
input has two equiprobable outputs and every three-owner input has eight.
Therefore every output column receives either zero mass or exactly `1/2` or
`1/8`, respectively. ∎

These charges are constant, whereas the stationary atomic flaw probabilities
are `Theta(n^-2)` and `Theta(n^-3)`.  Immediate geometric locality alone does
not restore the probability-scale charges used by standard resampling analyses.

## 2. Full mixing makes causality global

Let `K_m` be the lazy connected combined chain from PP3bkd and consider the
delete-then-mix action

```text
S_A^(t) = R_A K_m^t.
```

### Proposition PP3blf -- PROVED

Once `t` is at least the diameter of the state graph, every state has positive
transition probability from every deletion output.  Consequently the possible
causal neighborhood of `S_A^(t)` contains every atomic flaw.

For three-owner flaws, this full family has size

```text
Theta(n^4 log n).
```

#### Proof

Connectedness gives a path of length at most the diameter between any two
states.  Laziness pads a path to every larger time, so all transition entries
are positive.  Any state containing any chosen atomic flaw is therefore a
possible output.

PP3bje supplies `Theta(n^4 log n)` strongly generic three-owner flaws, and the
total number of geometric collinear triples gives the matching upper order. ∎

Thus full mixing recovers near-stationary charges but discards deterministic
causal sparsity.

## 3. The two endpoints

### Corollary PP3blg -- PROVED / FRONTIER SHARPENED

For residual three-owner flaws after parity preprocessing:

1. at `t=0`, immediate causal outdegree is `O(n^2 log n)` by PP3bks, but action
   charge is `1/8` by PP3ble;
2. after full pointwise mixing, charge is `(1+o(1))Theta(n^-3)` by PP3bkh, but
   possible causality is the full `Theta(n^4 log n)` flaw family by PP3blf;
3. multiplying the fully mixed endpoint scales recovers `Theta(n log n)`.

Hence neither endpoint simultaneously exposes the favorable residual
probability--locality product

```text
Theta(n^-3) * O(n^2 log n) = O(log n/n).
```

#### Proof

Combine the cited charge and causality statements. ∎

The missing estimate must interpolate between the endpoints.  Useful targets
include functions `gamma(t)` and `D(t)` controlling charge contraction and a
probabilistic or weighted causal light cone after `t` mixing steps, with a
criterion such as

```text
gamma(t) D(t) = o(1)
```

or an appropriate cluster/witness analogue.

A purely possible-reachability definition of `D(t)` becomes global quickly;
therefore likely or weighted causality may be essential.  The asymptotic seed
theorem remains open.
