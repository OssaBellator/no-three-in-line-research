# Sparse rollback converts terminal ancestry into cheap escape or host factorization

CMR433--CMR438 compress one deletion pass to at most `t` historical batch
exchange cycles, but those cycles are valid at different host epochs.  This
chapter gives an exact temporal lifting mechanism.  A perfect matching which
avoided a final essential edge before the deletions uses at most `t` deleted
edges.  Restoring only those matching edges, rather than an entire deletion
suffix, already recreates an avoiding state.

A minimum rollback has additional structure: every restored edge is essential
in the avoiding host.  Hence an expensive rollback factors off a large forced
matching and strictly reduces the residual host size.

Let

\[
G_0\supset G_1\supset\cdots\supset G_d=G,
\qquad
G_i=G_{i-1}-f_i,
\]

be a nested deletion pass on a balanced bipartite graph with `t` vertices on
each side.  Assume every `G_i` has a perfect matching and `G_0` has no essential
edge.  Put

\[
\Delta=E(G_0)\setminus E(G)=\{f_1,\ldots,f_d\}.
\]

For an edge `e` essential in `G`, define its **rollback number**

\[
\kappa(e)
=
\min\bigl\{|R|:R\subseteq\Delta,
\operatorname{PM}(G+R-e)\ne\varnothing\bigr\}.
\]

Here `G+R` means that the deleted edges in `R` are restored.

## 1. Sparse rollback escape

### Theorem CMR439 — PROVED

For every

\[
e\in\operatorname{Ess}(G),
\]

one has

\[
\boxed{1\le\kappa(e)\le t.}
\]

More precisely, every perfect matching

\[
M\in\operatorname{PM}(G_0),
\qquad e\notin M,
\]

supplies a rollback footprint

\[
R_M=M\cap\Delta
\]

such that

\[
|R_M|\le t,
\qquad
M\in\operatorname{PM}(G+R_M-e).
\]

### Proof

Because `G_0` has no essential edge, there is a perfect matching `M` of `G_0`
avoiding `e`.  Every edge of `M` which is not in `G` belongs to `\Delta`, so

\[
M\subseteq E(G)\cup R_M.
\]

Thus `M` is a perfect matching of `G+R_M-e`.  Since a perfect matching has
exactly `t` edges, `|R_M|\le t`.

The rollback footprint cannot be empty: if `R_M=\varnothing`, then `M` would be
a perfect matching of `G` avoiding the essential edge `e`.  Hence
`\kappa(e)\ge1`. ∎

This is sparse temporal lifting.  It restores only the deleted edges actually
used by one avoiding matching, not all deletions after the first-essentiality
time of `e`.

## 2. Minimum rollback sets are forced matching cores

Let `R\subseteq\Delta` attain `\kappa(e)` and put

\[
H=G+R-e.
\]

### Theorem CMR440 — PROVED

Every edge of `R` is essential in `H`.  Consequently:

1. `R` is a matching;
2. every perfect matching of `H` contains all edges of `R`;
3. writing `V(R)` for the endpoints of `R`, restriction gives the exact
   factorization
   \[
   \boxed{
   \operatorname{PM}(H)
   \cong
   \{R\}
   \times
   \operatorname{PM}\bigl(H-V(R)\bigr).
   }
   \]

In particular, if `|R|=k`, the residual matching problem has side length
`t-k`.

### Proof

Choose `r\in R`.  If `H` had a perfect matching `N` avoiding `r`, then

\[
N\subseteq E(G)\cup(R\setminus\{r\})
\]

and `N` would avoid `e`.  This would give a rollback set of size at most
`|R|-1`, contradicting minimality.  Hence every perfect matching of `H`
contains `r`.  This holds for every `r\in R`.

Essential edges in a matchable bipartite graph form a matching by CMR429, so
`R` is pairwise vertex-disjoint.  Since every perfect matching contains `R`,
removing those forced edges and their endpoints gives the displayed bijection.
∎

Thus rollback expense is not unstructured.  Every restored edge in a minimum
footprint is a forced factor of the avoiding matching space.

## 3. Cost-or-decomposition dichotomy

### Corollary CMR441 — PROVED

Fix an integer threshold

\[
1\le q\le t.
\]

For every final essential edge `e`, exactly one of the following alternatives is
available.

1. **Cheap rollback.**
   \[
   \boxed{\kappa(e)<q.}
   \]
   Restoring fewer than `q` deleted edges produces a perfect matching avoiding
   `e`.
