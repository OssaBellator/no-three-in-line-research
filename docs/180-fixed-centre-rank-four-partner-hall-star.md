# Rank-four partner support: robust Hall localization to a linear secondary-resource star

PP3acc--PP3ach reduce a fixed-centre rank-four binary `Xi` fibre to its
positive remote partner support. Sparse support is avoided by a conditioned
single-cycle first moment. If support avoidance is not certified, PP3acf gives a
square-root star or remote matching. That split is not yet sharp enough for the
matching interface.

The complete partner support is deleted from one conditioned residual endpoint
host. In a superregular host, a deletion graph of sublinear maximum degree
preserves superregularity and therefore preserves a spread perfect-matching law.
More generally, if deletion destroys every perfect matching, Hall's theorem and
lower regularity force one deleted endpoint resource to have linear degree.

Thus a fixed-cell remote matching is not an independent hard case. A genuine
rank-four matchability obstruction is a linear secondary-resource star, which is
exactly the repeated-resource pencil already handled by the conditional
binary-star, Hall, and two-resource-grid chain.

This chapter is a localization theorem. It does not pay residual source or
non-rank-four insertion cost.

## 1. A robust Hall deletion lemma

Let

```text
G=(L,R;E),  |L|=|R|=q,
```

be a bipartite endpoint host. Fix constants

```text
0<epsilon<delta<1.
```

Assume:

1. every vertex of `G` has degree at least `delta q`;
2. whenever `X subseteq L` and `Y subseteq R` satisfy

   ```text
   |X|,|Y| >= epsilon q,
   ```

   one has the lower-regularity estimate

   ```text
   e_G(X,Y) >= (delta-epsilon)|X||Y|.
   ```

Every `(epsilon,delta)`-superregular host has these two properties after the
usual harmless adjustment of constants.

Let `F subseteq E` be a deletion graph and put `H=G\F`.

### Theorem PP3aci -- PROVED

If `H` has no perfect matching, then

```text
Delta(F) >= epsilon(delta-epsilon) q.
```

#### Proof

Hall gives a nonempty `X subseteq L` with

```text
|N_H(X)|<|X|.
```

Put

```text
Y=R\N_H(X).
```

Then `|X|+|Y|>q`, and every allowed edge of `G[X,Y]` lies in `F`.

If `|X|<epsilon q`, every `x in X` has at most `|N_H(X)|<epsilon q`
possible neighbours outside `Y`. Hence

```text
d_F(x) >= delta q-epsilon q=(delta-epsilon)q.
```

If `|Y|<epsilon q`, then `q-|X|<|Y|<epsilon q`. Every `y in Y` has at
most `q-|X|<epsilon q` possible neighbours outside `X`, so again

```text
d_F(y) >= (delta-epsilon)q.
```

Otherwise both sets have size at least `epsilon q`. Lower regularity gives

```text
e_F(X,Y)
>=e_G(X,Y)
>=(delta-epsilon)|X||Y|.
```

Averaging over `X`, some `x in X` has deleted degree at least

```text
(delta-epsilon)|Y|
>=epsilon(delta-epsilon)q.
```

All cases prove the claim. ∎

This is stronger than a support-cardinality star--matching split: failure of
matchability forces a linear typed-resource star.

## 2. Low maximum degree preserves the conditioned host

Fix one source-admissible rank-four centre arc `a`, incoming or outgoing. Delete
the endpoints of `a` from the pool host and call the resulting balanced
conditioned host `G_a`, of side size `q=N-2`. Let `E_a` be the complete positive
remote partner support of the fixed rank-four fibre, and put

```text
H_a=G_a\E_a.
```

### Proposition PP3acj -- PROVED FROM PP3wy

Suppose `G_a` is `(epsilon,delta)`-superregular and

```text
Delta(E_a)=o(q).
```

Then, for every fixed `epsilon'>epsilon`,

```text
H_a
```

is `(epsilon',delta-o(1))`-superregular. In particular it has a perfect
matching, and a spread perfect-matching law is available on `H_a`.

#### Proof

This is the maximum-degree version of PP3wy. Removing `E_a` lowers every degree
by `o(q)` and changes every large-set density by `o(1)`. Standard slicing
preserves superregularity and its perfect-matching consequence. ∎

