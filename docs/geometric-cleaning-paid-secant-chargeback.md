# Incidence-resolved payment and recurrent secant chargeback

**Branch:** `research/geometric-cleaning`

GC2c--GC2f turn a dense family of line-blocked partners into a current-anchor
star or an endpoint-disjoint current-secant matching.  Those outputs are still
latent unless they retain actual destroyed syndrome weight.  The all-`n`
orbit-phase branch contains the exact payment mechanism needed here: correction
gain is transferred to current violated factors through occurrence-faithful
incidences, and a recurrent finite factor fibre charges back to one executable
improving correction.

This note imports that mechanism in branch-neutral form.  It does **not** declare
a prospective secant payable merely because it blocks an insertion.  A line
witness enters the paid router only through a current source factor and an exact
correction--factor charge.

## Current correction and defect incidence

Fix one geometric-cleaning snapshot.  Let `I` be a finite family of individually
hard-legal row--column-preserving corrections.  Correction `i` has exact gain

\[
g_i=\Phi(S)-\Phi(S_i)>0.
\]

Let `D` be the current violated geometric factors, each of weight `w_Q>0` and
scope rank at most `r`.  Write `i~Q` when correction `i` destroys `Q`, and put

\[
D_i=\sum_{Q:i\sim Q}w_Q.
\]

Assume

\[
g_i\le D_i,
\]

which is the exact destroyed-minus-created identity with nonnegative collateral,
and assume each current factor is incident to at most `r` corrections.  This
last condition holds when correction supports are pairwise disjoint and a
rank-`r` factor can meet at most one correction per scope point.

## GC2g -- factor-conservative current payment -- PROVED

Define

\[
\kappa=
\max_Q\sum_{i:i\sim Q}\frac{g_i}{D_i},
\qquad
K=\max\{1,\kappa\},
\]

and for every incidence put

\[
\boxed{
a_{iQ}=\frac{g_iw_Q}{KD_i}.
}
\]

Then:

1. every correction sends total charge `g_i/K`;
2. every current factor receives charge at most its current weight;
3. with `G=sum_i g_i`, the total factor-conservative payment is
   
   \[
   \boxed{
   P=\sum_Q\sum_i a_{iQ}=\frac GK\ge\frac Gr.
   }
   \]

### Proof

Summing over the neighbourhood of `i` gives

\[
\sum_{Q:i\sim Q}a_{iQ}
=
\frac{g_i}{KD_i}
\sum_{Q:i\sim Q}w_Q
=
\frac{g_i}{K}.
\]

For fixed `Q`, its received charge is

\[
\frac{w_Q}{K}
\sum_{i:i\sim Q}\frac{g_i}{D_i}
\le w_Q.
\]

Since `g_i/D_i<=1` and at most `r` corrections meet one factor,
`kappa<=r`, hence `K<=r`. QED.

For collinear triples one may take `r=3`, giving payment at least one third of
the total correction gain.

## GC2h -- paid current factors give a star or point-disjoint matching -- PROVED

Let a finite family `F` of distinct current violated collinear triples carry
factor-conservative payments `p_F>0`, with total

\[
P=\sum_Fp_F.
\]

For a selected point `z`, define

\[
L(z)=\sum_{F:z\in F}p_F.
\]

Fix thresholds `lambda,mu>0`.  Then one of the following occurs:

1. one factor has `p_F>mu`;
2. one point has paid load `L(z)>lambda`, and its star contains at least
   
   \[
   \boxed{
   \left\lfloor\lambda/\mu\right\rfloor+1
   }
   \]
   
   distinct factors;
3. there is a point-disjoint factor family of size at least
   
   \[
   \boxed{
   \left\lceil\frac{P}{3\lambda}\right\rceil.
   }
   \]

Every returned factor remains current and retains its exact payment and source
correction incidences.

### Proof

