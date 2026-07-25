# Dense-host first-moment conflict endpoint

**Branch:** `research/superregular-resampling`

This note records the strongest immediate endpoint available from the proved dense-host uniform cylinder spread. It does not solve the lopsided-resampling problem, but it cleanly separates conflict families already handled by global mass from those that genuinely need dependency control.

## Setup

Let \(G\) be a bipartite host on two vertex classes of size \(N\), and let \(\Omega_2(G)\) be the ordered pairs of edge-disjoint perfect matchings. Assume \(\Omega_2(G)\neq\varnothing\), let \(\mu_2\) be uniform on it, and put

\[
L_2=2d_{\min}-N-3,
\]

where \(d_{\min}\) is the minimum degree over both vertex classes. Assume \(L_2\ge1\).

A labelled cylinder is a compatible set of prescribed host edges, each assigned to one of the two matching layers. Let \(\mathcal B\) be any finite family of bad labelled cylinders, and write \(r(B)=|B|\).

## SRR4a — dense-host first-moment endpoint — PROVED

If every \(B\in\mathcal B\) has \(1\le r(B)\le L_2\) and

\[
\boxed{
\sum_{B\in\mathcal B}\frac{1}{(L_2+1)_{r(B)}}<1,
}
\]

then some state in \(\Omega_2(G)\) contains none of the bad cylinders.

Here \((x)_s=x(x-1)\cdots(x-s+1)\).

### Proof

By SRR3j, every compatible rank-\(s\) labelled cylinder has \(\mu_2\)-probability at most \(1/(L_2+1)_s\). An incompatible cylinder has probability zero, so the same upper bound is harmless for every member of \(\mathcal B\). Let \(X\) count the bad cylinders contained in a random state. Linearity of expectation gives

\[
\mathbb E X
=\sum_{B\in\mathcal B}\Pr(B\subseteq(M_1,M_2))
\le
\sum_{B\in\mathcal B}\frac{1}{(L_2+1)_{r(B)}}<1.
\]

Since \(X\) is a nonnegative integer, some state has \(X=0\). \(\square\)

## Uniform-rank corollary

If every bad cylinder has rank exactly \(r\le L_2\), it is enough that

\[
|\mathcal B|<(L_2+1)_r.
\]

For \(d_{\min}\ge\delta N\) with fixed \(\delta>1/2\) and fixed \(r\), this permits \(\Theta(N^r)\) bad cylinders with an explicit leading constant.

## Boundary of the result

SRR4a uses no dependency graph and therefore cannot exploit local sparsity when the displayed global sum exceeds one. Those instances remain the proper target of SRR2: compare a remote cylinder under flaw conditioning with its marginal, or build an exact resampling oracle whose witness tree is controlled. The theorem prevents that harder machinery from being invoked on cases already settled by the proved spread estimate.
