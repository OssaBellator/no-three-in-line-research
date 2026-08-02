# Local resource-incidence Hall packing

The Hall frontiers in `docs/652` and `docs/658` use motif-overlap degrees and a
second-stage centre-conflict matching bound. This chapter gives a host-auditable
way to derive the first-stage degrees directly from local coordinate resources.

## PP3dbc — Exact degree from local resource incidence

Let each candidate motif `v` use a finite resource set `R(v)`. Two motifs conflict
at the first packing stage exactly when their resource sets intersect. For each
resource `r`, let

```text
mu_r = |{v : r in R(v)}|.
```

Define the raw local load

```text
L_v = sum_{r in R(v)} (mu_r-1).
```

This counts every conflicting neighbour once for each shared resource. Therefore
the exact overlap degree is

```text
d_v = L_v - sum_{u != v} max(|R(u) intersect R(v)|-1,0).
```

The correction term removes duplicate counts caused by motif pairs sharing more
than one resource. In particular `d_v<=L_v`, with equality whenever every pair of
motifs shares at most one resource.

## PP3dbd — Incidence-only Caro--Wei certificate

Caro--Wei gives a resource-disjoint motif family of size at least

```text
ceil(sum_v 1/(d_v+1)).
```

Since `d_v<=L_v`, the purely local certificate

```text
q = ceil(sum_v 1/(L_v+1))
```

is always valid. It requires only each motif's resource list and the multiplicity
of each resource; the full conflict graph need not be materialized.

If every motif uses at most `s` resources and every resource occurs in at most
`lambda` motifs, then `L_v<=s(lambda-1)` and hence

```text
q >= ceil(M/(s(lambda-1)+1)).
```

The individual-load sum can be strictly stronger than this uniform corollary when
most motifs or resources are light.

## PP3dbe — Two-stage promotion interface

After selecting `q` resource-disjoint motifs, the three-good-centres law supplies
`3q` candidate centres. If the certified second-stage centre-conflict graph is
bipartite with maximum matching number at most `m`, at least

```text
3q-m
```

centres remain. Thus the 28-resource interface follows from the directly
auditable condition

```text
3*ceil(sum_v 1/(L_v+1)) - m >= 28.
```

The required selected motif counts remain ten for `m=0` or `m=2`, eleven for
`m=3` or `m=5`, and twelve for `m=6`.

## Verification

`scripts/check_hall_local_resource_incidence.py` exhausts all 54,263 multisets of
at most six nonempty motif types on four resources. For every family it computes
the exact independence number, verifies the duplicate-corrected degree identity,
and checks

```text
alpha >= ceil(sum_v 1/(d_v+1)) >= ceil(sum_v 1/(L_v+1)).
```

## Evidence boundary

This is a stronger coordinate-audit interface, not a geometric construction. The
conditional host must still provide actual motif resource sets, prove the separate
source and host-defect degree-two restrictions, and certify that the second-stage
graph covers every cross-copy centre conflict.
