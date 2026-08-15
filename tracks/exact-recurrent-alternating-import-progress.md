# Exact recurrent alternating-core import progress

**Branch:** `research/exact-recurrent-lyapunov-audit`

This track records only interfaces imported from the main-focus branch
`research/alternating-core-chain`. It does not identify the alternating-core
construction with the prime-power side-four construction.

## ERL1w — cross-branch contract audit

Four alternating-core interfaces were audited:

```text
occurrence-lineage gates
physical-signature lineage quotient
physical arithmetic-profile bound
cross-branch event interfaces
```

They provide conditional rules for exact owner continuation, finite physical
signature quotients, shared alias capacities, polynomial arithmetic labels and
physical event costs. They do not supply first-host occurrence records or values
for any of the sixteen required physical fields.

## ERL1x — exact safe score quotient

Under chart confinement and response disjointness, the 32 possible first-host
backgrounds have exactly three complete-score classes:

```text
offset 0: 20 backgrounds
offset 1:  8 backgrounds
offset 2:  4 backgrounds
```

For offset `c`, the score vector in response order
`3012,3210,2031,2310,3201` is

```text
(1+c,4+c,c,c,c).
```

Every class has minimizer face `{2031,2310,3201}`.

## ERL1y — exact side-four arithmetic-profile import

For side four, the normalized primitive direction universe has exactly 15
elements. The 225 ordered direction pairs contain 210 nonzero determinants, and
the nonzero determinant magnitudes are exactly `1,2,...,13`.

Every reduced determinant-ratio denominator is therefore at most 13, improving
the generic alternating-core safe bound 18. The exact conditional arithmetic
profile stock is 20,250 rather than 38,250. With 16 board anchors, the exact
non-scalar address coefficient is `324,000 * L_ext` rather than
`612,000 * L_ext`.

This does not populate `provenance.crt`: no physical source proves determinant
realization for the first host, and the external role dictionary bound `L_ext`
remains absent.

## ERL1z — exact safe 31-signature quotient

The three complete-score classes are not the exact geometric state alphabet.
Recomputing all 31 signature coordinates gives four classes:

```text
no active target pair: 20 backgrounds
active pair {00,01}:    4 backgrounds
active pair {01,11}:    4 backgrounds
both active pairs:      4 backgrounds
```

All 20 secant line-load coordinates vanish. The two offset-one classes have the
same score vector `(2,5,1,1,1)` but different pair-through coordinates. Thus
present score equality does not imply exact signature equality.

## ERL2a — symmetry does not repair the score collision

The ambient row/column/axis action contains 1152 maps, but only eight preserve
all standard-grid collinear triples. The exact first-host stabilizer preserving
the target and five-response menu is trivial.

The only nonidentity map preserving the lineage host and deletion set is
transposition. It sends target `01` to `10` and does not exchange the two
ordered target-pair activations. Therefore the four exact signature classes do
not reduce to three by symmetry.

## ERL2b — restoration-menu closure

Exact perfect-matching enumeration gives

```text
restore 02:   2031,2310,3012,3210
restore 20:   3012,3201,3210
restore both: 2031,2301,2310,3012,3201,3210.
```

For every safe background, the single-restoration minimizer faces are fixed:

```text
restore 02 -> {2031,2310}
restore 20 -> {3201}.
```

Simultaneous restoration exposes the new response `2301={02,13,20,31}` and
three previously absent secant lines:

```text
x+y=2
x+y=4
3x+y=6.
```

On the safe class, define

```text
a=1[{00,01} subset B]
b=1[{01,11} subset B]
u=1[11 in B]
v=1[22 in B].
```

Then `score(2301;B)=a+b+u+v`. Exactly ten operation-aware signatures
`(a,b,u,v)` occur. They collapse to eight six-response score vectors, with two
explicit collisions:

```text
(1,4,0,0,0,1): (0,0,0,1) and (0,0,1,0)
(2,5,1,1,1,2): (0,1,1,0) and (1,0,0,1).
```

Therefore the four-state current signature is not closed under the expanded
menu, and even the eight-state score quotient is non-injective. The minimum
known operation-aware geometric alphabet on the safe class has ten states.

## ERL2c — selector identity and gap congruence

The complete minimizer face under simultaneous restoration is not constant:

```text
{2031,2301,2310,3201}: 8 backgrounds
{2031,2310,3201}:      24 backgrounds.
```

Nevertheless, under the canonical rule “lexicographically least response in
the complete-score minimizer face,” the selected response is constant on the
safe class for every restoration menu:

