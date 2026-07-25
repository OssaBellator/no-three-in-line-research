# Conditional Hall localization inside a binary resource star

PP3wx returns a Hall rectangle whenever a chosen centre cell of a binary resource
star cannot be completed. In the adaptively cleaned endpoint branch, the original
host is near-complete, so that rectangle must be supplied almost entirely by the
centre's partner fibre.

A failed centre therefore has either a macroscopic partner rectangle or an
almost-full partner row/column on a secondary resource. If linearly many centres
fail, the star contains either cubic binary support or a large two-resource
incidence family.

## 1. Near-complete conditional host

Retain PP3wv--PP3xc. Let `G=(L,R;E)` have `q` vertices on each side, fix a starred
left resource `v`, and assume

```text
Delta(complement G) <= d.
```

For an allowed centre `a=(v,r)`, suppose `G_a` has no perfect matching. Let
`X_a,Y_a` be the PP3wx Hall witness and put

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
|P(a) cap (X_a x Y_a)| >= xy-ds = s(t-d).
```

#### Proof

PP3wx subtracts the cells already absent from `G`. Counting those cells by the
smaller side gives at most `ds`, because the complement degree is at most `d`. ∎

## 2. Rectangle or secondary-resource fan

Fix `0<alpha<1/2` and assume `d=o(q)`.

### Theorem PP3xe -- PROVED

Every failed centre cell has one of the following forms.

1. **Macroscopic partner rectangle:**

   ```text
   x >= alpha q and y >= alpha q,
   ```

   with

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

The first case is PP3xd. Otherwise `s<alpha q`, so `t>(1-alpha)q`. PP3xd gives at
least `s(t-d)` partner cells; averaging over the `s` resources on the smaller side
produces one resource incident with at least `t-d`. ∎

The secondary resource differs from the starred resource and from the right
endpoint of the centre cell, because every partner is compatible with the centre.

## 3. Every failed centre has a linear fibre

### Corollary PP3xf -- PROVED

Under `d=o(q)`, every failed centre cell satisfies, for all sufficiently large
`q`,

```text
|P(a)| >= q/2.
```

Consequently, if the starred resource has degree at least `delta q` and every
allowed centre fails, then

```text
|B_v| >= (delta/2)q^2.
```

#### Proof

Apply PP3xe with `alpha=1/4`. In the macroscopic case the fibre contains
`(1/16-o(1))q^2`, which exceeds `q/2` for large `q`. In the secondary-fan case it
contains at least `3q/4-o(q)`, also at least `q/2`. Sum over at least `delta q`
allowed centres; the centre fibres partition `B_v`. ∎

This is a quantitative near-complete version of PP3xa.

## 4. Many failed centres: cubic core or fan assignment

Let `A_fail` contain `h>=beta q` failed centres. Apply PP3xe to every centre.

### Proposition PP3xg -- PROVED

At least one of the following holds.

1. At least `beta q/2` centre fibres each contain
   `(alpha^2-o(1))q^2` partner cells. Hence

   ```text
   |B_v|=Omega(q^3).
   ```

2. At least `beta q/2` centres have a chosen secondary resource carrying
   `((1-alpha)-o(1))q` partners.

#### Proof

Pigeonhole the alternatives of PP3xe. In the first case, fibres with different
centres are disjoint conflict classes, so their sizes add. ∎

The first alternative satisfies the cubic-support hypothesis PP3kt and returns to
its linear fan/resource-bank conclusion.

## 5. Secondary-resource repetition or spread

Assume alternative 2 of PP3xg and assign one secondary resource to each selected
centre. Let `h_2` be the number of centres.

### Proposition PP3xh -- PROVED

For every integer `D>=1`, one of the following holds.

1. One secondary resource is assigned to at least `D` centres.
2. At least `h_2/D` distinct secondary resources are assigned.

Every retained centre-secondary pair supports `Omega(q)` partner cells.

#### Proof

This is the degree-or-support dichotomy for the assignment map. ∎

The first case is a two-resource pencil. The second is a spread secondary-resource
family.

## 6. Resource extraction from the spread case

Suppose the starred resource is left and write each centre as `a=(v,r_a)`.
The centre right endpoints `r_a` are pairwise distinct.

### Proposition PP3xi -- PROVED

After pigeonholing the side of the secondary resource, the following holds.

1. If the secondary resources are left resources, distinct secondary resources
   already give centre-secondary supports disjoint outside the common starred
   resource `v`.
2. If the secondary resources are right resources, regard every assignment as an
   arc

   ```text
   r_a -> w_a
   ```

   on the right-resource set. Distinct centres give distinct tails and distinct
   assigned secondary resources give distinct heads. The underlying undirected
   graph has maximum degree at most two, and therefore contains a matching of size
   at least one third of the number of arcs.

Hence the spread alternative contains a constant-fraction family whose centre and
secondary resources are pairwise disjoint outside `v`.

#### Proof

The left-secondary statement is immediate. In the right-secondary case, each
right resource occurs at most once as a tail and at most once as a head, so the
underlying graph is a disjoint union of paths and cycles and has maximum degree at
most two. Every such graph has a matching of size at least one third of its edges.
∎

Each retained support still carries a linear partner trace. This is the correct
resource-normalized input for a subsequent pencil, matching, or paid-star trade.

## 7. Revised conditional-star endpoint

A binary resource star in a near-complete endpoint host reduces to:

1. successful sparse-fibre conditional completion;
2. a macroscopic partner rectangle;
3. a cubic binary support core;
4. a repeated two-resource partner pencil;
5. a spread centre-secondary family with a constant-fraction resource matching;
6. source-invalid or paid collateral concentration.

An arbitrary weighted resource star and an arbitrary family of failed conditional
hosts are no longer terminal objects.
