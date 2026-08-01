# Rooted secant stars and compatible paid pairs have exact line-clean cylinders

This chapter records CMR3202--CMR3217 and installs CMR487--CMR496 as literal construction ancestry.

Executable checker:

```text
scripts/check_prime_power_rooted_star_compatible_pair_line_clean.py
```

## CMR3202 — literal clean base matching

The checker exhausts every collinearity-clean permutation matching on the physical side-five grid. Candidate boundary cells are generated outside the base state.

## CMR3203 — exact rooted-star family

For a boundary cell `a`, every candidate-only triple contained in the base matching plus `a` is generated. Distinct rooted arms are verified to have disjoint outside matching pairs.

## CMR3204 — secant-star bound

The outside-pair disjointness gives at most `floor(m/2)` rooted arms at one centre. The finite census verifies the bound for every generated centre.

## CMR3205 — exact cycle-arm survival

For every mixed contraction cycle containing the boundary arc, the cycle-flip state is generated. A rooted arm survives exactly when neither outside matching index lies on the cycle.

## CMR3206 — compatible rooted paid pair

Either boundary cell together with either outside endpoint of a rooted arm is checked to use distinct source rows and distinct target columns.

## CMR3207 — residual paid-line partial matching

After deleting the paid-pair rows and columns, every remaining cell on their joining line is generated and verified to be a partial matching.

## CMR3208 — exact derangement cylinder

The paid-line partial matching is extended canonically to one residual perfect matching. Residual perfect matchings avoiding that extension form the line-clean cylinder and are counted exactly by the derangement number `D_(m-2)`.

## CMR3209 — complete paid-line avoidance

Every cylinder state contains the paid pair and omits every other cell of its joining line.

## CMR3210 — rank-two collateral elimination

No cylinder state contains a candidate-only triple using both paid cells, because every possible third point lies on the omitted paid line.

## CMR3211 — rooted-arm destruction

For every rooted arm, the selected paid pair is retained while the arm's other outside endpoint and every other rooted-line cell are omitted.

## CMR3212 — equal-weight rooted bank

Every rooted arm receives exactly `D_(m-2)` line-clean states, giving an equal-weight multiset bank.

## CMR3213 — two-edge bottleneck compatibility

Every pair of distinct contraction arcs on one simple directed cycle is verified to have distinct sources and targets and hence forms a compatible paid pair.

## CMR3214 — bottleneck-pair cylinder

Every generated cycle-derived bottleneck pair receives the same exact line-clean derangement cylinder.

## CMR3215 — exhaustive physical census

```text
side = 5
56 clean base matchings
328 rooted-star centres
328 rooted arms
5,248 exact cycle-arm survival checks
328 rooted-arm cylinders
656 rooted-arm cylinder states
200 universal compatible-pair cylinders
400 universal cylinder state occurrences
156 residual paid-line cell incidences
130 cycle-derived bottleneck pairs
260 bottleneck-pair cylinder states
```

## CMR3216 — corruption rejection

Eight independently resealed mutations are rejected, including false theorem flags, removed rooted or cylinder coverage, a substituted contract, an all-`n` flag and a broken record seal.

Contract digest:

```text
4492a6220f6b7622373a872b1521478089d5dd319482c8110b8cfe1e4ae9495d
```

## CMR3217 — T02 consequence and honesty boundary

Installed kinds:

```text
boundary-rooted-secant-star-extraction
rooted-cycle-arm-survival
rooted-arm-line-clean-cylinder
rooted-arm-equal-weight-bank
two-edge-bottleneck-pair-cylinder
compatible-pair-line-clean-cylinder
```

Exact flags:

```text
rooted_star_pair_cylinder_ancestry_proved = 1
universal_pair_line_clean_cylinder_exact = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Availability of these full-parent cylinders inside restricted hosts is handled separately. No all-`n` theorem is claimed.
