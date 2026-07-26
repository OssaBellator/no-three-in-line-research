# Buffered role-domain square-root helper host

The critical helper theorem PP3arr is stated for one common helper reservoir, while
PP3avy uses role-specific gap domains after target-line pruning.  The missing bridge is
a buffered independent set.  If every one of `s` roles forbids at most `kappa s`
helpers, then an independent helper set of size

```text
b=(kappa+1)s
```

contains at least `s` allowed helpers for every role.  Hall's condition is then
automatic.  Failure of the buffered independent set is still at the square-root
threshold and gives the same target-order dense support alternatives.

Throughout, `kappa` is a fixed constant and `s` tends to infinity.  Bounded `s` is
handled by the bounded complete-support theorem PP3aqh--PP3aqt.

## 1. Scale-uniform critical support counting

Let `K` be a simple hypergraph of rank at most three on a helper set `H` of size `N`.
Let `b>=3`.

### Proposition PP3awj -- PROVED

If `K` has no independent set of size `b`, then one of the following holds.

1. More than `N/2` helpers occur as singleton edges.
2. After deleting singleton-edge vertices, the rank-two part has at least

   ```text
   (n)_2/[2(b)_2]
   ```

   edges.
3. After deleting singleton-edge vertices, the rank-three part has at least

   ```text
   (n)_3/[2(b)_3]
   ```

   edges.

#### Proof

This is exactly PP3arr with its parameter called `b` instead of `s`.  The proof counts
`b`-subsets containing a rank-two or rank-three edge and is independent of the
prime-patching scale. ∎

Thus PP3arr was already scale-uniform; only the later notation specialized it to
`b=W`.

## 2. Buffered Hall assignment

Let the marked gaps or endpoint roles be indexed by `j in [s]`.  For each role let

```text
H_j subseteq H,
|H\H_j|<=kappa s.
```

Put

```text
b=ceil((kappa+1)s).
```

### Proposition PP3awk -- PROVED

If `U subseteq H` is an independent set of size at least `b`, then there are pairwise
distinct helpers

```text
h_j in U cap H_j,
qquad j in [s].
```

#### Proof

For every role,

```text
|U cap H_j|
>=|U|-|H\H_j|
>=b-kappa s
>=s.
```

For any nonempty set `J` of roles, the union of their allowed sets inside `U` contains
the allowed set of one role and therefore has size at least `s>=|J|`.  Hall's theorem
gives the required system of distinct representatives. ∎

Any support-free superset remains support-free after selecting the `s` assigned
helpers.

## 3. Dense alternatives retain target scale

Assume

```text
c_0 s^2<=N<=c_1 s^2
```

for fixed positive constants, and let `b=ceil((kappa+1)s)`.

### Proposition PP3awl -- PROVED

Failure of an independent `b`-set gives one of:

1. `Omega(N)=Omega(s^2)` singleton-forbidden helpers;
2. `Omega(s^2)` distinct rank-two supports;
3. `Omega(s^3)` distinct rank-three supports.

#### Proof

In the nonsingleton branches, `n>=N/2=Theta(s^2)`.  Proposition PP3awj gives

```text
|K_2|>=Omega(n^2/b^2)=Omega(s^2),
|K_3|>=Omega(n^3/b^3)=Omega(s^3),
```

because `b=Theta(s)`. ∎

### Proposition PP3awm -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Every dense alternative of PP3awl yields a canonical structure of order `Omega(s)`.

1. Singleton erosion gives, after finite type and role refinement, `Omega(s)` distinct
   unary or transition supports, or one heavier fixed role.
2. A rank-two graph with `Omega(s^2)` edges has a vertex of degree `Omega(s)` or a
   matching of size `Omega(s)`.
3. A rank-three family with `Omega(s^3)` edges has, by the recursive link theorem,
   a fixed core and `Omega(s)` pairwise disjoint residual petals.

