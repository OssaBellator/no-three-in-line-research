# Bounded-denominator perfect-chamber absorbers

**Branch:** `research/bounded-denominator-absorbers`

This track is independent of the global alternating-closure proof once the reduced denominator is fixed. Its output is consumed by AC2–AC4 on `research/alternating-core-chain`.

## Proved inputs

For an aligned interpolation parameter `t'/q` in lowest terms:

- PA1 classifies all zero-leading-carry parameters;
- PA2 proves that perfect alignment is equivalent to divisibility of both relevant wrap indices by `q`;
- PA3 gives population at most `4p/q`;
- CF4 identifies explicit rational wrap centers;
- CF5 gives a divisor bound inside one perfect-wrap chamber;
- CF6 forces dispersion through many centers unless the multipliers have a large common divisor.

Thus only fixed or bounded `q` can support a positive-density obstruction.

## BDA1 — q-striped chamber decomposition

### Target statement

For every fixed integer `q>=2`, partition the perfectly aligned base parameters into `O_q(1)` classes such that within each class:

1. the source and target wrap indices have fixed residues modulo `q`;
2. the active points lie in explicit arithmetic intervals or multiplicative cosets;
3. every row and column is used at most once by each permutation layer;
4. the corresponding aligned triples share one finite list of rational interpolation patterns.

The decomposition must be canonical under the red–blue channel swap and stable under deletion of `O_q(1)` exceptional points.

## BDA2 — local alternating absorber

### Target statement

For each fixed denominator `q`, there is a constant `h(q)` and a finite family of row-column-preserving signed trades, each supported on at most `h(q)` active rows and columns, with this property:

Given a q-striped perfect chamber containing at least `h(q)` paid aligned certificates, one may select one trade whose positive state is the current local state and whose alternative state:

- preserves two points per active row and column;
- preserves disjointness of the two permutation layers;
- destroys a positive fraction `c_q` of the paid chamber certificates;
- creates at most `c_q/2` times that number of new certificates outside protected higher-height lines.

A bank version with a spread distribution is also acceptable.

## BDA3 — finite conflict regularization

### Target statement

The local trades from BDA2 can be selected on a linear-size disjoint subfamily of chamber blocks so that the labelled pair/triple conflict mass per block is `O_q(1)`. Consequently either:

1. one block improves immediately;
2. the product-state local lemma produces a joint improving state;
3. the blocks organize into one of finitely many q-periodic frozen templates.

The proof must use the bounded denominator and explicit wrap-index residues; generic bounded codegree is insufficient.

## BDA4 — exception classification

### Target statement

Classify every q-periodic frozen template from BDA3. Prove that each is one of:

- a subgroup-coset absorber already covered by I6;
- an order-two orbit covered by I10–I11;
- a finite translated-block template with an explicit independent-state trade;
- a bounded exceptional configuration removable by direct finite enumeration.

The classification must be uniform in `p` for fixed `q`.

## BDA5 — absorber interface theorem

### Target statement

For every fixed `q`, there are constants `p_0(q)` and `c(q)>0` such that any paid q-denominator perfect-alignment class in a prime grid with `p>=p_0(q)` admits a row-column-preserving alternating modification lowering the triple potential by at least `c(q)` times its paid incidence.

This is the theorem imported by AC2–AC4.

## Suggested constructions

- q-phase cyclic shifts inside wrap-index strips;
- small Fourier or difference-operator trades preserving row and column sums;
- subgroup-coset states when `q` divides a useful order in `F_p^*`;
- exact-cover matching on the finite quotient of rows and columns modulo `q`;
- precomputed trade libraries for small `q`, followed by a general lifting lemma.

## Required falsification

For every `q` tested, enumerate the finite quotient CSP and search for:

- chambers with no improving local trade;
- translated copies defeating synchronized shifts;
- order-two exceptions;
- collisions between the two permutation layers.

Any frozen template must be added to BDA4 rather than hidden in an asymptotic estimate.

## Completion criterion

This branch is complete when BDA1–BDA5 are proved for every fixed `q`, with an effective dependence on `q` and an exact interface usable by the alternating-core branch.