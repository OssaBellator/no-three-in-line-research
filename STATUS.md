# Status and honesty ledger

**Last updated:** 25 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

## What is genuinely proved

### Prime-power algebra, recursive banks, and first separation

- Every odd prime power admits nonlinear completed-reciprocal permutation
  channels, disjoint companion layers, exact displacement/carry identities, and
  recursive fibre banks.
- Balanced completed-reciprocal local laws exist exactly for
  \(p\equiv1\pmod4\). A non-reciprocal seven-map factorization gives a balanced
  recursive bank for every \(7^k\).
- For fixed balanced prime base, first separation gives expected syndrome
  \(O_p(N^2\log N)\). The logarithm is localized to binary same-layer prefix
  stars.

### Prefix, joint-parent, Hall, and line-clean repair

- Every binary star has a unique closest-pair prefix block; complete rematching
  destroys it.
- Rank-one quotient excess decomposes into modular third-point and collision
  carry energies. Normalized higher-rank prefix collateral is quadratic.
- Fine-to-coarse processing preserves unprocessed quotient charges.
- Nonroot layer fibres are disjoint, giving old-cell-clean joint-parent banks
  with total expected collateral \(O_p(N^2\log^2N)\).
- Global-baseline transfer and target-load contraction reduce positive load to
  inherited parent escape. Pure normalized four-point descent is false; exact
  root escapes are known for the prime-five and prime-seven terminal censuses.
- Sharp target-specific Hall blockers are singleton fans or one-slack boundary
  factors. Thin factors reduce to explicit primitive, quotient, and carry
  signatures.
- Universal line-clean paid-pair banks move the old target, avoid every other
  cell on the paid line, and remove rank-two-on-that-line collateral.
- Frozen line-clean banks lead to matching-vertex walls, repeated-cell secant
  stars, executable heavy prefix cells, dispersed full tokens, or repeated
  exact absolute tokens.

### Exact height and harmonic-packet completion

- Candidate-only triples above primitive height \(0.42t\) are exactly cleanable
  for all sufficiently large odd parent blocks, with protected-line reserve.
- For every fixed \(\eta>0\), the duplicated-row model exactly completes every
  height family \(\mathcal K\) satisfying
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
  exact harmonic packets.

### Exact token and selected-state accounting

For a full token \(\tau=(b,a,c,\theta)\),

\[
D_\tau^{(2)}
\le
\frac{t^2}{p^{2b}}+I_\tau^{(2)}.
\]

- One recursive ancestor or one one-layer whole-parent reset returns at most
  \(t/p^b\) token edges; one ordered joint-parent reset returns at most
  \(2t/p^b\).
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
- Distinct feasible perfect matchings differ by at least two entering and two
  leaving edges, so distinct-state expansion pays full-token incidence linearly.

### Packet termination and essential ancestry

- A conflict recreated by a selected transition contains an entering edge; the
  leaving set has equal cardinality.
- Every lossy packet reset in one deletion pass either removes a nonessential
  edge or exposes a fully forced certificate.
- Matchability-preserving deletions occur at most
  \[
  |E(G_0)|-t\le t(t-1)
  \]
  times.
- Essentiality persists under later matchability-preserving deletions. A fully
  forced packet triple is terminal for the current pass.
- The first-dirty packet schedule completes in polynomially many installations
  or reaches one terminal fully forced certificate in polynomially many
  installations.
- Essential edges form one monotone matching core \(E_*\) with \(|E_*|\le t\).
  After edge-set deduplication there are fewer than \(t^3+t\) forced rank-one,
  rank-two, or rank-three certificates and fewer than \(3t^3\) ancestry links.

### Exchange corridors and sparse common-epoch rollback

- Matching contraction turns alternating cycles into directed cycles.
- Every first-essentiality layer is an acyclic directed exchange corridor.
  Reachability chains lie on one batch exchange cycle, and the exact cycle-cover
  number is the reachability-poset width.
- Across one deletion pass, all first-essentiality edges are covered at their
  valid historical times by at most \(t\) batch exchange cycles.
- Every final essential edge has rollback number
  \[
  1\le\kappa(e)\le t.
  \]
  Restoring at most one matching's worth of deleted edges creates a common-epoch
  matching avoiding it.
- A minimum rollback set is forced in the avoiding host and factors the residual
  matching problem to side \(t-\kappa(e)\).
- A restored set \(R\) has exact labelled incidence
  \[
  \mathcal I(R)=(p+1)(h-1)|R|.
  \]
