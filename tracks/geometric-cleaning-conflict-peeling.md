# Exact high-load peeling for candidate-only conflicts

GC4 needs to reduce normalized candidate-only conflict load or return a
dense structured obstruction.  The combinatorial part of that dichotomy
is an exact weighted peeling statement.

Let \(V\) be the variables of a clone host or block product space.  Let
\(\mathcal C\) be a finite family of nonempty conflicts with weights
\(a_C>0\).  For \(D\subseteq V\), write

\[
d_D(v)=
\sum_{\substack{C\in\mathcal C\\C\subseteq V\setminus D\\v\in C}}a_C
\]

for the surviving normalized conflict load at \(v\), and put

\[
W=\sum_{C\in\mathcal C}a_C.
\]

## GC4a -- high-load peeling certificate

### Theorem GC4a -- PROVED

For every threshold \(\tau>0\), there is a deletion set \(D\) such that

\[
\max_{v\in V\setminus D}d_D(v)\leq\tau
\]

and

\[
\boxed{|D|\tau<W}
\]

unless \(D=\varnothing\), in which case the desired load cap already
held.

More precisely, the algorithm returns an ordering

\[
D=(v_1,\ldots,v_k)
\]

such that, immediately before \(v_i\) is deleted,

\[
d_{\{v_1,\ldots,v_{i-1}\}}(v_i)>\tau.
\]

The conflict weight removed at different steps is disjoint.  Therefore,
if a proposed budget permits deletion of at most \(k_0\) variables, then
one of the following exact alternatives holds:

1. the residual maximum load is at most \(\tau\) after at most \(k_0\)
   deletions;
2. the first \(k_0+1\) vertices form an ordered high-load witness carrying
   more than \((k_0+1)\tau\) distinct conflict weight.

### Proof

Start with \(D=\varnothing\).  While a surviving vertex has load greater
than \(\tau\), choose one such vertex \(v\), append it to \(D\), and
delete every surviving conflict containing \(v\).

The conflicts deleted at one step never appear at a later step.  The
weight deleted at the step for \(v_i\) is exactly its current load, hence
is greater than \(\tau\).  If the algorithm makes \(k\) deletions, it
therefore removes more than \(k\tau\) total weight.  Since it can remove
at most the original weight \(W\), \(k\tau<W\).  At termination no
surviving vertex has load greater than \(\tau\).

If the algorithm reaches step \(k_0+1\), the first \(k_0+1\) deleted
conflict families are disjoint and each has weight greater than
\(\tau\), which is the second alternative.
\(\square\)

## Consequences and remaining geometric step

If \(W\leq\epsilon|V|\tau\), GC4a gives the required cap after fewer than
\(\epsilon|V|\) deletions.  This is an exact sufficient condition; it
does not apply to the known \(\Omega(n^4\log n)\) latent triple mass when
the endpoint threshold is much smaller.

When the deletion budget is exceeded, the ordered witness is stronger
than a repeated high degree in the original hypergraph: every step
carries fresh conflict weight surviving all earlier deletions.  GC4's
remaining geometric task is precisely to show that a long such witness
in the collinearity hypergraph has algebraic structure, and then to charge
that structure to current syndrome incidence before delegating it to an
absorber or alternating bank.  The peeling lemma itself does not turn
latent conflict weight into paid weight.

The same algorithm can be run separately on pair, triple, row, and column
loads, with the deletion budgets added.  Thus it feeds either the P1
normalized-load endpoint or the D1 row/column-load endpoint.

`scripts/verify_conflict_peeling.py` exhaustively checks the disjoint
charge identity and residual cap for small pair/triple hypergraphs.
