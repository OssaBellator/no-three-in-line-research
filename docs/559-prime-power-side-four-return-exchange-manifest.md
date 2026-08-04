# Side-four return-exchange manifest

This post-ledger artifact enumerates every ordered old/new response transition inside the complete normalized side-four host catalogue. It grounds the returned-edge exchange state required by CMR1574--CMR1581 without claiming that recreated physical credits or return-kernel coefficients are already known.

```text
raw lineage manifest seal = 84ad1c92a9e0bcfb4d1f613e05edec20c4300022d96269ed561b45d32bf7432f
selected-response manifest seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
contract = data/prime_power_side_four_return_exchange_manifest_contract.json
contract seal = b6f768bae19061ffe35e1b0b437a402e4d49c7ce4ac8fa5bc5ea005518c565f9
compiled transition records seal = 1151a0d65b228612217b484e97256d36a1a809d95338f18a28b2eb58ab2a3274
checker = scripts/check_prime_power_side_four_return_exchange_manifest.py
```

## Exact transition universe

For each normalized host, the checker takes every ordered pair of distinct allowed perfect-matching responses. It retains both directions because the returned and entering edge sets reverse when the transition reverses.

```text
hosts = 86
response occurrences = 206
ordered distinct response transitions = 378
returned-edge state occurrences = 998
```

Every transition record contains:

```text
host identifier
old and new response permutations
old and new response-triple energies
all returned edges paired with same-source entering edges
all old edges paired with same-target entering edges
alternating-cycle lengths
churn size
canonical-selector source and destination flags
complete-minimizer-face source and destination flags
```

The recreated-credit class and exact return-kernel entries remain explicitly null.

## Exchange bijections and cycle signatures

For every changed source row, the old selected edge is paired with the new selected edge from that same source. For every changed target column, the old and new selected edges are paired at that target. The two pairings have equal cardinality.

The old/new symmetric difference is a disjoint union of even alternating cycles. The exact finite census is:

```text
churn 2 = 200 transitions
churn 3 = 114 transitions
churn 4 = 64 transitions

one 4-cycle = 200 transitions
one 6-cycle = 114 transitions
two 4-cycles = 32 transitions
one 8-cycle = 32 transitions
```

Thus every returned edge now carries an exact entering partner and one finite cycle-length label.

## Response-energy transitions

```text
0 -> 0 = 164
0 -> 1 = 41
0 -> 4 = 46
1 -> 0 = 41
1 -> 4 = 20
4 -> 0 = 46
4 -> 1 = 20
```

There are no self-transitions and no ordered transitions between distinct responses of equal positive energy in this finite catalogue.

## Selector and minimizer-face incidence

```text
canonical-selector source transitions = 120
canonical-selector destination transitions = 120
minimizer-face source transitions = 260
minimizer-face destination transitions = 260
transitions entirely inside a minimizer face = 164
```

The complete minimizer face remains visible; the canonical selector is not substituted for all tied responses.

## Return-kernel boundary

The manifest supplies the exact finite exchange signature required before a return coefficient can be computed:

```text
old matching
new matching
returned edge
same-source entering edge
same-target entering edge
alternating-cycle length
response energies
selector/minimizer labels
```

It does not yet supply:

```text
physical recreated-credit classes
absolute entering-owner order
credit-class provenance
exact K_{f,b} return-kernel entries
coarse class maxima
return child keys
positive child weights
```

Total churn is therefore not used as a return coefficient.

## Honesty boundary

```text
side_four_return_exchange_manifest_complete = 1
return_exchange_state_complete = 1

recreated_credit_classes_complete = 0
return_kernel_entries_complete = 0
return_coefficients_complete = 0
global_child_provenance_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract and compiled-record seals, all 378 transitions, all 998 returned-edge states, the exchange/cycle/energy censuses and twelve corruption cases were reproduced locally. The next step is to attach physical recreated-credit provenance and enumerate the exact classwise kernel entries.
