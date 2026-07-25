# Frozen-switch external blocker forest

PX319--PX323 close the packet-specific linear residue by using the exact blocker
list of one correcting transposition.  The same countdown extends to a general
frozen deterministic switch only after separating **external blockers**, which
use one or two new cells and can be neutralized by moving fixed witnesses, from
**internal blockers**, which use three new cells and cannot be suppressed while
all inserted switch cells remain frozen.

This distinction is essential.  The external first-order sectors admit a finite
causal blocker forest whenever old destruction exceeds the internal rank-three
load.  Internal support three remains governed by the thinning and terminal
rank-three ledgers PX201--PX204 and PX260--PX276.

## 1. Exact frozen-switch ledger

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

## 2. External and internal blocker sectors

For `T in B_sigma`, define its new-cell support by

\[
r(T)=|T\cap W|.
\]

### Theorem PX325 -- PROVED

Every blocker has `1<=r(T)<=3` and belongs to exactly one sector.

1. `r=1`: one prospective cell and two fixed points -- a prospective clean-star
   ray centred at the new cell.
2. `r=2`: two prospective cells and one fixed point -- a pair-line/radial
   certificate.
3. `r=3`: three prospective cells -- an internal rank-three certificate of the
   inserted switch block.

Let

\[
B_\sigma^{\rm ext}=\{T:r(T)\le2\},
\qquad
B_\sigma^{\rm int}=\{T:r(T)=3\},
\]

and write their sizes as `c_ext` and `c_3`, so

\[
c_\sigma=c_{\rm ext}+c_3.
\]

### Proof

A new triple must contain at least one inserted cell, otherwise it was already
present in `S`.  A triple has exactly three cells, giving the support range and
the exhaustive classification. \(\square\)

Support-one and support-two blockers can be neutralized while preserving `W` by
moving one of their fixed witnesses.  A support-three blocker contains only
cells of `W`; it cannot be removed under a genuinely frozen `W` interface.

## 3. Exact external blocker countdown

Work under the frozen-switch child interface for external blockers:

1. the rows and columns of `A` and `W` remain reserved;
2. a chosen support-one or support-two blocker is neutralized by a deeper
   clean-star or pair-line child;
3. previously suppressed blockers stay absent by PX278;
4. every new obligation is assigned to a deeper level.

### Theorem PX326 -- PROVED

Assume

\[
\boxed{d_\sigma>c_3.}
\]

Then the switch satisfies an exact external strict-sign-or-child countdown.

1. If `d_sigma>c_ext+c_3`, execute the switch immediately.
2. Otherwise, after suppressing any

   \[
   \boxed{
   b_\sigma=c_{\rm ext}+c_3-d_\sigma+1
   }
   \]

   distinct external blockers, the switch becomes strictly improving.

Moreover `1<=b_sigma<=c_ext`.

### Proof

The immediate case is PX324.  In the second case,
`d_sigma<=c_ext+c_3` gives `b_sigma>=1`, while `d_sigma>c_3` gives
`b_sigma<=c_ext`.  After suppressing `b_sigma` external blockers, the remaining
creation count is at most

\[
c_{\rm ext}+c_3-b_\sigma=d_\sigma-1.
\]

PX324 gives potential change at most `-1`. \(\square\)

### Corollary PX327 -- PROVED

Under `d_sigma>c_3`, every frozen switch satisfies the strict-sign-or-child
interface of PX280 using only support-one and support-two children.  At most
`b_sigma` child conversions are required before the original switch executes.

### Proof

Before the budget is exhausted, choose one unsuppressed external blocker.
PX325 identifies it as a clean-star-ray or pair-line child.  Each conversion
lowers the current external-blocker coordinate by one, and PX278 prevents
recurrence.  PX326 executes the switch when the budget is exhausted. \(\square\)

## 4. Exact remaining obstruction

### Corollary PX328 -- PROVED

Packet correcting transpositions have `|W|=2`, hence `c_3=0`.  Their complete
blocker forest PX319--PX323 is therefore an unconditional special case of
PX326--PX327.

For a general clean-star, radial, coordinate-field, or loaded-line switch, one
of the following holds.

1. `d_sigma>c_3`, and all external first-order debt is discharged by the finite
   blocker forest.
2. `c_3>=d_sigma`, so internal rank-three creation alone is large enough to pay
   the old destruction and is the unique remaining sign obstruction.

### Corollary PX329 -- PROVED REDUCTION

The general support-one and support-two first-order bookkeeping problem is
closed under the frozen-switch interface.  The remaining recursive frontier is
exactly:

1. internal support-three load `c_3>=d_sigma`, handled structurally or by the
   PX201/PX260 rank-three decoders;
2. constant-order trajectory residuals of order at most `Delta_0+1` from
   PX315--PX318;
3. terminal obstruction certificates surviving the exact optimizer.

Exact all-side closure still requires proving that these internal/terminal
obstructions are absorbable or incompatible with the product induction.

## 5. Verification

Run

```bash
python scripts/verify_product_universal_blocker_forest.py
```

The verifier exhausts destruction, external-creation, and internal-creation
counts, confirms the exact external blocker budget under `d_sigma>c_3`, checks
all support partitions of a three-cell certificate, and simulates the finite
causal countdown.
