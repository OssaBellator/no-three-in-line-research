# One-helper bridge and local-cost atomization diagnostic

Run

```text
python scripts/check_one_helper_bridge_atomization.py \
  experiments/one-helper-bridge-atomization-example.json
```

The exact path-atom counts are

```text
path length 1 A2 atoms 1 B3 atoms 0 B4 atoms 0 total 1
path length 2 A2 atoms 2 B3 atoms 1 B4 atoms 0 total 3
path length 3 A2 atoms 3 B3 atoms 2 B4 atoms 1 total 6
path length 4 A2 atoms 4 B3 atoms 3 B4 atoms 3 total 10
```

The stored rank-four partner petal fixes the bridge path

```text
0->1->4->2->3
```

inside a six-index cycle.  Its exact output continues as

```text
bridge cycle size 6
bridge fixed path arcs 4
bridge conditional cycles 1
bridge formula count 1
bridge local atoms 10
removal credit 100
credit per ten atoms 10.000000
heavy bridge helpers 40
exact fixed-role subfamily 40
theorem fixed-role lower bound 2
heavy role B3_bridge_middle
heavy atom weight 12
outcome one_helper_bridge_credit_scale_pencil
```

The conditional cycle count is `(6-5)!=1`.  Every stored helper has local cost at
least the credit because the same bridge-middle `B_3` atom has weight `12`, above
the atomization threshold `100/10=10`.

There are at most two bridge orientations and ten local atom positions, so the
general pigeonhole bound retains at least `ceil(40/20)=2` helpers.  The stored
uniform family retains all 40 and realizes the credit-scale fixed-centre path
pencil branch of PP3aov.
