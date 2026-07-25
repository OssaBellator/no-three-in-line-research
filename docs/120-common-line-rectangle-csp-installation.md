# Common-line rectangle CSP installation

PP3ok extracts a linear bank of pairwise row/column-disjoint alternating
rectangles. The previous interface PP3ol phrased installation as if the negative
diagonals first had to occur in the current endpoint state. This chapter gives a
more direct formulation: reserve the rectangle resources, choose one diagonal in
each block, and complete the remaining endpoint resources by a residual perfect
matching.

The resulting geometry is exactly a binary rank-at-most-three CNF, with a
quadratic shadow-cost objective.

## 1. Local permutation blocks

Let the extracted rectangles be indexed by \(s\in[k]\). Write their two
diagonals as

\[
D_s^0=\{p_s,t_s\}
\]

and

\[
D_s^1=\{p_s^*,t_s^*\},
\]

where \(D_s^0\) lies on one target-rich obstruction line and \(D_s^1\) is the
opposite rectangle diagonal.

The four endpoint resources of distinct blocks are disjoint.

### Proposition PP3om -- PROVED

Reserve the two left and two right endpoint resources of every block. If the
unreserved endpoint host has a perfect matching \(M_0\), then every binary vector
\(x\in\{0,1\}^k\) defines a perfect matching

\[
M_x
=
M_0\cup\bigcup_{s=1}^kD_s^{x_s}
\]

of the complete endpoint-resource set.

#### Proof

Each diagonal is a perfect matching between the two left and two right resources
of its rectangle. Different blocks use disjoint resources, and \(M_0\) uses only
the complement. Their union covers every left and right resource exactly once. ∎

Thus the rectangle bank is installable as a permutation family without first
realizing one chosen diagonal in the source.

## 2. Exact no-three CNF

Fix the retained source, patch points outside the bank, and the residual matching
\(M_0\). Let \(F\) denote their selected point set. Assume the rectangle supports
are disjoint from \(F\).

### Theorem PP3on -- PROVED

There is an explicitly constructible CNF formula \(\Phi\) on variables
\(x_1,\ldots,x_k\) such that

\[
F\cup\bigcup_sD_s^{x_s}
\]

is no-three-in-line if and only if \(x\) satisfies \(\Phi\).

Every clause has rank at most three. If every potentially selected collinear
triple depends nontrivially on at most two rectangle variables, then \(\Phi\) is
2-CNF.

#### Proof

The two states of one rectangle have the same row and column incidence vectors,
and supports of distinct rectangles are disjoint. Apply the exact binary-state
construction PP3bf. A collinear triple meets at most three variable supports, so
its forbidden state conjunction produces a clause of rank at most three. ∎

Unary source blockers become unit clauses, two-block interactions become binary
clauses, and triples using three rectangle blocks become ternary clauses.

## 3. Exact shadow-cost objective

For one installed state, controller-shadow insertion cost has two forms.

- A selected rectangle cell together with one retained source point blocks a
  candidate. This depends on one variable.
- Two selected rectangle cells block a candidate. This depends on at most two
  variables.

Let \(C(x)\) be total inserted shadow and let \(R(x)\) be the removal credit
relative to the chosen preparation state.

### Proposition PP3oo -- PROVED

The exact potential change

\[
\Delta(x)=C(x)-R(x)
\]

is a pseudo-Boolean polynomial of degree at most two:

\[
\Delta(x)
=
\Delta_0
+
\sum_s c_s(x_s)
+
\sum_{s<t}c_{st}(x_s,x_t).
\]

All coefficients are finite nonnegative incidence counts, except for the signed
removal-credit terms already included in \(c_s\) or \(\Delta_0\).

#### Proof

Every source-plus-inserted blocker uses one selected bank cell and is determined
by one local state. Every inserted-plus-inserted blocker uses two selected bank
cells and is determined by at most two local states. No controller-shadow blocker
pair uses three inserted cells. Sum all incidences with multiplicity and subtract
the designated removal credits. ∎

This is the rectangle-bank version of the endpoint potential identity PP3id and
the dynamic excess identity PP3kx.

## 4. Exact installation criterion

### Corollary PP3op -- PROVED

The common-line rectangle bank yields a strict source-admissible improvement if
there are:

1. a residual perfect matching \(M_0\);
2. a satisfying assignment \(x\) of the rank-at-most-three formula \(\Phi\);
3. a negative exact cost \(\Delta(x)<0\).

#### Proof

PP3om gives saturation, PP3on gives the no-three property, and PP3oo together
with PP3id or PP3kx gives strict potential decrease. ∎

When \(\Phi\) is 2-CNF, satisfiability is decidable by the implication graph.
When ternary clauses remain, the bounded-occurrence or local-lemma interfaces
from PP3bh--PP3bl apply.

## 5. Revised rectangle-installation endpoint

### Corollary PP3oq -- PROVED

Failure to convert the PP3ok bank has one of three exact forms.

1. **Residual matching failure:** reserving a proposed rectangle subbank leaves a
   Hall-deficient endpoint host.
2. **Geometric CSP failure:** the corresponding binary rank-at-most-three formula
   has no satisfying assignment.
3. **Paid-cost failure:** source-admissible assignments exist, but every one has
   nonnegative quadratic shadow change.

Thus common-line rectangle extraction and saturation installation are closed.
The remaining work is residual-host preparation and the satisfiable negative-cost
selection theorem for the resulting binary bank.