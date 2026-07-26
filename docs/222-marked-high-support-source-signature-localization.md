# Marked high-support source signatures: exact avoidance and sunflower localization

After the unary, transition, and dynamic-`Xi` conversions through PP3amq, the
unconverted terms in the exceptional marked-centre certificate PP3zd are the four
high-support source classes:

1. rank-four anchored pairs;
2. rank-four inserted triples;
3. rank-five inserted triples;
4. rank-six inserted triples.

Their thresholds are not ad hoc.  For a positive source-invalid signature of
endpoint rank `h` requiring `r` prescribed directed arcs, conditioning on the
marked endpoint gives the exact probability

```text
(b-1)_(h-1) / ((N-1)_(h-1) (b-1)_r).
```

This chapter uses that identity to avoid sparse positive support regardless of
witness multiplicity.  Dense support becomes a simple uniform link hypergraph.
A recursive star--matching theorem then produces a fixed-resource sunflower or a
resource-disjoint signature bank far larger than the target width.

The final sunflower/bank remains a source-host conversion interface; this chapter
does not assert that every dense source-signature hypergraph has a paid trade.

## 1. Distinct positive source signatures

Let a tied endpoint pool have `N` indices, fix a marked index `c`, and choose a
uniform `(b-1)`-subset of the other indices followed by a uniform single-cycle
state on the selected block.  Assume `b>=6`.

Count each positive source-invalid arc signature once, irrespective of the number
of retained-source witnesses certifying it.  Write

```text
S_P(c) = distinct rank-four anchored-pair signatures,
S_4(c) = distinct rank-four inserted-triple signatures,
S_5(c) = distinct rank-five inserted-triple signatures,
S_6(c) = distinct rank-six inserted-triple signatures.
```

Every signature contains `c` in one fixed typed role after finite role
pigeonholing.

### Proposition PP3amr -- PROVED

For a compatible signature that contains no proper directed cycle, the exact
conditioned selection probabilities are

```text
p_P = (b-3)/((N-1)(N-2)(N-3)),

p_4 = 1/((N-1)(N-2)(N-3)),

p_5 = (b-4)/((N-1)(N-2)(N-3)(N-4)),

p_6 = (b-4)(b-5)/((N-1)(N-2)(N-3)(N-4)(N-5)).
```

A signature whose prescribed arcs contain a proper directed cycle has probability
zero.

#### Proof

A rank-`h` signature needs its other `h-1` indices in the conditioned block, with
probability

```text
(b-1)_(h-1)/(N-1)_(h-1).
```

An anchored pair requires two prescribed arcs; an inserted triple requires three.
By PP3yy their conditional single-cycle probabilities are `1/(b-1)_2` and
`1/(b-1)_3`, unless a proper directed cycle is present.  Cancel factors for
`(h,r)=(4,2),(4,3),(5,3),(6,3)`. ∎

These are exactly the normalizations appearing in PP3yq--PP3yr.

## 2. Complete positive-support avoidance

Let `Z_other` contain every source-invalid count and normalized paid insertion
term except the complete positive support of the four classes above.

### Theorem PP3ams -- PROVED / CONDITIONAL RESIDUAL-SLACK INTERFACE

Suppose

```text
E Z_other <= 1-tau
```

for fixed `tau in (0,1)`.  If

```text
p_P S_P(c)+p_4 S_4(c)+p_5 S_5(c)+p_6 S_6(c)<tau,
```

then some marked single-cycle state is source-valid, selects none of the four
positive signature classes, and has remaining insertion cost below the marked
removal credit.  It gives a strict paid improvement.

#### Proof

Let `X_P,X_4,X_5,X_6` count selected distinct positive signatures.  Proposition
PP3amr gives the displayed expectation.  The nonnegative objective

```text
Z_other+X_P+X_4+X_5+X_6
```

has expectation below one.  In an outcome of value below one, every integer
source/signature count vanishes and the remaining normalized paid cost is below
one.  Avoiding a positive signature removes every witness multiplicity attached
to it. ∎

### Corollary PP3amt -- PROVED

Failure of high-support positive-signature avoidance under residual slack `tau`
forces at least one of

```text
S_P(c) >= tau (N-1)_3/(4(b-3)),
S_4(c) >= tau (N-1)_3/4,
S_5(c) >= tau (N-1)_4/(4(b-4)),
S_6(c) >= tau (N-1)_5/(4(b-4)(b-5)).
```

Thus a large witness multiplicity on a sparse arc support is not an independent
marked-host obstruction.

## 3. Recursive link sunflower theorem

