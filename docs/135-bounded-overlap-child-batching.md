# Bounded-overlap batching closes the diffuse child interface

PX280 reduces recursive termination to a strict-sign-or-child interface.  The
remaining difficulty is that one rematching step may replace `D` destroyed
unresolved certificates by `C>=D` newly created certificates.  One must assign
enough of the new certificates to deeper children that the current unresolved
coordinate decreases, while keeping the child banks structurally executable.

Every rank-at-most-three certificate uses at most six endpoint labels.  This
bounded support turns the assignment problem into an elementary hypergraph
edge-colouring statement.  Diffuse collateral with bounded endpoint overlap can
be scheduled in finitely many endpoint-disjoint child batches.  The only
remaining obstruction is a high-overlap endpoint core.

## 1. Certificate support hypergraph

Let `mathcal C` be a finite family of realized new certificates.  For
`gamma in mathcal C`, let `S(gamma)` be its endpoint-index support.  By PX201,

\[
1\le |S(\gamma)|\le6.
\]

Define the maximum endpoint overlap

\[
\Lambda(\mathcal C)
=
\max_x |\{\gamma:x\in S(\gamma)\}|.
\]

Two certificates conflict when their supports intersect.

### Theorem PX299 -- PROVED

The family `mathcal C` can be partitioned into at most

\[
\boxed{6\Lambda(\mathcal C)-5}
\]

subfamilies whose endpoint supports are pairwise disjoint.

Consequently `mathcal C` contains an endpoint-disjoint subfamily of size at
least

\[
\boxed{
\frac{|\mathcal C|}{6\Lambda(\mathcal C)-5}
}.
\]

### Proof

The conflict graph of one certificate `gamma` has degree at most

\[
\sum_{x\in S(\gamma)}(\deg(x)-1)
\le6(\Lambda-1).
\]

A graph of maximum degree at most `6(Lambda-1)` is greedily colourable with
`6Lambda-5` colours.  Each colour class has disjoint supports.  The largest
class gives the second display. \(\square\)

The estimate is valid with repeated geometric types because the vertices are
actual realized certificates.

## 2. Exact excess-to-child assignment

Suppose one decoder transition destroys `D>=1` unresolved certificates at its
current level and realizes `C` new unresolved certificates.

### Theorem PX300 -- PROVED

If `C<D`, the current unresolved coordinate strictly decreases immediately.
If `C>=D`, designate

\[
\boxed{q=C-D+1}
\]

of the new certificates as deeper children and leave the other `C-q=D-1`
unassigned at the current level.  Then the current unresolved coordinate
strictly decreases by at least one.

The designated set can be partitioned into at most

\[
\boxed{6\Lambda-5}
\]

endpoint-disjoint child batches, where `Lambda` is its maximum endpoint overlap.

### Proof

The first statement is direct counting.  In the second case, after designating
`q` certificates the unresolved remainder is

\[
C-q=C-(C-D+1)=D-1.
\]

Apply PX299 to the designated set. \(\square\)

Thus the number of new certificates is not itself an obstruction; only their
endpoint overlap affects scheduling.

## 3. Typed executable batches

Assume the selected state is decomposed into two permutation layers and `Q`
arithmetic channels.  Every endpoint has one of at most `2Q` layer-channel
types.

For every certificate in one endpoint-disjoint batch, choose one endpoint which
its child decoder is allowed to move.  The chosen endpoints are distinct.
Partition them by type.

### Theorem PX301 -- PROVED

A designated family of overlap at most `Lambda` can be scheduled into at most

\[
\boxed{2Q(6\Lambda-5)}
\]

endpoint-disjoint, single-type child blocks.

Across the complete schedule, any endpoint label is used by at most `Lambda`
child certificates.  Hence the additional historical-position degree needed to
process all these children is at most `Lambda` per endpoint label.

Blocks below the quantitative spread threshold may be sent directly to the
exact terminal optimizer PX273--PX276.

### Proof

PX299 supplies at most `6Lambda-5` support-disjoint colours.  Inside one colour,
chosen endpoints are distinct because the complete supports are disjoint.
Splitting by the at most `2Q` types gives the displayed number of blocks.

A label occurs in at most `Lambda` certificate supports, so it can be selected
and moved at most `Lambda` times across the schedule.  Each such move contributes
at most one historical position in its row and column. \(\square\)

This theorem permits several child blocks at the same causal depth; it does not
require one new recursion level per certificate.

## 4. Strict-sign-or-overlap dichotomy

### Corollary PX302 -- PROVED

Fix an overlap threshold `B>=1`.  Every decoder transition which destroys at
least one current unresolved certificate has one of the following outcomes.

1. **Immediate sign.**  It creates fewer certificates than it destroys.
2. **Bounded-overlap child conversion.**  Enough new certificates can be assigned
   to at most `2Q(6B-5)` typed endpoint-disjoint child blocks so that the current
   unresolved coordinate decreases.  The historical degree cost is at most `B`.
3. **High-overlap endpoint core.**  One endpoint label belongs to more than `B`
   realized new certificates.

In the third case, partitioning by the nine support sectors `(r,u)` produces one
fixed endpoint and one sector containing more than `B/9` certificates.

### Proof

Apply PX300.  If the designated excess family has maximum overlap at most `B`,
use PX301.  Otherwise some endpoint has degree greater than `B`.  There are nine
support sectors, so one sector carries more than one ninth of that endpoint
load. \(\square\)

Therefore the diffuse strict-sign-or-child frontier is closed under bounded
overlap.  The remaining geometric problem is sharply localized:

> classify a fixed endpoint supporting a large number of realized certificates
> in one rank/support sector.

Rank-one overlap is a coordinate star field, rank-two support four is a packet
hub, and the path/cycle sectors return to the rainbow and short-cycle decoders.
The exact quantitative conversion for every high-overlap sector is the next
frontier.

## 5. Verification

Run

```bash
python scripts/verify_product_bounded_overlap_batching.py
```

The verifier exhausts small support hypergraphs, checks the conflict-degree and
greedy-colouring bounds, tests exact excess assignment, and validates the typed
batch and historical-degree counts on randomized certificate families.