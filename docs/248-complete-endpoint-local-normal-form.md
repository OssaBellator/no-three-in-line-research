# Canonical endpoint trades have a complete rank-three local normal form

PP3ase--PP3ask fused every *listed* local source, transition, anchor, endpoint and
insertion restriction into one rank-three helper hypergraph, but retained a possible
"genuinely global condition outside the finite local normal form."  For canonical
source-admissible endpoint replacement trades, that residual alternative is empty.

Saturation is enforced by the explicit permutation cycle.  No-three validity is
exactly the one-, two-, or three-inserted-point trichotomy PP1c.  Controller-shadow
insertion is a pair potential and therefore uses at most two inserted source points.
Selected controllers are punctured after helper selection, and the fixed positive
ownership and global-label margins survive.  These exhaust the endpoint-host
obligations.

## 1. Exact endpoint obligations

Let `X` be the retained current source and let `A` be the cells inserted by one tied
endpoint replacement cycle.

### Proposition PP3atv -- PROVED

The complete admissibility and potential checklist is:

1. **saturation:** every affected row and column loses and gains one source point;
2. **cell distinctness:** no inserted cell duplicates a retained source cell;
3. **one-inserted source validity:** one cell of `A` lies on no secant of `X`;
4. **two-inserted source validity:** no pair of cells of `A` is collinear with one
   point of `X`;
5. **three-inserted source validity:** `A` contains no collinear triple;
6. **controller preservation:** every selected active controller is punctured and
   every unselected controller is fixed;
7. **candidate-shadow insertion:** every newly created blocker pair contains one or
   two cells of `A`;
8. **fixed transition, anchor, pool and distinguished-endpoint rules:** each is
   determined by at most three selected endpoint cells and fixed external data.

No other source-validity or dynamic-potential event exists.

#### Proof

Items 1--2 are the definition of a tied permutation replacement and PP3ia.  Items
3--5 are the exhaustive PP1c trichotomy because `X` is already no-three.  Item 6 is
PP3asu--PP3asx.  The controller-shadow potential is a sum over unordered source
pairs, so a pair newly present after the trade contains one or two inserted cells,
giving item 7.  The final item is the canonical finite list used in PP3ase. ∎

## 2. Strict alternation gives nonempty rank-three support

Let the marked cells be alternated with ordinary helpers.  Record, for every positive
check in PP3atv except the deterministic saturation statement, the ordinary-helper
indices appearing in its selected cells.

### Proposition PP3atw -- PROVED

Every forbidden endpoint pattern has nonempty helper support of size at most three.
More precisely:

1. cell distinctness and one-inserted events have support rank one;
2. pair potential, two-inserted, transition and same-slot anchor events have rank at
   most two;
3. internal source triples and any remaining bounded endpoint pattern have rank at
   most three.

#### Proof

Every selected cell in a strictly alternating cycle contains exactly one helper
index by PP3arp.  A pattern involving `r` selected cells therefore has helper support
between one and `r`.  Apply the bounds in PP3atv. ∎

The support is nonempty even when several selected cells share marked data, because
no selected cell is marked--marked.

## 3. Global allocation certificates are not host constraints

The endpoint cycle does not reassign movement or refill labels.  It only changes the
current source and possibly punctures selected controller values.

### Proposition PP3atx -- PROVED

Suppose the initial random two-sided allocation has fixed positive domain margin.
For a marked package of size `s<=W`:

1. puncturing selected marked/helper controllers deletes at most `2s<=2W=o(R)`
   values from any macro-label domain;
2. deleting source points and candidate entries otherwise improves every
   controller-aware safe domain;
3. a support-free cycle creates no new candidate-shadow incidence;
4. the balanced ownership and global label matching therefore remain valid with a
   fixed smaller positive margin.

#### Proof

Items 1--2 are PP3asu--PP3asv and retained-original domain monotonicity PP3ajm--
PP3ajr.  Item 3 is the zero-insertion conclusion of PP3asf.  Apply the certificate
monotonicity with the surviving margin. ∎

