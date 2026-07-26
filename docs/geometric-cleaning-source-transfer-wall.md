# Source-disjoint latent secants and the bounded-congestion transfer bridge

**Branch:** `research/geometric-cleaning`

GC2c--GC2f extract a current secant pair `{a,c}` and a prospective cross-cell
`rho` on one dangerous non-axis line.  GC2g--GC2j explain how a family closes
after current payment has been installed.  The missing implication cannot be a
direct same-line charge: the rectangle geometry forces the dangerous line to
avoid both removed cells.

This note proves that obstruction exactly and isolates the only viable payment
interface.  A latent witness must transfer to a *different* current factor, with
occurrence identity and bounded source congestion, or remain unpaid.

## Rectangle notation

Fix distinct current cells

`b=(r_b,c_b)` and `u=(r_u,c_u)`

in one permutation layer.  The rectangle correction removes `b,u` and inserts

`x=(r_b,c_u)` and `y=(r_u,c_b)`.

A line-blocker witness consists of one role `rho in {x,y}`, one non-axis line
`L`, and two surviving current cells `a,c` such that `a,c,rho` are collinear on
`L`.

## GC2k -- the dangerous secant line avoids both removed cells -- PROVED

For either cross-cell role, the non-axis witness line `L` contains neither `b`
nor `u`.

### Proof

If `rho=x`, then `x` and `b` lie on the same row and are distinct.  A non-axis
line meets that row in at most one point, so `b` is not on `L`.  Likewise `x`
and `u` lie on the same column and are distinct, while a non-axis line meets
that column in at most one point, so `u` is not on `L`.

The argument for `rho=y` is the same with the row and column roles exchanged.
QED.

Consequently the created triple `{a,c,rho}` is disjoint from the two deleted
cells.

## GC2l -- no same-line destroyed-factor payment -- PROVED

Every current factor destroyed by the rectangle correction contains `b` or
`u`.  Therefore no destroyed current collinear triple can be the dangerous
same-line triple `{a,c,rho}`, and no destroyed current triple supported on `L`
can contain the witness pair `{a,c}`.

### Proof

The correction changes membership only at `b,u,x,y`.  A current factor not
containing either removed cell remains present after the deletion step, so it
is not destroyed.  Hence every destroyed current factor contains `b` or `u`.
By GC2k neither removed cell lies on `L`.  Since `a,c` determine `L`, any
collinear triple containing both `a,c` lies on `L` and cannot contain `b` or
`u`. QED.

Thus a source-transfer theorem cannot preserve the witness pair.  It must use
another current factor incident with the correction.

## GC2m -- source-free latent-secants exist -- PROVED

There is a line-blocked rectangle correction which creates a collinear triple
but destroys no current collinear triple.

Take

- `b=(0,0)`;
- `u=(1,1)`;
- `x=(0,1)` and `y=(1,0)`;
- `a=(2,5)` and `c=(3,7)`.

The four current cells `{b,u,a,c}` contain no collinear triple.  The non-axis
line through `a,c` has equation `column=2*row+1`, so it also contains `x`.
After the correction, `{x,a,c}` is collinear.  Therefore the latent witness has
positive blocker weight while the same correction has zero destroyed current
syndrome weight.

### Proof

The six determinants for triples from `{b,u,a,c}` are nonzero by direct
substitution.  The displayed line contains `(0,1),(2,5),(3,7)`. QED.

This refutes every unconditional rule that assigns positive current payment to
a line blocker solely from `(b,u,rho,L,{a,c})`.

## Cross-line source maps

Let `W_lat` be a finite family of latent witnesses for current corrections.
Witness `w` has nonnegative latent weight `lambda_w`.  Let `D_cur` be current
destroyed factors with syndrome capacities `omega_Q`.

A **cross-line source map** is a map `sigma:W_lat -> D_cur` such that:

1. `sigma(w)` is destroyed by the same current correction as `w`;
2. the exact correction--factor incidence is retained;
3. `sigma(w)` need not lie on the dangerous line and need not contain its
   witness pair;
4. for some congestion constant `M>=1`, every current factor satisfies

   `sum_{w:sigma(w)=Q} lambda_w <= M * omega_Q`.

## GC2n -- bounded-congestion source transfer -- PROVED

Under a cross-line source map of congestion `M`, the scaled latent charges

`p_w=lambda_w/M`

are factor-conservative current payment.  Their total paid mass is exactly

`sum_w p_w = (sum_w lambda_w)/M`.

Every paid star or matching extracted from these charges retains exact current
source-factor and correction provenance, so GC2h--GC2j apply without further
loss except the factor `M`.

### Proof

For one current factor `Q`,

`sum_{w:sigma(w)=Q} p_w = (1/M) sum_{w:sigma(w)=Q} lambda_w <= omega_Q`.

Thus no current syndrome capacity is duplicated.  Summing over all witnesses
gives the total-mass identity.  Conditions 1 and 2 preserve the incidence rows
needed by GC2i chargeback. QED.

## Corrected GC2 frontier

The latent-to-paid problem is now exactly one of the following.

1. Construct a cross-line source map with polynomial or constant congestion.
2. Consume a capacity-one protected-line/source-transfer ticket.
3. Return the latent family unpaid to an arithmetic or alternating classifier.

The dangerous line itself cannot be its payment source.  Any future proof must
identify a different destroyed factor and prove that one factor is not reused
by too many latent witnesses.

## Finite check

`scripts/verify_geometric_source_transfer_wall.py` checks the row/column
exclusion in GC2k, the explicit GC2m coordinates, and every small integer
bounded-congestion charge matrix for GC2n.