# Bounded-overlap Hall packing

The preceding Hall chapters assumed or numerically amplified resource-disjoint
four-centre source motifs.  This chapter replaces exact disjointness at generation
time by a bounded-overlap condition and gives the sharp candidate-pool threshold.

## PP3czs — Greedy packing from bounded overlap

Let `M` candidate source motifs be vertices of a conflict graph, where two motifs
are adjacent when they share a resource that prevents simultaneous use.  If this
graph has maximum degree `Delta`, it contains an independent set of size at least

```text
ceil(M/(Delta+1)).
```

This follows by repeatedly selecting one motif and deleting it with at most
`Delta` neighbours.

## PP3czt — Exact Hall threshold with extra corruption

Each selected four-centre motif supplies three good centres before extra
cross-copy corruption.  If `e` selected good centres are additionally corrupted,
the guaranteed count is

```text
3*ceil(M/(Delta+1)) - e.
```

The mixed-degree Hall interface therefore follows whenever this quantity is at
least 28.  Writing

```text
q = ceil((28+e)/3),
```

the sharp minimum candidate-pool size is

```text
(q-1)*(Delta+1) + 1.
```

For overlap degree two, the exact thresholds are 28 candidates for `e=0`, still
28 for `e=2`, and 31 for `e=3`.

## PP3czu — Sharpness and corruption-rate form

The candidate threshold is sharp at the graph level.  A disjoint union of
`q-1` cliques `K_(Delta+1)` has maximum degree `Delta`, contains
`(q-1)*(Delta+1)` motifs, and has independence number exactly `q-1`.

If extra corruption is bounded by `rho` per selected motif with `rho<3`, it is
enough to select

```text
ceil(28/(3-rho))
```

motifs and therefore enough to generate

```text
(ceil(28/(3-rho))-1)*(Delta+1)+1
```

candidates.

The checker is `scripts/check_hall_overlap_packing.py`.

## Evidence boundary

This theorem reduces geometric disjointness to a bounded overlap-degree target.
It does not prove that the conditional host generates such a motif graph, nor
does it prove the required source and host-defect degree-two restrictions after
selection.
