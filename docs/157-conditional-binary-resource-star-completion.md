# Conditional completion of a binary resource star

PP3wu leaves a weighted endpoint-resource star as one possible concentration of a
linear binary-shadow dual packing. A perfect matching, however, uses exactly one
cell incident with a fixed endpoint resource. Therefore a resource star is not a
simultaneous family of binary constraints: after the unique selected star cell is
fixed, only the partner set attached to that cell remains relevant.

This chapter makes that conditioning exact. In a superregular endpoint host, every
subquadratic resource star has a centre cell whose partner set has sublinear size.
Fixing that centre cell and deleting its partners preserves a spread residual
matching. Consequently a genuinely hard resource star must already have quadratic
support, where PP3kr supplies a linear endpoint-cell fan.

## 1. Resource-star fibres

Let

```text
G = (L,R;E),   |L|=|R|=q,
```

be an endpoint host, and let `v` be one fixed left resource. Let `B_v` be a family
of binary conflicts that touch `v`. Every conflict has a unique cell incident
with `v`, because its two cells are compatible.

For every centre cell

```text
a = (v,r) in E,
```

define its partner fibre

```text
P(a) = {b in E : {a,b} in B_v}.
```

Compatibility gives

```text
P(a) subseteq (L\{v}) x (R\{r}).
```

The fibres partition the star conflicts, so

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

Every conflict in `B_v` contains exactly one cell incident with `v`. Since `M`
contains exactly one such cell, namely `a`, the only star conflicts that can occur
inside `M` are the pairs `{a,b}` with `b in P(a)`. The claim follows. ∎

Thus the entire resource star becomes one conditional unary deletion after the
centre edge is chosen.

## 2. Exact conditional hosts

For `a=(v,r)`, define the residual host

```text
G_a = G[L\{v}, R\{r}] \ P(a).
```

### Theorem PP3ww -- PROVED

The host `G` has a perfect matching avoiding every conflict in `B_v` if and only
if at least one centre cell `a=(v,r)` belongs to a perfect matching of `G` and the
conditional host `G_a` has a perfect matching.

Equivalently, it is enough that one `G_a` has a perfect matching; adjoining `a`
then gives a perfect matching of `G` avoiding the entire resource star.

#### Proof

If `N` is a perfect matching of `G_a`, then `N union {a}` is a perfect matching of
`G`. It contains no partner of `a`, so PP3wv shows that it avoids `B_v`.

Conversely, let `M` avoid `B_v`, and let `a` be its unique edge at `v`. Then
`M\{a}` uses neither `v` nor `r`, and PP3wv says it avoids `P(a)`. Hence it is a
perfect matching of `G_a`. ∎

This is an exact decomposition, with no probabilistic hypothesis.

## 3. Conditional Hall certificates

Suppose `G_a` has no perfect matching. Since both of its sides have size `q-1`,
Hall gives nonempty sets

```text
X_a subseteq L\{v},
Y_a subseteq R\{r},
```

such that

```text
|X_a|+|Y_a| > q-1
```

and every cell of `X_a x Y_a` is absent from `G_a`.

### Proposition PP3wx -- PROVED

For every failed centre cell `a`, the Hall rectangle decomposes as

```text
X_a x Y_a
subseteq
(E(complement G) cap (X_a x Y_a)) union (P(a) cap (X_a x Y_a)).
```

Consequently

```text
|P(a) cap (X_a x Y_a)|
>= |X_a||Y_a| - |E(complement G) cap (X_a x Y_a)|.
```

#### Proof

The only additional cells removed when passing from the induced residual host to
`G_a` are the partner cells in `P(a)`. ∎

Thus failure for every centre edge produces a family of explicit conditional Hall
rectangles. In a dense host, most of each such rectangle must come from the
corresponding partner fibre.

## 4. Superregular preservation under a sparse fibre

Fix constants `delta>0` and `epsilon>0`. Let `G` be
`(epsilon,delta)`-superregular. Suppose

```text
|P(a)| <= eta q
```

for some `eta=o(1)`.

### Proposition PP3wy -- PROVED FROM STANDARD REGULARITY ESTIMATES

After deleting the endpoints of `a` and the fibre `P(a)`, the conditional host
`G_a` is

```text
(epsilon', delta-o(1))-superregular
```

for every fixed `epsilon'>epsilon`, provided `eta` is sufficiently small in terms
of `epsilon'-epsilon` and `delta`.

In particular, `G_a` has a perfect matching for all sufficiently large `q`.

#### Proof

