# Old-grid endpoint-shadow potential diagnostic

Run

```text
python scripts/check_old_grid_endpoint_shadow_potential.py \
  experiments/old-grid-endpoint-shadow-potential-example.json
```

The stored source is the union of two edge-disjoint permutation layers on a `5 x 5`
old grid.  Both the initial source and the pool-compatible replacement source are
saturated and no-three.

The complete old-grid potential is

```text
Xi_old(S)
=
sum_z (b_S^old(z)-2 1_(z notin S)).
```

The initial source has ten positive old-grid cells carrying total nonaxis multiplicity
sixteen.  Replacing three selected-layer source points by three new matching points
changes the potential from

```text
16 to 13.
```

The exact pair-weight terms are

```text
removal term 27,
insertion term 24,
```

so

```text
13-16=24-27=-3.
```

The expected output is

```text
grid side 5
initial source size 10
final source size 10
initial endpoint potential 16
final endpoint potential 13
positive old-grid cells 10
positive-cell multiplicity 16
removed source points 3
inserted source points 3
removal term 27
insertion term 24
exact potential change -3
identity insertion-minus-removal -3
outcome old_grid_endpoint_shadow_potential
```

This verifies the constant two-axis baseline, nonnegativity, and the exact trade
identity in PP3axy--PP3aya.  It also exhibits an actual pool-compatible repair with
strict endpoint-shadow decrease.
