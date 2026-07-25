# All-n product track: finite-obstruction stage

**Branch:** `research/all-n-product-construction`

This stage continues
[`all-n-product-packet-trajectory-sign-stage.md`](all-n-product-packet-trajectory-sign-stage.md).
PX315--PX340 remove the growing trajectory census, the independent linear packet
residue, the external first-order sign ambiguity, and the linear internal
rank-three estimate above the square-root ambient threshold.  The surviving
terminal problem is finite for fixed base degree.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Historical-union cycle | **BOUNDED RESET CANDIDATE** | PX315 releases at most `s` ancestor levels to expose a principal cycle; its full causal cost remains subject to exact terminal evaluation. |
| Acyclic historical union | **CONSTANT CORE** | PX316--PX318 force `s<=Delta_0+1` and a finite exact template census. |
| Linear packet residue | **REDUCED** | PX319--PX323 give an exact `c_e-w_e+1` blocker budget for every positive correction edge. |
| External support-one/two debt | **CLOSED UNDER INTERNAL GAP** | PX324--PX329 give a finite causal child forest whenever `d_sigma>c_3`. |
| Internal rank-three support four | **CONSTANT-SCALE** | PX330--PX332 replace the coarse `O(t^4)` count by `3(t)_3/2`. |
| Internal rank-three support five/six | **SUBLINEAR** | PX333 hybrid thinning gives `o(s)` expected load uniformly above the ambient threshold. |
| Large-block strict sign | **AVAILABLE** | PX334--PX335 choose a matching with `c_3<s<=d_sigma`, then discharge all external blockers. |
| Terminal no-improvement family | **FINITE POLYHEDRAL** | PX336--PX340 reduce it to finitely many rational extreme rays for fixed `Delta_0`. |
| Geometric extreme-ray realizability | **OPEN** | Determine which finite rays can arise from actual grid line incidences. |
| Extreme-ray absorption | **OPEN** | Construct a nonprincipal/coupled absorber or rule out each realizable ray. |
| Composite-release causal cost | **OPEN** | A historical-union cycle is executable, but released ancestor recurrence must be paid in the exact terminal potential. |
| PX63 conversion | **OPEN** | Insert the finite-obstruction alternative into the product induction. |
| Infinite exact closure | **OPEN** | No all-side product closure follows yet. |

## 1. Large-block sign hierarchy

For a retained switch block of order `s`:

1. support-one and support-two creation are external blockers;
2. support-three creation is internal rank three;
3. hybrid thinning gives

   \[
   c_3<s;
   \]

4. every clean-star, radial, coordinate-field, or loaded-line switch destroys at
   least `s` old certificates;
5. therefore `d_sigma>c_3`, and the external blocker countdown is finite.

The former generic first-order constant problem is no longer present above the
square-root ambient threshold.

## 2. Terminal hierarchy

A trajectory terminal core now has the following alternatives.

1. Allowed principal cycle: PX287.
2. Historical back edge: PX294.
3. Single historical-layer cycle: PX311.
4. Composite historical-union cycle: PX315.
5. Acyclic historical union: constant child `s<=Delta_0+1` by PX316.
6. Constant child: exact move matrix and no-improvement cone by PX336--PX340.

Thus a failure of the present repair interface has a constant-size rational
certificate rather than a growing recursive template.

## Immediate frontier

1. **Extreme-ray census.** Instantiate PX339 for the actual base degree and list
   the geometrically feasible rays.
2. **Geometric feasibility.** Add determinant, line-uniqueness, and packet
   identities as equations cutting down the abstract cone.
3. **Absorber search.** Test nonprincipal two-block moves against every feasible
   ray and extract symbolic inequalities.
4. **Causal composite release.** Charge ancestor recurrence for PX315 cycles in
   the exact move matrix.
5. **Closure conversion.** State the PX63 induction with a finite terminal
   obstruction alternative, then eliminate that alternative.

## Verification

```bash
python scripts/verify_product_composite_history_cycle.py
python scripts/verify_product_packet_blocker_budget.py
python scripts/verify_product_universal_blocker_forest.py
python scripts/verify_product_rank_three_support_four.py
python scripts/verify_product_terminal_obstruction_cone.py
```

All five verifiers pass locally.  Exact infinite product closure and the
classical no-three-in-line conjecture remain open.
