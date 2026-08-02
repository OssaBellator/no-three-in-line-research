# Shell repertoire cycle mean

`docs/655` gives the exact cumulative-saving envelope for one prescribed burden
sequence. A geometric construction may instead choose among several macro states
whose available next variants depend on the current state. This chapter gives the
exact finite-state criterion.

Let a directed edge `e` represent one legal period transition. Write

```text
b(e) = 6*delta(e) + c(e)
w(e) = 3 - b(e),
```

where `w(e)` is its saving against the fifteen-control baseline.

## PP3dat — Reachable positive-cycle criterion

From an initial macro state, every fixed setup cost is amortizable exactly when
the reachable transition graph contains a directed cycle `C` with

```text
sum_{e in C} w(e) > 0.
```

Equivalently, a reachable cycle has mean burden below three.

### Proof

A positive cycle may be repeated until its accumulated saving exceeds any fixed
setup. Conversely, if every reachable cycle has nonpositive saving, removing a
cycle from a walk never decreases total saving. Every walk then has a simple
representative with at least as much saving, and the finite graph supplies a
uniform finite upper bound. ∎

## PP3dau — Optimal asymptotic rate is a cycle mean

The maximum asymptotic saving per period obtainable by an infinite legal walk is
the maximum reachable cycle mean of `w`, equivalently

```text
3 - minimum reachable cycle mean of b.
```

### Proof

Any long walk decomposes into a bounded simple prefix plus directed cycles, so its
limsup average cannot exceed the largest reachable cycle mean. Repeating a cycle
attaining that mean realizes equality. ∎

## PP3dav — Exact entry-plus-cycle setup bound

Suppose an entry path reaches a positive cycle with path saving `A` and cycle gain
`G>0`. The least number of complete cycle repetitions needed to beat setup `S`
is

```text
max(0, floor((S-A)/G) + 1).
```

An individually expensive entry or cycle edge is allowed; only the total cycle
gain controls indefinite amortization.

The checker example has entry saving `-2`, cycle burdens `(1,2)`, gain `3`, and
setup `7`; exactly four repetitions are necessary and sufficient.

## Verification

`scripts/check_shell_repertoire_cycle_mean.py` enumerates simple cycles in finite
transition graphs, checks the positive-cycle and entry formulas on exact rational
examples, and verifies bounded total saving in a graph with no positive cycle.

## Evidence boundary

No coordinate-level `(1,1,1)` macro transition graph with a reachable sub-three
mean-burden cycle has been constructed. The theorem is the exact scheduling
interface that such a repertoire must satisfy.
