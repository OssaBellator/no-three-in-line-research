# Exact-certificate realization and lineage import

**Branch:** `research/geometric-cleaning`

GC2eb--GC2ef collapse every failed local rank inventory to one exact prospective rank-three
certificate with explicit weight.  The remaining issue is temporal: a prospective certificate is
not current payment until one legal local state actually creates its exact occurrence.

This note gives that final import.  Under an occurrence-faithful realization contract, the selected
certificate is installed as one tagged lineage.  A single exact lineage never suffers the half-loss
of a diffuse star: its full weight either survives current or is assigned to one unique first
destruction.  For a bank, the usual half-survival/half-payment split returns a current anchor load of
at least `3W/(2N^2)`.

## Exact-certificate realization model

Let `I` be a compatible family of bridge, chord or transversal witnesses.  For each `v in I`,
GC2ee selects one exact prospective rank-three certificate `Q_v` with weight `h_v>0`, together with
its ordered matching prescription and exact fixed completion.

Assume the **exact-certificate realization contract**:

1. the selected prescription has one declared allowed matching extension `m_v`;
2. executing `m_v` creates the exact physical occurrence `Q_v`;
3. the chosen local states for all `v in I` have a legal compatible product;
4. every cross-witness certificate effect is included in the complete product ledger;
5. aliases of the same exact physical occurrence are aggregated before weights are counted;
6. every newly created selected occurrence receives one exact lineage tag;
7. failure returns the least matching, product, occurrence, alias, lineage or context field.

Write `B` for the resulting alias-aggregated selected certificate bank and

`W_B=sum_(Q in B) h_Q`.

## GC2eg -- one exact certificate becomes one current lineage -- PROVED UNDER THE REALIZATION CONTRACT

For one selected exact certificate `Q` of weight `h_Q`, executing its declared matching extension
creates one current factor lineage of the same full weight `h_Q`.  The lineage tag records the birth
event and the exact physical signature of `Q`.

If the same symbolic signature disappears and is later recreated, the recreated occurrence is a new
lineage and does not revive the original tag.

### Proof

The matching prescription and fixed completion are the complete physical address of `Q`.  Items 1
and 2 of the contract say that the declared extension is legal and satisfies every required moved
and fixed cell.  Thus the exact occurrence is present after execution.  Item 6 tags that occurrence
once.  The lineage convention is exactly the occurrence-faithful convention of GC2ch. QED.

No probability factor remains after the exact extension is chosen.

## GC2eh -- compatible product installs the exact bank -- PROVED

If every selected witness satisfies the realization contract, the product of the chosen local
states installs every certificate in `B` simultaneously.  After alias aggregation, the total newly
created selected-lineage weight is exactly

`W_B`.

### Proof

Item 3 gives a legal product state.  Each coordinate state creates its selected exact occurrence by
GC2eg.  Item 4 prevents an omitted cross-effect from invalidating the simultaneous statement, and
item 5 counts a physical occurrence only once.  Summing the fixed occurrence weights gives `W_B`.
QED.

This statement installs the selected certificates; it does not assert that the product has negative
potential change.

## GC2ei -- full survival or unique first-destruction ledger -- PROVED

Fix any later checkpoint.  Partition the original selected lineages into:

- surviving lineages, of total weight `S_B`;
- lineages already destroyed for the first time, of total weight `P_B`.

Then

`W_B=S_B+P_B`.

Every paid lineage is assigned injectively to one exact later event--factor destruction incidence.
For one selected exact certificate of weight `h_Q`, exactly one of the two alternatives has full
weight `h_Q`; there is no fractional loss.

### Proof

Apply the exact cohort identity GC2ch to the cohort `B`.  Each original lineage either remains the
same current occurrence or has one unique first destruction.  For a one-element cohort the two
weights are therefore `h_Q,0` or `0,h_Q`. QED.

## GC2ej -- surviving exact certificates concentrate on one current cell -- PROVED

Suppose the surviving bank has weight `S_B>0`.  For a board cell `z`, let `L(z)` be the total weight
of surviving selected certificates containing `z`.  Then

`sum_z L(z)=3S_B`.

Consequently one physical cell satisfies

`L(z)>=3S_B/N^2`.

In particular, if `S_B>=W_B/2`, one current cell has surviving rank-three incidence at least

`3W_B/(2N^2)`.

### Proof

Every exact rank-three certificate contains three distinct board cells and contributes its full
weight once to each of them.  Double-count certificate--cell incidences to obtain the identity, then
apply weighted pigeonhole over the `N^2` board cells. QED.

The selected cell and every surviving certificate are current physical objects, so this output may
enter the existing current-anchor pair-codegree and GC4 star routers.

## GC2ek -- exact prospective-certificate continuation -- PROVED UNDER THE LINEAGE-CYCLE CONTRACT

For every compatible bank of exact certificates returned by GC2ee--GC2ef, one of the following
holds:

1. one exact matching extension or product-realization field fails;
2. the chosen product state installs the alias-aggregated bank `B` with weight `W_B`;
3. at a later checkpoint, first-destruction payment has weight at least `W_B/2`;
4. at that checkpoint, one current physical cell supports surviving exact-certificate incidence at
   least `3W_B/(2N^2)`;
5. or the intervening history is a tagged-only recycling segment, an outer reset, or a named lineage
   contract failure.

Under the fixed-universe lineage-cycle contract of GC2cl, tagged-only recurrence erases, descends or
spends finite exact tickets.  Thus installed exact prospective mass cannot disappear without full
first-destruction payment or current anchored structure.

### Proof

Use GC2eh to install the bank.  GC2ei gives `W_B=S_B+P_B`, so at least one summand is at least
`W_B/2`.  The paid branch is alternative 3.  In the surviving branch apply GC2ej.  The global tagged
potential and tagged-only classification are GC2cj--GC2cl.  All omitted hypotheses return the least
failed field by item 7 of the realization contract. QED.

For a one-certificate bank, alternatives 3 and 4 preserve the full exact weight before the optional
`3/N^2` anchor localization.

## Corrected GC frontier

The exact certificate produced by a failed local margin is now tied to an executable event and an
occurrence-faithful temporal ledger.  The remaining geometry is current anchored incidence from the
surviving branch, exact first-destruction chargeback, block-tuple overload recursion, high pair
codegree, tagged-only recycling beyond the declared finite contract, global-context causes and
local superregular resampling.

## Finite check

`scripts/verify_geometric_exact_certificate_lineage_import.py` samples exact rank-three lineage
banks, recreation identities, destruction checkpoints and compatible realization systems.  It
checks full one-lineage survival/payment, `W_B=S_B+P_B`, first-destruction exclusivity, the half-bank
router and the `3S_B/N^2` current-cell incidence bound.