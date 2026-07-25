# Owner-labelled canonical certificates have finite line and token-edge stock

CMR552--CMR598 attach every fixed selector obstruction to an envelope-labelled
canonical selector, a protected absorption state, and then to exact lines,
prefix cells, tokens, or physical unavailable edges.  The remaining temporal
question is whether those geometric outputs can be presented repeatedly under
slightly different local descriptions.

The owner labels close that ambiguity.  Along one closure branch there are
polynomially many base selector signatures.  Each selector visits only
linearly many protected states during its absorption chase.  At one protected
state, the numbers of real-line signatures and labelled full-token edge pairs
are finite and explicit.  Consequently repeated wall, prefix, carry, or line
certificates either consume fresh owner-labelled stock, recur as one exact
owned certificate, or pay edge reintroduction.

Let the root parent have side

\[
t=p^h.
\]

Let `\mathfrak S` be the set of canonical selector signatures arising from
persistent pair and refined rooted-trace ancestry on one closure branch.  By
CMR556,

\[
|\mathfrak S|
\le
N_\Sigma,
\]

where

\[
N_\Sigma
=
(h+1)t^2(t-1)^2
+
2(h+1)t^4(t-1)^2.
\]

For `\Sigma\in\mathfrak S`, let its residual side be `n_\Sigma`, its paid-line
trace size be `\ell_\Sigma`, and let

\[
P_{\Sigma,0},P_{\Sigma,1},\ldots
\]

be the protected states actually visited by the CMR575 absorption chase.

## 1. Finite protected-state owner stock

### Theorem CMR599 — PROVED

For every selector `\Sigma`, the number of protected states visited by its
absorption chase is at most

\[
\boxed{
n_\Sigma-\ell_\Sigma+1
\le
t+1.
}
\]

Hence the total number `N_P` of owner-labelled protected states along the
closure branch satisfies

\[
\boxed{
N_P
\le
\sum_{\Sigma\in\mathfrak S}
(n_\Sigma-\ell_\Sigma+1)
\le
(t+1)N_\Sigma.
}
\]

### Proof

CMR575 permits at most `n_\Sigma-\ell_\Sigma` successful absorption steps and
counts the initial state.  Sum over the selector signatures and use
`n_\Sigma<=t`. ∎

The same physical partial matching under two different selector labels remains
two different ancestry owners, which is necessary because their paid lines and
collateral profiles may differ.

## 2. Finite owned real-line stock

At a protected state `P` whose inherited envelope has side `m<=t`, call

\[
(P,\Lambda)
\]

an **owned line signature** when `\Lambda` is a nonaxis real line containing at
least two parent-board cells.

### Theorem CMR600 — PROVED

One protected state has at most

\[
\boxed{
N_{\mathrm{line}}(P)
\le
\binom{m^2}{2}
\le
\binom{t^2}{2}
}
\]

owned line signatures.  Across the closure branch,

\[
\boxed{
\mathcal N_{\mathrm{line}}
\le
N_P\binom{t^2}{2}.
}
\]

### Proof

A real line containing at least two grid cells is determined by any two of its
cells.  Counting unordered cell pairs overcounts lines with more than two
cells and includes axis lines, so it is a valid upper bound.  Sum over the
owner-labelled protected states from CMR599. ∎

Thus repeated presentation of a low-height line, secant-star line, or
rank-zero collision line cannot be charged as fresh line stock indefinitely.

## 3. Exact owned token-edge stock

Fix one protected state `P` in an envelope of side

\[
m=p^g
\]

and residual side `n`.  Its canonical allowed residual universe has exact size

\[
|U_P|=n(n-1).
\]

An **owned labelled token-edge pair** is

\[
(P,\tau,e),
\qquad
e\in U_P\cap U_\tau^{(2)},
\]

where `\tau` includes nonroot depth, absolute prefix coordinates, layer, and
projective direction.

### Theorem CMR601 — PROVED

The exact number of owned labelled token-edge pairs at `P` is

\[
\boxed{
\mathcal N_{\mathrm{tok}}(P)
=
(p+1)(g-1)n(n-1).
}
\]

Across the complete closure branch,

\[
\boxed{
\mathcal N_{\mathrm{tok}}
\le
(p+1)(h-1)t(t-1)N_P.
}
\]

### Proof

CMR413 assigns exactly `(p+1)(g-1)` labelled nonroot full-token incidences to
every physical envelope edge.  The canonical allowed universe contains exactly
`n(n-1)` edges.  This gives the first identity.  Sum over protected states and
use `g<=h` and `n(n-1)<=t(t-1)`. ∎

