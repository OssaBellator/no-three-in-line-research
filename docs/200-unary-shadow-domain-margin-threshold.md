# Unary insertion shadow at the allocation-domain scale

The binary domain theorem PP3aha--PP3ahg absorbs every inserted-pair shadow of a
small source-valid endpoint state.  Unary insertion shadow is different: one
inserted endpoint cell and one retained source point may block a controller
candidate.  A large retained source contains many possible witness points, so a
small endpoint state does not by itself give an `o(R)` unary bound.

Source validity nevertheless removes unary witness multiplicity at one fixed
inserted cell.  For an inserted cell `a` and one controller candidate `z`, at
most one retained source point lies on the line `az`.  Thus the unary `Xi` cost
of one forced arc cell is exactly simple candidate-entry support, not repeated
weight on the same entry.

This yields a domain-scale alternative.  Unary shadow whose total incidence
weight is `o(R)` is absorbed together with all binary shadow by any fixed
positive controller-domain margin.  Applied to a comparable fixed-centre
arc-petal bank, either one petal completes directly or every petal carries
`Omega(R)` unary cost, producing the stronger global threshold
`A_2=Omega(R|B|)`.  Rank-three path-petal cost is binary and is already covered
by PP3aha--PP3ahg.

## 1. Uniqueness of a unary witness

Let `S_0` be the retained source after an endpoint trade, and let `P` be the set
of inserted endpoint cells.  Assume

```text
S_0 union P
```

is no-three-in-line.  A unary candidate incidence is a triple `(a,p,z)` with
`a in P`, `p in S_0`, and controller candidate cell `z` collinear with `a,p`.
Only noncontroller, nonaxis incidences counted by the dynamic `Xi` potential are
retained.

### Proposition PP3ahh -- PROVED

For every fixed inserted cell `a` and fixed candidate entry `z`, at most one
retained source point `p` gives a unary candidate incidence `(a,p,z)`.

#### Proof

If two distinct retained points `p,p'` both worked, then `a,p,p'` would lie on
the same line through `a,z`.  This contradicts the no-three property of the
completed source. ∎

Hence candidate-entry multiplicity in unary `Xi` can arise only from different
inserted cells, not from several retained witnesses for one inserted cell.

## 2. Simple support and unary incidence weight

Let

```text
U_Xi(P)
```

be the total number of unary candidate incidences, with the ordinary dynamic
`Xi` multiplicity.  Let `U_supp(P)` be the simple set of controller
edge--label entries occurring in at least one such incidence.

### Proposition PP3ahi -- PROVED

One has

```text
|U_supp(P)| <= U_Xi(P) <= |P| |U_supp(P)|.
```

For a fixed inserted cell `a`, its unary `Xi` contribution equals the number of
distinct candidate entries blocked with a retained source point.

#### Proof

The first inequality forgets multiplicity.  By PP3ahh, a fixed candidate entry
has at most one retained witness for each inserted cell, so its total unary
multiplicity is at most `|P|`.  For one fixed `a`, every supported entry has
multiplicity exactly one. ∎

This is the support interpretation needed for a forced arc cell in the
fixed-axis petal bank.

## 3. Combined unary and binary domain loss

For macro `i`, let

```text
d_M(i,A)
```

be the number of controller edges in that macro whose movement entry at label
`A` belongs to `U_supp(P)`.  Define `d_F(i,B)` on the refill side.  Let

```text
s=|P|.
```

Let `H_i^base(A,B)` include every source, anchor, and non-`Xi` exclusion, and let
`H_i^Xi(A,B)` also delete the complete unary and binary candidate support of the
trade.

### Theorem PP3ahj -- PROVED

For every macro and label pair,

```text
|H_i^base(A,B) \ H_i^Xi(A,B)|
<=
d_M(i,A)+d_F(i,B)+s(s-1).
```

In particular the crude total-weight criterion gives

```text
|H_i^base(A,B) \ H_i^Xi(A,B)|
<=
U_Xi(P)+s(s-1).
```

#### Proof

The unary movement and refill supports remove respectively at most the first
two displayed degrees.  PP3ahc bounds all binary inserted-pair shadow by
`s(s-1)` further values.  Taking the union gives the first inequality.  Both
unary degrees are bounded by the total simple unary support, which is at most
`U_Xi(P)` by PP3ahi; using the union rather than adding the two copies gives the
crude bound as stated. ∎

The degree form may be much sharper than the total-weight form when unary
entries are spread over final labels.

## 4. Domain-margin completion criterion

Fix constants `gamma,xi>0` and define

