# Asymmetric residual-host contraction

This chapter records CMR2852--CMR2863. It resolves the immediate contraction
interface left open by CMR2849. A forced labelled triple does not contract to a
smaller equal-layer square host. It contracts exactly to a two-layer host with
layer-specific surviving row and column domains, transported deleted/required
edges, and opposite-layer blockers at the prescribed physical cells.

The executable checker is:

```text
scripts/check_prime_power_asymmetric_residual_host_contraction.py
```

## CMR2852 — surviving layer domains

Let `(n,D,P)` be a feasible required-prefix context and let

\[
C\subseteq P,
\qquad |C|=3,
\]

be a compatible labelled collinear prescription. For layer
\(\lambda\in\{0,1\}\), write \(C_\lambda\) for the edges of `C` in that layer and
define

\[
R_\lambda
=[n]\setminus\{r:(\lambda,r,c)\in C_\lambda\},
\]

\[
K_\lambda
=[n]\setminus\{c:(\lambda,r,c)\in C_\lambda\}.
\]

Compatibility of `C` implies that its rows and columns are distinct within each
layer. Hence

\[
|R_\lambda|=|K_\lambda|=n-|C_\lambda|.
\]

The residual layer is therefore a perfect matching from `R_lambda` to
`K_lambda`; the two layers need not have the same matching size.

## CMR2853 — canonical asymmetric residual host

Define the residual host to consist of two layer-specific bipartite matching
boards

\[
R_0\times K_0,
\qquad
R_1\times K_1,
\]

using the original integer grid labels. A residual state contains one perfect
matching on each board and the two residual matchings remain physically
disjoint wherever their coordinate domains overlap.

This host type is canonical from the parent context and `C`. No arbitrary
residual family is supplied.

## CMR2854 — exact opposite-layer blockers

If `(lambda,r,c)` belongs to `C`, adjoining `C` forbids the residual edge

\[
(1-\lambda,r,c)
\]

whenever row `r` and column `c` survive in the opposite layer. Let

\[
B(C)
=
\{(1-\lambda,r,c):
 (\lambda,r,c)\in C,
 r\in R_{1-\lambda},
 c\in K_{1-\lambda}\}.
\]

These are exactly the additional deleted residual edges caused by the fixed
physical cells of `C`.

### Proof

A residual edge at the same physical cell would collide with the prescribed
edge after adjoining `C`, so every edge of `B(C)` is forbidden. Conversely, a
prescribed cell can affect the opposite residual layer only at that same
physical coordinate. If its row or column was already removed in the opposite
layer, the edge is absent from that layer domain and no blocker is needed. ∎

## CMR2855 — transported deleted and required contexts

Restrict the inherited deleted mask to surviving layer domains and add the
opposite-layer blockers:

\[
D^{\mathrm{res}}
=
\{(\lambda,r,c)\in D:r\in R_\lambda,
 c\in K_\lambda\}
\cup B(C).
\]

The residual required set is

\[
P^{\mathrm{res}}=P\setminus C.
\]

Compatibility of `P` implies that every edge of `P_res` lies in its surviving
layer domain and that

\[
D^{\mathrm{res}}\cap P^{\mathrm{res}}=\varnothing.
\]

Thus the parent context transports canonically to the asymmetric residual host.

## CMR2856 — restriction/adjoin bijection

Let

\[
\mathcal F^{\mathrm{res}}(n,D,P;C)
\]

be the family of residual two-layer states on the domains from CMR2852 which
avoid `D_res`, contain `P_res`, and satisfy physical-cell disjointness. Then
restriction and adjoining are inverse bijections:

\[
\boxed{
\mathcal F(n,D;P)
\longleftrightarrow
\mathcal F^{\mathrm{res}}(n,D,P;C)
}
\]

through

\[
S\longmapsto S\setminus C,
\qquad
S'\longmapsto S'\cup C.
\]

### Proof

Every parent state contains `C`. Removing it leaves one perfect matching on each
surviving layer domain, preserves every required edge outside `C`, and leaves
exactly the inherited mask plus the blockers of CMR2854. Conversely, a residual
state avoiding those blockers can be adjoined to `C` without a physical-cell
collision. The matching rows and columns removed by `C` are precisely the rows
and columns missing from the residual domains. The two operations are inverse. ∎

## CMR2857 — exact residual triple universe

Let `U_parent` be the exact realizable labelled collinear-triple universe of the
conditioned parent family and `U_res` the universe generated from the residual
family in the original grid coordinates. Then

