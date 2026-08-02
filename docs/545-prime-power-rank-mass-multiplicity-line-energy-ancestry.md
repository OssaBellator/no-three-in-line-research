# Installed rank-mass, multiplicity and line-energy ancestry

```text
checker = scripts/check_prime_power_rank_mass_multiplicity_line_energy_ancestry.py
contract = 681a56e37003368e62a92ae7df349488e03e03eec34c2cddf2ab39b8d6622bdd
source = CMR1702--CMR1773
```

## Theorem CMR4326 -- PROVED

The checker binds exactly docs 316--324 and their nine verifier entrypoints.

## Theorem CMR4327 -- PROVED

For every response law, total rank-`r` prescription probability mass is exactly `C(d,r)`. Forced prescriptions subtract one full unit each from the remaining stochastic mass.

## Theorem CMR4328 -- PROVED

Pointwise probability caps and conserved rank mass combine by a rankwise minimum. With a common response denominator this gives exact integer numerator capacities.

## Theorem CMR4329 -- PROVED

If one rank-`r` prescription supports at most `m_r` genuinely new credits, expected off-line collateral is at most `sum m_r(C(d,r)-F_r)` after forced contractions.

## Theorem CMR4330 -- CONDITIONAL STRICT CLOSURE

For an actual nonempty line-clean host, destruction above the multiplicity-corrected nonforced rank mass forces a strict-improvement response. This is conditional on the stated multiplicity caps and complete child accounting.

## Theorem CMR4331 -- PROVED

If possible canonical owners lie in edge support `A`, owned rank-`r` mass is at most `mu(A)C(d-1,r-1)`, where `mu(A)` is its matching number. A source-target cover size may replace `mu(A)`.

## Theorem CMR4332 -- CONDITIONAL STRICT CLOSURE

Destruction above the owner-support multiplicity capacity forces a strict response when every retained recurrent child owner lies in `A` and the response host is nonempty.

## Theorem CMR4333 -- PROVED

Prime-field reused supports of size one or two inherit the corresponding owner-support thresholds; two edges sharing a source or target have matching number one.

## Theorem CMR4334 -- PROVED

Rank-three geometric multiplicity is at most one. Rank-two multiplicity is the background load of the determined line. Rank-one multiplicity is the exact secant sum `sum C(h,2)` through the response point.

## Theorem CMR4335 -- PROVED

The exact maximum secant sum with background size `N` and line-height cap `H` is `floor(N/H)C(H,2)+C(N mod H,2)`. This yields explicit packed line-clean and owner-support thresholds.

## Theorem CMR4336 -- PROVED

Rank-one high multiplicity charges to pair-only secants and current labelled background triples with congestion at most three. Rank two leaves two low slots and charges the remainder with congestion one.

## Theorem CMR4337 -- PROVED

Pair-only secants through one response point form a matching on the background and number at most `floor(|B|/2)`. Local triple shadows are bounded by the current background triple potential.

## Theorem CMR4338 -- PROVED

The resulting potential-only multiplicity caps are

```text
m1 <= floor(|B|/2) + 3 Psi(B)
m2 <= 2 + Psi(B)
m3 = 1
```

and combine with packed-height caps rankwise.

## Theorem CMR4339 -- PROVED

For line profile `(h_l,k_l)`, the exact new uncorrected triple count is

```text
sum_l [k_l C(h_l,2) + C(k_l,2)h_l + C(k_l,3)]
```

and every corrected genuinely new row is bounded by this census.

## Theorem CMR4340 -- PROVED

Response pairs total exactly `C(d,2)` and response triples total `Psi(Q)`. Triple-free responses satisfy the explicit coefficient-seven background-triple bound, conditional on such a response being selected.

## Theorem CMR4341 -- HONEST ENDPOINT

The checker contract and sixteen fixture mutations preserve:

```text
all_line_clean_large_load_rows_closed = 0
all_owner_support_rows_closed = 0
geometric_multiplicity_caps_globally_sufficient = 0
triple_free_response_policy_globally_available = 0
line_energy_profile_rows_subcritical = 0
same_owner_diagonal_blocks_subcritical = 0
global_target_collateral_inequality_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

The complete nine-verifier execution was not observed locally.
