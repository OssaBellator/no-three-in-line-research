# An exact sparse four-cycle switching ratio

This note proves SAS2 for any host satisfying one concrete, checkable
switching hypothesis.  The hypothesis is strong and need not hold in every
intended sparse algebraic host; when it fails, longer alternating cycles
are still required.

Let \(G=(X,Y;E)\) be a balanced bipartite graph with nonempty perfect
matching space \(\Omega\), equipped with the uniform measure.  Fix an edge
\(e=(x,y)\).  For \(M\in\Omega\) containing \(e\), define

\[
S_M(e)=
\left\{
u\in X\setminus\{x\}:
(u,y)\in E,\ (x,M(u))\in E
\right\}.
\]

Each \(u\in S_M(e)\) supplies the alternating four-cycle switch

\[
\{(x,y),(u,M(u))\}
\longrightarrow
\{(x,M(u)),(u,y)\}.
\]

## SAS2a -- four-cycle switching theorem

### Theorem SAS2a -- PROVED

If

\[
|S_M(e)|\geq L
\]

for every perfect matching \(M\) containing \(e\), then

\[
\boxed{
\Pr(e\in M)\leq\frac1{L+1}.
}
\]

In particular, if \(L+1\geq c d\), then

\[
\Pr(e\in M)\leq\frac1{cd}.
\]

### Proof

Count labelled forward descriptions \((M,u)\) with \(e\in M\) and
\(u\in S_M(e)\).  There are at least
\(L|\Omega_e|\), where \(\Omega_e\) is the set of matchings containing
\(e\).

For a matching \(M'\) avoiding \(e\), a reverse description is unique if
it exists.  Indeed, the row \(u\) must be the unique row matched to \(y\)
in \(M'\), and the other cross edge must be
\((x,M'(x))\).  Switching those two edges back determines \(M\).
Therefore every \(M'\in\Omega\setminus\Omega_e\) receives at most one
forward description.  Hence

\[
L|\Omega_e|
\leq
|\Omega\setminus\Omega_e|.
\]

Rearranging gives

\[
\frac{|\Omega_e|}{|\Omega|}
\leq
\frac1{L+1}.
\]

\(\square\)

This is the desired \(O(d)\) forward-to-reverse switching ratio with
reverse multiplicity one.

## SAS3b -- conditioned version

Let \(Q\) be a prescribed compatible matching disjoint from \(e\).  Delete
the rows and columns covered by \(Q\), and call the residual graph \(G_Q\).

### Corollary SAS3b -- PROVED

If every perfect matching of \(G_Q\) containing \(e\) has at least \(L\)
valid four-cycle switches inside \(G_Q\), then

\[
\boxed{
\Pr(e\in M\mid Q\subseteq M)\leq\frac1{L+1}.
}
\]

### Proof

Conditioning on \(Q\) identifies the remaining random edges with a uniform
perfect matching of \(G_Q\).  Apply SAS2a in that graph. \(\square\)

Thus a four-cycle hypothesis stable after deleting any matching of rank at
most two gives the rank-three conditional edge bounds required by SAS3a.

## Scope of the hypothesis

For \(K_{N,N}\), every matching containing \(e\) has
\(|S_M(e)|=N-1\), and SAS2a gives the exact probability \(1/N\).

In contrast, the bipartite cycle with row \(i\) adjacent to columns \(i\)
and \(i-1\) has two perfect matchings but no four-cycle switch when its
length exceeds four.  An edge still has probability \(1/2=O(1/d)\), but
SAS2a has only \(L=0\).  This mandatory regression shows that the theorem
is sufficient, not necessary, and that longer alternating cycles are
essential for high-girth algebraic hosts.

`scripts/verify_sparse_switching.py` checks the exact complete-host ratio,
the reverse multiplicity, and the cycle obstruction.
