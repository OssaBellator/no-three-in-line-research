# Direct current-anchor matching neutralization

**Branch:** `research/geometric-cleaning`

GC2fa--GC2fe extract a finite switch fibre before applying the AN matching bank.  That switch is
needed in the original secant-star construction because the star anchor is a newly inserted candidate
point.  The stars produced by GC2eg--GC2ep are different: their anchor and every selected certificate
are already current physical occurrences.

For this current-anchor branch the fixed rectangle preparation is unnecessary.  After weighted AN2
endpoint-type extraction, one may move the selected endpoints directly inside their existing
permutation layer.  The original diagonal and the unchanged opposite layer give the same
degree-two forbidden-position system as AN1--AN3, while the fixed-only collateral is exactly zero.

## Direct current-star model

Fix a paid endpoint-disjoint current star through a current anchor `z`.  Its exact lineage set is `S`,
with weights `h_Q>0` and

`A_star=sum_(Q in S) h_Q`.

Each lineage has a current physical triple

`Q={z,x_Q,y_Q}`,

and the pairs `{x_Q,y_Q}` are endpoint-disjoint.  Assume the **direct current-anchor host contract**:

1. the current configuration is the union of two disjoint permutation layers;
2. every endpoint has one of at most `q_ch` declared channel labels;
3. moving either selected endpoint while fixing `z` and the other endpoint destroys the named exact
   lineage;
4. endpoints in one fixed layer/channel occupy distinct rows and columns;
5. after removing selected endpoints from one layer, the only forbidden replacement positions are
   their original cells and cells occupied by the unchanged other layer;
6. every allowed replacement matching preserves the declared row, column, layer and hard-context
   constraints;
7. aliases are aggregated, and failure returns the least layer, channel, endpoint, row, column,
   matching, occurrence or context field.

No rectangle switch or fixed preparation is performed.

## GC2ff -- weighted direct endpoint-type extraction -- PROVED

One permutation-layer/channel endpoint type occurs in a distinct-pair subfamily of weight at least

`A_star/(2q_ch)`.

The selected endpoints occupy distinct rows and distinct columns.

### Proof

Give each endpoint incidence of lineage `Q` weight `h_Q`.  Total endpoint-incidence weight is
`2A_star`, distributed among at most `2q_ch` types.  One type has incidence weight at least
`A_star/q_ch`.  A pair contributes at most twice its own weight to one type, so the total weight of
distinct pairs containing that type is at least `A_star/(2q_ch)`.  Choose one endpoint of the fixed
type from every represented pair.  The permutation-layer property gives distinct rows and columns.
QED.

No equal-weight assumption is used.

## GC2fg -- heavy current atom or legal direct AN block -- PROVED

Let the selected endpoint-type fibre have weight `A_type` and contain `t` distinct lineages.  Exactly
one of the following holds:

1. `t<=6`, and one exact current lineage has weight at least

   `A_type/6>=A_star/(12q_ch)`;

2. `t>=7`, and the selected endpoints define a legal AN matching block whose source weight is

   `a=A_type>=A_star/(2q_ch)`.

In the second branch every allowed matching moves every selected endpoint and destroys every selected
current lineage.

### Proof

The small branch is weighted pigeonhole.  In the large branch, index the selected endpoint columns and
rows by their original matching.  Forbid the original diagonal.  The unchanged other permutation
layer contributes at most one forbidden cell in each selected row and each selected column.  Thus the
union has forbidden row and column degree at most two.  AN1 gives a nonempty allowed matching family
for `t>=7`; AN3 shows that every selected endpoint moves.  Item 3 of the host contract then destroys
every named lineage. QED.

## GC2fh -- zero fixed-only collateral -- PROVED

For the direct current-anchor matching bank,

`F_fix=0`.

Every genuinely new exact certificate in a resulting state uses at least one moved matching cell.

### Proof

