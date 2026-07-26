# Post-trade decomposition makes every saturated endpoint package layer-assignable

PP3asl--PP3ass process a first endpoint package after its inserted cells have been
assigned to current permutation layers.  The assignment was left as a hypothesis.
That hypothesis is automatic: one must decompose the **post-trade source**, not try
to inherit the layers of the deleted source cells.

Any source-admissible saturation-preserving trade ends at another two-regular
bipartite source graph.  Alternating every component gives two current permutation
layers, and every inserted cell belongs to exactly one of them.  This remains true
when a replacement cell combines a column whose deleted point came from one old
layer with a row whose deleted point came from the other old layer.

## 1. Post-trade layer decomposition

Let `S` be a saturated source on `[m]^2`, and let a source-admissible trade produce
another source

```text
S'= (S\R) union D
```

with exactly two points in every old row and old column.

### Proposition PP3ath -- PROVED

There is a decomposition

```text
S'=P'_0 dot-union P'_1
```

where `P'_0,P'_1` are perfect matchings of the old row--column bipartite graph.

#### Proof

The bipartite graph of `S'` is two-regular.  Every connected component is therefore
an even cycle.  Colour the edges alternately on every component.  Each row and each
column receives one edge of each colour, so each colour class is a perfect matching.
∎

This is PP3asl applied at the actual post-trade state.

## 2. Automatic assignment of inserted cells

Put

```text
D_a=D cap P'_a,
```

for `a in {0,1}`.

### Proposition PP3ati -- PROVED

The inserted set has the canonical partition

```text
D=D_0 dot-union D_1.
```

Every cell of `D_a` is tied to one current permutation layer in exactly the sense
required by PP3asp: its old column and old row are the matched coordinates of
`P'_a`.

#### Proof

The two colour classes partition all edges of `S'`, hence they partition `D subseteq
S'`.  Membership in the matching `P'_a` is precisely the required current-layer
assignment. ∎

No information about the deleted edge that supplied the column or row is used.

## 3. Cross-origin replacement cells are harmless

Suppose the pre-trade source had a fixed decomposition

```text
S=P_0 dot-union P_1.
```

A replacement cell may use a column freed by deleting an edge of `P_0` and a row
freed by deleting an edge of `P_1`, or conversely.

### Proposition PP3atj -- PROVED

Such a cross-origin cell still belongs to exactly one post-trade layer `P'_a` and is
processed by the corresponding layerwise second trade.  Cross-origin information
does not enter the removal identity PP3asn.

#### Proof

The first statement is PP3ati.  The proof of PP3asn assigns each first-step insertion
incidence to the first later trade deleting one of its inserted endpoints.  It uses
only membership in the current blocks `D_a`; it never uses the pre-trade colour of a
deleted coordinate. ∎

Thus old-layer ancestry is not a geometric or potential-theoretic invariant that
must be preserved.

## 4. Compatibility with sequential layer trades

Starting from `S'`, perform a permutation replacement inside `P'_0` that deletes
all of `D_0` while leaving `P'_1` fixed.  Then perform the analogous replacement
inside `P'_1`.

### Proposition PP3atk -- PROVED

Each layer trade preserves saturation.  After the first layer trade, every cell of
`D_1` remains in the unchanged matching `P'_1`, so the second layer trade is still
well-defined.

#### Proof

A tied permutation replacement preserves one point of the active matching in every
row and column and fixes the other matching, by PP3ia.  The first replacement does
not alter any edge of `P'_1`, hence it does not alter `D_1 subseteq P'_1`. ∎

The two post-trade layers therefore provide a stable sequential architecture for the
complete cancellation package.

## 5. Automatic saturated composite theorem

Let the first trade have insertion and removal terms `I_1,R_1`, and let `s=|D|<=W`.

### Theorem PP3atl -- PROVED / CONDITIONAL JOINT LOCAL NORMAL FORM

Assume:

1. the first trade is source-admissible and saturation-preserving;
2. every local restriction for the later layer trades has the joint finite rank-three
   normal form;
3. the standard layerwise helper reservoirs and selected-controller punctures are
   available as in PP3asy and PP3atf.

Then exactly one of the following occurs.

1. At most two zero-insertion-cost layer trades delete all of `D` and

   ```text
   Xi(S_final)-Xi(S_initial)<=-R_1.
   ```

2. One post-trade layer yields a canonical converted structure of size at least

   ```text
   max(|D_0|,|D_1|)>=s/2.
   ```

3. A genuinely global nonlocal condition or near-complete coordinate cover is
   exposed.

#### Proof

Use PP3ath--PP3ati to obtain the layer partition automatically.  Apply PP3asy and
PP3atf in each occupied layer.  If both layers supply zero-cost trades, PP3atk and
PP3asn--PP3aso give the displayed composite bound.  Otherwise the larger occupied
block has size at least `s/2` and supplies the converted structure. ∎

The layer-assignment hypothesis in PP3asq is therefore redundant.

## 6. Exact architecture closure

### Corollary PP3atm -- PROVED

Every source-admissible endpoint replacement trade that preserves two points in every
row and column is automatically a saturated two-layer replacement package at its
post-trade state.

The only packages outside this architecture are operations that:

1. do not preserve saturation at an intermediate state;
2. are not represented as deletion followed by insertion of source cells; or
3. require a genuinely global constraint not encoded by the current source and its
   bounded local support table.

#### Proof

The first sentence is PP3ath--PP3atl.  The listed operations fail one of the stated
hypotheses by definition. ∎

Canonical endpoint-permutation, alternating-cycle, star, petal, fan, chord-cycle and
macro endpoint trades all preserve saturation and therefore satisfy the automatic
assignment theorem whenever their first state is source-admissible.

## 7. Revised layer frontier

### Corollary PP3atn -- PROVED

Failure of assignability to the saturated two-layer architecture is no longer an
independent frontier for source-admissible saturation-preserving endpoint packages.
The remaining alternatives are:

1. a genuinely global condition outside the finite local normal form;
2. a near-complete global coordinate cover in one post-trade layer;
3. a construction that deliberately passes through a nonsaturated intermediate
   object; or
4. a branch whose allocation framework cannot supply the initial source-admissible
   endpoint trade.

The no-three-in-line conjecture remains unproved.
