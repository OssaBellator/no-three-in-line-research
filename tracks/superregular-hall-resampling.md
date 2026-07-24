# Hall characterization of exact stationary flaw removal

The balanced-degree criterion SRR1b is sufficient but not necessary.
Stationarity and guaranteed flaw removal have an exact support-level
characterization: the allowed switching graph must satisfy Hall's
condition.  This removes degree regularity from the existence question.

Let \(\Omega=A\sqcup B\), where \(A\) is the flaw event and \(B\) is its
complement.  Let

\[
\Gamma\subseteq A\times B
\]

be the graph of allowed flaw-removing alternating-cycle switches.
Consider reversible kernels which use only edges of \(\Gamma\), together
with self-loops at states in \(B\).

## SRR1c -- exact Hall criterion

### Theorem SRR1c -- PROVED

The following are equivalent.

1. There is a symmetric stochastic kernel \(K\) on \(\Omega\) such that
   \(K(a,a)=0\) for \(a\in A\), \(K(a,b)>0\) only if \(ab\in\Gamma\),
   and the only transitions from a state in \(B\) are reverse switching
   edges or its self-loop.
2. There are nonnegative edge weights \(w_{ab}\) supported on \(\Gamma\)
   satisfying
   \[
   \sum_{b:ab\in\Gamma}w_{ab}=1\quad(a\in A),
   \qquad
   \sum_{a:ab\in\Gamma}w_{ab}\leq1\quad(b\in B).
   \]
3. For every \(S\subseteq A\),
   \[
   \boxed{|N_\Gamma(S)|\geq|S|.}
   \]
4. The switching graph has a matching saturating \(A\).

Whenever these conditions hold, \(K\) removes the flaw from every input
in \(A\), and the uniform measure on \(\Omega\) is stationary and
reversible.  If every edge of \(\Gamma\) is supported on at most \(s\)
alternating cycles and \(m\) matching edges, the same deterministic
support bounds hold for \(K\).

### Proof

Suppose (1) holds and put \(w_{ab}=K(a,b)\).  A flawed row has no
self-loop and no transition outside \(B\), so its incident weights sum to
one.  A row indexed by \(b\in B\) has total mass one; therefore the mass
it sends across \(\Gamma\) is at most one.  This proves (2).

For \(S\subseteq A\),

\[
|S|
=\sum_{a\in S}\sum_b w_{ab}
\leq
\sum_{b\in N(S)}\sum_a w_{ab}
\leq |N(S)|,
\]

so (2) implies (3).  Hall's marriage theorem gives the equivalence of
(3) and (4).

Given a matching saturating \(A\), pair every \(a\in A\) with its matched
state \(b(a)\).  Set

\[
K(a,b(a))=K(b(a),a)=1.
\]

Give every unmatched state of \(B\) a self-loop of probability one.
This is a symmetric permutation matrix, hence a stochastic, doubly
stochastic, reversible kernel.  Every flawed state moves across
\(\Gamma\), proving (1) and guaranteed flaw removal.  The support bound is
inherited from the selected switching edge.
\(\square\)

The implication (2) to (1) can also be used directly: put
\(K(a,b)=K(b,a)=w_{ab}\) and place the unused column capacity
\(1-\sum_a w_{ab}\) on the self-loop at \(b\).  This fractional form is
the useful one when the remote-event objective requires a dispersed
choice rather than the deterministic Hall matching.

## Consequence for the superregular bottleneck

The stationarity part of SRR1 no longer requires a regular switching
graph.  It is enough to prove the expansion inequality

\[
|N_\Gamma(S)|\geq|S|
\]

for the bounded-cycle switching graph.  The remaining quantitative task
is stronger: choose feasible weights \(w\) whose mass near every remote
event is small.  Hall feasibility alone does not imply that locality
bound, so SRR2 is not upgraded by this theorem.

`scripts/verify_hall_resampling.py` exhaustively checks the equivalence and
the resulting stationary kernels for all switching graphs with at most
three flawed and four nonflawed states.
