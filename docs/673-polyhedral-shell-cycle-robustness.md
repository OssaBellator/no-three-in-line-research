# Polyhedral shell-cycle robustness

`docs/667` treats independent edge-burden intervals. Coordinate repairs may
instead create correlated burden uncertainty, so edgewise upper bounds can be
strictly pessimistic. This chapter gives exact primitive-cycle and mixed-cycle
criteria for a compact polyhedral uncertainty set.

Let `U` be a compact polytope of edge-burden vectors, let `chi_C` be the edge
multiplicity vector of a reachable directed cycle `C`, and define

```text
g_C(b) = 3|C| - <b,chi_C>.
```

## PP3dcd — Support-function fixed-cycle criterion

Cycle `C` has positive saving for every burden vector in `U` exactly when

```text
max_{b in U} <b,chi_C> < 3 |C|.
```

Because the objective is linear, the maximum is attained at a vertex of `U`.
Thus a fixed reachable robust-positive cycle exists exactly when one reachable
cycle passes this finite vertex test.

Equivalently, with support function `h_U`, the fixed-cycle robust margin is

```text
rho_fixed = max_C (3|C| - h_U(chi_C)).
```

For an axis-aligned interval box, the support function reduces to the sum of
edgewise upper burdens, recovering `docs/667`.

## PP3dce — Primitive, mixed, and composite cycle criteria

For a finite menu of primitive cycles, the revealed-state primitive margin is

```text
rho_primitive = min_{b in U} max_C g_C(b).
```

Since the maximum over primitive cycles equals the maximum over probability
weights `lambda` on that menu, the bilinear minimax theorem gives

```text
rho_primitive
 = max_{lambda in simplex}
   (3 sum_C lambda_C |C| - h_U(sum_C lambda_C chi_C)).
```

The mixed weights are a dual certificate. When the weighted primitive cycles can
be concatenated into one closed walk, rational weights also give a deterministic
fixed composite execution after clearing denominators.

For two self-loop cycles and the uncertainty segment with vertices

```text
(b_1,b_2)=(1,4) and (4,1),
```

each primitive loop has worst-case saving `-1`. Choosing the better revealed loop
has margin `1/2`, and equal mixed weights certify the same value. Because the loops
share a base state, concatenating one copy of each gives a fixed composite closed
walk with robust total gain one.

Thus the example separates primitive loops from composite execution; it does not
separate all fixed closed walks from adaptive observation. Any theorem using the
mixed certificate must state whether its cycle menu can be concatenated and what
connector costs are incurred.

## PP3dcf — Exact correlated setup repayment

Fix an entry path and a cycle or executable closed walk. At uncertainty vertex
`u`, let entry saving be `A_u` and repeated-walk gain be `G_u>0`. The least number
of repetitions that beats setup `S` for every admissible burden vector is

```text
max_u max(0, floor((S-A_u)/G_u)+1).
```

For each fixed repetition count `r`, the total saving `A(b)+rG(b)` is affine in
the burden vector, so its minimum over `U` is attained at a vertex. Taking the
least strict-improvement count at each vertex and then the maximum gives the exact
formula.

Correlation can materially improve the bound over combining separate worst-case
entry loss and cycle gain. In the certified example

```text
(A,G)=(-2,3) or (1,1),  S=7,
```

the exact repetition count is seven, while separate extrema give the conservative
bound ten.

## Verification

`scripts/check_shell_polyhedral_cycle_robustness.py` uses exact rational arithmetic
to verify the support-function reduction, the primitive/mixed minimax value, the
robust composite closed walk in the two-loop example, and the correlated
setup-repayment formula.

## Evidence boundary

No coordinate macro transition graph currently supplies a certified polyhedral
burden set together with an executable robust-positive composite walk. The result
is an exact scheduling interface, not a geometric macro construction.
