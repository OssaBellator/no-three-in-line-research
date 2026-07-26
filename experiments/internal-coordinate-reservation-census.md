# Internal coordinate-reservation census diagnostic

Run

```text
python scripts/check_internal_coordinate_reservation_census.py \
  experiments/internal-coordinate-reservation-census-example.json
```

The stored finite scale treats a full quarter of the old coordinates as reserved by
slab pools:

```text
slab density = 0.25.
```

It then adds `10^12` further package reservations and a target marked set of size
`2*10^9`.  The remaining coordinate set still has density approximately `0.75` and
size

```text
74,999,998,998,000,000,000.
```

With helper constant two, the complete quadratic demand is

```text
8,000,000,000,000,000,000,
```

only about `10.67%` of the remaining reservoir and below the stored `2R` bound.

The exact output is

```text
m 100000000000000000000
M 5
R 5000000000000000000
W 2000000000
slab reserved 25000000000000000000
slab reserved density 0.25
small reserved 1000000000000
marked size 2000000000
total reserved 25000001002000000000
available coordinates 74999998998000000000
available density 0.74999998998
quadratic helper demand 8000000000000000000
helper demand to available ratio 0.10666666809173335
outcome internal_reservation_leaves_automatic_helper_reservoir
```

This verifies PP3auj--PP3aul in a finite model with a genuinely macroscopic slab
reservation.  A fixed-density reservation bounded away from one cannot obstruct the
sublinear quadratic helper demand.
