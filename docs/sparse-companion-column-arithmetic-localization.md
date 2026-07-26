# Arithmetic localization of singleton companion-column concentration

**Branch:** `research/sparse-algebraic-spread`

SAS5ay--SAS5bc reduce the weighted singleton reflected-defect route to either a
whole-fibre donor batch or one exact donor-labelled companion column `q` which occurs
in a quantified family of defect fibres.  The companion concentration is not
geometrically diffuse.  Inside one primitive singleton shape, the fixed companion
column determines the dilation parameter and hence the defect column uniquely.

This note turns the companion obstruction into one heavy exact defect fibre after
only the finite primitive-shape loss from SAS5r.

## Fixed singleton role

Fix one original swapped column `x`, one singleton mirror word and one failing
non-swapped position.  Let the other non-swapped position be the companion role.
For a record with primitive row shape `(A_0,B_0)`, the two non-swapped columns are

`c_j=x+A_0*s`,

`c_k=x+B_0*s`

for one nonzero integer parameter `s`, as in SAS5q.

The word and failing role determine whether the defect is at `j` and the companion at
`k`, or vice versa.

## SAS5bd -- exact inversion from a fixed companion column -- PROVED

Fix a donor-labelled companion column `q`.

1. If the defect is at `j` and the companion is at `k`, a record of primitive shape
   `(A_0,B_0)` with companion `q` exists only when

   `B_0 | (q-x)`.

   Then

   `s=(q-x)/B_0`

   and the defect column is uniquely

   `z=x+A_0*(q-x)/B_0`.

2. If the defect is at `k` and the companion is at `j`, existence requires

   `A_0 | (q-x)`,

   after which

   `s=(q-x)/A_0`

   and

   `z=x+B_0*(q-x)/A_0`.

In either orientation, the fixed data `(x,q,A_0,B_0,word,defect role)` determine at
most one integer parameter and at most one defect column.

### Proof

Substitute the fixed companion value into the primitive-dilation equations.  The
appropriate primitive coefficient must divide `q-x`; division gives the unique
integer parameter, and substitution into the other arm gives the unique defect
column. QED.

Board range, distinctness and colour conditions may rule out this reconstructed
record but cannot create a second one.

## Canonical companion witnesses

Fix the exact companion column `q` returned by SAS5bb.  For every retained defect
fibre `F_z` whose companion obstruction set contains `q`, choose the least exact
record in `F_z` having companion `q`.  Assign the fibre the primitive shape of that
canonical witness.

## SAS5be -- primitive shape injects companion-obstructed fibres -- PROVED

Two distinct defect fibres assigned the same primitive shape are impossible.
Consequently the number of distinct fibres in one fixed-`q` companion concentration
is at most

`4*(N-1)^2`.

### Proof

The original swapped column, companion column, singleton word and failing role are
fixed.  SAS5bd says one primitive shape reconstructs at most one defect column.
Distinct fibres have distinct defect columns, so the shape assignment is injective.
SAS5r bounds the primitive-shape dictionary by `4(N-1)^2`. QED.

No exact row scale or base row is needed for this fibre-level injectivity.
Different row triples with the same primitive shape and parameter all belong to the
same reconstructed defect fibre.

## SAS5bf -- weighted fixed-companion concentration gives one heavy fibre -- PROVED

Let a fixed companion column `q` obstruct a family of distinct defect fibres of total
fibre load `V>0`.  Then one exact defect fibre has load at least

`V/[4*(N-1)^2]`.

The same fibre comes with a canonical primitive shape and an exactly reconstructed
dilation parameter from SAS5bd.

### Proof

Assign every fibre its canonical witness shape.  SAS5be makes the assignment
injective into at most `4(N-1)^2` shapes.  Weighted pigeonhole gives the bound. QED.

## SAS5bg -- quantitative import from the singleton companion router -- PROVED

In the bad branch of SAS5bc, one exact companion column obstructs fibres of total load
strictly greater than

`h*W/(2*b*d)`.

Therefore one exact defect fibre has load strictly greater than

`h*W/[8*b*d*(N-1)^2]`.

### Proof

Apply SAS5bf to the companion concentration returned by SAS5bc and substitute its
lower bound. QED.

This is fibre load, not necessarily the total weight of records using the selected
companion `q`.  The theorem uses the companion only to reconstruct the defect fibre.

## SAS5bh -- heavy-fibre repair or donor-companion saturation -- PROVED WITH ORIGINAL-SWAP COMPOSITION

Let `F_z` be the heavy exact fibre supplied by SAS5bf or SAS5bg.  Exactly one of the
following holds:

1. there is a donor

   `r in D_ell \ ({x,y} union C_z)`,

   and the composed move `omega union {z,r}` repairs the entire fibre;
2. no such donor exists, and every donor outside the original swap appears as a
   companion somewhere in the fibre:

   `D_ell\{x,y} subseteq C_z`.

   In particular

   `|C_z\{x,y}|>=d-2`.

### Proof

If a safe donor exists, SAS5ay gives outcome 1.  Otherwise every donor outside
`{x,y}` lies in the obstruction set by definition, proving outcome 2. QED.

The saturation outcome is an exact one-fibre arithmetic obstruction: a single defect
column supports records whose companion set covers the complete available donor class
outside the original swap.

## Corrected SAS6 frontier

The singleton weighted obstruction has now been compressed twice:

- SAS5bc returns one companion column shared across a weighted fibre family;
- SAS5bd--SAS5bg turn that family into one heavy exact defect fibre;
- SAS5bh either repairs that fibre or proves near-complete donor-companion saturation
  inside it.

The remaining arithmetic work is to classify the row-triple/dilation set within one
saturated fibre, compare the combined move with the original energy, and handle high
incidence and board-boundary profiles.

## Finite check

`scripts/verify_sparse_companion_column_arithmetic.py` exhausts small primitive shapes,
fixed swapped and companion columns, both defect orientations and board ranges.  It
checks divisibility, unique parameter/defect reconstruction, shape injectivity,
weighted fibre localization and the safe-donor/saturation dichotomy.