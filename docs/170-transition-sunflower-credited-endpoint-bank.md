# Transition sunflowers yield credited endpoint banks

PP3zw--PP3zz convert a failed fixed-centre transition choice into a linear
sunflower of source-invalid transition certificates. The petals share only the
fixed captive centre. Their predecessor/middle endpoint resources and their
chosen retained-source witness resources are pairwise disjoint.

This chapter identifies the exact interface supplied by that sunflower. After
pigeonholing the source permutation layer and the controller status of the
witness anchors, one obtains either a large free endpoint bank or a large bank
inside one controller pool. At the slab-optimal exponents, either bank is much
larger than the marked-bank size required by PP3xp--PP3zd.

The conclusion is a localization statement, not a completed paid trade. Moving
a selected witness anchor removes its chosen transition certificate, but new
endpoint insertions can create source or `Xi` collateral. Those costs remain the
existing star/resource-bank conversion problem.

## 1. Witness-anchor layer extraction

Let

```text
(r_i,p_i,z_i),  1<=i<=H,
```

be a predecessor sunflower from PP3zy, with fixed centre `c`; the successor case
is transposed. Thus the typed resource sets

```text
R(r_i,p_i,z_i)
```

are pairwise disjoint. Write the saturated retained source as the disjoint union
of its two permutation layers.

### Proposition PP3aaa -- PROVED

There is a subfamily of at least

```text
ceil(H/2)
```

petals whose witness anchors all lie in one source permutation layer. In this
subfamily the witness anchors are pairwise distinct and use pairwise distinct old
rows and old columns.

#### Proof

Pigeonhole the two source permutation layers. Pairwise disjointness of the
resource sets includes the typed source rows and columns of the anchors, so the
retained anchors in the selected layer are row/column-disjoint. ∎

## 2. Exact free-or-one-pool pigeonhole

Fix the same-layer subfamily and let its size be `L`. A witness anchor is
**free** when it lies outside the selected controller pools. Otherwise it is
**captive** and belongs to exactly one of the `M` controller pools.

Let `f` be the number of free anchors and let `h_j` be the number in controller
pool `j`. Then

```text
L=f+sum_j h_j.
```

### Proposition PP3aab -- PROVED

The same-layer family contains either a free endpoint bank or a bank inside one
controller pool of size at least

```text
ceil(L/(M+1)).
```

#### Proof

The `M+1` classes are the free class and the `M` controller-pool classes. One
class has size at least the ceiling of their average. If it is the free class,
use those anchors. Otherwise use the anchors in the corresponding controller
pool. ∎

Combining PP3aaa and PP3aab gives a bank of size at least

```text
ceil(ceil(H/2)/(M+1)).
```

with one uniform endpoint-permutation interface.

## 3. Slab-optimal size comparison

For the transition sunflower supplied by PP3zy,

```text
H=Omega(N),
N=m^(19/20+o(1)),
M=m^(1/20+o(1)).
```

### Corollary PP3aac -- PROVED

The free-or-one-pool bank has size

```text
Omega(N/M)=m^(9/10-o(1)).
```

In particular it contains a subbank of the marked-bank target size

```text
W=m^(19/40+o(1)).
```

#### Proof

Apply PP3aaa--PP3aab and use

```text
N/M=m^(18/20+o(1))=m^(9/10+o(1)).
```

Since `9/10>19/40`, the extracted bank is asymptotically larger than `W`. ∎

Thus the loss from pigeonholing a controller pool is harmless at the current
exponents.

## 4. Exact certificate-removal credit

For every selected petal, retain the chosen source-invalid certificate

```text
z_i collinear with the two inserted cells of r_i->p_i->c.
```

The certificate is an incidence record; the same transition could have another
retained-source witness, so deleting `z_i` is not asserted to make that
transition source-valid by itself.

### Proposition PP3aad -- PROVED

Let `B` be any extracted free or one-pool subbank, and apply an endpoint
derangement to its witness anchors.

1. Saturation is preserved because the anchors lie in one permutation layer and
   use distinct rows and columns.
2. In the free case the fixed controller infrastructure is preserved.
3. In the one-pool case the move is pool-compatible and preserves the global
   candidate-cell universe used by the dynamic `Xi` potential.
4. Before replacement insertions are charged, at least `|B|` distinct chosen
   transition-certificate incidences are removed.

#### Proof

An endpoint permutation on row/column-disjoint points of one permutation layer
preserves every row and column degree. Free anchors are outside the controller
pools. Captive anchors selected by PP3aab all lie in one controller pool, so the
pool-compatible identity PP3ky applies.

A derangement moves every selected anchor. Petal resource-disjointness makes the
chosen anchor records distinct, and each moved `z_i` deletes its own selected
collinearity certificate. Summing gives `|B|` removed certificate incidences
before any insertion collateral is counted. ∎

This is exactly the credited endpoint-bank input: one certified removal unit per
selected endpoint, with all new source and `Xi` costs charged on the insertion
side.

## 5. Revised fixed-centre transition endpoint

### Corollary PP3aae -- PROVED

The transition alternative in the fixed captive-centre certificate has one of
the following forms.

1. **Paid clean-chain completion:** PP3zu gives a source-valid strict decrease.
2. **Weighted clean-chain concentration:** deterministic source cost,
   additional-arc source mass, or `Xi` cost reaches the clean-chain credit scale.
3. **Free credited endpoint bank:** a row/column-disjoint free bank of size at
   least `W` is available for the distinguished endpoint-trade machinery.
4. **One-pool credited endpoint bank:** a bank of size at least `W` lies in one
   controller pool and is available for marked filler dilution and the
   single-cycle dynamic-`Xi` machinery.

#### Proof

Use PP3zz. The clean-chain alternatives are unchanged. In either sunflower
alternative, apply PP3aaa--PP3aad and then restrict the resulting bank to size
`W`. ∎

Therefore a fixed-centre transition sunflower is no longer a separate support
object. It rejoins the existing paid source-star/resource-bank conversion
frontier. What remains is concentrated insertion collateral, a full-pool
`Xi`-weight threshold, or failure of the corresponding endpoint-trade host.

## 6. Finite diagnostic

The script

```text
scripts/check_transition_sunflower_bank.py
```

checks a finite sunflower instance, verifies pairwise noncentral resource
disjointness, performs the exact layer/controller-class pigeonhole, and confirms
the `ceil(L/(M+1))` bank bound. It verifies the combinatorial bookkeeping only;
it does not prove asymptotic source-validity or paid conversion.
