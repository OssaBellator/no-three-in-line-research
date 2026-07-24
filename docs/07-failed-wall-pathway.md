# Failed wall pathway and counterexamples

This chapter records a tempting but false termination argument.

## 1. The proposed wall route

The idea was:

1. expand a shadow-clean reservoir by adding blocks containing high-load anchors or blocker-matching endpoints;
2. complete all reservoir blocks using one common translation or one common affine slope;
3. average over the common state and show eventual negative drift.

Finite-geometry arguments showed that a minimal set of forbidden cells blocking all local affine states can form a full affine wall. This suggested adding wall anchors until the reservoir became repairable.

## 2. Translated-block obstruction

Let \(B\) be an absorber block and choose a vector \(v\) of primitive height at least \(H\). Suppose

\[
B_0=B,
\quad B_1=B+v,
\quad B_2=B+2v
\]

are disjoint in the grid. Install translated copies of every state:

\[
A_{j,\omega}=A_\omega+jv.
\]

For every common state \(\omega\) and every \(z\in A_\omega\),

\[
z,
\quad z+v,
\quad z+2v
\]

form a high collinear triple.

### Counterexample F1 — REFUTED CLAIM

A fully expanded, shadow-clean reservoir need not have any improving synchronized state.

Take all three blocks into the reservoir and choose a current common state minimizing the potential among common states. There are no outside anchors left and no possible expansion, yet every common state has at least \(h\) bad triples.

### Consequences

The following are false without additional hypotheses:

- wall expansion always terminates in negative drift;
- a common translation state suffices;
- switching to a common affine slope resolves the final obstruction.

The defect is synchronization. Independent block states can destroy the translated corresponding-cell triples.

## 3. What survives

The full-product CSP formulation survives:

- each block is a variable with \(h\) states;
- an anchored high line forbids one labelled assignment on two variables;
- a candidate-only high line forbids one labelled assignment on three variables.

Under small normalized conflict mass per variable, the local lemma applies.

## 4. Another failed shortcut

Bounded line occupancy and bounded pair codegree do not imply an expander/private-repair property. Cycle-like labelled CSPs can have:

- no degree-one check;
- no private repair;
- bounded edge size;
- bounded pair codegree.

Arithmetic structure must be used, not only generic sparsity.
