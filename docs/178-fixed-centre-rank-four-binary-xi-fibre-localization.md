# Fixed-centre rank-four binary Xi fibre localization

The single-cycle marked-filler endpoint leaves rank-four binary `Xi` weight as
the last unlocalized marked binary support rank. Its local geometry is exact. A
binary pattern on four endpoint indices consists of two vertex-disjoint directed
arcs. If its support contains the captive centre `c`, exactly one of those arcs is
the incoming or outgoing cycle arc at `c`; the other is a remote partner arc.

Conditioning on one centre arc therefore turns the entire rank-four contribution
of that role into one weighted partner fibre. The random marked block and
single-cycle law give an exact normalization for the fibre. A cheap fibre can be
absorbed into the existing paid first-moment criterion. If no cheap admissible
centre arc exists, almost every incoming and outgoing centre cell carries a heavy
partner fibre. A dyadic decomposition then yields either a large uniform partner
fan or one fixed rank-four pattern with concentrated multiplicity.

This chapter localizes rank four. It does not by itself convert the final partner
fan or high-multiplicity pattern; those feed the existing conditional binary-star,
Hall, candidate-line, and paid-collateral interfaces.

## 1. Disjoint-arc roles

Let a controller pool have endpoint indices `V`, with `|V|=N`, and fix `c in V`.
For distinct noncentre indices define the nonnegative weights

```text
gamma_in(r;u,v)
```

on the binary pattern

```text
r -> c,   u -> v,
```

and

```text
gamma_out(s;u,v)
```

on

```text
c -> s,   u -> v.
```

In both cases the three displayed noncentre indices are distinct. The weight
aggregates every rank-four binary `Xi` insertion incidence supported on the two
displayed arcs.

### Proposition PP3abv -- PROVED

Every rank-four binary `Xi` pattern whose endpoint-index support contains `c`
belongs to exactly one of the two displayed roles. Consequently

```text
D_B,4(c)
=
 sum_{r,u,v} gamma_in(r;u,v)
 +
 sum_{s,u,v} gamma_out(s;u,v),
```

where each sum is over distinct noncentre indices.

#### Proof

A binary permutation pattern consists of two compatible directed arcs. Support
rank four means that the two arcs use four distinct endpoint indices, so they are
vertex-disjoint. Exactly one arc contains `c`, and `c` is uniquely its head or its
tail. This gives the incoming or outgoing role and no pattern is counted twice.
∎

For an incoming centre arc and an outgoing centre arc write

```text
F_in(r)  = sum_{u,v} gamma_in(r;u,v),
F_out(s) = sum_{u,v} gamma_out(s;u,v).
```

These are the exact weighted partner-fibre masses.

## 2. Exact one-arc conditional law

Fix an incoming arc `r->c`. Choose a uniform `(b-2)`-subset of
`V\{r,c}`, adjoin `r,c`, and then choose a uniform directed Hamilton cycle on the
selected block conditioned on containing `r->c`. The outgoing case is transposed.

Put

```text
kappa_N,b = (b-3)/((N-2)(N-3)).
```

### Proposition PP3abw -- PROVED

For every `4<=b<=N`:

1. every selected block has exactly

   ```text
   (b-2)!
   ```

   directed Hamilton cycles containing the fixed centre arc;
2. over the joint random block and conditional cycle, every prescribed remote arc
   `u->v` disjoint from the fixed centre arc appears with probability exactly

   ```text
   kappa_N,b;
   ```
3. the expected rank-four fibre cost whose centre arc is fixed equals

   ```text
   kappa_N,b F_in(r)
   ```

   in the incoming case and `kappa_N,b F_out(s)` in the outgoing case.

#### Proof

Contract the fixed directed arc. There are `b-1` cyclic objects and hence
`(b-2)!` directed cyclic orders. A fixed remote arc requires both its endpoints in
the block, with probability

```text
(b-2)_2/(N-2)_2,
```

and, conditional on selection, has probability `1/(b-2)` under the one-arc
conditioned cycle law. Their product is

```text
(b-3)/(N-2)_2 = kappa_N,b.
```

Linearity of expectation gives the fibre-cost identities. ∎

Thus rank-four weight has an exact one-arc normalization, rather than only the
coarse `O(b/N^2)` estimate in the marked-load formula.

## 3. One-arc paid completion criterion

Fix a unary-source-admissible incoming centre arc `r->c`. Let `Q_r` be the exact
expected number of all remaining source-invalid canonical patterns in the random
block and conditional cycle. Let `J_r` be the exact expected `Xi` insertion cost
excluding the rank-four fibre whose centre arc is `r->c`. Let `R_c>0` be the exact
removal credit obtained by moving `c`.

Define `Q_s,J_s` analogously after conditioning on an outgoing arc `c->s`.

### Theorem PP3abx -- PROVED

A source-valid strict pool-compatible decrease exists if either

```text
Q_r + [kappa_N,b F_in(r)+J_r]/R_c < 1
```

for one admissible incoming arc, or

```text
Q_s + [kappa_N,b F_out(s)+J_s]/R_c < 1
```

for one admissible outgoing arc.

#### Proof

Average the nonnegative random variable

```text
number of source violations + insertion cost/R_c
```

over the relevant one-arc conditioned family. Proposition PP3abw supplies the
exact displayed rank-four contribution. An outcome with value below one has zero
source violations and insertion cost below `R_c`. Apply the pool-compatible
insertion-cost-minus-removal-credit identity PP3kx. ∎

