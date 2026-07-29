# Near-biregular criterion for threshold transportation cost

**Branch:** `research/superregular-resampling`

SRR2x--SRR2ab express conditioned endpoint cost through the relative threshold imbalance

\[
 \epsilon_k=\left(1-\frac{d_k-b_k}{D_k}\right)_+.
\]

This note gives a directly checkable sufficient condition for small `epsilon_k`. If a low-event switching graph is near-biregular around one reference degree, then left degree deficit, right load excess and local conditioning loss enter additively.

## Reference-degree parameters

Fix one event-cost threshold `k`. Let `rho_k>0` be a reference switching degree. Assume the unconditioned threshold graph satisfies

\[
 d_k\ge(1-\eta_k)\rho_k,
 \qquad
 D_k\le(1+\zeta_k)\rho_k,
\]

with `eta_k,zeta_k>=0`. Suppose deterministic remote conditioning deletes at most

\[
 b_k\le\beta_k\rho_k
\]

low-cost incidences from any one flawed state.

Write `d_k'` and `D_k'` for the conditioned left minimum degree and right maximum load.

## SRR2ac -- conditioned degree window -- PROVED

The conditioned threshold graph satisfies

\[
 \boxed{
 d_k'\ge(1-\eta_k-\beta_k)\rho_k,
 \qquad
 D_k'\le(1+\zeta_k)\rho_k.
 }
\]

The lower bound is interpreted as zero when its right-hand side is negative.

### Proof

Conditioning deletes at most `b_k` incidences at each left vertex, so `d_k'>=d_k-b_k`. Substitute the two hypotheses. Edge deletion cannot increase a right endpoint load, hence `D_k'<=D_k`. QED.

## SRR2ad -- additive relative-imbalance bound -- PROVED

Define

\[
 \widehat\epsilon_k
 =
 \min\left\{1,
 \frac{\eta_k+\beta_k+\zeta_k}{1+\zeta_k}
 \right\}.
\]

Then

\[
 \boxed{
 \left(1-\frac{d_k'}{D_k'}\right)_+
 \le\widehat\epsilon_k.
 }
\]

### Proof

When `1-eta_k-beta_k<=0`, the right side is capped at one and the claim is immediate. Otherwise SRR2ac gives

\[
 \frac{d_k'}{D_k'}
 \ge
 \frac{1-\eta_k-\beta_k}{1+\zeta_k}.
\]

Subtract from one to obtain the displayed numerator `eta_k+beta_k+zeta_k`. QED.

Thus the three geometric losses have distinct meanings but combine in one dimensionless quantity:

- `eta_k`: deficient forward switching degree;
- `zeta_k`: excessive reverse endpoint load;
- `beta_k`: actual local incidence removed by conditioning.

## SRR2ae -- near-biregular deficiency and cost bound -- PROVED

If the flawed-state side has size `n`, then the conditioned low-cost Hall deficiency obeys

\[
 \boxed{
 \delta_k'\le\lfloor n\widehat\epsilon_k\rfloor.
 }
\]

Consequently, for integer endpoint costs with maximum `C`,

\[
 \boxed{
 \operatorname{OPT}(c\mid\mathcal C)
 \le
 \sum_{k=1}^{C}\lfloor n\widehat\epsilon_k\rfloor.
 }
\]

### Proof

Apply SRR2x to the conditioned degree/load ratio and use SRR2ad. The exact endpoint-cost layer-cake formula then sums the threshold deficiencies. QED.

## SRR2af -- robust budget criterion -- PROVED

Let `T` be the allowed endpoint event budget. If

\[
 \boxed{
 \sum_{k=1}^{C}\lfloor n\widehat\epsilon_k\rfloor<T,
 }
\]

then an integral saturating switching matching exists with endpoint event cost below `T`.

Conversely, if the minimum endpoint cost is at least `T`, then at least one threshold satisfies

\[
 \widehat\epsilon_k\ge\frac{T}{nC}.
\]

Hence one threshold has quantified combined forward-degree deficit, reverse-load excess or conditioning loss.

### Proof

The first claim is SRR2ae plus matching-polytope integrality. For the converse, if every threshold had `widehat epsilon_k<T/(nC)`, then every floor term would be less than `T/C`, and their sum would be less than `T`. QED.

## SRR2ag -- updated SRR2 target -- PROVED AS A REDUCTION

To prove low transportation cost for an actual bounded-cycle switching graph, it is sufficient to exhibit at every event threshold:

1. one reference degree `rho_k`;
2. small forward deficit `eta_k`;
3. small reverse overload `zeta_k`;
4. small local conditioning loss `beta_k`.

No separate global expansion estimate is required once these four quantities are controlled. The remaining geometric work is to derive such near-biregular threshold windows for the actual rank-two/rank-three event inventories in arbitrary superregular hosts and then insert the resulting pathwise cost into the local-conflict endpoint.

## Finite check

`scripts/verify_srr_near_biregular_slack.py` samples small bipartite threshold graphs and conditioned edge deletions, computes exact Hall deficiencies, and verifies the reference-degree imbalance and cost bounds.