# First-host route-cover admission theorem

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact Boolean classification of source-closed directed-edge sets. It does not prove that any symbolic menu edge is physically legal or closed by one of the five accepted route classes.

## Route-closed edges

A directed menu edge is called **route-closed** only when the closure-route source gate admits at least one exact route for that edge:

```text
physical exclusion
terminal or improving output
bounded strict potential
finite unrestorable capacity
decorated outer reset.
```

Merely having a symbolic gate address, a local restoration candidate, or an alternating-core acceptance rule does not make an edge route-closed.

The current source gate has

```text
route-closed directed edges   0
complete label covers         0
complete menu covers          0.
```

## Pair-coverage criterion

Every scalar residual cover chooses one direction from each relevant reversal pair.

For the selected-label problem there are three bidirected label pairs. For the full menu problem there are four bidirected square edges.

A route-closed set contains a scalar-compatible residual cover exactly when:

1. at least one direction is route-closed in every reversal pair; and
2. the uniquely chosen directions are not one of the two directed cycles.

Equivalently, after pair coverage is established, the only obstruction is an exact directed cycle. If at least one reversal pair is route-closed in both directions, one can choose the direction on that pair to break any cycle, so a scalar cover necessarily exists.

## Complete label-mask census

There are six selector-changing directed edges and therefore 64 possible route-closed masks.

```text
masks covering all three label pairs   27
masks containing a label cover          25
pair-covered directed-cycle failures     2
all infeasible masks                     39
```

The feasible masks by number of route-closed edges are

```text
3 edges:  6
4 edges: 12
5 edges:  6
6 edges:  1.
```

The six size-three masks are exactly the six minimum label-scalar residual covers.

The two cycle obstructions are

```text
00->01, 01->11, 10->00
00->10, 01->00, 11->01.
```

## Complete menu-mask census

There are eight directed menu edges and therefore 256 route-closed masks.

```text
masks covering all four square pairs   81
masks containing a menu cover           79
pair-covered directed-cycle failures     2
all infeasible masks                    177
```

The feasible masks by size are

```text
4 edges: 14
5 edges: 32
6 edges: 24
7 edges:  8
8 edges:  1.
```

The fourteen size-four masks are exactly the fourteen scalar-compatible menu residual covers.

The two cycle obstructions are

```text
00->01, 01->11, 11->10, 10->00
00->10, 10->11, 11->01, 01->00.
```

## Useful sufficient patterns

The four restore directions form one additive menu cover:

```text
00->01
00->10
01->11
10->11.
```

The four delete directions form the opposite additive cover:

```text
01->00
10->00
11->01
11->10.
```

Closing all six selector-changing directions always contains a label cover. Closing all six changing directions plus either one of the two selector-neutral directions always contains a menu cover.

Closing only one bit family cannot contain a menu cover because two reversal pairs remain uncovered.

## Physical ingestion consequence

A future source batch need not choose a scalar order first. It may instead populate route evidence edge by edge. The admission checker then asks whether the resulting route-closed set contains one of the exact covers.

The source must still provide the route-specific evidence demanded by the closure-route gate. Pair coverage alone is combinatorial; it is not evidence of physical exclusion, descent, capacity or reset.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_route_cover_admission.py \
  --check data/exact_recurrent_first_host_route_cover_admission.json
```

The checker enumerates all 64 label masks and all 256 menu masks, reconstructs the six and fourteen minimal covers, proves the two-cycle criterion, verifies the sufficient patterns, joins the current zero-admission source gate, and rejects fifteen deliberate corruptions.

Physical transition legality, owner identity, capacities, outer profiles, child rows, strict Lyapunov slack, global termination and `all_n_proved_by_checker` remain zero.
