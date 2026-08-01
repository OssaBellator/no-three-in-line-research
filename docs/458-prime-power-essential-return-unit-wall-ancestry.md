# Essential-return unit walls are exact lower-dimensional construction transitions

This chapter records CMR3034--CMR3047. It installs the CMR727--CMR747 essential-return Hall-wall branch as literal construction ancestry.

The executable checker is:

```text
scripts/check_prime_power_essential_return_unit_wall_ancestry.py
```

## CMR3034 — literal essential-return host

A side-`m` balanced bipartite host is generated from its exact physical edge set. Its perfect-matching family and essential-edge set are enumerated directly. For an essential returned edge `e`, the avoiding host is exactly `H-e`.

## CMR3035 — exact deficiency-one removal

For every generated essential edge, the checker verifies

```text
maximum matching size of H-e = m-1
maximum Hall deficiency of H-e = 1
```

No larger Hall batch is silently introduced.

## CMR3036 — canonical minimal unit wall

The first minimum-cardinality lexicographic deficient source set `X` is selected and `Y=N_{H-e}(X)` is regenerated. The checker verifies

\[
|Y|=|X|-1,
\]

that the source endpoint of `e` lies in `X`, that its target endpoint lies outside `Y`, and that `e` is the unique host edge repairing the cut.

Every nontrivial wall target has at least two neighbours in `X`; singleton walls are recorded separately.

## CMR3037 — stored avoidance witness

The canonical complete-host matching avoiding `e` supplies at least one edge from `X` outside `Y`. The first such edge is stored as the deletion-ancestry witness and is checked to be absent from the current host.

## CMR3038 — exact wall-factor product

After removing the endpoints of `e`, the wall factor and complementary factor are generated with their original vertex labels. The full family is checked to equal exactly

\[
\{e\}\times\operatorname{PM}(H_A)\times\operatorname{PM}(H_B).
\]

## CMR3039 — strict factor-side mass descent

The two factor sides satisfy

\[
a+b=m-1.
\]

Every positive child is therefore strictly smaller than the parent, including the singleton-wall and full-wall boundary cases.

## CMR3040 — exact rank-two target rectangles

Every active compatible collinear target containing `e` leaves exactly two local target edges. The checker reconstructs their factor locations and verifies the exact product occurrence condition.

## CMR3041 — forced-or-deletable wall action

For every such target, exactly one executable branch is recorded.

1. Every local target edge is factor-essential, so the full target is forced in every parent matching and is dispatched to the installed target scheduler.
2. The first nonessential local target edge is deleted, the child family remains nonempty, the target becomes inactive, and no previously inactive target is activated.

## CMR3042 — finite wall normalization

At one fixed wall owner, every nonterminal target action spends one previously available factor edge. Thus the normalization depth is bounded by the literal factor-edge stock.

## CMR3043 — exact factor-tree mass identity

Every unit-wall split replaces side `m` by sides `a,b` with `a+b=m-1`. Hence total active factor-side mass decreases exactly by one at every split.

## CMR3044 — tree node and depth bounds

The checker verifies the symbolic bounds

```text
splits <= d
created nodes <= 2d+1
leaves <= d+1
root-to-leaf depth <= d
```

for every split pair through initial side seven.

## CMR3045 — tree-wide edge and certificate stock

The complete tree edge stock is bounded by

\[
\sum_{j=1}^{d}j^2,
\]

and the owner-labelled certificate stock by

\[
\sum_{j=1}^{d}\binom{j^2}{3}.
\]

For `d=7`, both maxima attain the displayed bounds:

```text
edge stock = 140
certificate stock = 28,512
```

The inherited full-token stock is obtained by multiplying edge stock by `(p+1)(h-1)`.

## CMR3046 — exhaustive finite regression and corruption rejection

The side-three census records:

```text
247 matchable hosts
513 essential-return host/edge pairs
252 singleton unit walls
261 robust unit walls
150 forced wall-target cases
42 deletable wall-target cases
576 full-family state incidences
28 symbolic split pairs through side seven
8 rejected corruptions
```

Every host, wall, factor family, target action and seal is regenerated from literal data.

The contract digest is:

```text
97e448a12314e894018ee0065b9e58b0b4d0172c22f1b619ad7329989f7be0e5
```

## CMR3047 — T02 consequence and honesty boundary

The following installed operations now have genuine ancestry:

```text
essential-return-unit-wall-extraction
essential-unit-wall-factor-split
unit-wall-local-edge-deletion
unit-wall-forced-target-dispatch
unit-wall-factor-tree-split
```

The checker reports:

```text
essential_return_unit_wall_ancestry_proved = 1
unit_wall_factorization_exact = 1
unit_wall_target_normalization_exact = 1
unit_wall_factor_tree_stock_exact = 1
all_owner_operations_proved = 0
all_scheduler_operations_proved = 0
all_restoration_operations_proved = 0
all_returned_edge_operations_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

Other restoration, owner and scheduler operations, global transition exhaustiveness and termination remain open. No all-`n` theorem is claimed.
