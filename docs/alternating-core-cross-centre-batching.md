# Cross-centre blocker batching under bounded residual reuse

**Branch:** `research/alternating-core-chain`

AC3aj--AC3ak can return a family of alternative-target blocker arms whose residual supports are disjoint within each arm. This note gives the exact batching statement available as soon as residual-block reuse is bounded. It also identifies the only obstruction: one residual block reused by many arms.

## Setup

Let \(\mathcal A\) be a finite family of alternative-target blocker arms. Each arm \(a\) has nonnegative paid target weight \(w(a)\) and a residual support \(S(a)\) with

\[
|S(a)|\le 2.
\]

Assume the current scope-complete conflict model has the following property: two arms with disjoint residual supports are jointly installable, and every conflict between arms is witnessed by a shared residual block. Put

\[
W=\sum_{a\in\mathcal A}w(a).
\]

## AC3al — bounded-reuse cross-centre batching — PROVED

For every integer \(\rho\ge1\), one of the following holds:

1. some residual block belongs to more than \(\rho\) arm supports; or
2. there is a jointly installable family \(\mathcal I\subseteq\mathcal A\) satisfying
   \[
   \boxed{
   \sum_{a\in\mathcal I}w(a)
   \ge
   \frac{W}{2\rho-1}.
   }
   \]

### Proof

Suppose outcome 1 fails. Form the intersection graph on \(\mathcal A\), joining two arms when their residual supports meet. Fix an arm \(a\). Each block in \(S(a)\) belongs to at most \(\rho-1\) other arm supports, and \(|S(a)|\le2\). Therefore

\[
\deg(a)\le2(\rho-1).
\]

The intersection graph has maximum degree at most \(2\rho-2\), so greedy colouring uses at most \(2\rho-1\) colours. Each colour class has pairwise disjoint residual supports and is jointly installable by the scope-complete hypothesis. One colour class carries at least a \(1/(2\rho-1)\) fraction of the total weight. \(\square\)

## Consequence for the AC3 router

The support-disjoint alternative-target output of AC3ak now has an exact dichotomy. Bounded residual reuse gives a constant-fraction installable paid batch. Failure is not a diffuse incompatibility graph: it is one current residual block supporting more than \(\rho\) alternative-target arms. That high-reuse block can be passed directly to the one-block phase-fan, depth-two literal, orbit-phase, rational-inverse, or bounded-denominator classification interfaces.

The theorem does not claim that the resulting batch improves; its joint collateral still has to be audited. It completes the combinatorial installation step under the stated scope-complete conflict model.

## Finite check

`scripts/verify_ac_cross_centre_batching.py` exhausts small support systems, positive integer weights, and all reuse thresholds. It verifies the high-reuse alternative and the weighted disjoint-support bound.
