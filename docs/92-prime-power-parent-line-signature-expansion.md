# Linear real-line signature expansion in a frozen parent cover

CMR186 forces at least `t-1` candidate cylinders in a frozen one-layer parent
bank, but many cylinders might in principle reuse the same geometric line. The
parent-board geometry prevents excessive reuse: every certificate line is a
partial matching, and a small family of such lines can be avoided
simultaneously.

Fix one nonroot one-layer envelope parent of size `t>=5`. Its column set is `C`,
its inherited moved-layer row set is `R`, and its allowed states are the
derangements of the old matching between `C` and `R`. Candidate certificates
have ranks one, two, or three and use fixed selected points outside the moved
layer block.

## 1. Certificate lines are genuine matching lines

### Theorem CMR196 — PROVED

No candidate certificate is supported on a horizontal or vertical real line.
Consequently every real line supporting a candidate certificate meets the
`C` by `R` parent board in a partial matching: at most one cell in each source
column and at most one cell in each target row.

### Proof

Consider a horizontal line whose row belongs to `R`. The current saturated
state has exactly two selected points in that grid row. One is the old moved
layer point and belongs to the removed block; only the opposite-layer point
remains fixed outside. A rank-one certificate would need two fixed outside
points on the horizontal line, which is impossible. Rank-two and rank-three
certificates would need at least two compatible candidate cells, but distinct
cells on one horizontal line share their target row and are incompatible.

The vertical case is identical. In a source column of `C`, one current point is
the old moved-layer point and the other is the opposite-layer point. Thus only
one fixed outside point remains, while two candidate cells in that column are
column-incompatible.

Every other real line meets each grid column and each grid row at most once, so
its parent-board cells form a partial matching. ∎

## 2. Avoiding a small line family

Let `Lambda` be a family of `q` real lines. Forbid

1. the old parent matching; and
2. every parent-board cell lying on a line of `Lambda`.

### Theorem CMR197 — PROVED

If

\[
q<\left\lfloor\frac t2\right\rfloor,
\]

then the remaining board has a perfect matching. This matching is a
derangement which uses no parent-board cell from any line in `Lambda`.

### Proof

By CMR196, each line contributes a partial matching to the forbidden board.
Together with the old diagonal, every source and target vertex has forbidden
degree at most `q+1`. Hence the allowed bipartite graph has minimum degree at
least

\[
t-q-1.
\]

The hypothesis implies `q+1<=t/2`, so the allowed minimum degree is at least
`t/2`.

The Hall argument from CMR128 applies verbatim. If a left set has size at most
`t/2`, one of its vertices already has at least `t/2` neighbours. If it has
size greater than `t/2` and its neighbourhood were smaller, a right vertex
outside the neighbourhood would have all its neighbours in a left complement
of size below `t/2`, contradicting the minimum-degree bound. Thus Hall's
condition holds and the perfect matching exists. ∎

The theorem is deliberately line-based. Several candidate certificates on one
line are all avoided at once.

## 3. Linear signature requirement

### Corollary CMR198 — PROVED

Every rank-`1/2/3` candidate-cylinder cover of the full parent derangement bank
uses at least

\[
\boxed{
\left\lfloor\frac t2\right\rfloor
}
\]

distinct real certificate lines.

In particular, every globally frozen inherited parent core has at least that
many real-line signatures in its candidate cover.

### Proof

Let `Lambda` be the set of all real lines supporting at least one candidate
certificate. If its size were smaller than `floor(t/2)`, CMR197 would give a
parent derangement using no candidate cell on any certificate line. Such a
state contains none of the prescribed cylinders and is therefore uncovered, a
contradiction. ∎

### Historical-ledger form

Let `Lambda_old` be any previously recorded set of internal line signatures in
the same envelope epoch. A new frozen parent cover has one of two outcomes:

1. it introduces a line outside `Lambda_old`; or
2. `Lambda_old` already contains at least `floor(t/2)` line signatures capable
   of supporting the complete cover.

Thus a no-return proof may now focus on bounded reuse of a **linear** line
population rather than arbitrary individual cylinders.

## 4. Interaction with the extremal secant fan

The equality case of CMR186 is stronger: a complete row or column shadow has
`t-1` distinct certificate lines, and CMR188 extracts a matching-or-star
alternating bank from their fixed secant endpoints.

CMR198 handles every nonextremal cover as well. Even when rank-two and
rank-three cylinders dominate, a frozen cover cannot collapse onto a bounded
number of geometric lines.

The remaining signature theorem is to refine these real-line signatures by
primitive direction, first-separation depth, and carry cell, and then prove
that one refined signature has bounded reuse inside a fixed closure envelope.

No all-`n` theorem is claimed here. The degree thresholds and small normalized
forbidden-line boards are checked in
[`scripts/verify_prime_power_parent_line_signatures.py`](../scripts/verify_prime_power_parent_line_signatures.py).
