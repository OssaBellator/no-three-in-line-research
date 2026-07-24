# Iterated Hall-wall peeling on dense parent hosts

CMR203--CMR205 peel one majority wall from the full derangement law. The
matching argument itself is deterministic and can be iterated after forbidding
the designated wall cells. This chapter carries the iteration until the host
reaches the sharp half-degree matching threshold.

Let `H` be a balanced bipartite graph on `t+t` vertices. Its edges are allowed
parent-board cells. Assume that every vertex on both sides has degree at least
`d`, and that a family of rank-`1/2/3` candidate cylinders covers every perfect
matching of `H`.

## 1. Dense-host Hall wall

### Theorem CMR206 — PROVED

There is one source row or target column containing at least

\[
\boxed{
d-\left\lfloor\frac{t-1}{2}\right\rfloor
}
\]

allowed cells which occur in candidate certificates.

After assigning one containing certificate to each such cell, one rank occurs
on at least one third of that number, rounded up.

### Proof

Let `U` be the union of allowed host cells which occur in candidate
certificates. If `H\setminus U` had a perfect matching, that matching would
contain no candidate cylinder and would be uncovered. Hence Hall's theorem
gives a source set `A` with

\[
|N_{H\setminus U}(A)|<|A|.
\]

Put `T` equal to the complement of that neighbourhood. Then `|A|+|T|>t`, and
every host edge in `A times T` belongs to `U`.

Write `a=|A|` and `b=|T|`. If `a<=b`, then

\[
b\ge\left\lceil\frac{t+1}{2}\right\rceil.
\]

Every source vertex of `A` has at least `d` host neighbours in total and at
most `t-b` outside `T`. It therefore has at least

\[
d-(t-b)
\ge
d-\left\lfloor\frac{t-1}{2}\right\rfloor
\]

supported host neighbours in `T`. If `b<a`, apply the same argument on the
target side. The three-rank pigeonhole principle proves the final assertion.
∎

## 2. One degree-preserving peel

Put

\[
h=\left\lceil\frac t2\right\rceil,
\qquad
e=d-h.
\]

For `e>=1`, CMR206 supplies at least `e+1` supported cells in one board row or
column.

### Theorem CMR207 — PROVED

Choose

\[
b(e)=\left\lceil\frac{e+1}{3}\right\rceil
\]

cells assigned certificates of one common majority rank, and delete those
cells from `H`. Call the new host `H'`.

Then

1. every vertex of `H'` has degree at least `d-b(e)`;
2. every perfect matching of `H'` avoids all chosen certificates;
3. the remaining candidate certificates cover every perfect matching of `H'`;
4. `H'` still has a perfect matching whenever `d-b(e)>=h`.

### Proof

The chosen cells lie in one source row or one target column. The wall vertex
loses `b(e)` edges, while every vertex on the other side loses at most one.
Thus the new minimum degree is at least `d-b(e)`.

Each chosen certificate contains its assigned deleted wall cell, so no perfect
matching of `H'` can realize that certificate. The original candidate family
covered every perfect matching of `H`; hence after the chosen certificates are
removed, the remaining family covers every perfect matching of `H'`.

Finally a balanced bipartite graph of minimum degree at least `t/2` has a
perfect matching by the Hall argument used in CMR128. ∎

## 3. Complete half-degree descent

Start with the derangement host

\[
H_0=K_{t,t}\setminus I,
\qquad d_0=t-1.
\]

Define guaranteed degrees recursively while `e_j=d_j-h>=1`:

\[
b_j=\left\lceil\frac{e_j+1}{3}\right\rceil,
\qquad
d_{j+1}=d_j-b_j.
\]

### Theorem CMR208 — PROVED

Repeated application of CMR207 reaches a residual host `H_*` with

\[
\delta(H_*)\ge h=\left\lceil\frac t2\right\rceil
\]

and hence with a perfect matching.

The process has the following exact properties.

1. The number of peels is `O(log t)`.
2. The peeled wall cells are all distinct.
3. The total number of peeled cells is
   \[
   \boxed{
   d_0-h
   =
   \left\lfloor\frac t2\right\rfloor-1.
   }
   \]
4. Every perfect matching of `H_*` avoids every certificate assigned to a
   peeled cell.

### Proof

At each stage CMR207 applies. The guaranteed excess obeys

\[
e_{j+1}
=
e_j-\left\lceil\frac{e_j+1}{3}\right\rceil
<
\frac{2e_j}{3}
\]

for `e_j>=1`, proving logarithmic termination. The process stops at excess
zero, so the telescoping sum of all `b_j` equals `e_0=d_0-h`.

Deleted cells never re-enter the host, hence they are distinct. Every assigned
certificate contains its deleted cell, so every residual perfect matching
avoids all of them. The final minimum-degree and perfect-matching statements
follow from CMR207. ∎

## 4. Executable wall or linear candidate-only avoidance

### Corollary CMR209 — PROVED

During the CMR208 descent, at least one of the following holds.

1. Some peeled majority wall has rank one or rank two. CMR201 gives an
   executable alternating endpoint bank neutralizing a positive fraction of
   that wall's certificates.
2. Every peeled majority wall has rank three. Then there are
   \[
   \boxed{
   \left\lfloor\frac t2\right\rfloor-1
   }
   \]
   distinct rank-three candidate triples, each with a different designated
   peeled cell, and one residual parent matching avoids all of them
   simultaneously.

In the second alternative the globally frozen state must be explained by
candidate certificates outside this entire linear rank-three family.

### Proof

The first alternative is CMR201. Otherwise every assigned certificate in every
peel has rank three. CMR208 gives the exact number of distinct peeled cells and
a residual perfect matching avoiding all assigned certificates. Since the
remaining candidate family covers that matching, its new triples lie outside
the peeled family. ∎

## 5. Revised internal no-return endpoint

The candidate-only Hall wall is not stable under parent resampling. Either an
anchored wall exposes an executable alternating bank, or a linear family of
rank-three candidate triples can be removed simultaneously while preserving a
dense perfect-matching host.

The remaining theorem is now to iterate **certificate-family replacement**:
show that repeatedly replacing a linear avoided rank-three family by a new
cover cannot reuse the same primitive line/carry signatures before the
half-degree host or the envelope depth supplies a strict payment.

No all-`n` theorem is claimed here. The degree recurrence, telescoping peel
count, and residual matching threshold are checked in
[`scripts/verify_prime_power_iterated_hall_peeling.py`](../scripts/verify_prime_power_iterated_hall_peeling.py).
