# Small endpoint trades bypass all binary shadow multiplicity

The fixed-cell domain theorem PP3agu--PP3agz uses one centre cell and its
residual partner lines.  The same support argument applies to every binary
insertion-shadow term of a source-valid endpoint trade.

If a trade inserts `s` endpoint cells, its binary shadow is supported on the
secant lines determined by unordered pairs of inserted cells.  There are at
most

```text
binom(s,2)
```

such lines.  Every nonaxis line contributes a matching between controller edges
and movement labels, and another matching between controller edges and refill
labels.  Therefore arbitrary weight or candidate multiplicity on all binary
`Xi` patterns removes at most `binom(s,2)` entries at any controller edge or
final label.  Every paired macro domain loses at most `2 binom(s,2)` values.

At all active endpoint and marked-cycle scales this is `o(R)`.  Hence a fixed
positive controller-domain margin absorbs the complete rank-three and rank-four
binary insertion shadow.  The weighted binary stars, fixed-cell heavy pencils,
and candidate-rich grids remain relevant to monotone `Xi` improvement, but they
are not obstructions to direct final allocation when the nonbinary domains have
robust slack.

## 1. Secant support of a source-valid endpoint state

Let

```text
P={p_1,...,p_s}
```

be the inserted endpoint cells of one saturation-preserving trade.  The cells
form a matching between their old-column and old-row resources.  Assume the
completed source is no-three-in-line.

Let

```text
L(P)={line(p_i,p_j): 1<=i<j<=s}.
```

### Proposition PP3aha -- PROVED

Every line in `L(P)` is nonvertical and nonhorizontal, and

```text
|L(P)|=binom(s,2).
```

#### Proof

Distinct inserted cells use distinct old columns and distinct old rows, so their
joining line is nonaxis.  If two unordered pairs determined the same geometric
line, that line would contain at least three distinct inserted cells, contrary
to source validity. ∎

The equality is useful but not essential below; the upper bound by
`binom(s,2)` holds without source validity.

## 2. Binary candidate entries form a union of line matchings

Let `Z_2(P)` be the simple candidate-entry support created by pairs of inserted
cells.  Thus a movement entry `(e,A)` belongs to `Z_2(P)` when its candidate
cell `(x_e,A)` lies on one of the lines in `L(P)`.  Define refill entries
analogously.

### Theorem PP3ahb -- PROVED

The movement and refill parts of `Z_2(P)`, viewed as bipartite graphs between
controller edges and final labels, satisfy

```text
Delta(Z_2^M(P)) <= binom(s,2),
Delta(Z_2^F(P)) <= binom(s,2).
```

These are simple-support bounds and are independent of every binary pattern
weight or candidate multiplicity.

#### Proof

By PP3agu, one nonaxis line contributes at most one movement entry at a fixed
movement label and at most one movement entry at a fixed controller edge.  Sum
over the `binom(s,2)` secant lines.  The refill proof is transposed. ∎

A candidate cell may be counted by several weighted binary patterns, but its
controller-edge--label entry is deleted only once.

## 3. Exact loss from a refined same-slot domain

Let

```text
H_i^base(A,B)
```

be the macro domain after every source, anchor, unary insertion, and other
nonbinary exclusion has been imposed.  Let

```text
H_i^bin(A,B)
```

be the domain after also deleting all binary candidate entries created by `P`.

### Proposition PP3ahc -- PROVED

For every macro `i` and label pair `(A,B)`,

```text
|H_i^base(A,B) \ H_i^bin(A,B)|
<=
2 binom(s,2)
=
s(s-1).
```

#### Proof

At movement label `A`, PP3ahb removes at most `binom(s,2)` controller edges in
the full controller layer, and hence no more in macro `i`.  At refill label `B`
it removes at most the same number.  Take the union. ∎

The bound simultaneously covers support-rank two, three, and four binary `Xi`
patterns: endpoint-index rank changes multiplicity bookkeeping but not the fact
that every selected binary pair lies on one of the same secant lines.

