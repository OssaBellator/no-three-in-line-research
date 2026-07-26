# Fixed-relative random permutations have a logarithmic collinearity barrier

The exact seed CSP may be written as one permutation `sigma` and one fixed
relative derangement `pi`, with the second layer `tau=sigma o pi`.  A natural
first attempt is to fix `pi` and choose `sigma` uniformly at random.

This chapter computes the relevant cylinders exactly.  Every labelled
collinear triple is a three-assignment event of probability `1/(n)_3`, but the
number of grid triples is `Theta(n^4 log n)`.  Consequently every fixed
relative derangement has `Theta(n log n)` expected forbidden triples.  The
natural canonical-event conflict graph also has degree `Omega(n^3 log n)`, so
the uniform symmetric permutation local-lemma criterion misses by a logarithmic
factor.

This is a barrier for the naive random model and dependency estimate, not an
impossibility theorem.  Nonuniform measures, cluster expansion, resampling
oracles, entropy compression, or explicit nonlinear constructions remain
possible.

## 1. Exact labelled triple cylinders

Fix a derangement `pi` of `[n]` and choose `sigma` uniformly from `S_n`.  Put

```text
tau=sigma o pi.
```

Let

```text
T={(x_1,r_1),(x_2,r_2),(x_3,r_3)}
```

be one nonaxis collinear grid triple.  Its columns and rows are pairwise
distinct.  For a layer pattern

```text
epsilon=(epsilon_1,epsilon_2,epsilon_3) in {0,1}^3
```

put

```text
z_i=pi^(epsilon_i)(x_i).
```

### Proposition PP3bde -- PROVED

The event that the three cells of `T` are selected with layer pattern
`epsilon` is impossible when the domains `z_1,z_2,z_3` are not distinct.  When
they are distinct, it is the canonical permutation event

```text
sigma(z_i)=r_i,  i=1,2,3,
```

and has probability exactly

```text
1/(n)_3.
```

Different feasible layer patterns for the same geometric triple are disjoint.

#### Proof

A first-layer cell `(x,r)` means `sigma(x)=r`; a second-layer cell means
`sigma(pi(x))=r`.  This gives the displayed assignments.  If two domains
coincide, the event asks one permutation value to equal two distinct rows and
is impossible.  Otherwise a uniform permutation realizes three prescribed
distinct domain--image pairs with probability `1/(n)_3`.

For one selected cell, both layer descriptions cannot hold: they would give
`sigma(x)=sigma(pi(x))`, hence `x=pi(x)`, contradicting that `pi` is a
derangement.  Therefore a realized triple has a unique layer pattern. ∎

Let `a_pi(T)` be the number of feasible layer patterns.  Then

```text
1<=a_pi(T)<=8,
```

because the all-first-layer pattern always has distinct domains.

### Corollary PP3bdf -- PROVED

For every nonaxis collinear triple `T`,

```text
Pr(T is selected)=a_pi(T)/(n)_3.
```

If `C_n` is the number of nonaxis collinear triples in `[n]^2`, then the number
`X_pi` of selected forbidden triples satisfies

```text
C_n/(n)_3
<= E X_pi <=
8C_n/(n)_3.
```

#### Proof

Sum the disjoint cylinders from PP3bde and then sum over all geometric triples.
The all-first-layer pattern gives the lower bound and the eight possible
patterns give the upper bound. ∎

## 2. Number of grid triples

Use one orientation of every primitive nonaxis integer direction

```text
v=(a,b),
a>0,
b!=0,
gcd(a,|b|)=1.
```

Put `m=max(a,|b|)`.

### Proposition PP3bdg -- PROVED

The number of nonaxis collinear triples satisfies

```text
C_n=Theta(n^4 log n).
```

#### Proof

For the upper bound, orient every triple by its primitive direction and its
first point.  Once the first point and direction are fixed, the two later
multiples have at most `O((n/m)^2)` choices.  There are at most `n^2` first
points and `O(m)` primitive directions with maximum coordinate `m`.  Hence

```text
C_n
<= O(n^4) sum_(m<=n) 1/m
=O(n^4 log n).
```

