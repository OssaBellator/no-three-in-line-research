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

## BDA1 — q-striped chamber decomposition — PROVED

### Target statement

For every fixed integer `q>=2`, partition the perfectly aligned base parameters into `O_q(1)` classes such that within each class:

1. the source and target wrap indices have fixed residues modulo `q`;
2. the active points lie in explicit arithmetic intervals or multiplicative cosets;
3. every row and column is used at most once by each permutation layer;
4. the corresponding aligned triples share one finite list of rational interpolation patterns.

The decomposition must be canonical under the red–blue channel swap and stable under deletion of `O_q(1)` exceptional points.

### Resolution

[`bounded-denominator-strip-proof.md`](bounded-denominator-strip-proof.md)
partitions arbitrary wrap residues into exactly `q^2` canonical classes of
explicit carry intervals.  PA2 identifies a perfect chamber with the
zero-zero class, and the note derives its single rational interpolation
pattern directly.  The construction is invariant under source-target
reversal and point deletion.  `scripts/verify_q_strips.py` exhaustively
checks the interval and interpolation identities through `p=43`.

## BDA2 — local alternating absorber — PARTIAL

### Target statement

For each fixed denominator `q`, there is a constant `h(q)` and a finite family of row-column-preserving signed trades, each supported on at most `h(q)` active rows and columns, with this property:

Given a q-striped perfect chamber containing at least `h(q)` paid aligned certificates, one may select one trade whose positive state is the current local state and whose alternative state:

- preserves two points per active row and column;
- preserves disjointness of the two permutation layers;
- destroys a positive fraction `c_q` of the paid chamber certificates;
- creates at most `c_q/2` times that number of new certificates outside protected higher-height lines.

A bank version with a spread distribution is also acceptable.

### Proved state-bank component

[`bounded-denominator-local-bank.md`](bounded-denominator-local-bank.md)
proves BDA2a: every selected chamber block of at least seven cells has a
collision-free row-column-preserving permutation bank with the exact AN1
cylinder bounds and an AN4-type collateral formula.

The same note proves the support obstruction BDA2b. A trade on `h(q)`
rows cannot destroy a fixed fraction of arbitrarily many cell-private
certificates. Thus the remaining BDA2/BDA3 work must prove paid incidence
concentration on bounded blocks or select a parallel bank of such blocks;
bounded support alone is insufficient.

## BDA3 — finite conflict regularization

### Target statement

The local trades from BDA2 can be selected on a linear-size disjoint subfamily of chamber blocks so that the labelled pair/triple conflict mass per block is `O_q(1)`. Consequently either:

1. one block improves immediately;
2. the product-state local lemma produces a joint improving state;
3. the blocks organize into one of finitely many q-periodic frozen templates.

The proof must use the bounded denominator and explicit wrap-index residues; generic bounded codegree is insufficient.

### Proved combinatorial reduction

[`bounded-denominator-conflict-regularization.md`](bounded-denominator-conflict-regularization.md)
proves BDA3a. If the total integer labelled conflict mass on \(n\)
candidate chamber blocks is at most \(D_qn\), deterministic
regularization retains at least half the blocks with load at most
\(4D_q\), and greedy colouring extracts a linear-size compatible
subfamily. In the paid weighted form, either such a family retains a
constant fraction of paid mass or more than half the paid mass lies on
high-load blocks. Thus the remaining BDA3 step is the \(q\)-stripe
arithmetic bound on total conflict mass, or classification of its
high-load alternative as a periodic template.

[`bounded-denominator-product-bank.md`](bounded-denominator-product-bank.md)
proves BDA3b. On any compatible block family, the independent product of
the BDA2a banks has an exact normalized collateral sum over every local
and cross-block candidate triple. If paid destroyed weight exceeds fixed
collateral plus that sum, a joint improving state exists. Thus the
remaining BDA3 arithmetic must bound this explicit sum or classify the
quantified high-collateral family.

