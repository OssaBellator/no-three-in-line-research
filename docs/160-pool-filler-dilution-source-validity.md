# Pool-filler dilution for marked credited endpoints

PP3tk retains pool-local anchored-pair and inserted-triple mass as explicit
hypotheses. The guaranteed credited bank inside one controller pool has size only
`m^(19/40+o(1))`, which is below the scale at which the crude pool-local
rank-four estimate closes a trade using only credited endpoints.

The full controller pool is much larger: it has `N=m^(19/20+o(1))` endpoints.
Use it as a filler reservoir. Force one credited endpoint into a random
`b=m^kappa` subbank and choose the other endpoints from the full pool. The total
high-support source load summed over all possible marked endpoints is small enough
that almost every endpoint of a credited bank of size `m^(19/40)` is good when
`kappa<19/80`.

This closes pool-local high-support source validity for a resource-bank endpoint,
provided the selected filler block is already hard-unary clean and supports a
fixed-rank spread matching law. A predetermined captive star centre can still be
exceptional; its exceptional marked load becomes an explicit concentration
certificate.

## 1. Full-pool source pattern counts

Let a controller pool contain `N` tied endpoint indices. Retain the full-pool
high-support bounds PP3jj and PP3jk:

```text
P_4(N) = O(m D_m N^2),
Q_4(N) = O(N^3),
Q_5(N) = O(N^4),
Q_6(N) = O(N^5),
```

where `P_4` counts support-rank-four anchored pairs and `Q_h` counts inserted
collinear triples of endpoint-index support rank `h`.

For an endpoint index `c`, define:

```text
D_P(c) = number of P_4 patterns whose support contains c,
D_h(c) = number of Q_h patterns whose support contains c.
```

Counting support incidences gives

```text
sum_c D_P(c) = 4 P_4(N),
sum_c D_h(c) = h Q_h(N).
```

### Proposition PP3xp -- PROVED

The displayed incidence identities hold exactly when patterns are counted once by
their endpoint-index support.

#### Proof

A rank-four pair pattern contains four endpoint indices, and a rank-`h` triple
pattern contains `h`. Double-count pattern-index incidences. ∎

## 2. Random filler block through one marked endpoint

Fix `c` and choose a uniform `(b-1)`-subset of the other `N-1` pool endpoints.
Adjoin `c` to obtain a marked `b`-endpoint block.

Assume the prepared block supports a matching-state distribution with fixed-rank
cylinder bounds

```text
Pr(F selected) <= (K/b)^r
```

for every prescribed compatible set of `r<=3` inserted cells.

### Proposition PP3xq -- PROVED

The expected high-support source-invalid count is at most a fixed constant times

```text
L_b(c)
+ m D_m b^2/N^2
+ b/N + b^2/N + b^3/N,
```

where the marked-centre load is

```text
L_b(c)
=
K^2 D_P(c) b/N^3
+
K^3 [
  D_4(c)/N^3
  + D_5(c) b/N^4
  + D_6(c) b^2/N^5
].
```

#### Proof

A rank-four pair containing `c` requires three further indices, so its selection
probability is `O((b/N)^3)`; the matching pair then occurs with probability
`O(b^-2)`. This gives `O(D_P(c)b/N^3)`.

A rank-four pair not containing `c` contributes

```text
O(P_4(N)(b/N)^4 b^-2)
= O(m D_m b^2/N^2).
```

For a rank-`h` triple containing `c`, select `h-1` further indices and then pay the
rank-three matching probability. The contribution is

```text
O(D_h(c) b^(h-4)/N^(h-1)).
```

For a triple not containing `c`, PP3jk gives

```text
O(Q_h(N)(b/N)^h b^-3)
= O(b^(h-3)/N),
```

which yields the final three terms for `h=4,5,6`. ∎

## 3. Total marked-centre load

### Theorem PP3xr -- PROVED

Summed over all `N` possible marked endpoints,

```text
sum_c L_b(c)
=
O(m D_m b/N + 1 + b + b^2).
```

#### Proof

