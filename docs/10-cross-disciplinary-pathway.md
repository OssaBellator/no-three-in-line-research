# Cross-disciplinary interpretations

The problem has useful analogues in several applied fields. These analogues suggest algorithms and invariants that are not obvious from pure incidence geometry.

## 1. Radar and Costas arrays

A permutation matrix can represent one pulse in each time slot and each frequency. A repeated displacement produces ambiguity sidelobes. Costas arrays demand every displacement occur once.

Modular hyperbolas have a relaxed two-Costas property: every exact displacement occurs at most twice between two fixed channels. This yields a uniform dyadic secant-shadow bound.

A collinear triple is a third-order chirp ambiguity: three transmissions fit a constant-rate frequency trajectory. The complementary-hyperbola seed suppresses monochromatic third-order ambiguity and confines all defects to cross-channel interactions.

## 2. Error-correcting codes

- selected points are variable assignments;
- collinear triples are failed parity checks;
- row-column-preserving switches are codeword-preserving updates;
- a low-syndrome hyperbola seed is a received word with \(O(n\log n)\) failed checks;
- a stalled local decoder produces a trapping set;
- multiplicative orbit blocks form a structured codebook closed under updates;
- Möbius cycles are algebraically classified trapping cores.

The natural decoder is not generic bit flipping; it is a multiscale cycle decoder whose local state space preserves an algebraic ambiguity bound.

## 3. Discrete tomography

Rows, columns, and protected directions are projection line sums. A switching component is a discrete-tomography ghost: a signed function with zero sums in the measured directions.

Difference-operator trades explain how to preserve any finite direction set exactly. The main difficulty is binary executability and global installation, not the formal kernel.

## 4. Frequency hopping and interleavers

The Hamiltonian representation

\[
S_\pi=
\{(i,\pi(i)),(i,\pi(i+1))\}
\]

is a cyclic interleaver. The design goal is to spread local adjacency under all rational slope projections. This resembles turbo-code interleaver design, where short correlated patterns must be dispersed while preserving a permutation constraint.

## 5. Constraint satisfaction and statistical physics

Orbit block states form a finite-domain CSP. Each high line forbids one labelled assignment on two or three variables. Candidate-only concentration resembles a glassy phase with local minima. Synchronized states correspond to a low-dimensional replica-symmetric ansatz and can be trapped; independent block states are essential.

## 6. Proposed applied-style algorithm

1. Generate several complementary hyperbola seeds.
2. Select a seed minimizing empirical dyadic syndrome.
3. Build the cross-channel syndrome graph.
4. Peel leaves greedily.
5. Extract a Möbius cycle from the core.
6. Enumerate all cyclic matching states.
7. Score each state using exact real-line collateral.
8. Apply the best negative-drift state.
9. Recompute only affected line checks.
10. Escalate a persistent cycle to a SAT/ILP subproblem on its local block.

This hybrid decoder mirrors practical systems: fast local updates for ordinary noise and exact optimization for rare trapping cores.
