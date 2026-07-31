# Prime-patching parity index supplement: `docs/543--548`

This supplement continues the cumulative parity index after `docs/542`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3cnd--PP3cnf | Six rational frontier rows admit a common period/denominator normal form, strict additive slack composition, and an exact 24-period, 480-denominator fixture | PROVED | `docs/543-six-frontier-rational-compatibility-ledger.md` |
| PP3cng--PP3cni | Lengths four and seven admit modulo-three phase locking through a translated semigroup, exact locked conductors, and a uniform threshold 74 | PROVED | `docs/544-phase-locked-marker-semigroup-synchronization.md` |
| PP3cnj--PP3cnl | Optional frontier refinements admit minimum-cost slack purchase, a dual threshold certificate, and a unique exact six-row optimum | PROVED | `docs/545-optimal-purchase-of-global-slack.md` |
| PP3cnm--PP3cno | Hall switching, threshold phases, and shell phases admit a synchronous product reduction and a shortest seven-step mixed return cycle | PROVED | `docs/546-product-automaton-for-cross-frontier-synchronization.md` |
| PP3cnp--PP3cnr | Rational frontier proportions admit balanced all-length rounding, strict-slack transfer, and an exact period-120 integerization certificate | PROVED | `docs/547-all-length-balanced-integerization.md` |
| PP3cns--PP3cnu | Typed frontier certificates compose, the stored abstract model closes every length from 361 onward, and geometric closure reduces to six explicit realization statements | PROVED / CONDITIONAL APPLICATION | `docs/548-conditional-end-to-end-compatibility-closure.md` |

## Compatibility update

### Common ledger

The six frontier losses scale to

```text
(28,27,20,15,12,10)/480,
```

with total `112/480=7/30`, global margin `120/480=1/4`, and base slack `1/60`.
All state data factor through period 24.  The stored perturbation budget is
`1/240`, leaving robust slack `1/80`.

### Boundary and phase synchronization

Requiring the number of seven-block markers to lie in one prescribed residue
modulo three replaces `<4,7>` by a translate of `<4,21>`.  Its Apéry table is

```text
(0,21,42,63),
```

with conductor 60.  The three exact phase thresholds are 60, 67, and 74, so an
arbitrary modulo-three phase selector is feasible for every length at least 74.

### Slack optimization

Reducing aggregate loss from `7/30` to `1/5` requires `1/30` improvement.  In the
stored price table the unique optimum saturates Hall by `1/40` and purchases
`1/120` from boundary, at exact cost `1/24` and dual price two.

### Cross-frontier automaton

The Hall/threshold/shell product has 24 states and is strongly connected.  Its
shortest mixed return cycles have six `A` letters and one `B`, hence length seven.
Two repetitions contract the Hall deviation by `9/65536<1/100` while resetting
both phases.

### All-length integerization

Largest-remainder rounding of

```text
(28,27,20,15,12,18)/120
```

has coordinate error below one and period increment 120.  Six-row normalized
rounding loss is below `6/N`, so the ledger's `1/60` slack absorbs it for every
`N>=361`.

### Conditional integration

The exact synthetic fixture composes all displayed arithmetic data for every
length from 361 onward.  This is not a proof of the no-three-in-line conjecture.
The remaining work is to realize, with the same constants, the actual boundary,
Hall, threshold, prefix, shell, and interaction rows in one geometric
prime-patching construction.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_543_548.py
```

or individually with

```bash
python scripts/check_six_frontier_parameter_ledger.py
python scripts/check_phase_locked_marker_semigroup.py
python scripts/check_optimal_slack_purchase.py
python scripts/check_product_synchronizer_automaton.py
python scripts/check_all_length_balanced_rounding.py
python scripts/check_end_to_end_compatibility_fixture.py
```

The diagnostics verify 24 combined residue states, phase-locked marker schedules
through length 1000, the full exact `1/480` slack-allocation grid, all 24 product
automaton states and all words through the first mixed return length, balanced
rounding through length 2000, and 4640 end-to-end synthetic side lengths from 361
through 5000.

The next available theorem identifier is `PP3cnv`.
