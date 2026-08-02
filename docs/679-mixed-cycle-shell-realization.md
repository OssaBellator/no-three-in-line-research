# Mixed-cycle shell realization

The mixed-cycle minimax certificate in `docs/673` is initially a convex weight
vector on primitive cycles. This chapter shows when that certificate becomes a
deterministic fixed closed walk and quantifies connector repayment when the cycles
have different base states.

## PP3dcv — Rational mixed weights give a fixed composite walk

Let primitive cycles `C_1,...,C_t` share a common base state. Suppose rational
weights `lambda_i` sum to one and have robust mixed margin

```text
rho = min_{b in U} sum_i lambda_i g_{C_i}(b) > 0.
```

Choose a common denominator `L` and integers `n_i=L lambda_i`. Concatenate `n_i`
copies of each primitive cycle. The resulting fixed closed walk has robust gain

```text
min_{b in U} sum_i n_i g_{C_i}(b) = L rho > 0.
```

Thus rational mixed certificates at a common base require no burden observation
and no randomization; clearing denominators gives a deterministic executable
supercycle.

## PP3dcw — Connector losses are finitely amortizable

Now let the primitive cycles have different base states in one strongly connected
macro graph. Fix a connector tour that visits the required bases and returns to its
start. Let its worst-case saving be `A_connector`, and let the cleared cycle bundle
have robust gain `G_bundle>0`.

Repeating the cycle bundle `r` times before paying the connector tour and setup `S`
gives guaranteed saving

```text
A_connector + r G_bundle - S.
```

The least strict-improvement repetition count is exactly

```text
max(0, floor((S-A_connector)/G_bundle)+1).
```

Hence every positive rational mixed certificate becomes a fixed finite-memory
schedule whenever finite connector paths are certified. Connector loss changes only
the transient repetition count, not the positive asymptotic mean.

## PP3dcx — Exact two-loop realization

For the uncertainty vertices

```text
(1,4) and (4,1),
```

the two primitive self-loops each have robust gain `-1`. Equal mixed weights have
margin `1/2`. Clearing the denominator gives one copy of each loop, whose fixed
composite walk has robust total gain one.

If the loops instead lie at different states and the connector tour has saving
`-1`, one bundle only ties, while two bundles give strict gain one. With setup five,
exactly seven bundles are required.

A second three-cycle example with equal weights has mixed margin `2/3`; one copy of
each cycle gives a fixed composite robust gain two.

## Verification

`scripts/check_shell_mixed_cycle_realization.py` uses exact rational arithmetic to
clear mixed weights, verify the robust gains of the resulting composite incidence
vectors, and check the connector/setup repetition formula.

## Evidence boundary

This is an execution theorem for a certified macro graph, not a construction of
that graph. The no-three-in-line program still lacks coordinate macro cycles,
connector paths, and a burden polytope whose mixed certificate is positive.
