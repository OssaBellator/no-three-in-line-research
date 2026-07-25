# Marked pool dilution for unary source obstruction

PP3ya makes almost every endpoint of a credited resource bank light for anchored
transitions and all high-support source classes. The remaining source-validity
condition is the unary forbidden endpoint graph on the marked filler block.

For a fixed marked endpoint `c`, a forbidden arc containing `c` needs one further
selected endpoint and then one matching edge. Its expected contribution is
proportional to the full-pool unary degree of `c` divided by the full pool size.
Unmarked unary arcs contribute their global density times the filler-block size.
Thus adaptive filler size closes unary source validity at every endpoint of
sublinear full-pool unary degree.

If no credited endpoint is unary-light, the obstruction is highly structured:
linearly many distinct tied resources each have linear unary degree. Because the
credited bank is much smaller than the full pool, Hall extracts a resource-
disjoint unary matching of the same order.

## 1. Full-pool unary support

Let the full controller pool have `N` tied endpoint indices. Let `F_2` be the
family of unary-forbidden candidate cells with endpoint-index support size two,
and let

```text
U_2=|F_2|,
theta=U_2/N^2.
```

Support-rank-one diagonal cells are separated; a derangement never selects them,
and in a general spread law their total contribution is `O(1/b)`.

For an endpoint index `c`, let `d_U(c)` be the number of cells of `F_2` whose
support contains `c`.

### Proposition PP3yc -- PROVED

```text
sum_c d_U(c)=2U_2.
```

#### Proof

Every support-rank-two unary cell contains exactly two endpoint indices. ∎

## 2. Marked unary expectation

Fix `c`, choose a uniform `(b-1)`-subset of the other pool endpoints, and assume
the prepared block has one-edge cylinder probability at most `K/b`.

### Proposition PP3yd -- PROVED

The expected number of selected support-rank-two unary cells is at most a fixed
constant times

```text
U_b(c) + theta b,
```

where

```text
U_b(c)=K d_U(c)/N.
```

#### Proof

A forbidden cell containing `c` needs its other support index selected, with
probability `O(b/N)`, and then its matching edge, with probability `O(1/b)`. This
gives `O(d_U(c)/N)`.

A forbidden cell not containing `c` needs two selected indices and one matching
edge, contributing

```text
O(U_2 (b/N)^2 b^-1)=O(theta b).
```

∎

## 3. Adaptive filler size

Assume `theta=o(1)`. Let `b_max=m^(kappa+o(1))` with fixed
`0<kappa<19/80`.

### Proposition PP3ye -- PROVED

There is a sequence

```text
b -> infinity,
b <= b_max,
theta b -> 0.
```

For this choice, every marked endpoint satisfying

```text
d_U(c)=o(N)
```

has unary expectation `o(1)`.

#### Proof

Choose `b` to grow more slowly than both `b_max` and `theta^(-1/2)`. Apply PP3yd.
∎

The slower adaptive choice only improves all high-support and transition bounds in
PP3xq and PP3xx.

## 4. Fully source-light credited endpoints

Let `C` be a credited endpoint bank of size

```text
H=m^(19/40+o(1))
```

inside a full pool of size

```text
N=m^(19/20+o(1)).
```

Let `C_good` be the `H-o(H)` endpoints supplied by PP3ya.

### Theorem PP3yf -- PROVED

If `C_good` contains an endpoint `c` with `d_U(c)=o(N)`, then one adaptive marked
filler block through `c` has total source-invalid expectation `o(1)` for:

1. unary forbidden cells;
2. anchored transitions;
3. support-rank-four anchored pairs;
4. inserted triples of support rank four, five, and six;
5. the universal transposition and directed-triangle classes.

Hence the block supports a source-valid pool-compatible state under the prepared
fixed-rank spread law.

#### Proof

Use PP3ye for unary cells, PP3ya for transitions and high-support classes, and the
universal `O(1/b)` bounds for the remaining low-support events. Add all nonnegative
objectives before choosing the filler block. Apply PP3ix or the corresponding
first-moment/LLL distribution theorem. ∎

Thus a single unary-light credited endpoint removes every pool-local source-mass
hypothesis.

## 5. Failure forces many linear unary degrees

Suppose no sequence of endpoints from `C_good` has `d_U(c)=o(N)`.

### Proposition PP3yg -- PROVED

After passing to a subsequence, there is a fixed `rho>0` such that at least
`(1-o(1))H` credited endpoints satisfy

```text
d_U(c)>=rho N.
```

After pigeonholing left versus right typed incidence, there is a set `S` of
`Omega(H)` distinct typed endpoint resources on one bipartition side, each having
unary-forbidden degree at least `rho N/2`.

#### Proof

If the minimum normalized unary degree on `C_good` tended to zero, choosing a
minimum-degree endpoint would contradict the hypothesis. Hence it is bounded below
along a subsequence. Each endpoint has two typed resources, so one side carries at
least half of its support degree. Pigeonhole the side. Tied matching endpoints
have distinct left resources and distinct right resources. ∎

## 6. Hall extraction of a unary resource matching

### Theorem PP3yh -- PROVED

The unary support incident with `S` contains a matching of endpoint cells
saturating `S` for all sufficiently large `m`. In particular, it contains a
resource-disjoint unary-forbidden cell bank of size `Omega(H)`.

#### Proof

Let `h=|S|=O(H)`. Every resource in `S` has at least `rho N/2` forbidden neighbours
on the opposite side. Since

```text
H/N=m^(-19/40+o(1))=o(1),
```

one has `rho N/2>h` for large `m`.

For every nonempty subset `X subseteq S`, its neighbourhood contains the
neighbourhood of any one member and therefore has size at least `rho N/2>h>=|X|`.
Hall's theorem gives a matching saturating `S`. ∎

The matching uses distinct resources on both sides and is therefore the exact
unary resource-bank input of PP3kh and PP3wg.

## 7. Witness localization of the unary matching

Choose one retained-source witness pair for every matched forbidden cell.

### Corollary PP3yi -- PROVED

The unary matching from PP3yh yields one of:

1. a source point contained in polynomially many witness pairs, giving source-star
   removal credit;
2. a polynomial vertex-disjoint witness-pair matching, giving a resource-disjoint
   credited endpoint bank;
3. concentrated paid insertion collateral for the corresponding star/resource
   trade.

#### Proof

Apply the witness star/matching dichotomy PP3we and the endpoint extraction PP3wf
--PP3wg. ∎

## 8. Revised pool-compatible source endpoint

For a large credited resource bank inside one controller pool, pool-local source
validity now has an exact alternative.

1. A unary-light credited endpoint exists, and PP3yf supplies a fully source-valid
   filler-diluted block through it.
2. There is an `Omega(H)` unary-forbidden resource matching, which rejoins the
   source-star/resource-bank conversion branch.
3. A predetermined captive star centre may remain exceptional even though almost
   every resource-bank endpoint is source-light.

Pool-local pair, triple, transition, and diffuse unary mass are no longer separate
obstructions for the resource-bank branch.
