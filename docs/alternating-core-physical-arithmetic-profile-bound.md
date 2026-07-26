# Polynomial physical arithmetic profiles from grid determinants

**Branch:** `research/alternating-core-chain`

AC3an gives a finite BDA profile count in terms of an external denominator bound
`Q` and direction bound `M`. AC3hw leaves same-denominator non-scalar arithmetic
changes as one recurrent AC4 field. This note proves explicit polynomial choices
for `Q` and `M` when the arithmetic data are physically realised by determinant
ratios of grid-direction vectors.

The contract is deliberately narrow. An arbitrary normalized arithmetic label,
an outside-board anchor, an unbounded-arity formula or a subgroup/coset name not
reconstructed from bounded physical data receives no bound here.

## Physical direction universe

Let the board be `[n] x [n]`, with `n>=2`, and put

\[
M=n-1.
\]

Every nonzero difference of two board cells has coordinates in `[-M,M]^2`.
Normalize a primitive direction by changing sign so that its first nonzero
coordinate is positive. For the finite BDA convention with positive first
coordinate, write

\[
D_M
=
\{(x,y):1\le x\le M,\ |y|\le M,\ \gcd(x,|y|)=1\}
\]

and `N_M=|D_M|`.

## AC3mr -- physical direction and determinant bounds -- PROVED

Every primitive direction obtained from two board cells belongs to the ambient
signed direction universe of infinity norm at most `M`. In particular,

\[
\boxed{N_M\le M(2M+1).}
\]

For any two such directions

\[
d=(a,b),\qquad e=(c,d),
\]

the determinant satisfies

\[
\boxed{|\det(d,e)|\le 2M^2=2(n-1)^2.}
\]

### Proof

Coordinate differences have absolute value at most `M`; dividing by their gcd
cannot increase that bound. The crude direction count chooses the positive first
coordinate in `M` ways and the second coordinate in `2M+1` ways. Finally,

\[
|ad-bc|\le |ad|+|bc|\le 2M^2.
\]

QED.

The determinant estimate is intentionally safe rather than sharp for primitive
vectors.

## Determinant-rational realization

Call a reduced rational arithmetic parameter **determinant-realized** when it has
form

\[
\frac{u}{v},
\qquad
u=\det(d_1,e_1),
\quad
v=\det(d_2,e_2)\ne0,
\]

for physical primitive directions of the preceding type. More generally, a
reduced denominator `q` is determinant-realized when it is the denominator after
cancelling such a ratio.

## AC3ms -- polynomial reduced denominator bound -- PROVED

Every determinant-realized reduced denominator satisfies

\[
\boxed{2\le q\le Q_{\rm det}:=2(n-1)^2}
\]

whenever it is nontrivial. Its reduced numerator has absolute value at most the
same safe bound.

### Proof

Before reduction, the denominator has absolute value at most `2M^2` by AC3mr.
Cancelling a common divisor can only decrease its absolute value. The numerator
is treated identically. QED.

Thus determinant ratios cannot introduce an unbounded denominator field on a
fixed board.

## AC3mt -- polynomial physical BDA profile stock -- PROVED UNDER THE DETERMINANT-REALIZATION CONTRACT

Assume every BDA arithmetic profile

\[
\pi=(q,d,e,\xi)
\]

has:

- determinant-realized denominator `2<=q<=Q_det`;
- physical primitive directions `d,e in D_M`;
- scalar residue `xi mod q`.

Then the complete exact profile stock is at most

\[
\boxed{
L_{\rm phys}(n)
=
N_M^2\sum_{q=2}^{Q_{\rm det}}q
\le
N_M^2\frac{Q_{\rm det}(Q_{\rm det}+1)}2.
}
\]

Using `N_M<=M(2M+1)` and `Q_det=2M^2`,

\[
\boxed{L_{\rm phys}(n)=O(n^8).}
\]

For a fixed denominator `q`, the sharper stock is

\[
\boxed{qN_M^2=O(n^6).}
\]

### Proof

Choose the two primitive directions and then one of `q` residues. Summing over
all determinant-realized denominators gives the first formula. The polynomial
orders follow from `N_M=O(n^2)` and `Q_det=O(n^2)`. QED.

This is AC3an with explicit physical parameters rather than external `Q,M`.

## Physical same-denominator non-scalar words

Let `L_ext` bound the remaining finite role data at one physical occurrence:
current/new rank, channel word, bank type, owner route, closure role and any
other already proved finite decoration. Assume also that the physical anchor is
a board cell, so there are at most `n^2` anchors.

## AC3mu -- polynomial same-denominator non-scalar address stock -- PROVED UNDER THE PHYSICAL ANCHOR/ROLE CONTRACT

For one fixed denominator `q`, the complete physical non-scalar address stock is
at most

\[
\boxed{
N_{\rm ns}(q)
\le
n^2L_{\rm ext}\,qN_M^2.
}
\]

Under the determinant denominator bound,

\[
\boxed{N_{\rm ns}(q)=O(L_{\rm ext}n^8).}
\]

Across every determinant-realized denominator,

\[
\boxed{
N_{\rm ns}^{\rm tot}
\le
n^2L_{\rm ext}N_M^2
\frac{Q_{\rm det}(Q_{\rm det}+1)}2
=
O(L_{\rm ext}n^{10}).
}
\]

A weighted family of physical same-denominator profile episodes of total weight
`W` therefore contains one exact physical address of weight at least

\[
\boxed{W/N_{\rm ns}^{\rm tot}.}
\]

### Proof

Choose the board anchor, finite external role, exact denominator, two directions
and scalar residue. The fixed-`q` and total formulae follow by multiplication and
summation. Weighted pigeonhole gives the final statement. QED.

Historical multiplicity of one address is not payment. Repetition still enters
the AC3kz--AC3lc cycle router.

## AC3mv -- corrected arithmetic multiplicity interface -- PROVED

Under the physical determinant-rational, board-anchor and finite-role contracts:

1. primitive direction and projective slope have polynomial stocks;
2. reduced denominator and scalar residue have polynomial stocks;
3. the exact BDA arithmetic profile has stock `O(n^8)`;
4. the complete physical same-denominator non-scalar address has stock
   `O(L_ext n^10)`;
5. this physical arithmetic address may be used as a polynomial AC3ka field or
   reset decoration.

The following remain outside the theorem:

- a denominator supplied only as an abstract normalized label;
- an RI subgroup/coset, order or root name not reconstructed from bounded
  physical determinants;
- anchors outside a proved polynomial physical universe;
- unbounded-arity arithmetic formulae;
- external role dictionaries without a polynomial `L_ext` bound;
- recurrence of an exact address without payment, descent, impossibility or a
  capacity-one ticket.

### Proof

Items 1--4 are AC3mr--AC3mu. Item 5 is the polynomial-field requirement of AC3ka.
The exclusions lack one of the physical reconstruction hypotheses and therefore
cannot inherit the displayed bounds. QED.

## Consequence

The denominator and direction components of the physical BDA frontier are no
longer generic multiplicity parameters. A surviving arithmetic recurrence must
now either violate the determinant-realization contract, use an unbounded
external role/anchor dictionary, or repeat one exact polynomially indexed
physical profile. The first two are explicit realization gaps; the last enters
the macro-cycle payment/descent/ticket router.

## Finite check

`scripts/verify_ac_physical_arithmetic_profile_bound.py` enumerates primitive
directions on boards through side eight, checks every determinant, exhausts all
reduced ratios of nonzero determinants, verifies the denominator ceiling and
compares exact direction/profile/address counts with every displayed bound.