\[
\boxed{
\mathcal U_{\mathrm{res}}
=
\{T\in\mathcal U_{\mathrm{parent}}:T\cap C=\varnothing\}.
}
\]

### Proof

A parent triple disjoint from `C` remains in the restricted residual state. A
residual triple is realized in a residual state and remains the same physical
triple after adjoining `C`. The original row and column labels are unchanged, so
physical collinearity is unchanged. ∎

This avoids any unproved rank-compression or nonlinear coordinate relabelling.

## CMR2858 — odd residual cardinality

Every parent state contains `2n` labelled edges. Removing the forced triple gives

\[
\boxed{|S\setminus C|=2n-3,}
\]

which is odd.

No standard saturated two-layer square host has odd state cardinality: a side
`m` host has exactly `2m` selected edges.

## CMR2859 — unequal residual layer sizes

Put

\[
c_\lambda=|C_\lambda|.
\]

Since

\[
c_0+c_1=3,
\]

one has `c0 != c1`. Therefore

\[
\boxed{n-c_0\ne n-c_1.}
\]

The residual perfect matchings have unequal sizes in the two labelled layers.
This gives a second obstruction, stronger than an unspecified relabelling issue.

## CMR2860 — standard square-host obstruction

The residual family cannot be isomorphic, by a labelled-edge cardinality
preserving map, to the saturated family of any standard equal-layer square host.
Indeed the residual cardinality is odd by CMR2858, while every standard host
state has even cardinality. Equivalently, its two layer matching sizes are
unequal by CMR2859.

The correct local contraction target is therefore the asymmetric host of
CMR2853, not another plain `F(m,D;P)` context.

## CMR2861 — geometry-preserving representation

The asymmetric residual host retains the original row and column coordinates as
subsets of `[n]`. Consequently determinant-zero collinearity is evaluated in the
same physical grid before and after restriction.

A future compressed-coordinate presentation may be useful for enumeration, but
it would require a separate affine-geometry theorem. No such compression is
used or claimed here.

## CMR2862 — exhaustive finite regression

The checker exhausts 376 distinct side-three contractions arising from masks of
size zero or one and at most one additional required residual edge:

```text
376 contraction scenarios
416 parent state occurrences
416 residual state occurrences
1,128 opposite-layer blockers
188 prescriptions of layer type 3+0
188 prescriptions of layer type 0+3
```

It also exhausts 1,056 distinct side-four contractions with no initial deletion
and at most one additional required residual edge:

```text
1,056 contraction scenarios
2,592 parent state occurrences
2,592 residual state occurrences
1,904 residual realizable triples
3,168 opposite-layer blockers
168 prescriptions of layer type 3+0
360 prescriptions of layer type 2+1
360 prescriptions of layer type 1+2
168 prescriptions of layer type 0+3
```

For every scenario the generated residual family equals literal restriction,
adjoining is its inverse, and the residual triple universe is the exact disjoint
restriction. Ten malformed inputs or corrupted manifests are rejected.

The contract digest is:

```text
fcc593f5812912d031ed90ab37e0fae105a35302a48b757f3fe69a7e80a0403b
```

The censuses are regression evidence. CMR2852--CMR2861 are exact finite
combinatorial statements.

## CMR2863 — T02 consequence and honesty boundary

The first-missing conditioned branch now has an exact generated contraction
target:

```text
parent deleted/required square context
+ forced labelled triple
-> layer-specific surviving domains
+ inherited deleted/required edges
+ exact opposite-layer blockers
-> asymmetric residual family
```

The checker records:

```text
surviving_layer_domains_generated = 1
opposite_layer_blockers_exact = 1
deleted_required_transport_exact = 1
restriction_adjoin_bijection = 1
residual_triple_universe_generated = 1
triple_universe_disjoint_restriction_exact = 1
triple_contraction_residual_cardinality_odd = 1
residual_layer_sizes_unequal = 1
standard_equal_layer_square_host_representability = 0
asymmetric_residual_host_generated = 1
actual_global_parent_rule_complete = 0
all_n_proved_by_checker = 0
```

This closes the local residual-host identification for one forced labelled
triple. It does not yet generate subsequent dispatches on arbitrary asymmetric
hosts, compose repeated contractions, or trace owner, routing, factor and
closure-envelope transitions into the enlarged context model. Global recurrence
exhaustiveness, termination, genuine T03/T04 population, every exceptional
chamber and the all-`n` implication remain open.
