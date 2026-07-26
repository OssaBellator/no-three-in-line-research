# Constant-arity completeness paths have a polynomial support cover

CMR862--CMR877 attach one canonical new target triple to every nonimproving
candidate and give a support packing/cover dichotomy. Along one stable-owner
root-to-leaf path, support-disjoint triple signatures consume distinct resources.
A deletion child spends one previously undeleted labelled edge; a conditioned
branch contracts three labelled edges. These two resources have polynomial total
capacity.

Fix one labelled two-layer owner of side `n`, and follow one root-to-leaf path of
the completeness scheduler before any owner, factor-vertex, or envelope exit and
before strict potential improvement. Let

\[
U_n=2n^2-2n
\]

be the maximum single-edge deletion depth from CMR833, and define

\[
\boxed{
B_n
=
U_n+\left\lfloor\frac{2n}{3}\right\rfloor.
}
\]

Let `\mathcal C` be the distinct canonical new labelled triple signatures
encountered on the path.

## 1. Deletion and contraction resources

### Theorem CMR878 -- PROVED

Along the path:

1. at most `U_n` distinct labelled edges are deleted by single-edge side branches;
2. the total number of rank-three conditioned contractions is at most
   \[
   \boxed{\left\lfloor\frac{2n}{3}\right\rfloor;}
   \]
3. every canonical candidate triple is resolved by one deletion of one of its
   edges, one conditioned contraction, or a structural/potential exit.

### Proof

The first statement is CMR833 on a labelled universe of size `2n^2` with a
surviving state of size `2n`. Every rank-three contraction lowers the common state
cardinality by three, which starts at `2n` and never increases. The final
statement is CMR867--CMR868. ∎

## 2. Support-disjoint signatures consume distinct resources

### Theorem CMR879 -- PROVED

Let `C_1,...,C_r` be canonical triples on the path with pairwise disjoint
nine-atom supports. If none is terminated by a structural or potential exit,
then

\[
\boxed{r\le B_n.}
\]

### Proof

Resolve each signature by CMR867. A deletion resolution chooses one edge of its
triple. Support disjointness makes these deleted edges distinct across the
family. A conditioned resolution contracts its rank-three prescription; support
disjointness makes the prescriptions endpoint- and cell-disjoint, so no
contraction is charged to two signatures. CMR878 gives at most `U_n` deletions
and at most `floor(2n/3)` contractions. ∎

If one contraction or deletion invalidates a later signature through an owner or
endpoint change, that is the excluded structural-exit branch.

## 3. Historical support-matching number is polynomial

### Theorem CMR880 -- PROVED

Absent a structural or potential exit, the support hypergraph of `\mathcal C`
has matching number at most

\[
\boxed{\nu(\mathcal C)\le B_n.}
\]

### Proof

Any support matching is a pairwise support-disjoint family and is bounded by
CMR879. ∎

This is a path-history statement; the triples need not occur simultaneously.

## 4. Polynomial support cover

### Theorem CMR881 -- PROVED

Absent a structural or potential exit, there is a support cover

\[
W\subseteq\Omega_n
\]

meeting every distinct canonical triple signature on the path and satisfying

\[
\boxed{|W|\le9B_n.}
\]

### Proof

Take a maximal support matching. By CMR880 it has at most `B_n` members. The
union of their nine-atom supports covers every signature by maximality and has
size at most `9B_n`. ∎

## 5. One support atom carries many distinct signatures

### Theorem CMR882 -- PROVED

If `L=|\mathcal C|`, then one physical cell or one labelled matching vertex
belongs to at least

\[
\boxed{
\left\lceil\frac{L}{9B_n}\right\rceil
}
\]

distinct canonical triple signatures.

### Proof

Assign each signature to its first atom in the cover from CMR881 and average. ∎

A matching-vertex atom refines by CMR874 to a distinct-cell wall or a repeated
physical cell.

## 6. Episode bound without triple or support recurrence

Let `M` be the number of nonimproving target-destroying candidate episodes on the
path. Fix integers `lambda,d>=2`.

### Theorem CMR883 -- PROVED

Before a structural or potential exit, at least one of the following holds.

1. One exact labelled canonical triple occurs in at least `lambda` episodes.
2. One support atom belongs to at least `d` distinct canonical triple signatures.
3.
   \[
   \boxed{
   M
   \le
   (\lambda-1)9B_n(d-1).
   }
   \]

### Proof

If branch 1 fails, CMR871 gives at least
`ceil(M/(lambda-1))` distinct signatures. If branch 2 also fails, CMR882 gives

\[
\left\lceil\frac{L}{9B_n}\right\rceil\le d-1,
\]

so `L\le9B_n(d-1)`. Multiply by `lambda-1`. ∎

This is an explicit polynomial history bound for fixed thresholds.

## 7. Geometric interpretation of the concentrated atom

### Theorem CMR884 -- PROVED

The support-concentration branch of CMR883 is exactly one of:

1. one physical target cell occurring in `d` distinct new-triple signatures;
2. one labelled source column or target row incident with `d` signatures, which
   yields at least `ceil(sqrt(d))` distinct cells on that vertex or one physical
   cell in more than `sqrt(d)` signatures.

### Proof

These are the support atom types of CMR873. Apply CMR874 in the matching-vertex
case. ∎

Both outputs enter the recurrent-cell, candidate-wall, secant-star, protected-
line, and target-handoff machinery already indexed.

## 8. Constant-arity path endpoint

### Corollary CMR885 -- PROVED

At one stable owner, a constant-arity completeness path reaches at least one of:

1. the explicit episode bound CMR883;
2. one recurrent exact new triple;
3. one recurrent physical target cell;
4. a labelled matching-vertex wall or repeated-cell star;
5. distinct deletion depletion;
6. compatible forced-triple contraction;
7. owner, factor, endpoint, or envelope exit;
8. strict potential improvement.

Thus the remaining completeness tree cannot have both long paths and diffuse
new-triple geometry. Long paths force one of the existing local geometric
recurrence mechanisms. The unresolved issue is global merging of side branches
which reach the same recurrent support atom or structural owner.

### Proof

Combine CMR878--CMR884 with CMR870--CMR877 and the local recurrence endpoints
CMR698--CMR829. ∎

No all-`n` theorem is claimed. Resource capacities, support matching and cover,
concentration, and episode arithmetic are checked in
[`scripts/verify_prime_power_constant_arity_path_budget.py`](../scripts/verify_prime_power_constant_arity_path_budget.py).
