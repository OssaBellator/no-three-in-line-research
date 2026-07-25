# Persistent-cross signatures have finite envelope stock and joint-absence recurrence

CMR527--CMR534 reduce one persistent unavailable row-column cross to trace-cell
signatures, compatible paid-pair banks, one-arm line stars, exact pair
recurrence, or weighted line-clean selection.  The remaining temporal question
is how often those signatures can recur while the closure envelope changes.

The closure envelope already supplies the needed coarse clock.  By CMR174--CMR175
a branch has at most `h+1` nested envelope epochs when the root side is
`t=p^h`.  Inside one epoch of side `m`, persistent-cross pair and trace
signatures have exact finite stocks.  Exceeding those stocks forces exact
signature recurrence.

For pair recurrence, the central blocker and both partner edges are unavailable
at every selected occurrence.  A multi-edge version of the absence-run ledger
then gives either explicit reintroduction payment or one interval on which all
three edges remain continuously unavailable.  In the latter interval the fixed
compatible partner pair is governed by the CMR531 weighted line-clean selector
with deterministic paid-edge surcharge two.

## 1. Canonical envelope-epoch assignment

Let a closure branch start in a parent of side

\[
t=p^h.
\]

Assign every persistent-cross episode to the current canonical envelope as in
CMR175.

### Theorem CMR535 — PROVED

The assigned envelopes form a nested chain

\[
E_0\supseteq E_1\supseteq\cdots\supseteq E_g
\]

with

\[
\boxed{g\le h.}
\]

Hence every episode collection is partitioned among at most

\[
\boxed{h+1}
\]

envelope epochs.

If `J` episodes occur in total, one epoch contains at least

\[
\boxed{
\left\lceil\frac{J}{h+1}\right\rceil
}
\]

of them.

### Proof

CMR174 makes envelope depth nonincreasing and strictly decreases it whenever
the envelope expands.  There are `h+1` possible depths from `h` through zero.
CMR175 gives the canonical assignment.  Apply pigeonhole to the episode
counts. ∎

This prevents recurrence from being hidden by indefinite oscillation between
parent scales.

## 2. Exact pair and trace signature stocks

Fix one envelope epoch of side `m` and one matching layer.

A **pair signature** is the ordered data

\[
\Sigma_{\mathrm{pair}}=(e,r_y,c_x),
\]

where

\[
e=(u,v),\qquad
r_y=(u,y),\ y\ne v,\qquad
c_x=(x,v),\ x\ne u.
\]

A **trace signature** is the ordered data

\[
\Sigma_{\mathrm{tr}}=(e,w,\varepsilon),
\]

where `w\ne e` lies in the row or column arm of `e` and
`\varepsilon\in\{\mathrm{row},\mathrm{column}\}` records the arm.

### Theorem CMR536 — PROVED

Inside one epoch of side `m`, the exact numbers of possible signatures are

\[
\boxed{
N_{\mathrm{pair}}(m)
=
m^2(m-1)^2
}
\]

and

\[
\boxed{
N_{\mathrm{tr}}(m)
=
2m^2(m-1).
}
\]

Across a nested envelope chain of sides `m_0,\ldots,m_g`, the total
epoch-labelled stocks are

\[
\boxed{
\mathcal N_{\mathrm{pair}}
=
\sum_{j=0}^{g}m_j^2(m_j-1)^2
\le
(h+1)t^2(t-1)^2
}
\]

and

\[
\boxed{
\mathcal N_{\mathrm{tr}}
=
\sum_{j=0}^{g}2m_j^2(m_j-1)
\le
2(h+1)t^2(t-1).
}
\]

### Proof

Choose the central cell `e` in `m^2` ways.  For a pair signature, choose the
row-arm target `y` in `m-1` ways and the column-arm source `x` in `m-1`
ways.  For a trace signature, choose one of the two arms and then one of its
`m-1` noncentral cells.

Sum over the epoch chain.  CMR535 gives at most `h+1` terms, and every side is
at most `t`. ∎

The epoch label is essential: the same physical-looking local pattern at two
different envelope scales is treated as two different ancestry states.

## 3. Finite signature support or exact recurrence

### Theorem CMR537 — PROVED

Fix an integer `\lambda\ge2`.

For any collection of `J_{\mathrm{pair}}` pair episodes along one closure
branch, at least one of the following holds.

1. Some epoch-labelled pair signature occurs in at least `\lambda` episodes.
2. The total number of pair episodes satisfies
   \[
   \boxed{
   J_{\mathrm{pair}}
   \le
   (\lambda-1)\mathcal N_{\mathrm{pair}}
   \le
   (\lambda-1)(h+1)t^2(t-1)^2.
   }
   \]

Likewise, for `J_{\mathrm{tr}}` trace episodes, either one epoch-labelled trace
signature occurs at least `\lambda` times, or

\[
\boxed{
J_{\mathrm{tr}}
\le
2(\lambda-1)(h+1)t^2(t-1).
}
\]

### Proof

If no signature occurs `\lambda` times, every signature multiplicity is at
most `\lambda-1`.  Multiply that maximum multiplicity by the exact stocks from
CMR536. ∎

Thus all nonrecurrent cross ancestry is already polynomially bounded.

## 4. Multi-edge joint absence runs

Let

\[
A_0,A_1,\ldots,A_N
\]

be the available-edge sets in one fixed envelope epoch.  Fix a finite edge set

\[
F=\{f_1,\ldots,f_d\}
\]

and selected episode times at which every edge of `F` is absent.  Let `I(f)`
count absent-to-present reintroductions of edge `f`.

A **joint absence run** is a maximal interval on which every edge of `F`
remains absent and which contains at least one selected episode time.

