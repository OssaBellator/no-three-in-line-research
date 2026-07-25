# Rank-four partner Hall-star diagnostic

This check accompanies
`docs/180-fixed-centre-rank-four-partner-hall-star.md`.

Run:

```bash
python scripts/check_rank_four_partner_hall_star.py \
  experiments/rank-four-partner-hall-star-example.json
```

The stored host is `K_(8,8)`. The positive rank-four partner support is the full
star from remote tail resource `0` to all eight remote head resources. Deleting
that support isolates one left vertex, so the residual host has maximum matching
size seven.

The checker extracts the Hall witness

```text
X={0},
N_H(X)=empty,
Y=all eight right resources,
```

and verifies that the complete Hall rectangle `X x Y` lies in the partner
support. The maximum support degree is eight. For

```text
epsilon=1/4,
delta=3/4,
```

PP3aci requires degree at least

```text
epsilon(delta-epsilon)q = 1.
```

The example therefore realizes the linear partner-resource-star branch.

Removing the last support edge leaves one residual edge at the formerly isolated
tail and exercises the support-avoiding perfect-matching branch. A cyclic
two-regular support also leaves a perfect matching and illustrates that a large
remote matching or diffuse support is not by itself a matchability obstruction.

The diagnostic checks the finite Hall and lower-regularity bookkeeping. It does
not verify the residual source or paid first moments in PP3ack.
