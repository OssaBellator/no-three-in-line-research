# Joint local-constraint fusion diagnostic

Run

```text
python scripts/check_joint_local_constraint_fusion.py \
  experiments/joint-local-constraint-fusion-example.json
```

The stored model has `W=10`, `N=100`, and five local constraint families: source,
transition/anchor, distinguished endpoint, endpoint arc, and insertion.  Every
support has rank at most three, and the first ten helpers avoid all families
simultaneously.

The dense failure model partitions the 100 helpers into nine cliques and assigns
the clique-edge supports cyclically to three local constraint types.  Its
independence number is at most nine.  The union contains 506 rank-two supports,
compared with the critical threshold 55.  Finite type refinement leaves the source
family with 176 edges.

The exact output is

```text
W 10
N 100
joint maximum support rank 3
chosen helper count 10
selected local constraints 0
dense fused clique parts 9
dense fused rank-two edges 506
rank-two density threshold 55.0
concentrated constraint type source
concentrated type edges 176
outcome joint_local_constraints_independent_or_concentrated
```

This verifies PP3asf--PP3asi: one independent block satisfies every encoded local
constraint, while failure of the fused table concentrates in one original
constraint family at target scale.
