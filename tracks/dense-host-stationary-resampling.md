# Exact stationary four-cycle resampling in dense hosts

The complete-host oracles SRR1a and SRR3a equalize every flawed state's
forward degree. Missing host edges make those degrees state-dependent.
For a four-cycle switch, however, every nonflawed output still has at
most one reverse predecessor. This one-sided uniqueness is enough to
normalize each flawed row separately while preserving symmetry.

Let \(G=(X,Y;E)\) be a balanced bipartite graph with
\(|X|=|Y|=N\). For \(x\in X\) and \(y\in Y\), write \(d(x)\) and
\(d(y)\) for their host degrees. Fix a host edge \(e=(i,j)\).

## SRR1d -- one-layer dense-host oracle

### Theorem SRR1d -- PROVED

Let \(\Omega(G)\) be the set of perfect matchings of \(G\), and assume
it is nonempty. For every flawed state \(\pi\in\Omega(G)\) with
\(\pi(i)=j\), define

\[
U_\pi
=
\{u\in X\setminus\{i\}:
  (i,\pi(u))\in E,\ (u,j)\in E\}.
\]

Then

\[
\boxed{|U_\pi|\ge d(i)+d(j)-N-1.}
\]

If this lower bound is at least one, there is a symmetric stochastic
kernel on \(\Omega(G)\) which:

1. sends every flawed state to a nonflawed state with probability one;
2. changes only the alternating four-cycle on rows \(i,u\);
3. is reversible and stationary for the uniform measure on
   \(\Omega(G)\); and
4. from each flawed state chooses every \(u\in U_\pi\) with probability
   \(1/|U_\pi|\).

In particular, minimum degree at least \(\delta N\) gives at least
\((2\delta-1)N-1\) choices whenever that quantity is positive.
The kernel also removes any forbidden partial matching that contains
the distinguished edge \(e\).

### Proof

The set

\[
\pi^{-1}(N_G(i))\cap N_G(j)
\]

has size at least \(d(i)+d(j)-N\). It contains \(i\), because
\(\pi(i)=j\) and \(e\in E\). Deleting \(i\) proves the lower bound.
For \(u\in U_\pi\), swap \(\pi(i)\) and \(\pi(u)\). Both new edges are
in \(G\), so the result is a perfect matching of \(G\); it avoids \(e\)
because \(i\) was the unique preimage of \(j\).

