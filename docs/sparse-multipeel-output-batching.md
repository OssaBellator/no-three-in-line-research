# Batching the outputs of heavy active-record peeling

**Branch:** `research/sparse-algebraic-spread`

SAS5dh--SAS5dl convert each nonimproving heavy active record into one of four positive outputs:
an original-swap repair word, a donor-swap repair word, designated divisor-scale mass or a
positive mixed-curvature fibre.  This note aggregates those outputs over a complete sequence of
one-or-two-donor peel steps.

The key point is bounded exact-record reuse.  A rank-three record can be repaired by at most three
pairwise endpoint-disjoint donor swaps.  A positive mixed-curvature record relative to the fixed
original swap meets at most two donors.  Hence donor-word and positive-fibre outputs cannot be
reused across an arbitrarily long peel.

## Peel sequence and output mass

Fix the original swap `omega` and an endpoint-disjoint donor bank.  Consider a peel sequence

`j=1,...,p`

from SAS5dg/SAS5dl.  Step `j` chooses a distinct active exact record `Q_j` of weight `Omega_j` and
deletes its one or two incident donors.  Hence the canonical donor selected at distinct steps is
distinct.  The number of steps satisfies

`p<=K_0`,

where

`K_0=24*binom(N,3)*(N-2)^2`.

If a step gives an improving composed move, the process terminates.  Otherwise SAS5dk assigns it
one of four output types:

- `O`: an original-swap repair word of weight at least `Omega_j/48`;
- `D`: a donor-swap repair word of weight at least `Omega_j/48`;
- `L`: designated divisor-scale repair mass at least `Omega_j/4`;
- `P`: a positive-curvature endpoint-pair/orientation/scope-type fibre of weight at least
  `Omega_j/96`.

Let `M_O,M_D,M_L,M_P` be the sums of `Omega_j` over the corresponding step types, and put

`Omega_peel=M_O+M_D+M_L+M_P`.

## SAS5dm -- donor-repair record reuse is at most three -- PROVED

Let `T` be a pairwise endpoint-disjoint donor family.  Fix one exact rank-three record `Q`.  The
number of donors `tau in T` for which swapping `tau` repairs `Q` is at most three.

### Proof

A swap can change the satisfaction of `Q` only if at least one of its endpoints belongs to the
three-column scope of `Q`.  Distinct donors have disjoint endpoint sets, so distinct repairing
donors require distinct scope columns.  There are only three.  In the two-mismatch repair case,
both mismatched columns must be the two endpoints of one donor, which only improves the bound.
QED.

Consequently, if selected donor-repair families over distinct donors have total weighted mass
`R_sel`, the union of their exact record signatures has weight at least `R_sel/3`.

## SAS5dn -- positive-curvature reuse is at most two -- PROVED

Fix the original swap `omega`.  One exact rank-three record with nonzero mixed curvature relative
to `omega` and a donor swap can occur for at most two pairwise endpoint-disjoint donors.

### Proof

Nonzero mixed curvature requires the record scope to meet the endpoint set of `omega` and the
endpoint set of the donor.  Since the scope has rank three and already uses at least one original
endpoint column, at most two scope columns remain.  Pairwise endpoint-disjoint donors require a
distinct remaining scope column. QED.

Therefore selected positive-curvature fibres of total weighted mass `P_sel` have exact-signature
union weight at least `P_sel/2`.

## SAS5do -- aggregate output conversion over a peel sequence -- PROVED

Assume no peel step gives an improving composed move.  Then:

1. **original outputs:** one original-swap repair word has weight at least

   `M_O/(48*K_0)`;

2. **donor outputs:** the selected donor-repair families have total mass at least `M_D/48`;
   one of the twelve repair-word types has selected mass at least `M_D/576`, and its exact-record
   union has weight at least

   `M_D/1728`;

3. **designated-scale outputs:** the total designated repaired scale mass is at least

   `M_L/4`;

