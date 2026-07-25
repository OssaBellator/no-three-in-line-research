# Repeated unavailable-token episodes pay finite stock, reintroduction, or one persistent blocker

CMR512--CMR516 convert every heavy unavailable row/column star into a heavy
full-prefix token or a dispersed unavailable-token bank.  The remaining issue is
temporal reuse: the same unavailable cells may appear in several line-clean or
ancestor-return episodes.

This chapter gives an exact multiplicity ledger.  Repeated episodes either use
many distinct labelled token-edge pairs, exceed the finite labelled stock, or
reuse one pair many times.  Reuse of one pair further splits into absent-to-
present reintroduction payment or one long interval on which the edge remains
continuously unavailable.

Fix a parent block of side

\[
t=p^h,
\qquad h\ge2.
\]

For every nonroot full token

\[
\tau=(b,a,c,\theta),
\qquad 1\le b<h,
\]

write `U_\tau^{(2)}` for its edge universe.

## 1. One-token persistence or finite stock

Consider `J` episodes attached to one fixed token `\tau`.  In episode `j`, let

\[
E_j\subseteq U_\tau^{(2)}
\]

be a set of unavailable witness edges with

\[
|E_j|\ge H.
\]

### Theorem CMR517 — PROVED

For every integer `\lambda\ge2`, at least one of the following holds.

1. **Persistent token edge.** Some edge belongs to at least `\lambda` of the
   witness sets `E_j`.
2. **Finite-stock episode bound.**
   \[
   \boxed{
   J
   \le
   \frac{(\lambda-1)|U_\tau^{(2)}|}{H}
   =
   \frac{(\lambda-1)t^2}{Hp^{2b}}.
   }
   \]

### Proof

If the first branch fails, every edge of `U_\tau^{(2)}` belongs to at most
`\lambda-1` witness sets.  Double-count the incidences `(j,e)`:

\[
JH
\le
\sum_j|E_j|
\le
(\lambda-1)|U_\tau^{(2)}|.
\]

Use CMR394 for the exact token stock. ∎

Thus repeated heavy visits to one exact token are finite unless one exact cell
recurs as an unavailable blocker.

## 2. Global labelled token-edge stock

A **labelled token-edge pair** is a pair `(\tau,e)` with
`e\in U_\tau^{(2)}`.  Every parent edge belongs, at every nonroot depth, to one
prefix pair and to all `p+1` direction labels.

### Theorem CMR518 — PROVED

The total number of labelled nonroot token-edge pairs in one parent is exactly

\[
\boxed{
\mathcal N_{
\mathrm{lab}}
=
(p+1)(h-1)t^2.
}
\]

Let a collection of episodes have tokens `\tau_j` and unavailable witness sets

\[
E_j\subseteq U_{\tau_j}^{(2)}.
\]

Put

\[
W=\sum_j|E_j|.
\]

For every integer `\lambda\ge2`, either some labelled pair `(\tau,e)` occurs in
at least `\lambda` episodes, or

\[
\boxed{
W
\le
(\lambda-1)(p+1)(h-1)t^2.
}
\]

### Proof

CMR413 assigns exactly `(p+1)(h-1)` nonroot labels to every edge, giving the
stock identity.  If every labelled pair occurs at most `\lambda-1` times,
double-count all episode-witness incidences. ∎

This simultaneously controls heavy tokens at different depths, prefix cells,
and direction labels.

## 3. Continuous absence runs and reintroduction

Let

\[
A_0,A_1,\ldots,A_m
\]

be the available-edge sets inside one fixed envelope epoch.  Fix an edge `e` and
consider episode times

\[
0\le t_1<t_2<\cdots<t_r\le m
\]

at which `e\notin A_{t_i}`.  Partition these occurrences into maximal blocks
which lie inside one interval of continuous absence of `e`.  Call those blocks
**absence runs**.

Let

\[
I(e)
=
|\{i: e\in A_i\setminus A_{i-1}\}|
\]

be the number of absent-to-present reintroductions of `e`.

### Theorem CMR519 — PROVED

The number `\rho(e)` of absence runs containing the selected episode times
satisfies

