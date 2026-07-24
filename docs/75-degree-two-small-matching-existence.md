# Small degree-two forbidden matching boards

CMR110 gives a quantitative state count for endpoint boards of size at least
seven. The alternating-closure descent needs less: after a new secant star has
been extracted, it only needs one row-column-preserving state that moves every
chosen endpoint and avoids the other permutation layer.

Let `F` be a forbidden subset of a `t` by `t` matching board with at most two
forbidden cells in each row and column. Let `G` be the bipartite graph of allowed
cells.

## Theorem CMR128 — PROVED

For every

\[
t\ge4,
\]

`G` has a perfect matching.

Consequently every endpoint-disjoint secant star of size at least four, whose
chosen movable endpoints lie in one permutation layer, has at least one
row-column-preserving alternating state that

1. moves every chosen endpoint;
2. avoids every cell occupied by the other permutation layer;
3. preserves saturation and layer disjointness;
4. destroys all chosen original star triples.

### Proof

Every vertex of `G` has degree at least

\[
t-2\ge\frac t2.
\]

We verify Hall's condition. Let `A` be a subset of the left vertex class.

If `|A|<=t/2`, then

\[
|N(A)|\ge\delta(G)\ge\frac t2\ge|A|.
\]

Now suppose `|A|>t/2`. If `|N(A)|<|A|`, then the right-side complement

\[
T=R\setminus N(A)
\]

is nonempty. Every vertex of `T` has all its neighbours in the left-side
complement of `A`, which has size

\[
t-|A|<\frac t2.
\]

This contradicts `delta(G)>=t/2`. Hence `|N(A)|>=|A|` in every case, and Hall's
theorem gives a perfect matching.

For an alternating endpoint board, the forbidden cells are the original
endpoint matching and the cells occupied by the other permutation layer. Their
row and column degrees are at most two. An allowed perfect matching therefore
moves every endpoint, avoids the other layer, and uses exactly the old endpoint
row and column sets. The four conclusions follow. ∎

## Sharpness of the size threshold

The statement is false at `t=3`. Normalize the first forbidden matching to the
identity and take the second to be the transposition `(0 1)` fixing `2`. The
first two source rows then both have only target `2` available, so no perfect
matching exists.

Thus size four is the correct universal threshold when no further structure is
assumed. No spread or state-count claim is made for sizes four through six.

The finite small-board checks are included in
[`scripts/verify_prime_power_global_baseline_closure.py`](../scripts/verify_prime_power_global_baseline_closure.py).
