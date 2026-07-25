# Exact stationary resampling on the complete matching space

This note proves all five SRR1 properties for the complete bipartite host.
It is a base case and a semantics check for the desired superregular
oracle; it does not yet handle missing host edges.

Let \(\mu\) be the uniform measure on perfect matchings of \(K_{N,N}\).
Represent a matching by a bijection \(\pi:X\to Y\). For a forbidden partial
matching \(F\), \(1\leq |F|\leq3\), choose one distinguished edge
\(e=(i,j)\in F\).

Define the all-state kernel \(\mathcal R_F\) as follows:

1. choose \(u\) uniformly from \(X\setminus\{i\}\);
2. exchange \(\pi(i)\) and \(\pi(u)\).

## SRR1a -- complete-host oracle

### Theorem SRR1a -- PROVED

The kernel \(\mathcal R_F\) has these properties.

1. If \(F\subseteq\pi\), then \(F\nsubseteq\mathcal R_F(\pi)\).
2. Every output is a perfect matching.
3. The uniform measure \(\mu\) is stationary.
4. The symmetric difference is one alternating four-cycle and has exactly
   four edges.
5. If \(B\) is a canonical partial-matching event of fixed size \(s\),
   vertex-disjoint from \(F\), then for an input drawn from
   \(\mu(\,\cdot\mid F)\),
   \[
   \Pr(B\text{ after }\mathcal R_F)
   =
   \frac{N-1-s}{N-1}\frac1{(N-|F|)_s}.
   \]
   Relative to its unconditioned probability \(1/(N)_s\), this is at most
   \[
   \exp\left(
   \frac{|F|s}{N-|F|-s+1}
   \right)
   =1+O_{|F|,s}(N^{-1}).
   \]

### Proof

If \(F\subseteq\pi\), then \(\pi(i)=j\). Since \(u\ne i\),
\(\pi(u)\ne j\), and after the exchange the distinguished edge is absent.
This proves item 1. Exchanging two images of a bijection leaves a
bijection, proving item 2.

Every transition exchanges the images of one unordered row pair
\(\{i,u\}\), and the same exchange returns to the original matching.
Hence the transition matrix is symmetric. It has \(N-1\) equally weighted
outgoing transitions from every state, so it is doubly stochastic and the
uniform measure is stationary.

The old edges

\[
(i,\pi(i)),\quad(u,\pi(u))
\]

are replaced by

\[
(i,\pi(u)),\quad(u,\pi(i)).
\]

The four distinct edges form one alternating four-cycle, proving item 4.

Put \(k=|F|\). Since \(B\) and \(F\) are vertex-disjoint,

\[
\Pr_\mu(B\mid F)=\frac1{(N-k)_s}.
\]

The exchange cannot create \(B\) if it was absent: it changes only rows
\(i,u\), and if \(u\) is a row of \(B\), that row receives the column
\(j\), which is disjoint from \(B\). If \(B\) was present, it survives
exactly when \(u\) is not one of its \(s\) rows. This has probability
\((N-1-s)/(N-1)\), giving the exact formula.

Finally,

\[
\frac{\Pr(B\text{ after }\mathcal R_F)}{\Pr_\mu(B)}
\leq
\prod_{\ell=0}^{s-1}
\frac{N-\ell}{N-k-\ell}
\leq
\left(1+\frac{k}{N-k-s+1}\right)^s,
\]

and \(1+x\leq e^x\) gives the stated bound. \(\square\)

## Stationarity convention

Item 3 must mean stationarity of the **all-state Markov kernel** above.
If instead it meant that an input sampled from \(\mu(\,\cdot\mid F)\) is
mapped back to \(\mu\), it would contradict item 1: every output would
avoid \(F\), whereas \(\mu(F)>0\). This distinction should be retained in
the general SRR1 statement.

## Four-cycle correlation regression

For \(K_{2,2}\), the events containing the two opposite edges
\((1,1)\) and \((2,2)\) each have probability \(1/2\), while their
intersection also has probability \(1/2>1/4\). Thus even the complete
matching space has positive correlations between compatible disjoint
edges. The oracle works by an explicit stationary switching; it does not
derive a negative-dependency graph from spread.

## Remaining extension

In a superregular subgraph, the cross edges of the four-cycle need not
exist. Extending SRR1a requires a bounded alternating-cycle kernel whose
forward and reverse choices are balanced closely enough to preserve a
stationary measure and the remote-event estimate. Superregularity alone
must be used to prove that balance; it cannot be inferred from SR1 spread.
