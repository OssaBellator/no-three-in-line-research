# Relative threshold slack for endpoint transportation

**Branch:** `research/superregular-resampling`

SRR2s--SRR2w bound every low-cost Hall deficiency by the threshold minimum left degree `d_k`, maximum right load `D_k` and local conditioning loss.  This note converts those parameters to a dimensionless relative slack.  The resulting criterion is the form needed for superregular switching graphs: prove that low-event left degree is close to reverse endpoint load at every threshold.

## Relative imbalance

For a threshold graph with `n` flawed states, define

\[
\varepsilon_k=
\begin{cases}
1,&d_k=0\text{ or }D_k=0,\\
\left(1-\frac{d_k}{D_k}\right)_+,&d_k,D_k>0.
\end{cases}
\]

Under conditioning, let `b_k` be a valid uniform upper bound on the number of low-cost incidences deleted at any one flawed state.  Put

\[
\varepsilon_k^{\rm cond}=
\begin{cases}
1,&d_k\le b_k\text{ or }D_k=0,\\
\left(1-\frac{d_k-b_k}{D_k}\right)_+,&d_k>b_k,\ D_k>0.
\end{cases}
\]

## SRR2x -- relative-slack deficiency bound -- PROVED

For every threshold `k`,

\[
\boxed{
\delta_k\le \lfloor n\varepsilon_k\rfloor.
}
\]

### Proof

If `d_k=0` or `D_k=0`, the right side is `n`, the trivial deficiency bound.  Otherwise SRR2s gives

\[
\delta_k\le n\left(1-\frac{d_k}{D_k}\right)_+.
\]

The deficiency is an integer, so it is at most the floor of the right-hand side. QED.

In particular, exact low-cost Hall saturation follows whenever `d_k>=D_k`.

## SRR2y -- conditioned relative-slack bound -- PROVED

If conditioning deletes at most `b_k` low-cost incidences at each flawed state and creates none, then

\[
\boxed{
\delta_k^{\rm cond}\le
\lfloor n\varepsilon_k^{\rm cond}\rfloor.
}
\]

### Proof

SRR2u gives conditioned minimum degree at least `(d_k-b_k)_+` and right load at most `D_k`.  Apply SRR2x with those parameters. QED.

Thus conditioning enters through the additive relative loss `b_k/D_k`, not through the total number of conditioned host cells.

## SRR2z -- relative-slack endpoint-cost criterion -- PROVED

For an integer endpoint cost with thresholds `1,...,C`,

\[
\boxed{
\operatorname{OPT}(c\mid\mathcal C)
\le
\sum_{k=1}^{C}\lfloor n\varepsilon_k^{\rm cond}\rfloor
\le
n\sum_{k=1}^{C}\varepsilon_k^{\rm cond}.
}
\]

Consequently a declared event budget `T` is bank-ready whenever

\[
n\sum_{k=1}^{C}\varepsilon_k^{\rm cond}<T.
\]

### Proof

The exact endpoint-cost formula is the sum of threshold deficiencies.  Apply SRR2y at every threshold and sum. QED.

## SRR2aa -- multistep relative-slack drift audit -- PROVED UNDER DETERMINISTIC LOCALITY

For a deterministic path of one- or two-layer resampling steps `j`, let `n_j`, `C_j` and `epsilon_{j,k}^{cond}` be valid conditional parameters at step `j`.  The total endpoint event cost along the path is at most

\[
\boxed{
\sum_j\sum_{k=1}^{C_j}
\lfloor n_j\varepsilon_{j,k}^{\rm cond}\rfloor.
}
\]

Hence a current/protected drift budget `T_path` is sufficient whenever this sum is below `T_path`.

### Proof

Condition on the complete preceding history.  Deterministic locality makes the displayed parameters valid at the current step, so SRR2z applies.  Sum the pathwise deterministic bounds. QED.

## SRR2ab -- failed budget exposes relative threshold imbalance -- PROVED

If

\[
\operatorname{OPT}(c\mid\mathcal C)\ge T>0,
\]

then for some threshold `k`,

\[
\boxed{
\varepsilon_k^{\rm cond}\ge\frac{T}{nC}.
}
\]

Equivalently, one low-event threshold has left-degree loss satisfying

\[
D_k-(d_k-b_k)
\ge
\frac{T}{nC}D_k
\]

whenever `d_k>b_k` and `D_k>0`.

### Proof

SRR2z gives `T<=n sum_k epsilon_k^{cond}`.  One of the `C` summands is at least `T/(nC)`.  Rearranging its definition gives the final inequality. QED.

This is a concrete geometric failure output: a high endpoint cost forces one event threshold where reverse endpoint load exceeds conditioned low-event degree by a quantified relative amount.

## Updated SRR frontier

The superregular switching target can now be stated dimensionlessly.  For every actual rank-two/rank-three event threshold, prove small relative imbalance

\[
\varepsilon_k^{\rm cond}
=
\left(1-\frac{d_k-b_k}{D_k}\right)_+.
\]

The remaining work is to derive those ratios from bounded-cycle switching geometry in arbitrary superregular hosts and to feed the resulting pathwise sum into the local conflict endpoint.

## Finite check

`scripts/verify_srr_relative_threshold_slack.py` enumerates small threshold graphs and conditioned edge deletions, computes exact Hall deficiencies and verifies the relative-slack bounds.