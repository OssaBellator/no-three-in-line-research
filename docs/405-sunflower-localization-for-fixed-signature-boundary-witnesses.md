# Sunflower localization for fixed-signature boundary witnesses

`docs/399` reduces a fixed-signature boundary-conflict packing to either a
heavily reused boundary role or a boundary-disjoint bank.  Repeating that
alternative informally suggests a common boundary core with disjoint petals.
This chapter makes that conclusion exact by applying the finite sunflower
lemma to the boundary sets of canonical witness paths.

The statements are general.  They do not yet convert the returned sunflower
into a valid prime-patching trade.

## 1. Boundary-set multiplicity

Fix a canonical conflict signature with `r` ordered boundary roles, where

```text
2<=r<=4.
```

For a canonical path `P`, let `B(P)` be its unordered set of boundary vertices.
Because the path is simple, `|B(P)|=r`.

### Proposition PP3bxd -- PROVED / FIXED-SIGNATURE SET MULTIPLICITY

Among canonical paths of one fixed signature, at most `r!` distinct ordered
role tuples have the same unordered boundary set.

Consequently, if every path weight is at most `L` and the total packing weight
is `Lambda`, then the number `N` of distinct boundary sets satisfies

```text
N>=Lambda/(r! L).
```

#### Proof

An unordered set of `r` distinct vertices has exactly `r!` orderings.  A fixed
signature and one ordered role tuple determine the canonical boundary part of
the witness path, so at most one canonical path uses that tuple.  Thus at most
`r!` paths share one boundary set.

Each such set therefore carries total weight at most `r! L`.  Covering total
weight `Lambda` requires at least `Lambda/(r!L)` distinct sets. ∎

The factorial loss is harmless here because `r<=4`.

## 2. A self-contained sunflower bound

A family of sets is a **sunflower** when every two members have the same
intersection.  That common intersection is the core; deleting it leaves
pairwise disjoint petals.

### Theorem PP3bxe -- PROVED / FINITE UNIFORM SUNFLOWER LEMMA

Let `F` be a family of distinct `r`-element sets.  For every integer `s>=2`,
if

```text
|F|>r! (s-1)^r,
```

then `F` contains a sunflower of size `s`.

Equivalently, every nonempty `F` contains a sunflower of size at least

```text
ceil((|F|/r!)^(1/r)).
```

#### Proof

Proceed by induction on `r`.  The case `r=1` is immediate.

Choose a maximal pairwise disjoint subfamily `M`.  If `|M|>=s`, it is a
sunflower with empty core.  Otherwise the union

```text
U=union_(A in M) A
```

has size at most `r(s-1)`.  Maximality says every member of `F` meets `U`.
Hence some `u in U` belongs to at least

```text
|F|/[r(s-1)]
```

members.  Removing `u` from all members that contain it gives a family of
distinct `(r-1)`-sets of size greater than

```text
r!(s-1)^r/[r(s-1)]
 =(r-1)!(s-1)^(r-1).
```

By induction these reduced sets contain a sunflower of size `s`.  Restoring
`u` adds it to the common core and preserves disjoint petals.

For the equivalent form, put

```text
s=ceil((|F|/r!)^(1/r)).
```

When `s>=2`, one has `s-1<(|F|/r!)^(1/r)`, so the strict hypothesis holds.
For `s=1` the claim is trivial. ∎

## 3. Fixed-signature boundary sunflowers

### Theorem PP3bxf -- PROVED / BOUNDED-CORE DISJOINT-PETAL WITNESS BANK

Let a fixed-signature packing have total weight `Lambda>0`, `r` boundary
roles, and maximum individual path weight at most `L`.  Then its canonical
paths contain a sunflower of size at least

```text
ceil((Lambda/((r!)^2 L))^(1/r)).
```

The sunflower has a boundary core `C` of size at most `r`; outside `C`, the
witness paths are pairwise boundary-disjoint.  If the sunflower has at least
two distinct members, then

```text
|C|<=r-1.
```

Using the fixed-signature packing from `PP3bwh`, every covering rotation with
exact recleaning cost `c_min>3` therefore supplies a boundary sunflower of
size at least

```text
ceil(((c_min-3)/(1530 (r!)^2 L))^(1/r)).
```

Uniformly over `r<=4`, the weaker but signature-free bound is

```text
ceil(((c_min-3)/(881280 L))^(1/4)),
```

because `1530*(4!)^2=881280`.

#### Proof

By `PP3bxd`, the family of distinct boundary sets has size at least

```text
Lambda/(r!L).
```

Apply `PP3bxe` to that `r`-uniform set family.  The guaranteed sunflower size
is at least

```text
ceil(((Lambda/(r!L))/r!)^(1/r)).
```

This is the displayed bound.  Distinct `r`-sets cannot have intersection of
size `r`, so a sunflower with at least two members has core size at most
`r-1`.

Finally `PP3bwh` gives one fixed signature with packing weight at least

```text
(c_min-3)/1530.
```

Substitute this value, and then use `r<=4` and `r!<=24` for the uniform
version. ∎

This absorbs both branches of `docs/399`: a repeated hub becomes part of the
sunflower core, while the remaining boundary roles form disjoint petals.

## 4. Revised recleaning frontier

Large exact recleaning cost now yields a bounded-core geometric object:

1. one of at most 510 signatures carries constant packing mass;
2. that signature has at most four boundary roles;
3. after a fourth-root worst-case loss, its canonical paths share one fixed
   boundary core and are disjoint outside that core.

The remaining conversion may classify the at most `2^4` possible core-role
patterns and work with disjoint petals.  No unbounded boundary intersection
pattern remains.

## 5. Finite diagnostic

The script

```bash
python scripts/check_fixed_signature_boundary_sunflowers.py
```

exhausts all uniform set families on a six-element ground set for the audited
small parameters and verifies the sunflower threshold and the weighted
boundary-set multiplicity calculation exactly.

The next theorem identifier after this chapter is `PP3bxg`.
