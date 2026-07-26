# Designated credit under permanent matching-block refinement

The fixed-attempt extraction theorems produce blocker stars, blocker endpoint banks,
and same-slot anchor banks.  The fixed-infrastructure restart theorem realizes a
repair by partitioning its marked source cells among the permanent matching blocks

```text
E_1,...,E_M,E_*,Q.
```

This chapter verifies the missing call-site property: every extracted unit of credit
is an incidence containing an actual current source cell selected for deletion, and
blockwise realization removes every designated unit exactly once or earlier by a
favourable controller-entry deletion.

No abstract controller, label, line, or witness record is treated as payment unless a
specific marked source endpoint is attached to it.

## 1. Typed designated-credit records

A **cell-shadow credit record** is a tuple

```text
(z,{p,q},d),
```

where `z` is a fixed movement/refill candidate cell, `{p,q}` is a current source
blocker pair through `z`, and `d in {p,q}` is the marked source endpoint designated to
pay the incidence.

An **active-anchor credit record** is a tuple

```text
(e,A,B,p,d),
```

where `(e,A,B,p)` is a current active same-slot anchor incidence and `d` is either the
retained anchor `p` or one source endpoint of the active controller edge `e` selected
for deletion.

Multiplicity is retained: two records with the same marked endpoint but different
candidate cells, labels, controller edges, or anchor witnesses are distinct credit
units.

### Proposition PP3axa -- PROVED

Deleting the marked source cell `d` destroys its designated credit record unless the
candidate entry or active controller entry has disappeared earlier.  In the latter
case the chronological contribution is already nonpositive.

#### Proof

For a cell-shadow record, deleting `d` removes the blocker pair `{p,q}` from the fixed
candidate-cell count.  For an active-anchor record, deleting the anchor or controller
edge removes the active tuple.  Earlier candidate/controller deletion is favourable
by PP3aqu--PP3ara and PP3auz--PP3ava. ∎

## 2. Fixed-label blocker fibres attach source endpoints

A full fixed-label resource matching from PP3ald consists of records

```text
(e_j,{p_j,q_j}),
```

with distinct controllers, endpoint-disjoint blocker pairs, and no selected
controller equal to a selected blocker endpoint.

### Proposition PP3axb -- PROVED

After the layer refinement in PP3alf, choosing one common-layer endpoint

```text
d_j in {p_j,q_j}
```

for every retained record gives pairwise distinct current source cells.  Each
`d_j` carries one distinct cell-shadow credit record, and puncturing `d_j` as an
unrelated active controller does not remove that record.

#### Proof

Endpoint-disjointness gives distinct `d_j`.  Witness uniqueness PP3alc makes the
candidate entries distinct in the fixed-label fibre.  The designated candidate is
controlled by `e_j`, while `d_j` is disjoint from `e_j`; removing candidate entries
controlled by `d_j` therefore does not remove the record through the candidate
controlled by `e_j`. ∎

The transposed refill statement is identical.

## 3. Fixed-label anchor columns attach retained anchors

An endpoint-disjoint family from PP3alj consists of physical controller--anchor pairs

```text
(e_j,p_j).
```

### Proposition PP3axc -- PROVED

After retaining a common source layer for the anchors, the points `p_j` are pairwise
distinct current source cells, disjoint from all retained controller edges.  Marking
`p_j` gives one distinct active-anchor credit record per pair.  Puncturing `p_j` as an
unrelated controller elsewhere preserves the designated record controlled by `e_j`.

#### Proof

The family is endpoint-disjoint by construction.  Fixed-label physical-pair uniqueness
PP3ali prevents duplicate records.  The active same-slot tuple is controlled by
`e_j`, not by the unrelated controller role of `p_j`. ∎

A source-star alternative marks its repeated actual source centre and carries all
incident records with full multiplicity.

## 4. Fixed-macro defect cores attach blocker endpoints

The full resource matching in PP3alo--PP3alq has distinct typed labels, distinct
controllers, endpoint-disjoint blocker pairs, and no controller/blocker overlap.

### Proposition PP3axd -- PROVED