Return the heavy factor if present.  Otherwise a point load exceeding `lambda`
needs more than `lambda/mu` factors.  If every point load is at most `lambda`,
greedily choose one remaining triple and delete every triple meeting it.  Each
step deletes payment at most the sum of the three point loads, hence at most
`3lambda`.  The selected triples are point-disjoint and their deletion classes
partition the family, proving the bound. QED.

This is the paid analogue of GC2c--GC2f.  The star or matching consists of
current violated factors, not merely current secants supporting prospective
blockers.

## GC2i -- recurrent paid fibres charge back to executable descent -- PROVED

Let `S` be any nonempty subfamily of `b` current factors with total actual
payment

\[
W=\sum_{Q\in S}\sum_i a_{iQ}>0.
\]

Then some incident correction satisfies

\[
\boxed{
g_i\ge\frac{W}{rb}.
}
\]

Executing it decreases the current potential by at least `W/(rb)`.

### Proof

The payment on `S` is a sum of at most `rb` nonzero correction--factor charges,
because each of the `b` rank-`r` factors meets at most `r` corrections.  One
charge is at least `W/(rb)`.  Its correction row has total charge at most `g_i`,
so the same lower bound holds for the correction gain.  The correction was
assumed current, hard-legal and row--column preserving. QED.

Consequently, if a role-tagged star or matching signature has fibre capacity at
most `B`, a recurrent current fibre of payment `W` gives immediate descent at
least `W/(rB)`.

## Role-tagged paid-secant ledger

For every paid star or matching returned by GC2h, retain a state-qualified
record

\[
(\text{snapshot},\text{role},\text{geometric signature}),
\]

where the role distinguishes at least:

- `current-defect-star`;
- `current-defect-matching`;
- `latent-line-star`;
- `latent-line-matching`.

The last two roles receive **zero current payment** unless an explicit source
map converts them to the first two roles.  Equal slopes, lines or endpoint pairs
do not identify a latent blocker with a current violated factor.

## GC2j -- conditional closure of the latent-to-paid secant interface -- PROVED UNDER THE SOURCE-PAYMENT CONTRACT

Suppose every GC2c--GC2f latent line-blocker output is handled by one of:

1. it already contains a current violated source factor and an
   occurrence-faithful charge from GC2g;
2. a source-transfer theorem maps its witnesses to a current factor family,
   without duplicating factor weight, and retains correction incidences;
3. it consumes a capacity-one protected-line or source-transfer ticket;
4. it is passed as an explicitly unpaid structured core to the alternating
   branch.

Assume also that every paid role-tagged signature fibre has finite capacity.
Then the paid part cannot recur indefinitely:

- a first paid signature strictly grows the finite ledger;
- a recurrent paid fibre gives executable descent by GC2i;
- a ticketed transfer consumes finite capacity;
- an unpaid output remains visibly unpaid and cannot be used in a decrease
  estimate.

### Proof

GC2g makes payment factor-conservative.  GC2h routes every paid factor family to
a heavy factor, star or matching.  First exposure grows the finite role-tagged
ledger.  On recurrence, finite fibre capacity and GC2i give strict current
descent.  Ticketed transfers are finite.  The fourth route asserts no payment
and therefore cannot be recycled as if it had destroyed current syndrome. QED.

## Corrected GC2 frontier

The orbit-phase all-`n` progress is useful, but at a precise point.  It closes
**recurrence after current payment has been installed**.  The remaining GC2
obligation is now the source-transfer theorem itself:

- connect a latent dangerous secant to current destroyed factors;
- preserve occurrence identity and correction provenance;
- avoid counting one current factor through several latent line witnesses;
- or return the latent family unpaid to an arithmetic/alternating classifier.

Thus the phrase "latent-to-paid conversion" has an exact mathematical meaning:
construct the GC2g charge matrix, or prove a capacity-respecting transfer into
one.

## Finite check

`scripts/verify_geometric_paid_secant_chargeback.py` exhausts small nonnegative
correction--factor charge systems of rank at most three and small weighted
three-uniform factor families.  It checks factor capacities, the `G/r` payment
bound, the star/matching alternative and the `W/(rb)` recurrent chargeback.