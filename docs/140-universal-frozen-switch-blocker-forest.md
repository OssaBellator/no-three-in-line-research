# Universal frozen-switch blocker forest

PX319--PX323 close the packet-specific linear residue by using the exact blocker
list of one correcting transposition.  The argument depends only on a frozen
deterministic switch and therefore extends to every clean-star, radial,
coordinate-field, and loaded-line switch.

A fixed switch has an exact old-deletion set and a finite list of prospective
new triples.  Each prospective triple uses one, two, or three new cells.  Once
`C-D+1` blockers are assigned to deeper ancestor-safe children, the original
switch is strictly improving.  This supplies the previously missing general
first-order strict-sign-or-child interface; the remaining issue is the terminal
absorption of the resulting bounded-support children, not another linear
creation estimate.

## 1. Frozen deterministic switch

Let `S` be the current selected state.  A deterministic switch `sigma` deletes a
set `A` of current cells and inserts a disjoint set `W`, preserving the required
row and column counts.  Put

\[
S^\sigma=(S\setminus A)\cup W.
\]

Let `D_sigma` be the set of old collinear triples of `S` meeting `A`, and let
`B_sigma` be the set of new collinear triples of `S^sigma` which are not triples
of `S`.  Write

\[
d_\sigma=|D_\sigma|,\qquad c_\sigma=|B_\sigma|.
\]

### Theorem PX324 -- PROVED

The exact potential change is

\[
\boxed{
\Phi(S^\sigma)-\Phi(S)=c_\sigma-d_\sigma.
}
\]

If a subset `R subseteq B_sigma` is permanently suppressed while the switch
support remains frozen, then

\[
\boxed{
\Phi(S^\sigma_R)-\Phi(S)\le c_\sigma-|R|-d_\sigma.
}
\]

### Proof

Every old triple either avoids `A` and survives unchanged, or meets `A` and is
deleted.  Every triple present after the switch but not before belongs to
`B_sigma`.  These two disjoint changes give the equality.  Suppressing the
members of `R` removes at least `|R|` prospective created triples and cannot add
another triple to the frozen list. \(\square\)

This is the set-theoretic form of the causal ledger PX235--PX239.

## 2. Exact blocker countdown

### Theorem PX325 -- PROVED

If `c_sigma<d_sigma`, execute the switch immediately.  Otherwise, after assigning
and permanently suppressing any

\[
\boxed{
b_\sigma=c_\sigma-d_\sigma+1
}
\]

distinct blockers from `B_sigma`, the switch becomes strictly improving, with
potential change at most `-1`.

### Proof

After suppressing `b_sigma` blockers, PX324 gives

\[
c_\sigma-b_\sigma-d_\sigma=-1.
\]

The number `b_sigma` lies between one and `c_sigma` whenever
`c_sigma>=d_sigma>=1`. \(\square\)

Thus a nonimproving fixed switch has a finite exact debt, not an asymptotic
creation coefficient.

## 3. Every blocker is a bounded-support child

For `T in B_sigma`, define its **new-cell support** by

\[
r(T)=|T\cap W|.
\]

### Theorem PX326 -- PROVED

Every blocker has

\[
\boxed{1\le r(T)\le3.}
\]

It belongs to exactly one of the following geometric sectors.

1. `r=1`: one prospective cell and two fixed points -- a prospective clean-star
   ray centred at the new cell.
2. `r=2`: two prospective cells and one fixed point -- a pair-line/radial
   certificate.
3. `r=3`: three prospective cells -- an internal rank-three certificate of the
   inserted switch block.

### Proof

A new triple must contain at least one inserted cell, otherwise it was already
present in `S`.  A triple has exactly three cells, giving the support range and
the exhaustive classification. \(\square\)

The support-one and support-two sectors are the exact geometric children decoded
by PX228, PX249--PX262, and PX319--PX323.  The support-three sector is included
in the rank-three terminal table of PX273.

## 4. Causal blocker forest

Work under the **frozen-switch child interface**:

1. the rows and columns of `A` and `W` remain reserved while a blocker child is
   neutralized;
2. previously suppressed blockers stay forbidden by the historical-position or
   packet-complement constraints of PX278;
3. every new obligation produced during child neutralization is assigned to a
   deeper level.

### Theorem PX327 -- PROVED

Every frozen switch with `d_sigma>=1` satisfies the strict-sign-or-child
interface of PX280.  At its level it either:

1. executes immediately and strictly decreases the triple potential; or
2. removes one unassigned blocker from the current list and assigns its
   support-at-most-three certificate to a deeper child.

After at most `b_sigma` child conversions, the original switch executes with
strict decrease.

### Proof

Use PX325.  Before the blocker budget is exhausted, choose one unsuppressed
member of `B_sigma`; PX326 makes it a valid bounded-support child.  The frozen
interface and PX278 keep earlier blockers absent.  Each conversion lowers the
current blocker coordinate by one.  Once `b_sigma` blockers have been converted,
PX325 executes the switch. \(\square\)

### Corollary PX328 -- PROVED

Clean-star, radial, coordinate-field, loaded-line, and packet-correction switches
all have a finite causal blocker forest.  Their linear first-order creation
terms cannot cause an infinite same-level loop.

### Corollary PX329 -- PROVED REDUCTION

After PX315--PX318 and PX324--PX328, the remaining recursive frontier consists
of bounded-support terminal obstruction certificates:

1. constant-order trajectory residuals of order at most `Delta_0+1`;
2. support-one, support-two, and support-three blocker children which survive the
   exact terminal optimizer.

The general diffuse clean-star/radial **first-order bookkeeping problem is
closed** under the frozen-switch interface.  Exact all-side closure still
requires showing that the finite terminal obstruction family is absorbable or
incompatible with the product induction.

## 5. Verification

Run

```bash
python scripts/verify_product_universal_blocker_forest.py
```

The verifier exhausts destruction/creation counts, confirms the exact blocker
budget, checks all support partitions of a three-cell prospective certificate,
and simulates finite causal countdowns.
