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
AC3s--AC3u additionally import only the proved canonical-literal
representation: a shared certificate has rank at most three and either
compresses to seven mismatch states or returns an exact-phase
sensitivity witness.  No general OP2 expansion statement is assumed.
AC3v--AC3x are internal to the alternating branch: the primal
projection of all finite factor and constraint scopes proves exact
scope completion and payment additivity, while a dense projection is
returned with one finite structural incidence label.  These results do
not import an arithmetic expansion theorem from another branch.
AC3y--AC3z are also internal: they localize all phase sensitivity to one
block, compress exact phases by observable behavior, and audit any
proposed arithmetic chart.  They do not assume that OP2 or RI has
already proved that chart complete.
AC3aa--AC3ac import only the proved O1 partition and OP1a canonical
phase-literal representation.  They construct the exact active-literal
chart, prove that an exact O1 channel can require all \(h\) labels, and
give a hard-exact heavy-soft chart with explicit \(2\tau\) one-block
collateral error and at most \(3W/\tau\) heavy literals.  Large hard
and heavy-soft literal families enter the subsequent internal routers;
a subgroup-coset or bounded-denominator label is not called terminal
until the independent RI or BDA paid-collateral interface applies.
AC3ad--AC3af are again internal finite combinatorics.  Once OP2 or the
main chain localizes a literal to the current phase context, they
compute exact drift and reduce the activated rank-three bucket to an
effectively rank-one obstruction, a bounded transversal, a paid
depth-two literal, or a residual-disjoint bank.  They do not assume a
global OP2 expansion theorem or promote an RI/BDA label to a terminal
absorber.
AC3ag--AC3ai are also internal.  At one fixed global centre literal
they turn varying residual contexts into an effectively rank-one
class, a paid simultaneously realizable context bank, a depth-two
literal, or a residual-block phase fan.  The cross-centre hard-literal
mixture is passed to AC3aj--AC3ak; arithmetic classification of the
structured outputs remains an explicit OP2/RI/BDA interface.
AC3aj--AC3ak close that cross-centre combinatorial step at every
current block.  Safe nonimproving target buckets are disjointly paid;
unsafe targets give fixed exclusions, a common current residual
literal, or support-disjoint alternative-target blockers.  Only the
scope-complete arithmetic installation/classification of the explicit
outputs remains an OP2/RI/BDA interface.

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
