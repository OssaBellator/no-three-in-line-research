# Fixed routing gives exact child products and strict child handoff

This chapter records CMR2920--CMR2931. CMR2900--CMR2919 install genuine
construction ancestry for changes between routing skeletons. The present chapter
handles the complementary fixed-routing operation: once one routing skeleton is
chosen, the factor family becomes an exact product of strict child factors, and
a mixed-clean obstruction hands off to one strict child.

The executable checker is:

```text
scripts/check_prime_power_factor_child_product_ancestry.py
```

## CMR2920 — typed fixed-routing product split

Let `H` be a nontrivial balanced factor host inside the canonical factor envelope
of CMR656. Choose one feasible factor matching `M` and reconstruct its routing
skeleton `Gamma(M)`.

The checker emits the typed operation

```text
transition_kind = fixed-routing-child-product-split
```

with the literal parent factor context, the canonical routing skeleton, the
parent and strict-child envelope data, and one generated child context for every
nonempty routing cell.

## CMR2921 — exact child contexts

For every nonempty routing cell `(r,s)`, define

\[
X_{rs}=\{x\in X_r:M(x)\in Y_s\},
\qquad
Y_{rs}=\{y\in Y_s:M^{-1}(y)\in X_r\}.
\]

The child context has:

```text
ambient side = p^h
layer 0 rows = X_rs
layer 0 columns = Y_rs
layer 1 rows/columns = empty
deleted edges = inherited deleted edges in X_rs x Y_rs
required edges = empty
prefix depth = beta+1
```

Every child is therefore an established asymmetric context, not an anonymous
factor object.

## CMR2922 — exact fixed-routing product bijection

Let `F_Gamma` be the parent perfect matchings whose reconstructed routing
skeleton is `Gamma`. The checker generates every child matching family and
forms their Cartesian product. Union of the child matchings gives exactly

\[
\boxed{
\mathcal F_\Gamma
\cong
\prod_{r,s}\operatorname{PM}(H[X_{rs},Y_{rs}]).
}
\]

The generated product family and the directly filtered parent family agree as
canonically ordered sets of labelled edges.

### Proof

Fixing the routing skeleton fixes the source and target vertex partitions. Every
matching edge is internal to its unique routing cell, distinct cells have
disjoint source and target sets, and arbitrary child perfect matchings unite to
one parent matching with the prescribed skeleton. Restriction and union are
inverse. ∎

This is the executable CMR659 product factorisation.

## CMR2923 — positive child count and strict factor-side descent

The canonical first split occupies at least two positive routing cells. Their
positive matching sizes sum to the parent factor side `d`, so every child has

\[
1\le d_{rs}\le d-1.
\]

The checker rejects a purported fixed-routing product with fewer than two
positive children or a non-strict child matching size.

## CMR2924 — strict prefix-envelope descent

Every generated child lies in one depth-`beta+1` prefix cell. Its envelope side
is

\[
\frac{p^h}{p^{\beta+1}},
\]

strictly smaller than the parent envelope side

\[
\frac{p^h}{p^\beta}.
\]

Thus the child contexts carry both strict factor-side and strict geometric
envelope descent.

## CMR2925 — theorem-derived product labels

The product transition labels are reconstructed from literal theorem data:

```text
operation_slot = CMR659-CMR663-fixed-routing-child-product
owner/factor = digest of ambient side, factor domains and deleted edges
routing = digest of the selected routing skeleton
envelope = digest of parent and child prefix depths/sides
```

Therefore

```text
factor_product_construction_ancestry_proved = 1
```

for this operation kind.

## CMR2926 — exact mixed-clean predicate

For every state in the generated product, inspect all physically collinear
three-edge subsets in original grid coordinates. A triple is mixed exactly when
its edges belong to more than one generated child context.

The strict handoff operation is admitted only when no product state contains a
mixed triple. This is the literal mixed-clean hypothesis of CMR682.

## CMR2927 — global clean state versus pure-dirty child

In a mixed-clean product, every candidate triple is pure in one child. Hence a
product state is globally clean exactly when all of its child restrictions are
pure-clean.

If the generated product has no globally clean state, at least one child family
has no pure-clean matching.

### Proof

With no mixed triple, the triple count is the sum of the child triple counts.
A sum of nonnegative integers is zero exactly when every summand is zero. ∎

## CMR2928 — canonical dirty-child selection

The checker lists every child whose complete feasible family is pure-dirty and
selects the first child in canonical routing-cell order.

It records the exact selected child context rather than only its side or prefix
label.

## CMR2929 — strict mixed-clean child handoff

The typed operation

```text
transition_kind = mixed-clean-strict-child-handoff
```

is emitted only when:

1. the fixed-routing product is mixed-clean;
2. no globally clean product state exists; and
3. the selected child has no pure-clean matching.

The selected child has matching size at most `d-1` and prefix depth exactly
`beta+1`. Thus the CMR683 lexicographic geometric measure decreases in its first
two coordinates.

This proves

```text
mixed_clean_child_handoff_ancestry_proved = 1
```

without claiming the preceding mixed-atom deletion branch.

## CMR2930 — finite product and handoff regression

The checker exhausts distinct routing skeletons for factor hosts of matching size
at most three in the binary side-four and ternary side-three domains. It records:

```text
176 fixed-routing product splits
422 generated strict child contexts
192 fixed-routing factor states
7 rejected malformed or corrupted cases
```

A separate binary side-eight witness uses two routing children. The first child
has matching size three and is forced to the collinear matching

```text
(0,0), (2,2), (4,4)
```

while the second child is the off-line singleton `(1,3)`. The product is
mixed-clean, has no globally clean state, and hands off canonically to the strict
size-three child.

The contract digest is:

```text
bd725106632e65cac38f2b33fb1787f3d5ef93d0825c4ccfc0d2afd2c6492dae
```

## CMR2931 — T02 consequence and honesty boundary

Two genuine factor operations now have exact construction ancestry:

```text
routing-skeleton-change
fixed-routing-child-product-split
mixed-clean-strict-child-handoff
```

Routing changes have finite-stock/full-token payment; fixed routing has exact
product semantics; the mixed-clean dirty branch has strict child descent.

The remaining fixed-product operation is the CMR677--CMR681 mixed-atom deletion
or forced-certificate procedure. Owner changes, closure-envelope changes,
restoration, returned-edge, target-handoff and scheduler transitions also remain
uninstalled.

The checker therefore preserves:

```text
factor_product_construction_ancestry_proved = 1
mixed_clean_child_handoff_ancestry_proved = 1
mixed_atom_deletion_ancestry_proved = 0
all_construction_ancestry_proved = 0
global_transition_kind_bank_exhaustive = 0
global_termination_proved = 0
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

No all-`n` theorem, genuine T03/T04 population, chamber proof or final implication
is claimed.
