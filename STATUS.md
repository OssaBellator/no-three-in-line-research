# Status and honesty ledger

**Last updated:** 26 July 2026

## External status

The classical no-three-in-line conjecture

\[
D(n)=2n
\]

remains open. This repository does **not** contain a complete proof.

## Closed prime-power components

### Algebra, recursive banks, and height cleaning

- Nonlinear completed-reciprocal channels exist at every odd prime power.
- Balanced recursive banks exist for every prime power with
  \(p\equiv1\pmod4\) and for every power of seven.
- First-separation summation gives expected syndrome
  \(O_p(N^2\log N)\).
- Prefix and joint-parent collateral, Hall-wall peeling, line-clean paid-pair
  banks, and exact high-slice cleaning are proved at their stated scales.
- All relevant intermediate-height dyadic bands partition into
  \[
  P_\eta(t)
  \le
  \left\lceil\frac{1+\log_2t}{2}\right\rceil
  \]
  exactly cleanable harmonic packets.

### Token and selected-state accounting

- One recursive ancestor or one one-layer whole-parent reset returns at most
  \(t/p^b\) edges of a full token at depth \(b\); one ordered joint-parent
  reset returns at most \(2t/p^b\).
- One prefix pass plus one packet sweep has labelled incidence
  \[
  (p+1)t(h-1)\bigl(h+P_\eta(t)\bigr)
  =O_p(t\log^2t).
  \]
- Exact selected-state cycles are erasable under a monotone forbidden mask.
- Distinct feasible matchings pay at least two entering and two leaving edges.
- Recreated selected conflicts contain entering edges; entering and leaving
  churn have equal cardinality.

### Packet termination and ancestry

- Every lossy packet reset in one deletion pass pays a permanent nonessential
  deletion or reaches a fully forced certificate.
- Permanent deletion responses occur at most \(t(t-1)\) times.
- Essentiality persists under later matchability-preserving deletions, so a
  fully forced packet triple is terminal for the pass.
- Packet scheduling completes or reaches one terminal certificate in a
  polynomial number of installations.
- All essential edges lie in one final matching core of size at most \(t\).
  Edge-set deduplication gives fewer than \(t^3+t\) forced rank-one, rank-two,
  or rank-three certificates and fewer than \(3t^3\) ancestry links.

### Exchange corridors and rollback

- First-essentiality layers are exact directed exchange corridors.
- Reachability chains batch onto one alternating cycle; the exact cycle-cover
  number is the reachability-poset width.
- All first-essentiality edges in a pass are covered at their valid historical
  times by at most \(t\) batch cycles.
- Every final essential edge has a common-epoch rollback using at most \(t\)
  deleted edges.
- A minimum rollback footprint is a forced matching and factors the avoiding
  host to lower side length.
- Restoring \(R\) edges has exact labelled full-token incidence
  \[
  (p+1)(h-1)|R|.
  \]
- A clean harmonic packet of weight \(W\) gains at most
  \[
  2(t-1)^2W|R|
  \]
  represented triples after restoration.

### Minimum-cost marked faces

Give returned or unavailable edges binary cost one.

- Minimum rollback is a minimum-cost assignment problem.
- Every alternating cycle has nonnegative cost relative to an optimum.
- The tight host contains exactly the minimum-cost states.
- If the optimum cost is \(k\), potentials lie in \([-k,0]\).
- The optimum family factors over strongly connected exchange blocks; at most
  \(k\) blocks are marked-active.
- Every optimum has a balanced cross-level skeleton of at most \(2k\) edges.
- Conditional on that skeleton, the remaining state space factors by potential
  level.
- Inside one level, markedness is right-column polarized. The marked-source
  split either factors or moves along a mixed-colour zero-cost cycle.

### Mixed-cycle endpoint

- Canonical mixed-cycle witnesses either pack vertex-disjointly, concentrate
  through one vertex, or disappear after deleting a sparse boundary interface.
- Vertex-disjoint mixed cycles flip simultaneously.
- Concentration yields one colour-boundary edge with many return cycles.
  Directed edge Menger gives an edge-disjoint theta fan or a small return cut;
  the cut concentrates further on a second edge.
- Theta-fan entering sets form a sunflower with one common boundary edge and
  pairwise disjoint private route edges.
- Dirty theta states either pay private edge incidence or expose a conflict
  rooted on the common boundary edge and the base matching.
- Rooted collinearity conflicts form a repeated-cell secant star with disjoint
  outside pairs.
- A two-edge bottleneck is a compatible rank-two completion cylinder.

### Universal line-clean splice and availability

