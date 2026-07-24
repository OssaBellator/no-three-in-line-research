# An exact four-endpoint trap and the corrected escape target

CMR141--CMR142 reduce a hypothetical positive global saturated minimum to a
finite balanced cycle of four-endpoint trades. It is tempting to strengthen
this to a universal local-descent statement: every positive-potential saturated
state should admit a decreasing four-endpoint move, or every four-core cycle
should be impossible. Both statements are false.

This chapter records an exact `N=4` counterexample and identifies the extra
structure required by the remaining prime-power theorem.

## 1. A two-state terminal cycle at potential one

Let the two permutation layers be written as row tuples indexed by columns
`0,1,2,3`. Define

```text
A0 = (0,1,3,2)
A1 = (2,3,0,1)

B0 = (1,0,2,3)
B1 = (2,3,0,1)
```

Let `A` and `B` be the corresponding saturated states.

### Theorem CMR143 — PROVED BY EXHAUSTIVE FINITE CHECK

Both `A` and `B` are disjoint saturated states with exactly one real collinear
triple:

```text
A: (1,1,A0), (0,2,A1), (2,0,A1)
B: (2,2,B0), (1,3,B1), (3,1,B1)
```

Rematching all four points of layer zero sends `A` to `B`, and the reverse
rematching sends `B` to `A`. Both moves are allowed degree-two endpoint moves
and destroy the unique source triple.

Every allowed four-endpoint move from either state has target potential either
`1` or `4`. In particular, neither state has a strictly improving
four-endpoint move, and choosing a minimum-potential child gives the directed
cycle

\[
A\longleftrightarrow B.
\]

### Proof

All statements are finite. The checker verifies disjointness, saturation, all
`56` triples of each eight-point state, and every allowed rematching of either
complete layer. The outgoing potential multisets are

\[
\{1,4,4,4\}
\]

for both `A` and `B`. ∎

## 2. The trap is not globally optimal

Define

```text
C0 = (0,1,3,2)
C1 = (2,3,1,0).
```

### Theorem CMR144 — PROVED BY EXHAUSTIVE FINITE CHECK

The state `C` is saturated, disjoint, and has no real collinear triple.
Consequently the two-cycle from CMR143 is a genuine local terminal component
above the global minimum:

\[
\Phi(C)=0
<
1=\Phi(A)=\Phi(B).
\]

Thus the following statements are refuted:

1. every positive-potential saturated state has a decreasing four-endpoint
   move;
2. every balanced four-core defect-flow cycle is impossible;
3. a monotone invariant depending only on the normalized four-board and current
   triple potential can prove the full theorem.

### Proof

The checker exhausts all triples of `C`. The conclusions follow from CMR143. ∎

## 3. Corrected inherited-escape target

The prime-power closure does not arrive at an arbitrary four-board. Its terminal
board has ancestry:

- an original binary same-layer star and unique prefix owner;
- a recursive-compatible parent node;
- a sequence of child-pencil and alternating expansions;
- fixed quotient states protected by fine-to-coarse invariance;
- target triples carrying first-separation and primitive carry signatures.

### Corrected four-core escape lemma — OPEN

For a four-endpoint one-target core arising from the prime-power closure, use
its inherited node, scale, quotient, and carry data to prove one of:

1. an allowed state lowers the fixed global baseline;
2. the core expands back to an inherited parent or opposite-layer bank with a
   strictly smaller lexicographic ancestry signature;
3. the terminal cycle consumes a quotient or carry signature which cannot
   balance around the cycle;
4. the core is one of a finite family of locally trapped components, each with
   an explicit larger escape move.

CMR143 shows that option 4 cannot be omitted in a purely local theorem. The
next computation should enumerate four-core strongly connected components in
small prime-power hosts while retaining their prefix ancestry, rather than
studying normalized boards alone.

No all-`n` theorem is claimed here. The exact state and outgoing-move checks are
included in
[`scripts/verify_prime_power_four_endpoint_core.py`](../scripts/verify_prime_power_four_endpoint_core.py).
