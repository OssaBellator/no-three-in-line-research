# A balanced switching-graph criterion for stationary resampling

The complete-host oracle uses four-cycles available everywhere.  This note
gives an exact sufficient condition for the same stationary flaw-removal
mechanism in an arbitrary matching space.

Let \(\Omega\) be a finite matching state space with the uniform measure,
and let \(A\subsetneq\Omega\) be the flaw event that a prescribed partial
matching is present.  Build a bipartite switching graph

\[
\Gamma\subseteq A\times(\Omega\setminus A).
\]

An edge records one allowed alternating-cycle switch.

## SRR1b -- balanced switching criterion

### Theorem SRR1b -- PROVED

Suppose every state in \(A\) has exactly \(L\geq1\) switching neighbours
and every state in \(\Omega\setminus A\) has at most \(L\) reverse
neighbours.  Define a Markov kernel \(K\) by:

- from \(\omega\in A\), choose each switching neighbour with probability
  \(1/L\);
- from \(\omega\notin A\), move to each reverse neighbour with probability
  \(1/L\) and stay put with the remaining probability
  \(1-\deg_\Gamma(\omega)/L\).

Then:

1. every transition from a flawed state removes the flaw;
2. the uniform measure on \(\Omega\) is stationary;
3. \(K\) is reversible;
4. if every switching edge is supported on at most \(s\) alternating
   cycles and \(m\) matching edges, the resampling support has those same
   deterministic bounds.

### Proof

Every neighbour of a vertex in \(A\) lies outside \(A\), proving flaw
removal.  Across every switching edge the transition probability in each
direction is \(1/L\).  All remaining mass is placed on a diagonal
self-loop, so \(K\) is symmetric and every row sums to one.  A symmetric
stochastic matrix is doubly stochastic and reversible with respect to the
uniform measure.  The support assertion is inherited from the switching
labels. \(\square\)

The exact-left-degree assumption can be implemented with labelled
switching descriptions: duplicate descriptions are allowed provided their
reverse multiplicity is counted.  What matters is the transition weight,
not whether the underlying unlabelled neighbour is repeated.

## Remote-event clause

Let \(B\) be another matching event.  Couple the input and output through
one switching edge.  If the status of \(B\) can change only when the
switching support meets a controlled neighbourhood \(N(B)\), then

\[
\Pr(B\text{ after resampling}\mid A)
\leq
\Pr(B\mid A)
+\Pr(\text{switch meets }N(B)\mid A).
\]

Thus the SRR1 remote-event estimate reduces to two quantitative inputs:

1. a lopsided bound comparing \(\Pr(B\mid A)\) with \(\Pr(B)\);
2. a switching-locality bound of order \(o(\Pr(B))\), or a sharper
   cancellation argument.

Stationarity alone does not provide either input.

## Complete-host specialization

For a distinguished edge \(e=(i,j)\) in \(K_{N,N}\), let \(A\) be the
matchings containing \(e\).  From a flawed matching, swap the image of
\(i\) with the image of any one of the other \(N-1\) rows.  Hence
\(L=N-1\).  A matching avoiding \(e\) has exactly one reverse description:
the other row is the row currently matched to \(j\).  The theorem therefore
gives a stationary four-cycle oracle with a self-loop of mass
\((N-2)/(N-1)\) at every nonflawed state.

For a superregular host, SRR1 is now reduced to constructing a bounded
alternating-cycle switching graph with:

- uniform or weight-balanced forward degree;
- reverse multiplicity no larger than the forward degree;
- a remote-neighbourhood estimate.

The first two bullets are a matching-space switching theorem; spread by
itself does not imply them.
