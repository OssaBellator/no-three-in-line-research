# Thin first-separation populations give carry dispersion or a heavy cell

CMR295 and CMR296 extract a large family of thin-blocker lines with one common
Hall-pair separation depth and one projective direction.  The remaining base
coordinate of that signature is the common row prefix of the two Hall endpoint
cells.  Endpoint disjointness gives an exact capacity bound for one such cell.
Comparing the prefix scale with the square-root scale produces the same two
outcomes as the earlier carry-cell machinery: many distinct carry cells or one
heavy carry cell.

Let a normalized inherited parent block have size

\[
t=p^h.
\]

Fix two source slices whose displacement is divisible by `p^b`.  Consider a
family `F` of `M` compatible line events such that:

1. every event uses one endpoint on each fixed source slice;
2. the two endpoint row coordinates differ by a multiple of `p^b`;
3. the first-slice endpoint cells are pairwise distinct;
4. all endpoint pairs have one common projective direction after division by
   `p^b`.

For a row residue `c mod p^b`, let `F_c` be the events whose two Hall endpoint
rows are congruent to `c` modulo `p^b`.  The fixed source slices are also
congruent modulo `p^b`, so `(c,b)` identifies one normalized prefix carry cell.

## 1. Exact cell capacity and support

### Theorem CMR302 — PROVED

For every row-prefix cell,

\[
\boxed{|F_c|\le\frac{t}{p^b}.}
\]

Moreover,

\[
\boxed{
\#\{c:F_c\ne\varnothing\}
\ge
\operatorname{ceil}\left(\frac{Mp^b}{t}\right)
}
\]

and some cell satisfies

\[
\boxed{
|F_c|
\ge
\operatorname{ceil}\left(\frac{M}{p^b}\right).
}
\]

### Proof

The first endpoint rows in one residue class modulo `p^b` are distinct by
hypothesis.  Exactly `t/p^b` normalized rows lie in that class, proving the
capacity bound.  The support lower bound follows by dividing the total
population `M` by this capacity.  There are exactly `p^b` row residue classes,
so ordinary pigeonholing gives the final inequality. ∎

## 2. Square-root carry dichotomy

### Corollary CMR303 — PROVED

At least one of the following holds.

1. **Heavy carry cell.** Some prefix carry cell contains at least
   \[
   \boxed{
   \operatorname{ceil}\left(\frac{M}{\sqrt t}\right)
   }
   \]
   events.
2. **Carry dispersion.** The family occupies more than
   \[
   \boxed{\frac{M}{\sqrt t}}
   \]
   distinct prefix carry cells.

Every event in either outcome retains the same projective line direction.

### Proof

If `p^b<=sqrt(t)`, CMR302 gives a cell of size at least

\[
M/p^b\ge M/\sqrt t.
\]

If `p^b>sqrt(t)`, its support bound gives

\[
Mp^b/t>M/\sqrt t
\]

occupied cells.  The projective direction was fixed before the partition by
row residue. ∎

## 3. Width-two consequence

### Corollary CMR304 — PROVED

Let a sharp width-two blocker lie in a parent block of size `t=p^h`.  It exposes
one fixed projective direction and either

1. a prefix carry cell containing at least
   \[
   \boxed{
   \operatorname{ceil}\left(
   \frac{t-2}{(h+p-1)\sqrt t}
   \right)
   }
   \]
   canonical chord events; or
2. more than
   \[
   \boxed{
   \frac{t-2}{(h+p-1)\sqrt t}
   }
   \]
   distinct occupied carry cells.

The same conclusion holds with the sharper denominator `v_p(d)+p` when the
Hall-slice separation `d` is retained.

### Proof

Use the population `M` from CMR295 and apply CMR303. ∎

## 4. Width-three consequence

### Corollary CMR305 — PROVED

Let a sharp width-three blocker with `t=p^h>=10` be reduced to the disjoint
triple family from CMR288.  It exposes one fixed projective direction and either

1. a prefix carry cell containing at least
   \[
   \boxed{
   \operatorname{ceil}\left(
   \frac{t-9}{(h+p-1)\sqrt t}
   \right)
   }
   \]
   retained triples; or
2. more than
   \[
   \boxed{
   \frac{t-9}{(h+p-1)\sqrt t}
   }
   \]
   distinct occupied carry cells.

Again `h+p-1` may be replaced by `v_p(D)+p`, where `D` is the outer Hall-slice
separation.

### Proof

Apply CMR303 to the common-signature population from CMR296.  Cell-disjointness
of the retained triples implies the required distinctness of their first outer
endpoint cells. ∎

## 5. Revised carry-ledger target

The thin Hall obstruction is no longer an anonymous family of `t-O(1)` lines.
At one absolute first-separation scale and one direction in
`P^1(F_p)`, it supplies either

- a carry cell with load `Omega_p(sqrt(t)/log(t))`; or
- `Omega_p(sqrt(t)/log(t))` distinct occupied carry cells.

This exactly matches the local alternatives used by the earlier aligned-anchor
and collision-carry decompositions.  The remaining global theorem is a
bounded-reuse statement: charge dispersed cells to scale-direction complexity,
and show that a heavy cell opens an absorber or forces strict envelope
expansion.

No all-`n` theorem is claimed here.  Cell capacities, support counts, and the
square-root dichotomy are checked in
[`scripts/verify_prime_power_thin_signature_cells.py`](../scripts/verify_prime_power_thin_signature_cells.py).
