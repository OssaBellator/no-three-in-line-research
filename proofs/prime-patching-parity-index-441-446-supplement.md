# Prime-patching parity index supplement: `docs/441--446`

This supplement continues the cumulative parity index after `docs/440`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cbj--PP3cbl | Abstract stopping codes can be realized by composable local symbol kernels; prefix-free recovery prevents class summation and failed retention localizes to one bad symbol prefix | PROVED | `docs/441-realizable-stopping-symbol-chains.md` |
| PP3cbm--PP3cbo | The full residual Hall incidence graph after core conditioning edge-colors into private-marker banks; intrinsic color recovery removes every bank-count loss | PROVED | `docs/442-edge-colored-private-petal-banks.md` |
| PP3cbp--PP3cbr | Randomized threshold kernels have an exact complementary-slackness gap decomposition, with suboptimality localized to priced target slack or reduced-cost threshold mass | PROVED | `docs/443-complementary-slackness-for-threshold-kernels.md` |
| PP3cbs--PP3cbu | Unequal symbol survivals reduce to sorted bank-to-leaf assignment and a finite search over ordered full prefix trees | PROVED | `docs/444-unequal-symbol-prefix-tree-optimization.md` |
| PP3cbv--PP3cbx | The exact shell rate is certified by a critical simple cycle, rational cross-power comparisons, an algebraic critical polynomial, and a rational uniqueness reserve | PROVED | `docs/445-exact-critical-cycles-for-shell-rates.md` |
| PP3cby--PP3cca | Condensation resolvents admit exact forward--backward sensitivities for every bridge and local SCC block, plus a simultaneous all-upper perturbation envelope | PROVED | `docs/446-forward-backward-sensitivity-for-condensation-resolvents.md` |

## Frontier update

### Boundary recleaning

Prefix-coded stopping levels now have an implementation theorem.  If stopping
class `i` has base load `lambda_i` and writes symbols with local load factors
`r_s`, then its realized chain has load

```text
lambda_i product_(s in w_i) r_s.
```

Prefix-free terminal tags make the combined load the maximum class load.  If a
promised word-retention product fails, one concrete symbol-prefix transition
violates its local retention estimate.

### Localized Hall transport

After deleting a common target core, let `Delta_R` be the maximum residual
source or target degree.  The entire residual graph decomposes into
`Delta_R` matchings, not merely one extracted matching.  Thus all common-core
plus private-marker actions split into private-petal banks, and one bank contains
at least

```text
ceil(E_R/Delta_R)
```

residual actions.  Intrinsic bank-color recovery gives a combined kernel load
`h/q` independent of the number of colors.

### Fractional direct-clean layers

The randomized threshold LP now has a pointwise audit identity:

```text
lambda-Phi(z)
 =sum_y z_y(lambda-L_y)
  +sum_(x,h) alpha_(x,h)[c_(x,h)(z)-m_x(z)].
```

Optimality is therefore equivalent to saturation of every positively priced
target and use only of price-minimizing thresholds.  Any gap returns either
priced column slack or positive reduced-cost threshold mass.

### Support-chord repair words

Schedule symbols may have unequal retention probabilities.  For a fixed prefix
tree, heavier banks optimally occupy higher-survival leaves.  With `K` banks it
suffices to enumerate ordered full binary trees with `K` leaves and depth at
most `K-1`.  The stored asymmetric audit has exact optimum `2/3` with words

```text
00, 01, 11, 100, 101.
```

### Clean-macro shells

The rational rate oracle is complemented by an exact algebraic endpoint.  A
critical cycle `C_*` is selected without radicals by cross-power comparisons;
the optimal rate is the positive root of

```text
x^(ell_*)-P_*=0.
```

The stored graph has unique critical cycle `(0,1)`, exact rate `sqrt(3/5)`, and
a rational edgewise robustness factor `1001/1000`.

### Integration

Forward and backward condensation prices

```text
F_i=U_iR_i,
G_i=R_iV_i
```

give exact finite differences

```text
Delta K=F_u H G_v
```

for one bridge perturbation and

```text
Delta K=U_i H V_i
```

for one local SCC-resolvent perturbation.  All-upper prices bound simultaneous
nonnegative uncertainty and identify which local bounds dominate the final core
correction.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_441_446.py
```

or individually with

```bash
python scripts/check_realizable_stopping_symbol_chains.py
python scripts/check_hall_core_petal_edge_coloring.py
python scripts/check_threshold_lp_complementary_slackness.py
python scripts/check_unequal_symbol_prefix_trees.py
python scripts/check_exact_critical_shell_cycles.py
python scripts/check_condensation_resolvent_sensitivities.py
```

The local audits verify all fifteen stopping-class unions, 1,331 residual Hall
rectangles and 10,164 colored edges, exact primal--dual gap decompositions,
1,680 asymmetric prefix-tree assignments, all five simple shell cycles with an
exact algebraic winner, and eleven exact condensation sensitivity identities
plus a simultaneous perturbation envelope.

The next available theorem identifier is `PP3ccb`.