```text
J_i^base(gamma+xi)
=
{(A,B): |H_i^base(A,B)| >= (gamma+xi)R}.
```

### Theorem PP3ahk -- PROVED

Suppose

```text
d_M(i,A)+d_F(i,B)+s(s-1) <= xi R
```

for every macro and label pair.  Then

```text
J_i^base(gamma+xi) subseteq J_i^Xi(gamma)
```

for every macro.

A sufficient label-free condition is

```text
U_Xi(P)+s(s-1) <= xi R.
```

Consequently, if the base margin graphs satisfy PP3fy or PP3gl and the local
width inequality PP3ho holds, the complete endpoint trade supports the final
controller-aware allocation.

#### Proof

Apply PP3ahj to every margin-compatible pair.  Its post-shadow domain has size
at least

```text
(gamma+xi)R-xi R=gamma R.
```

The same global ownership and label matching therefore remain available, and
PP3ho--PP3hq complete the patch. ∎

This is again a direct-completion statement rather than a monotone `Xi`
decrease.

## 5. Active-state criterion

### Corollary PP3ahl -- PROVED

Let an active endpoint state have

```text
s=m^(kappa+o(1)),
kappa<19/40.
```

If its unary insertion weight satisfies

```text
U_Xi(P)=o(R),
```

then for every fixed `xi>0`,

```text
U_Xi(P)+s(s-1) <= xi R
```

for all sufficiently large `m`.  Therefore every robust non-`Xi` domain margin
absorbs the full unary and binary insertion shadow.

#### Proof

The unary term is `o(R)` by hypothesis and the binary term is `o(R)` by
PP3ahe. ∎

Thus credit-scale unary cost is not automatically hard for final allocation;
it becomes hard only when it reaches the much larger controller-domain scale.

## 6. Consequence for fixed-centre petal banks

Let `B` be a comparable incoming or outgoing arc-petal bank from
PP3ada--PP3ade.  For a state based on petal `e`, write

```text
a(e)
```

for the unary `Xi` contribution of its forced arc cell, and let `U_0(e)` be all
other unary insertion weight of the completed state.  Let the state insert `s`
cells.

### Theorem PP3ahm -- PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE

Assume:

1. the source-valid state law and non-`Xi` base domains are prepared;
2. the base compatibility graphs have margin `xi R` and satisfy PP3fy or PP3gl;
3. for every retained petal state,

   ```text
   U_0(e) <= xi R/4,
   s(s-1) <= xi R/4;
   ```

4. the local width condition PP3ho holds.

Then at least one of the following occurs.

1. Some petal satisfies

   ```text
   a(e) <= xi R/2,
   ```

   and its source-valid completion gives the final patch directly through
   PP3ahk.
2. Every petal in `B` satisfies

   ```text
   a(e) > xi R/2,
   ```

   so the global rank-two unary table obeys

   ```text
   A_2 >= sum_{e in B}a(e) > (xi/2)R|B|.
   ```

#### Proof

In the first case,

```text
a(e)+U_0(e)+s(s-1) <= xi R,
```

so PP3ahk preserves the allocation domains and completes.  Otherwise sum the
strict lower bound over the petal bank. ∎

For a target bank `|B|=W`, failure therefore forces

```text
A_2=Omega(RW),
```

which is stronger than the removal-credit-scale threshold in PP3adf whenever
the usable trade credit is `o(R)`.

Rank-three outer path-petal and middle-grid local costs are binary inserted-pair
shadow.  Under the same robust-domain assumptions they are already absorbed by
PP3ahf, regardless of their weighted multiplicity.

## 7. Revised marked-petal endpoint

### Corollary PP3ahn -- PROVED

In the robust direct-allocation branch:

1. fixed-centre path-petal, rank-four partner, and choice-grid binary `Xi` cost
   is not an independent obstruction;
2. fixed-axis arc-petal unary cost completes whenever it is `o(R)` together with
   the other unary state cost;
3. persistent arc-petal failure is a domain-scale unary core

   ```text
   A_2=Omega(RW),
   ```

   or a non-`Xi` margin, source, anchor, or endpoint-host failure.

The remaining unary problem is therefore controller-domain-scale shadow, not
merely local cost comparable with a small removal-credit bank.

## 8. Finite diagnostic

The script

```text
scripts/check_unary_shadow_domain_margin.py
```

checks a finite source-valid inserted/retained state, verifies uniqueness of the
retained witness for each inserted-cell--candidate pair, constructs the unary
and binary candidate supports, and reports the exact domain-margin outcome.
