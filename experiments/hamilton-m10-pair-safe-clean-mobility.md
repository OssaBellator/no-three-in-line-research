# Exact pair-safe frustration repair and clean mobility at `m=10`

The checker `scripts/check_hamilton_m10_pair_safe_clean_mobility.cpp`
reconstructs all `9!=362,880` directed Hamilton cycles on ten pair vertices,
all pair-parity predicates, all `2^10` orientation vectors on each pair-safe
cycle, and all `120` successor rotations per cycle.

## Frustration census

```text
Hamilton cycles             362,880
pair-safe cycles            342,720
parity-satisfiable cycles   297,886
clean orientation vectors 115,586,396
```

The exact frustration-index distribution on pair-safe cycles is

```text
lambda=0 : 297,886
lambda=1 :  42,190
lambda=2 :   2,582
lambda=3 :      62
```

The clean parity graphs have cyclomatic-rank distribution

```text
rank 0 : 296,298
rank 1 :   1,588
```

## One-rotation repair

Every one of the `44,834` pair-safe inconsistent cycles has a pair-safe
successor rotation directly to a parity-satisfiable cycle:

```text
1 -> 0 : 42,190 cycles
2 -> 0 :  2,582 cycles
3 -> 0 :     62 cycles
```

Thus the pair-safe distance to the clean set is zero or one.

## Marked frustration-core targeting

Every edge violated by every orientation attaining the minimum frustration
index was tested.  Across

```text
13,185,264 optimal violated-edge instances
```

each instance has a direct clean successor rotation whose source triple meets
an endpoint of the selected edge.  The exact minima are

```text
clean rotations from one positive-frustration cycle: 11
targeted clean rotations for one optimal violated edge: 6
untargetable optimal violated edges: 0
```

## Clean induced graph

```text
clean induced components                         1
minimum clean degree                            69
maximum clean degree                           120
minimum clean rotations meeting every owner set 40
```

The favorable clean connectivity and owner-intersecting targetability therefore
survive the first appearance of consistent rank-one parity cycles.

## Reproduction

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_m10_pair_safe_clean_mobility.cpp \
  -o /tmp/check_hamilton_m10_pair_safe_clean_mobility
/tmp/check_hamilton_m10_pair_safe_clean_mobility
```

The output must match
`experiments/hamilton-m10-pair-safe-clean-mobility-audit.json`.
