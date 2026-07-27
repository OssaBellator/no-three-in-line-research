# Line and repeated-cell structure of cross-star product collateral

**Branch:** `research/geometric-cleaning`

GC2dc--GC2dg reduce every genuine product-bank failure to one exact block tuple of one of three
profiles:

- a `(1,1)` bridge;
- an oriented `(2,1)` chord;
- a `(1,1,1)` transversal.

This note records the geometry inside that tuple.  Every certificate lies on one exact board line.
After separating axis lines, a bounded non-axis line dictionary localizes the weight, and the line
contains only finitely many moved cells.  Weighted incidence then produces one repeated physical
replacement cell.

## Board-line dictionary

Let the board be `[N]^2`.  Let `L_N` be the set of non-axis lines containing at least two board
cells, and put

`ell_N=|L_N|`.

Every such line is determined by its lexicographically least unordered pair of board cells, so

`ell_N<=binom(N^2,2)`.

A non-axis line contains at most `N` board cells, because it meets every board row in at most one
cell.

Use the normalized expected certificate weights `e_Q` from GC2de.  All statements below are inside
one fixed physical block tuple returned by GC2df.

## GC2dh -- exact line address and axis split -- PROVED

Every bridge, chord or transversal certificate has one unique supporting board line.

For a bridge, the line contains its one fixed `Z` cell and its two moved matching cells.  For a
chord, it contains the two moved cells from the double block and the one moved cell from the single
block.  For a transversal, it contains one moved cell from each of the three blocks.

Consequently every weighted tuple family of total normalized mass `V` splits canonically as

`V=V_axis+V_non`,

where `V_axis` is supported on rows or columns and `V_non` is supported on `L_N`.  At least one part
has mass at least `V/2`.

### Proof

A rank-three certificate is a collinear triple, and three distinct collinear board cells determine
one line.  The profile determines which cells are moved and which are fixed.  Partition by whether
the unique line is horizontal or vertical. QED.

The axis part is an exact row- or column-collision witness and returns to the permutation/collision
constraint ledger.  The rest of the note treats the non-axis part.

## GC2di -- weighted non-axis line localization -- PROVED

Suppose `V_non>0`.

1. For a chord or transversal tuple, one exact non-axis line carries normalized mass at least
   
   `V_non/ell_N`.

2. For a bridge tuple, one exact pair `(z,L)`, consisting of the fixed `Z` cell and a non-axis line
   through it, carries normalized mass at least
   
   `V_non/(N*ell_N)`.

In particular, if `V_non>=V/2`, the displayed lower bounds become `V/(2 ell_N)` and
`V/(2N ell_N)` respectively.

### Proof

For chords and transversals, partition by the at most `ell_N` supporting lines.  For bridges, first
partition by line.  A non-axis line contains at most `N` possible fixed board cells, so a second
pigeonhole selects one `z`. QED.

## GC2dj -- repeated moved-cell incidence on one line -- PROVED

Fix one localized non-axis line class of normalized mass `U>0`.

1. **Bridge:** in each of its two moved blocks, one exact moved cell carries certificate-incidence
   mass at least
   
   `U/N`.

2. **Oriented chord:** in the double block, one exact moved cell carries incidence mass at least
   
   `2U/N`;
   
   in the single block, one exact moved cell carries incidence mass at least
   
   `U/N`.

3. **Transversal:** in each of the three blocks, one exact moved cell carries incidence mass at
   least
   
   `U/N`.

### Proof

A non-axis line contains at most `N` board cells.  Sum certificate weights over incidences with the
moved cells of one named block.  A bridge or transversal contributes one incidence per certificate
to each named block.  A chord contributes two incidences to its double block and one to its single
block.  Weighted pigeonhole gives the bounds. QED.

The repeated cell is a physical cell occurrence, not merely a repeated line direction.

## GC2dk -- import into the bounded cause dictionary -- PROVED AS AN INTERFACE

Under the existing occurrence-faithful cause contracts:

1. the localized non-axis line is one exact line atom and has assignment cause degree at most `2t`
   by GC3l, where `t` is the target-batch size;
2. if the repeated moved cell is used only in a prospective inserted-cell role, it has assignment
   degree at most two by GC3j;
3. if the cell is current target or partner support, its exact `p`- or `t`-role cost is the one in
   GC3j--GC3k;
4. failure of any of these role claims returns the exact current/support/global-context cause field.

### Proof

The line and cell supplied by GC2di--GC2dj are exact physical objects.  Apply the corresponding
role-degree theorem from GC3j--GC3l.  Those theorems are occurrence-faithful and therefore do not
permit a prospective cell or line to be used as unexplained current payment. QED.

## GC2dl -- cross-star geometric router -- PROVED UNDER THE PRODUCT-CAUSE CONTRACT

Let one bridge, chord or transversal block tuple carry normalized mass `V>0`.  Then at least one of
the following holds:

1. an axis row/column collision carries mass at least `V/2`;
2. a bridge has one exact `(fixed cell, non-axis line)` class of mass at least
   
   `V/(2N ell_N)`;
3. a chord has one exact non-axis line class of mass at least
   
   `V/(2 ell_N)`;
4. a transversal has one exact non-axis line class of mass at least
   
   `V/(2 ell_N)`;
5. inside alternatives 2--4, one repeated moved cell has the incidence mass stated in GC2dj and
   enters the bounded physical cause ledger of GC2dk;
6. the product-certificate or physical-role contract fails and returns its least exact failed
   field.

### Proof

Apply the axis split from GC2dh.  In the non-axis branch use GC2di and then GC2dj.  Import the exact
line and repeated cell through GC2dk. QED.

Thus the three cross-star profiles no longer end at an abstract block interaction.  They expose one
axis collision or one exact non-axis line together with a repeated physical moved cell.

## Corrected GC frontier

The compatible product-bank branch is now reduced to:

- axis collisions already controlled by permutation constraints;
- a non-axis line atom of degree at most `2t`;
- a repeated moved-cell support with its exact rectangle-role degree;
- or a named global-context/contract failure.

The next geometric task is to charge or install the repeated line/cell classes across several block
tuples and combine them with labelled paid-overload recursion, high created-pair multiplicity and
identity-sensitive or unbounded recycling.

## Finite check

`scripts/verify_geometric_cross_star_line_incidence.py` exhausts small board lines and all three
cross-star profiles, then samples weighted tuple families.  It checks unique line addresses, the
axis split, the `binom(N^2,2)` line stock, the at-most-`N` line occupancy and every repeated-cell
incidence inequality.