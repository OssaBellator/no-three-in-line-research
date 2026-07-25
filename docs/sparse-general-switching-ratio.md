# Exact labelled switching ratio for arbitrary alternating cycles

The four-cycle theorem SAS2a has reverse multiplicity one.  Longer cycles
can have many descriptions leading to the same output.  The correct
counting statement retains those labels and pays exactly for their
maximum reverse multiplicity.

Let \(\Omega\) be a finite nonempty matching state space and fix an edge
\(e\).  Write

\[
A=\{M\in\Omega:e\in M\},
\qquad
B=\Omega\setminus A.
\]

Let \(\mathcal D\) be any finite multiset of labelled valid
alternating-cycle switches from \(A\) to \(B\).  Parallel descriptions are
retained.  Write \(d^+(M)\) for the number of descriptions sourced at
\(M\in A\), and \(d^-(M')\) for the number terminating at \(M'\in B\).

## SAS2b -- general switching-ratio theorem

### Theorem SAS2b -- PROVED

If

\[
d^+(M)\geq L>0\quad(M\in A),
\qquad
d^-(M')\leq R\quad(M'\in B),
\]

then, for the uniform measure on \(\Omega\),

\[
\boxed{
\Pr(e\in M)
\leq
\frac{R}{L+R}.
}
\]

In particular, if \(L/R\geq cd\), then

\[
\Pr(e\in M)\leq\frac1{1+cd}\leq\frac1{cd}.
\]

### Proof

Count labelled switching descriptions by their source and target:

\[
L|A|
\leq
|\mathcal D|
\leq
R|B|.
\]

Thus \(L|A|\leq R(|\Omega|-|A|)\), which rearranges to

\[
(L+R)|A|\leq R|\Omega|.
\]

Division by \((L+R)|\Omega|\) proves the result.
\(\square\)

No injectivity of a switching description is assumed.  The reverse
factor \(R\) is exactly the price of ambiguous cycle decompositions.

## SAS3c -- conditioned arbitrary-cycle version

Let \(Q\) be a compatible prescribed partial matching disjoint from
\(e\), and let \(\Omega_Q\) be the matching space after deleting the rows
and columns covered by \(Q\).

### Corollary SAS3c -- PROVED

If a labelled switching family on \(\Omega_Q\) has minimum forward
multiplicity \(L_Q\) and maximum reverse multiplicity \(R_Q\), then

\[
\boxed{
\Pr(e\in M\mid Q\subseteq M)
\leq
\frac{R_Q}{L_Q+R_Q}.
}
\]

### Proof

Conditioning identifies the residual edges with a uniform element of
\(\Omega_Q\).  Apply SAS2b to that state space.
\(\square\)

Consequently, if \(L_Q/R_Q\geq cd\) uniformly after every deletion of
rank at most two, SAS3a supplies rank-three \(O(1/d)\)-spread.  The same
statement for all ranks gives all-rank spread.

## Remaining algebraic-host problem

SAS2 is now reduced to a purely host-specific construction:

1. select one bounded alternating-cycle length, possibly longer than
   four;
2. prove a uniform lower bound on labelled cycles removing \(e\);
3. canonicalize enough of each cycle that the reverse description count
   is smaller by a factor \(\Omega(d)\);
4. preserve that ratio after the vertex deletions needed for conditioning
   and after deleting the first perfect matching.

The degree-two high-girth cycle remains a valid warning: its edge
probability is \(1/2\), but any useful description family must use the
whole alternating cycle rather than a nonexistent four-cycle.

`scripts/verify_general_switching_ratio.py` exhaustively checks the exact
bound for labelled switching multigraphs with up to three states on each
side and edge multiplicity at most two.
