# Conditional Hall localization inside a binary resource star

PP3wx returns a Hall rectangle whenever a chosen centre cell of a binary resource
star cannot be completed. In the adaptively cleaned endpoint branch, the original
host is near-complete: its forbidden complement has small maximum degree. The
Hall rectangle must therefore be supplied almost entirely by the centre's partner
fibre.

This gives a sharp second-level dichotomy. A failed centre has either a
macroscopic partner rectangle or an almost-full partner row/column on a secondary
resource. If linearly many centre cells fail, the star contains either cubic
binary support or a large two-resource incidence pencil.

## 1. Near-complete conditional host

Retain the notation of PP3wv--PP3xc. Let `G=(L,R;E)` have `q` vertices on each
side, fix the starred left resource `v`, and assume

```text
Delta(complement G) <= d.
```

For an allowed centre cell `a=(v,r)`, suppose the conditional host `G_a` has no
perfect matching. Let `X_a,Y_a` be the Hall witness from PP3wx and put

```text
x=|X_a|,  y=|Y_a|,  s=min(x,y),  t=max(x,y).
```

Since the residual sides have size `q-1`, integer Hall deficiency gives

```text
x+y >= q.
```

### Proposition PP3xd -- PROVED

The partner fibre satisfies

```text
|P(a) cap (X_a x Y_a)| >= xy-d s = s(t-d).
```

#### Proof

PP3wx subtracts the cells already absent from `G`. Count those absent cells by the
smaller side of the rectangle. Each resource has complement degree at most `d`,
so at most `d s` original missing cells lie in the rectangle. ∎

## 2. Rectangle or secondary-resource fan

Fix a constant `0<alpha<1/2` and assume `d=o(q)`.

### Theorem PP3xe -- PROVED

Every failed centre cell `a` has one of the following forms.

1. **Macroscopic partner rectangle:**

   ```text
   x >= alpha q  and  y >= alpha q,
   ```

   and therefore

   ```text
   |P(a) cap (X_a x Y_a)|
   >= alpha^2 q^2-dq
   = (alpha^2-o(1))q^2.
   ```

2. **Secondary-resource fan:** one resource on the smaller Hall side is incident
   with at least

   ```text
   t-d >= (1-alpha)q-d
   ```

   partner cells from `P(a)`.

#### Proof

If both sides are at least `alpha q`, apply PP3xd directly.

Otherwise `s<alpha q`. Since `s+t>=q`, one has `t>(1-alpha)q`. Proposition PP3xd
puts at least `s(t-d)` partner cells in the Hall rectangle. Average these cells
over the `s` resources on the smaller side. One resource is incident with at
least `t-d` of them. ∎

The secondary resource is different from the starred resource `v` and from the
right endpoint of `a`, because every partner cell is compatible with `a`.

## 3. Quantitative lower bound for every failed centre

### Corollary PP3xf -- PROVED

If `d<=q/4`, then every failed centre cell satisfies

```text
|P(a)| >= q/4.
```

Consequently, if `G` has minimum degree at least `delta q` at the starred resource
and every allowed centre fails, then

```text
|B_v| >= (delta/4)q^2.
```

#### Proof

Use PP3xe with `alpha=1/4`. The macroscopic rectangle contains at least
`q^2/16-dq`, which is at least linear for sufficiently large `q`; the secondary
fan contains at least `3q/4-d>=q/2`. A uniform weaker bound `q/4` covers both
cases. Sum over at least `delta q` allowed centre cells, whose fibres partition
`B_v`. ∎

This gives a direct quantitative version of PP3xa in a near-complete host.

## 4. Many failed centres: cubic core or fan assignment

Let `A_fail` be a set of `h` failed centre cells, with `h>=beta q` for fixed
`beta>0`. Apply PP3xe to each centre.

### Proposition PP3xg -- PROVED

At least one of the following holds.

1. At least `beta q/2` centre fibres each contain
   `(alpha^2-o(1))q^2` partner cells. Hence

   ```text
   |B_v| = Omega(q^3).
   ```

2. At least `beta q/2` centres have a chosen secondary resource carrying
   `((1-alpha)-o(1))q` partners.

#### Proof

Pigeonhole the two alternatives of PP3xe over `A_fail`. In the first case the
fibres are disjoint as conflict classes because their centre cells differ, so the
partner counts add. ∎

The first alternative is stronger than the cubic support hypothesis PP3kt and
therefore returns immediately to its linear fan/resource-bank conclusion.

## 5. Secondary-resource repetition or spread

Assume the second alternative of PP3xg. Assign to each selected centre one
secondary resource supplied by PP3xe. Let `h_2` be the number of selected centres.

### Proposition PP3xh -- PROVED

For every integer `D>=1`, one of the following holds.

1. One secondary resource is assigned to at least `D` different centre cells.
2. At least `h_2/D` distinct secondary resources are assigned.

In both cases, every centre-secondary pair supports `Omega(q)` partner cells.

#### Proof

This is the elementary degree-or-support dichotomy for the assignment map from
centres to secondary resources. ∎

The first case is a two-resource pencil: the fixed starred resource and one
secondary resource jointly support many centre fibres. The second case is a
spread family of distinct secondary resources and can be matched or pigeonholed
against the centre cells.

## 6. Two-resource grid interpretation

Suppose the fixed starred resource is a left resource. A centre cell is
`a=(v,r_a)`.

- If the secondary resource is left, then `P(a)` contains almost a full row on a
  second left resource, across right resources excluding `r_a`.
- If the secondary resource is right, then `P(a)` contains almost a full column
  on a right resource distinct from `r_a`.

### Proposition PP3xi -- PROVED

After pigeonholing the side of the secondary resource, the repeated-secondary
alternative of PP3xh gives one fixed ordered pair of endpoint-resource types and
many centre cells whose partner fibres contain linear traces in the same
row/column pencil.

The spread-secondary alternative gives a growing matching of centre resources to
secondary resources unless a third resource is repeated polynomially often.

#### Proof

There are only two secondary-resource sides. In the spread case, greedily choose
centre-secondary pairs with distinct secondary resources; centre right endpoints
are already distinct because the centre cells share the fixed left resource.
Any failure of resource disjointness is repetition at another typed resource. ∎

## 7. Revised conditional-star endpoint

A binary resource star in a near-complete endpoint host now reduces to:

1. a successful sparse-fibre conditional completion;
2. a macroscopic partner rectangle;
3. a cubic binary support core;
4. a two-resource partner pencil;
5. a spread centre-secondary resource family;
6. source-invalid or paid collateral concentration.

An arbitrary weighted endpoint-resource star and an arbitrary family of failed
conditional hosts are no longer terminal objects.
