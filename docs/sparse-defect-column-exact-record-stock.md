# Exact record stock inside one reflected defect column

**Branch:** `research/sparse-algebraic-spread`

SAS5cr--SAS5cv construct a weighted endpoint-disjoint donor bank once every defect-column
fibre contains at most `K_rec` exact geometric-label record signatures.  This note derives
that stock from the standard-grid geometry instead of leaving it abstract.

Fixing the reflected word, the original swap, the failing non-swapped role and the exact
defect column already fixes two scope columns and their row positions.  The third scope
column is therefore uniquely reconstructed from each row triple.  The only remaining safe
label freedom occurs in a singleton word at the other non-swapped position, and contributes
at most the number `b` of block labels.

## Fixed reflected defect address

Fix:

- an `N x N` standard grid;
- one original cross-label swap `omega={x,y}`;
- one reflected repair word `w` from SAS5z;
- one failing non-swapped row position `h`;
- one exact defect column `z notin {x,y}`;
- one required defect label `ell`;
- a balanced block-colour alphabet of size `b`.

An exact record has increasing rows

`r_1<r_2<r_3`

and one scope column at each row position.  Symbolic aliases with the same rows, columns and
required labels are already merged into one exact signature.

There are two word types.

1. **Double-scope word.**  Both `x` and `y` occur in fixed ordered positions, and `z` is the
   unique non-swapped scope column at position `h`.
2. **Singleton word.**  Exactly one of `x,y`, denoted `s`, occurs in one fixed position; `z`
   occurs at the fixed failing position `h`; the third position is non-swapped.

## SAS5cw -- two fixed columns reconstruct the third column -- PROVED

Fix one increasing row triple and any two distinct row positions whose exact scope columns
are fixed.  There is at most one rational value of the third scope column which makes the
three grid cells collinear.  Hence there is at most one board-valid integer third column.

In particular:

1. a double-scope defect record is completely determined geometrically by its row triple;
2. in a singleton defect record, the fixed swapped column `s` and fixed defect column `z`
   uniquely reconstruct the remaining non-swapped column.

### Proof

This is SAS5k applied to the two fixed cells.  Two distinct points determine one rational
line, and evaluating that line at the third row gives at most one column.  Integrality,
board range and column distinctness only delete candidates. QED.

Thus a singleton fibre has no free `N`-sized companion-column factor after the defect column
and failing role are fixed.

## SAS5cx -- double-scope exact-record stock -- PROVED

Inside one fixed double-scope reflected defect address, the number of exact geometric-label
record signatures at column `z` is at most

`K_double=binom(N,3)`.

### Proof

Choose the increasing row triple in `binom(N,3)` ways.  The word fixes the ordered positions
of `x,y,z`, so the complete scope is fixed.  The repair word fixes the required labels at
`x,y`, and the defect address fixes the required label `ell` at `z`.  Therefore each row
triple contributes at most one exact signature. QED.

## SAS5cy -- singleton exact-record stock -- PROVED

Inside one fixed singleton reflected defect address, the number of exact geometric-label
record signatures at column `z` is at most

`K_single=b*binom(N,3)`.

If the other non-swapped position is certified label-correct in the current colouring, the
sharper bound

`K_single<=binom(N,3)`

holds.

### Proof

Choose the increasing row triple.  SAS5cw uniquely reconstructs the remaining non-swapped
column, if it exists on the board.  The repair word fixes the required label at the swapped
column, and the defect address fixes `ell` at `z`.  Without further information, the required
label at the remaining position has at most `b` choices.  If that position is certified
label-correct, its required label equals the current label of its reconstructed column and is
therefore forced. QED.

The factor `b` is safe even when the canonical defect class records only the least failing
non-swapped position and the later position may also fail.

## SAS5cz -- uniform reflected-defect stock bound -- PROVED

For every fixed reflected word, failing role, exact defect column and defect label,

`K_rec<=b*binom(N,3)`.

For double-scope words and label-certified singleton words,

`K_rec<=binom(N,3)`.

In a balanced colouring with `d` columns of each label and `N=b*d`, the uniform bound may be
written

`K_rec<=(N/d)*binom(N,3)`.

### Proof

Apply SAS5cx or SAS5cy according to the word type.  The balanced-colour reformulation uses
`b=N/d`. QED.

No multiplicity factor appears: repeated symbolic copies of one exact rows/columns/labels
record are one aggregate exact signature by SAS5ch.

## SAS5da -- explicit weighted donor-bank threshold -- PROVED

Use the weighted defect-column notation of SAS5cr--SAS5cv.  Let

`W_Z=sum_z L(z)`,

`k=|Z|`,

`m=min(k,(d-3)_+)`,

and assume `m>0`.  Then the endpoint-disjoint matched donor bank can be chosen with

`L_match>=m*W_Z/[k*b*binom(N,3)]`.

For double-scope or label-certified singleton fibres, the stronger bound is

`L_match>=m*W_Z/[k*binom(N,3)]`.

Under the global column-incidence cap `Lambda`, a simultaneously compatible subbank retains
at least the corresponding quantity divided by `4Lambda+1`.

Consequently the uniform constructed scale-dominance criterion is

`m*W_Z > 2*k*b*binom(N,3)*Omega_cross`.

When it holds, one donor has a positive composed-move barrier at least

`[m*W_Z/(k*b*binom(N,3))-2Omega_cross]/m`.

When it fails, the collateral-dominant branch gives

`Omega_cross>=m*W_Z/[2*k*b*binom(N,3)]`.

The factor `b` is omitted in the sharper word classes.  For a compatible simultaneous
subbank, insert the additional factor `4Lambda+1` in the denominator and threshold.

### Proof

Substitute the stock bound from SAS5cz into SAS5cs, SAS5ct and SAS5cv.  The barrier and
collateral alternatives are exactly the two sides of the aggregate donor-bank threshold.
QED.

## Corrected SAS6 frontier

The weighted reflected-defect construction no longer depends on an unspecified exact-record
stock.  Every fixed defect column has at most `b*binom(N,3)` signatures, and the common
geometric regimes have the sharper `binom(N,3)` stock.  Diffuse defect mass therefore enters
the scale/collateral router through an explicit polynomial inequality.

The remaining sparse work is to exploit the heavy exact cross record forced in the
collateral-dominant branch, continue the coprime donor-saturated progression, and treat the
high-incidence and reflected-board boundary profiles.  Improving the cubic row-triple stock
requires additional arithmetic concentration, not further label bookkeeping.

## Finite check

`scripts/verify_sparse_defect_column_exact_record_stock.py` exhausts small row triples,
reflected word positions, board-valid defect columns and label alphabets.  It checks unique
third-column reconstruction, the double/singleton signature stocks, the label-certified
improvement and the substituted weighted donor-bank threshold.