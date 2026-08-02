# Resource-multiplicity Hall packing

The Hall interfaces in `docs/652` and `docs/658` use the motif-overlap graph.
This chapter replaces an externally supplied graph degree sequence by a quantity
computed directly from motif-resource incidence data.

Let motif `i` use the finite resource set `R_i`. For each resource `r`, let

```text
mu_r = number of candidate motifs containing r.
```

Define the local overlap load

```text
L_i = sum_{r in R_i} (mu_r-1).
```

## PP3dbc — Incidence-derived degree certificate

Let `d_i` be the degree of motif `i` in the resource-overlap graph. Then

```text
d_i <= L_i.
```

### Proof

Every neighbour of motif `i` shares at least one resource with it. For a fixed
resource `r in R_i`, at most `mu_r-1` other motifs share that resource. Summing
over `R_i` counts every neighbour at least once and may count a neighbour more
than once, proving the inequality. ∎

This certificate is directly auditable from coordinates once each motif's
resource list is known; no separate overlap-graph construction is required.

## PP3dbd — Local Caro--Wei packing bound

The candidate family contains a resource-disjoint subfamily of size at least

```text
ceil(sum_i 1/(L_i+1)).
```

### Proof

Caro--Wei gives an independent set of size at least
`sum_i 1/(d_i+1)`. Since `d_i<=L_i`, each summand is at least
`1/(L_i+1)`. Resource-disjoint motif families are exactly independent sets in the
overlap graph. ∎

If every motif uses at most `s` resources and every resource occurs in at most
`rho` motifs, then `L_i<=s(rho-1)` and therefore

```text
q >= ceil(M/(s(rho-1)+1)).
```

The local bound is sharp: groups of motifs sharing one private resource produce
a disjoint union of cliques, and equality holds group by group.

## PP3dbe — Two-stage Hall condition from incidence loads

After selecting

```text
q = ceil(sum_i 1/(L_i+1))
```

resource-disjoint motifs, there are `3q` intrinsically good centres. If the
certified selected-centre conflict graph is bipartite with matching number at
most `m`, at least `3q-m` centres remain. Hence the 28-resource interface follows
whenever

```text
3*ceil(sum_i 1/(L_i+1)) - m >= 28.
```

The selected motif requirement remains ten for `m=0,1,2`, eleven for
`m=3,4,5`, and twelve for `m=6`.

`scripts/check_hall_resource_multiplicity_packing.py` exhausts all 16,383
families of at most seven distinct nonempty motif types on four labelled
resources, compares the certificate with the exact independence number, checks
the uniform corollary, and verifies sharp clique examples.

## Evidence boundary

The theorem converts coordinate-level incidence multiplicities into a rigorous
packing guarantee. The repository still lacks an explicit asymptotic host family
whose motif resource lists, centre-conflict matching bound, source degree-two
condition, and host-defect degree-two condition are all certified together.
