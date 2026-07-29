# Tensor-product threshold slack for bounded-cycle switchings

**Branch:** `research/superregular-resampling`

SRR2ac--SRR2ag reduce endpoint transportation cost to forward deficit, reverse overload and local conditioning loss relative to one reference degree.  Bounded-cycle switchings are often assembled from a fixed number of local choice layers.  This note gives the exact error composition for a coordinatewise tensor product of those layers.

## Tensor threshold graph

For `1<=i<=t`, let

\[
G_i\subseteq A_i\times B_i
\]

be one low-event threshold graph.  Its left minimum degree and right maximum load are `d_i` and `D_i`.

The tensor graph has left side `A_1 x ... x A_t`, right side `B_1 x ... x B_t`, and

\[
(a_1,...,a_t)\sim(b_1,...,b_t)
\quad\Longleftrightarrow\quad
a_i\sim b_i\text{ in every }G_i.
\]

Fix reference degrees `rho_i>0` and errors `eta_i,zeta_i>=0` satisfying

\[
d_i\ge\rho_i(1-\eta_i),
\qquad
D_i\le\rho_i(1+\zeta_i).
\]

Put

\[
\rho=\prod_i\rho_i,
\qquad
A=\prod_i(1-\eta_i),
\qquad
B=\prod_i(1+\zeta_i).
\]

## SRR2ah -- exact tensor degree factorization -- PROVED

The tensor graph has

\[
\boxed{d=\prod_i d_i,\qquad D=\prod_i D_i.}
\]

### Proof

The degree of a left tuple is the product of its coordinate degrees, so its minimum is the product of the coordinate minima.  The same argument on the right gives the maximum reverse load. QED.

## SRR2ai -- multiplicative near-biregularity -- PROVED

The tensor parameters satisfy

\[
\boxed{d\ge\rho A,\qquad D\le\rho B.}
\]

### Proof

Multiply the coordinate inequalities and apply SRR2ah. QED.

## SRR2aj -- conditioned tensor imbalance -- PROVED

Suppose deterministic remote conditioning deletes at most `beta rho` low-event incidences from the degree of any fixed left tensor state and creates no new incidence.  Then

\[
d'\ge\rho(A-\beta)_+,
\qquad
D'\le\rho B,
\]

and the relative threshold imbalance is at most

\[
\boxed{
\epsilon_{\rm tensor}
\le
\left(1-\frac{(A-\beta)_+}{B}\right)_+.
}
\]

### Proof

Subtract the local loss from the left minimum degree, keep the deletion-monotone right-load bound, and apply SRR2x--SRR2ab. QED.

## SRR2ak -- tensor endpoint-cost criterion -- PROVED

For threshold levels `k`, let the tensor data be `n_k,t_k,eta_{i,k},zeta_{i,k},beta_k`.  Then

\[
\boxed{
\operatorname{OPT}(c\mid\mathcal C)
\le
\sum_k
\left\lfloor
n_k
\left(
1-
\frac{
(\prod_i(1-\eta_{i,k})-\beta_k)_+
}{
\prod_i(1+\zeta_{i,k})
}
\right)_+
\right\rfloor.
}
\]

### Proof

Insert SRR2aj into the exact threshold layer-cake endpoint-cost bound. QED.

## SRR2al -- one bad layer or bank-ready tensor -- PROVED

Fix `0<=tau<1` and at most `t` layers.  If

\[
\eta_i\le\tau,
\qquad
\zeta_i\le\tau,
\qquad
\beta\le\tau
\]

for every layer, then

\[
\boxed{
\epsilon_{\rm tensor}
\le
\Phi_t(\tau):=
1-
\frac{((1-\tau)^t-\tau)_+}{(1+\tau)^t}.
}
\]

Consequently failure of this target returns one exact layer with forward deficit above `tau`, reverse overload above `tau`, or conditioning loss above `tau`.

### Proof

The products obey `A>=(1-tau)^t` and `B<=(1+tau)^t`.  Substitute in SRR2aj.  The contrapositive gives the bad-layer output. QED.

## Updated SRR frontier

For switching graphs that genuinely factor into a bounded number of local threshold layers, the geometric task is now layer-local: bound each forward deficit, reverse overload and conditioned incidence loss.  Nonproduct interactions and the proof that actual geometric switching families admit such a factorization remain open.

## Finite check

`scripts/verify_srr_tensor_product_slack.py` constructs small tensor products, verifies exact degree factorization and audits the multiplicative and conditioned imbalance bounds.