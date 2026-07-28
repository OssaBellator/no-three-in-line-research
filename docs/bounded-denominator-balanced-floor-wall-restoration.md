# Bounded-jump wall restoration for balanced-floor profiles

**Branch:** `research/bounded-denominator-absorbers`

BDA5k--BDA5l localize heavy balanced floors, while BDA5bl--BDA5bp reduce recurrent exact profiles to one least-field restoration gate.  This note identifies the arithmetic shape of that gate when the least field is an integer floor coordinate with bounded numerator jumps.

The theorem is deliberately local.  It does not pay the wall crossing; it replaces an arbitrary balanced-floor cycle by one exact downward crossing with bounded overshoot.

## Floor-coordinate model

Fix a denominator `q>=2`.  Let one complete physical profile contain an integer numerator coordinate `z` and its floor field

\[
f(z)=\left\lfloor\frac zq\right\rfloor.
\]

Along every legal transition, `z` changes by an integer increment `d` satisfying

\[
|d|\le B.
\]

The exact transition address retains the denominator, numerator field, operation word, physical occurrence, role and every payment-sensitive legality field.  A changed denominator, changed numerator interpretation or omitted field is an outer reset.

## BDA5bq -- canonical minimum-floor excursion -- PROVED

Let an exact simple profile cycle have a nonconstant floor field `f(z)`.  Put

\[
a=\min f(z)
\]

over the cycle.  Rotate at the first edge leaving the band `f=a`, and let the first later edge returning to that band be the **minimum-floor restoration edge**.

### Proof

The nonconstant cyclic floor word attains `a`, leaves it and later returns because the complete profile cycle closes.  First-exit and first-return conventions make the excursion canonical. QED.

## BDA5br -- restoration is a bounded downward wall crossing -- PROVED

Let `z` be the numerator immediately before the minimum-floor restoration edge and let `d` be that edge's increment.  Then

\[
d<0,
\qquad
-B\le d\le-1,
\]

and there is a unique overshoot `r` satisfying

\[
\boxed{
z=(a+1)q+r,
\qquad 0\le r\le B-1.}
\]

The restored numerator `z+d` lies in the band

\[
aq\le z+d\le(a+1)q-1.
\]

### Proof

Immediately before restoration the floor is greater than `a`, so `z>=(a+1)q`.  Immediately after restoration the floor is `a`, so `z+d<=(a+1)q-1`.  Hence `d<0`.  Since `d>=-B`,

\[
z\le(a+1)q-1+B,
\]

which gives `0<=r<=B-1`.  The lower bound on the restored numerator is the definition of floor `a`.  Uniqueness of `r` is immediate. QED.

Thus the wall shape is determined by the finite pair `(r,d)` once the floor level and decorated operation edge are fixed.

## BDA5bs -- finite wall-address stock -- PROVED UNDER THE FINITE-NUMERATOR-RANGE CONTRACT

Suppose the physical numerator coordinate ranges over a finite interval containing `H` possible floor levels, there are `m` declared floor fields and `L_edge` decorated operation-edge types.  Then the ambient stock of minimum-floor restoration addresses is at most

\[
\boxed{mH B^2 L_{\rm edge}.}
\]

### Proof

Choose the floor field, minimum level, overshoot `r` with at most `B` choices, negative increment `d` with at most `B` choices and decorated edge type.  The physical validity equations only reduce the ambient product. QED.

If translation by `q` is an exact symmetry of the complete physical profile, the level-free wall-shape stock is the sharper `mB^2L_edge`; otherwise the floor level must remain in the address.

## BDA5bt -- monotone floor fields cannot recur -- PROVED

If every legal transition in an epoch has `d>=0`, or every transition has `d<=0`, then no exact cycle can have a nonconstant floor field.

### Proof

A monotone integer numerator returning to its initial value is constant.  Its floor is therefore constant, contradicting the hypothesis.  Equivalently, BDA5br requires a negative restoration edge after an upward exit and the reversed argument requires a positive exit. QED.

## BDA5bu -- balanced-floor restoration router -- PROVED UNDER THE COMPLETE-WALL CONTRACT

Every recurrent balanced-floor profile whose numerator jumps are bounded has one of the following continuations:

1. the floor field is monotone, so nonconstant recurrence is impossible by BDA5bt;
2. the canonical wall edge carries current payment;
3. the wall edge gives strict denominator, valuation, rank or support descent;
4. the exact `(field,a,r,d,edge)` crossing is physically impossible;
5. the crossing consumes a capacity-one wall-restoration ticket from the finite stock of BDA5bs;
6. or the denominator, numerator range, role, occurrence, operation or legality interpretation changes, giving an explicit reset.

Consequently the balanced-floor part of BDA6 reduces to paying or excluding finitely addressed downward wall crossings rather than classifying arbitrary recurrent floor words.

### Proof

Use BDA5bq to select the canonical restoration and BDA5br to identify its bounded wall shape.  BDA5bs gives the finite stock under the declared range contract, while BDA5bt removes monotone cases.  Every omitted changing field is returned as a reset. QED.

## Finite check

`scripts/verify_bda_balanced_floor_wall.py` exhausts bounded integer cycles for small denominators and jump bounds, checking canonical minimum-floor restoration, negative crossing direction and the exact overshoot range.