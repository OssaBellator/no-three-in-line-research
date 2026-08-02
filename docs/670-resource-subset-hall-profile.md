# Resource-subset Hall profile

The local-load certificate in `docs/664` uses each motif's load in the full
candidate family. This chapter adds a complementary certificate that follows how
those loads fall under iterative deletion.

## PP3dbu — Resource degeneracy from induced motif families

Let `V` be a finite family of candidate motifs with resource sets `R(v)`. For a
nonempty subfamily `U subseteq V`, define

```text
mu_r(U) = |{v in U : r in R(v)}|,
L_v(U) = sum_{r in R(v)} (mu_r(U)-1).
```

The degree of `v` in the resource-overlap graph induced by `U` is at most
`L_v(U)`. Define the resource degeneracy

```text
kappa_R = max_{empty != U subseteq V} min_{v in U} L_v(U).
```

Every induced overlap graph therefore has a vertex of degree at most `kappa_R`,
so the full overlap graph is `kappa_R`-degenerate.

The value `kappa_R` is obtained directly by repeatedly deleting a motif of minimum
current local load and taking the maximum deleted load. This requires only the
resource lists and their changing multiplicities; no pairwise conflict graph is
needed.

## PP3dbv — Peeling and Caro--Wei are complementary

A `kappa_R`-degenerate graph is `(kappa_R+1)`-colourable. Hence there is a
resource-disjoint motif family of size at least

```text
q_peel = ceil(M/(kappa_R+1)).
```

The full-family incidence Caro--Wei certificate from `docs/664` is

```text
q_CW = ceil(sum_v 1/(L_v(V)+1)).
```

Neither bound dominates the other. Therefore the directly host-auditable combined
certificate is

```text
q_profile = max(q_CW,q_peel).
```

The exhaustive four-resource audit over all 54,263 multisets of at most six
nonempty motif types gives

```text
q_peel > q_CW : 1,884 families,
q_CW > q_peel : 6,142 families,
q_peel = q_CW : 46,237 families.
```

Thus the induced-subfamily profile supplies genuine information not present in the
initial-load sum, while the two certificates must be retained together.

## PP3dbw — Two-stage Hall promotion criterion

After selecting `q_profile` resource-disjoint motifs, the three-good-centres law
supplies `3*q_profile` candidate centres. If the selected-centre conflict graph is
bipartite with matching number at most `m`, at least

```text
3*q_profile-m
```

centres remain. The 28-resource interface follows from

```text
3*max(
  ceil(sum_v 1/(L_v(V)+1)),
  ceil(M/(kappa_R+1))
)-m >= 28.
```

This criterion is computable directly from a coordinate-derived motif list plus a
separate certificate for the selected-centre conflicts.

## Verification

`scripts/check_hall_resource_subset_profile.py` exhausts the same 54,263 motif
families as the local-incidence audit. It verifies the exact independence number
against both bounds, records the strict-improvement counts above, and includes
explicit examples showing that each certificate can beat the other.

## Evidence boundary

This remains a promotion interface. No asymptotic coordinate host has yet supplied
the motif resource lists, selected-centre conflict graph, or the simultaneous
source- and host-defect degree-two restrictions required by the geometric Hall
step.
