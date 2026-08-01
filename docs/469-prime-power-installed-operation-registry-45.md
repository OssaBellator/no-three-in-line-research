# The installed operation registry now contains forty-five kinds

This chapter records CMR3178--CMR3189.

Executable checker:

```text
scripts/check_prime_power_installed_operation_registry_45.py
```

## CMR3178 — sealed predecessor registry

The extension binds the exact thirty-nine-kind registry:

```text
aa7b4d1b0d7c1e7c76b8e22e547c132db5ee848c633cfc5cb45b41a76e522144
```

## CMR3179 — exact new contract

All boundary-fan and theta-payment entries bind:

```text
7089d93aa893b506e3e9d183d29869961c5e4fc59a25547d1a0c7e5607f084be
```

## CMR3180 — six unique operation identifiers

Exactly six kinds from CMR3177 are added. Duplicate, missing and substituted entries are rejected.

## CMR3181 — owner effects

All six operations remain within the current same-level owner. The full installed bank has 27 owner-changing and 18 same-owner kinds.

## CMR3182 — payment census

```text
owner-witness-stock: 3
scheduler-dispatch: 3
```

## CMR3183 — fan extraction dispatch

Boundary-fan extraction must continue to either a theta fan or the small-cut scheduler.

## CMR3184 — finite cut and bottleneck stocks

Small cuts and fixed two-edge bottlenecks are owner-labelled finite witnesses, not anonymous repeated states.

## CMR3185 — theta state dispatch

A theta-cycle flip enters the conflict scheduler. It is not itself counted as descent.

## CMR3186 — private-edge payment

Private theta edges receive owner-witness and full-token payment.

## CMR3187 — rooted-conflict dispatch

A boundary-rooted conflict must enter the rooted-star or pair-cylinder geometry scheduler.

## CMR3188 — exact census and corruption rejection

```text
base kinds: 39
new kinds: 6
installed kinds: 45
bound contracts: 15
owner-changing kinds: 27
same-owner kinds: 18
rejected corruptions: 9
```

Registry seal:

```text
2a5dfa1457e056259566eaf4e54034801f3a37ff57cd0548fbd0e117589b04b3
```

Contract digest:

```text
414d203835f3d1677bf20e7e1a0d02872653a56608e02b2fe7ab8d0aa49da4ae
```

## CMR3189 — honesty boundary

```text
installed_transition_kind_bank_45_exhaustive = 1
installed_payment_assignment_45_complete = 1
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Installed-bank exhaustiveness remains distinct from global construction exhaustiveness.
