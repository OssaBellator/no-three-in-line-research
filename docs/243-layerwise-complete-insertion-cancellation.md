# Layerwise complete insertion cancellation removes the common-layer hypothesis

PP3arx--PP3asd cancel the complete insertion table of a first endpoint trade when
all newly inserted cells lie in one current permutation layer.  A saturated source,
however, has two points in every old row and column and therefore decomposes into
two permutation layers.  The inserted set may be split between them.

The common-layer hypothesis is unnecessary.  Process the layer blocks one after
another.  Every first-step insertion incidence disappears when the first one of its
inserted endpoints is removed.  Zero-cost later layer trades never recreate it.
Thus the layerwise removal terms cover the complete first insertion table exactly
once, including all cross-layer incidences.

The helper demand is also additive: if the layer block sizes are `s_a`, then

```text
sum_a s_a^2 <= (sum_a s_a)^2.
```

Hence a target package of total size `W` needs at most square-root-critical total
helper volume `O(W^2)`, even when it is spread across both source layers.

## 1. Two permutation layers of a saturated source

View a saturated source `S subseteq [m]^2` as a bipartite graph from old columns to
old rows.  Every vertex has degree two.

### Proposition PP3asl -- PROVED

The source admits a decomposition

```text
S=P_0 dot-union P_1
```

where `P_0` and `P_1` are perfect matchings, hence permutation layers.

#### Proof

Every connected component of the bipartite source graph is an even cycle.  Colour
the edges of each cycle alternately with colours zero and one.  Every row and every
column receives exactly one edge of each colour, so each colour class is a perfect
matching. ∎

The decomposition need not be unique; any fixed alternating colouring is sufficient.

## 2. Layer partition of one inserted set

Let a first source-admissible endpoint trade replace old source cells by a newly
inserted set `D`.  Assume every member of `D` is assigned to one of the current
permutation layers in which its row/column replacement is tied.  Write

```text
D=D_0 dot-union D_1,
s_a=|D_a|,
s=s_0+s_1.
```

The same statements below hold for any fixed bounded number of layers.

### Proposition PP3asm -- PROVED

The square-root helper demands satisfy

```text
s_0^2+s_1^2 <= s^2.
```

More generally, for any partition `s=sum_a s_a`,

```text
sum_a s_a^2 <= s^2.
```

#### Proof

Expand `s^2`; all cross terms are nonnegative. ∎

Thus separate critical hosts of sizes `Theta(s_a^2)` consume total volume
`O(s^2)`.

## 3. Sequential deletion covers all first insertion incidences

Let the exact first-trade insertion and removal terms be `I_1,R_1`.  Starting from
the post-first-trade source, perform source-admissible second trades

```text
T_(2,0), T_(2,1)
```

where `T_(2,a)` deletes every cell of `D_a`.  Let their insertion and removal terms
be `I_(2,a),R_(2,a)` in the current active universe at that stage.

### Theorem PP3asn -- PROVED

One has

```text
R_(2,0)+R_(2,1) >= I_1.
```

This includes first-step incidences whose blocker pair or source witness uses cells
from both layers.

#### Proof

Every incidence counted by `I_1` contains at least one member of `D` by PP3arx.
Assign the incidence to the first layerwise trade that deletes one of its members.
Immediately before that trade the incidence is still active unless it has already
been removed by an earlier layer trade or by a favourable candidate-universe
deletion.  In the former case it was already counted in an earlier removal term; in
the latter case the universe deletion is an additional nonpositive contribution.
Otherwise the assigned trade destroys it and counts its full candidate-entry
multiplicity in its removal term.  Summing over incidences gives the inequality. ∎

No temporal coexistence or cross-layer independence is required.

## 4. Zero-cost layerwise cancellation

### Theorem PP3aso -- PROVED

If every layerwise second trade has zero insertion cost,

```text
I_(2,0)=I_(2,1)=0,
```

then the complete three-trade package satisfies

```text
Xi(S_final)-Xi(S_initial) <= -R_1.
```

#### Proof

Add the exact dynamic identities:

```text
Delta Xi
=
(I_1-R_1)
+
sum_a (I_(2,a)-R_(2,a)).
```

Use PP3asn and the zero-cost hypotheses. ∎

The theorem is stronger when puncturing deletes candidate entries between layer
trades, because candidate-universe shrinkage can only lower the chronological
potential.

## 5. Preparing each layer block

### Theorem PP3asp -- PROVED / CONDITIONAL JOINT LOCAL NORMAL FORM

Suppose each nonempty layer block `D_a` has an unreserved helper set of size
`Theta(max(s_a^2,1))` in its own permutation layer.  Then exactly one of the
following occurs for that block.

1. A joint-support-free source-valid layer cycle moves all of `D_a` with insertion
   cost zero.
2. An `Omega(s_a)` canonical star, matching, endpoint bank, transition sunflower,
   anchor bank, or fixed-core petal structure is extracted.
3. A genuinely global condition outside the finite rank-three local normal form
   prevents the layer trade.

For `s_a>=3`, apply PP3ase--PP3asj at scale `s_a`.  For `s_a<=2`, use the bounded
marked complete-support theorem PP3aqh--PP3aqt directly.

#### Proof

The rank-three counting argument PP3arr is scale-exact after replacing `W` by
`s_a`.  Bounded blocks are covered by the finite complete-support construction. ∎

## 6. Saturated two-layer composite theorem

### Theorem PP3asq -- PROVED / CONDITIONAL GLOBAL-NORMAL-FORM INTERFACE

Let a first endpoint replacement trade insert `s<=W` cells into a saturated source.
Assume:

1. every inserted cell is tied to one of the two permutation layers from PP3asl;
2. each occupied layer contains the required `Theta(max(s_a^2,1))` unreserved helper
   indices;
3. every actual source, transition, anchor, endpoint, and insertion restriction is
   represented by the joint finite local normal form.

Then exactly one of the following occurs.

1. A sequence of at most two zero-cost layerwise second trades moves every inserted
   cell and the complete package decreases `Xi` by at least `R_1`.
2. A canonical converted structure of size `Omega(max_a s_a)` is produced.  In
   particular, because there are two layers,

   ```text
   max(s_0,s_1) >= s/2.
   ```

3. A genuinely global nonlocal condition or a shortage of unreserved indices in one
   occupied layer is exposed.

#### Proof

Apply PP3asp to each occupied layer adaptively.  If both give zero-cost cycles, use
PP3aso.  Otherwise one layer gives a converted structure; the largest block has size
at least `s/2`. ∎

Thus a target package `s=Theta(W)` still gives a target-order structure in the
conversion branch.

## 7. Bounded-layer extension

### Corollary PP3asr -- PROVED

For a source decomposed into at most `k=O(1)` permutation layers, the same theorem
holds with at most `k` second trades and a converted structure of size at least
`s/k`.  The total critical helper volume remains at most `O(s^2)`.

#### Proof

Use the general inequality in PP3asm and repeat the proof of PP3asq. ∎

## 8. Revised co-layering frontier

### Corollary PP3ass -- PROVED

Failure of the entire marked set to lie in one permutation layer is no longer an
independent obstruction for saturated sources.  It reduces to:

1. a zero-cost sequence of at most two layerwise cycles;
2. a target-order canonical support structure in one layer;
3. absence of enough unreserved indices in an occupied layer;
4. a genuinely global restriction outside the finite local normal form;
5. an endpoint package that cannot be assigned to the fixed two-layer replacement
   architecture at all.

Cross-layer insertion incidences require no separate localization or payment.

The no-three-in-line conjecture remains unproved.
