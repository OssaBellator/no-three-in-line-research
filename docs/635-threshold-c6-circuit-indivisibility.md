# Threshold `C6` circuit indivisibility

`docs/629` identifies each nearest legal threshold replacement as a simultaneous
alternating six-cell cycle on three source rows and three action columns.  This
chapter proves that the six-cell operation cannot be split into smaller visible
margin-preserving edits.

## 1. Transportation-kernel circuit

### Theorem PP3cxt -- PROVED / ALTERNATING-CYCLE CIRCUIT

For every one of the eight nearest legal targets, the six signed source changes
form a circuit of the integer row-column transportation kernel.

#### Proof

Each of the three participating rows and columns is incident with one `+1` and
one `-1`.  Hence the full signed support has zero row and column margins.  Its
support graph is a simple alternating cycle, and deleting any support edge leaves
an endpoint of nonzero signed degree.  ∎

## 2. Complete subset audit

### Theorem PP3cxu -- PROVED / NO PROPER BALANCED SUBSET

For each target, among the `2^6=64` subsets of its signed support, exactly two
have zero row and column margins: the empty subset and the complete six-cell
cycle.

#### Proof

The checker evaluates the four row sums and four column sums for all subsets of
all eight supports.  Every proper nonempty subset has a nonzero margin.  ∎

## 3. Exposed-state consequence

### Theorem PP3cxv -- PROVED / ATOMIC SOURCE-OPERATION REQUIREMENT

No sequence of two or more nonempty visible sub-edits can implement a target
while preserving all source margins after every visible step.  At least one
visible step must contain the complete six-cell signed cycle.

Thus the missing prime-patching operation is not merely a convenient compound of
two conservative swaps: it must be a genuine atomic `C6` primitive, or a larger
geometric edit whose visible source-margin change contains that full circuit.
Exposed no-three legality remains unproved.
