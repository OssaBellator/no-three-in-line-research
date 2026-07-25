# Thin Hall blockers have negligible canonical cover mass

CMR276 and CMR277 isolate width-three full candidate triples and width-two
chords with external third-point witnesses. These canonical events are highly
incompatible in matching space: every one prescribes a different cell on the
same two or three Hall-side board vertices. Their total target-specific measure
is only quadratic-inverse. Thus a frozen thin blocker must be accompanied by an
almost complete additional rank-three cover.

Retain the target-specific state space

\[
\Omega_*
=
\{\pi\in S_t:z_*\notin\pi\}.
\]

The rank-three atom bound from CMR248 is

\[
\alpha_3
=
\frac1{(t-1)^2(t-2)}.
\]

## 1. Exact width-two chord structure

### Theorem CMR284 — PROVED

Let a sharp target-specific Hall blocker have smaller side `n=2`. Its available
line--rectangle incidence structure is one of the following.

1. **Perfect chord matching.** The target cell lies outside the Hall rectangle.
   Every one of the `t-1` blocking lines has two available Hall cells, and the
   resulting chords form a perfect matching between the two sets of `t-1` Hall
   cells.
2. **One repeat and the target omission.** The target cell lies in the Hall
   rectangle. Every blocking line is a full available chord; one available Hall
   cell lies on two chords, `z_*` is uncovered by the available line sets, and
   every other Hall cell lies on exactly one chord.
3. **One deficient line.** The target cell lies in the Hall rectangle. Exactly
   `t-2` lines are full available chords forming a matching, the remaining line
   has exactly one available Hall cell, and all covered Hall cells are distinct.
   The unique uncovered Hall cell is `z_*`.

In every case there are at least `t-2` full chords with pairwise disjoint Hall
endpoints.

### Proof

CMR277 gives

\[
D+\Omega\le1.
\]

Both quantities are nonnegative integers.

If `D=0`, every line has two available Hall cells. If also `Omega=0`, the
`2(t-1)` available chord incidences cover `2(t-1)` distinct Hall cells. Thus
`z_*` cannot lie in the rectangle, and the chords form the perfect matching.
If `Omega=1`, the same incidence count covers `2(t-1)-1` distinct cells. The
sole permitted uncovered Hall cell is `z_*`, and exactly one available cell is
repeated.

If `D=1`, then `Omega=0`. Exactly one line has one available Hall cell and every
other line is full. All available incidences are distinct. The union has
`2(t-1)-1` cells, so the sole uncovered Hall cell is `z_*`. The full chords are
pairwise endpoint-disjoint.

In the repeated-cell case, remove one of the two chords using the repeated cell.
At least `t-2` pairwise endpoint-disjoint full chords remain. ∎

## 2. Width-three disjoint triple extraction

### Theorem CMR285 — PROVED

Let a sharp target-specific Hall blocker have smaller side `n=3`. It contains at
least

\[
\boxed{t-9}
\]

lines with three available Hall-rectangle cells whose candidate triples are
pairwise disjoint as board cells.

Every two of these rank-three matching events are mutually exclusive under
`Omega_*`.

### Proof

CMR276 gives at least `t-5` full available three-cell lines and total repeated
available-incidence mass at most four. For every Hall cell used by more than one
full line, remove all but one of those lines. Removing at most

\[
\sum_z\max\{0,\deg(z)-1\}
\le4
\]

lines makes the surviving full triples cell-disjoint. At least `t-9` remain.

All surviving triples use the same three source vertices when the smaller Hall
side is on the source side, or the same three target vertices in the dual case.
Distinct prescriptions on a common matching vertex cannot occur in one perfect
matching. Hence the events are pairwise mutually exclusive. ∎

## 3. Canonical thin-event mass

### Theorem CMR286 — PROVED

For a width-two blocker, choose one candidate-only rank-three witness containing
each of the `t-2` disjoint full chords from CMR284. For a width-three blocker,
use the `t-9` disjoint full triples from CMR285.

In either case the chosen canonical events are pairwise mutually exclusive and
their union has target-specific probability at most

\[
\boxed{
\frac1{(t-1)^2}.
}
\]

### Proof

In width two, every chosen event contains its distinct full chord. All chords
prescribe different cells on the same two Hall-side matching vertices, so two
events cannot occur together. CMR248 gives

\[
\Pr(\text{chosen width-two event})\le\alpha_3.
\]

Therefore the union probability is at most

\[
(t-2)\alpha_3
=
\frac1{(t-1)^2}.
\]

The width-three events are mutually exclusive by CMR285, and their number is at
most `t-2` for every relevant block size. The same bound follows. ∎

## 4. Cubic outside-cover expansion

### Corollary CMR287 — PROVED

Assume the target-specific cover is anchored-free, so every bad event has rank
three. If it contains a sharp width-two or width-three Hall blocker, then beyond
the canonical thin events chosen in CMR286 it contains at least

\[
\boxed{
t(t-2)^2
}
\]

additional distinct candidate-only rank-three prescriptions.

### Proof

The canonical family covers probability at most `1/(t-1)^2`. Hence the other
rank-three events must cover probability at least

\[
1-rac1{(t-1)^2}.
\]

Every rank-three event has probability at most

\[
\alpha_3
=
\frac1{(t-1)^2(t-2)}.
\]

The union bound therefore requires at least

\[
\left(1-rac1{(t-1)^2}\right)
(t-1)^2(t-2)
=
\bigl((t-1)^2-1\bigr)(t-2)
=
t(t-2)^2
\]

additional events. ∎

## 5. Revised thin-blocker endpoint

Width-two and width-three geometry cannot by itself explain a frozen parent.
Its canonical events occupy only `O(t^{-2})` of matching space. Freezing forces
a cubic additional candidate-only population, to which CMR250's localized
vertex-load and dyadic-height conclusions apply.

The remaining theorem should combine the exact thin geometry with that cubic
outside population: either extract an anchored continuation, force a second
Hall factor on a different board vertex, or charge the additional events to
low-height quotient/carry signatures.

No all-`n` theorem is claimed here. The width-two incidence classification,
width-three disjoint extraction, and cover-mass arithmetic are checked in
[`scripts/verify_prime_power_thin_blocker_expansion.py`](../scripts/verify_prime_power_thin_blocker_expansion.py).