Every perfect matching of `H_a`, together with `a`, avoids the entire rank-four
fibre, irrespective of its weights.

## 3. Paid source-valid completion or a residual core

Let `P_a,Q_a` denote the remaining source-invalid pair and triple counts after
fixing `a` and deleting `E_a`. Let `C_a` be the remaining insertion cost and let
`R_a>0` be the guaranteed removal credit.

### Theorem PP3ack -- PROVED FROM PP3xb

Under the hypotheses of PP3acj, a source-valid strict decrease exists whenever

```text
K^2 P_a/q^2
+
K^3 Q_a/q^3
+
E[C_a]/R_a
<1,
```

after restoring the fixed spread constants.

#### Proof

Use a spread perfect matching of the superregular host `H_a`. The first two
terms bound the expected source-invalid count, and the last term is normalized
remaining paid cost. A first-moment outcome has no source violation and cost
below `R_a`. Since the matching lies in `H_a`, no positive-support remote partner
arc is selected, so the entire fixed rank-four fibre contributes zero. Apply
PP3kx. ∎

Negating this criterion gives residual source or non-rank-four paid
concentration; it does not restore a rank-four multiplicity core.

## 4. Hard rank-four fibres have a linear secondary resource

### Corollary PP3acl -- PROVED

Suppose the conditioned host `G_a` is `(epsilon,delta)`-superregular. Then at
least one of the following holds.

1. `H_a` is superregular and the paid source-valid criterion PP3ack succeeds.
2. `H_a` is matchable, but its spread/source/paid completion returns a residual
   alternating-host, source, or non-rank-four paid core.
3. `H_a` has no perfect matching, and one remote tail or head resource belongs to
   at least

   ```text
   epsilon(delta-epsilon)q
   ```

   positive-support partner arcs.

#### Proof

If `H_a` is superregular, use PP3ack or its negation. If it is matchable but not
in the superregular completion regime, use the alternating-component
factorization PP3tn--PP3vf and retain its explicit residual core. If it is
unmatchable, apply PP3aci with `F=E_a`. ∎

In alternative 3, every rank-four pattern contains:

```text
the fixed centre cell a,
one fixed remote tail or head resource,
one varying opposite remote resource.
```

This is a repeated secondary-resource binary pencil. It feeds the conditional
Hall and two-resource-choice-grid chain PP3xd--PP3xo.

## 5. Slab-optimal scale

Use

```text
N=m^(19/20+o(1)),
q=N-2,
W=m^(19/40+o(1)).
```

### Corollary PP3acm -- PROVED

For fixed superregular constants, the hard rank-four matchability branch contains
a secondary-resource star of size

```text
Omega(N)=m^(19/20+o(1)),
```

and hence a `W`-sized substar.

#### Proof

PP3acl gives a fixed positive constant times `q=N-2`. Since

```text
19/20 > 19/40,
```

the star is asymptotically larger than `W`. ∎

This improves the `Omega(N/sqrt(b))` square-root family of PP3acg to a linear
star whenever the complete partner-support deletion actually destroys
matchability.

## 6. Revised rank-four endpoint

### Corollary PP3acn -- PROVED

At a source-light captive centre in the superregular conditioned branch,
rank-four binary `Xi` weight reduces to one of:

1. complete avoidance of the positive partner support and a strict paid trade;
2. residual conditioned source or non-rank-four paid concentration;
3. a matchable non-superregular residual host, hence an alternating
   cycle-star/theta support core;
4. a linear repeated secondary-resource pencil, hence the conditional Hall,
   binary-cell-fan, and two-resource-choice-grid frontier.

Therefore fixed-cell remote matchings and square-root partner stars are no
longer independent rank-four frontiers. The rank-four branch rejoins already
listed residual collateral, alternating-host, conditional Hall, quadratic-fan,
and weighted choice-grid conversion problems.

## 7. Finite diagnostic

The script

```text
scripts/check_rank_four_partner_hall_star.py
```

checks a finite bipartite host and partner-support deletion. It verifies the
minimum-degree and lower-regularity hypotheses exactly, computes a maximum
matching of the residual host, and, on failure, extracts a Hall witness and
checks the linear deleted-degree conclusion of PP3aci. The stored example is a
complete host whose partner support deletes one full remote-resource star.
