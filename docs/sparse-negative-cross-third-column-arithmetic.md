# Arithmetic reconstruction of the varying third column in a negative cross fibre

**Branch:** `research/sparse-algebraic-spread`

SAS5bs--SAS5bw reduce negative mixed curvature to one fixed original endpoint, one fixed
donor endpoint, one single-swap-only orientation and one of three endpoint-incidence
types for the third scope column.  Two of those types already fix the third column as a
swap mate.  In the remaining outside-endpoint type, collinearity with the two fixed
endpoint columns is a one-ratio Diophantine equation.

This note reconstructs the varying third column from a finite primitive row-ratio address.
It closes the column-arithmetic part of the negative cross fibre without claiming that
records with the same third column have the same rows, labels or energy collateral.

## Two fixed columns and one varying column

Fix distinct columns `a,b` from the two disjoint swap endpoint sets.  Let one rank-three
record place `a,b,c` at three distinct ordered row positions `i,j,k`.  Write the
corresponding rows as `r_i,r_j,r_k`, and put

`A=r_j-r_i`,

`B=r_k-r_i`.

Then `A` and `B` are nonzero and distinct.  Collinearity is equivalent to

`A*(c-a)=B*(b-a)`.

Let

`g=gcd(|A|,|B|)`,

`A_0=A/g`,

`B_0=B/g`.

Thus `gcd(|A_0|,|B_0|)=1`.

## SAS5bx -- exact third-column divisibility criterion -- PROVED

For fixed `a,b`, ordered row-position assignment `(i,j,k)` and primitive row ratio
`(A_0,B_0)`, an integer third column exists if and only if

`A_0 divides (b-a)`.

When it exists it is unique and equals

`c=a+B_0*(b-a)/A_0`.

### Proof

Divide the collinearity equation by `g` to obtain

`A_0*(c-a)=B_0*(b-a)`.

Coprimality implies `A_0` divides `b-a`.  Solving gives the displayed value.  Conversely,
that value is integral under the divisibility condition and satisfies the equation. QED.

Board validity and distinctness are then checked directly; they do not create a second
solution.

## SAS5by -- finite primitive ratio stock -- PROVED

For an `N`-row board, the ordered primitive pair `(A_0,B_0)` belongs to a dictionary of
size at most

`4*(N-1)^2`.

There are at most six ordered assignments of the fixed columns `a,b` and the third column
to the increasing row positions.  Hence the complete safe reconstruction-address stock

`(row-position assignment,A_0,B_0)`

has size at most

`24*(N-1)^2`.

### Proof

Each nonzero oriented row gap lies in

`{-(N-1),...,-1,1,...,N-1}`,

so there are fewer than `2(N-1)` choices for each primitive coordinate and at most
`4(N-1)^2` ordered pairs.  Multiply by the six permutations of three columns among the
three row positions. QED.

The bound is safe rather than sharp because row ordering, coprimality and board validity
remove many addresses.

## SAS5bz -- mate-type fibres already have a fixed third column -- PROVED

Inside the scope-type dictionary of SAS5bv:

1. if the third column is the mate of `a` in the original swap, it is fixed;
2. if the third column is the mate of `b` in the donor swap, it is fixed.

Only the outside-all-endpoints type has a varying third column.

### Proof

Each transposition has exactly two fixed endpoint columns.  Once one endpoint is `a` or
`b`, its mate is the other named endpoint of that same transposition. QED.

## SAS5ca -- weighted localization to one exact third column -- PROVED

Let one fixed endpoint-pair/orientation/scope-type fibre have total record weight `V>0`.
Then:

1. in either mate type, the complete weight `V` already lies on one exact third column;
2. in the outside-endpoint type, one reconstruction address carries weight at least

   `V/[24*(N-1)^2]`,

   and all records in that address have the same exact third column, reconstructed by
   SAS5bx.

### Proof

The mate cases are SAS5bz.  In the outside type, partition by the at most
`24(N-1)^2` addresses from SAS5by and use weighted pigeonhole.  SAS5bx makes the third
column unique inside the selected address. QED.

This is a column concentration, not an exact-record concentration: row scale, base row and
required labels may still vary.

## SAS5cb -- quantitative negative-cross column router -- PROVED

Use the exact fibre supplied by SAS5bw from a divisor scale of weight `L_g`.

For every `eta in (0,1)`, if `C_minus>=eta*L_g`, then one of the following holds:

1. a mate-type fibre of negative curvature has one fixed third column and weight at least
   `eta*L_g/24`;
2. an outside-endpoint reconstruction address has one exact third column and weight at
   least

   `eta*L_g/[576*(N-1)^2]`.

If the composed move improves, replace `eta*L_g` by the strict bound `L_g`; hence one of
the same outputs has weight respectively greater than

`L_g/24`

or

`L_g/[576*(N-1)^2]`.

### Proof

SAS5bw first supplies an endpoint-pair/orientation/scope-type fibre of weight at least
`eta L_g/24`, or strictly more than `L_g/24` in the improving branch.  Apply SAS5ca.
The outside-type denominator is `24*24(N-1)^2=576(N-1)^2`. QED.

## Corrected SAS6 frontier

The negative mixed-curvature branch now reaches one exact third column after a finite
primitive row-ratio split.  What remains inside that column fibre is the row-scale/base
row and required-label structure, plus compatibility across several such fibres.  The
other exact-scale obstruction remains the coprime donor-saturated progression, together
with high-incidence and board-boundary profiles.

## Finite check

`scripts/verify_sparse_negative_cross_third_column.py` exhausts small boards, all ordered
row triples, all placements of two fixed columns and all valid third columns.  It checks
the divisibility formula, uniqueness, safe address stock, mate-type collapse and the
weighted constants in SAS5ca--SAS5cb.