- Every compatible paid pair has an exact line-clean derangement cylinder of
  size \(D_{m-2}\).
- Every completion contains the pair and no other cell on its joining line, so
  rank-two-on-that-line collateral is absent.
- Every rooted-star arm and every two-edge bottleneck pair has such a cylinder.
- In a restricted current host, define the minimum number
  \(\kappa_L\) of unavailable residual edges used by a line-clean completion.
  Then
  \[
  0\le\kappa_L\le m-2.
  \]
- A minimum restoration footprint is forced and factors the residual host.
- For every threshold, line-clean availability is either cheap restoration or
  strict lower-dimensional factorization.
- Cheap restoration has exact token cost and recreated-conflict support bounds.

### Canonical selector and protected-certificate normal form

- Persistent cross and rooted-trace ancestry have polynomial signature stock or
  reduce to one fixed compatible-pair line-clean selector.
- Every selector has one canonical forbidden matching, one fixed collateral
  profile, and one fixed allowed-edge universe.
- Failed selectors polarize into static collateral or dynamic unavailable-edge
  inventory; all selector, line, token, edge, and protected-state charges are
  owner-labelled.
- Heavy lines and secant stars execute by monotone protected absorption.
- Persistent unavailable contacts amplify to jointly absent cores, batch
  absorption, or simultaneous row/column token walls.
- Threshold-one dynamic selectors have the uniform near-static collateral bound
  \(S\ge77/480\).

### Product potential and essential recursion

- A large protected core leaves a balanced sparse interface of at most twice
  the free side.
- Fixing the interface skeleton gives an exact protected-factor/free-factor
  product.
- Candidate conflicts split exactly into pure protected, pure free, and sparse
  mixed atoms. Each mixed atom is a Cartesian rectangle and has protected rank
  at most two.
- A completely dirty clean-factor product yields a bounded free/interface atom
  or a rank-one/rank-two protected prescription with quantitative support.
- Nonessential prescriptions pay matching-preserving deletion and private
  restoration. Essential prescriptions contract exactly and transfer to the
  other factor.
- Forced product certificates can disappear only through certificate-edge
  deletion, skeleton churn, or an entering-edge alternating cycle.
- Contracting the complete essential core leaves a residual host with no
  essential edges. Core-anchored conflicts are rank at most two and enter a
  finite deletion/contraction recursion.

### Prime-power factor-prefix recursion

- Every reduced factor has one canonical deepest full-prefix envelope.
- At its first nontrivial digit split, every matching has an exact \(p\times p\)
  child transport table.
- Fixing the vertex-routing skeleton factors the matching family exactly across
  strict child prefix cells.
- A side-\(d\) factor has at most \(p^{2d}\) routing skeletons.
- Long factor histories recur in one fixed child product or are finitely
  bounded.
- Child loads give heavy strict blocks or dispersed absolute carry cells.

## Important corrections

- Naive sequential two-layer rematching may reoccupy an old first-layer cell.
- Static token consumption is not monotone; exact token-restoring cycles exist.
- Recreated conflicts are supported by entering edges, not leaving edges.
- Historical alternating cycles are not automatically executable in the final
  host; sparse rollback and minimum-cost normalization are the valid temporal
  replacements.
- Theta-fan cycles sharing a boundary edge are structural alternatives, not a
  simultaneous-flip family.
- The matching relabelling which makes a canonical forbidden matching diagonal
  is combinatorial only; real collinearity is always evaluated in the original
  parent-board coordinates.
- One new edge may unlock several old essential edges when they lie on the same
  alternating cycle. Entering-edge payment is per affected alternating
  component, not per omitted essential edge.

## Current open frontier

1. **Recurrent child-product potential.** Inside one fixed prefix-routing
   skeleton, recurse on the strict child hosts or extract and pay cross-child
   mixed atoms without losing owner labels.
2. **Routing-change payment.** Convert repeated changes of child routing into
   full-token return, deletion ancestry, or strict closure-envelope expansion.
3. **Prime-field and low-height transfer.** Integrate the remaining low-height
   signatures and rebuild the endpoint for prime fields not covered by the
   balanced recursive families.
4. **Arbitrary side lengths.** Extend balanced prime families, control CRT
   projections, and cover every positive integer \(n\).

## Bottom line

There is no complete proof. Through CMR663, line-clean selection, dynamic
availability, protected-certificate execution, sparse-interface product
factorisation, mixed-conflict rectangles, essential-core contraction, forced-
certificate escape payment, and strict prefix-routing recursion are closed at
their stated scales.

The principal remaining prime-power theorem is payment across a recurrent
strict child product. Arbitrary side-length coverage remains necessary
afterward.
