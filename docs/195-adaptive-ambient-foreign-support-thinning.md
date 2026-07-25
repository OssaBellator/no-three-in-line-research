# Adaptive ambient thinning localizes foreign shadow support

The recapture-free endpoint PP3afu--PP3afz leaves a purely foreign unary or
binary support core on the selected `q`-bank.  That core may be tested before
the two-scale thinning.

A foreign unary support cell has two endpoint indices.  A binary support event
has endpoint-index rank two, three, or four.  Conditional on retaining one
incident endpoint index, a rank-`h` support survives a uniform `q`-subbank with
the exact factor

```text
(q-1)_(h-1)/(Q-1)_(h-1).
```

Therefore vanishing ambient support density remains locally sparse after an
adaptive thinning.  The rank-four term has one extra factor `q`, so choose the
subbank size slowly enough that its ambient density times `q` still tends to
zero.  This choice is compatible with source regularization and the
`q^3/Q=o(1)` self-recapture condition.

After deleting `o(q)` exceptional indices, the recapture-free zero-cost theorem
applies.  Persistent foreign support failure must consequently be a
positive-density ambient unary, rank-three binary, or rank-four binary
fixed-resource star.

## 1. Ambient support degrees

Let the full credited bank have endpoint-index set `[Q]`.

For one typed endpoint resource `v`, let

```text
Delta_1(v)
```

be its degree in the foreign unary support.

For `h=2,3,4`, let

```text
Delta_h(v)
```

be the number of foreign binary support events of endpoint-index rank `h`
incident with `v`.  Put

```text
Delta_h=max_v Delta_h(v).
```

A rank-`h` event incident with `v` uses `h-1` additional endpoint indices.

## 2. Exact conditional survival

Choose a uniform `q`-subset `I` of `[Q]`.  For a retained resource `v` whose
underlying endpoint index lies in `I`, let `d_h^I(v)` be its selected support
degree of rank `h`.

### Proposition PP3aga -- PROVED

Conditional on retaining the index of `v`,

```text
E d_1^I(v)
=
Delta_1(v) (q-1)/(Q-1),
```

and for `h=2,3,4`,

```text
E d_h^I(v)
=
Delta_h(v) (q-1)_(h-1)/(Q-1)_(h-1).
```

The equalities hold when every support has exactly the displayed endpoint-index
rank and is counted once.

#### Proof

After conditioning on the endpoint index of `v`, each incident support survives
exactly when its other `h-1` distinct indices belong to the remaining uniform
`q-1` subset.  The hypergeometric probability is the displayed falling-
factorial ratio.  The unary case is `h=2` with a one-cell support family. ∎

## 3. Adaptive subbank size

Define ambient normalized degrees

```text
epsilon_1=Delta_1/Q,
epsilon_3=Delta_3/Q^2,
epsilon_4=Delta_4/Q^3.
```

Rank-two binary support satisfies `Delta_2=O(Q)` automatically.

### Proposition PP3agb -- PROVED

Assume

```text
epsilon_1->0,
epsilon_3->0,
epsilon_4->0.
```

There is a sequence `q=q_Q` such that

```text
q->infinity,
q^3/Q->0,
epsilon_4 q->0,
```

and `q` may be chosen below every previously imposed polynomial upper scale.

#### Proof

Choose `q` tending to infinity more slowly than

```text
Q^(1/4)
```

and

```text
epsilon_4^(-1/2)
```

whenever `epsilon_4>0`.  Also take the minimum with all earlier admissible
upper scales.  Then `q^3/Q->0` and `epsilon_4 q->0`. ∎

Smaller `q` only improves the source-thinning estimates PP3jl--PP3jn.

## 4. Deleting support-degree exceptions

Use the adaptive `q` of PP3agb.  Conditional expectations from PP3aga give

```text
E d_1^I(v) <= (1+o(1)) epsilon_1 q,
E d_2^I(v) = O(q),
E d_3^I(v) <= (1+o(1)) epsilon_3 q^2,
E d_4^I(v) <= (1+o(1)) epsilon_4 q^3.
```

### Theorem PP3agc -- PROVED

