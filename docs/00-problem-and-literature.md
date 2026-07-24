# Problem, conventions, and literature

## Problem

Let \([n]^2=\{1,\ldots,n\}^2\). Define \(D(n)\) as the largest size of a subset \(S\subseteq[n]^2\) such that every Euclidean line contains at most two points of \(S\).

Rows alone give the upper bound

\[
D(n)\le2n.
\]

The conjecture is that equality holds for every \(n\).

## Current external status

As of 24 July 2026, the conjecture remains open. Ghosal, Goenka, Grebennikov, Keevash, Kwan and Pham proved that for every fixed \(k\ge3\) and sufficiently large \(n\), the maximum size of a subset of the \(n\times n\) grid with at most \(k\) points per line is exactly \(kn\). Their paper explicitly excludes \(k=2\).

Kovács, Nagy and Szabó developed randomised algebraic constructions and improved lower bounds for the general no-\((k+1)\)-in-line problem. These works reinforce the role of modular/algebraic constructions, but do not prove \(D(n)=2n\).

## Conventions

- A **real line** is an ordinary Euclidean line in the integer grid.
- A **toroidal fibre** is a congruence class such as \(bx-ay\equiv c\pmod n\). Every real line of direction \((a,b)\) lies in one toroidal fibre, but a fibre may contain several disjoint real line segments.
- A primitive direction is \((a,b)\in\mathbb Z^2\) with \(\gcd(a,b)=1\).
- Its height is
  \[
  h(a,b)=\max(|a|,|b|).
  \]
- The maximum number of grid points on a line of height at least \(H\) is
  \[
  \ell_H=1+\left\lfloor\frac{n-1}{H}\right\rfloor.
  \]
- A configuration is **saturated** when it contains exactly two points in every row and column.

## Core warning

Several seductive arguments become false when one silently replaces Euclidean collinearity by modular collinearity. This repository always states which notion is in use.

## References

1. A. Ghosal et al., *No-\((k+1)\)-in-line problem for \(k\ge3\)*, arXiv:2607.05255.
2. B. Kovács, Z. L. Nagy, D. R. Szabó, *Randomised algebraic constructions for the no-\((k+1)\)-in-line problem*, arXiv:2508.07632.
3. S. Glock et al., *Conflict-free hypergraph matchings*, arXiv:2205.05564.
4. F. Joos, D. Mubayi, Z. Smith, *Conflict-free Hypergraph Matchings and Coverings*, arXiv:2407.18144.
5. M. Ceko, S. Pagani, R. Tijdeman, *Algorithms for linear time reconstruction by discrete tomography II*, arXiv:2010.07862.
