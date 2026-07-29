# Paid replenishment source bank

**Branch:** `research/bounded-denominator-absorbers`

BDA5ca--BDA5ce bound large balanced-floor restorations by a finite initial positive-source mass. This note allows replenishment, provided every deposit is itself recorded and paid by an external bank.

## Source account

Fix a same-dictionary epoch and a cycle-length cap `L>=2`. Let `C_0>=0` be the initial positive numerator-source mass. A replenishment event deposits an exact amount `r>=0`; write

\[
R_{\rm tot}=\sum r.
\]

A negative restoration jump of size `J` consumes

\[
c(J)=\left\lceil\frac{J}{L-1}\right\rceil
\]

units from the source account, as supplied by BDA5bv--BDA5bz. The account may never become negative.

## BDA5cf -- exact replenished mass inequality -- PROVED

For every prefix of the epoch,

\[
\sum_{\text{restorations}} c(J)
\le C_0+\sum_{\text{deposits}}r.
\]

### Proof

This is the nonnegativity invariant of the exact source account after adding every recorded deposit and subtracting every restoration cost. QED.

## BDA5cg -- thresholded restoration count -- PROVED

For `J_0>=1`, the number `N_{>=J_0}` of restoration jumps satisfying `J>=J_0` obeys

\[
\boxed{
N_{\ge J_0}
\le
\left\lfloor
\frac{C_0+R_{\rm tot}}
{\lceil J_0/(L-1)\rceil}
\right\rfloor.
}
\]

### Proof

Every selected restoration consumes at least `ceil(J_0/(L-1))` source units. Apply BDA5cf. QED.

## BDA5ch -- dyadic replenishment bank -- PROVED

For every dyadic bin `2^b<=J<2^{b+1}`,

\[
N_b
\le
\left\lfloor
\frac{C_0+R_{\rm tot}}
{\lceil2^b/(L-1)\rceil}
\right\rfloor.
\]

Thus unbounded jump size is harmless when replenishment mass is globally paid.

## BDA5ci -- replenishment router -- PROVED UNDER THE PAID-DEPOSIT CONTRACT

Every replenishment has one continuation:

1. debit a finite external collateral or source bank by its exact deposit amount;
2. consume a capacity-one deposit ticket;
3. strictly lower a declared denominator, valuation, depth or owner potential;
4. or return an explicit reset in source dictionary, multiplicity, lineage or payment interpretation.

If the external deposit bank has finite total capacity `B`, then `R_tot<=B`, and BDA5cg--BDA5ch give finite restoration counts.

## BDA5cj -- BDA6 interface -- PROVED UNDER COMPLETE SOURCE LINEAGE

Large balanced-floor recurrence is now localized to an exact pair of resources:

- one negative restoration edge;
- and the positive source mass or paid replenishment that compensates it.

No arbitrary repeated large-jump word remains. A proof need only pay, descend, ticket or rule out the selected source/restoration address. Genuinely free or cyclically self-replenishing sources are returned as the remaining obstruction.

## Finite check

`scripts/verify_bda_paid_replenishment_bank.py` generates source epochs with exact deposits and restoration costs and verifies the prefix mass invariant, thresholded count and dyadic lower-cost bounds.