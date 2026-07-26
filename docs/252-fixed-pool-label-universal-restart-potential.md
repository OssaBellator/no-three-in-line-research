# Fixed pool-label universal restart potential

The fixed-attempt theorem PP3auq--PP3auw leaves one comparability problem: after a
paid source repair, a new controller pairing could in principle change the active
same-slot anchor table even when the slab coordinates and numerical labels are
unchanged.

The correct invariant is larger than one active controller matching but much smaller
than the universe of all possible slab architectures.  Freeze the pool coordinate
sets and label sets once.  Count:

1. every excess blocker incidence through every movement/refill candidate cell; and
2. every latent same-slot anchor incidence for every possible pair
   `x in X_i`, `y in Y_i`.

The resulting potential is independent of the current pairing between `X_i` and
`Y_i`.  Pool-compatible endpoint permutations therefore preserve its universe
exactly.  Actual controller-aware allocation defects are subsets of this permanent
universe.

## 1. Fixed coordinate and label infrastructure

For each macro `i in [M]`, fix old-coordinate sets

```text
X_i,Y_i subseteq [m],
|X_i|=|Y_i|=R,
```

with all `X_i` pairwise disjoint and all `Y_i` pairwise disjoint.  Fix the complete
movement and refill label sets

```text
Aset,Bset subseteq {m+1,...,m+T}.
```

At every restart, the distinguished source layer contains a perfect matching

```text
E_i subseteq X_i x Y_i.
```

The pairing inside `X_i x Y_i` may change, but the coordinate sets and label sets do
not.

Let

```text
V_cell
=
union_i ({(x,A):x in X_i,A in Aset}
         union
         {(B,y):B in Bset,y in Y_i}).
```

For a saturated source `S`, let `b_S(z)` be the number of source blocker pairs through
`z`.  Define the fixed excess-cell potential

```text
Xi_cell(S)=sum_(z in V_cell) (b_S(z)-1).
```

By PP3kv, every summand is a nonnegative integer and is positive exactly when the
corresponding movement/refill candidate cell has a nonaxis blocker pair.

### Proposition PP3aux -- PROVED

`V_cell` and `Xi_cell` are independent of the current perfect matching between each
`X_i` and `Y_i`.

#### Proof

The movement cells depend only on `X_i` and `Aset`; the refill cells depend only on
`Y_i` and `Bset`.  For every saturated source there is exactly one axis blocker pair
through each candidate cell, so subtracting one remains valid after the pairing
changes.  This is PP3ku--PP3kw. ∎

## 2. Latent same-slot anchor universe

For a source point `p=(u,v)`, define

```text
lambda(p)
=
# {(i,x,y,A,B):
      x in X_i,
      y in Y_i,
      A in Aset,
      B in Bset,
      (A-v)(B-u)=(x-u)(y-v)>0}.
```

Put

```text
Lambda(S)=sum_(p in S) lambda(p).
```

This counts every same-slot anchor incidence for every *latent* pair `(x,y)` in the
fixed pool rectangle, not only for the pairs currently used by `E_i`.

### Proposition PP3auy -- PROVED

`Lambda` is a nonnegative integer depending only on the current source and the fixed
coordinate-label infrastructure.  It is independent of the current pool pairing.

For every current matching `E_i`, the complete actual same-slot anchor mass is at
most `Lambda(S)`.

#### Proof

The defining tuple set uses the full Cartesian product `X_i x Y_i`.  An actual
same-slot anchor incidence uses one current edge `(x,y) in E_i` and satisfies exactly
the displayed product equation PP3dv, so it is one of the latent tuples. ∎

The controller point itself never contributes as an anchor: for `p=(x,y)` the right
side is zero, while positivity is required.

## 3. Universal restart potential

Define

```text
Omega(S)=Xi_cell(S)+Lambda(S).
```

### Proposition PP3auz -- PROVED

`Omega` is a fixed nonnegative integer potential for every source state obtainable by
pool-compatible endpoint permutations.  It simultaneously dominates:

1. every movement/refill noncontroller blocker incidence used by the fixed allocation
   attempt; and
2. every same-slot retained-anchor incidence for every possible restart pairing.

#### Proof

The first assertion is PP3aux and the second is PP3auy.  Both summands are
nonnegative integer incidence counts on fixed universes. ∎

Thus changing the controller matching inside a pool does not introduce a new type of
entry outside `Omega`.

## 4. Exact dynamic identity

Let a source repair remove a set `D`, insert a set `A`, preserve saturation, and
preserve every coordinate set `X_i,Y_i`.  Put `F=S\D`.

For source points `p,q`, let

```text
omega(p,q)=# {z in V_cell:p,q,z collinear}.
```

Define

```text
C_cell(D)
=
sum_(d in D) sum_(p in F) omega(d,p)
+
sum_({d,e} subseteq D) omega(d,e),

I_cell(A)
=
sum_(a in A) sum_(p in F) omega(a,p)
+
sum_({a,b} subseteq A) omega(a,b),

C_anchor(D)=sum_(d in D) lambda(d),
I_anchor(A)=sum_(a in A) lambda(a).
```

### Theorem PP3ava -- PROVED