```text
blocked      -> 3012
restore 02   -> 2031
restore 20   -> 3201
restore both -> 2031.
```

The positive next-distinct-energy gap is also constant per menu:

```text
blocked      gap 3
restore 02   gap 1
restore 20   gap 1
restore both gap 1.
```

Thus selector identity and selector-stability gap admit a one-state quotient
inside each fixed restoration menu even though the exact face and operation
geometry require more states. This is a partial congruence result only; it does
not identify child rows, weights, budgets, continuation edges or capacities.

## ERL2d — exact Boolean selector boundary and descent obstruction

Use restoration bits

```text
r02=1 iff edge 02 is restored
r20=1 iff edge 20 is restored.
```

The exact selected-response predicates are

```text
3012 iff not r02 and not r20
2031 iff r02
3201 iff not r02 and r20.
```

The two-bit cube has eight directed single-bit context edges. Six change the
selected response and two toggle `r20` while retaining `2031`. The six exact
false-to-true selector gates split as two gates for each of `3012`, `2031` and
`3201`, improving the generic three-label single-bit bound from 12 to 6. The
exact arbitrary-jump gate stock is 10 rather than the generic bound 12.

After projecting the six changing edges to selected labels, every ordered pair
of distinct labels occurs. Hence the label graph is the complete bidirected
triangle with one three-vertex strongly connected component.

A scalar label potential can strictly pay at most one direction from each of
the three unordered label pairs. Therefore

```text
maximum selector edges payable by strict label descent  3
minimum selector edges requiring another closure route   3.
```

Likewise the four-state menu graph is bidirected on all four cube edges, so a
menu-state-only scalar can strictly pay at most four of its eight directed
edges. At least four menu edges require physical exclusion, richer-state
progress, finite capacity, terminal output or builder reset.

These are symbolic lower bounds. Persistent owner identity, legal transition
realization and gate capacities remain unpopulated.

## Import boundary

Current source coverage still has zero of sixteen physical fields populated.
There is no proof that legal operations, intermediate states, child rows,
weights, budgets, continuation identity or shared capacities factor through the
ten operation-aware signatures.

The selector Boolean interface now supplies six exact symbolic gate addresses,
but no gate is attached to a persistent physical owner token and no closure
route or capacity is populated. Selected-label-only and menu-state-only strict
potentials are both refuted on the complete symbolic edge stocks.

The arithmetic import supplies a finite conditional CRT alphabet but not the
actual CRT profile or continuation/payment data.

Therefore:

```text
alternating_core_recurrence_closure_import_allowed = 0
promotion_to_recurrent_row_allowed = 0
all_n_proved_by_checker = 0
```

## Executable artifacts

```text
scripts/check_exact_recurrent_first_host_alternating_lineage_import.py
data/exact_recurrent_first_host_alternating_lineage_import.json
docs/exact-recurrent-first-host-alternating-lineage-import.md

scripts/check_exact_recurrent_first_host_side_four_arithmetic_profile_import.py
data/exact_recurrent_first_host_side_four_arithmetic_profile_import.json
docs/exact-recurrent-first-host-side-four-arithmetic-profile-import.md

scripts/check_exact_recurrent_first_host_safe_signature_quotient.py
data/exact_recurrent_first_host_safe_signature_quotient.json
docs/exact-recurrent-first-host-safe-signature-quotient.md

scripts/check_exact_recurrent_first_host_safe_signature_symmetry.py
data/exact_recurrent_first_host_safe_signature_symmetry.json
docs/exact-recurrent-first-host-safe-signature-symmetry.md

scripts/check_exact_recurrent_first_host_restoration_menu_closure.py
data/exact_recurrent_first_host_restoration_menu_closure.json
docs/exact-recurrent-first-host-restoration-menu-closure.md

scripts/check_exact_recurrent_first_host_restoration_selector_face.py
data/exact_recurrent_first_host_restoration_selector_face.json
docs/exact-recurrent-first-host-restoration-selector-face.md

scripts/check_exact_recurrent_first_host_selector_boolean_boundary.py
data/exact_recurrent_first_host_selector_boolean_boundary.json
docs/exact-recurrent-first-host-selector-boolean-boundary.md

.github/workflows/exact-recurrent-first-host-alternating-lineage-import.yml
```

The next admissible cross-branch result must attach physical owner identities and
registered closure routes to all realized selector gates, populate a
payment-complete physical signature map and continuation edges, prove operation
and child-row congruence on the ten exact operation-aware states, or attach a
physically determinant-realized CRT profile and finite external role address.
