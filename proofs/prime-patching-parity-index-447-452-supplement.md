# Prime-patching parity index supplement: `docs/447--452`

This supplement continues the cumulative parity index after `docs/446`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3ccb--PP3ccd | Shared stopping words form an acyclic marker automaton with an exact path-sum load dynamic program; excess load localizes to one bad transition or lost state tag | PROVED | `docs/447-acyclic-marker-automata.md` |
| PP3cce--PP3ccg | A proper coloring of the residual Hall graph makes every color-tagged target private; exact and compressed color recovery give loads `1/d` and `g/d` | PROVED | `docs/448-color-coded-hall-petal-banks.md` |
| PP3cch--PP3ccj | Randomized threshold optima admit sparse rational bases, exact primal--dual basis certificates, and a finite exact basis-enumeration oracle | PROVED | `docs/449-finite-basis-certificates-for-threshold-kernels.md` |
| PP3cck--PP3ccm | Unequal symbol survivals admit sorted fixed-tree assignments and a correct `O(3^K)` subset dynamic program over binary prefix trees | PROVED | `docs/450-subset-dynamic-programming-for-unequal-symbol-codes.md` |
| PP3ccn--PP3ccp | A unique shell critical cycle has an exact cross-power stability cone, exact one-edge margins, and a piecewise-constant logarithmic gradient | PROVED | `docs/451-critical-cycle-stability-cones.md` |
| PP3ccq--PP3ccs | Condensation resolvents have exact mixed finite differences, a complete finite multilinear expansion, and a rigorous pair-price bound on higher-order error | PROVED | `docs/452-higher-order-sensitivity-for-condensation-resolvents.md` |

## Frontier update

### Boundary recleaning

Stopping words may now share arbitrary acyclic marker states. With root loads
`lambda_r` and local edge factors `q_e`, the state certificate is

```text
B(v)=sum_(P:r->v) lambda_r product_(e in P)q_e.
```

It is evaluated by one topological pass. Recoverable terminal labels combine by
a maximum. Any excess terminal load exposes a local factor violation, a lost
state marker, or a terminal collision.

### Localized Hall transport

A proper edge coloring of the complete residual Hall graph makes every tagged
target `(y,c)` private. Uniform choice among at least `d` residual actions gives

```text
lambda<=1/d.
```

If colors are compressed into code fibers of size at most `g`, the bound becomes
`g/d`. This uses every residual action rather than selecting one matching bank.

### Fractional direct-clean layers

The randomized threshold LP now has a finite exact basis format. Some optimum
uses at most `|X|+|Y|-1` threshold variables. A support, an active-column set,
the rational basis solution, and target prices form a complete certificate.
The stored audit recovers the mixed optimum `3/5` from four exact bases, versus
deterministic optimum `5/6`.

### Support-chord repair words

Unequal symbol survivals require a subset recurrence rather than a contiguous
interval split. For bank set `S`,

```text
V(S)=min_(A proper subset S)
 min(max(V(A)/p_0,V(S\A)/p_1),
     max(V(A)/p_1,V(S\A)/p_0)).
```

This gives an exact `O(3^K)` dynamic program. The six-bank audit agrees with all
30,240 tree assignments and has optimum `5/18`.

### Clean-macro shells

The unique critical cycle now comes with its complete multiplicative stability
region. Every competitor `C` imposes the exact cross-power inequality

```text
(P_* Gamma_*)^(ell_C)>=(P_C Gamma_C)^(ell_*).
```

Within the strict region, only critical-cycle edges affect the local rate and
their logarithmic derivatives are their cycle multiplicities divided by
`ell_*`. The stored graph has exact one-edge walls `5/6` and `6/5`.

### Integration

Several condensation-block perturbations now admit an exact finite interaction
expansion. For compatible bridges `e=(u,v)` and `f=(s,t)`,

```text
Delta_e Delta_f K=F_u H_e T_(v,s) H_f G_t.
```

All higher compatible chains appear once in the multilinear path expansion. An
all-upper pair-price sum rigorously bounds the error left after retaining only
first-order sensitivities.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_447_452.py
```

or individually with

```bash
python scripts/check_acyclic_marker_automata.py
python scripts/check_color_coded_hall_banks.py
python scripts/check_threshold_lp_basis_certificates.py
python scripts/check_unequal_symbol_code_dp.py
python scripts/check_critical_cycle_stability_cones.py
python scripts/check_higher_order_condensation_sensitivities.py
```

The local audits verify 512 automaton subgraphs, 3,375 residual Hall graphs and
21,600 colored edges, four exact optimal threshold bases, all 30,240 assignments
on 42 ordered six-leaf trees, five shell cycles with exact stability walls, and
a complete three-atom condensation expansion including its quadratic remainder
envelope.

The next available theorem identifier is `PP3cct`.