Thus ownership, Hall and label matching are consequences already carried by the
allocation certificate; they are not additional global choices in the endpoint
helper selection.

## 4. Completeness of the fused support table

Let `K_complete` be the union of the helper supports of every positive event in
PP3atv, excluding controller membership singletons handled by selected puncturing.

### Theorem PP3aty -- PROVED

For a canonical tied endpoint replacement cycle:

```text
rank(K_complete)<=3,
```

and an independent helper block gives simultaneously:

1. a saturated source state;
2. no duplicate inserted cell;
3. complete no-three validity;
4. every transition, anchor, pool and distinguished-endpoint condition;
5. fixed unpunctured controllers;
6. zero candidate-shadow insertion cost; and
7. preservation of the positive-margin ownership and global label certificates.

#### Proof

Rank and local admissibility are PP3atw.  Saturation is deterministic.  Puncture the
selected controllers by PP3asu and use PP3atx for the global certificates.  Since the
PP1c cases and the pair-potential insertion cases are exhaustive, independence omits
every possible source or dynamic-potential obstruction. ∎

There is no unrepresented endpoint-host condition for this canonical trade class.

## 5. Unconditional critical endpoint-host theorem

### Theorem PP3atz -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Let a marked block have size `s<=W` and let an occupied post-trade layer contain
`Theta(max(s^2,1))` unreserved coordinates.  For the canonical endpoint trade class,
exactly one of the following occurs.

1. A strictly alternating source-valid cycle exists, has zero insertion cost, and
   preserves all allocation certificates after selected-controller puncturing.
2. The complete support table yields an `Omega(s)` canonical star, matching, endpoint
   bank, transition sunflower, anchor bank, fixed-core petal bank, or
   `A_2/B_3/B_4` structure.

No third "global local-host" alternative remains.

#### Proof

For `s>=3`, apply the exact square-root counting theorem PP3arr to `K_complete` and
convert its dense alternatives by PP3art.  For `s<=2`, use the bounded complete-
support theorem PP3aqh--PP3aqt.  The independent branch is PP3aty. ∎

Coordinate supply is automatic under standard `o(m)` reservations by PP3atf.

## 6. Complete canonical endpoint package

### Corollary PP3aua -- PROVED / CONDITIONAL INITIAL SOURCE-ADMISSIBLE TRADE

Let a first source-admissible saturation-preserving endpoint trade insert at most
`W` cells.  Then the post-trade source automatically decomposes into two layers, and
in every occupied layer PP3atz supplies either a zero-cost cancellation cycle or a
canonical converted structure.

Consequently the full package has exactly one of:

1. complete layerwise insertion cancellation with

   ```text
   Delta Xi<=-R_1;
   ```

2. a target-order canonical converted structure; or
3. a near-complete genuinely reserved-coordinate cover.

#### Proof

Use PP3ath--PP3atl for automatic post-trade assignment, PP3atf for coordinates, and
PP3atz in each occupied layer.  If all layers give cycles, apply PP3asn--PP3aso. ∎

The former unspecified global host alternative has disappeared.

## 7. Revised endpoint frontier

### Corollary PP3aub -- PROVED

For canonical post-allocation endpoint replacement trades, none of the following is
an independent frontier:

1. source-clean or internal no-three validity;
2. transition, anchor, pool or distinguished-endpoint feasibility;
3. Hall, perfect matching or alternating-cycle existence;
4. controller density or controller preservation;
5. ownership and global-label certificate preservation;
6. common-layer assignment; or
7. moderate coordinate shortage.

The remaining concentrated problems are now:

1. obtaining the first source-admissible saturated endpoint trade from the macro
   patch architecture;
2. excluding a genuinely near-complete exogenous coordinate reservation; and
3. completing branches that do not possess the slab-optimal initial random two-sided
   allocation certificate.

The no-three-in-line conjecture remains unproved.
