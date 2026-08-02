# Hall conflict-graph packing interface

This chapter refines the numerical bad-centre amplification law from
`docs/646-bad-centre-amplification.md`. It isolates the exact combinatorial
quantity that cross-copy geometry must control.

## PP3czs — Conflict-graph reduction

Assume `t` resource-disjoint four-centre source motifs have been constructed.
Each motif supplies three intrinsically good centres, so there are `3t` candidate
good centres before cross-copy interference.

Let `H` be the graph whose vertices are those `3t` centres and whose edges join
pairs that cannot both be retained because of a certified cross-copy conflict.
A set of simultaneously retainable centres is exactly an independent set of
`H`. Therefore the maximum retainable pool is

```text
alpha(H) = 3t - tau(H),
```

where `tau(H)` is the minimum vertex-cover number. The 28-resource Hall interface
is met exactly when

```text
3t - tau(H) >= 28.
```

This replaces the undifferentiated extra-corruption count by an exact conflict
packing invariant.

## PP3czt — Bipartite matching certificate

If the certified cross-copy conflict graph is bipartite, König's theorem gives

```text
tau(H) = nu(H),
```

where `nu(H)` is the maximum matching number. Hence the Hall condition becomes

```text
3t - nu(H) >= 28.
```

For a matching of `e` independent corruption edges, `nu(H)=e`, recovering the
earlier `3t-e` law exactly. For an arbitrary graph with `E` edges,
`tau(H) <= E`, so `3t-E >= 28` remains a sufficient but potentially non-sharp
certificate.

## PP3czu — Exact motif count under a matching bound

Under a proved bipartite conflict model with `nu(H) <= m`, the least motif count
certified by this interface is

```text
ceil((28+m)/3).
```

In particular:

- ten motifs tolerate matching number at most two;
- a third independent cross-copy conflict forces eleven motifs;
- eleven motifs tolerate matching number at most five;
- a sixth forces twelve motifs.

The checker exhaustively verifies `alpha+tau=n` on all 32,768 simple graphs on
six labelled vertices and verifies `tau=nu` on all 5,177 bipartite members.

## Evidence boundary

This is an exact conditional packing theorem. The repository still lacks a
geometric construction of resource-disjoint motifs, a proof that all cross-copy
failures are represented by the chosen graph, and the source/host-defect
degree-two restrictions required by the mixed-degree Hall interface.