Deleting one vertex from each side changes normalized degrees and densities by
`O(1/q)`. Deleting `P(a)` removes at most `eta q` edges in total, hence at most
`eta q` edges from any one vertex. Minimum degree therefore decreases by at most
`eta q+1`.

For subsets `X,Y` of size at least `epsilon'(q-1)`, at most `eta q` edges are
removed from `X x Y`, so the density change is at most

```text
eta q / (|X||Y|) <= eta/(epsilon'^2 q) = o(1).
```

The regularity discrepancy inherited from `G` changes only by the usual
`O(1/q)` vertex-deletion term. Thus the conditional host remains superregular
with the displayed parameters. A superregular balanced bipartite graph has a
perfect matching. ∎

The total-size hypothesis is stronger than necessary; maximum fibre-resource
degree `o(q)` gives the same conclusion by the usual slicing estimate.

## 5. Subquadratic stars have a sparse conditional fibre

Let

```text
h_v = |B_v|.
```

There are at most `q` centre cells incident with `v`.

### Theorem PP3wz -- PROVED

Some centre cell `a` satisfies

```text
|P(a)| <= h_v/q.
```

Hence if

```text
h_v = o(q^2),
```

then one conditional fibre has size `o(q)`. In a superregular host, PP3wy and
PP3ww give a perfect matching avoiding the entire resource star.

#### Proof

Average the identity

```text
h_v = sum_a |P(a)|
```

over the at most `q` centre cells. Empty fibres are allowed and are immediately
favourable. Apply PP3wy and PP3ww. ∎

Thus a polynomial weighted resource star of subquadratic support is not an
asymptotic obstruction in the superregular branch.

## 6. Quadratic support returns to the endpoint-cell fan

### Corollary PP3xa -- PROVED

Suppose the binary resource star at `v` is not closed by PP3wz along a subsequence.
Then there is a constant `rho>0` such that

```text
h_v >= rho q^2
```

along a further subsequence. Proposition PP3kr then gives one centre cell `a`
with at least `rho q` distinct binary-conflict partners.

That cell fan has the candidate-line dichotomy PP3ks: either one controller
candidate line contains a polynomial number of partners, or polynomially many
distinct controller candidates occur.

#### Proof

Failure of `h_v=o(q^2)` gives the displayed lower bound after passing to a
subsequence. Apply PP3kr and PP3ks. ∎

The weighted dual concentration has therefore been converted back to the stronger
unweighted fan geometry whenever conditional completion fails.

## 7. Paid and source-valid conditional completion

Fix a centre cell `a`. Let `P_a` and `Q_a` count the remaining source-invalid
pairs and triples in the conditional host, and let `C_a` denote any remaining
non-star insertion-shadow cost selected by its residual matching.

### Theorem PP3xb -- PROVED FROM SR1 AND THE PAID FIRST MOMENT

Assume `G_a` is superregular and has designated removal credit `R_a>0`. For the
spread perfect-matching constant `K`, if

```text
K^2 P_a/(q-1)^2
+ K^3 Q_a/(q-1)^3
+ E[C_a]/R_a
< 1,
```

then there is a residual perfect matching such that adjoining `a`:

1. avoids every binary conflict touching `v`;
2. is source-admissible;
3. has insertion cost below `R_a`;
4. strictly decreases the paid controller-shadow potential.

#### Proof

Choose a spread perfect matching of `G_a`. The first two terms bound the expected
number of source-invalid patterns. The final term is the normalized expected paid
cost. Their sum below one gives a source-valid residual matching with cost below
`R_a`. Proposition PP3wv removes the entire star, and the paid-potential identity
finishes. ∎

## 8. Revised weighted resource-star endpoint

### Corollary PP3xc -- PROVED

A weighted binary endpoint-resource star in the superregular branch has one of the
following forms.

1. **Conditional sparse-fibre completion:** one centre cell has `o(q)` partners,
   and the entire star is avoided by fixing that cell and completing the residual
   matching.
2. **Conditional Hall concentration:** every viable centre cell returns a Hall
   rectangle whose missing mass is concentrated in its partner fibre or in the
   original host complement.
3. **Quadratic cell-fan concentration:** the star has `Omega(q^2)` supported
   conflicts, hence one centre cell has `Omega(q)` partners and the candidate-line
   structure PP3ks.
4. **Paid collateral concentration:** a source-invalid or non-star insertion cost
   consumes the available conditional removal credit.

Therefore the high-price binary resource core is no longer blocked merely by a
resource star of polynomial size. The genuinely hard star has quadratic support,
a conditional Hall family, or paid/source concentration.
