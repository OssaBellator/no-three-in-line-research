# Conditional completion of a binary resource star

PP3wu leaves a weighted endpoint-resource star as one possible concentration of a
linear binary-shadow dual packing. A perfect matching uses exactly one cell
incident with a fixed endpoint resource. After that centre cell is fixed, only its
own partner fibre can create a conflict.

This conditioning closes every subquadratic resource star in a superregular host.
A genuinely hard star must instead have quadratic support, return a conditional
Hall family, or carry paid/source concentration.

## 1. Resource-star fibres

Let

```text
G=(L,R;E),  |L|=|R|=q,
```

and fix a left resource `v`. Let `B_v` be a family of binary conflicts touching
`v`. Each conflict has a unique cell incident with `v`, because its two cells are
compatible.

For every allowed centre cell `a=(v,r)`, define

```text
P(a)={b in E : {a,b} in B_v}.
```

Compatibility gives

```text
P(a) subseteq (L\{v}) x (R\{r}).
```

The fibres partition the star conflicts:

```text
|B_v| = sum_{a incident with v} |P(a)|.
```

### Proposition PP3wv -- PROVED

Let `M` be a perfect matching of `G`, and let `a` be its unique edge incident with
`v`. Then `M` avoids every conflict in `B_v` if and only if

```text
(M\{a}) cap P(a) = empty.
```

#### Proof

Only conflicts whose centre is the selected cell `a` can occur in `M`. Those are
exactly the pairs `{a,b}` with `b in P(a)`. ∎

## 2. Exact conditional hosts

For `a=(v,r)`, put

```text
G_a = G[L\{v},R\{r}] \ P(a).
```

### Theorem PP3ww -- PROVED

The host `G` has a perfect matching avoiding all conflicts in `B_v` if and only if
`G_a` has a perfect matching for at least one allowed centre cell `a`.

#### Proof

A perfect matching of `G_a`, together with `a`, is a perfect matching of `G` and
avoids `P(a)`, so PP3wv removes the entire star. Conversely, deleting the unique
edge at `v` from any star-avoiding perfect matching leaves a perfect matching of
the corresponding `G_a`. ∎

Thus a resource star is an exact family of conditional unary-deletion problems.

## 3. Conditional Hall certificates

If `G_a` has no perfect matching, Hall gives nonempty

```text
X_a subseteq L\{v},
Y_a subseteq R\{r}
```

with

```text
|X_a|+|Y_a|>q-1
```

and `X_a x Y_a` absent from `G_a`.

### Proposition PP3wx -- PROVED

Every failed centre cell has a Hall rectangle satisfying

```text
X_a x Y_a
subseteq
(E(complement G) cap (X_a x Y_a))
union
(P(a) cap (X_a x Y_a)).
```

Consequently

```text
|P(a) cap (X_a x Y_a)|
>= |X_a||Y_a|-|E(complement G) cap (X_a x Y_a)|.
```

#### Proof

The only cells additionally removed from the induced residual host are the cells
of `P(a)`. ∎

Failure for every centre therefore produces a family of explicit conditional Hall
rectangles.

## 4. Sparse fibres preserve superregularity

Fix constants `delta>0` and `epsilon>0`. Suppose `G` is
`(epsilon,delta)`-superregular and

```text
|P(a)| <= eta q,
```

where `eta=o(1)`.

### Proposition PP3wy -- PROVED FROM STANDARD REGULARITY ESTIMATES

For every fixed `epsilon'>epsilon`, the conditional host `G_a` is

```text
(epsilon',delta-o(1))-superregular
```

for sufficiently large `q`. In particular, it has a perfect matching.

#### Proof

Deleting the endpoints of `a` changes normalized degrees and densities by
`O(1/q)`. Deleting `P(a)` removes at most `eta q` edges at any vertex, so minimum
degree decreases by at most `eta q+1`.

For subsets `X,Y` of size at least `epsilon'(q-1)`, the total number of removed
fibre edges in `X x Y` is at most `eta q`; hence the density change is at most

```text
eta q/(|X||Y|) <= eta/(epsilon'^2 q)=o(1).
```

The inherited regularity discrepancy changes by `o(1)`. The standard perfect-
matching consequence of superregularity finishes. ∎

The stronger hypothesis `Delta(P(a))=o(q)` may be used instead, with the standard
slicing estimate.

## 5. Subquadratic stars have a sparse fibre

Let

```text
h_v=|B_v|.
```

A `(epsilon,delta)`-superregular host has at least `delta q` allowed centre cells
incident with `v`.

### Theorem PP3wz -- PROVED

Some allowed centre cell `a` satisfies

```text
|P(a)| <= h_v/(delta q).
```

Therefore, if

```text
h_v=o(q^2),
```

then one conditional fibre has size `o(q)`, and PP3wy--PP3ww give a perfect
matching avoiding the entire resource star.

#### Proof

Average the fibre-partition identity over the at least `delta q` allowed centre
cells. ∎

A polynomial weighted resource star with subquadratic support is thus not an
obstruction in the superregular branch.

## 6. Failure returns to the endpoint-cell fan

### Corollary PP3xa -- PROVED

If the resource star is not closed by PP3wz along a subsequence, then after passing
to a further subsequence there is a fixed `rho>0` such that

```text
h_v >= rho q^2.
```

Proposition PP3kr then gives one centre cell with at least `rho q` distinct
partners. PP3ks further gives either a partner-rich controller-candidate line or
polynomially many distinct controller candidates.

#### Proof

Failure of `h_v=o(q^2)` supplies the fixed positive lower density; apply PP3kr and
PP3ks. ∎

Thus conditional completion converts a weighted resource-star obstruction back to
the stronger unweighted fan geometry whenever the star is genuinely hard.

## 7. Paid source-valid conditional completion

Fix a centre cell `a`. Let `P_a,Q_a` count the remaining source-invalid pairs and
triples in `G_a`, and let `C_a` be the remaining non-star insertion cost of its
residual matching.

### Theorem PP3xb -- PROVED FROM SR1 AND THE PAID FIRST MOMENT

Assume `G_a` is superregular and the trade has guaranteed removal credit `R_a>0`.
For the spread constant `K`, if

```text
K^2 P_a/(q-1)^2
+ K^3 Q_a/(q-1)^3
+ E[C_a]/R_a
<1,
```

then adjoining `a` to a suitable residual perfect matching:

1. avoids every binary conflict touching `v`;
2. is source-admissible;
3. has insertion cost below `R_a`;
4. strictly decreases the paid potential.

#### Proof

Choose a spread perfect matching of `G_a`. The first two terms bound the expected
number of source-invalid patterns, and the last is normalized expected cost. A
first-moment choice has no source violation and cost below `R_a`. PP3wv removes
the star. ∎

## 8. Revised weighted resource-star endpoint

### Corollary PP3xc -- PROVED

A weighted binary endpoint-resource star in the superregular branch has one of:

1. a sparse conditional fibre and complete star avoidance;
2. a family of conditional Hall rectangles;
3. quadratic support, hence a linear endpoint-cell fan with PP3ks line/candidate
   structure;
4. source-invalid or paid collateral concentration.

The high-price binary core is therefore not blocked merely by a polynomial
resource star. The hard object is a quadratic fan, a conditional Hall family, or
paid/source concentration.