The criterion separates one complete rank-four partner fibre from every residual
source and paid term.

## 4. Cheap fibre or near-complete heavy fibres

Let `I_c` and `O_c` be the unary-source-admissible incoming and outgoing centre
indices from PP3abg. Fix a positive local budget `lambda`.

Call an incoming fibre light when

```text
kappa_N,b F_in(r) < lambda,
```

and define light outgoing fibres identically.

### Proposition PP3aby -- PROVED

At least one of the following holds.

1. An admissible incoming centre arc has normalized rank-four fibre load below
   `lambda`.
2. An admissible outgoing centre arc has normalized rank-four fibre load below
   `lambda`.
3. Every admissible incoming and outgoing centre arc has normalized fibre load at
   least `lambda`.

If `d_U(c)=o(N)`, alternative 3 contains `N-o(N)` heavy incoming fibres and
`N-o(N)` heavy outgoing fibres.

#### Proof

The three alternatives are the exact partition according to whether either light
set is nonempty. The final statement uses PP3abg, which gives
`|I_c|,|O_c|=N-o(N)`. ∎

Under alternatives 1 or 2, PP3abx leaves only residual conditioned source or paid
concentration. Alternative 3 is a near-complete family of heavy conditional
binary-star fibres.

## 5. Dyadic support or multiplicity inside one fibre

Let one heavy fibre have positive partner-arc weights `w_e`, total mass

```text
F=sum_e w_e,
```

and maximum weight `w_max`. Put

```text
L=ceil(log_2(1+w_max)).
```

For `0<=j<L`, let

```text
E_j={e: 2^j <= w_e < 2^(j+1)}.
```

### Proposition PP3abz -- PROVED

Some dyadic level satisfies

```text
2^j |E_j| >= F/(2L).
```

Consequently, for every integer target `q>=1`, one of the following holds.

1. **Uniform partner fan:** one level contains at least `q` distinct partner arcs,
   each with weight in one common dyadic interval.
2. **Multiplicity core:** one fixed partner arc has weight strictly greater than

   ```text
   F/(2Lq).
   ```

#### Proof

Since every weight in `E_j` is below `2^(j+1)`,

```text
F < 2 sum_j 2^j |E_j|.
```

One of the `L` summands is therefore at least `F/(2L)`. If its level size is at
least `q`, use alternative 1. Otherwise `|E_j|<q`, so

```text
2^j > F/(2Lq),
```

and every member of that nonempty level gives alternative 2. ∎

A uniform partner fan is exactly one endpoint-cell fibre `P(a)` in the
conditional binary-resource-star interface PP3wv--PP3xc. The multiplicity
alternative is a fixed pair of disjoint inserted cells carrying concentrated
rank-four `Xi` incidence weight.

## 6. Slab-optimal consequence

Use

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80,
W=m^(19/40+o(1)).
```

Then

```text
kappa_N,b=(1+o(1))b/N^2.
```

### Corollary PP3aca -- PROVED

A fibre with normalized load at least `lambda` has raw weight

```text
F >= (1-o(1)) lambda N^2/b.
```

Taking `q=W` in PP3abz yields either:

1. a fixed centre cell with at least `W` distinct remote partner arcs in one
   dyadic weight level; or
2. one fixed rank-four binary pattern of weight

   ```text
   Omega(lambda N^2/(bWL)).
   ```

If all pattern weights are polynomially bounded in `m`, then `L=m^(o(1))` and the
multiplicity scale is

```text
lambda m^(57/40-kappa-o(1)).
```

#### Proof

Invert the exact normalization in PP3abw and apply PP3abz with `q=W`. The exponent
identity is

```text
2(19/20)-19/40 = 57/40.
```

Polynomial weight bounds give `L=O(log m)=m^(o(1))`. ∎

The partner-fan alternative already has the marked-bank target size. The other
alternative is no longer diffuse: one exact disjoint-arc pattern carries the
large multiplicity.

## 7. Revised rank-four binary endpoint

### Corollary PP3acb -- PROVED

At a source-light captive centre, the rank-four binary `Xi` alternative reduces
to one of:

1. a source-admissible incoming or outgoing centre arc with rank-four fibre load
   below the available local budget, followed by the one-arc paid criterion
   PP3abx;
2. residual source or lower/higher paid concentration after fixing such an arc;
3. a near-complete family of heavy incoming and outgoing partner fibres;
4. a target-size uniform endpoint-cell partner fan inside one heavy fibre;
5. one fixed rank-four disjoint-arc pattern with concentrated `Xi` multiplicity.

Thus an arbitrary rank-four binary support table is no longer an independent
frontier. The remaining rank-four objects are conditional partner fans,
conditioned collateral, or one exact high-multiplicity pattern.

## 8. Finite diagnostic

The script

```text
scripts/check_rank_four_binary_xi_fibres.py
```

checks a finite weighted instance. It verifies the disjoint-arc input, computes
the exact normalization `(b-3)/((N-2)(N-3))`, finds a cheap admissible fibre or
certifies that every admissible incoming and outgoing fibre is heavy, and checks
the dyadic partner-fan/multiplicity dichotomy. For small instances it enumerates
all random-block conditional Hamilton cycles and verifies both the exact state
count and the expected fibre-cost identity.
