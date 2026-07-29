# Asymptotic cycle-rate polytopes for interactions

`docs/500` computes exact finite powers of a Pareto transfer matrix.  For an
all-scale construction, repeated interaction motifs also need a certified
long-run rate description.  This chapter identifies that description with a
finite rational circulation polytope and obtains periodic implementations with
vanishing finite-length overhead.

Let `G=(V,E)` be a finite strongly connected transition graph.  Edge `e` has a
nonnegative rational vector `v_e` containing work and every omitted-output
coordinate.  A length-`N` walk has average label equal to its total vector
divided by `N`.

## 1. Exact asymptotic rate polytope

### Theorem PP3ciw -- PROVED / CIRCULATION RATE POLYTOPE

The set of limiting average vectors of arbitrarily long walks is

```text
R={sum_e x_e v_e :
   x_e>=0,
   sum_(e out of u) x_e=sum_(e into u) x_e for every u,
   sum_e x_e=1}.
```

Equivalently, `R` is the convex hull of the mean vectors of the finitely many
simple directed cycles.

#### Proof

Empirical edge frequencies of a long walk have asymptotically vanishing flow
imbalance, so every limit is a normalized circulation.  Every nonnegative
circulation decomposes into directed cycles; after normalization its projected
vector is a convex combination of cycle means.  Conversely, long repetitions
of cycles, joined by bounded connecting paths, realize every rational convex
combination up to vanishing bridge frequency. ∎

## 2. Periodic realization and finite-length overhead

### Theorem PP3cix -- PROVED / EVENTUALLY PERIODIC RATE CERTIFICATE

Every rational point of `R` whose supporting circulation is Eulerian-connected
has an exact periodic realization.  In general, a rational point has a walk
implementation whose length-`N` average differs from it by at most `C/N` in
every coordinate, where `C` is the total label cost of a fixed finite set of
connecting paths.

#### Proof

Clear denominators of a connected rational circulation and apply the Euler
construction of `PP3cih`.  For several cycle components, traverse the requested
integer number of copies of each cycle and use fixed connecting paths between
them.  Only the bounded connectors fail to match the desired circulation, so
the average error is `O(1/N)`. ∎

## 3. Exact scalar separation

### Theorem PP3ciy -- PROVED / MINIMUM-CYCLE-MEAN ORACLE

For every nonnegative rational weight vector `lambda`,

```text
min_(r in R) lambda dot r
```

is the minimum mean weight of a directed cycle when edge `e` is assigned scalar
weight `lambda dot v_e`.  An exact minimum-cycle-mean algorithm therefore
separates a proposed asymptotic rate from `R` and returns a critical periodic
interaction pattern.

#### Proof

A linear functional on the convex hull of cycle means is minimized at one of
those means.  Exact rational minimum-cycle-mean algorithms evaluate the finite
cycle system without enumerating all long walks. ∎

## 4. Stored exact fixture

The audit `scripts/check_asymptotic_interaction_cycle_rates.py` has two states and
three simple cycle means:

```text
A  = (1,2,0),
D  = (1,0,2),
BC = (3/2,1/2,1/2).
```

The coordinate cap `(3/2,1/2,1/2)` uniquely selects the alternating cycle
`BC`.  Weight `(1,1,1)` gives minimum cycle mean `5/2`.  Even lengths realize
the target exactly by repeating `BC`; at odd length `N`, the best closed walk
has scalar overhead exactly `1/(2N)`.

## 5. Prime-patching consequence

Repeated interaction corrections now have a finite asymptotic certificate:
a rational rate polytope, a periodic controller, and an exact cycle-mean
separator.  This is the first integration mechanism in the current chain that
controls every sufficiently long repetition with an explicit `O(1/N)` boundary
term rather than certifying only one fixed length.
