# Finite full-grid response policies and side-six traps have executable ancestry

This chapter records **CMR3990--CMR4005** and binds source **CMR1278--CMR1317**.

Canonical checker:

```text
scripts/check_prime_power_finite_grid_response_ancestry.py
```

Contract:

```text
caa854d1cac17e5d4680558a9829b01a5d19b86a811e2baae47170d4839f3114
```

## CMR3990--CMR3993 — side three and side four

The checker executes the authoritative finite verifier modules. On the full standard side-three grid there are six physical saturated states, eight dirty labelled states and twenty-four target responses, all clean. The resulting four-class dirty offspring block is exactly zero.

On the full standard side-four grid there are 216 ordered states, 90 physical states and 176 dirty ordered states. The complete 10,368-response search gives a strict decrease for every dirty state.

## CMR3994--CMR3997 — side five and extension-free response families

The full side-five grid has 5,280 ordered states, 2,040 physical states and 5,216 dirty ordered states. The exact 2,400-entry target-response table selects a strict decrease for every dirty state.

The union over all forbidden extensions through one target cell equals the extension-free family of perfect matchings avoiding the opposite matching and that target cell. A canonical compatible extension is recovered after selecting a response. Ambient optimization and fixed-bank blockage remain distinct operations.

## CMR3998--CMR4002 — side-six trap classification

The full side-six grid has 190,800 ordered states and 67,950 physical states. Of the 190,684 dirty ordered states, 189,476 improve immediately. Exactly 1,208 are immediate one-layer traps; 1,120 escape after one equal response and 64 after two.

The remaining closed class has 24 ordered states representing twelve physical configurations. Its functional graph has six directed two-cycles and twelve one-step feeders. A recorded clean two-layer state gives an ambient strict escape from every closed trap.

## CMR4003--CMR4005 — coordinate and policy honesty

The numerical potential policies apply only to full standard grids and verified copies obtained by translation and one common nonzero scale. They do not transfer by arbitrary relabelling to scattered residual factors. The side-six trap class proves that repeated one-layer fixed-target banks are not globally sufficient.

```text
finite_grid_response_ancestry_proved = 1
side_three_full_grid_strict_improvement_exact = 1
side_four_full_grid_finite_improvement_exact = 1
side_five_full_grid_finite_improvement_exact = 1
extension_free_target_response_family_exact = 1
side_six_target_response_traps_exact = 1

scattered_residual_finite_grid_policy_proved = 0
one_layer_fixed_target_policy_globally_sufficient = 0
global_target_collateral_inequality_proved = 0
all_n_proved_by_checker = 0
```

The wrapper compiles and seals the expected censuses. Its complete side-five and side-six inherited enumeration has not been executed in the current local environment; an actual repository run is required before claiming that consolidated execution passed.
