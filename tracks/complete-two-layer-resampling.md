# Stationary resampling on two edge-disjoint complete matchings

SRR1a treats one perfect matching of \(K_{N,N}\). The exact-cover state
space for SRR3 consists of ordered pairs of edge-disjoint perfect
matchings. A four-cycle switch in one layer has only two possible
cross-layer obstructions, which can be removed while keeping the forward
degree constant.

Let

\[
\Omega_2=
\{(\pi,\rho):\pi,\rho:X\to Y\text{ bijections and }
\pi(x)\neq\rho(x)\text{ for every }x\}.
\]

Fix a labelled layer-one edge \(e=(i,j)\), and let

\[
A=\{(\pi,\rho)\in\Omega_2:\pi(i)=j\}.
\]

Assume \(N\geq4\). For a flawed state define

\[
b_1=\pi^{-1}(\rho(i)),
\qquad
b_2=\rho^{-1}(j).
\]

Both differ from \(i\). Swapping \(\pi(i)\) and \(\pi(u)\) preserves
edge-disjointness exactly when \(u\notin\{b_1,b_2\}\).

Choose a fixed ordering of \(X\). If \(b_1\neq b_2\), allow every row
outside \(\{i,b_1,b_2\}\). If \(b_1=b_2\), additionally discard the first
row outside \(\{i,b_1\}\). In both cases the allowed set has exactly

\[
L=N-3
\]

rows.

## SRR3a -- complete two-layer stationary oracle

### Theorem SRR3a -- PROVED

The selected layer-one four-cycle switches form a bipartite switching
graph between \(A\) and \(\Omega_2\setminus A\) with:

1. forward degree exactly \(N-3\) at every flawed state;
2. reverse degree at most one at every nonflawed state;
3. every switch preserving both perfect matchings and their
   edge-disjointness;
4. every forward switch removing \(e\);
5. symmetric difference equal to one four-cycle in the selected layer.

Consequently the balanced switching kernel of SRR1b is reversible and
stationary for the uniform measure on \(\Omega_2\), and it removes every
labelled forbidden partial matching containing \(e\). The same result
holds with the two layers exchanged.

### Proof

In a flawed state, \(\pi(i)=j\) and \(\rho(i)\neq j\), so
\(b_1,b_2\neq i\). After swapping the images of \(i\) and \(u\), the only
new possible cross-layer collisions are

\[
\pi(u)=\rho(i)
\quad\text{at row }i,
\qquad
j=\rho(u)
\quad\text{at row }u.
\]

These occur exactly at \(u=b_1\) and \(u=b_2\). The selected rows avoid
both, proving edge-disjointness. The canonical extra deletion when they
coincide makes the number of choices exactly \(N-3\).

No selected \(u\) carries \(j\) in \(\pi\), because row \(i\) is its
unique preimage. Thus the swapped layer avoids \(e\). Swapping two images
of one permutation preserves both permutation layers and changes exactly
the four edges of their alternating four-cycle.

Now fix a nonflawed output \((\pi',\rho)\). Any reverse switch introducing
\((i,j)\) must use the unique row

\[
u=(\pi')^{-1}(j).
\]

That row determines the predecessor by swapping \(i\) and \(u\), so there
is at most one reverse switching edge. SRR1b applies with
\(L=N-3\): a flawed state chooses each forward edge with probability
\(1/L\); a nonflawed state uses each reverse edge with probability
\(1/L\) and puts the remaining mass on its self-loop. The kernel is
symmetric, stochastic, stationary, and reversible.

If a labelled forbidden partial matching contains \(e\) in layer one,
removing \(e\) removes that event. Layer symmetry gives the other case.
\(\square\)

## Scope

This proves the stationary and exact-cover-preservation parts of SRR3 in
the complete host. A geometric conflict can be split into at most
\(2^3\) labelled layer assignments, and each labelled event may choose
one distinguished edge for this oracle.

The remote-event estimate is still required before an iterative local
lemma can use these oracles. In a superregular host, missing cross edges
also require longer switching cycles and a Hall/flow argument.

`scripts/verify_complete_two_layer_resampling.py` exhaustively checks the
switching degrees, exact-cover invariants, reversibility, and stationarity
for \(N=4,5\).
