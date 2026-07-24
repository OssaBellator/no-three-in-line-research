# Unresolved-lemma branch map

This map records how the parallel research branches connect. A branch should merge only proved results; open statements remain labelled as targets.

## Main dependent chain

### `research/alternating-core-chain`

Sequential dependency:

```text
AN4 normalized collateral
 -> AC1 second-order concentration
 -> AC2 paid structural re-extraction
 -> AC3 monotone carry complexity
 -> AC4 alternating-core termination
 -> AC5 reverse-scale compatibility
 -> AC6 prime-minus-one completion
```

This is the only branch intended to carry the full local-to-global proof chain.

## Independent inputs to the main chain

### `research/bounded-denominator-absorbers`

Consumes PA/CF chamber structure; returns a decreasing trade for every fixed reduced denominator `q`. Imported by AC2–AC4.

### `research/rational-inverse-expansion`

Solves I12 and classifies simultaneous small-doubling/order-two chains. Imported by AC3–AC4 when carry propagation enters a multiplicative structured exception.

### `research/geometric-cleaning`

Removes the hypotheses behind S2, S5, L4 and P1. Can feed AC5 or bypass the alternating chain by reaching a matching/product-state endpoint.

### `research/orbit-phase-expansion`

Alternative decoder. May prove the local termination portion of AC4 by a phase/Tanner argument, but is logically independent while under development.
The alternating branch's AC3p--AC3r interface is the exact star-shaped
special case to be used when an orbit-phase alphabet realizes one
shared-token role: it contracts feasibility to one common phase message
without importing the unresolved general Tanner-expansion claim.

## Independent selection endpoints

### `research/superregular-resampling`

Dense-host local-load endpoint: resampling oracle or conflict-free exact-cover theorem.

### `research/sparse-algebraic-spread`

Sparse-host `O(1/d)` spread and two-layer selection. Independent of the dense resampling theorem.

These branches can replace or supplement the complete-clone endpoint once a suitable candidate host is constructed.

## Independent all-n routes

Each starts only after a prime-minus-one or other infinite family of exact constructions is available.

### `research/all-n-prime-patching`

Extend a solved `m x m` configuration to nearby `n x n` by a boundary/distributed absorber, then combine with a proven gap theorem.

### `research/all-n-composite-modulus`

Construct algebraic seeds directly over composite moduli or prime powers, including nonunit rows and real-lift carry control.

### `research/all-n-product-construction`

Prove a saturation-preserving product/composition theorem and use arithmetic factorization to cover all side lengths.

The three all-n branches are alternatives and should not be coupled unless one develops a proven interface to another.

## Merge discipline

- Do not merge a target statement as `PROVED` without a complete argument and exact hypotheses.
- Preserve counterexamples and regression tests.
- When a branch proves an interface theorem, update this map and the theorem index in the same pull request.
- Results that only improve constants should merge into their source track rather than creating another dependency.
- A complete no-three-in-line proof requires one successful local/global construction chain and one successful all-n route.
