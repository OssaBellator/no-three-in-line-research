# Carry-sensitive phase codes and orbit-Tanner expansion

**Branch:** `research/orbit-phase-expansion`

This is an alternative decoder track. It groups the unresolved phase-code and orbit-expansion ideas because a phase code is only useful if its labelled conflict graph has a provable expansion/private-repair property.

## Proved inputs

- O1: multiplicative orbit blocks preserve row and column sets;
- O2–O3: cross-channel secants are projective involutions and the syndrome graph is properly edge-coloured;
- O4–O5: cycle banks and window-product hyperbola covers;
- I2/I6: common-ratio banks and full coset absorber banks;
- the generic claim “bounded line occupancy plus bounded pair codegree implies private repair” is refuted.

## OP1 — Carry-sensitive phase alphabet — PARTIAL

### Target statement

For an orbit block of order `h`, construct a finite state alphabet `A_h` and an encoding of each state by:

- multiplicative phase;
- product-carry signature;
- coordinate-wrap phase;
- optional denominator or coset label;

such that every real collinear triple involving the block forbids a labelled assignment on at most three variables and the forbidden label depends only on a bounded amount of phase data.

The number of states should be `Omega(h)` and every state must preserve the same active rows and columns.

[`orbit-phase-literals-and-decoder.md`](orbit-phase-literals-and-decoder.md)
proves OP1a: the O1 alphabet `Z/hZ` gives exactly `h` row-column-preserving
states, and every realizable real triple is one canonical forbidden partial
assignment on at most three block variables. It also gives a lossless
constant-length carry decoration. The remaining OP1 issue is uniform
compression of the numerical carry values into signature layers useful to
OP2.

## OP2 — Arithmetic Tanner graph

### Target statement

Build a bipartite or factor graph whose variable nodes are orbit blocks and whose check nodes are real collinear triples. Prove an arithmetic expansion theorem:

For every set `U` of at most `eta m` variables, either

1. at least `c|U|` checks have a unique or privately repairable incidence in `U`;
2. the variables in `U` lie in a bounded union of multiplicative cosets or carry chambers;
3. `U` contains a paid common-ratio bank or a bounded-denominator absorber block.

The theorem must use the Möbius/carry labels; unlabelled degree and codegree hypotheses are insufficient.

### Acyclic case proved

[`orbit-phase-forest-completion.md`](orbit-phase-forest-completion.md)
proves OP2a: when every check forbids one canonical phase assignment,
alphabets have size at least two, checks have arity at least two, and the
factor-incidence graph is a forest, leaf elimination constructs a
conflict-free phase assignment in linear time. Hence only unary saturation
or cyclic residual cores require arithmetic expansion or absorption.

### Pseudoforest case proved

[`orbit-phase-pseudoforest-completion.md`](orbit-phase-pseudoforest-completion.md)
proves OP2b: the same conclusion holds when every incidence component has
at most one cycle.  Leaf elimination reduces the only nonforest core to an
alternating cycle, and one phase choice breaks its closing check.
Consequently OP2 arithmetic expansion is needed only for unary saturation
or a component with at least two independent cycles.

[`orbit-phase-cactus-completion.md`](orbit-phase-cactus-completion.md)
proves OP2c for a multiply-cyclic class. If every residual check has arity
two and the contracted variable multigraph is a cactus, block-tree dynamic
programming either constructs an assignment or compresses the entire
obstruction to explicit unary saturation at an articulation variable.

[`orbit-phase-factor-cactus-completion.md`](orbit-phase-factor-cactus-completion.md)
proves OP2d for the full factor-incidence cactus, without a binary-arity
restriction. Variable articulations carry label-set messages and check
articulations carry one mismatch bit. The exact block dynamic program
returns an assignment, variable saturation, or two-state check
saturation. Consequently a residual topological core must now contain a
noncactus factor block with at least two independent incidence cycles.

[`orbit-phase-feedback-completion.md`](orbit-phase-feedback-completion.md)
proves OP2e beyond the cactus boundary. If deleting \(f\) variable nodes
leaves a factor-incidence cactus, conditioning those variables and
running OP2d decides the instance in \(O(h^{f+3}I)\) time. Hence every
fixed-feedback-variable core, including theta blocks, is an exact finite
interface. A residual topology needing new OP2 expansion may be assumed
to have unbounded variable-deletion distance from the cactus class.

## OP3 — Phase-flip decoder

### Target statement

Given OP2, define a local or batch decoder that changes phases while preserving row and column saturation. Prove that whenever the syndrome is nonzero, one decoder round either:

- reduces the triple potential by at least `c` times the number of private checks;
- increases a monotone structured-core potential;
- delegates a bounded structured component to an existing absorber.

The decoder must handle cycle-like cores and the exact `p=11` frozen one-colour example by permitting opposite-colour or multi-block phase changes.

### Proved decoder components

The phase-literal note proves the exact identity
`Delta Phi = created weight - destroyed weight`, its check-disjoint batch
version, and a lexicographic termination lemma for rounds that either lower
`Phi` or increase a bounded structured-core potential. OP3 remains open
until OP2 supplies one of those certified moves for every nonzero
syndrome.

## OP4 — Product-state completion

### Target statement

After removing all structured exceptions, show that the residual labelled CSP has normalized pair/triple conflict mass below the product-state local-lemma threshold. Deduce a global phase assignment with no bad triple.

OP2a already completes every acyclic residual component exactly. OP4 may
delete those components before estimating normalized conflict mass on the
cyclic core.

OP2b also deletes every unicyclic component.  Thus the residual core for
the OP4 estimate may be assumed to have cyclomatic number at least two in
each component.

OP2c additionally deletes satisfiable binary cactus blocks and turns every
unsatisfiable binary cactus into a unary certificate before that estimate.
OP2d does the same for arbitrary-arity factor cacti, with a possible
two-state check-saturation certificate.
OP2e does the same for every fixed variable-deletion distance from a
factor cactus, at the cost of enumerating the bounded feedback alphabet.

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

The forest and pseudoforest boundaries, unary-saturation exception, and a
multiply-cyclic unsatisfiable example are retained by
`scripts/verify_phase_forest.py` and
`scripts/verify_phase_pseudoforest.py`. Binary cactus compression and its
unary-saturation obstruction are retained by
`scripts/verify_phase_cactus.py`. High-arity factor-cactus messages are
checked by `scripts/verify_phase_factor_cactus.py`. Conditioning across
one feedback variable on every binary theta instance is checked by
`scripts/verify_phase_feedback.py`.

## Completion criterion

This branch is complete when the remaining OP1 compression and OP2–OP5
provide a rigorous saturation-preserving decoder theorem, not merely an
empirical expansion claim.
