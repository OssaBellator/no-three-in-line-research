# Alternating-core cumulative integrated source/certificate bank

This note records AC5cx--AC5db. It extends the one-epoch split-certificate network of AC5cs--AC5cw to repeated restricted-menu epochs without preissuing certificate capacity or reusing spent physical source mass.

## Contract

Fix finite physical source classes `S`, certificate classes `C` and layer-defect classes `D`. The complete retained state includes both compatibility relations `S -> C` and `C -> D`, current nonnegative integral source balances `p_t(s)`, current nonnegative integral certificate balances `q_t(c)`, exact named deposits before each epoch and exact defect demands `d_t(x)`. Every paid unit must follow one retained path `s -> c -> x` and debit one unit from both current balances. Relabelling, omitted compatibility, hidden deposits or source-less creation is outside the contract.

## Theorem block

### AC5cx — exact balance recurrence

Before epoch `t`, add the named deposits to `p_t` and `q_t`. After selecting an integral flow, subtract the actual source-edge and certificate-throughput usage. Every balance remains an exact nonnegative integer.

### AC5cy — simultaneous epoch criterion

Split every certificate class into an input and output vertex with capacity `q_t(c)`, give every source vertex capacity `p_t(s)`, and route to the defect demands. The epoch is fully paid exactly when the maximum flow equals `sum_x d_t(x)`.

### AC5cz — cumulative debit identity

Across every fully paid prefix, cumulative source use is at most initial source balance plus named source deposits, and cumulative certificate use is at most initial certificate balance plus named certificate deposits. No unit is debited twice.

### AC5da — first mixed cut

If the first unpaid epoch has maximum flow `F_t < sum_x d_t(x)`, a canonical minimum cut retains its exact source classes, certificate classes, defect classes and unpaid mass `sum_x d_t(x)-F_t`. This is the returned physical obstruction.

### AC5db — reset boundary

Changing either compatibility layer, changing a retained address, hidden replenishment, fractional issuance, splitting one source occurrence, or paying a defect outside a retained path returns reset or amplification rather than payment.

## Finite audit

Run:

`python scripts/verify_ac_cumulative_integrated_source_certificate_bank.py`

The deterministic audit checks 5,000 systems and 6,454 epochs, with 17,626 source classes, 17,578 certificate classes, 17,446 defect classes, 30,946 source/certificate arcs, 30,621 certificate/defect arcs, 43,468 demand units, 27,731 paid units, 15,737 unpaid units and 257 cases where greedy sequential issuance fails although the simultaneous network succeeds.

## Scope

This theorem does not construct the physical source/certificate/defect graph or prove its capacities and deposits. It does not prove AC5, AC6 or the no-three-in-line conjecture.