\[
\boxed{\rho(e)\le1+I(e).}
\]

Consequently some one continuous-absence run contains at least

\[
\boxed{
\left\lceil\frac r{1+I(e)}\right\rceil
}
\]

of the episode occurrences.

More quantitatively, for every integer `\sigma\ge2`, either one absence run
contains at least `\sigma` occurrences, or

\[
\boxed{
I(e)
\ge
\left\lceil\frac r{\sigma-1}\right\rceil-1.
}
\]

### Proof

Between two distinct absence runs, the edge must become available at least once,
which contributes one absent-to-present transition.  Hence `\rho(e)-1\le I(e)`.
Pigeonhole gives the first bound.  If every run contains at most `\sigma-1`
occurrences, then `r\le\rho(e)(\sigma-1)`; combine this with the run bound. ∎

The reintroduction count is one summand of the full-token return mass
`I_\tau^{(2)}` from CMR395 whenever `e\in U_\tau^{(2)}`.

## 4. Three-way temporal endpoint

### Corollary CMR520 — PROVED

Consider any episode collection as in CMR518 inside one fixed envelope epoch.
Fix integers `\lambda,\sigma\ge2`.  At least one of the following holds.

1. **Finite fresh labelled stock.**
   \[
   \boxed{
   W
   \le
   (\lambda-1)(p+1)(h-1)t^2.
   }
   \]
2. **Reintroduction payment.** Some edge-token pair occurring at least
   `\lambda` times has
   \[
   \boxed{
   I(e)
   \ge
   \left\lceil\frac\lambda{\sigma-1}\right\rceil-1.
   }
   \]
3. **Persistent blocker run.** One labelled pair `(\tau,e)` occurs in at least
   `\sigma` episodes while `e` remains continuously unavailable throughout the
   interval spanning those occurrences.

### Proof

If the first branch fails, CMR518 gives a labelled pair occurring at least
`\lambda` times.  Apply CMR519 to those occurrences. ∎

The only unpriced repetition is therefore a persistent unavailable cell in one
fixed token and one fixed envelope epoch.

## 5. Free-absorption episodes

Suppose episode `j` uses the adaptive forbidden matching of CMR507 and absorbs a
matching

\[
S_j
\]

of unavailable residual edges with

\[
|S_j|\ge s.
\]

### Corollary CMR521 — PROVED

For `J` such episodes and every integer `\lambda\ge2`, either

1. some parent edge belongs to at least `\lambda` absorbed matchings `S_j`; or
2. 
   \[
   \boxed{
   J
   \le
   \frac{(\lambda-1)t^2}{s}.
   }
   \]

For a recurrent absorbed edge, CMR519 gives the same reintroduction-versus-
persistent-absence alternative.

### Proof

The parent has `t^2` physical edges.  If no edge occurs in `\lambda` absorbed
matchings, double-count the at least `Js` absorption incidences.  Apply CMR519 to
a recurrent edge. ∎

Free absorption is therefore not an infinite new resource.  It consumes finite
physical edge stock, pays reintroduction, or repeatedly identifies one
continuously unavailable blocker.

## 6. Revised frontier

The adaptive line-clean endpoint now has temporal accounting on every
nonpersistent branch.

- Heavy-token and dispersed-token episodes consume finite labelled stock unless
  one labelled edge recurs.
- Recurrent labelled edges pay the existing reintroduction ledger unless they
  remain continuously unavailable.
- Large free-absorption matchings obey the same physical-edge ledger.

The immediate remaining theorem is geometric treatment of a **persistent
blocker**: one exact cell remains unavailable through many rooted-arm,
bottleneck, or ancestor-return episodes inside one envelope epoch.  Such a cell
should force protected-reserve depletion, a stable Hall wall, a fixed
prefix/quotient/carry signature, deletion ancestry, or strict envelope
expansion.

No all-`n` theorem is claimed.  Incidence stock, absence-run arithmetic, and the
three-way threshold alternatives are checked in
[`scripts/verify_prime_power_unavailable_temporal_ledger.py`](../scripts/verify_prime_power_unavailable_temporal_ledger.py).
