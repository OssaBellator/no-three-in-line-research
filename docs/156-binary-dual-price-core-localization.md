# Binary dual price-core localization

PP3wn uses only the support size of a linear binary dual packing. The dual prices
carry more information. For each endpoint resource, sum the dual weight of all
conflicts touching it. Cell feasibility bounds this incident weight by the
resource price times `q`, plus the total price on the opposite resource side.

After removing high-incident resources, a weighted greedy algorithm extracts a
large resource-disjoint conflict matching. Therefore a linear dual value gives
either a large rectangle bank or a sublinear high-price resource core carrying a
positive fraction of the dual mass.

## 1. Incident dual weight

Retain the feasible dual variables of PP3le and put

$$
Y = sum_B y_B.
$$

For an endpoint resource `v`, define

$$
I_v = sum_{B touching v} y_B,
$$

where a conflict is counted once for `v`. Every binary conflict touches exactly
four distinct endpoint resources.

### Proposition PP3wo -- PROVED

One has

$$
sum_v I_v = 4Y.
$$

#### Proof

Exchange the order of summation. Every conflict contributes its weight once to
each of its four resources. ∎

## 2. Resource incidence is controlled by price

### Proposition PP3wp -- PROVED

For every endpoint resource `v`,

$$
I_v <= q lambda_v + 1.
$$

More precisely, the final `1` may be replaced by the total price on resources of
the opposite bipartition.

#### Proof

Suppose `v` is a left resource; the right-resource proof is transposed. Sum the
cell constraints

$$
sum_{B containing a} y_B <= lambda_v + lambda_right(a)
$$

over all endpoint cells `a` incident with `v`. Each conflict touching `v`
contains exactly one such cell, so the left side is `I_v`. There are at most `q`
such cells, and the sum of their opposite-resource prices is at most the total
dual price, which is at most one. ∎

Hence a resource carrying incident dual weight `K` has price at least
`(K-1)/q`.

## 3. Weighted greedy matching outside a price core

Fix a threshold `K>0` and put

```text
H_K = {v : I_v > K}.
```

Let `Y_0` be the total dual weight of conflicts avoiding every resource in
`H_K`.

### Theorem PP3wq -- PROVED

The conflicts avoiding `H_K` contain a resource-disjoint matching of size at
least

$$
Y_0/(4K).
$$

#### Proof

Greedily select any remaining positive-weight conflict and delete every conflict
sharing one of its four resources. Since every selected resource has incident
weight at most `K`, one step deletes total dual weight at most `4K`. To remove
initial weight `Y_0`, at least `Y_0/(4K)` selections are required. ∎

The selected conflict weights themselves need not be comparable; the theorem
uses deleted total weight to lower-bound the number of disjoint supports.

## 4. Size of the high-price core

### Proposition PP3wr -- PROVED

For `K>1`,

$$
|H_K| < q/(K-1).
$$

#### Proof

PP3wp gives `lambda_v > (K-1)/q` for every `v in H_K`. Sum over `H_K` and use
`sum_v lambda_v <= 1`. ∎

Thus high incident dual weight can occur only on a small resource set.

## 5. Square-root dichotomy

Assume

$$
Y >= rho q
$$

for fixed positive `rho`. Take

```text
K = sqrt(q),
s = rho sqrt(q)/8.
```

### Corollary PP3ws -- PROVED

At least one of the following holds for all sufficiently large `q`.

1. There is a resource-disjoint binary-conflict matching of size at least
   
   $$
   rho sqrt(q)/8.
   $$
2. A set of at most
   
   $$
   (1+o(1)) sqrt(q)
   $$
   
   endpoint resources meets conflicts of total dual weight at least
   
   $$
   rho q/2.
   $$

#### Proof

Let `H=H_K`. If conflicts avoiding `H` have weight at least `rho q/2`, PP3wq
gives a disjoint matching of size at least

$$
(rho q/2)/(4 sqrt(q)) = rho sqrt(q)/8.
$$

Otherwise conflicts touching `H` carry more than half the total lower bound.
Proposition PP3wr gives the resource-set size. ∎

The second alternative is a weighted endpoint-resource core, not merely a
single high-degree support vertex.

## 6. One resource inside the price core

### Corollary PP3wt -- PROVED

In alternative 2 of PP3ws, some resource in the high-price core is incident with
dual weight at least

$$
Omega(sqrt(q)).
$$

#### Proof

Assign every conflict touching the core to one of its core resources. There are
`O(sqrt(q))` resources and total assigned weight `Omega(q)`. Pigeonhole. ∎

By PP3wp that resource has price `Omega(q^(-1/2))`.

## 7. Revised weighted binary endpoint

### Corollary PP3wu -- PROVED

A linear binary-congestion dual packing yields one of:

1. an `Omega(sqrt(q))` resource-disjoint conflict matching, hence the alternating
   rectangle/unary alternatives of PP3wk--PP3wm;
2. an `O(sqrt(q))` high-price endpoint-resource core carrying `Omega(q)` dual
   weight;
3. one resource in that core carrying `Omega(sqrt(q))` incident dual weight.

Thus the hard binary branch reduces to paid installation of a growing rectangle
bank or conversion of a polynomial weighted resource star. Diffuse fractional
dual mass is no longer an open case.