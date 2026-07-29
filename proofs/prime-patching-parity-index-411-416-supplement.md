# Prime-patching parity index supplement: `docs/411--416`

This supplement continues the cumulative parity index after `docs/410`.

| ID | Statement | Status | Location |
|---|---|---|---|
| PP3bxw--PP3bxy | A boundary sunflower with `q` petal-local targets per path and target reuse at most `h` has fractional load at most `h/q`; an intrinsic petal marker makes the reservoirs disjoint and gives the exact optimum | PROVED | `docs/411-sunflower-petal-reservoir-expansion.md` |
| PP3bxz--PP3byb | Backward Hall endpoint mass plus low collision energy, small endpoint atoms, or bounded path merging forces many distinct raw-congestion sources | PROVED | `docs/412-collision-aware-endpoint-localization-for-hall-walks.md` |
| PP3byc--PP3bye | A rooted codegree fan contains a common target subset of every order up to its codegree scale; weighted and dyadic forms produce rooted biclique collision cores | PROVED | `docs/413-rooted-biclique-extraction-from-codegree-fans.md` |
| PP3byf--PP3byh | Corridors of size at most `s` and cycle-vertex load `Delta` split into at most `s(Delta-1)+1` vertex-disjoint repair banks, with a matching weighted pigeonhole bound | PROVED | `docs/414-corridor-intersection-coloring-and-repair-banks.md` |
| PP3byi--PP3byk | Per-boundary multiplicative potentials telescope shell products exactly; logarithmic drops and integer rational-base drops give horizon-free contraction criteria | PROVED | `docs/415-telescoping-potentials-for-shell-expansion.md` |
| PP3byl--PP3byo | Positive diagonal potentials characterize type-matrix contraction, bound arbitrary repetition by a resolvent, and quantify a perturbation reserve for exceptional transitions | PROVED | `docs/416-diagonal-potentials-and-resolvent-reserves-for-type-loads.md` |

## Frontier update

### Boundary recleaning

The sunflower from `docs/405` can now be treated as a direct-clean action graph.
If every petal has at least `q` local repair targets and no target is reused by
more than `h` petals, then

```text
lambda_*<=h/q.
```

If the final target intrinsically records one changed petal vertex, disjointness
of the petals forces `h=1`.  The exact optimum is then the reciprocal of the
minimum petal reservoir size.  The remaining geometric task is explicit: build
several clean actions whose target retains a petal marker after the common core
is repaired.

### Localized Hall transport

A depth obstruction already places a definite endpoint mass on raw-congestion
sources.  That mass now yields a cardinality bound

```text
|H_theta|>=p^2/chi,
```

where `chi` is the collision probability of two independent backward walks.
Alternatively

```text
|H_theta|>=p/beta
```

when every endpoint atom is at most `beta`.  Hence a persistent Hall obstruction
either spreads over many raw sources or exhibits a bounded-depth path-merging
core.

### Fractional direct-clean layers

A dyadic codegree fan no longer remains an unstructured collection of pair
overlaps.  If every fan source shares at least `a` root targets, then for every
`q<=a` one `q`-target set is common to at least

```text
ceil(|F| binom(a,q)/binom(d,q))
```

fan sources.  Direct-clean failure therefore contains a rooted biclique of
controlled target order.  A next repair layer can condition on that common
small target core.

### Support-chord repair words

The complete family inside one dyadic type now decomposes into vertex-disjoint
corridor banks.  With corridor size `s_tau` and maximum cycle-vertex load
`Delta_tau`, at most

```text
s_tau(Delta_tau-1)+1
```

banks are needed.  This turns the prior one-bank extraction into a full
coloring and provides separate target reservoirs for every state of the type.

### Clean-macro shells

Scale-tail charging is complemented by an exact telescoping route.  If an
invariant potential satisfies

```text
p_i Phi(J_(i+1))<=Phi(J_i),
```

then

```text
product_i p_i<=Phi(J_0)/Phi(J_r).
```

In particular, integer drops with rational base `B` give an exact machine
certificate `product p_i<=B^(J_0-J_r)`.  This prevents the same invariant budget
from being charged independently at several thresholds.

### Integration

A type load matrix contracts exactly when it has a positive strict
supersolution.  A certificate

```text
Ma<=q a,
q<1
```

also controls all repetition depths:

```text
sum_(t>=0) M^t b<=beta a/(1-q)
```

for `b<=beta a`.  Exceptional transitions with potential load `epsilon` remain
safe whenever `q+epsilon<1`.  This converts the integration frontier from an
existential spectral-radius condition into explicit rational inequalities with
a quantified reserve.

## Exact diagnostics

Run the complete group with

```bash
python scripts/check_frontier_411_416.py
```

or individually with

```bash
python scripts/check_sunflower_petal_reservoir_expansion.py
python scripts/check_hall_endpoint_collision_localization.py
python scripts/check_rooted_biclique_extraction.py
python scripts/check_corridor_intersection_coloring.py
python scripts/check_telescoping_shell_potentials.py
python scripts/check_type_matrix_potential_resolvent.py
```

The local audits verify exact source-subset expansion, 169 positive backward
paths through depth six, 75 rooted fan families and 85 target-subset orders,
3,858 support-chord corridors in 39 dyadic types, 625 rational shell profiles,
and exact rational type resolvents through twelve stages.

The next available theorem identifier is `PP3byp`.
