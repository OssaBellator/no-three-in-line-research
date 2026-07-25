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
- Universal line-clean paid-pair banks apply to singleton, width-two,
  width-three, and finite-width Hall families. They move the old target, remove
  every other cell of the paid line, and eliminate rank-two-on-that-line
  collateral.
- A frozen two-slice line-clean bank forces a dyadic band containing
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
- In particular, any two dyadic intermediate-height bands beginning at height
  at least five can be cleaned simultaneously.
- All dyadic bands from \(\max\{5,t^\eta\}\) to \(t\) partition into
  \[
  P_\eta(t)
  \le
  \left\lceil\frac{1+\log_2t}{2}\right\rceil
  \]
  exact harmonic packets. One full packet sweep therefore uses only
  \(O(\log t)\) whole-parent replacements.
- The existence of one clean state for every packet is proved. Sequential
  preservation of earlier packets is not; this is now a recurrence problem,
  not a missing packet construction.

### Heavy, dispersed, and repeated full tokens

- Every heavy carry-cell certificate opens an executable prefix continuation:
  external witnesses return to an earlier block, internal witnesses transfer to
  a deeper closest pair, and equilateral witnesses use their common block.
- Fresh dispersed full tokens have a finite static budget. Static monotonicity
  is false, so the ledger counts exact edge reintroductions.
- For a full token
  \[
  \tau=(b,a,c,\theta),
  \]
  the exact initial edge stock is
  \[
  \frac{t^2}{p^{2b}},
  \]
  and the dynamic inventory is
  \[
  D_\tau^{(2)}
  \le
  \frac{t^2}{p^{2b}}+I_\tau^{(2)}.
  \]
- One recursive ancestor reset returns at most \(t/p^b\) full-token edges. In a
  descending one-pass prefix schedule,
  \[
  I_\tau^{(2),\mathrm{coarse}}
  \le
  \frac{2bt}{p^b}.
  \]
- At the deep threshold \(p^b\ge t^{2/3}\),
  \[
  D_\tau^{(2)}
  \le
  t^{2/3}+2h t^{1/3}.
  \]
- The direction-labelled full-token return mass over all nonroot tokens in one
  prefix pass is \(O_p(t^2\log t)\).
- Arbitrary recursive histories factor through reset multiplicity: excessive
  return forces repeated use of one of at most \(2b\) compatible ancestor
  depth-layer slots.
- A whole-parent one-layer reset, including an exact-packet replacement, returns
  at most \(t/p^b\) full-token edges. One ordered joint-parent reset returns at
  most \(2t/p^b\).
- One complete harmonic packet sweep contributes
  \[
  I_\tau^{(2),\mathrm{packet}}
  \le
  \frac{P_\eta(t)t}{p^b}
  \]
  to one token. At the deep threshold, one prefix pass plus one packet sweep
  gives
  \[
  D_\tau^{(2)}
  \le
  t^{2/3}
  +
  \left(
  2h+
  \left\lceil\frac{1+\log_2t}{2}\right\rceil
  \right)t^{1/3}.
  \]
- The aggregate direction-labelled return mass of one prefix pass plus one
  packet sweep remains \(O_p(t^2\log t)\).
- Every off-token witness certificate already opens an executable prefix
  continuation. The residual repeated-token branch is fully forced exchange
  ancestry together with repeated use of ancestor or packet states.

## Important corrections

- The former CMR138 claim that naive sequential two-layer rematching destroys
  every selected geometric target is **refuted as stated**: the second layer may
  reoccupy an old first-layer cell. Valid replacements are CMR129, CMR155, and
  CMR164.
- Static token consumption is not monotone; CMR350 records exact two-step
  token-restoring cycles. Every current no-return statement includes
  reintroduction, reset multiplicity, or a scheduled-pass hypothesis.

## What remains conditional

1. **Repeated ancestor/packet-state payment.** Charge repeated use of one
   compatible ancestor or harmonic-packet state to destroyed coarse target
   load, envelope expansion, reserve consumption, or new exchange ancestry.
2. **Packet no-return.** One exact state per packet and the complete one-sweep
   return budget are proved. Show that installing later packets does not
   recreate an unbounded number of earlier packet conflicts, or charge every
   recreation to a monotone quantity.
3. **Forced ancestry width.** Bound the width of the fully forced
   certificate-exchange DAG or resample several exchange cycles together.
4. **Low-height carry absorption.** Charge the remaining lower-height lines to
   first-separation, quotient, and primitive carry signatures.
5. **Prime-field terminal conversion.** Transfer the inherited-envelope and
   exact-covering mechanism to prime-field carry cycles.
6. **Square-root divisor boundary.** Remove or absorb the residual nearly
   singular collision terms.
7. **Further balanced prime families.** Extend the non-reciprocal factorization
   beyond prime seven.
8. **CRT and arbitrary side lengths.** Control mixed projections and cover every
   positive integer \(n\).

## Bottom line

There is no complete proof. On the prime-power route, the generic first moment,
prefix and joint-parent collateral, terminal contraction, Hall-blocker repair,
heavy-token continuation, exact harmonic-packet completion, and the complete
one-pass prefix-plus-packet token-return budget are closed. The principal
remaining theorem is dynamic: prevent repeated ancestor and packet states, and
fully forced exchange ancestry, from recycling the same geometric defects.
Arbitrary side-length coverage remains necessary afterward.