## 4. Robust compatibility survives binary shadow

Fix constants `gamma,xi>0` and put

```text
J_i^base(gamma+xi)
=
{(A,B): |H_i^base(A,B)| >= (gamma+xi)R}.
```

### Theorem PP3ahd -- PROVED

If

```text
s(s-1) <= xi R,
```

then

```text
J_i^base(gamma+xi) subseteq J_i^bin(gamma)
```

for every macro `i`.

Therefore every balanced ownership and global label matching supported by the
margin graphs remains valid after all binary insertion shadow of the endpoint
trade is added.

#### Proof

For every margin-compatible pair, PP3ahc gives

```text
|H_i^bin(A,B)|
>=
(gamma+xi)R-s(s-1)
>=
gamma R.
```

The pair remains in the post-trade threshold graph. ∎

## 5. Active-scale saving

The controller pool size is

```text
R=m^(19/20+o(1)).
```

### Corollary PP3ahe -- PROVED

If the endpoint state size satisfies

```text
s=m^(kappa+o(1)),
kappa<19/40,
```

then

```text
s^2/R=o(1).
```

In particular this holds for:

1. two-scale endpoint banks with `kappa<1/40`;
2. fixed-centre marked-cycle and filler states with `kappa<19/80`;
3. all bounded and polylogarithmic endpoint trades.

#### Proof

The exponent of `s^2/R` is

```text
2kappa-19/20<0.
```

The displayed active ranges lie strictly below `19/40`. ∎

Thus every fixed positive domain margin eventually dominates the complete
binary candidate support of one active trade.

## 6. Direct binary-shadow bypass theorem

### Theorem PP3ahf -- PROVED / CONDITIONAL DIRECT-COMPLETION INTERFACE

Suppose a source-admissible endpoint, cycle, rectangle, or filler trade inserts
`s` endpoint cells and:

1. every source, anchor, unary insertion, and nonbinary obstruction is already
   included in `H_i^base(A,B)`;
2. the margin graphs `J_i^base(gamma+xi)` satisfy PP3fy or PP3gl;
3. the local width condition in PP3ho holds;
4. `s(s-1)<=xi R`.

Then arbitrary binary controller-shadow multiplicity created by the trade does
not prevent the final allocation.  The same balanced ownership and global
label matching remain available after every rank-two through rank-four binary
candidate entry is deleted, and PP3hq gives the saturated no-three patch.

#### Proof

The trade is source-admissible by hypothesis.  Apply PP3ahd to preserve the
margin compatibility graphs after the binary support is inserted, then apply
PP3ho and PP3hq. ∎

As in PP3agz, this is a direct completion theorem.  It need not decrease the
integer `Xi` potential and is used only when the nonbinary controller domains
already have fixed positive allocation slack.

## 7. Revised binary paid frontier

### Corollary PP3ahg -- PROVED

In the robust-domain branch, none of the following is an independent final
obstruction:

- positive-density ambient rank-three or rank-four binary stars;
- fixed-cell heavy partner pencils;
- weighted complete two-resource grids;
- candidate-rich projective covers;
- support-ranked binary `Xi` multiplicity of an active endpoint state.

All are supported on at most `binom(s,2)` secant-line matchings and are absorbed
by `o(R)` domain loss.

The binary structures remain necessary in branches that seek a monotone `Xi`
decrease before allocation.  The genuinely open direct-completion cases are
now:

1. failure of the nonbinary domain margin or global allocation criterion;
2. unary insertion shadow involving retained source points;
3. source, anchor, or endpoint-host failure;
4. trades too large to satisfy `s^2=o(R)`;
5. branches where no direct final allocation is yet available.

## 8. Finite diagnostic

The script

```text
scripts/check_binary_shadow_allocation_bypass.py
```

enumerates every inserted-pair secant of a finite source-valid endpoint state,
constructs its movement and refill candidate traces, verifies the
`binom(s,2)` incidence-degree bound, and checks the exact macro-domain margin.