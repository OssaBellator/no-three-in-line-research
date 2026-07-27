# Polynomial physical address stock for non-scalar bounded-denominator profiles

**Branch:** `research/bounded-denominator-absorbers`

BDA5as--BDA5au terminate every transition cycle made only from physical
`h <-> h+q` moves and strict effective-denominator descent.  The remaining
same-denominator frontier contains a genuinely non-scalar change: a primitive
direction, transverse direction, anchor, residue, or finite role changes while
the reduced denominator stays fixed.

This note does not terminate recurrence of one exact address.  It proves that,
under the board-realization contract used by the absorber, every such address
belongs to an explicit polynomial dictionary.  Hence a long same-denominator
history must repeat one exact physical address; it cannot escape through an
unnamed or super-polynomial arithmetic alphabet.

## Physical direction universe

Work on an `n x n` board, `n>=2`, and put `M=n-1`.  Normalize every nonzero
integer direction by dividing by the gcd of its coordinates and changing sign
so that its first nonzero coordinate is positive.  Let

\[
\mathcal D_M=
\{(x,y):1\le x\le M,\ |y|\le M,\ \gcd(x,|y|)=1\}
\cup\{(0,1)\},
\]

and write `N_M=|D_M|`.

## BDA5av -- physical directions and determinants -- PROVED

Every primitive direction determined by two board cells lies in
`D_M`.  Consequently

\[
\boxed{N_M\le M(2M+1)+1.}
\]

For any two physical primitive directions `d,e`,

\[
\boxed{|\det(d,e)|\le 2M^2=2(n-1)^2.}
\]

### Proof

A coordinate difference of two board cells has absolute value at most `M`.
Dividing by the common gcd cannot increase either coordinate, and the sign
normalization gives either a positive first coordinate or the unique vertical
direction `(0,1)`.  The displayed count is the ambient number of such pairs.
For `d=(a,b)` and `e=(c,d')`,

\[
|\det(d,e)|=|ad'-bc|\le |ad'|+|bc|\le2M^2.
\]

QED.

## Determinant-realized parameters

Call a reduced rational parameter determinant-realized when it is the reduction
of

\[
\frac{\det(d_1,e_1)}{\det(d_2,e_2)},
\qquad \det(d_2,e_2)\ne0,
\]

for physical primitive directions.  This is the contract satisfied when the
bounded denominator is obtained from the actual collinearity determinant of
board cells.

## BDA5aw -- reduced denominator ceiling -- PROVED

Every nontrivial determinant-realized reduced denominator satisfies

\[
\boxed{2\le q\le Q_{\rm det}:=2(n-1)^2.}
\]

The absolute value of the reduced numerator obeys the same ceiling.

### Proof

Before cancellation, numerator and denominator are nonzero determinants of
absolute value at most `2M^2` by BDA5av.  Reduction can only decrease their
absolute values.  QED.

## BDA5ax -- polynomial physical BDA profile stock -- PROVED UNDER THE DETERMINANT-REALIZATION CONTRACT

Assume an arithmetic profile records

\[
\pi=(q,d,e,\xi),
\]

where `2<=q<=Q_det`, `d,e in D_M`, and `xi` is a scalar residue modulo `q`.
Then the total exact profile stock is at most

\[
\boxed{
L_{\rm phys}(n)
=N_M^2\sum_{q=2}^{Q_{\rm det}}q
\le N_M^2\frac{Q_{\rm det}(Q_{\rm det}+1)}2
=O(n^8).
}
\]

For one fixed denominator `q`, the sharper stock is

\[
\boxed{qN_M^2=O(n^6).}
\]

### Proof

Choose the two primitive directions and one of the `q` scalar residues.  Sum
over the determinant-realized denominators.  Since `N_M=O(n^2)` and
`Q_det=O(n^2)`, the total is `O(n^8)`.  QED.

## BDA5ay -- complete same-denominator physical address stock -- PROVED UNDER THE BOARD-ANCHOR/FINITE-ROLE CONTRACT

Let `L_ext` bound all remaining finite decorations at one occurrence: current
or created rank, channel word, role word, bank type, owner route, closure role,
and any other already proved finite label.  Assume the anchor is a board cell.
For fixed `q`, the complete physical non-scalar address stock is at most

\[
\boxed{
N_{\rm ns}(q)\le n^2L_{\rm ext}\,qN_M^2.
}
\]

Across all determinant-realized denominators,

\[
\boxed{
N_{\rm ns}^{\rm tot}
\le n^2L_{\rm ext}N_M^2
\frac{Q_{\rm det}(Q_{\rm det}+1)}2
=O(L_{\rm ext}n^{10}).
}
\]

Therefore a weighted family of physical same-denominator episodes of total
weight `W` contains one exact address of weight at least

\[
\boxed{W/N_{\rm ns}^{\rm tot}.}
\]

### Proof

Choose the board anchor, external role, denominator, two primitive directions,
and scalar residue.  Multiplication gives the fixed-denominator bound and
summation gives the total bound.  Weighted pigeonhole gives the final claim.
QED.

## Consequence for BDA6

The physical same-denominator frontier now has an explicit dichotomy.

1. Some arithmetic field is not reconstructed from a board anchor,
   determinant-realized denominator, physical directions, and a finite role
   word; this is a named realization gap.
2. One exact address from a polynomial dictionary recurs.

The second case must still be paid, descended, erased, or ticketed.  This note
therefore closes the address-alphabet task, not the global transition-cycle
termination theorem.

## Finite check

`scripts/verify_bda_physical_address_stock.py` enumerates normalized primitive
directions on boards through side eight, checks every determinant and every
reduced determinant ratio, verifies the denominator ceiling, and compares the
exact profile counts with the displayed ambient bounds.
