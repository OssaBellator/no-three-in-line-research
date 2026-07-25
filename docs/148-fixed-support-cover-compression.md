# Fixed-support cover compression for terminal blockers

PX356--PX370 convert nonimproving terminal banks into large families of
external blocker certificates.  Every such blocker contains one or two fixed
selected points.  Rather than neutralizing blockers one at a time, this
chapter compresses the whole family onto a small selected-point cover.

A maximal disjoint-support family has endpoints meeting every blocker support.
Assign each blocker to one covering selected point, then retain the heaviest
layer/channel type.  The resulting selected points form one row-column
compatible endpoint block and carry at least a `1/(2q)` share of the entire
blocker debt.

This is an exact causal compression.  It does not by itself bound collateral
from rematching the cover block, but it turns a diffuse family of candidate
centres into one weighted endpoint move with explicit suppression credit.

## 1. Maximal support matching gives a cover

Let `C` be a finite family of external blocker certificates.  For each
`T in C`, let `S(T)` be its fixed selected-point support.  Thus

\[
1\le |S(T)|\le2.
\]

Choose a maximal subfamily `Q subseteq C` whose supports are pairwise disjoint,
and put

\[
V=\bigcup_{T\in Q}S(T).
\]

### Theorem PX371 -- PROVED

The set `V` meets every blocker support:

\[
\boxed{S(T)\cap V\ne\varnothing\quad(T\in C).}
\]

Moreover

\[
\boxed{|V|\le2|Q|.}
\]

### Proof

If some support `S(T)` were disjoint from `V`, it could be added to `Q`,
contradicting maximality.  The size bound follows because every support in
`Q` has order at most two. \(\square\)

Thus `V` is a selected-point vertex cover of the complete blocker family.

## 2. Assigning blocker debt to cover points

Choose, for every blocker `T`, one point

\[
a(T)\in S(T)\cap V.
\]

For `z in V`, define its assigned blocker weight

\[
w(z)=|\{T\in C:a(T)=z\}|.
\]

Then

\[
\sum_{z\in V}w(z)=|C|.
\]

Assume the selected state has two permutation layers and at most `q` channels.
Partition `V` into its at most `2q` layer/channel types.

### Theorem PX372 -- PROVED

Some type class `V_*` satisfies

\[
\boxed{
W_*:=\sum_{z\in V_*}w(z)\ge\frac{|C|}{2q}.
}
\]

The points of `V_*` occupy distinct rows and columns.

### Proof

Pigeonhole the total assigned weight `|C|` over at most `2q` type classes.
Points in one permutation layer form a partial matching, so their rows and
columns are distinct. \(\square\)

## 3. Exact causal suppression credit

Freeze the parent terminal buffer switch.  Rematch the selected points of
`V_*` inside their common layer/channel while forbidding every current
position.

### Theorem PX373 -- PROVED REDUCTION

Every allowed rematching of `V_*` suppresses all blockers assigned to points
of `V_*`.  Hence the coupled parent/child move receives exact causal
suppression credit at least

\[
\boxed{W_*\ge\frac{|C|}{2q}.}
\]

The original parent-core destruction remains available when the frozen parent
switch executes.

### Proof

A blocker assigned to `z in V_*` contains `z` as a fixed selected point.
Forbidding the current position of `z` moves it away from the blocker triple,
so that blocker is absent when the parent switch is executed.  Distinct
blockers are counted with their geometric multiplicity, giving total credit
`W_*`.  The parent core and buffer support remain frozen during the child
rematching, so its old destruction has not yet been spent. \(\square\)

This is the multi-block form of the exact `Gamma_A(W)` cancellation from
PX235--PX239.

## 4. Size--weight dichotomy inside the cover

Let

\[
t=|V_*|.
\]

### Theorem PX374 -- PROVED

For every threshold `T>=1`, one of the following holds.

1. `t>=T`, giving a compatible endpoint block of order at least `T` and
   suppression credit `W_*>=|C|/(2q)`.
2. Some selected point `z in V_*` has

   \[
   \boxed{
   w(z)>\frac{|C|}{2qT}.
   }
   \]

### Proof

If `t<T`, the average assigned weight on `V_*` is greater than

\[
W_*/T\ge |C|/(2qT).
\]

One point has at least the average. \(\square\)

The second outcome is a weighted one-point child, handled by the actual
buffer-cycle theorem PX342.

## 5. Application to weighted terminal covers

Assume a terminal bank destroys `D` designated old certificates in every
state and is nonimproving.

### Theorem PX375 -- PROVED REDUCTION

At least one exact return type has a blocker family `C` satisfying either

\[
|C|\ge\frac{Dn}{48}
\]

or

\[
|C|\ge\frac{Dn^2}{32}.
\]

For every threshold `T`, that family gives either:

1. a compatible endpoint block of order at least `T` with exact parent-blocker
   suppression credit at least

   \[
   \boxed{
   \frac{Dn}{96q}
   }
   \]

   in the one-variable case, or

   \[
   \boxed{
   \frac{Dn^2}{64q}
   }
   \]

   in the two-variable case; or
2. a weighted one-point child of designated weight greater than

   \[
   \boxed{
   \frac{Dn}{96qT}
   }
   \]

   or respectively

   \[
   \boxed{
   \frac{Dn^2}{64qT}.
   }
   \]

### Proof

Use PX357 for the family size, PX372--PX373 for the suppression credit, and
PX374 for the size--weight dichotomy. \(\square\)

### Corollary PX376 -- PROVED REDUCTION

For an original terminal core `D>=1`, choose

\[
T=n^{2/3}.
\]

A one-variable return gives either:

- an endpoint block of order at least `n^(2/3)` carrying suppression credit at
  least `n/(96q)`; or
- a weighted one-point child of weight greater than

  \[
  \boxed{n^{1/3}/(96q).}
  \]

A two-variable return gives either the same large endpoint block with
quadratic suppression credit, or a one-point child of weight greater than

\[
\boxed{n^{4/3}/(64q).}
\]

before the independent geometric caps of PX367--PX370 are applied.

For `q=n^{o(1)}`, the endpoint-block outcome lies strictly above the
square-root ambient threshold and enters PX334--PX335.  Its parent suppression
credit is at least linear in `n`, while hybrid thinning makes the internal
rank-three load sublinear in the retained block order.

The one-point alternative feeds back into the weighted buffer cover of
PX356.  PX365 and PX368 then exclude directed-path or mixed-shadow recurrence
once the designated weight exceeds their incidence caps.

PX371--PX376 reduce the persistent terminal return to a weighted endpoint
block or a high-weight one-point core without discarding the multiplicity of
the parent blocker family.  The remaining sign question is now confined to
nondegenerate rank-one returns whose support cover is too small to enter the
large-block theorem.

## 6. Verification

Run

```bash
python scripts/verify_product_fixed_support_cover.py
```

The verifier exhausts all support systems of order at most five, checks that
maximal disjoint supports cover the full family, validates the type-weight
pigeonhole constants, and checks every displayed size--weight inequality.