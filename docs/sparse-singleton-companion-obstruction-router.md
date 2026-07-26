# Weighted singleton-scope fibres and companion-column obstructions

**Branch:** `research/sparse-algebraic-spread`

SAS5at--SAS5ax close the weighted double-scope reflected-defect route because every
record in one defect-column fibre has the same column scope.  A singleton-scope
mirror word has one additional non-swapped companion column which may vary inside
the fibre.  A donor repairs the whole fibre only when it avoids every such companion.

This note gives the exact weighted dichotomy.  Fibres excluding only a bounded
number of donor-labelled companions admit a large whole-fibre donor matching.
Failure concentrates weighted fibres on one exact donor companion column.
All repair statements use the corrected composed move: the fixed original swap is
applied once together with the donor bank.

## Singleton defect fibres

Fix one original swap `omega={x,y}`, one singleton-scope mirror word, one failing
non-swapped position and required label `ell`.  Let `Z` be the defect columns.

For `z in Z`, let `F_z` be the multiset of retained mirror records whose defect
column is `z`, with total weight

`L(z)=sum_(Q in F_z)w(Q)`.

Each record in `F_z` has scope consisting of:

- one original swapped column;
- the defect column `z`;
- one companion column `c(Q)`.

After `omega`, the swapped scope column and every nondefect literal are correct;
only `z` has the wrong label.

Let

`D_ell={q:kappa(q)=ell}`

be the donor class, of size `d`.  Define the donor-companion obstruction set

`C_z={q in D_ell:q=c(Q) for some Q in F_z}`.

A whole-fibre donor for `z` must avoid `{x,y}` and `C_z`.  Since `z` has the wrong
label, `z notin D_ell`.

## SAS5ay -- safe donors repair an entire singleton fibre after the original swap -- PROVED WITH ORIGINAL-SWAP COMPOSITION

If

`q in D_ell \ ({x,y} union C_z)`,

then the combined move `omega union {z,q}` repairs every record in `F_z`
simultaneously.

### Proof

The original swap puts the required label at the unique swapped scope column of
every mirror record.  The donor `q` supplies `ell` to `z`.  It is outside every
record scope because it avoids the two original swap columns, the defect column is
not donor-labelled, and it avoids every companion in `C_z`.  Therefore the donor
transposition changes no other scope literal and all records in the fibre become
satisfied. QED.

A donor outside one chosen record is not enough; whole-fibre repair requires avoiding
the complete companion obstruction set.

## SAS5az -- bounded companion obstruction gives a donor matching -- PROVED

Fix an integer `h>=0`.  Call a fibre `h`-good when

`|C_z \ {x,y}|<=h`.

Every `h`-good defect has at least

`g=(d-2-h)_+`

safe donors.  Every set of at most `g` distinct `h`-good defect columns admits an
injective assignment of safe donors.  The donor transpositions are endpoint-disjoint
and disjoint from `omega`.

### Proof

At most two donor columns are excluded by `{x,y}`, and at most `h` further donors
are excluded by the companion set.  Thus every good defect sees at least `g` safe
donors.  For a chosen defect set of size at most `g`, every nonempty subset has a
union of safe neighbours of size at least `g`, hence at least the subset size.
Hall's condition gives an injection.  Defects are not donor-labelled, chosen donors
are distinct, and all donors avoid `x,y`. QED.

The neighbour sets need not be equal; the uniform degree lower bound is enough
because the selected left side has size at most that lower bound.

## SAS5ba -- weighted good-fibre bank -- PROVED

Let `Z_good` be the `h`-good defects, let `k_good=|Z_good|`, and write

`W_good=sum_(z in Z_good)L(z)`.

Put

`m=min(k_good,(d-2-h)_+)`.

The `m` heaviest good fibres admit an endpoint-disjoint donor bank `B` such that

`sum_(z in B)L(z) >= (m/k_good)*W_good`

when `k_good>0`.  Applying `omega` once together with the donor bank repairs every
record in all selected fibres.

Under global column incidence `Lambda`, one interaction-independent subbank `I`
retains at least

`[1/(4*Lambda+1)]*sum_(z in B)L(z)`

of the fibre weight, and donor energy increments are additive relative to the
post-`omega` coloring.

### Proof

The top `m` of `k_good` nonnegative loads retain at least an `m/k_good` fraction.
SAS5az supplies distinct safe donors and SAS5ay gives simultaneous whole-fibre
repair.  For the global statement, colour the donor interaction graph with at most
`4*Lambda+1` colours, weight each transposition by `L(z)`, and choose a heaviest
colour class.  Apply SAS5ak from the post-`omega` baseline. QED.

## SAS5bb -- bad fibres concentrate on one exact donor companion -- PROVED

Let `Z_bad` be the fibres with

`|C_z \ {x,y}|>h`

and total weight

`W_bad=sum_(z in Z_bad)L(z)`.

Then some exact donor column `q in D_ell\{x,y}` belongs to `C_z` for a weighted
family of bad defect fibres of total load greater than

`h*W_bad/d`.

### Proof

Count weighted incidences `(z,q)` with `z in Z_bad` and
`q in C_z\{x,y}`, giving each incidence weight `L(z)`.  Every bad fibre contributes
more than `h L(z)`, so total incidence weight exceeds `h W_bad`.  There are at most
`d` donor columns.  Weighted pigeonhole gives one column with incidence load greater
than `h W_bad/d`. QED.

This is a whole-fibre obstruction certificate: the same donor-labelled companion
column lies in at least one record of every retained fibre.  It need not carry all
record weight within each fibre, so no stronger record-incidence claim is made.

## SAS5bc -- weighted singleton companion router -- PROVED

Let a singleton reflected-label defect family have total weight `W`, and retain one
required-label class of weight `W_ell>=W/b` as in SAS5ae.  Fix `h>=0` and split its
fibre weight into `W_good+W_bad=W_ell`.

One of the following holds:

1. `W_good>=W_ell/2`; with `m=min(k_good,(d-2-h)_+)`, an original-plus-donor
   whole-fibre batch repairs weight at least

   `W*m/(2*b*k_good)`,

   and under global incidence `Lambda` an additive compatible subbatch repairs at
   least

   `W*m/[2*b*k_good*(4*Lambda+1)]`;
2. `W_bad>W_ell/2`; one exact donor companion column obstructs fibres of total load
   greater than

   `h*W/(2*b*d)`.

### Proof

One of the good and bad weights is at least half of `W_ell`.  In the good branch,
apply SAS5ba and substitute `W_good>=W/(2b)`.  In the bad branch, apply SAS5bb and
substitute `W_bad>W/(2b)`. QED.

The second branch is an exact companion-column concentration suitable for the
column-pair, arithmetic-dilation or high-incidence classifiers.  It is not asserted
to be an improving move.

## Corrected SAS6 frontier

The weighted reflected-defect routes now have parallel forms:

- double-scope fibres repair directly with `d-2` donor supply;
- singleton fibres with at most `h` donor companions repair with `d-2-h` supply;
- failure returns one exact donor-labelled companion column obstructing a quantified
  weighted fibre family.

Remaining work is to classify this companion-column concentration through the
primitive dilation parameter, handle high global incidence and board-boundary
profiles, and compare the full composed move with the original energy.

## Finite check

`scripts/verify_sparse_singleton_companion_router.py` exhausts small singleton fibre
systems, donor classes and companion obstruction sets.  It checks safe whole-fibre
repair under original-swap composition, Hall matching for all good subsets, top-load
retention, the weighted bad-companion concentration and compatible weighted
subbank extraction.