With probability `1-o(1)`, after deleting `o(q)` endpoint indices from the
random subbank, every remaining typed resource satisfies

```text
d_1=o(q)
```

and

```text
d_2+d_3+d_4=o(q^2).
```

#### Proof

For unary support, declare a retained resource exceptional when

```text
d_1^I(v)>sqrt(epsilon_1) q.
```

Proposition PP3aga and Markov show that an `o(1)` fraction of retained resources
is exceptional.

For rank three use threshold

```text
sqrt(epsilon_3) q^2.
```

For rank four use

```text
sqrt(epsilon_4 q) q^2.
```

The corresponding exceptional probabilities tend to zero because
`epsilon_3->0` and `epsilon_4 q->0`.

Rank-two binary degree is at most the number of possible partner indices times
a fixed typed multiplicity, hence `O(q)=o(q^2)` without deletion.  Delete every
endpoint index having either typed resource exceptional.  Only `o(q)` indices
are removed, and all support degrees can only decrease. ∎

## 5. Joint recapture-free source-valid selection

### Corollary PP3agd -- PROVED

Under the hypotheses of PP3agb, one may choose a retained subbank of size
`(1-o(1))q` satisfying simultaneously:

1. the source-validity regularization PP3jl--PP3jn;
2. zero selected credit-line self-recapture PP3afp;
3. foreign unary degree `o(q)`;
4. foreign binary degree `o(q^2)`;
5. positive removal credit on every retained endpoint.

#### Proof

The self-recapture failure probability is `O(q^3/Q)=o(1)`.  The support-degree
exceptional set is `o(q)` with probability `1-o(1)` by PP3agc.  The source
thinning objective is `o(1)` and may be imposed by Markov.  Intersect the good
events, then delete the exceptional endpoint indices.  Deletion preserves all
other properties and the retained chosen credits. ∎

## 6. Paid completion or ambient density core

### Theorem PP3age -- PROVED

Suppose the source and endpoint host hypotheses hold.  Then at least one of the
following occurs.

1. A recapture-free source-admissible endpoint permutation has zero insertion
   shadow and strictly decreases `Xi`.
2. Along a subsequence,

   ```text
   Delta_1=Omega(Q).
   ```

3. Along a subsequence,

   ```text
   Delta_3=Omega(Q^2).
   ```

4. Along a subsequence,

   ```text
   Delta_4=Omega(Q^3).
   ```

#### Proof

If all three normalized ambient degrees tend to zero, apply PP3agd and then
the zero-cost endpoint PP3afv.  Negating this gives a subsequence on which one
normalized degree is bounded below by a positive constant. ∎

Rank-two binary support cannot obstruct this adaptive thinning by itself.

## 7. Structural interpretation

### Corollary PP3agf -- PROVED

Every non-paid alternative in PP3age is a positive-density fixed-resource
support star on the ambient credited bank:

1. a linear foreign unary fibre;
2. a quadratic rank-three binary star;
3. a cubic rank-four binary star.

The unary alternative feeds witness-star/resource-bank extraction.  The binary
alternatives feed fixed-cell fans, conditional Hall, two-resource grids, or
alternating-host localization.

#### Proof

The definitions of the ambient maximum degrees give the stated star sizes.
Apply PP3wc--PP3wh, PP3wv--PP3xc, and PP3afh--PP3afm according to support rank
and host type. ∎

## 8. Revised foreign-collateral endpoint

### Corollary PP3agg -- PROVED

Diffuse foreign insertion support is no longer an independent paid
resource-bank obstruction.  Adaptive ambient thinning absorbs every support
family satisfying

```text
Delta_1=o(Q),
Delta_3=o(Q^2),
Delta_4=o(Q^3).
```

The remaining foreign-collateral objects are positive-density ambient unary or
binary resource stars, source/host failure, or local multiplicity at the
credit scale after conditioning on a fixed fan centre.

## 9. Finite diagnostic

The script

```text
scripts/check_ambient_foreign_support_thinning.py
```

enumerates uniform subbanks, verifies the exact conditional survival factors
for unary and rank-two through rank-four binary supports, and reports the best
selected support degrees.
