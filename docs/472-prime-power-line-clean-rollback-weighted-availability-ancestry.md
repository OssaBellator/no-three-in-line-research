# Line-clean cylinders have exact rollback availability and weighted selection

This chapter records CMR3218--CMR3233 and installs CMR497--CMR506 as literal construction ancestry.

Executable checker:

```text
scripts/check_prime_power_line_clean_rollback_weighted_availability.py
```

## CMR3218 — literal residual line-clean universe

After deleting one paid pair, the checker represents the residual complete host with the paid-line perfect matching removed. Its feasible states are the exact residual derangements.

## CMR3219 — canonical minimum restoration

For every residual subhost, all line-clean derangements are generated and the lexicographically first state with minimum unavailable-edge count is selected.

## CMR3220 — exact restoration footprint

The selected unavailable edges are restored literally. Their count equals the minimum line-clean restoration number.

## CMR3221 — restored edges are essential

Every perfect matching of the restored available host is regenerated and checked to contain the entire minimum restoration footprint.

## CMR3222 — forced-core product

Removing the restored matching edges and their endpoints gives a residual factor whose perfect-matching count agrees exactly with the restored host family.

## CMR3223 — cheap or strict factor branch

At threshold two, minimum cost below two is recorded as cheap restoration; cost at least two produces strict side descent by the forced restoration core.

## CMR3224 — exact token incidence

With sample `p=2,h=3`, every restored edge contributes exactly six labelled nonroot full-token incidences.

## CMR3225 — recreated-conflict support

Every compatible rank-two candidate present after restoration but absent before it is checked to contain a restored edge.

## CMR3226 — derangement marginal

For every physical side-seven paid pair, every allowed residual edge occurs in exactly a `1/(n-1)` fraction of the line-clean cylinder states.

## CMR3227 — weighted selector

For each unavailable-edge pattern, the checker minimizes the integer-weighted score `q X + r`, where `X` is the physical collinear-triple count and `r` the restoration count. The selected state is checked against the exact average.

## CMR3228 — cheap-clean endpoint

Whenever the weighted average is below one in normalized units, the selected state has zero created triples and restores fewer than `q` unavailable edges.

## CMR3229 — failure polarization

Every failed cheap-clean profile enters either the frozen-collateral branch or the unavailable-edge depletion branch.

## CMR3230 — concentration and dispersion

Unavailable inventories are double-counted across cylinders. The literal family exercises edge concentration, and a separate explicit family exercises the dispersed distinct-edge endpoint.

## CMR3231 — exhaustive finite census

```text
64 residual subhosts
48 cheap restoration profiles
16 forced-factor profiles
66 restored-edge incidences
396 sample full-token incidences
132 restored-supported candidate incidences
3,528 physical side-seven paid-pair profiles
17,640 derangement marginal checks
198 cheap-clean selections
3,330 weighted failure profiles
3,328 frozen-collateral branches
2 unavailable-depletion branches
298 literal unavailable incidences on 10 distinct edges
12 explicit dispersed unavailable edges
```

## CMR3232 — corruption rejection

Eight independently resealed mutations are rejected, including substituted contracts, false theorem flags, missing endpoint coverage, incorrect subhost census, an all-`n` flag and a broken record seal.

Contract digest:

```text
c56a0c82ee03ed6498ac5c974e64c8129344a921a262e3d13cb28672df39ab2e
```

## CMR3233 — T02 consequence and honesty boundary

Installed kinds:

```text
line-clean-minimum-restoration
line-clean-forced-core-contraction
line-clean-cheap-restoration
line-clean-weighted-selection
line-clean-unavailable-edge-concentration
line-clean-unavailable-inventory-payment
```

Exact flags:

```text
line_clean_rollback_availability_proved = 1
line_clean_weighted_selection_proved = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Adaptive unavailable-edge absorption, token splicing and temporal return scheduling remain open.
