# Boundary-rooted conflicts are secant stars and two-edge bottlenecks are rank-two cylinders

CMR482--CMR486 pay a boundary theta fan unless one conflict is completed by the
common source-switch edge `a` together with base-matching cells. CMR480--CMR481
also leave a possible two-edge cycle bottleneck. This chapter identifies both
exceptions with structures already present in the repair programme.

A boundary-rooted collinearity conflict is exactly one arm of a repeated-cell
secant star centered at the grid cell corresponding to `a`. A fixed pair of
contraction edges lying on many mixed cycles is a compatible rank-two partial
matching; all associated cycle-flip states lie in one exact rank-two completion
cylinder.

Let `P` be a collinearity-clean perfect matching of side `m`, and let `a` be a
nonmatching candidate cell. Define

\[
\mathcal R_a
=
\{C:C\text{ is a candidate-only collinear triple},\ a\in C\subseteq P\cup\{a\}\}.
\]

Every member has the form

\[
C=\{a,p_x,p_y\},
\qquad
p_x,p_y\in P.
\]

## 1. Rooted triples form a secant star

### Theorem CMR487 — PROVED

Distinct members of `\mathcal R_a` have pairwise disjoint outside pairs:

\[
\boxed{
C\ne C'
\quad\Longrightarrow\quad
(C\setminus\{a\})\cap(C'\setminus\{a\})=\varnothing.
}
\]

Consequently, the lines supporting the rooted triples are distinct lines
through the fixed cell `a`, and

\[
\boxed{|\mathcal R_a|\le\left\lfloor\frac m2\right\rfloor.}
\]

Thus `\mathcal R_a` is exactly a repeated-cell secant star with cell-disjoint
outside pairs in the sense used by CMR390.

### Proof

Suppose two distinct rooted triples shared one outside matching cell `p_x`.
Their supporting real lines both contain `a` and `p_x`, so they are the same
line. Their two other outside cells are distinct, since the triples are
distinct. The base matching `P` would then contain three collinear cells,
contradicting its cleanliness.

Therefore the outside pairs are disjoint. Each consumes two different matching
cells, giving the cardinality bound. The supporting lines are distinct by the
same uniqueness-of-a-line argument. ∎

The rooted exception of CMR484 is therefore an already recognized geometric
endpoint, not an arbitrary common-edge conflict.

## 2. Exact presence under a cycle flip

Let `\Gamma` be a mixed contraction cycle containing the boundary arc `a`, and
let `P_\Gamma` be the matching obtained by flipping its alternating cycle. Write
`V(\Gamma)` for its contraction vertices.

### Theorem CMR488 — PROVED

For a rooted triple

\[
C=\{a,p_x,p_y\}\in\mathcal R_a,
\]

one has

\[
\boxed{
C\subseteq P_\Gamma
\iff
x,y\notin V(\Gamma).
}
\]

In particular, a cycle flip destroys a rooted arm exactly when its route visits
at least one endpoint index of that arm. Any rooted arm using a boundary-cycle
endpoint is absent from every theta state through `a`.

### Proof

The cycle flip inserts `a` and removes precisely the base matching edges whose
indices lie in `V(\Gamma)`. Every base matching edge outside that vertex set is
unchanged. The displayed equivalence follows. ∎

Thus cleaning the rooted star inside a theta family is an exact route-
transversal problem for a matching of outside vertex pairs.

## 3. Rooted theta endpoint

### Corollary CMR489 — PROVED

Let `P_1,\ldots,P_q` be the boundary-theta states of CMR482, and let
`\mathcal C` be a collinearity-triple family clean in `P`. If all theta states
are dirty, then at least one of the following holds.

1. **Private route payment.** There are `q` pairwise distinct private entering
   edges supporting recreated conflicts.
2. **Secant-star endpoint.** The rooted subfamily `\mathcal R_a` is nonempty and
   consists of at most `\lfloor m/2\rfloor` cell-disjoint arms through the fixed
   center `a`.

For every theta route, the rooted conflicts surviving in that state are exactly
the arms whose two outside indices the route avoids.

### Proof

CMR484 gives private payment unless an `a`-rooted conflict exists. Apply CMR487
to the complete rooted subfamily and CMR488 to each theta route. ∎

This feeds the rooted branch directly into the existing secant-star carry and
line-energy machinery.

## 4. Two contraction edges form a compatible paid pair

Let `b_1=i_1\to j_1` and `b_2=i_2\to j_2` be distinct contraction arcs lying on
one simple directed cycle.

### Theorem CMR490 — PROVED

The corresponding bipartite host edges

\[
\ell_{i_1}r_{j_1},
\qquad
\ell_{i_2}r_{j_2}
\]

form a compatible partial matching:

\[
\boxed{i_1\ne i_2,\qquad j_1\ne j_2.}
\]

If `L` distinct directed cycles contain both arcs and `P_1,\ldots,P_L` are the
corresponding single-cycle flip states, then every `P_s` contains the same fixed
paid pair. Deleting the two used source vertices and two used target vertices
gives `L` distinct residual perfect matchings of side `m-2`.

### Proof

A simple directed cycle uses each vertex once as an arc source and once as an
arc target. Distinct arcs on it therefore have distinct sources and distinct
targets, which is exactly bipartite compatibility.

Every cycle-flip state contains every nonmatching edge of its cycle, hence the
fixed pair. After deleting the pair and its endpoints, the remaining edges form
a perfect matching on the residual balanced host. Distinct full matchings
containing the same fixed pair remain distinct after restriction: any difference
must occur away from endpoints already occupied by the pair. ∎

Thus the two-edge bottleneck of CMR480 is an exact rank-two completion cylinder,
not an unstructured overlap event.

## 5. Combined endpoint

### Corollary CMR491 — PROVED

After minimum-cost normalization, sparse level-skeleton reduction, and same-
level colour polarization, every mixed zero-cost obstruction reaches at least
one of the following structures.

1. A vertex-disjoint mixed-cycle batch giving simultaneous resampling.
2. A sparse boundary-tail interface whose deletion leaves colour factorization.
3. A boundary theta fan whose dirty nonrooted states pay pairwise distinct
   private entering edges.
4. A repeated-cell secant star centered at one boundary source-switch cell.
5. A compatible rank-two paid-pair cylinder arising from a two-edge cycle
   bottleneck.

### Proof

Combine CMR476, CMR481, CMR486, CMR489, and CMR490. ∎

## 6. Revised frontier

The active frontier has now returned to geometric objects already developed in
the repository.

- The secant-star branch should be charged by the existing carry-dispersion,
  line-energy, heavy-prefix, wall, or token alternatives.
- The fixed rank-two cylinder should be integrated with line-clean paid-pair
  completion and rank-zero/rank-one collateral bounds.
- Private theta edges and simultaneous cycle batches already carry explicit
  incidence payment.
- Sparse interfaces give recursive dimension reduction.

The next strict theorem should therefore splice CMR491 into the existing
CMR330--CMR393 line-clean/secant-star endpoint, rather than introduce another
abstract matching-state count.

No all-`n` theorem is claimed. Rooted-star disjointness, cycle-arm presence, and
rank-two compatibility are checked in
[`scripts/verify_prime_power_rooted_star_pair_cylinder.py`](../scripts/verify_prime_power_rooted_star_pair_cylinder.py).
