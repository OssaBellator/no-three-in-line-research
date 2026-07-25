# Fixed-centre transition choice cores

PP3zj--PP3zp reduce a fixed-centre transition obstruction to a polynomial bank of
clean local Hamilton-chain segments or to a near-complete predecessor/successor
role-star family. The role-star can be sharpened further using only the sparse
middle relation.

If no clean five-index segment exists, the sets of middle choices having at least
three safe outer neighbours cannot both be large: every distinct pair between
those sets must belong to the middle forbidden relation `M_c`. Since
`|M_c|=O(mD_m+N)`, one outer role is two-valued outside only
`m^(1/2+o(1))` exceptional middles.

Thus the remaining transition support is a small high-choice core plus a
bounded-choice local state family. Whenever clean segments do exist, their local
choice and the remaining single-cycle completion admit the same joint paid
averaging used for two-resource grids.

## 1. Three-choice middle sets

Retain the notation of PP3zj--PP3zp. Define

```text
P_3={p: |A_L(p)|>=3},
S_3={s: |A_F(s)|>=3}.
```

Let `C_c` be the set of ordered five-tuples `(r,p,c,s,t)` of distinct indices
forming a locally transition-clean chain.

### Proposition PP3zq -- PROVED

If `C_c` is empty, then

```text
|P_3||S_3|-N <= |M_c|.
```

Consequently

```text
min(|P_3|,|S_3|) <= sqrt(|M_c|+N).
```

#### Proof

Take distinct `p in P_3` and `s in S_3`. If `(p,s) notin M_c`, Proposition PP3zk
with the constant threshold `3/N` supplies a clean choice of `r,t`, contrary to
`C_c=empty`. Hence every distinct pair in `P_3 x S_3` lies in `M_c`.

At most `N` pairs have `p=s`. Therefore

```text
|P_3||S_3|-N <= |M_c|.
```

The square-root bound follows. ∎

## 2. Slab-optimal exceptional-core size

### Corollary PP3zr -- PROVED

At

```text
N=m^(19/20+o(1)),
```

absence of a clean local chain implies

```text
min(|P_3|,|S_3|)=m^(1/2+o(1)).
```

More precisely the minimum is

```text
O(sqrt(mD_m+N))=m^(1/2+o(1)).
```

#### Proof

Insert PP3zj into PP3zq. Since `mD_m=m^(1+o(1))` dominates
`N=m^(19/20+o(1))`, its square root is `m^(1/2+o(1))`. ∎

This exceptional core is much smaller than the full pool size `N`.

## 3. Bounded-choice outer relation

### Proposition PP3zs -- PROVED

If `|P_3|=m^(1/2+o(1))`, then every `p outside P_3` has at most two safe
predecessors:

```text
|A_L(p)|<=2.
```

Thus the predecessor-safe relation outside the exceptional middle set has at most
`2N` edges. The transposed statement holds when `S_3` is the small set.

#### Proof

This is the definition of `P_3`, followed by summation over the remaining
middles. ∎

The support of a failed predecessor role is therefore the complement of an
explicit two-valued relation, apart from the small high-choice core. This is
strictly stronger than a generic near-complete transition star.

## 4. Exact extension of a clean local segment

Fix one clean segment

```text
h=(r,p,c,s,t) in C_c.
```

On a selected filler block containing these five indices, contract the directed
path

```text
r->p->c->s->t
```

to one ordered object.

### Proposition PP3zt -- PROVED

If the filler block has size `b>=5`, the number of single-cycle states containing
all four arcs of `h` is

```text
(b-5)!.
```

Conditional on `h`, every additional prescribed compatible rank-`u` arc forest
has probability at most

```text
1/(b-5)_u,
```

unless it creates a proper directed cycle, in which case its probability is zero.

#### Proof

After contracting the four-arc path, there are `b-4` cyclic objects. Their number
of directed cyclic orders is `(b-5)!`. Contract any additional compatible path
forest in the same way. Each additional prescribed arc reduces the object count
by one, giving the displayed ratio. A proper directed cycle cannot lie inside one
Hamilton cycle. ∎

Thus fixing a clean segment retains a fixed-rank spread law on the remaining
single-cycle completion, with `b` replaced by `b-4`.

## 5. Paid averaging over clean segments

For `h in C_c`, let:

- `P_h,Q_h` count all remaining source-invalid pair and triple patterns after the
  four local arcs are fixed;
- `J_h` be the remaining expected `Xi`-insertion cost under the conditional
  single-cycle completion;
- `R_h>=R_*>0` be the exact guaranteed removal credit.

### Theorem PP3zu -- PROVED

If `C_c` is nonempty and

```text
(1/|C_c|) sum_{h in C_c} [
  K^2 P_h/(b-4)^2
  + K^3 Q_h/(b-4)^3
  + J_h/R_*
] < 1,
```

then one clean local segment and one conditional single-cycle completion are
source-admissible and have insertion cost below removal credit. Hence they give a
strict pool-compatible decrease of `Xi`.

#### Proof

Choose `h` uniformly from `C_c`, then choose a uniform conditional single-cycle
completion. Proposition PP3zt supplies the fixed-rank cylinder estimates. The
displayed expression bounds the expected number of remaining source violations
plus normalized paid cost. An outcome below one has no source-invalid event and
cost below `R_*<=R_h`. Apply PP3kx. ∎

This converts the polynomial chain bank of PP3zl into an explicit paid-selection
interface.

## 6. Revised transition endpoint

### Corollary PP3zv -- PROVED

A fixed-centre transition core now has one of the following forms.

1. **Paid clean-chain bank:** `C_c` is large and satisfies the averaged source and
   paid criterion PP3zu.
2. **Weighted clean-chain concentration:** `C_c` is nonempty, but its averaged
   residual source or `Xi` cost reaches the removal-credit scale.
3. **Predecessor bounded-choice core:** outside at most `m^(1/2+o(1))` middle
   indices, every middle has at most two safe predecessors. The complementary
   forbidden role-star contains the fixed-anchor fan PP3zo.
4. **Successor bounded-choice core:** the transposed alternative.

The generic transition-degree core, the middle-role core, and a diffuse
near-complete role star are no longer independent frontiers. The unresolved
support object is a small high-choice core plus a two-valued outer relation, or
paid/source concentration on the clean-chain bank.
