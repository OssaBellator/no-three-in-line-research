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

### Essential core and exchange corridors

- Essential edges in any matchable balanced bipartite host form a matching.
- Across one nested deletion pass, all first-essentiality layers partition one
  final essential core `E_*` with
  \[
  |E_*|\le t.
  \]
- After identifying certificates with the same prescribed edge set, there are
  fewer than \(t^3+t\) fully forced rank-`1/2/3` certificates and fewer than
  \(3t^3\) distinct CMR217 ancestry links.
- Matching contraction turns alternating exchange cycles into directed cycles.
  Newly essential matching edges lie in an acyclic directed exchange corridor.
- Reachability on one first-essentiality layer is a partial order. Every chain
  lies on one alternating cycle through the deleted edge and can be exchanged
  in one batch.
- The exact exchange-cycle cover number of the layer is its reachability-poset
  width.
- A layer of size `n` has either a batch cycle containing at least
  \(\lceil\sqrt n\rceil\) newly essential edges or an antichain of that size.
- Across the full deletion pass, all first-essentiality edges are covered at
  their valid historical times by at most
  \[
  \sum_iw_i\le |E_*|\le t
  \]
  batch exchange cycles.

### Sparse rollback and exact payment

Let `G` be the final host of a deletion pass, let

\[
\Delta=E(G_0)\setminus E(G),
\]

and for `e\in\operatorname{Ess}(G)` define

\[
\kappa(e)
=
\min\{|R|:R\subseteq\Delta,\ \operatorname{PM}(G+R-e)\ne\varnothing\}.
\]

- Every final essential edge has
  \[
  1\le\kappa(e)\le t.
  \]
- If `R` is a minimum rollback set for `e`, every edge of `R` is essential in
  `G+R-e`. Hence `R` is a forced matching and
  \[
  \operatorname{PM}(G+R-e)
  \cong
  \{R\}\times
  \operatorname{PM}\bigl((G+R-e)-V(R)\bigr).
  \]
- For every threshold `q`, either `\kappa(e)<q`, or the avoiding matching problem
  factors to side at most `t-q`.
- Every fully forced rank-`1/2/3` terminal certificate can be destroyed by such
  a rollback for any one prescribed edge.
- Choosing one minimum rollback footprint for every edge of `E_*` gives
  \[
  \sum_{e\in E_*}|R_e|\le t^2.
  \]
  These footprints admit a disjoint-packing versus common-deleted-edge
  concentration dichotomy.
- A restored set `R` has exact direction-labelled full-token incidence
  \[
  \mathcal I(R)=(p+1)(h-1)|R|.
  \]
  All chosen minimum rollback footprints for `E_*` have total labelled incidence
  at most
  \[
  (p+1)(h-1)t^2.
  \]
- If a packet family was clean before rollback, every recreated conflict uses a
  restored edge. A clean packet of harmonic weight `W` gains at most
  \[
  2(t-1)^2W|R|
  \]
  represented triples.

### Canonical optimal rollback face

Give every deleted edge unit cost and every final-host edge zero cost in
`G_0-e`.

- The rollback number is exactly the minimum assignment cost:
  \[
  \kappa(e)
  =
  \min\{|M\cap\Delta|:M\in\operatorname{PM}(G_0-e)\}.
  \]
- Relative to one minimum-cost matching, give a contraction arc `j -> k` weight
  \[
  c(\ell_jr_k)-c(m_k)\in\{-1,0,1\}.
  \]
  Every directed alternating cycle has nonnegative total weight.
- Any two minimum rollback matchings differ only by zero-weight alternating
  cycles. Positive-cost excursions are unnecessary.
- Shortest-path potentials produce nonnegative reduced arc costs. The subgraph
  consisting of the base matching and all zero-reduced-cost edges has perfect
  matchings **exactly** equal to the minimum rollback states.
- The potentials are integral and may be chosen in
  \[
  -(t-1)\le\phi(j)\le0.
  \]
  Every tight exchange arc satisfies
  \[
  \phi(k)-\phi(j)
  =c(\ell_jr_k)-c(m_k)
  \in\{-1,0,1\}.
  \]

Thus the cheap rollback branch is a canonical layered tight matching host, not
an arbitrary family of expanded states. The remaining task is geometric
analysis of its potential levels and zero-cost components.

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

1. **Tight rollback-host geometry.** Convert a large potential level, a dense
   zero-cost component, or many unit level changes into target-load destruction,
   reserve depletion, prefix/line-clean continuation, Hall decomposition, or
   envelope expansion.
2. **Rollback concentration conversion.** If many minimum rollback footprints
   use one deleted edge, exploit its earlier certificate and p-adic/carry
   signature.
3. **Exchange-antichain geometry.** Convert a large CMR437 reachability antichain
   into a Hall separator, p-adic/carry concentration, or executable inherited
   repair.
4. **Repeated local ancestor resets.** Attach the same minimum-cost/tight-face
   normalization to repeated compatible prefix-ancestor slots.
5. **Low-height carry absorption.** Charge the remaining lower-height lines to
   first-separation, quotient, and primitive carry signatures.
6. **Prime-field terminal conversion.** Transfer the inherited-envelope and
   exact-covering mechanism to prime-field carry cycles.
7. **Square-root divisor boundary.** Remove or absorb the residual nearly
   singular collision terms.
8. **Further balanced prime families.** Extend the non-reciprocal factorization
   beyond prime seven.
9. **CRT and arbitrary side lengths.** Control mixed projections and cover every
   positive integer \(n\).

## Bottom line

There is no complete proof. On the prime-power route, packet construction,
packet recurrence, state-cycle erasure, polynomial packet termination, exact
exchange corridors, linear temporal cycle compression, common-epoch sparse
rollback, rollback host factorization, rollback token/packet accounting, and the
canonical layered optimal rollback face are closed at their stated scales.

The principal remaining prime-power theorem is a geometric progress certificate
for the tight rollback host, together with a corresponding minimum-cost
normalization for repeated local ancestor resets. Arbitrary side-length coverage
remains necessary afterward.
