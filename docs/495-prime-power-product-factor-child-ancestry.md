# Product rectangles, factor recursion and child routing have literal construction ancestry

This chapter records **CMR3538--CMR3561** and installs source theorems CMR629--CMR690 as one executable construction bank.

Canonical checker:

```text
scripts/check_prime_power_product_factor_child_ancestry.py
```

Contract:

```text
0ce977177196fbffe8c8ffc446346dde64347999b299307f96ca74d4586e4e12
```

## CMR3538 — exact product conflict decomposition

Every protected/free product state is regenerated from literal factor matchings. Candidate conflicts split exactly into pure protected, pure free and mixed classes.

## CMR3539 — mixed-atom rectangle ancestry

Every mixed atom is represented by its absolute parent-grid edges. Its occurrence family is checked to be the exact Cartesian rectangle determined by its protected and free prescriptions.

## CMR3540 — dirty-product concentration

The finite product fixture has nonempty pure-clean factor families. The mixed rectangles cover every dirty pure-clean product state and satisfy the CMR632 averaging inequality.

## CMR3541 — protected prescription deletion

Rank-one and rank-two protected prescriptions are processed in the literal protected host. A lexicographically selected nonessential edge is deleted and the child matching family is regenerated.

## CMR3542 — essential-core concentration and private restoration

Surviving prescriptions lie in the final essential matching core. Deleted prescriptions receive distinct selected edges, and every recreation subset is charged to its selected restoration code.

## CMR3543 — exact essential contraction

All 247 matchable side-three bipartite hosts are enumerated. Contracting the complete essential core gives exactly the projected residual matching family.

## CMR3544 — residual essential-core elimination

Every nonempty residual host obtained from complete-core contraction is checked to have empty essential core.

## CMR3545 — transferred trigger ranks

All CMR638 rank-one/rank-two transfer patterns are enumerated. No contraction creates a transferred prescription of rank greater than two.

## CMR3546 — free-factor deletion budget

Transferred one-edge and two-edge prescriptions are processed in all matchable side-three hosts. Every selected free edge is nonessential and its deletion preserves a perfect matching.

## CMR3547 — alternating deletion/contraction stock

The exact factor-side and edge-stock inequalities underlying CMR641 are checked for the finite parameter bank.

## CMR3548 — essentiality-loss entering support

Across all pairs of matchable side-three hosts, every omitted old essential edge is checked to require a genuinely new matching edge.

## CMR3549 — alternating-component witness

Every alternating component containing an omitted essential edge contains an entering edge of the later matching. Affected components inject into entering-edge witnesses.

## CMR3550 — forced-certificate witness stock

The finite three-type deletion/skeleton/entering-edge witness universe and recurrence bound are checked over sample sides and thresholds.

## CMR3551 — pure-factor normalization

For every matchable side-three host, the checker repeatedly contracts the complete essential core, verifies that the residual core is empty, and records the accumulated forced matching.

## CMR3552 — anchored deletion recursion

Every core-anchored residual prescription has rank one or two. One residual edge is deleted while preserving matchability, after which the complete core is recomputed.

## CMR3553 — pure-factor monotone budgets

Per-host contractions are bounded by the initial side, selected anchored deletions are distinct, and the stage bound `d+d^2+1` is enforced.

## CMR3554 — factor-prefix envelope and transport

Side-two, side-three and sampled side-four factors inside a side-eight parent receive their canonical prefix depth. Every matching transport table has exact margins and child-cell capacity.

## CMR3555 — routing skeleton product factorization

Every realised routing skeleton is regenerated from absolute vertex-routing sets. The number of states with that skeleton equals the product of the exact child-factor matching counts.

## CMR3556 — heavy/dispersed child alternative

Every transport table satisfies the square-root heavy-child or dispersed-child-cell alternative.

## CMR3557 — multi-child atom boxes

Cross-child atoms in the literal two-child fixture have only `(2,1)` or `(1,1,1)` rank patterns. Their occurrence sets equal the exact Cartesian child boxes.

## CMR3558 — routing-change edge support

All routing-changing pairs of complete side-four factor matchings are checked. Every change has at least two entering and two leaving support edges, all lying on changed alternating components.

## CMR3559 — mixed-child finite deletion

All 49 matchable pairs of side-two child hosts are processed. Active nonforced mixed atoms lose a nonessential child edge; deletions never activate a new atom.

## CMR3560 — forced-child terminality and strict recursion

The terminal product is either mixed-clean or contains an all-essential forced atom. The clean branch has exact pure-factor additivity; every recursive child continuation has smaller factor side and deeper prefix envelope.

## CMR3561 — finite ancestry consequence and honesty boundary

Observed finite census includes:

```text
247 matchable side-three hosts
64,128 essentiality-loss escape instances
64,128 affected alternating components
4,320 factor-prefix profiles
29,984 transport-table checks
21,076 routing-product factorisations
264 routing-changing matching pairs
49 mixed-child host pairs
7 mixed-child deletion steps
9 forced-child endpoints
40 mixed-clean endpoints
10 rejected contract corruptions
```

Exact flags:

```text
product_conflict_rectangle_ancestry_proved = 1
essential_prescription_transfer_exact = 1
forced_product_certificate_escape_exact = 1
pure_factor_essential_recursion_exact = 1
factor_prefix_routing_exact = 1
multi_child_conflict_rectangles_exact = 1
routing_change_edge_support_exact = 1
mixed_child_deletion_recursion_exact = 1
forced_child_certificate_ancestry_exact = 1
product_factor_child_ancestry_proved = 1

global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The checker installs literal finite ancestry for CMR629--CMR690 only. It does not prove that all original construction operations are registered or that every branch terminates.
