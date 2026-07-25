# Two-sided transition pseudoforest product

PP3zw--PP3aac treat one bounded-choice outer role at a time. The predecessor and
successor relations can be combined more strongly.

Choose one injective predecessor design

```text
f(p) in A_L(p)
```

and one injective successor design

```text
g(s) in A_F(s).
```

For almost every ordered pair `(p,s)`, the five indices

```text
f(p), p, c, s, g(s)
```

are distinct. If the middle pair `(p,s)` is not forbidden, they form a locally
transition-clean five-index chain. Since the middle relation has only
`m^(1+o(1))` pairs, two large injectively designed outer state sets cannot coexist
without producing a clean chain.

The exact alternative is therefore:

- one outer two-valued family has a minimal theta/handcuff Hall core;
- a clean five-index chain exists;
- or one side has only `m^(1/2+o(1))` nonempty choices.

This is stronger than merely saying that one side has few choices of degree at
least three.

## 1. Nonempty bounded-choice state sets

Fix the captive centre `c`. Let `P` be a set of possible predecessor middles and
`S` a set of possible successor middles such that

```text
1 <= |A_L(p)| <= 2   for p in P,
1 <= |A_F(s)| <= 2   for s in S.
```

Every member of `A_L(p)` is distinct from `p,c`, and every member of `A_F(s)` is
distinct from `s,c`.

Assume both labelled choice multigraphs satisfy PP3zw. Choose injective designs

```text
f:P->V,
g:S->V.
```

Thus the values of `f` are pairwise distinct and the values of `g` are pairwise
distinct.

Let

```text
M_c={(p,s): p->c->s is source-invalid}
```

be the sparse middle-role relation of PP3zj.

## 2. Collision pairs between the two designs

Call `(p,s) in P x S` a collision pair when the five-index string

```text
f(p),p,c,s,g(s)
```

has a repeated index.

### Proposition PP3aad -- PROVED

The number of collision pairs is at most

```text
|P|+|S|+2 min(|P|,|S|)
<= 3(|P|+|S|).
```

#### Proof

The only possible equalities, besides those excluded inside the individual choice
sets, are

```text
p=s,
f(p)=s,
g(s)=p,
f(p)=g(s).
```

The first and fourth classes have size at most `min(|P|,|S|)`. Since `f` is
injective, for each `s` at most one `p` satisfies `f(p)=s`, giving at most `|S|`
pairs. Similarly `g(s)=p` contributes at most `|P|` pairs. Sum. ∎

## 3. Product bound in the absence of a clean chain

### Theorem PP3aae -- PROVED

If no locally transition-clean five-index chain

```text
r->p->c->s->t
```

exists with `p in P`, `s in S`, `r in A_L(p)`, and `t in A_F(s)`, then

```text
|P||S|
<= |M_c|+3(|P|+|S|).
```

#### Proof

Take a noncollision pair `(p,s)`. The outer transitions

```text
f(p)->p->c,
c->s->g(s)
```

are source-valid by the definitions of `A_L(p)` and `A_F(s)`. If `(p,s)` were not
in `M_c`, all three consecutive two-step transitions would be source-valid and
the five indices would be distinct, giving a clean chain. Therefore every
noncollision pair belongs to `M_c`. Apply PP3aad. ∎

This bound uses one design from each pseudoforest family; it does not require the
individual choice sets to have three options.

## 4. Slab-optimal collapse of one state side

Recall

```text
|M_c| <= 2mD_m+2N = m^(1+o(1)),
N=m^(19/20+o(1)).
```

### Corollary PP3aaf -- PROVED

If both two-valued choice families satisfy the pseudoforest criterion and no clean
five-index chain exists, then

```text
min(|P|,|S|)=O(m^(1/2+o(1))).
```

More quantitatively, if `|P|,|S|>=12`, then

```text
min(|P|,|S|)
<= 2 sqrt(|M_c|)+12.
```

#### Proof

Let `x=min(|P|,|S|)` and `y=max(|P|,|S|)`. If `y>=12`, then

```text
xy <= |M_c|+3(x+y)
```

implies, after moving the linear terms and splitting according to whether
`y<=2x` or `y>2x`, that `x=O(sqrt(|M_c|)+1)`. The displayed constant is a safe
uniform rearrangement. Insert the divisor bound for `M_c`. ∎

Thus absence of a clean chain collapses one complete nonempty local-state side to
square-root size. The stronger linear-size role-star from PP3zm cannot survive on
both sides once injective designs exist.

## 5. Combined Hall/chain/small-core trichotomy

### Corollary PP3aag -- PROVED

For the bounded-choice predecessor and successor relations at one captive centre,
at least one of the following holds.

1. **Predecessor bicyclic Hall core:** the predecessor family contains a minimal
   theta or handcuff obstruction from PP3zx.
2. **Successor bicyclic Hall core:** the transposed family contains such an
   obstruction.
3. **Clean chain:** there is a locally source-valid path

   ```text
   r->p->c->s->t
   ```

   available for the conditional paid single-cycle theorem PP3zu.
4. **Small predecessor state core:** only `m^(1/2+o(1))` predecessor middles have
   any safe outer choice.
5. **Small successor state core:** the transposed alternative.

The generic two-valued outer relations are therefore not terminal. The remaining
support objects are minimal bicyclic Hall cores or one square-root-sized local
state core at the captive centre.

## 6. Revised transition frontier

Combine PP3aag with PP3zu.

- A clean chain succeeds under the support-ranked paid average of PP3zu.
- Failure of either injective design is one explicit bicyclic Hall core.
- If both designs exist but no clean chain does, one side has only
  `m^(1/2+o(1))` nonempty local states.

The fixed-centre transition problem is now reduced to paid concentration on clean
chains, a theta/handcuff support core, or a square-root local-state core. The
near-complete role-star, diffuse middle relation, and generic two-valued table are
no longer separate frontiers.
