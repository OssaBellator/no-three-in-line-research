# Side-four compulsory-row obligation worklist

This post-ledger artifact compiles the complete normalized side-four host and selector manifests into one compulsory coefficient worklist. It does not introduce a theorem identifier after CMR4517 and does not claim that a recurrent weighted row is complete or strict.

```text
source manifest = data/prime_power_side_four_selected_response_provenance_manifest.json
source seal = 0eb284dd945b3022b529551c5d5f0407884f8ed1958de02b58e3cff024f5a4e6
contract = data/prime_power_side_four_compulsory_row_obligation_worklist.json
contract seal = 62c6c448b40a8b0294a35673aac997eac73c3380b1cceedffe9616c2326f3211
compiled rows seal = b33e4fa3e442349edacbb14a65b088a92b823c67b6a4f810958076a65e3e797b
checker = scripts/check_prime_power_side_four_compulsory_row_obligation_worklist.py
```

## Compiled normalized row context

Every one of the 86 selected-response records is expanded into a deterministic context containing:

```text
stable host identifier
normalized owner scope
zero-response or blocker-alternative fate
exact deletion/collision key
canonical selected response and full minimizer face
minimum response energy and next-energy gap
exact selected-response secant-line signature
side-four target-01 interface
prime-power label p=2, k=2
CRT-not-applied label
contained blocker identifiers
```

The exact selected-response secant geometry has six distinct line signatures. Their host multiplicities are:

```text
signature used by 2 hosts: 1
signature used by 9 hosts: 1
signature used by 13 hosts: 2
signature used by 15 hosts: 1
signature used by 34 hosts: 1
```

## Compulsory category surface

Each row contains exactly the six categories required by the compulsory weighted certificate schema:

```text
return
selector
collision
line
interface
geometric
```

The resulting census is:

```text
rows = 86
compulsory category slots = 516
known coefficients = 86
unresolved coefficients = 430
unresolved child keys = 516
unresolved positive child weights = 516
```

The geometric coefficient is the exact selected minimum response energy. It is zero on 75 zero-response rows and positive on the 11 blocker-alternative rows. No other coefficient is assigned a default value. In particular, unresolved return, selector, collision, line and interface terms are not silently set to zero.

## Honesty boundary

```text
side_four_compulsory_row_obligation_worklist_complete = 1
compiled_normalized_row_context_complete = 1

global_child_provenance_complete = 0
compulsory_coefficients_complete = 0
child_weights_complete = 0
complete_weighted_rows_strict = 0
all_n_proved_by_checker = 0
```

The contract and compiled-row seals, all 86 contexts, all 516 category slots, the coefficient census and twelve corruption cases were reproduced locally. The next task is to populate the 430 unresolved coefficients and bind every category occurrence to an exact child key and positive weight.