Insert the incidence identities PP3xp into the definition of `L_b(c)` and use the
full-pool bounds. The pair term is

```text
O(P_4(N)b/N^3)=O(m D_m b/N).
```

The rank-four, rank-five, and rank-six triple terms are respectively
`O(1)`, `O(b)`, and `O(b^2)`. ∎

This is a count of marked badness over the whole pool, not merely an average over
a preselected credited subset.

## 4. Slab-optimal exponent calculation

Use

```text
N = m^(19/20+o(1)),
H = m^(19/40+o(1)),
b = m^(kappa+o(1)),
```

where `H` is the credited resource-bank size in the pool.

### Corollary PP3xs -- PROVED

If

```text
0<kappa<19/80,
```

then

```text
sum_c L_b(c)=o(H).
```

Also the unmarked terms in PP3xq satisfy

```text
m D_m b^2/N^2
+ b/N+b^2/N+b^3/N
=o(1).
```

#### Proof

The marked-load exponents are

```text
1/20+kappa
and
2kappa,
```

both strictly below `19/40` when `kappa<19/80`. For the unmarked terms, the pair
exponent is `2kappa-9/10`, and the largest triple exponent is
`3kappa-19/20`; both are negative with substantial slack. ∎

The exponent `19/80` is the half-width of the credited bank and is stronger than
what the unmarked source terms alone require.

## 5. Almost every credited endpoint is source-light

Let `C` be any credited endpoint set of size at least `cH` for fixed `c>0`.

### Theorem PP3xt -- PROVED

For `kappa<19/80`, there is a sequence `eta_m -> 0` such that all but `o(H)`
endpoints `c in C` satisfy

```text
L_b(c) <= eta_m.
```

For each such endpoint, some marked filler block of size `b` has high-support
source-invalid expectation `o(1)` under its fixed-rank spread matching law.

#### Proof

Choose `eta_m` tending to zero slowly enough that

```text
sum_c L_b(c)/eta_m = o(H).
```

Markov's inequality and PP3xs leave only `o(H)` exceptional pool endpoints, hence
only `o(H)` exceptional credited endpoints. For every remaining centre, average
PP3xq over the filler choice and then choose one block no worse than its
expectation. ∎

No distributional assumption on the credited set inside the pool is needed.

## 6. Source-valid paid trade through a good endpoint

### Corollary PP3xu -- PROVED UNDER THE PREPARED-HOST HYPOTHESIS

Suppose a good credited endpoint `c` from PP3xt can be placed in a hard-unary-clean
pool-compatible block of size `b` whose state law has the fixed-rank spread bound.
If the expected Xi-insertion cost of that state law is below the guaranteed
removal credit by a fixed positive margin, then there is a source-admissible
pool-compatible trade moving `c` and strictly decreasing `Xi`.

#### Proof

The high-support source-invalid expectation is `o(1)` by PP3xt. Include the
low-support source diagnostics and normalized insertion cost in the same
nonnegative first-moment objective. The prepared-host hypothesis supplies their
required bounds. Apply the dynamic identity PP3kx. ∎

For a resource bank, almost every credited endpoint is eligible for this theorem.
For a star bank with a predetermined centre, failure means that specific centre
has marked source load bounded away from zero or the hard-unary/paid hypotheses
fail.

## 7. Revised pool-local source endpoint

### Corollary PP3xv -- PROVED

At the slab-optimal scales, pool-local high-support pair/triple mass is no longer
an independent obstruction for a positive-density credited resource bank.
Almost every credited endpoint admits a growing filler-diluted block with
vanishing high-support source expectation.

The remaining pool-compatible obstacles are:

1. hard-unary concentration preventing preparation of a spread block through the
   chosen endpoint;
2. unary or binary Xi-insertion weight comparable with its removal credit;
3. a predetermined captive star centre with exceptional marked source load;
4. low-support transition concentration tied to that centre.

Thus the global-to-pool gap survives only at marked exceptional centres or in paid
and hard-unary collateral, not across the whole credited resource bank.
