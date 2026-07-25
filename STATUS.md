# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

## What is genuinely proved

### Prime-power algebra and recursive banks

- Every odd prime power admits nonlinear completed-reciprocal permutation
  channels, disjoint companion layers, exact displacement/carry identities, and
  recursive fibre banks.
- Balanced completed-reciprocal local laws exist exactly for
  \(p\equiv1\pmod4\). A non-reciprocal seven-map factorization supplies a
  balanced recursive bank for every \(7^k\).
- For fixed balanced prime base, first separation gives expected syndrome
  \(O_p(N^2\log N)\). The logarithmic term is localized to binary same-layer
  prefix stars.

### Prefix, joint-parent, and alternating repair

- Every binary star has a unique closest-pair prefix block; complete rematching
  destroys it.
- Rank-one quotient excess decomposes into modular third-point and collision
  carry energies. Normalized higher-rank prefix collateral is quadratic.
- Fine-to-coarse processing preserves unprocessed quotient charges.
- Nonroot layer fibres are disjoint, giving old-cell-clean joint-parent banks
  with total expected collateral \(O_p(N^2\log^2N)\).
- Global-baseline transfer and target-load contraction reduce positive load to
  inherited parent escape. Abstract four-point descent alone is false, but exact
  \(N=5\) and prime-seven parent censuses escape their terminal traps.

### Sharp Hall blockers and line-clean banks

- Every target-specific family of at most \(t-2\) nonaxis lines is avoidable
  while one designated old endpoint is moved.
- A sharp \(t-1\)-line blocker is a singleton fan or a one-slack Hall-boundary
  factor.
- Broad factors and widths four through six reduce to low primitive height.
  Width two and width three reduce to explicit primitive/carry signatures.
- Universal line-clean paid-pair banks move the old target, remove every other
  cell of the paid line, and eliminate rank-two-on-that-line collateral.
- A frozen two-slice line-clean bank forces a dyadic band with
  \[
  \Omega\!\left(\frac{H^3}{\log t}\right)
  \]
  distinct replacement-line signatures.
- Those lines convert to a matching-vertex wall, a repeated-cell secant star,
  an executable heavy prefix cell, or dispersed full prefix tokens.

### Exact high-height and harmonic-band cleaning

- Candidate-only triples above primitive height \(0.42t\) are exactly cleanable
  for all sufficiently large odd parent blocks, with a protected-line reserve.
- For every fixed \(\eta>0\), the duplicated-row model gives exact
  target-specific completion for every height family \(\mathcal K\) satisfying
  \[
  \min\mathcal K\ge t^\eta,
  \qquad
  \sum_{K\in\mathcal K}\frac1K<\frac32.
  \]
- Any two dyadic intermediate-height bands beginning at height at least five can
  be cleaned simultaneously.
- All relevant dyadic bands partition into
  \[
  P_\eta(t)
  \le
  \left\lceil\frac{1+\log_2t}{2}\right\rceil
  \]
  exact harmonic packets. One packet sweep uses only \(O(\log t)\)
  whole-parent replacements.
- The existence of one clean state for every packet is proved. The remaining
  question is sequential preservation, not packet construction.

### Full-token return, state expansion, and packet recreation

For a full token

\[
\tau=(b,a,c,\theta),
\]

the exact initial edge stock and dynamic inventory are

\[
|U_\tau^{(2)}|=\frac{t^2}{p^{2b}},
\qquad
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}+I_\tau^{(2)}.
\]

- One recursive ancestor reset returns at most \(t/p^b\) token edges. In one
  descending prefix pass,
  \[
  I_\tau^{(2),\mathrm{coarse}}
  \le
  \frac{2bt}{p^b}.
  \]
- At \(p^b\ge t^{2/3}\),
  \[
  D_\tau^{(2)}
  \le
  t^{2/3}+2h t^{1/3}.
  \]
- A whole-parent one-layer reset returns at most \(t/p^b\) token edges; one
  ordered joint-parent reset returns at most \(2t/p^b\).
- One packet sweep contributes
  \[
  I_\tau^{(2),\mathrm{packet}}
  \le
  \frac{P_\eta(t)t}{p^b}.
  \]
- Exact edge-incidence accounting sharpens the aggregate direction-labelled
  return mass of one two-layer prefix pass to
  \[
  (p+1)t h(h-1),
  \]
  and one prefix pass plus one packet sweep to
  \[
  (p+1)t(h-1)\bigl(h+P_\eta(t)\bigr)
  =O_p(t\log^2t).
  \]
  The earlier \(O_p(t^2\log t)\) tokenwise union bounds remain valid but are not
  sharp.
- Exact selected-state cycles are erasable under a monotone forbidden mask.
- Two distinct feasible selected perfect matchings return at least two old
  edges. Hence a cycle-erased sequence of distinct states pays returned-edge and
  full-token incidence mass linearly; factorial state counts are no longer the
  quantitative endpoint.
- If a later reset recreates a triple from an earlier clean packet, that triple
  contains a newly returned edge. For packet weight \(W\), at most
  \[
  2(t-1)^2W|R|
  \]
  packet triples are recreated by a reset returning \(R\).
- For a first-dirty packet schedule with total packet weight \(W_*\), cumulative
  returned-edge churn \(C\), packet count \(P\), and installation count \(T\),
  \[
  T
  \le
  P+2(t-1)^2W_*C.
  \]
  Thus packet losses and distinct-state expansion are charged to the same churn
  variable.
- Every off-token witness certificate already opens an executable prefix
  continuation. The remaining forced branch is exchange ancestry.

## Important corrections

- The former CMR138 claim that naive sequential two-layer rematching destroys
  every selected geometric target is **refuted as stated**: the second layer may
  reoccupy an old first-layer cell. Valid replacements are CMR129, CMR155, and
  CMR164.
- Static token consumption is not monotone; CMR350 records exact two-step
  token-restoring cycles. Every current no-return statement includes
  reintroduction, reset multiplicity, cycle erasure, or a scheduled-pass
  hypothesis.

## What remains conditional

1. **Global churn payment.** Bound cumulative returned-edge churn by destroyed
   target load, strict envelope expansion, protected-reserve depletion, or a new
   monotone packet potential.
2. **Forced ancestry width.** Convert excess churn into bounded width or
   simultaneously resample several fully forced certificate-exchange cycles.
3. **Low-height carry absorption.** Charge the remaining lower-height lines to
   first-separation, quotient, and primitive carry signatures.
4. **Prime-field terminal conversion.** Transfer the inherited-envelope and
   exact-covering mechanism to prime-field carry cycles.
5. **Square-root divisor boundary.** Remove or absorb the residual nearly
   singular collision terms.
6. **Further balanced prime families.** Extend the non-reciprocal factorization
   beyond prime seven.
7. **CRT and arbitrary side lengths.** Control mixed projections and cover every
   positive integer \(n\).

## Bottom line

There is no complete proof. On the prime-power route, the generic first moment,
prefix and joint-parent collateral, terminal contraction, Hall-blocker repair,
heavy-token continuation, exact harmonic-packet completion, one-sweep return
costs, exact state-cycle erasure, polynomial state-expansion payment, and packet
recreation charging are closed.

The principal remaining prime-power theorem is now a global bound or conversion
for cumulative returned-edge churn and fully forced exchange ancestry. Arbitrary
side-length coverage remains necessary afterward.
