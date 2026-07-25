# Fixed-centre transition-role localization

PP3zd leaves anchored-transition degree as one possible support core at a fixed
captive centre. Under the single-cycle state law, a transition is a forbidden
directed two-step path. A cycle containing the marked endpoint `c` uses
transitions in exactly three roles:

```text
r -> p -> c,      p -> c -> s,      c -> s -> t.
```

The middle role is much smaller than the generic transition population. The exact
factorization PP3jc and divisor bound PP3jd give only `O(mD_m+N)` middle-role
patterns at `c`, which is `o(N^2)` in a slab-optimal pool. Therefore failure to
choose a clean local Hamilton-chain segment forces a near-complete predecessor or
successor transition-star family. Witness localization supplies a polynomial
fixed-anchor algebraic fan inside that family; it does not by itself replace the
full role-star obstruction.

## 1. Three transition relations at a fixed centre

Let `V` be the `N` tied endpoint indices of one controller pool and fix `c in V`.
For distinct indices, define

```text
L_c={(r,p): r->p->c is source-invalid},
M_c={(p,s): p->c->s is source-invalid},
F_c={(s,t): c->s->t is source-invalid}.
```

For a middle choice `p`, put

```text
A_L(p)={r in V\{p,c}: (r,p) notin L_c}.
```

For a successor choice `s`, put

```text
A_F(s)={t in V\{s,c}: (s,t) notin F_c}.
```

A five-index chain

```text
r->p->c->s->t
```

is locally transition-clean at `c` when all three displayed two-step paths are
source-valid.

## 2. Middle-role divisor bound

### Proposition PP3zj -- PROVED

The number of forbidden middle-role pairs satisfies

```text
|M_c| <= 2mD_m+2N.
```

At the slab-optimal pool size

```text
N=m^(19/20+o(1)),
```

one has

```text
|M_c|=m^(1+o(1))=o(N^2).
```

#### Proof

Fix a retained source anchor `z=(u,v)`. The transition `p->c->s` is collinear
with `z` exactly when

```text
(u-x_p)(v-y_s)=(u-x_c)(v-y_c).
```

For a nonzero right side, PP3jd gives at most `2D_m` ordered pairs `(p,s)` for
this anchor. For the zero-product case, at most two retained axis anchors occur,
each contributing at most `N` pairs. Sum over at most `2m` retained anchors and
then forget witness multiplicity. Finally `mD_m=m^(1+o(1))`, whereas
`N^2=m^(19/10+o(1))`. ∎

Thus the middle transition relation has vanishing density.

## 3. Local clean-chain criterion

Fix `eta=eta_N` with `eta->0` and `eta N->infinity`. Define

```text
P_eta={p: |A_L(p)|>=eta N},
S_eta={s: |A_F(s)|>=eta N}.
```

### Proposition PP3zk -- PROVED

If there are distinct `p in P_eta` and `s in S_eta` with `(p,s) notin M_c`, then
there are at least

```text
(eta N-2)(eta N-3)
```

ordered choices `(r,t)` for which `r->p->c->s->t` is locally transition-clean and
all five indices are distinct.

#### Proof

Choose `r in A_L(p)` avoiding `s`, and then choose `t in A_F(s)` avoiding `p`
and `r`. The displayed weaker product absorbs all endpoint exclusions. ∎

Every such path is contained in a single-cycle permutation: contract the path to
one ordered block and cyclically arrange it with the remaining indices.

## 4. Many clean chains or a role-star family

### Theorem PP3zl -- PROVED

Fix `rho>0`. Suppose

```text
|P_eta|>=rho N,
|S_eta|>=rho N.
```

Then, for `eta` chosen slowly enough, there are

```text
Omega(rho^2 eta^2 N^4)
```

locally transition-clean ordered chains through `c`.

#### Proof

Among the `|P_eta||S_eta|` ordered middle pairs, only `|M_c|=o(N^2)` are
forbidden by PP3zj. Excluding the diagonal leaves `Omega(rho^2N^2)` clean pairs.
Apply PP3zk to each pair. ∎

