# Open bottlenecks and research roadmap

## Bottleneck 1: carry-cycle dispersion

### Conjectured lemma O6

For every real-collinearity Möbius cycle \(C\) of length \(k\), either:

1. some noncurrent cyclic state satisfies
   \[
   \mathcal A(C)<kD(C),
   \]
   hence decreases the triple potential; or
2. the ratio word contains a proper constant-ratio or bounded-window-product subcycle that is itself an executable multiplicative orbit absorber.

### Why it matters

This would classify every residual cross-channel trapping core as either decodable or reducible to a smaller algebraic absorber.

### Main obstacle

The Möbius dynamics is modular, while actual bad triples are filtered by integer representatives and Euclidean carry conditions. A modular secant need not be a real secant in the square.

## Bottleneck 2: cycle collateral

For a cycle bank \(M_s\), decompose the summed collateral

\[
\mathcal A=A_1+A_2+A_3.
\]

- \(A_1\): one cycle cell and two outside points;
- \(A_2\): two cycle cells and one outside point;
- \(A_3\): three cycle cells.

The states partition the cycle block, strongly constraining \(A_1\) and equal-diagonal-label contributions to \(A_2,A_3\). A usable theorem should bound these in terms of \(k\), \(q_s\), and a scale-sensitive outside shadow.

## Bottleneck 3: multiscale preservation

A cycle repair at one height band can create defects at lower heights. Descending-height processing protects higher heights, but the hyperbola cycle states need a compatible reverse-scale potential and admissibility bank.

## Bottleneck 4: all \(n\), not only \(p-1\)

The hyperbola seed naturally lives on \((p-1)\times(p-1)\). A complete proof needs one of:

- an embedding/patching argument between nearby primes;
- a prime-power or composite-modulus analogue;
- a product construction preserving exact two-per-row/column saturation;
- a separate finite set of exceptional sizes.

## Bottleneck 5: computational falsification

Before attempting a universal proof, the following should be exhaustively tested for small primes:

- whether every residual syndrome cycle has an improving cyclic state;
- distribution of \(q_s\) for real carry-filtered cycles;
- existence of cycles with \(\mathcal A\ge kD\) and no proper low-complexity subcycle;
- whether two-channel seeds with primitive ratio empirically outperform arbitrary ratios.

## Recommended order of work

1. Implement exact Möbius cycle extraction and cycle-state scoring.
2. Search for counterexamples to O6 up to at least \(p=101\).
3. If none occur, classify short cycles symbolically.
4. Prove a scale-local \(A_1+A_2\) bound for constant-ratio cycles.
5. Develop an additive-combinatorial inverse theorem for small average window-product complexity.
6. Integrate with descending dyadic scales.
7. Address composite \(n\).
