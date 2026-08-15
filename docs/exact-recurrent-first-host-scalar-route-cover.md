# First-host scalar route-cover classification

**Branch:** `research/exact-recurrent-lyapunov-audit`

**Status:** exact symbolic classification on the chart-safe restoration cube. It does not prove that any restoration edge is physically legal, persistent under one owner identity, or equipped with a finite capacity.

## Context graph

Use the four restoration states

```text
00  blocked       selected 3012
01  restore 20    selected 3201
10  restore 02    selected 2031
11  restore both  selected 2031.
```

Every undirected edge of this two-bit square is present in both directions. A directed transition is called **scalar-paid** when

```text
potential(source) > potential(target).
```

The opposite direction must receive another closure route such as physical exclusion, finite capacity, terminal output, builder reset, or progress in a richer coordinate.

## Potentials depending only on the selected label

The selected-label graph is the complete bidirected triangle on

```text
3012, 2031, 3201.
```

There are six strict label orders. Every order pays exactly one direction from each unordered label pair and therefore pays exactly three of the six selector-changing gates.

Across all six orders, the three residual gates always contain

```text
2 gates flipping r02
1 gate flipping r20.
```

Choosing one external-route direction from each of the three bidirected label pairs gives eight formal three-edge covers. Exactly six are compatible with a scalar label order. The remaining two leave a directed three-cycle and cannot be paid by any label-only scalar.

Thus

```text
maximum selector gates paid by label scalar   3
minimum non-label-descent selector routes     3.
```

## Arbitrary potentials on the four menu states

The four menu states have 24 strict total orders but only 14 distinct edge orientations. This is the standard census of acyclic orientations of a four-cycle:

```text
all one-direction-per-edge choices   16
acyclic scalar-compatible choices    14
cyclic incompatible choices           2.
```

Every menu scalar pays exactly four of the eight directed menu edges. Its four residual routes contain exactly

```text
3 selector-changing edges
1 selector-neutral edge
2 edges flipping r02
2 edges flipping r20.
```

Therefore menu-state refinement does **not** increase the number of selector-changing gates paid: it remains three.

It does expand which triples can be paid. The 14 menu orientations project onto all eight tournaments on the three selected labels:

```text
12 menu orientations -> 6 transitive label tournaments, twice each
 2 menu orientations -> 2 directed label cycles, once each.
```

The two cyclic lifts are exact.

### Cyclic lift A

Low-to-high menu order:

```text
11 < 01 < 00 < 10
```

Paid menu edges:

```text
00->01
01->11
10->00
10->11
```

Their selector-changing projection is

```text
2031->3012->3201->2031.
```

### Cyclic lift B

Low-to-high menu order:

```text
10 < 00 < 01 < 11
```

Paid menu edges:

```text
00->10
01->00
11->01
11->10
```

Their selector-changing projection is the reverse directed cycle

```text
2031->3201->3012->2031.
```

These cycles become compatible with a scalar only because response `2031` is represented by two distinct menu states, `10` and `11`.

## Additive bit potentials are much narrower

For a potential of the form

```text
V(r02,r20)=alpha*r02+beta*r20
```

with nonzero coefficient signs, only four edge orientations occur—one for each sign pair `(sign alpha, sign beta)`.

All four project to transitive selected-label tournaments. They cover only four of the fourteen arbitrary menu-scalar orientations. The two cyclic lifts, and eight additional acyclic menu patterns, require interaction-sensitive state beyond an additive sum of the two restoration bits.

The restore-edge count among the fourteen arbitrary menu orientations has exact distribution

```text
paid restores 0: 1 orientation
paid restores 1: 4 orientations
paid restores 2: 4 orientations
paid restores 3: 4 orientations
paid restores 4: 1 orientation.
```

## Exact proof obligation

The scalar optimization is now complete:

```text
label-only scalar:
  paid selector gates       3
  external selector routes  3

arbitrary menu scalar:
  paid menu edges           4
  external menu routes      4
  selector-changing routes  3
  selector-neutral routes   1.
```

A physical proof may choose any scalar-compatible cover, but must source every residual route. No current artifact identifies the symbolic menu edges with persistent physical owner tokens, proves transition legality, assigns finite boundary capacities, or supplies recurrent child rows.

## Executable audit

Run

```bash
python scripts/check_exact_recurrent_first_host_scalar_route_cover.py \
  --check data/exact_recurrent_first_host_scalar_route_cover.json
```

The checker enumerates all label and menu orders, all one-direction-per-pair route choices, both cyclic lifts, all four additive bit potentials, the restore-count distribution, and rejects fifteen deliberate corruptions.

Physical chart confinement, occurrence coverage, transition legality, owner identity, capacities, child rows, strict Lyapunov slack, global termination, and `all_n_proved_by_checker` remain zero.