The repair satisfies the exact identity

```text
Omega(F union A)-Omega(S)
=
[I_cell(A)+I_anchor(A)]
-
[C_cell(D)+C_anchor(D)].
```

#### Proof

The `Xi_cell` identity is PP3kx because `V_cell` is fixed.  The anchor term is linear
in source points, so deleting `D` subtracts `C_anchor(D)` and inserting `A` adds
`I_anchor(A)`.  Add the two identities. ∎

No pairing-change correction appears.

## 5. Universal insertion support still has rank three

Consider a tied endpoint cycle with marked source cells alternating with ordinary
helpers.  Form one support hypergraph containing every positive event that would:

1. violate source validity or cell distinctness;
2. create a new `Xi_cell` incidence; or
3. insert a source point `a` with `lambda(a)>0`.

### Proposition PP3avb -- PROVED

Every event in this universal support table has nonempty ordinary-helper support of
rank at most three.

More precisely:

1. a latent-anchor insertion event has rank one;
2. a new candidate-cell blocker incidence has rank at most two; and
3. source-validity and all bounded endpoint conditions have rank at most three.

#### Proof

`Lambda` is linear, so a new latent-anchor incidence contains exactly one inserted
source cell.  `Xi_cell` is a pair potential, so a new incidence contains one or two
inserted source cells.  The no-three and bounded endpoint checklist is PP3atv--PP3atw.
Strict alternation gives one ordinary helper in every selected cell. ∎

Although the latent anchor universe is large, it creates no new support *type*; all
its positive events belong to one unary family.

## 6. Pool-compatible block decomposition

Keep one distinguished source matching layer in the form

```text
P=E_1 dot-union ... dot-union E_M dot-union E_*,
```

where each `E_i` is a perfect matching between `X_i` and `Y_i`, and let `Q` be the
complementary source matching layer.  For a marked set `D subseteq P union Q`, put

```text
D_i=D cap E_i,
D_*=D cap E_*,
D_Q=D cap Q.
```

### Proposition PP3avc -- PROVED

Process every nonempty block by a tied cycle using helpers from the same matching
block.  Then:

1. every `E_i` remains a perfect matching between the same `X_i,Y_i`;
2. `E_*` and `Q` remain perfect matchings on their original coordinate sets;
3. the source remains saturated;
4. different blocks may be processed sequentially; and
5. if the block sizes are `s_j`, then

```text
sum_j s_j^2 <= (sum_j s_j)^2.
```

#### Proof

A tied permutation within one matching block preserves its row and column sets and
fixes every other block.  The square inequality follows by expanding the square of
the total marked size. ∎

At the slab-optimal scale, each pool has size `R` while every target block has size at
most

```text
W=Theta(sqrt(R)).
```

Thus the pool itself supplies the critical `Theta(s_j^2)` helper volume; the
complement blocks have linear ambient size.

## 7. Universal pool-compatible paid conversion

Suppose a marked set `D`, `|D|<=W`, carries designated incidence credit `c(D)>0` in
`Omega`.  Credit may be distributed across different infrastructure blocks.

### Theorem PP3avd -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Exactly one of the following occurs.

1. Sequential pool-compatible cycles delete every cell of `D`, preserve all fixed
   coordinate and label infrastructure, and satisfy

   ```text
   Omega(S_final)-Omega(S_initial)<=-c(D).
   ```

2. One universal support table produces an `Omega(|D|)` canonical source star,
   matching, endpoint bank, transition sunflower, anchor bank, fixed-core petal bank,
   or `A_2/B_3/B_4` structure.

#### Proof

Apply the critical rank-three support theorem separately in each nonempty block,
using PP3avb and PP3avc.  In the independent branch, the block cycle has zero
universal insertion cost.  Assign every designated incidence to the first block cycle
that deletes one of its marked endpoints, exactly as in PP3asn and PP3aue.  The total
removal is at least `c(D)`, while all block insertion terms vanish, so PP3ava gives the
displayed decrease.

In a dense support branch, finite type refinement gives one of the canonical
structures already converted through PP3aug and PP3aqo--PP3aqt. ∎

The number of nonempty blocks may grow with `W`; only the total square helper volume
matters.  Bounded blocks consume `O(1)` padding each, hence `O(W)` total padding.

## 8. Fixed infrastructure endpoint

### Corollary PP3ave -- PROVED

All source repairs generated by the controller-aware allocation frontier may be
chosen pool-compatible with one permanently fixed collection

```text
(X_i,Y_i,Aset,Bset)_(i in [M]).
```

Actual blocker stars and banks carry `Xi_cell` credit.  Actual same-slot anchor stars
and banks carry `Lambda` credit because their active tuples belong to the latent
anchor universe.  Every canonical credited structure therefore enters PP3avd.

No pool or label restart is needed after a paid repair.

### Corollary PP3avf -- PROVED

Within the slab-optimal controller-aware architecture, the candidate universe can be
fixed once at the coordinate-label level even though controller pairings evolve.
Restart comparability reduces to ordinary monotonicity of the single nonnegative
integer `Omega`.

The no-three-in-line conjecture remains unproved.