- Every conflict recreated from a host-clean family uses a restored edge. For a
  harmonic packet of weight \(W\), rollback creates at most
  \[
  2(t-1)^2W|R|
  \]
  represented triples.

### Canonical minimum-cost marked faces

Give returned or deleted edges binary cost one and current edges cost zero.

- The rollback number is the minimum assignment cost.
- Relative to one optimum, every alternating cycle has nonnegative cost.
- All other optima are obtained by zero-cost cycle flips.
- Shortest-path potentials produce a tight host whose perfect matchings are
  exactly the minimum-cost states.
- If the optimum cost is \(k\), potentials lie in \([-k,0]\).
- The optimum family factors over strongly connected exchange blocks; rollback
  cost splits additively across them and at most \(k\) blocks are active.
- Every optimum has a balanced cross-level skeleton of at most \(2k\) edges.
  Conditional on that skeleton, the remaining choices factor independently by
  potential level.
- Inside one level, markedness is determined solely by the right endpoint. The
  marked-source split either factors uniquely or changes along a mixed-colour
  zero-cost cycle.

### Mixed-cycle endpoint through CMR491

- Cyclic colour-boundary arcs have canonical simple mixed-cycle witnesses of
  length at most the local side.
- For every concentration threshold, the witnesses either contain a large
  vertex-disjoint family, concentrate through one exchange vertex, or are sparse
  enough that deleting their tails leaves a colour-separated residual host.
- Vertex-disjoint mixed cycles flip simultaneously and independently.
- Exchange-vertex concentration produces one colour-boundary edge with many
  distinct return cycles. Directed edge Menger gives either an edge-disjoint
  theta fan or a small return-path cut; the latter concentrates further on a
  second edge.
- A theta fan has entering sets forming a sunflower with core equal to the common
  boundary edge. Noncore entering edges are private across the fan.
- Dirty theta states either pay distinct private route edges or expose a conflict
  completed by the common boundary edge and base matching.
- For collinearity triples, those rooted conflicts form a repeated-cell secant
  star with pairwise disjoint outside pairs and at most \(\lfloor m/2\rfloor\)
  arms.
- Two fixed contraction edges lying on many mixed cycles form a compatible
  rank-two partial matching; the cycle states give distinct residual perfect
  matchings in one side-\(m-2\) completion cylinder.

## Important corrections

- Naive sequential two-layer rematching does not necessarily destroy every
  selected target: the second layer may reoccupy an old first-layer cell.
- Static token consumption is not monotone; exact token-restoring cycles exist.
- The support edges of recreated selected triples are entering edges, not
  leaving edges. Entering and leaving sets have equal cardinality, so the
  numerical churn bounds remain correct.
- Historical alternating cycles are not automatically executable in the final
  host. Sparse rollback and minimum-cost normalization are the valid
  common-epoch replacements.

## What remains open or conditional

1. **Secant-star splice.** Feed the CMR487 rooted star into the existing
   carry-dispersion, line-energy, wall, heavy-prefix, or full-token alternatives
   with a monotone target-load or reserve payment.
2. **Rank-two cylinder splice.** Integrate the CMR490 fixed pair cylinder with
   line-clean paid-pair completion and rank-zero/rank-one collateral bounds.
3. **Sparse-interface recursion.** Turn deletion of the CMR476 boundary-tail
   interface into a formally decreasing envelope or host-decomposition measure.
4. **Two-edge geometric concentration.** Attach primitive-height, quotient,
   carry, Hall, reserve, or envelope signatures to the CMR480 bottleneck pair.
5. **Low-height carry absorption.** Charge the remaining lower-height lines to
   first-separation, quotient, and primitive carry signatures.
6. **Prime-field transfer.** Rebuild the inherited-envelope and exact-covering
   endpoint for complementary-hyperbola carry cycles.
7. **Square-root divisor boundary.** Remove or absorb the remaining nearly
   singular collision terms.
8. **Further balanced prime families and arbitrary side lengths.** Extend the
   non-reciprocal balanced factorizations, control CRT projections, and cover
   every positive integer \(n\).

## Bottom line

There is no complete proof. On the prime-power route, harmonic-packet
construction, packet termination, polynomial ancestry, sparse common-epoch
rollback, minimum-cost marked-face normalization, sparse level skeletons,
mixed-cycle packing/concentration, theta-fan private-edge payment, rooted
secant-star identification, and fixed rank-two cylinder reduction are closed at
their stated scales.

The principal current theorem is a splice from the final secant-star and
rank-two cylinder branches into the already developed line-clean, carry,
prefix, reserve, target-load, and envelope machinery. Arbitrary side-length
coverage remains necessary afterward.