Choosing one blocker endpoint from a common source layer gives a pairwise distinct
marked source set carrying one cell-shadow credit unit per selected bad entry.  All
credit survives unrelated controller puncturing exactly as in PP3axb.

#### Proof

The source-resource conditions in PP3alo give endpoint distinctness and
controller/blocker disjointness.  Each selected entry has its own controller and typed
label, hence its own candidate cell.  Apply PP3axa. ∎

Thus every mass alternative in PP3aur--PP3aut refines to actual marked source cells,
not merely labels or controller records.

## 5. Truncation to the host scale

The extraction theorems may produce more than `W` credited endpoints.

### Proposition PP3axe -- PROVED

From any credited star or endpoint bank of size `H>=cW` for fixed `c>0`, one may retain
an arbitrary subfamily of size

```text
s=min(W,floor(cW/2))=Theta(W)
```

such that:

1. the marked source cells remain distinct whenever the original family was a bank;
2. every retained cell keeps its complete designated multiplicity; and
3. `1<=s<=W`, as required by PP3aud, PP3aue, and PP3awo.

#### Proof

All required properties are hereditary under taking a subfamily.  In a star, retain
the centre and any `s` designated incidences; in a bank, retain any `s` records. ∎

For a smaller current canonical structure arising inside one block, use its actual
size `1<=s<=W`; the scale-uniform host PP3awj--PP3awp applies.

## 6. Permanent-block partition and first deletion

Let `D` be the final marked source set and let `C` be its multiset of designated credit
records.  Partition

```text
D=D_1 dot-union ... dot-union D_k
```

by the permanent matching blocks, and process the nonempty blocks sequentially.

For a record `c in C`, let `j(c)` be the first processed block containing one of its
marked source endpoints or its marked active controller edge.

### Theorem PP3axf -- PROVED

Every designated credit record is removed at stage `j(c)` or has already disappeared
favourably.  Consequently the sum of blockwise removal terms plus favourable entry
deletions is at least the complete designated multiplicity `|C|`.

#### Proof

Before stage `j(c)`, none of the marked source resources assigned to the record has
been deleted.  At stage `j(c)`, PP3axa removes the record.  If a prior block changes or
punctures its active controller/candidate entry, the record disappears earlier with a
nonpositive chronological contribution.  Assign the record to its first such event.
Different records remain distinct even when assigned to the same source deletion,
because the potential counts candidate, label, and witness multiplicity. ∎

This includes cross-block blocker pairs and controller--anchor records: no layer or
block localization of the second endpoint is needed.

## 7. Source-valid host realization

### Theorem PP3axg -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

For every credited structure extracted by PP3alc--PP3aut, permanent-block refinement
has exactly one of the following outcomes.

1. Sequential pool-compatible cycles delete all marked source cells, create zero
   current insertion/activation cost, and decrease the current potential by at least
   the complete designated credit.
2. One block's scale-uniform support table produces a current canonical credited
   structure, which is paid directly.

#### Proof

Use PP3axb--PP3axe to obtain the marked source set and credit records.  Partition by
PP3avc.  Every block has its own quadratic helper reservoir; role-domain constraints
are handled by PP3awo.  Independent block cycles are source-valid and zero-cost by the
complete restart-support theorem.  The total removal bound is PP3axf.  A dense block
is converted by PP3awm and paid by PP3auc--PP3aui. ∎

No extraction theorem needs to know the eventual permanent block of a selected
endpoint.

## 8. Audit endpoint

### Corollary PP3axh -- PROVED

The designated-credit edge in the acyclic dependency audit is closed for:

1. fixed-label movement/refill blocker fibres;
2. fixed-label same-slot anchor rows and columns;
3. fixed-macro movement/refill defect cores;
4. repeated-centre source stars; and
5. resource-disjoint chronological endpoint banks.

Every unit used by the fixed-attempt theorem is attached to a current source cell,
survives the stated puncturing refinements, and is counted exactly once under
permanent-block realization.

The next assembly target is the formal consolidation of PP3avj, PP3awo, PP3aww, and
PP3axg into one exact-width prime-patching lemma with an explicit hypothesis list.

The no-three-in-line conjecture remains unproved.
