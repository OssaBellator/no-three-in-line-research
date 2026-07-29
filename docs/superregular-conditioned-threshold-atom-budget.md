# Superregular conditioned threshold atom budget

This note records SRR2cf--SRR2cj. It composes exact remote conditioning, threshold retention and perturbation-stable witness-atom budgets.

## Contract

Fix one endpoint-cost threshold. Candidate weights and costs, the conditioned retained candidate set, the complete conflict graph and one exact witness atom for every conflict edge are retained. Reference atom burdens, burden removals/additions and capacity deposits/losses are recorded coordinatewise.

## Theorem block SRR2cf--SRR2cj

### SRR2cf — conditioned burden identity

For every atom,
`B_actual = B_reference - B_removed + B_added`,
where edge burden is the sum of its two endpoint weights.

### SRR2cg — actual capacity identity

For every atom,
`C_actual = C_reference + C_deposit - C_loss`.

### SRR2ch — paid threshold execution

If `B_actual(a) <= C_actual(a)` for every atom and retained candidate weight is `W`, then a compatible low-cost subfamily has weight at least
`W^2 / (W + sum_a C_actual(a))`.

### SRR2ci — exact overloaded atom

If the paid condition fails, the least exact atom with positive `B_actual-C_actual` is retained as the conditioning/geometry obstruction.

### SRR2cj — reset boundary

Omitted candidates, unrecorded conflict edges, changed witness atoms or nonlocal conditioning return reset.

## Proof

The coordinatewise identities partition weighted conflict degree. The weighted independent-set bound gives `W^2/(W+B_actual)`, which is at least the displayed bound when all atom burdens are paid.

## Finite audit

Run `python scripts/verify_srr_conditioned_threshold_atom_budget.py`.

## Scope

The theorem does not construct the geometric candidate family or prove its concrete atom capacities. It does not prove SRR2, SRR4 or the no-three-in-line conjecture.