2. **Strict host factorization.** A minimum rollback set `R` has
   \[
   |R|=\kappa(e)\ge q,
   \]
   every edge of `R` is forced in `G+R-e`, and
   \[
   \boxed{
   \operatorname{PM}(G+R-e)
   \cong
   \{R\}
   \times
   \operatorname{PM}\bigl((G+R-e)-V(R)\bigr)
   }
   \]
   with residual side length at most `t-q`.

### Proof

Apply CMR440 to a minimum rollback set.  The two cases are the alternatives
`\kappa(e)<q` and `\kappa(e)\ge q`. ∎

Large temporal lifting cost therefore forces an exact lower-dimensional host,
which is one of the desired ancestry endpoints.

## 4. Terminal certificate escape

### Corollary CMR442 — PROVED

Let `Q` be a fully forced rank-`1/2/3` certificate in the final host `G`.  For
every prescribed edge `e\in Q`, there is a rollback set `R_e` with

\[
1\le |R_e|\le t
\]

such that `G+R_e` has a perfect matching avoiding `e`, and hence avoiding `Q`.
In particular,

\[
\boxed{
\min_{e\in Q}\kappa(e)\le t.
}
\]

For every threshold `q`, the terminal certificate therefore admits either a
rollback using fewer than `q` deleted edges or an exact factorization which
removes at least `q` rows and `q` columns from the residual matching problem.

### Proof

Apply CMR439 and CMR441 to any prescribed edge of `Q`.  A perfect matching
avoiding one prescribed edge cannot realize the whole certificate. ∎

CMR442 resolves the purely temporal existence question.  The remaining issue is
to pay for restored forbidden edges in the geometric repair ledger.

## 5. Global rollback incidence and overlap

Let

\[
E_*=\operatorname{Ess}(G),
\qquad
s=|E_*|\le t,
\]

and choose one minimum rollback set `R_e` for each `e\in E_*`.

### Theorem CMR443 — PROVED

The total rollback incidence satisfies

\[
\boxed{
\sum_{e\in E_*}|R_e|
\le st
\le t^2.
}
\]

For every integer `\lambda\ge2`, at least one of the following holds.

1. **Rollback concentration.** Some deleted edge belongs to at least `\lambda`
   of the sets `R_e`.
2. **Disjoint rollback packing.** There is a pairwise disjoint subfamily of size
   at least
   \[
   \boxed{
   \left\lceil
   \frac{s}{t(\lambda-1)}
   \right\rceil.
   }
   \]

More generally, if attention is restricted to edges with `\kappa(e)<q`, the
factor `t` in the denominator may be replaced by `q-1`.

### Proof

The incidence bound follows from CMR439 and `s\le t`.

Assume the concentration alternative fails, so every deleted edge belongs to at
most `\lambda-1` rollback sets.  Greedily choose one rollback set and discard
all sets intersecting it.  A chosen set has at most `t` edges, and each of those
edges belongs to at most `\lambda-1` sets.  Hence one greedy choice discards at
most `t(\lambda-1)` sets, including itself.  The displayed packing bound
follows.  If every chosen footprint has size at most `q-1`, use that bound in
place of `t`. ∎

This is the first common-epoch rollback dichotomy.  Many final essential edges
have disjoint sparse escape footprints, or many escapes concentrate on one
previously deleted edge.  The concentration branch is suitable for Hall,
prefix, carry, or envelope analysis; the disjoint branch is suitable for a
reserve-depletion or independent-rollback argument.

## 6. Revised frontier

The temporal exchange obstruction now has three exact layers.

1. CMR438 compresses all historical essentiality creation to at most `t` batch
   exchange cycles.
2. CMR439--CMR442 show that every final forced edge or certificate can be escaped
   in a common expanded final epoch by restoring at most `t` deleted edges.
3. CMR440--CMR441 show that an expensive minimum rollback is itself a forced
   matching core and gives strict host factorization.
4. CMR443 bounds total minimum-rollback incidence by `t^2` and gives a disjoint
   packing versus concentrated deleted-edge dichotomy.

What remains is geometric payment for the cheap rollback branch: show that
restoring a small forbidden set consumes protected reserve, destroys target
load, opens a prefix/line-clean continuation, or forces envelope expansion.
Repeated compatible local ancestor resets still require an analogous canonical
rollback class.

No all-`n` theorem is claimed here.  Sparse rollback, minimum-core
factorization, terminal-certificate escape, and finite packing bounds are
checked in
[`scripts/verify_prime_power_sparse_rollback.py`](../scripts/verify_prime_power_sparse_rollback.py).
