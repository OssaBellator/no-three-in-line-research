# Exact petal collateral and all-rank closure

**Branch:** `research/alternating-core-chain`

AC3io gives a common-parent menu of edge-petal states, each destroying the same
private pivot bucket of weight `D`.  Its original failure statement used the
union `F` of all boundary-supported candidate triples and therefore left a
fixed-boundary candidate term.  The menu has a stronger exact ledger: in every
selected state, created triples partition into boundary-supported and
petal-specific triples.  Averaging those exact state values produces a realized
rank profile, so neither collateral class remains a static terminal output.

The results below retain all common-parent payment and legality hypotheses of
AC3io.

## Exact statewise partition

Let

\[
S_1,\ldots,S_p
\]

be the legal petal states.  Every state destroys the same certified current
payment `D`.  For state `j`, define:

- `B_j`: exact weight of newly created triples containing no off-boundary
  inserted cell;
- `C_j`: exact weight of newly created triples containing at least one
  off-boundary inserted cell.

The two classes are disjoint and include every newly created triple in `S_j`.
The definition is statewise: a boundary candidate suppressed by a
petal-specific removal contributes zero to `B_j`.

For ranks `r=1,2,3`, also write

\[
B_{j,r},\qquad C_{j,r}
\]

for the exact new-cell-rank subdivisions relative to the common parent state.

## AC3kn -- exact petal-state drift identity -- PROVED

For every `j`,

\[
\boxed{
\Phi(S_j)-\Phi(S)
=
B_j+C_j-D.
}
\]

Moreover,

\[
\boxed{
B_j=\sum_{r=1}^3B_{j,r},
\qquad
C_j=\sum_{r=1}^3C_{j,r}.
}
\]

Under the uniform law on the `p` petal states,

\[
\boxed{
\mathbb E[\text{created collateral}]
=
\frac1p\sum_{j=1}^p(B_j+C_j).
}
\]

This equality strengthens AC3io's safe upper bound

\[
F+\frac1p\sum_j C_j.
\]

The candidate-union quantity `F` remains a valid upper bound on the boundary
expectation but is not needed for failure routing.

### Proof

Every created triple in one state either contains an off-boundary inserted cell
or it does not, giving a disjoint exhaustive partition.  AC3fa assigns each
created triple its exact pre-transition new-cell rank one, two or three.  Every
state destroys the same private payment `D`, so the ordinary created-minus-
destroyed identity gives the first display.  Averaging the exact statewise
partition gives the final equality. QED.

## AC3ko -- failed petal menu realizes half-payment collateral -- PROVED

If some state satisfies

\[
B_j+C_j<D,
\]

that state improves.  If no petal state improves, then

\[
\frac1p\sum_j(B_j+C_j)\ge D.
\]

Consequently at least one of the following holds.

1. **Realized boundary state:** some `j` satisfies
   \[
   \boxed{B_j\ge D/2.}
   \]
2. **Realized off-boundary state:** some `j` satisfies
   \[
   \boxed{C_j\ge D/2.}
   \]

Thus AC3io's alternatives `F>=D/2` and `sum_j C_j>=pD/2` may be replaced, for
execution purposes, by one actual child state carrying at least `D/2` exact
created mass in one category.

### Proof

If no state improves, every `B_j+C_j` is at least `D`, proving the averaged
inequality.  If both category averages were less than `D/2`, their sum would be
less than `D`.  Hence one category average is at least `D/2`, and some state is
at least its category average. QED.

## AC3kp -- boundary and off-boundary mass enter the all-rank pivot adapter -- PROVED

In either outcome of AC3ko, choose the realizing child state and the selected
category.  One rank `r in {1,2,3}` has exact created weight at least

\[
\boxed{D/6.}
\]

The AC3gg--AC3gm orientation and union-safe pivot interface therefore gives,
for every extraction parameter `K>=1`, one of:

- an improving state;
- an explicit complete-envelope overload;
- executable pivot payment at least
  \[
  \boxed{D/(6K)};
  \]
- a next-generation rank return at least
  \[
  \boxed{D/(18K)}.
  \]

The conclusion is identical for boundary-supported and petal-specific
collateral.  The geometric category is retained as a finite role decoration,
not as an unpaid terminal object.

### Proof

The selected category is the sum of its three exact rank classes, so one class
carries at least one third of `D/2`.  The child state realizes that entire rank
class.  Apply the all-rank pivot orientation, compatible extraction and failed-
pivot return to weight at least `D/6`. QED.

## AC3kq -- common-parent petal collateral is closed -- PROVED UNDER AC3io HYPOTHESES

A common-parent paid edge-petal family now has only the following exits:

1. one child state improves;
2. a realized boundary rank enters AC3kp;
3. a realized off-boundary rank enters AC3kp;
4. the AC3kp overload/pivot/next-rank outputs;
5. loss of the common-parent, private-payment or legal-state hypotheses, retained
   as the exact parent/owner/context outer reset.

Therefore fixed-boundary candidate collateral and pairwise petal-specific raw
mass are no longer terminal AC4 entries.  The residual AC3ie/AC3ip work is
precisely to obtain a common-parent paid family or classify the parent/payment
reset; once AC3io applies, its collateral side is total.

### Proof

AC3ko gives improvement or one realized category.  AC3kp routes the realized
category.  If the AC3io hypotheses fail, their changed field is retained rather
than inferred. QED.

## Consequence

The petal menu is now aligned with the other alternative-state banks.  Exact
statewise creation, rather than the union of possible boundary candidates,
feeds the universal rank router.  Edge-disjointness remains useful for
constructing the petal family and identifying off-boundary roles, but no
collateral union term survives after a common-parent paid menu is installed.

## Finite check

`scripts/verify_ac_petal_rank_closure.py` exhausts representative petal menus,
statewise boundary/off-boundary/rank ledgers, exact drift identities, the
half-payment realization alternative and all `D/6`, `D/(6K)`, `D/(18K)`
constants.
