# Weighted AN switch/type coverage for paid current stars

**Branch:** `research/geometric-cleaning`

GC2ev--GC2ez replace an externally supplied current-star fraction by a finite AN address dictionary.
The original AN2 theorem already contains a sharper physical address decomposition: after fixing an
admissible rectangle switch, every star endpoint has one of only `2q` layer/channel types.  This note
adds the weighted form, separates the small fibre before the `t>=7` matching threshold, and substitutes
the resulting exact factor into the current-star feedback bounds.

## Switch-covered current-star model

Fix a paid endpoint-disjoint current star through anchor `z`, with exact lineage set `S`, weights
`h_Q>0` and total weight

`A_star=sum_(Q in S) h_Q`.

Assume the **finite switch-coverage contract**:

1. there is a finite ordered admissible switch dictionary `W`, with `K_sw=|W|>=1`;
2. every lineage has at least one switch address whose fixed rectangle operation supports an AN
   neutralization of that lineage through `z`;
3. assigning endpoint-disjoint lineages to the same switch preserves one common post-switch layer and
   channel decomposition;
4. the current configuration uses two permutation layers and at most `q_ch>=1` hyperbola channels;
5. in one fixed layer/channel, chosen endpoints occupy distinct rows and columns;
6. after the fixed switch, the only forbidden matching positions are the original diagonal and the
   other-layer occupied cell, so forbidden row and column degree are at most two;
7. exact aliases are aggregated and failure returns the least switch, role, layer, channel, endpoint,
   row, column or context field.

Assign each lineage to its least legal switch address.

## GC2fa -- canonical switch fibre -- PROVED

One switch fibre has total star weight at least

`A_star/K_sw`.

### Proof

The canonical least-address assignment partitions the exact lineage weight into at most `K_sw`
nonnegative fibres.  A heaviest fibre carries at least the average. QED.

## GC2fb -- weighted AN2 endpoint-type extraction -- PROVED

Inside a fixed switch fibre of weight `A_sw`, one fixed permutation-layer/hyperbola-channel endpoint
type occurs in a distinct-pair subfamily of weight at least

`A_sw/(2q_ch)`.

The selected endpoints occupy distinct rows and columns.

### Proof

Give each endpoint incidence of lineage `Q` weight `h_Q`.  The two endpoints of every pair contribute
total incidence weight `2A_sw`, distributed among at most `2q_ch` types.  One type has incidence weight
at least `A_sw/q_ch`.  A pair contributes at most twice its own weight to one type, so the weight of
distinct pairs containing that type is at least `A_sw/(2q_ch)`.  Choose one endpoint of that type from
each represented pair.  The permutation-layer property gives distinct rows and columns. QED.

This is the weighted form of AN2; no equal-weight assumption is used.

## GC2fc -- small heavy atom or legal AN block -- PROVED

Let the selected endpoint-type fibre have weight `A_type` and contain `t` distinct star lineages.
Exactly one of the following holds:

1. `t<=6`, and one exact current lineage has weight at least

   `A_type/6>=A_star/(12q_ch K_sw)`;

2. `t>=7`, and the chosen endpoints define a legal AN matching block with forbidden row and column
   degree at most two.  Every allowed matching moves every chosen endpoint and destroys all selected
   exact current star lineages.  The executable source weight is at least

   `A_star/(2q_ch K_sw)`.

### Proof

In the small case, weighted pigeonhole over at most six exact lineages gives the first bound.  In the
large case, GC2fb supplies distinct rows and columns.  The switch-coverage contract gives exactly the
two forbidden-position families of AN3, hence degree at most two.  AN1--AN3 apply for `t>=7`, and the
selected source weight is the GC2fa--GC2fb product bound. QED.

The heavy-atom branch is already a current occurrence-faithful lineage; it requires no prospective
realization step.

## GC2fd -- explicit switch/type installed-bank bounds -- PROVED UNDER THE DECLARED CONTRACTS

Use

`Delta_cap=L_cert*(N^2-2)`,

`K_tri=binom(N^2,2)`.

For every `epsilon in (0,1)`, an installed bank of birth weight `W_B` has one continuation:

1. first-destruction payment at least `W_B/2`;
2. one exact current heavy lineage has weight greater than

   `W_B/[8q_ch K_sw N^2(2Delta_cap-1)]`;

3. one AN matching state decreases `Phi` by more than

   `3epsilon W_B/[4q_ch K_sw N^2(2Delta_cap-1)]`;

4. one exact fixed-only certificate has weight greater than

   `3(1-epsilon)W_B/
    [8q_ch K_sw K_fix N^2(2Delta_cap-1)]`;

5. one exact matching-dependent certificate has weight greater than

   `(1-epsilon)W_B/
    [1024q_ch K_sw N^2(2Delta_cap-1)K_tri]`;

6. or one finite-decoration, switch-coverage, matching, certificate, lineage, context or outer-reset
   field fails.

### Proof

GC2er gives a paid star of weight

`A_star>3W_B/[2N^2(2Delta_cap-1)]`.

Apply GC2fa--GC2fc.  In the small branch, multiply the star bound by `1/(12q_ch K_sw)`; since
`3/(2*12)=1/8`, alternative 2 follows.  In the large branch use

`rho=1/(2q_ch K_sw)`

in GC2es and GC2et.  GC2ew loses at most `K_fix` in the fixed branch.  Substitution gives alternatives
3--5. QED.

## GC2fe -- weighted physical AN-coverage router -- PROVED UNDER THE SWITCH-COVERAGE CONTRACT

Every surviving exact-certificate bank now has one nested continuation:

1. at least half its birth weight is first-destruction payment;
2. a small switch/type fibre already contains one quantitatively heavy exact current lineage;
3. a large fibre gives quantified AN descent;
4. failed margin gives one quantitatively heavy exact fixed-only or matching-dependent certificate;
5. all exact outputs enter the existing lineage and finite-signature feedback routers;
6. or one switch-coverage, finite-decoration, execution or context field fails.

### Proof

Combine GC2fd with GC2eg--GC2ep and GC2ey--GC2ez.  The small-fibre output is already current; the two
failed-margin outputs are tagged only when a completed realizing state is installed. QED.

## Corrected GC frontier

The abstract AN address loss is now the explicit product `2q_ch K_sw`.  Weighted endpoint-type
extraction is automatic from the two-layer, finite-channel host, and fibres below the AN threshold
produce a heavy exact current atom instead of a coverage failure.

The remaining geometry is proof that every current-star physical role has at least one admissible
switch in the finite switch dictionary, payment or neutralization of heavy exact current/feedback
certificates, block-tuple overload recursion, unbounded context dictionaries, pool depletion,
global-context causes and local superregular resampling.

## Finite check

`scripts/verify_geometric_weighted_an_switch_coverage.py` samples weighted endpoint-disjoint stars,
nonempty finite switch-address sets, two-layer/channel endpoint types and post-switch forbidden
matchings.  It checks the `1/K_sw` switch fibre, weighted `1/(2q_ch)` AN2 extraction, small heavy-atom
bound, degree-two AN block condition and all integrated birth-weight constants.
