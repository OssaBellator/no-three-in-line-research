# Crossing defects force closure-envelope expansion

CMR174 gives a monotone envelope depth but does not prescribe how to use a
triple which crosses the current envelope. The correct deterministic rule is to
move one of its outside points. This turns every crossing defect into a strict
reverse-scale payment.

## 1. Crossing-target rule

Let `E` be the current closure envelope, and let `Q` be a current real triple.
Call `Q` **crossing** if at least one of its point columns lies outside `E`.

### Theorem CMR193 — PROVED

If `Q` is crossing, there is an alternating four-endpoint move which

1. preserves saturation and layer disjointness;
2. destroys `Q`;
3. moves a column outside `E`;
4. strictly decreases the depth of the next closure envelope.

### Proof

Choose a point `P` of `Q` whose column lies outside `E`. In the permutation
layer containing `P`, pad `P` with arbitrary further layer points to obtain four
endpoints. Their forbidden board consists of the four old cells and the cells
occupied by the opposite layer, so it has row and column degree at most two.
CMR128 supplies an allowed matching which moves every endpoint and in particular
removes the old cell of `P`. Thus `Q` is destroyed.

The moved-column history now contains every earlier moved column in `E` and the
column of `P` outside `E`. Their least common prefix block strictly contains
`E`, so CMR174 says its depth is strictly smaller. ∎

The rule is independent of quotient or carry data. It should always be applied
before attempting an internal signature argument.

## 2. Batch parent lifting: crossing or internal mass

Use the notation of CMR190. Thus `R` terminal targets in one nonroot envelope
produce one parent state with at least

\[
M(R)=\left\lceil\frac{2R}{11}\right\rceil
\]

new triples outside all chosen terminal subcovers.

### Theorem CMR194 — PROVED

At least one of the following holds.

1. **Strict envelope expansion.** One of the `M(R)` new triples is crossing, and
   CMR193 supplies a target move which strictly decreases envelope depth.
2. **Internal defect mass.** All `M(R)` new triples have every point column in
   the current envelope `E`.

In the second alternative every new triple still touches the replacement layer
block from CMR191.

### Proof

If one of the new triples has a point column outside `E`, apply CMR193 to it.
Otherwise every one of them is internal by definition. CMR191 gives the final
replacement-touching assertion. ∎

## 3. Bounded number of crossing resolutions

### Corollary CMR195 — PROVED

Along one alternating closure branch, the strict-expansion alternative of
CMR194 can occur at most `k` times for `N=p^k`.

After the final strict expansion, every later CMR190 batch produces at least
`ceil(2R/11)` new replacement-touching triples wholly inside one fixed envelope.

### Proof

Every strict expansion decreases the nonnegative integer envelope depth. By
CMR174 the depth starts at most `k`, so there are at most `k` decreases. Once no
further decrease occurs, CMR194 leaves only the internal alternative. ∎

## 4. Revised no-return target

Cross-envelope recycling is now closed by a finite reverse-scale budget. The
remaining obstruction is entirely internal to one fixed envelope epoch:

- its two inherited layer row sets remain invariant;
- the disjoint-fibre parent bank remains executable;
- every terminal batch generates a `2/11` population of internal
  replacement-touching triples;
- no later move in the epoch may appeal to a coarser envelope without spending
  one of the bounded CMR195 expansions.

The next theorem must charge repeated internal batches to first-separation and
primitive carry signatures inside this fixed envelope, or show that their
linear defect growth exceeds the envelope's joint-parent collateral budget.

No all-`n` theorem is claimed here. The prefix-depth and crossing-target
identities are checked in
[`scripts/verify_prime_power_envelope_expansion.py`](../scripts/verify_prime_power_envelope_expansion.py).