These are exactly the source-star, transition, anchor-bank, endpoint-bank, arc-petal,
path-grid, partner-fan, or insertion-pencil classes already converted in
PP3ama--PP3aui.

#### Proof

The rank-two statement is the ordinary star--matching argument with threshold a small
constant multiple of `s`.  The rank-three statement is PP3ams, which supplies
`Omega(|K_3|^(1/3))=Omega(s)` petals after fixing a core.  Finite canonical-type
refinement loses only an absolute factor. ∎

This is the scale-adaptive form of PP3art required by PP3atz.

## 4. Trimming a larger pool

A permanent matching block may have size `R` much larger than `s^2`.

### Proposition PP3awn -- PROVED

Suppose a matching block contains at least `c_1 s^2` unreserved helpers.  Choose any
subreservoir `H` of size

```text
N=floor(c_1 s^2).
```

If every role forbids at most `kappa s` helpers in the full block, it forbids at most
`kappa s` helpers in `H`.  Therefore PP3awk--PP3awm apply inside `H`.

#### Proof

Restriction to a subset cannot increase any role's number of forbidden helpers.
The support hypergraph restricts to rank at most three.  Apply the preceding results. ∎

At the largest block scale `s=W` one may simply take `H` to be the full `R=Theta(W^2)`
pool.  The buffered set has size only `Theta(W)`, so it fits inside `H`.

## 5. Role-domain critical host theorem

### Theorem PP3awo -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

Let `s<=W` marked roles lie in one current matching block.  Assume:

1. the block has `Theta(max(s^2,1))` unreserved helper edges;
2. every role domain omits at most `kappa s` helpers for one fixed `kappa`;
3. all remaining positive source, insertion, transition, anchor, endpoint, and
   activation events form a simple helper-support hypergraph of rank at most three.

Then exactly one of the following occurs.

1. There is a role-respecting injective helper assignment whose selected helper set is
   independent in the complete support table.
2. The support table yields an `Omega(s)` canonical converted structure.

#### Proof

For bounded `s`, use PP3aqh--PP3aqt with finite padding.  For large `s`, trim to a
quadratic subreservoir by PP3awn and seek an independent buffered set of size
`b=ceil((kappa+1)s)`.  If it exists, PP3awk gives the role-respecting assignment.  If
not, PP3awl--PP3awm give item 2. ∎

The selected cycle uses only the final `s` assigned helpers; the larger buffered set is
an auxiliary certificate.

## 6. Repair of the activation-clearing interface

In PP3avw, `L=O(s)` target lines and the marked-edge exclusion remove at most

```text
2L+s<=kappa s
```

helpers from every cyclic gap, for a fixed constant `kappa` after finite role
refinement.

### Corollary PP3awp -- PROVED / CONDITIONAL EXISTING CONVERSION INTERFACES

The invocation of a "role-domain version" in PP3avy is justified by PP3awo.
Consequently target-line pruning followed by the current restart-support table gives
exactly:

1. a pool-compatible target-clean support-free clearing cycle; or
2. an `Omega(s)` current canonical credited structure.

The same theorem also supplies the scale-adaptive conversion step used in PP3atz and
PP3aud for every `1<=s<=W`.

#### Proof

Use the displayed domain-loss bound in PP3awo.  The complete restart-support rank is
at most three by PP3avb.  Apply PP3awo and then the existing current conversion and
direct-payment interfaces. ∎

## 7. Revised hypothesis audit

The first scale mismatch in the focused assembly is therefore closed:

- block refinement may produce any size `1<=s<=W`;
- a larger pool may be trimmed to `Theta(s^2)` helpers;
- role-specific line pruning costs only `O(s)` values per role;
- a buffered independent set supplies Hall automatically; and
- dense failure still returns an `Omega(s)` canonical object.

The next audit target is the exact preservation of designated credit and source-valid
marked endpoints when the extracted fixed-label or fixed-macro structures are refined
across permanent matching blocks.

The no-three-in-line conjecture remains unproved.