Fix a nonflawed output \(\pi'\). Any reverse switch that introduces
\((i,j)\) must use

\[
u=(\pi')^{-1}(j),
\]

and swapping rows \(i,u\) uniquely reconstructs its predecessor.
Consequently every output has at most one flawed predecessor.

Give a forward edge from \(\pi\) weight \(1/|U_\pi|\), and give its
reverse edge the same weight. Every flawed row has total weight one.
Every nonflawed row has at most one reverse edge, of weight at most one;
place its unused mass on its self-loop. The resulting matrix is
symmetric and stochastic, hence reversible and uniform-stationary.
\(\square\)

## SRR3f -- two-layer dense-host oracle

Let

\[
\Omega_2(G)=
\{(\pi,\rho):
  \pi,\rho\in\Omega(G),\
  \pi(x)\ne\rho(x)\text{ for every }x\}.
\]

### Theorem SRR3f -- PROVED

Assume \(\Omega_2(G)\ne\varnothing\). In a flawed state
\((\pi,\rho)\) with \(\pi(i)=j\), let \(U_{\pi,\rho}\) consist of the
rows \(u\ne i\) for which swapping \(\pi(i)\) and \(\pi(u)\):

- uses two edges of \(G\); and
- remains edge-disjoint from \(\rho\).

Then

\[
\boxed{
|U_{\pi,\rho}|
\ge d(i)+d(j)-N-3.
}
\]

If the displayed lower bound is at least one, choosing each admissible
row with probability \(1/|U_{\pi,\rho}|\), symmetrizing the reverse
edge, and adding nonflawed self-loops gives a reversible
uniform-stationary flaw-removal kernel on \(\Omega_2(G)\). It preserves
the host, both perfect-matching constraints, and cross-layer
edge-disjointness, and its symmetric difference is one four-cycle in
the selected layer. The same statement holds with the layers exchanged.

Minimum degree at least \(\delta N\) supplies
\((2\delta-1)N-3\) choices whenever this is positive.
Again, removing \(e\) removes every labelled partial-matching flaw that
contains it.

### Proof

Before enforcing cross-layer disjointness, the same intersection as in
SRR1d supplies at least \(d(i)+d(j)-N\) candidate rows, including
\(i\). The only new cross-layer collisions after the swap are

\[
\pi(u)=\rho(i)
\quad\text{or}\quad
j=\rho(u).
\]

They occur at the two uniquely determined rows

\[
b_1=\pi^{-1}(\rho(i)),
\qquad
b_2=\rho^{-1}(j).
\]

Deleting \(i,b_1,b_2\), with coincidences counted only once, proves the
lower bound.

For any nonflawed output \((\pi',\rho)\), a reverse switch again must use
the unique row \(u=(\pi')^{-1}(j)\), and it uniquely reconstructs the
predecessor. Thus reverse degree is at most one even though the forward
degrees vary. The state-dependent symmetric weighting from SRR1d
therefore gives the asserted kernel. \(\square\)

## SRR3j -- dense-host uniform cylinder spread from switching

Let \(d_{\min}\) be the minimum degree of \(G\) on both vertex classes
and put

\[
\boxed{
L_2=2d_{\min}-N-3.
}
\]

Assume \(\Omega_2(G)\ne\varnothing\), and let \(\mu_2\) be its uniform
measure.

### Theorem SRR3j -- PROVED

If \(L_2\geq1\), then every host edge \(e\), in either specified layer,
satisfies

\[
\boxed{
\Pr_{\mu_2}(e\text{ occurs in that layer})
\leq\frac1{L_2+1}.
}
\]

More generally, let \(F\) be any globally compatible set of \(s\)
labelled host edges across the two layers.  If \(1\leq s\leq L_2\),
then

\[
\boxed{
\Pr_{\mu_2}(F\subseteq(M_1,M_2))
\leq
\prod_{t=0}^{s-1}\frac1{L_2-t+1}
=
\frac1{(L_2+1)_s}.
}
\]

Here \((x)_s=x(x-1)\cdots(x-s+1)\).  In particular, if
\(d_{\min}\geq\delta N\) for fixed \(\delta>1/2\), the uniform
two-layer host measure is fixed-rank

\[
\left(\frac{1+o(1)}{(2\delta-1)N}\right)\text{-spread}.
\]

### Proof

For one labelled edge, form the bipartite switching graph from states
containing it to states avoiding it.  SRR3f gives every flawed state at
least \(L_2\) outgoing four-cycle switches, while every nonflawed state
has at most one reverse predecessor.  Double-counting switching edges
gives

\[
L_2|\Omega_e|\leq|\Omega_2(G)\setminus\Omega_e|.
\]

Rearranging proves the first box.

Order the \(s\) labelled edges of \(F\) and condition successively.
After \(t\) edges have been fixed, apply the same switching graph to the
next edge inside the conditioned state space.  A switch already counted
by SRR3f preserves the other layer.  To preserve the fixed edges in its
own layer, discard partner rows supporting those edges; there are at
most \(t\) such rows.  Every flawed conditioned state therefore has at
least \(L_2-t\) valid forward switches, and reverse degree is still at
most one.  If the conditioned state space is empty the desired
probability is zero; otherwise the same double count gives conditional
probability at most \(1/(L_2-t+1)\).  Multiplication over
\(t=0,\ldots,s-1\) proves the cylinder bound.  The asymptotic statement
is immediate for fixed \(s\). \(\square\)

SRR3j obtains the natural fixed-rank spread directly for the uniform
two-layer measure on every sufficiently dense host; no external spread
measure is needed.  It still does not prove SRR2: a spread upper bound
does not control the ratio between a remote cylinder conditioned on a
flaw and its marginal.  The remaining theorem is precisely that
lopsided correlation comparison, now separated from both stationarity
and uniform cylinder rarity.

## Deterministic locality retained

Put

\[
D_1=d(i)+d(j)-N-1
\quad\text{or}\quad
D_2=d(i)+d(j)-N-3
\]

in the one- or two-layer setting. From any flawed state, the probability
that the partner row lies in a specified set \(R\subseteq X\setminus
\{i\}\) is at most

\[
\frac{|R|}{D_\ell}.
\]

The same bound holds for a specified set of partner columns because
\(\pi\) is injective. A remote same-layer partial matching whose rows
and columns avoid \(i,j\) cannot be created by the switch, and the other
layer is unchanged pathwise.

These are switching-support bounds. They do **not** compare a remote
cylinder conditioned on the flaw with its uniform marginal in an
arbitrary missing-edge host. That correlation estimate remains the
precise SRR2 bottleneck; density or superregularity must still control
it.

`scripts/verify_dense_host_resampling.py` enumerates perfect matchings
and ordered edge-disjoint pairs in complete and one-edge-deleted hosts.
It checks the degree bounds, unique reverse predecessor, flaw removal,
host preservation, and exact row and column sums of the rational kernel.
It also checks the uniform labelled-cylinder spread bound and each of
its sequential conditional factors on complete small hosts.
