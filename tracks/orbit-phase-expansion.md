# Carry-sensitive phase codes and orbit-Tanner expansion

**Branch:** `research/orbit-phase-expansion`

This is an alternative decoder track. It groups the unresolved phase-code and orbit-expansion ideas because a phase code is only useful if its labelled conflict graph has a provable expansion/private-repair property.

## Proved inputs

- O1: multiplicative orbit blocks preserve row and column sets;
- O2–O3: cross-channel secants are projective involutions and the syndrome graph is properly edge-coloured;
- O4–O5: cycle banks and window-product hyperbola covers;
- I2/I6: common-ratio banks and full coset absorber banks;
- the generic claim “bounded line occupancy plus bounded pair codegree implies private repair” is refuted.

## OP1 — Carry-sensitive phase alphabet

### Target statement

For an orbit block of order `h`, construct a finite state alphabet `A_h` and an encoding of each state by:

- multiplicative phase;
- product-carry signature;
- coordinate-wrap phase;
- optional denominator or coset label;

such that every real collinear triple involving the block forbids a labelled assignment on at most three variables and the forbidden label depends only on a bounded amount of phase data.

The number of states should be `Omega(h)` and every state must preserve the same active rows and columns.

## OP2 — Arithmetic Tanner graph

### Target statement

Build a bipartite or factor graph whose variable nodes are orbit blocks and whose check nodes are real collinear triples. Prove an arithmetic expansion theorem:

For every set `U` of at most `eta m` variables, either

1. at least `c|U|` checks have a unique or privately repairable incidence in `U`;
2. the variables in `U` lie in a bounded union of multiplicative cosets or carry chambers;
3. `U` contains a paid common-ratio bank or a bounded-denominator absorber block.

The theorem must use the Möbius/carry labels; unlabelled degree and codegree hypotheses are insufficient.

## OP3 — Phase-flip decoder

### Target statement

Given OP2, define a local or batch decoder that changes phases while preserving row and column saturation. Prove that whenever the syndrome is nonzero, one decoder round either:

- reduces the triple potential by at least `c` times the number of private checks;
- increases a monotone structured-core potential;
- delegates a bounded structured component to an existing absorber.

The decoder must handle cycle-like cores and the exact `p=11` frozen one-colour example by permitting opposite-colour or multi-block phase changes.

## OP4 — Product-state completion

### Target statement

After removing all structured exceptions, show that the residual labelled CSP has normalized pair/triple conflict mass below the product-state local-lemma threshold. Deduce a global phase assignment with no bad triple.

This is an alternative to the perfect-matching selection endpoint and may operate directly in the bounded-hyperbola orbit universe.

## OP5 — Interface theorem

### Target statement

For every bounded-channel hyperbola seed, the phase-code decoder either reaches zero syndrome or returns a structured component covered by:

- the alternating-core chain;
- the bounded-denominator absorber track;
- the rational inverse-expansion track.

No residual generic cycle core may remain unclassified.

## Candidate methods

- nonbacktracking expansion of the properly edge-coloured secant graph;
- spectral analysis after quotienting by multiplicative cosets;
- unique-neighbour expansion in each carry-signature layer;
- expander-code bit-flip analysis with weighted syndrome;
- entropy compression over the finite phase alphabet;
- exact small-core classification plus expansion outside the classified radius.

## Mandatory counterexamples

- simple labelled cycles with no private check;
- translated absorber walls;
- constant-ratio cycles and order-two orbits;
- the frozen `p=11` cycle;
- cores in which every check has degree two within the active variable set.

## Completion criterion

This branch is complete when OP1–OP5 provide a rigorous saturation-preserving decoder theorem, not merely an empirical expansion claim.