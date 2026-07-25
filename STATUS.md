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
  exact harmonic packets. Packet construction is no longer open.

### Full-token return and selected-state expansion

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
- Exact edge-incidence accounting gives
  \[
  \text{one prefix pass}
  \le
  (p+1)t h(h-1)
  \]
  and
  \[
  \text{prefix pass + packet sweep}
  \le
  (p+1)t(h-1)\bigl(h+P_\eta(t)\bigr)
  =O_p(t\log^2t).
  \]
- Exact selected-state cycles are erasable under a monotone forbidden mask.
- Two distinct feasible selected perfect matchings differ by at least two
  entering and two leaving edges, so distinct-state expansion pays full-token
  incidence mass linearly.

### Packet recreation and local termination

- A selected conflict recreated by a reset `M -> M'` contains an **entering**
  edge of `M'\setminus M`. The leaving set `M\setminus M'`, returned to the
  complementary available host, has exactly the same cardinality.
- Inside one certificate-directed deletion pass, every lossy packet reset either
  deletes a nonessential edge while preserving a perfect matching or exposes a
  fully forced rank-three CMR217 certificate.
- Permanent deletion responses occur at most
  \[
  |E(G_0)|-t\le t(t-1)
  \]
  times.
- Essentiality is monotone under later matchability-preserving deletions. A
  fully forced packet triple is therefore terminal for the current pass.
- The first-dirty packet schedule either cleans every packet within
  \[
  P\bigl(1+t(t-1)\bigr)
  \]
  installations or reaches one terminal forced certificate within
  \[
  P\bigl(2+t(t-1)\bigr)
  \]
  installations.

### Polynomial essential-core ancestry ledger

- Essential edges in any matchable balanced bipartite host form a matching.
- Across one nested deletion pass, essential sets grow monotonically and all
  first-essentiality layers partition one final essential core `E_*` with
  \[
  |E_*|\le t.
  \]
- After identifying certificates with the same prescribed edge set, the number
  of fully forced rank-`1/2/3` certificates is at most
  \[
  \binom t1+\binom t2+\binom t3<t^3+t.
  \]
- Their total distinct CMR217 ancestry links, counted once per prescribed edge,
  are at most
  \[
  \binom t1+2\binom t2+3\binom t3<3t^3.
  \]
- Thus raw edge-set ancestry width is polynomial. The remaining challenge is to
  exploit these links geometrically or algorithmically through simultaneous
  low-overlap exchange flips, p-adic/carry concentration, host decomposition, or
  envelope expansion.

## Important corrections

- The former CMR138 claim that naive sequential two-layer rematching destroys
  every selected geometric target is **refuted as stated**: the second layer may
  reoccupy an old first-layer cell. Valid replacements are CMR129, CMR155, and
  CMR164.
- Static token consumption is not monotone; CMR350 records exact two-step
  token-restoring cycles.
- CMR418--CMR421 originally called the support edges of recreated selected
  triples “returned” edges. The support edges are entering edges
  `M'\setminus M`; the returned leaving set `M\setminus M'` has equal size, so
  all numerical bounds remain correct.

## What remains conditional

1. **Geometric exchange-ancestry resolution.** From the fewer than `3t^3`
   distinct exchange links, extract a large low-overlap family for simultaneous
   flipping, or force p-adic/carry concentration, strict host decomposition, or
   envelope expansion.
2. **Repeated local ancestor resets.** Extend the deletion/ancestry payment to
   repeated compatible prefix-ancestor slots not arising from packet loss.
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

There is no complete proof. On the prime-power route, packet construction,
packet recurrence, state-cycle erasure, polynomial packet termination, and raw
edge-set ancestry width are now closed at their stated scales.

The principal remaining prime-power theorem is geometric use of the polynomial
exchange-ancestry ledger, together with a corresponding payment for repeated
local ancestor resets. Arbitrary side-length coverage remains necessary
afterward.
