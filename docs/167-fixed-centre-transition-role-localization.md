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
successor transition star. Witness localization then produces one retained source
anchor supporting a polynomial fixed-anchor transition fan.

## 1. Three transition relations at a fixed centre

Let `V` be the `N` tied endpoint indices of one controller pool and fix `c in V`.
For distinct indices, define three simple forbidden relations:

```text
L_c = {(r,p): r->p->c is source-invalid},
M_c = {(p,s): p->c->s is source-invalid},
F_c = {(s,t): c->s->t is source-invalid}.
```

For a middle choice `p`, let

```text
A_L(p)={r in V\{p,c}: (r,p) notin L_c}.
```

For a successor choice `s`, let

```text
A_F(s)={t in V\{s,c}: (s,t) notin F_c}.
```

A five-index chain

```text
r->p->c->s->t
```

is **locally transition-clean at `c`** when `(r,p) notin L_c`,
`(p,s) notin M_c`, and `(s,t) notin F_c`.

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
with `z` exactly when PP3jc gives

```text
(u-x_p)(v-y_s)=(u-x_c)(v-y_c).
```

For a nonzero right side, PP3jd gives at most `2D_m` ordered pairs `(p,s)` for
this anchor. For the zero-product case, at most two retained axis anchors occur
and each contributes at most `N` pairs. Sum over at most `2m` retained anchors;
counting distinct forbidden pairs rather than witnesses only decreases the result.
Finally `mD_m=m^(1+o(1))` and `N^2=m^(19/10+o(1))`. ∎

Thus the middle transition relation has vanishing density.

## 3. Local clean-chain criterion

Fix a parameter `eta=eta_N` with `eta->0` and `eta N->infinity`. Define

```text
P_eta={p: |A_L(p)|>=eta N},
S_eta={s: |A_F(s)|>=eta N}.
```

### Proposition PP3zk -- PROVED

If there are distinct `p in P_eta` and `s in S_eta` with

```text
(p,s) notin M_c,
```

then there are at least

```text
(eta N-2)(eta N-3)
```

ordered choices `(r,t)` for which

```text
r->p->c->s->t
```

is locally transition-clean and all five indices are distinct.

#### Proof

Choose `r in A_L(p)` avoiding `s`; this leaves at least `eta N-1` choices. For
each such `r`, choose `t in A_F(s)` avoiding `p` and `r`; this leaves at least
`eta N-2` choices. The displayed weaker product allows the endpoint exclusions
uniformly. ∎

Every such directed path is contained in a single-cycle permutation: contract the
path to one block and cyclically order it with the remaining indices.

## 4. Many clean chains or a role-star family

### Theorem PP3zl -- PROVED

Fix `rho>0`. Suppose

```text
|P_eta|>=rho N,
|S_eta|>=rho N,
```

and choose `eta` slowly enough that

```text
|M_c|=o(rho^2 N^2).
```

Then there are

```text
Omega(rho^2 eta^2 N^4)
```

locally transition-clean ordered chains through `c`.

#### Proof

Among the `|P_eta||S_eta|` ordered middle pairs, only `|M_c|=o(N^2)` are
forbidden. Excluding the diagonal still leaves `Omega(rho^2N^2)` clean pairs.
Apply PP3zk to each pair. ∎

The polynomial chain population is the correct input for a subsequent joint
source/paid thinning: one may average any nonnegative diagnostics over the chain
choices before completing the remaining single cycle.

### Corollary PP3zm -- PROVED

If no such polynomial clean-chain bank exists along a subsequence, then after
passing to a further subsequence at least one of the following holds.

1. **Predecessor-role star family:** all but `o(N)` choices of `p` satisfy

   ```text
   |{r: (r,p) in L_c}| >= (1-o(1))N.
   ```

2. **Successor-role star family:** all but `o(N)` choices of `s` satisfy

   ```text
   |{t: (s,t) in F_c}| >= (1-o(1))N.
   ```

#### Proof

By PP3zj the middle relation cannot cover a positive-density product
`P_eta x S_eta`. Hence one of `P_eta,S_eta` has size `o(N)`. Outside `P_eta`, a
middle `p` has fewer than `eta N` clean predecessors, so at least
`N-O(eta N)` predecessors are forbidden. The successor statement is transposed.
Let `eta->0` slowly. ∎

A fixed-centre transition core is therefore not diffuse across the three roles.

## 5. Witness uniqueness in one role star

Consider the predecessor-role family; the successor case is transposed. For every
forbidden transition `r->p->c`, choose one retained source anchor `z=(u,v)` on the
line through the inserted cells.

### Proposition PP3zn -- PROVED

Fix `p,c` and one retained anchor `z=(u,v)`.

1. If `v!=y_c`, then `z` witnesses at most one predecessor `r` in a transition
   `r->p->c`.
2. If `v=y_c`, then `z` can witness any predecessor only when `u=x_p`. Since the
   retained source contains at most one point in old row `y_c`, the axis case can
   occur for at most one middle index `p`.

#### Proof

The factorization for `r->p->c` is

```text
(u-x_r)(v-y_c)=(u-x_p)(v-y_p).
```

When `v!=y_c`, the equation determines `x_r`, and the endpoint pool has distinct
old columns. When `v=y_c`, the left side is zero. Since `p!=c` gives
`y_p!=y_c`, the right side vanishes only when `u=x_p`. The saturation statement
bounds the retained anchors on row `y_c`. ∎

Thus, except for one possible axis-heavy middle, a near-complete role star uses
linearly many distinct retained source anchors.

## 6. Fixed-anchor transition fan

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

distinct middle indices `p`.

At the slab-optimal scale this fan has size

```text
m^(9/10-o(1)).
```

The successor-role alternative gives the transposed fixed-anchor fan

```text
c -> s -> t_s.
```

#### Proof

There are `Omega(N)` middle indices, each with `Omega(N)` forbidden predecessors.
By PP3zn, their nonaxis witnesses are distinct for a fixed middle, so the number
of middle-anchor incidences is `Omega(N^2)`. There are at most `2m` retained
source anchors. Pigeonhole one anchor of degree `Omega(N^2/m)`. Since
`N=m^(19/20+o(1))`, the exponent is `19/10-1=9/10`. ∎

For the chosen anchor, the predecessor is determined from the middle by the exact
product correspondence

```text
(u-x_r)(v-y_c)=(u-x_p)(v-y_p).
```

The remaining transition obstruction is therefore one explicit fixed-anchor
algebraic fan, not a generic `N^2` transition table.

## 7. Revised fixed-centre transition endpoint

### Corollary PP3zp -- PROVED

The transition alternative in the nine-core certificate PP3zd reduces to one of:

1. a polynomial bank of locally clean five-index chain segments through the
   captive centre, available for joint source/paid thinning and single-cycle
   completion;
2. a predecessor-role fixed-anchor transition fan of size
   `Omega(N^2/m)`;
3. a successor-role fixed-anchor transition fan of the same size.

The middle-role transition core and an unstructured fixed-centre transition table
are no longer separate frontiers.
