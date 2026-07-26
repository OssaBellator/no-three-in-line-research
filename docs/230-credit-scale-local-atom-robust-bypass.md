# Credit-scale local atoms are absorbed in the robust branch

PP3aor--PP3aox reduce every explicit petal endpoint to at most ten local
`A_2`, `B_3`, and `B_4` insertion atoms.  This is the correct endpoint for a
one-step monotone `Xi` argument, but it is still too fine for robust final
allocation.

Binary insertion multiplicity is invisible at the controller-domain scale: a
source-valid state with `s` inserted endpoint cells uses only the
`binom(s,2)` secant lines determined by those cells.  Unary multiplicity on one
fixed inserted cell is also simple support.  Consequently a local atom whose
weight is comparable with a small marked removal credit is absorbed whenever
that credit is `o(R)`.  Only controller-domain-scale unary support can survive.

This chapter separates the robust and monotone frontiers.  In the robust branch,
credit-scale local atoms disappear.  The surviving one-step problem is confined
to branches without a fixed positive controller-domain margin.

## 1. Binary local atoms depend only on the inserted state size

Let a source-valid endpoint state insert a set `P` of size `s`.  Give every
selected `B_3` and `B_4` atom arbitrary nonnegative multiplicity.

### Proposition PP3aoy -- PROVED

For every macro `i` and final label pair `(A,B)`, the complete binary local table
removes at most

```text
s(s-1)
```

values from the paired controller domain.

#### Proof

Every selected binary atom is supported on one unordered pair of inserted
cells.  PP3aha--PP3ahc show that the resulting secant lines have movement and
refill degree at most `binom(s,2)` each.  Their union therefore removes at most
`2 binom(s,2)=s(s-1)` values.  The bound forgets all `B_3/B_4` weight. ∎

### Corollary PP3aoz -- PROVED

At every active marked or endpoint scale

```text
s=o(sqrt(R)),
```

all local `B_3` and `B_4` atoms are absorbed by any fixed positive
controller-domain margin, irrespective of their weights.

#### Proof

Then `s(s-1)=o(R)`.  Apply PP3ahd--PP3ahf. ∎

Thus a credit-scale binary atom is never a robust-domain obstruction.

## 2. Unary local atoms are simple candidate support

Let `P` be the inserted state and let

```text
U_loc(P)
```

be the total `A_2` weight of the finitely many fixed local path atoms retained
after PP3aok--PP3aox.  Let `d_M(i,A)` and `d_F(i,B)` be their movement and refill
simple-support degrees.

### Proposition PP3apa -- PROVED

For every fixed inserted cell and candidate entry, at most one retained source
point witnesses a unary blocker.  Hence

```text
d_M(i,A)+d_F(i,B) <= U_loc(P)
```

for every macro-label pair, and the complete local unary table removes at most

```text
d_M(i,A)+d_F(i,B)
```

values from that paired domain.

#### Proof

This is PP3ahh--PP3ahi restricted to the finite local atom table.  A fixed
inserted cell cannot have two retained witnesses on the same candidate line,
because that would give three source points on one line.  Forgetting candidate
multiplicity gives the displayed degree bound. ∎

## 3. Sub-domain-scale local tables complete directly

Fix constants `gamma,xi>0`.  Suppose the non-`Xi` base domains support one of the
robust global allocation criteria at threshold `(gamma+xi)R`.

### Theorem PP3apb -- PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE

Assume:

1. the conditioned petal skeleton is source-clean;
2. an independent residual helper completion from PP3aoo is available;
3. the completed state inserts `s=o(sqrt(R))` cells;
4. for every macro-label pair,

   ```text
   d_M(i,A)+d_F(i,B)+s(s-1) <= xi R;
   ```

5. the local width condition PP3ho holds.

Then the complete local `A_2/B_3/B_4` table, with arbitrary binary weight, does
not prevent final controller-aware allocation.

A sufficient label-free condition is

```text
U_loc(P)+s(s-1) <= xi R.
```

#### Proof

The independent helper completion removes every nonlocal source and insertion
event by PP3aol.  Proposition PP3apa bounds local unary domain loss, while
PP3aoy bounds all local binary loss.  Apply PP3ahj--PP3ahk and retain the same
balanced ownership and global label matching. ∎

### Corollary PP3apc -- PROVED

Suppose the marked removal credit satisfies

```text
R_* = o(R)
```

and the fixed local path has at most ten atoms, each of weight `O(R_*)`.  Then

```text
U_loc(P)=o(R).
```

Consequently PP3apb completes directly whenever the non-`Xi` robust certificate
is available.

#### Proof

There are at most ten local atoms by PP3aor.  The unary subtable therefore has
total weight `O(R_*)=o(R)`, and the binary table is already absorbed by
PP3aoz. ∎

This includes every genuinely credit-scale atom produced by PP3aos or PP3aov
when the marked credit is asymptotically below the controller-pool size.

## 4. Domain-scale unary failure returns to a source star

The only remaining robust possibility is that the unary simple support reaches a
fixed fraction of `R` in one paired domain.

### Theorem PP3apd -- PROVED / CONDITIONAL COMPOSITE INTERFACE

Let a source-valid state insert `s=o(sqrt(R))` cells.  If the non-`Xi` base
domain has margin `xi R` but the local unary table destroys that margin, then
some inserted cell `a` and one movement or refill type have a fibre of size

```text
C > xi R/(2s).
```

The post-trade source contains a genuine source star centred at `a` with `C`
distinct retained partners.  Hence one of the following occurs.

1. A marked second trade moves `a` and the two-step cancellation theorem
   PP3ahq--PP3ahs gives strict `Xi` improvement.
2. Final allocation completes after the star support is charged.
3. Marked source, transition, endpoint-host, or foreign insertion preparation
   fails explicitly.

#### Proof

Apply PP3ahp to the failed domain.  Its witness uniqueness gives distinct
partners and exact removal credit by PP3aho.  Then apply the composite source-star
interface PP3ahq--PP3aht. ∎

At active scales the star degree is

```text
Omega(R/s)=omega(sqrt(R)).
```

Thus domain-scale unary failure produces a super-target second-generation centre.

## 5. Revised credit-scale atom endpoint

### Corollary PP3ape -- PROVED

The local-atom frontier splits as follows.

1. **Robust final-allocation branch:** all `B_3/B_4` multiplicity and every
   `A_2` table of size `o(R)` are absorbed.  Domain-scale unary failure becomes a
   super-target post-trade source star and enters the composite conversion.
2. **Monotone-only branch:** a single credit-scale `A_2`, `B_3`, or `B_4` atom
   remains relevant because the proof insists on one-step `Xi` descent without
   a robust final-domain margin.
3. **External branch:** source-clean skeleton, independent helper completion,
   controller-pool, distinguished-endpoint, Hall, alternating, or global
   allocation preparation fails.

Hence credit-scale local atoms are no longer a frontier in the robust branch.
The genuinely live atom problem is restricted to monotone-only architectures.

The no-three-in-line conjecture remains unproved.
