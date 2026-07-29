# Near-product perturbation stability for switching thresholds

**Branch:** `research/superregular-resampling`

SRR2ah--SRR2al give exact threshold slack when the switching graph factors as a bounded tensor product. Actual geometric switching graphs may contain a bounded nonproduct interaction layer. This note shows that such perturbations enter only through local incidence losses and reverse-load additions.

## Reference product graph

At one endpoint-cost threshold, let `G_0=(A,B;E_0)` be a reference tensor graph with

\[
d_0=\min_{a\in A}\deg_{G_0}(a),\qquad
D_0=\max_{b\in B}\deg_{G_0}(b).
\]

Let `G` be obtained by:

- deleting at most `lambda_L` incidences at each left vertex;
- adding at most `lambda_R` incidences at each right endpoint.

A remote condition may additionally delete at most `b` incidences at each left vertex.

## SRR2am -- perturbation degree bounds -- PROVED

The perturbed threshold graph satisfies

\[
\boxed{d\ge(d_0-\lambda_L)_+,\qquad D\le D_0+\lambda_R.}
\]

### Proof

No left vertex loses more than `lambda_L` reference incidences. No right endpoint receives more than `lambda_R` new incidences. QED.

## SRR2an -- conditioned near-product imbalance -- PROVED

After remote conditioning,

\[
\boxed{
\epsilon
\le
\left(
1-
\frac{(d_0-\lambda_L-b)_+}{D_0+\lambda_R}
\right)_+.
}
\]

The exact Hall deficiency is at most `floor(|A| epsilon)`.

### Proof

Conditioning lowers the left minimum degree by at most `b` and cannot invalidate the reverse-load upper bound. Apply SRR2x--SRR2ab. QED.

## SRR2ao -- endpoint-cost perturbation bound -- PROVED

For threshold-indexed data,

\[
\operatorname{OPT}(c\mid\mathcal C)
\le
\sum_k
\left\lfloor
n_k
\left(
1-
\frac{(d_{0,k}-\lambda_{L,k}-b_k)_+}
{D_{0,k}+\lambda_{R,k}}
\right)_+
\right\rfloor.
\]

Thus nonproduct interactions are harmless whenever their local left loss and right overload are small compared with the tensor reference degree.

## SRR2ap -- failed budget localizes a perturbation threshold -- PROVED

If the displayed sum exceeds a target budget `T`, then some threshold `k` has

\[
1-
\frac{(d_{0,k}-\lambda_{L,k}-b_k)_+}
{D_{0,k}+\lambda_{R,k}}
\ge
\frac{T}{\sum_j n_j}
\]

up to the harmless floor allocation. Hence failure returns one exact threshold with excessive product deficit, nonproduct deletion, reverse overload or conditioning loss.

## SRR2aq -- SRR interface -- PROVED UNDER LOCAL PERTURBATION ACCOUNTING

The geometric switching task now has a robust decomposition:

1. identify a bounded tensor reference graph;
2. prove its layer errors;
3. charge every nonproduct interaction by `lambda_L,lambda_R`;
4. charge remote conditions by `b`;
5. insert the resulting threshold imbalance into the exact min-cost objective.

Interactions not admitting bounded local incidence accounting are returned as the remaining obstruction.

## Finite check

`scripts/verify_srr_near_product_perturbation.py` constructs random tensor graphs, applies bounded left deletions and bounded right additions, and checks the degree, load and relative-imbalance inequalities.