### Theorem CMR538 — PROVED

The number `\rho(F)` of joint absence runs satisfies

\[
\boxed{
\rho(F)
\le
1+\sum_{f\in F}I(f).
}
\]

If the selected pattern occurs `r` times, one joint absence run contains at
least

\[
\boxed{
\left\lceil
\frac{r}
{1+\sum_{f\in F}I(f)}
\right\rceil
}
\]

occurrences.

For every integer `\sigma\ge2`, either one joint run contains at least
`\sigma` occurrences, or

\[
\boxed{
\sum_{f\in F}I(f)
\ge
\left\lceil\frac{r}{\sigma-1}\right\rceil-1.
}
\]

### Proof

Between two consecutive joint absence runs, at least one member of `F`
becomes available.  Charge the gap to the first such absent-to-present
transition.  Chronological gaps are disjoint, so one reintroduction event is
not charged twice.  Hence `\rho(F)-1` is at most the total reintroduction
count.

Pigeonhole gives the largest-run bound.  If every run contains at most
`\sigma-1` selected occurrences, then
`r\le\rho(F)(\sigma-1)`; combine with the run bound and rearrange. ∎

CMR519 and CMR533 are the cases `d=1` and `d=2`.

## 5. Recurrent pair signatures

Suppose one epoch-labelled pair signature

\[
\Sigma=(e,r_y,c_x)
\]

occurs in `\lambda` absorption-deficiency episodes.  At every occurrence all
three edges are unavailable: `e` is the persistent blocker, and `r_y,c_x`
are the two unavailable partners supplied by CMR524.

### Corollary CMR539 — PROVED

For every integer `\sigma\ge2`, at least one of the following holds.

1. **Three-edge reintroduction payment.**
   \[
   \boxed{
   I(e)+I(r_y)+I(c_x)
   \ge
   \left\lceil\frac{\lambda}{\sigma-1}\right\rceil-1.
   }
   \]
2. **Jointly persistent cross signature.**  One interval contains at least
   `\sigma` selected episodes while all three edges
   \[
   \boxed{e,\ r_y,\ c_x}
   \]
   remain continuously unavailable.

In the second branch, the pair

\[
Z=\{r_y,c_x\}
\]

is compatible and has fixed paid-edge restoration surcharge `c_Z=2`.
At every epoch inside the joint run, CMR531 supplies either

\[
X_L(\delta)=0,\qquad T_Z(\delta)<q,
\]

or the exact weighted obstruction

\[
\boxed{
A_L+\frac2q+\frac{|B_L|}{q(n-1)}\ge1.
}
\]

### Proof

Apply CMR538 to the three-edge set
`F=\{e,r_y,c_x\}`.  Compatibility of the partner pair is CMR527, and the
weighted selector with surcharge two is CMR531. ∎

Thus exact pair recurrence cannot remain a purely temporal label: it pays
reintroduction or becomes one fixed common-epoch line-clean selection problem.

## 6. Trace-signature recurrence

A repeated trace signature records one fixed central blocker `e`, one fixed
row- or column-arm trace cell `w`, one fixed arm, and one fixed envelope epoch.
The trace cell is not asserted to be unavailable.

### Theorem CMR540 — PROVED

For every threshold `\lambda\ge2`, the complete closure-branch cross history
reaches at least one of the following endpoints.

1. **Finite pair ancestry.**
   \[
   J_{\mathrm{pair}}
   \le
   (\lambda-1)(h+1)t^2(t-1)^2.
   \]
2. **Pair reintroduction or fixed selector.**  One pair signature recurs
   `\lambda` times and reaches CMR539.
3. **Finite trace ancestry.**
   \[
   J_{\mathrm{tr}}
   \le
   2(\lambda-1)(h+1)t^2(t-1).
   \]
4. **Fixed trace-line ancestry.**  One epoch-labelled trace signature recurs
   at least `\lambda` times.

In branch 4, the same central cell and the same arm cell determine the same
grid line whenever the rooted center is fixed.  Even without fixing the rooted
center, the recurrence is confined to one row/column incidence slot inside one
canonical envelope epoch.

### Proof

Apply CMR537 separately to pair and trace episodes.  In the recurrent pair
branch use CMR539.  The geometric statement in the trace branch is uniqueness
of the real line through two fixed cells. ∎

The fourth branch is deliberately not declared paid.  Its trace cell may be
available, so unavailable-edge inventory cannot be invoked without additional
provenance.

## 7. Revised frontier

Cross recurrence across envelope ancestry now has a finite exact ledger.

- There are at most `h+1` envelope epochs.
- Pair ancestry has stock at most
  \[
  (h+1)t^2(t-1)^2.
  \]
- Trace ancestry has stock at most
  \[
  2(h+1)t^2(t-1).
  \]
- Excess pair recurrence pays reintroduction or becomes one jointly persistent
  three-edge signature with a fixed CMR531 selector.
- Excess trace recurrence becomes one fixed envelope, central cell, arm, and
  trace-cell incidence signature.

The immediate prime-power frontier is therefore reduced to two qualitative
payments:

1. convert repeated failure of the fixed CMR531 selector into reserve
   depletion, full-token return, carry/quotient concentration, deletion
   ancestry, or envelope expansion;
2. convert a recurrent fixed trace-line incidence into the same progress
   alternatives without falsely treating the trace cell as unavailable.

No all-`n` theorem is claimed.  Exact signature counts, multiplicity bounds,
multi-edge joint absence runs, and threshold arithmetic are checked in
[`scripts/verify_prime_power_cross_signature_ancestry.py`](../scripts/verify_prime_power_cross_signature_ancestry.py).