For the lower bound, restrict to directions `(m,b)` with
`1<=b<=m`, `gcd(m,b)=1`, and `m<=n/12`.  Choose the first point in a fixed
central rectangle of area `Omega(n^2)` and choose two positive multiples at
most `floor(n/(4m))`.  All resulting triples remain in the board and are
uniquely oriented.  This gives

```text
C_n
>= Omega(n^4)
sum_(m<=n/12) phi(m)/m^2.
```

The elementary totient estimate

```text
sum_(m<=N) phi(m)/m^2=Theta(log N)
```

gives the lower bound. ∎

Horizontal and vertical triples are omitted because saturation already fixes
their line occupancies at two.

### Theorem PP3bdh -- PROVED

Uniformly for every derangement `pi`,

```text
E X_pi=Theta(n log n).
```

In particular, the first moment of the uniform fixed-relative model cannot
prove seed existence.

#### Proof

Combine PP3bdf, PP3bdg, and `(n)_3=Theta(n^3)`.  The constants are uniform in
`pi` because `1<=a_pi(T)<=8` for every triple. ∎

This does not say that a typical state is irreparable; it says that zero bad
triples is not obtained from the unconditioned first moment.

## 3. Natural canonical-event conflict graph

Use the canonical events from PP3bde.  Two events conflict in the standard
permutation dependency graph when they prescribe different images for one
domain or different domains for one image.

### Proposition PP3bdi -- PROVED

For all sufficiently large `n`, the maximum degree `D_n` of this natural
canonical-event graph satisfies

```text
D_n=Omega(n^3 log n).
```

#### Proof

Choose a canonical triple event containing an image row `r` in the middle half
of the board.  Count all-first-layer canonical events containing image `r` at
a different domain.

Choose the corresponding cell `(x,r)` with `x` in the middle half.  For every
primitive direction `(m,b)` with `1<=b<=m`, `gcd(m,b)=1`, and `m<=n/12`, there
are `Omega((n/m)^2)` choices of two forward or backward multiples that stay in
the board.  Summing over `Omega(n)` choices of `x` gives

```text
Omega(n^3)
sum_(m<=n/12) phi(m)/m^2
=
Omega(n^3 log n)
```

distinct canonical events using image `r`.  Discarding the events that use the
same domain--image assignment as the fixed event removes only one column's
contribution, of lower order.  Every remaining event conflicts with the fixed
event through image `r`. ∎

### Corollary PP3bdj -- PROVED

For the canonical probability

```text
p_n=1/(n)_3,
```

the uniform symmetric local-lemma expression satisfies

```text
e p_n(D_n+1)=Omega(log n).
```

It therefore exceeds one for all sufficiently large `n`.  The standard
symmetric criterion on the natural canonical-event graph cannot establish the
seed theorem.

#### Proof

Insert PP3bdi and `(n)_3=Theta(n^3)`. ∎

This conclusion is intentionally limited.  It does not rule out an asymmetric
or cluster-expansion local lemma, a different lopsidependency graph, a
nonuniform permutation measure, or a constructive correction process.

## 4. Revised probabilistic seed frontier

### Corollary PP3bdk -- PROVED

The exact prime-minus-one seed frontier cannot be closed by either of the two
most direct uniform arguments:

1. the unconditioned first moment, because every fixed `pi` has
   `Theta(n log n)` expected bad triples; or
2. the uniform symmetric permutation local lemma on canonical triple events,
   because its left side is `Omega(log n)`.

A successful asymptotic proof must exploit additional structure, for example:

```text
nonuniform relative-cycle geometry,
correlated or sequential permutation measures,
stronger local-lemma criteria,
explicit nonlinear arithmetic permutations,
or a repair/absorption theorem for the initial bad-line set.
```

The asymptotic seed theorem and the no-three-in-line conjecture remain
unproved.

## 5. Finite diagnostic

Run

```bash
python scripts/check_fixed_relative_random_barrier.py \
  experiments/fixed-relative-random-barrier-example.json
```

The checker enumerates maximal nonaxis lines, all of their collinear triples,
all feasible layer patterns, the exact expectation numerator, and a row-image
conflict lower bound in the natural canonical dependency graph.