There is no fixed rectangle preparation.  The anchor, unchosen endpoints, opposite permutation layer
and every other fixed cell are identical before and after the operation.  A certificate using only
fixed cells would therefore already have been present before the matching.  Hence no fixed-only new
certificate exists, and the fixed collateral total is zero. QED.

This removes the heavy fixed-switch branch rather than merely relabelling it.

## GC2fi -- direct installed-bank execution bounds -- PROVED UNDER THE HOST CONTRACT

Use

`Delta_cap=L_cert*(N^2-2)`

and

`K_tri=binom(N^2,2)`.

For every `epsilon in (0,1)`, an installed exact-certificate bank of birth weight `W_B` has one
continuation:

1. first-destruction payment at least `W_B/2`;
2. one exact current heavy lineage has weight greater than

   `W_B/[8q_ch*N^2*(2Delta_cap-1)]`;

3. one direct AN matching state decreases `Phi` by more than

   `3epsilon*W_B/[4q_ch*N^2*(2Delta_cap-1)]`;

4. one exact matching-dependent prospective certificate has weight greater than

   `(1-epsilon)*W_B/
    [512q_ch*N^2*(2Delta_cap-1)*K_tri]`;

5. or one finite-decoration, direct-host, matching, inventory, lineage, context or outer-reset field
   fails.

### Proof

GC2er supplies a paid current star with

`A_star>3W_B/[2N^2(2Delta_cap-1)]`.

Apply GC2ff--GC2fg.  In the small branch, multiply by `1/(12q_ch)`; since
`3/(2*12)=1/8`, alternative 2 follows.

In the large branch,

`a>=A_star/(2q_ch)`.

GC2fh gives `F_fix=0`.  If the complete matching-dependent collateral expectation satisfies

`E_AN<=(1-epsilon)*a`,

the single-witness average gives descent at least `epsilon*a`, proving alternative 3.

Otherwise `E_AN>(1-epsilon)*a`.  One of the three rank contributions satisfies

`128*T_r/(t)_r>(1-epsilon)*a/3`.

Therefore one ordered prescription carries weight greater than `(1-epsilon)*a/384`, and one of at
most `K_tri` exact completions has weight greater than

`(1-epsilon)*a/(384K_tri)`.

Substituting the strict star bound and `a>=A_star/(2q_ch)` gives alternative 4 because
`3/(4*384)=1/512`.  All excluded hypotheses are the named failures. QED.

## GC2fj -- direct current-anchor router -- PROVED UNDER THE DECLARED CONTRACTS

Every surviving exact-certificate bank now has one nested continuation:

1. at least half its birth weight is first-destruction payment;
2. a small endpoint-type fibre already contains one quantitatively heavy exact current lineage;
3. a large endpoint-type fibre gives direct AN descent with no switch loss and no fixed collateral;
4. failed margin gives one quantitatively heavy matching-dependent exact certificate;
5. every exact output enters the existing occurrence-faithful lineage and finite-signature feedback
   routers;
6. or one direct-host, finite-decoration, execution or context field fails.

### Proof

Combine GC2fi with GC2eg--GC2ep and GC2ey--GC2ez.  The small output is already current.  The
matching-dependent output is tagged only when its realizing completed matching state is installed.
QED.

## Corrected GC frontier

For already-current certificate stars, the abstract switch dictionary is unnecessary.  Weighted
endpoint-type extraction retains `1/(2q_ch)` directly, the matching family has degree-two forbidden
positions, and fixed-switch collateral vanishes exactly.

The remaining geometry is payment or neutralization of the resulting heavy exact current/feedback
certificates, roles outside the direct two-permutation-layer/channel host, block-tuple overload
recursion, unbounded contexts, pool depletion, global-context causes and local superregular
resampling.

## Finite check

`scripts/verify_geometric_direct_current_anchor_matching.py` samples weighted endpoint-disjoint stars
inside two disjoint permutation layers.  It checks weighted endpoint-type extraction, the small
heavy-atom branch, row/column degree two of the direct forbidden system, existence of an allowed
matching, destruction of every selected old lineage, zero fixed-only collateral and all integrated
birth-weight constants.