The owner `P` is part of the label.  The same physical edge under a later
protected matching therefore cannot consume the earlier state's stock.

## 4. Owned token-episode recurrence

Consider any family of token or wall episodes along the branch.  Episode `j`
has one owner `P_j`, one full token `\tau_j`, and a witness set

\[
E_j
\subseteq
U_{P_j}\cap U_{\tau_j}^{(2)}.
\]

Put

\[
W=\sum_j|E_j|.
\]

### Theorem CMR602 — PROVED

For every integer `\lambda>=2`, at least one of the following holds.

1. **Exact owned token-edge recurrence.**  Some tuple
   \[
   \boxed{(P,\tau,e)}
   \]
   occurs in at least `\lambda` episode witness sets.
2. **Finite owned token incidence.**
   \[
   \boxed{
   W
   \le
   (\lambda-1)\mathcal N_{\mathrm{tok}}.
   }
   \]

If every episode has `|E_j|>=H`, then in the second branch

\[
\boxed{
J
\le
\frac{(\lambda-1)\mathcal N_{\mathrm{tok}}}{H}.
}
\]

### Proof

Double-count incidences between episodes and owned labelled token-edge pairs.
If no tuple occurs `\lambda` times, every tuple contributes at most
`\lambda-1`.  Apply CMR601. ∎

This applies simultaneously to heavy protected-contact tokens, persistent
walls, and dispersed carry-cell witnesses.

## 5. Owned line-episode recurrence

Suppose episode `j` produces a set `\mathcal L_j` of owned line signatures,
with

\[
|\mathcal L_j|\ge R.
\]

### Theorem CMR603 — PROVED

For every integer `\lambda>=2`, at least one of the following holds.

1. **Exact owned line recurrence.**  One fixed owned line `(P,\Lambda)` occurs
   in at least `\lambda` episode outputs.
2. **Finite owned line history.**
   \[
   \boxed{
   J
   \le
   \frac{(\lambda-1)\mathcal N_{\mathrm{line}}}{R}.
   }
   \]

In the recurrent branch, the paid pair, canonical collateral profile,
primitive height, support cells, and selector owner of the line are fixed.  It
is one static certificate, not `\lambda` fresh geometric charges.

### Proof

Double-count episode-line incidences among the finite stock from CMR600.  If no
owned line occurs `\lambda` times, total incidence is at most
`(\lambda-1)\mathcal N_{\mathrm{line}}`. ∎

The theorem applies to the rank-zero height bands of CMR565--CMR568 and the
paid-endpoint secant bands of CMR569.

## 6. Unified owner-labelled certificate endpoint

### Corollary CMR604 — PROVED

Across one closure branch, reuse of canonical wall, prefix, carry, secant, and
low-height-line certificates reaches at least one of the following endpoints.

1. **Finite owner-state stock.**  At most `(t+1)N_\Sigma` protected states are
   visited.
2. **Finite owned line stock.**  Nonrecurrent line episodes obey CMR603.
3. **Finite owned token-edge stock.**  Nonrecurrent token episodes obey CMR602.
4. **Fixed owned line certificate.**  One exact `(P,\Lambda)` recurs and is
   charged once to its static profile.
5. **Owned edge reintroduction.**  One exact `(P,\tau,e)` recurs across distinct
   absence runs and pays CMR519.
6. **Persistent owned token edge.**  One exact `(P,\tau,e)` remains unavailable
   on a long interval and enters CMR586--CMR598 with its complete owner fixed.

### Proof

Use CMR599 to enumerate owners, CMR600--CMR603 for line and token incidence,
and CMR519 in the recurrent edge branch.  Apply CMR598 to a long persistent
owned-edge interval. ∎

## 7. Revised frontier

Certificate reuse is no longer an anonymous temporal resource.

- Selector and protected-state ownership has polynomial stock.
- Real lines and labelled token-edge pairs have explicit finite owner-labelled
  universes.
- Repeated owned lines are one fixed static certificate.
- Repeated owned edges pay reintroduction or become a persistent unavailable
  core governed by the selector-slack and batching theorems.

The remaining prime-power frontier is therefore **execution of one fixed owned
certificate**, not its temporal accounting: show that a fixed low-height line,
secant star, matching wall, heavy prefix cell, dispersed carry family, or
persistent core forces strict potential decrease, protected-reserve depletion,
deletion ancestry, full-token return, or envelope expansion.

No all-`n` theorem is claimed.  Owner-state counts, line stock, exact token-edge
incidence, and recurrence inequalities are checked in
[`scripts/verify_prime_power_owned_certificate_stock.py`](../scripts/verify_prime_power_owned_certificate_stock.py).