[`bounded-denominator-profile-localization.md`](bounded-denominator-profile-localization.md)
proves BDA3c. Once the \(q\)-stripe arithmetic partitions collateral
triples into \(L_q\) finite profiles, failure of the BDA3b inequality
forces one profile to carry at least \((W-F)_+/L_q\) normalized
collateral, with an explicit conversion to raw candidate weight. This
removes mixtures of residue, carry, and rank types from the BDA4 input.
BDA3d unconditionally reduces the block-rank component to one of six
patterns, carrying at least \((W-F)/6\) when \(W>F\). The remaining
arithmetic task is to prove \(L_q=O_q(1)\) for the actual strip
residue/carry signatures and classify each heavy profile.

[`bounded-denominator-finite-transition.md`](bounded-denominator-finite-transition.md)
proves BDA3e: the intrinsic strip/rank/interpolation word has at most
\(6(q^2\varphi(q))^3\) values. It also proves BDA4a: once the remaining
geometric address is compressed to a complete finite profile, every
long non-improving trajectory reaches a directed profile cycle of length
at most the number of profiles. The unresolved arithmetic is now
precisely the finite refinement of block identities, anchors, coarse
carries, and channel data, followed by classification of those cycles.

[`bounded-denominator-relative-address.md`](bounded-denominator-relative-address.md)
proves BDA3f: the collinearity determinant discards absolute coarse
positions and depends only on coordinate residues and four relative
quotient variables. A relative window of width \(W\) therefore costs at
most \((2W+1)^4\) additional profiles. The same note proves the
residue-only wall: identical residue triples can be collinear or
noncollinear, so some relative carry information is genuinely necessary.
The remaining address problem is now relative rather than absolute.

[`bounded-denominator-primitive-slope.md`](bounded-denominator-primitive-slope.md)
proves BDA3g. On every compatible collinear triple the four coordinate
differences factor uniquely as

\[
(U,S)=m(a,b),\qquad(V,T)=n(a,b)
\]

with \((a,b)\) a normalized primitive spatial direction, and the two
point scales satisfy four explicit congruences modulo \(q\). Thus an
unbounded relative-address escape is a primitive-slope/scale chain, not
an arbitrary four-variable profile. Finiteness is still open, but BDA4
may now classify repeated slopes via the CR/WQ interface and charge
genuinely new direction classes.

[`bounded-denominator-valuation-charts.md`](bounded-denominator-valuation-charts.md)
proves BDA3h. Prime power by prime power, the minimum valuation of the
four difference residues equals the common valuation of the two point
scales. After dividing it out, the residue matrix has a unit pivot which
recovers both the primitive-direction and relative-scale projective
classes. A local component is invisible exactly when both scales vanish
modulo that full prime power. Hence the remaining singular slope chain
is a common-scale valuation tower, not an arbitrary composite-modulus
zero-divisor case.

The same note proves BDA4b, which makes that tower finite inside every
actual grid box. Removing one common prime factor from both point scales
decreases the exact height
\(V_q=\sum_{\ell\mid q}\min(v_\ell(m),v_\ell(n))\) by one, and
\[
V_q\leq\sum_{\ell\mid q}\lfloor\log_\ell N\rfloor.
\]
After the unique \(q\)-smooth common content is removed, every
prime-power component has a full-precision unit pivot. Thus BDA4 no
longer has an internally infinite singular-division case; it must
classify the resulting \(q\)-primitive profiles and their genuine
transition cycles.

It also proves BDA3i, which glues all prime-power unit-pivot charts by
CRT. The normalized residue matrix uniquely determines its direction
and scale classes in \(\mathbb P^1(\mathbb Z/q\mathbb Z)\), whose size
is \(q\prod_{\ell\mid q}(1+1/\ell)\). Including the unique unit scalar,
there are exactly
\(\varphi(q)|\mathbb P^1(\mathbb Z/q\mathbb Z)|^2\) unimodular
rank-one residue matrices. Thus the remaining address escape is in
integer lifts and genuine profile cycles, not a hidden composite-ring
factorization ambiguity.

BDA3j gives those integer lifts a unique normal form. Every address is
\(h(a,b)^{\mathsf T}(u,v)\), with both two-vectors primitive and
\(h>0\); its exact box height is
\(h\|(a,b)\|_\infty\|(u,v)\|_\infty\). The BDA4b common content is
exactly the \(q\)-smooth part of \(h\), so after content removal the
only radial parameter is a unit modulo \(q\). The unbounded BDA4
classification is therefore reduced to two primitive rational
directions and one coprime radial scalar, rather than four unrelated
integer lifts.