This polynomial chain population is an averaging bank for subsequent source and
paid diagnostics before the remaining single-cycle completion is selected.

### Corollary PP3zm -- PROVED

If no such polynomial clean-chain bank exists along a subsequence, then after
passing to a further subsequence at least one of the following holds.

1. **Predecessor-role star family:** all but `o(N)` choices of `p` satisfy

   ```text
   |{r:(r,p) in L_c}| >= (1-o(1))N.
   ```

2. **Successor-role star family:** all but `o(N)` choices of `s` satisfy

   ```text
   |{t:(s,t) in F_c}| >= (1-o(1))N.
   ```

#### Proof

The middle relation cannot cover a positive-density product `P_eta x S_eta`, so
one of `P_eta,S_eta` has size `o(N)`. Outside the small set, fewer than `eta N`
clean choices remain in the corresponding outer role. Let `eta->0` slowly. ∎

A fixed-centre transition core is therefore not diffuse across its three roles.

## 5. Witness uniqueness inside one role star

Consider the predecessor-role family; the successor case is transposed. For every
forbidden transition `r->p->c`, choose one retained source anchor `z=(u,v)` on the
line through the two inserted cells.

### Proposition PP3zn -- PROVED

Fix `p,c` and one retained anchor `z=(u,v)`.

1. If `v!=y_c`, then `z` witnesses at most one predecessor `r`.
2. If `v=y_c`, then `z` can witness a predecessor only when `u=x_p`. Since the
   retained source contains at most one point in old row `y_c`, this axis case can
   occur for at most one middle index `p`.

#### Proof

The factorization for `r->p->c` is

```text
(u-x_r)(v-y_c)=(u-x_p)(v-y_p).
```

When `v!=y_c`, the equation determines `x_r`, and pool old columns are distinct.
When `v=y_c`, the left side is zero. Since `p!=c` gives `y_p!=y_c`, the right
side vanishes only when `u=x_p`. Saturation bounds the retained anchors on row
`y_c`. ∎

Except for one possible axis-heavy middle, every near-complete local star uses
linearly many distinct source-anchor witnesses.

## 6. A fixed-anchor fan inside the role star

### Theorem PP3zo -- PROVED

Under the predecessor-role alternative of PP3zm, after discarding the possible
axis-heavy middle there are `Omega(N^2)` distinct middle-anchor incidences
`(p,z)`. Consequently one retained source anchor `z` witnesses transitions

```text
r_p -> p -> c
```

for at least

```text
Omega(N^2/m)
```

distinct middle indices `p`. At the slab-optimal scale this is

```text
m^(9/10-o(1)).
```

The successor-role alternative contains the transposed fan `c->s->t_s`.

#### Proof

There are `Omega(N)` middle indices, each with `Omega(N)` forbidden predecessors.
By PP3zn their nonaxis witnesses are distinct for a fixed middle, so there are
`Omega(N^2)` middle-anchor incidences. Pigeonhole over at most `2m` retained
source anchors. ∎

For the selected anchor, the predecessor is determined from the middle by

```text
(u-x_r)(v-y_c)=(u-x_p)(v-y_p).
```

This fan is an explicit algebraic certificate contained in the role-star. The
other witness anchors remain part of the obstruction and must still be converted
or paid.

## 7. Revised fixed-centre transition endpoint

### Corollary PP3zp -- PROVED

The transition alternative in the nine-core certificate PP3zd reduces to one of:

1. a polynomial bank of locally clean five-index chain segments through the
   captive centre, available for joint source/paid thinning and single-cycle
   completion;
2. a near-complete predecessor-role transition-star family containing a
   fixed-anchor algebraic fan of size `Omega(N^2/m)`;
3. a near-complete successor-role transition-star family containing the
   transposed fixed-anchor fan.

The middle-role transition core and an unstructured three-role transition table
are no longer separate frontiers. The near-complete outer-role star itself remains
the exact unresolved transition object.
