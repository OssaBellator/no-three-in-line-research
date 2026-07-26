# Paid GC4 import for surviving created-collateral stars

**Branch:** `research/geometric-cleaning`

GC2ch--GC2cl attach exact lineage tags to created collateral.  At every checkpoint a selected
created-star cohort is at least half paid by first destructions or at least half survives as a
current endpoint-disjoint star.  The surviving branch is now physically current, but its
interface to the GC4 star machinery still needs to be stated without the latent-weight caveat.

This note makes that import exact.  Surviving lineages are current factor incidences and
cohorts born at different events are disjoint as lineage objects.  A bank of surviving stars
therefore carries genuinely paid current weight.  The existing GC4e conflict regularization
then gives either a labelled paid overload or a simultaneously compatible current-star family
with an explicit fraction of the original created weight.

## Cohort-bank notation

Fix executed birth events indexed by a finite set `I`.  Event `i` supplies one selected
endpoint-disjoint created-collateral star cohort `C_i` through its inserted anchor `q_i`, with
initial lineage weight

`W_i>0`.

At a later common checkpoint write

`W_i=S_i+P_i`,

where `S_i` is the weight of original lineages still current and `P_i` is the weight already
assigned to unique first-destruction incidences.  Put

`W_tot=sum_i W_i`,

`S_tot=sum_i S_i`,

`P_tot=sum_i P_i`.

Discard empty survivor cohorts.  For every remaining `i`, let `Star_i` be the exact surviving
current star and give it weight `S_i`.

Join two surviving stars in the GC4 conflict graph whenever the existing installation
contract declares them incompatible.  For a surviving star `i`, put

`Lambda_i=sum_(j in N[i])S_j`.

The conflict labels and installation semantics are exactly those of GC4e--GC4f.

## GC2cm -- exact aggregate cohort survival/payment identity -- PROVED

At every common checkpoint,

`W_tot=S_tot+P_tot`.

Consequently at least one of

`P_tot>=W_tot/2`,

`S_tot>=W_tot/2`

holds.  Equality may be assigned canonically to the payment branch.

### Proof

GC2ch gives `W_i=S_i+P_i` for each cohort.  Sum over `i` and compare the two nonnegative
summands with half their total. QED.

The identity has no cross-cohort double counting because one lineage has one birth event and
one first-destruction event.

## GC2cn -- surviving cohort weight is current paid incidence -- PROVED

Every factor in `Star_i` is a current exact factor lineage at the checkpoint.  The weights
`S_i` are therefore current syndrome/factor-incidence weights, not latent candidate weights.

Moreover, survivor sets from distinct cohorts are disjoint as lineage objects, even when two
cohorts contain the same geometric-label signature at different times.

### Proof

A surviving original lineage has not yet been destroyed, so by definition it remains the same
current exact occurrence.  GC2ch assigns each lineage to its unique birth cohort.  Recreation
of the same signature creates a new lineage and therefore cannot belong to an earlier cohort.
QED.

Thus the caveat in GC4c and GC4e disappears for these weights: every retained or overloaded
star mass is already paid current structure.

## GC2co -- paid conflict regularization of surviving stars -- PROVED

For every real `K>=1`, at least one of the following GC4e alternatives holds:

1. some surviving star has paid closed-neighbourhood overload

   `Lambda_i>K*S_i`;

2. there is a simultaneously compatible surviving-star family `J` with

   `sum_(i in J)S_i>=S_tot/K`.

If both witnesses exist, choose the overload branch canonically first.  The second family is a
current paid star family ready for the existing GC4 installation or neutralization interface.

### Proof

Apply GC4e to the conflict graph with vertex weights `S_i`.  GC2cn verifies the current-paid
hypothesis, so neither alternative is merely prospective. QED.

For a single surviving cohort the conflict graph has one vertex and the compatible-family
alternative returns the entire surviving star.

## GC2cp -- birth-weight quantitative installation/overload router -- PROVED

Fix `K>=1`.  At every common checkpoint, at least one of the following holds:

1. first-destruction rows have paid at least `W_tot/2`;
2. one surviving star has a paid overload `Lambda_i>K*S_i`;
3. a simultaneously compatible current-star family has total weight at least

   `W_tot/(2*K)`.

### Proof

If `P_tot>=W_tot/2`, use alternative 1.  Otherwise GC2cm gives `S_tot>W_tot/2`.  Apply GC2co.
Its overload branch gives alternative 2, while its compatible branch has weight at least
`S_tot/K>W_tot/(2K)`. QED.

This converts a bank of prospective birth weights into current paid installation weight with
only the unavoidable half-survival factor and the GC4 conflict factor `K`.

## GC2cq -- labelled paid overload continuation -- PROVED

Assume the conflict edges incident with every surviving star use at most `T` exact GC4f
certificate labels, and suppose GC2cp returns an overload

`Lambda_i>K*S_i`

with `K>1`.  Then one certificate label `lambda` carries neighbouring paid current-star weight
strictly greater than

`(K-1)*S_i/T`.

For every `Q>=1`, that label class contains either:

1. a further restricted paid overload; or
2. a simultaneously compatible current-star subfamily of weight greater than

   `(K-1)*S_i/(T*Q)`.

### Proof

Apply GC4f.  GC2cn again supplies the current-paid hypothesis for every star weight in the
label class. QED.

Thus the overload branch also enters an exact finite certificate recursion; it does not return
to latent created collateral.

## GC2cr -- complete surviving-collateral GC4 router -- PROVED UNDER THE EXISTING GC4 CONTRACTS

Suppose a finite bank of executed multiplicative-overload events supplies selected birth-star
weights `W_i`.  At every common checkpoint the bank has one exact continuation:

1. at least half of `W_tot` is already paid by unique first destructions;
2. a compatible current-star family retains at least `W_tot/(2K)`;
3. one paid current-star overload enters the labelled GC4f recursion;
4. independently, the global tagged potential `Phi_tag` strictly decreases on every event
   destroying previously untagged current factors;
5. if the tagged potential has zero drift, the history lies in the tagged-only lineage-cycle
   branch of GC2cl.

No survivor weight is counted in both the compatible-family and first-destruction ledgers.
Repeated geometric signatures are separated by lineage.

### Proof

Use GC2cp for the first three alternatives.  Use GC2cj--GC2ck for the independent tagged-
potential alternatives.  Disjointness follows from the survival/first-destruction partition
and the lineage convention. QED.

## Corrected GC frontier

The executed created-collateral branch now reaches the existing paid GC4 machinery directly.
Its live outputs are:

- a compatible current-star bank with explicit retained weight;
- a labelled paid current-star overload;
- high created-pair multiplicity;
- or tagged-only lineage recycling.

The remaining work is to execute the compatible current-star bank through the final cleaning
move, resolve the labelled overload recursion against the endpoint theorem, and classify
finite tagged-only recycling.  Other interfaces remain isolated-cell prospective stars not
yet tied to an executed event, pool depletion, global context causes and local superregular
resampling.

## Finite check

`scripts/verify_geometric_surviving_star_gc4_import.py` exhausts small weighted cohort banks and
conflict graphs and samples larger systems.  It checks aggregate survival/payment, lineage
disjointness, the weighted independent-set guarantee, the half-plus-conflict constant and the
labelled overload recursion bounds.