Let `H` be a simple `k`-uniform hypergraph with `E>0` edges.

### Theorem PP3amu -- PROVED

There is an integer `j` with `0<=j<=k-1`, a fixed set `F` of `j` vertices, and a
family of at least

```text
c_k E^(1/k)
```

edges containing `F` whose residual sets `e\F` are pairwise disjoint.  Here
`c_k>0` depends only on `k`; one may take `c_k=1/k!`.

Thus the hypergraph contains either a resource-disjoint edge matching (`j=0`) or
a sunflower with a nonempty fixed resource core and pairwise disjoint petals.

#### Proof

Induct on `k`.  The case `k=1` is immediate.  Put `D=ceil(E^((k-1)/k))`.
If every vertex degree is below `D`, greedy matching selects at least
`E/(kD)=Omega_k(E^(1/k))` disjoint edges.

Otherwise fix a vertex of degree at least `D` and pass to its `(k-1)`-uniform
link, which has at least `D` edges.  The induction hypothesis gives a fixed core
and pairwise disjoint residual petals of size at least

```text
c_(k-1) D^(1/(k-1)) >= c_(k-1) E^(1/k).
```

Adjoin the fixed vertex to the core and weaken constants to `1/k!`. ∎

This theorem records every possible depth of nested partner concentration rather
than stopping after the first high-degree vertex.

## 4. Marked-source sunflower scales

After pigeonholing the finitely many typed roles and arc orientations, each dense
signature class in PP3amt gives a simple link on the other endpoint indices:

```text
anchored pair: k=3,
rank-four triple: k=3,
rank-five triple: k=4,
rank-six triple: k=5.
```

### Corollary PP3amv -- PROVED

Failure of positive-support avoidance yields one of the following fixed-core
sunflowers or resource-disjoint signature banks:

```text
anchored pair: Omega(N/b^(1/3)),
rank-four triple: Omega(N),
rank-five triple: Omega(N/b^(1/4)),
rank-six triple: Omega(N/b^(2/5)).
```

All hidden constants depend only on `tau` and the finite typed role count.

#### Proof

Apply PP3amu to the lower bounds in PP3amt.  Taking the appropriate `k`-th roots
gives the four displayed scales. ∎

## 5. Comparison with the marked target width

Use

```text
N=m^(19/20+o(1)),
b=m^(kappa+o(1)),
0<kappa<19/80,
W=m^(19/40+o(1)).
```

### Proposition PP3amw -- PROVED

Every scale in PP3amv is `omega(W)`.  The smallest exponent is the rank-six value

```text
19/20-2kappa/5
>
19/20-2(19/80)/5
=
171/200
>
19/40.
```

#### Proof

The anchored-pair, rank-four, and rank-five exponents are larger.  The displayed
calculation handles the smallest rank-six exponent. ∎

Therefore every dense high-support marked-source class contains a target-size
subsunflower or signature bank with substantial polynomial slack.

## 6. Revised marked-host endpoint

### Theorem PP3amx -- PROVED / CONDITIONAL SOURCE-HOST CONVERSION INTERFACE

For a free or one-controller-punctured marked centre tested with single-cycle
filler states, at least one of the following occurs.

1. A source-valid strict paid state exists after complete positive-support
   avoidance.
2. Unary source support gives a converted source star or credited witness bank by
   PP3amk--PP3amq.
3. Anchored-transition support gives a paid clean-chain state or a target-size
   transition endpoint bank by PP3zj--PP3aaj.
4. Rank-two unary or rank-three/rank-four binary `Xi` support gives avoidance,
   fixed-resource pencils, or endpoint banks by PP3ama--PP3amq.
5. One of the four high-support source classes gives a target-size fixed-core
   sunflower or resource-disjoint signature bank as in PP3amv.
6. Residual marked source/paid load already consumes the centre credit.
7. Source, Hall, alternating, distinguished-endpoint, or endpoint-host preparation
   fails explicitly.

#### Proof

Combine the reduced nine-core certificate PP3zd with the transition reductions,
the ambient unary/binary positive-support theorems, and PP3ams--PP3amw. ∎

### Corollary PP3amy -- PROVED

An exceptional marked centre is no longer described by nine unrelated weighted
support degrees.  It reduces to paid completion, residual credit-scale collateral,
or one of three explicit source-host geometries:

1. a credited endpoint bank;
2. a fixed-resource or nested-resource pencil;
3. a fixed-core source-invalid sunflower with pairwise disjoint petals.

The remaining marked-host task is to convert these simple host geometries, not to
control diffuse witness multiplicity.

The no-three-in-line conjecture remains unproved.
