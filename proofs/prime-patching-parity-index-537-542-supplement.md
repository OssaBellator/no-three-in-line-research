# Prime-patching parity index supplement: `docs/537--542`

This supplement continues the cumulative parity index after `docs/536`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cml--PP3cmn | Critical marker semigroups admit Apéry conductor tables, reduced-cost residue correction, and explicit two-generator action-rate meshes | PROVED | `docs/537-apery-certificates-for-marker-semigroups.md` |
| PP3cmo--PP3cmq | Automaton-constrained Hall transfers admit max-product envelopes, critical switching-cycle rates, and switch-aware reverse-load horizons | PROVED | `docs/538-automaton-constrained-switching-for-hall-transfers.md` |
| PP3cmr--PP3cmt | Zero-sum threshold macrocycles admit common prefix boxes, finite phase optimization, and arbitrary-concatenation all-window discrepancy certificates | PROVED | `docs/539-common-box-concatenation-of-threshold-cycles.md` |
| PP3cmu--PP3cmw | Regular prefix-tree profiles satisfy quasi-powers normality, a local Gaussian law, and exact finite moment/mode certificates | PROVED | `docs/540-gaussian-profiles-for-regular-prefix-trees.md` |
| PP3cmx--PP3cmz | Shell components admit exact shared startup buffers, reserve-pooling domination, and finite phase-torus optimization | PROVED | `docs/541-shared-reserve-pooling-for-shell-schedules.md` |
| PP3cna--PP3cnc | Normal interaction semigroups admit rational normal fans, quasipolynomial support values, and exact parametric optimizer formulas | PROVED | `docs/542-normal-fans-for-interaction-lattice-slices.md` |

## Frontier update

### Boundary recleaning

Mixed marker lengths now carry an explicit Apéry witness for every large side.
For critical lengths four and seven,

```text
Ap(S,4)=(0,21,14,7),
conductor=18.
```

The stored catalogue has exact cost `F(N)=N` for every `N>=18`, and adjacent
critical action-rate points have `N` times their `l_1` gap at most 56.

### Localized Hall transport

Switching constraints can now sharpen Hall mixing.  Two binary kernels with
contraction factors `1/2` and `3/4` are controlled by the automaton forbidding
`BB`.  Seven blocks have worst deviation `81/4096`; eight have `81/8192`, so
eight is the sharp one-percent horizon.  Degree 20 gives load `4177/163840`.

### Fractional direct-clean layers

Several zero-sum threshold cycles can now share one prefix box.  Across all 12
phase pairs of the stored two cycles, exactly three attain box width one.  Their
arbitrary concatenations have every prefix in one unit box and every interval
residual bounded by one.

### Support-chord repair words

The binary-node count `J_n` in a uniformly chosen legal prefix tree now has

```text
E J_n=n/3+O(1),
Var(J_n)=n/18+O(1),
```

and a local Gaussian law.  At 200 leaves the exact normalized mean and variance
are approximately `0.33041901` and `0.05569327`; the exact two-sigma mass is
approximately `0.94950416`.

### Clean-macro shells

Startup reserve can now be shared across shell components.  In the stored
period-three pair, each component separately needs `l_1` reserve one, while
three aligned phase pairs cancel slot by slot and need zero pooled reserve.

### Integration

Every rational downstream price vector now lies in a finite normal-fan cone.  On
the stored slice

```text
{(N-2b,2b):0<=b<=floor(N/2)},
```

the three cones `alpha<beta`, `alpha=beta`, and `alpha>beta` give exact optimizer
sets and parity-dependent support formulas for every `N`.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_537_542.py
```

or individually with

```bash
python scripts/check_apery_marker_certificates.py
python scripts/check_automaton_switched_hall_products.py
python scripts/check_threshold_cycle_concatenation.py
python scripts/check_regular_prefix_profile_clt.py
python scripts/check_shared_shell_reserves.py
python scripts/check_interaction_normal_fans.py
```

The local audits verify 500 marker lengths, every allowed Hall word through
length 20, all 12 threshold phase pairs with 350 repeated slots, every legal-tree
profile through 200 leaves, all nine shell phase pairs with 100 repeated periods,
and every interaction length through 300 against 120 integer weight pairs.

The next available theorem identifier is `PP3cnd`.
