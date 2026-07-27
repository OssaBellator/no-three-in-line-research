# All-n product track: paired terminal integration and finite-range frontier

**Branch:** `research/all-n-product-construction`

This track began with terminal Hall-core classification. The later historical,
packet, buffer, and paired-label chapters now carry those local terminal
interfaces into one factor-compatible rectangle-label repair tree. The active
remaining obstruction is no longer an unclassified terminal core: it is finite
coverage below the explicit asymptotic cutoff.

The classical no-three-in-line conjecture and exact all-side product closure
remain open.

## Current ledger

| Item | Status | Current result |
|---|---|---|
| Terminal Hall failure | **CLASSIFIED** | PX270 localizes every failure to a complete forbidden rectangle and bounds deficiency by `2Delta-m`. |
| Sharp and maximal Hall cores | **ABSORBED** | PX271 and PX281--PX286 delete the common-label deficiency and rematch every remaining endpoint. |
| Terminal exact optimization | **SUBPOWER** | PX273--PX276 enumerate one- and two-block terminal states in `N^o(1)` time and emit replayable obstruction certificates. |
| Paid-certificate recurrence | **CLOSED** | PX277--PX280 give causal lexicographic descent and prevent paid defects from returning. |
| Principal cycle escape | **AVAILABLE** | PX287--PX290 give an executable directed cycle trade whenever one exists. |
| Trajectory-saturated core | **INTEGRATED** | PX291--PX293 classify it; the historical reset, overlap, antichain, coupled-absorber, and buffer chapters 134--152 feed it back into the rectangle-label tree. |
| Strict-sign-or-child interface | **INTEGRATED** | The diffuse packet, line, radial, mixed-shadow, and terminal-return branches are lifted to exact rectangle-label moves through PX397--PX449. |
| Dependency audit | **CLOSED FOR ACTIVE PATH** | PX451--PX455 and the repository scanner audit move-space tags, constants, theorem uniqueness, and the paired-label dependency chain. |
| Effective asymptotic cutoff | **EXPLICIT** | PX962--PX965 give `d(N)<10^(2469/41)N^(6/41)` and lower the common cutoff to `N>=10^2874`. |
| Below-cutoff coverage | **OPEN** | Orders below `10^2874` need a structural bridge, exact extension chain, interval-specific theorem, or finite classification. |
| Infinite exact closure | **OPEN** | No theorem currently covers every side length. |

## 1. Terminal structure now used by the active path

For an order-`m` allowed graph with forbidden degree `Delta`, every positive
matching deficiency produces a complete forbidden rectangle `S x B` with

\[
|S|+|B|=m+\delta,
\qquad
|S|,|B|\le\Delta,
\qquad
\delta\le2\Delta-m.
\]

Maximal deficiency is removed by deleting exactly the shared labels and
rematching the exposed cross-blocks. When a principal directed cycle exists,
PX287--PX290 execute it. When it does not, PX291--PX293 force a fully forbidden
row and column and hence a trajectory-saturation certificate.

The later historical-reset and buffer-return chapters no longer treat that
certificate as a terminal dead end. They convert it into a deeper causal child,
a coupled move, or an audited finite obstruction, all in rectangle-label move
space.

## 2. Paired-label splice

PX397--PX403 audit the actual PX63 entry. PX404--PX410 use the true PX64 line
cap. PX411--PX444 lift terminal, first-generation, packet, mixed-shadow, and
recurrence moves to exact permutations of the two rectangle labels. PX445--PX450
then give the conditional asymptotic strict-decrease loop.

The combined causal vector decreases lexicographically at every repair
transition. Consequently every positive factor-compatible rectangle state above
the common cutoff has a finite repair subtree ending in a strict reduction of
the integer bad-triple potential.

## 3. Active numerical root

The exact nested depth, Cartesian incidence constant, packet-family-free path,
and rational divisor witnesses make the asymptotic branch effective. The current
`3/41` product certificate gives

\[
\mathfrak d(N)<10^{2469/41}N^{6/41}
\]

and the common cutoff

\[
\boxed{N\ge10^{2874}}.
\]

The verifier confirms that `10^2873` fails the same divisor-controlled
retained-order inequality for this witness. Further universal-exponent tuning is
secondary to the finite-range bridge.

## Immediate frontier

1. **Finite-range bridge.** Construct an extension or absorber chain covering
   every order below `10^2874`, or replace the universal divisor estimate by
   interval-specific bounds that descend through the range.
2. **Recursive produced-base closure.** Prove an iteration theorem from the
   existing exact sides `6`, `8`, `10`, or `12`, especially a closure based at
   side ten or twelve.
3. **Side-seven finite classification.** Continue the exact multiplicity-two
   selector census from global case `80`; postpone multiplicity one until its
   certificate structure is understood.
4. **Low-multiplicity proof compression.** Measure explicit bottom-permutation
   triple covers and combine them with minimized top-assumption nogoods.
5. **General repair/resampling.** Seek a theorem coordinating many product
   projection fibres, or a conflict-free exact-cover/resampling result that
   subsumes the finite host searches.
6. **Independent geometric frontiers.** The hyperbola pathway still needs
   second-generation collateral concentration, monotone alternating closure, or
   bounded-denominator chamber absorption.

## Verification

```bash
python scripts/verify_product_terminal_hall_core.py
python scripts/verify_product_terminal_core_optimizer.py
python scripts/verify_product_causal_lexicographic_descent.py
python scripts/verify_product_sharp_hall_absorber.py
python scripts/verify_product_maximal_deficiency_absorber.py
python scripts/verify_product_terminal_cycle_escape.py
python scripts/verify_product_trajectory_saturated_core.py
python scripts/verify_product_splice_interface.py
python scripts/verify_product_entry_invariant_dependencies.py
python scripts/verify_product_three_forty_first_divisor_cutoff.py
```
