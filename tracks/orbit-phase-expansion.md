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

[`orbit-phase-incidence-treewidth.md`](orbit-phase-incidence-treewidth.md)
proves OP2f by dynamic programming directly on a factor-incidence tree
decomposition. A bag variable carries its phase label and a bag check
carries one accumulated mismatch bit, giving exact completion in

\[
O\!\left(\max\{h,4\}^{t+1}(|V|+|\mathcal C|+I)\right)
\]

for incidence treewidth \(t\). Hence bounded-width strip and ladder
cores are also finite interfaces, even when their feedback distance
grows.

[`orbit-phase-core-preprocessing.md`](orbit-phase-core-preprocessing.md)
proves OP2g, an exact fixed-point preprocessing for every canonical
phase instance. Tautological and duplicate checks are deleted, a
forbidden partial assignment subsumes each of its extensions, and unary
nogoods propagate domain deletions. The procedure preserves the complete
satisfying-assignment set and either exposes an empty-domain certificate
or leaves an antichain of arity-at-least-two checks on nontrivial
domains. Arithmetic expansion is therefore needed only for this
irreducible canonical core.

[`orbit-phase-antichain-lubell.md`](orbit-phase-antichain-lubell.md)
proves OP2h. Every irreducible canonical check family satisfies the
nonuniform Lubell bound

\[
\sum_C
\left(
\binom n{|C|}
\prod_{v\in C}|\mathcal A_v|
\right)^{-1}
\leq1.
\]

For a common \(h\)-phase alphabet and rank-two/three checks this becomes
\(M_2/(\binom n2h^2)+M_3/(\binom n3h^3)\leq1\). The bound is sharp for
a complete fixed-rank layer, so it both supplies an exact normalized
budget and proves that antichain preprocessing alone cannot replace the
missing arithmetic expansion theorem.

OP2i localizes that budget. The weighted variable loads sum to at most
the maximum check rank \(r\), so at threshold \(\theta\) all heavy load
is supported on at most \(r/\theta\) variables, while every other
variable has load below \(\theta\). Some phase literal has load at most
\(r/(n|\mathcal A_v|)\). This gives an exact bounded-kernel/low-load
alternative for the current irreducible core; the remaining arithmetic
task is to control the residual after conditioning on that kernel or to
classify it as a structured exception.

OP2j supplies that conditioning audit. A surviving rank-\(k\) check
meeting \(j\) of \(f\) fixed variables has exact Lubell amplification
\[
\frac{\binom nk}{\binom{n-f}{k-j}}
\prod_{v\in S_C\cap H}|\mathcal A_v|.
\]
Checks disjoint from a bounded kernel inflate only by \(1+O_r(f/n)\).
If the conditioned residual is still heavy, one of at most
\(\sum_{j\le r-1}\binom fj\) kernel-intersection patterns carries the
amplified obstruction. Thus the remaining expansion theorem may work
with a low-load residual or one explicit kernel star, not an
unstructured conditioning loss.

OP2k bounds every such kernel star. For one fixed intersection
\(J\subseteq H\), surviving checks share the literals
\(\alpha|_J\), so residualization is injective and preserves the
antichain property. Its amplified source mass is therefore at most one.
Summing gives an explicit \(P(f,r)\) ceiling for the entire amplified
audit. Conditioning on a bounded kernel can now produce only finitely
many unit-Lubell kernel stars; OP2 still has to expand or classify each
star arithmetically.

[`orbit-phase-literal-star-router.md`](orbit-phase-literal-star-router.md)
proves OP2l--OP2m for the one-literal stars actually activated by a
phase change.  Fixing the target centre phase leaves residual scopes of
size at most two, and every residual forbidden literal equals its
current phase.  The bucket is therefore exactly a transversal system.
A maximal residual matching of size \(\nu\) gives a transversal of size
at most \(2\nu\): either there are \(m\) disjoint blocker arms, or at
most \(2(m-1)\) auxiliary phase changes block the entire bucket.
Weighted bucket mass \(W\) similarly yields either a current residual
literal of load greater than \(\Delta\), extending the fixed kernel, or
at least \(\lceil W/(2\Delta)\rceil\) disjoint arms.  The remaining
arithmetic task is now confined to those paid depth-two kernels and
large disjoint-arm families.

[`orbit-phase-external-collateral.md`](orbit-phase-external-collateral.md)
proves OP2n for the latter output.  Choose one action variable on each
residual-disjoint arm and restrict it to its noncurrent phases.  Every
selected blocker then disappears, while every external hard check and
weighted soft factor projects exactly to a forced status or a canonical
action check.  The projected instance still has rank at most three, so
the disjoint-arm output can recurse through the same phase machinery
without hiding collateral.

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
`Phi` or increase a bounded structured-core potential.

OP3c in the literal-star router sharpens the one-block identity.  The
destroyed incident weight \(D(v)\) is independent of the target phase,
while all possible creations partition into their unique target
buckets.  Hence some phase creates at most \(E(v)/(h_v-1)\), and
\((h_v-1)D(v)>E(v)\) gives an improving flip.  If no target improves,
every target bucket has weight at least \(D(v)\).  Hard-unsafe targets
return aligned hard blocker stars instead.  OP3 remains open because
its final arithmetic expansion/classification theorem is not yet
proved.

OP3d--OP3f in the external-collateral note close the generic batching
gap.  OP3d audits every correction on its complete support.  OP3e joins
two candidates whenever their supports overlap or a hard/soft check
meets both supports; every independent family is then jointly hard-legal
and has exactly additive drift.  Weighted Caro--Wei extraction either
returns an executable batch with a quantified share of the individual
gain or retains more than half of that gain on degree-at-least-\(D\)
candidates.  Every high-conflict edge keeps an explicit shared-variable
or check-scope witness.  The remaining problem is to classify those
paid edge witnesses arithmetically.

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
OP2f additionally deletes every bounded factor-incidence-treewidth core
through an exact separator table.
OP2g may be applied first: it removes subsumed checks and propagates all
forced labels before any residual conflict-mass or topology estimate.
OP2h then supplies a unit Lubell-mass budget for the resulting
irreducible check family.
OP2i further confines all variables above any fixed normalized-load
threshold to a bounded kernel and gives explicit low-load literals
outside it.
OP2j tracks the exact Lubell amplification caused by conditioning that
kernel and localizes any large residual increase to one kernel
intersection pattern.
OP2k additionally caps every fixed intersection pattern at unit Lubell
mass and the full amplified ancestor audit at \(P(f,r)\).
OP2l--OP2m route every activated one-literal star to a bounded
transversal correction, a paid deeper current-literal kernel, or a
large residual-disjoint blocker family.
OP2n projects every such disjoint-arm family to an exact
rank-at-most-three action CSP with all external collateral retained.
OP3d--OP3f make bounded corrections scope-complete and extract a
weighted independent batch unless paid gain concentrates on witnessed
high-conflict candidates.

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
`scripts/verify_phase_feedback.py`. Bounded-width noncactus ladders are
checked by `scripts/verify_phase_incidence_treewidth.py`.
Activated rank-two literal stars, maximal-matching transversals, paid
residual loads, and exact phase averaging are checked by
`scripts/verify_phase_literal_star_router.py`.  Exact action projection,
external hard/soft collateral, scope-complete correction batches, and
weighted high-conflict extraction are checked by
`scripts/verify_phase_external_collateral.py`.

## Completion criterion

This branch is complete when the remaining OP1 compression and OP2–OP5
provide a rigorous saturation-preserving decoder theorem, not merely an
empirical expansion claim.