[`bounded-denominator-lift-separation.md`](bounded-denominator-lift-separation.md)
proves BDA3k. Distinct primitive lifts in one projective residue class
have determinant a nonzero multiple of \(q\), hence their rational
slopes are separated by at least \(q/A^2\) under norm bound \(A\).
It also proves BDA4c: within one complete atlas profile and bounded
slope windows, a large lift family repeats one exact pair of primitive
factors; the remaining radial parameters then occupy one residue class
modulo \(q\). Thus the only unbounded alternatives are quantitatively
separated rational directions or a single \(q\)-spaced radial chain.
The remaining classification must charge the former through
carry/wrap-center dispersion and send the latter through the
common-ratio or subgroup-coset interfaces.

BDA4d adds the density threshold needed for that interface. A radial
chain of \(K\) addresses in matrix-height box \(N\) forces
\[
N\geq
\|d\|_\infty\|c\|_\infty\bigl(1+q(K-1)\bigr).
\]
Consequently any chain with \(K\geq\delta N\) has primitive factor
height \(O(1/(q\delta))\), leaving only a finite shape library. A chain
dense in its permitted radial progression also contains a linear
matching of \(q\)-adjacent parameters, all with the same rank-one
increment \(qdc^{\mathsf T}\). The remaining geometric blocker is
anchor/translation regularization for these identical increments.

[`bounded-denominator-radial-pair-regularization.md`](bounded-denominator-radial-pair-regularization.md)
proves BDA4e. An adjacent radial-pair support uses at most five rows and
five columns when the two relative types occur at one common anchor.
Bounded coordinate load therefore yields a
constant-fraction paid compatible subfamily by an explicit conflict
colouring. High coordinate load instead concentrates a constant share
of that coordinate's current paid incidence on one of five affine
anchor laws. The remaining absorber construction may consequently work
with compatible common increments or with a one-dimensional paid anchor
chain. The remaining prerequisite is paid co-anchor extraction, or a
classification of why adjacent relative types fail to co-anchor.

BDA4f supplies that extraction above an exact half-capacity threshold.
If aggregate occurrence weights \(w_{P,j}\leq\beta\) occupy \(J\)
radial slots at each anchor, total paid mass \(W\) produces adjacent
co-anchored overlap at least
\[
\bigl(2W-\beta|\mathcal A|(J+1)\bigr)_+.
\]
An odd/even split retains half of this weight on radially disjoint
pairs, which can then enter BDA4e. Failure is the explicit complementary
low-occupancy inequality, not an unspecified co-anchoring obstruction.

[`bounded-denominator-radial-rectangle-decoder.md`](bounded-denominator-radial-rectangle-decoder.md)
proves BDA5a--BDA5b for one clean co-anchored adjacent pair. On either
radial role, the opposite rectangle diagonal is empty, full in the
other colour, or singly blocked. The first case gives a one-layer
rectangle switch; the second gives an exact two-colour phase flip; and
if neither is available, the two roles give disjoint one-blocker
alternating-path seeds. Every admissible state destroys both radial
triples, leaving only its explicitly measurable collateral.

BDA5c couples any compatible family of at least two single-blocker
rectangles, including the two roles of one clean radial pair. All active
rectangles are switched simultaneously, while the opposite-layer
blocker cells are rematched by a derangement. This preserves both layers
and frees every desired cross cell. For families of size at least seven,
BDA5d applies AN1 to give the exact normalized rank-one, rank-two, and
rank-three collateral criterion. BDA5e closes the last local occupancy
case: every clean pair has a legal one- or two-layer decoder, so only
its explicit collateral remains to be paid.

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

The cyclic two-forbidden-matching local bank and deterministic conflict
regularization are retained as exhaustive regressions in
`scripts/verify_bda_local_bank.py` and
`scripts/verify_bda_conflict_regularization.py`. Product-bank cylinder
factorization is checked by `scripts/verify_bda_product_bank.py`.

Any frozen template must be added to BDA4 rather than hidden in an asymptotic estimate.

## Completion criterion

This branch is complete when BDA2–BDA5 are proved for every fixed `q`, with an effective dependence on `q` and an exact interface usable by the alternating-core branch. BDA1 is now proved.