4. **positive outputs:** the selected positive-curvature fibres have total mass at least
   `M_P/96`; one of the twenty-four orientation/endpoint-pair/scope-type classes has selected
   mass at least `M_P/2304`, and its exact-record union has weight at least

   `M_P/4608`.

### Proof

For type `O`, one step has `Omega_j>=M_O/p>=M_O/K_0`; apply the local `Omega_j/48` bound.  For type
`D`, sum the local `Omega_j/48` bounds, pigeonhole over twelve repair words, then apply SAS5dm.
For type `L`, sum the local `Omega_j/4` bounds; these are bank scale coordinates attached to
distinct surviving donor steps.  For type `P`, sum the local `Omega_j/96` bounds, pigeonhole over
the twenty-four exact classes of SAS5di, then apply SAS5dn. QED.

The donor and positive branches retain genuine distinct physical record weight, not merely a sum
with hidden reuse.

## SAS5dp -- four-way multi-peel batching router -- PROVED

Assume a nonimproving peel sequence removes active records of total weight `Omega_peel>0`.  Since

`M_O+M_D+M_L+M_P=Omega_peel`,

one output type carries at least `Omega_peel/4`.  Hence at least one of the following holds:

1. one original-swap repair word has weight at least

   `Omega_peel/(192*K_0)`;

2. one donor repair-word type has distinct exact-record union weight at least

   `Omega_peel/6912`;

3. the total designated repaired divisor-scale mass is at least

   `Omega_peel/16`;

4. one positive-curvature orientation/endpoint-pair/scope-type class has distinct exact-record
   union weight at least

   `Omega_peel/18432`.

If an improving composed move appears at any step, it is the fifth immediate output.

### Proof

Choose a largest one of `M_O,M_D,M_L,M_P` and substitute its lower bound
`Omega_peel/4` into SAS5do. QED.

This router is deliberately asymmetric.  Original-swap repair mass is one fixed global object and
therefore loses the peel-count factor `K_0`; donor and positive outputs use bounded exact-record
reuse and retain constants independent of the number of peel steps.

## SAS5dq -- arithmetic continuation of the batched outputs -- PROVED AS AN INTERFACE

Each output of SAS5dp enters an existing exact arithmetic dictionary:

1. original or donor repair words enter the twelve-word decomposition of SAS5j--SAS5l;
2. designated divisor-scale mass enters the primitive progression and saturated donor-class
   machinery of SAS5bi--SAS5br;
3. positive-curvature classes have one of the two exact tables `(1,0,0,0)` or `(0,0,0,1)` and one
   of the same three third-column incidence types used in the negative-cross arithmetic router;
4. an improving composed move lowers the nonnegative integer energy.

Thus a complete heavy-record peel cannot terminate in an unstructured collection of small local
certificates.  It produces one quantitatively heavy word, scale or positive cross class, or an
actual descent.

### Proof

The first three statements are the definitions and exact classifications from SAS5j--SAS5l,
SAS5bi--SAS5br and SAS5di.  The fourth is the energy interpretation of a negative composed
increment.  SAS5dp supplies the quantitative mass. QED.

## Corrected SAS6 frontier

The heavy-record branch now has a complete aggregate output router.  The live tasks are narrower:

- run the rational-address/progression analysis on the heavy donor or original repair-word class;
- classify the positive current-only/composed-only third-column arithmetic;
- exploit the large designated-scale branch against the coprime donor-saturated progression;
- and handle high-incidence and reflected-board boundary profiles.

The peel itself, exact active stock, local scalar conversion and multi-step reuse are no longer
open interfaces.

## Finite check

`scripts/verify_sparse_multipeel_output_batching.py` exhausts small donor-scope incidence systems
and samples weighted peel sequences.  It checks the three-use donor-repair cap, the two-use
positive-curvature cap, all aggregate mass inequalities and the four-way constants in SAS5dp.