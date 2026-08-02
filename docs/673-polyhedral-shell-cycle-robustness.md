# Polyhedral shell-cycle robustness

`docs/667` treats independent edge-burden intervals. Coordinate repairs may
instead create correlated burden uncertainty, so edgewise upper bounds can be
strictly pessimistic. This chapter gives the exact fixed-cycle criterion for a
polyhedral uncertainty set.

Let `U` be a compact polytope of edge-burden vectors and let `chi_C` be the edge
multiplicity vector of a reachable directed cycle `C`.

## PP3dcd — Support-function robust-cycle criterion

Cycle `C` has positive saving for every burden vector in `U` exactly when

```text
max_{b in U} <b,chi_C> < 3 |C|.
```

Because the objective is linear, the maximum is attained at a vertex of `U`.
Thus a fixed reachable robust-positive cycle exists exactly when one reachable
cycle passes this finite vertex test.

For an axis-aligned interval box, the support function reduces to the sum of
edgewise upper burdens, recovering `docs/667`.

## PP3dce — Fixed versus revealed-state adaptation

A fixed cycle chosen before the burden vector is known can be strictly weaker than
a cycle selected after the realized burden is revealed.

Consider two self-loop cycles and the uncertainty segment with vertices

```text
(b_1,b_2)=(1,4) and (4,1).
```

Each fixed cycle has worst-case saving `-1`, so no fixed robust-positive cycle
exists. Yet at every point of the segment, choosing the better revealed cycle
gives saving at least `1/2`; the minimum occurs at the midpoint `(5/2,5/2)`.

Therefore a theorem based on adaptive state observation must state that
information structure explicitly. The fixed-cycle criterion cannot be replaced by
“every realization has some positive cycle.”

## PP3dcf — Exact correlated setup repayment

Fix an entry path and a cycle. At uncertainty vertex `u`, let entry saving be
`A_u` and cycle gain be `G_u>0`. The least number of repetitions that beats setup
`S` for every admissible burden vector is

```text
max_u max(0, floor((S-A_u)/G_u)+1).
```

The formula is exact because each expression is affine in the uncertainty vector,
so it suffices to check vertices.

Correlation can materially improve the bound over combining separate worst-case
entry loss and cycle gain. In the certified example

```text
(A,G)=(-2,3) or (1,1),  S=7,
```

the exact repetition count is seven, while separate extrema give the conservative
bound ten.

## Verification

`scripts/check_shell_polyhedral_cycle_robustness.py` uses exact rational arithmetic
to verify the support-function reduction, the fixed/adaptive gap over the full
uncertainty segment, and the correlated setup-repayment formula.

## Evidence boundary

No coordinate macro transition graph currently supplies a certified polyhedral
burden set with a fixed reachable robust-positive cycle. The result is an exact
scheduling interface, not a geometric macro construction.
