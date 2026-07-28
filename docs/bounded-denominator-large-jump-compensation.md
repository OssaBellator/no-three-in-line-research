# Large-jump compensation for balanced-floor restoration cycles

**Branch:** `research/bounded-denominator-absorbers`

BDA5bq--BDA5bu give a finite wall address when the numerator jump size is bounded. This note handles the complementary unbounded-jump case. A large negative jump returning to the minimum balanced-floor band cannot occur alone in a closed numerator cycle: exact closure forces a positive source edge of comparable size.

The conclusion is cycle-local. It does not assert that the compensating positive edge is automatically payable; it exposes the exact physical source edge which must be paid, descended, ruled out or ticketed.

## Closed numerator cycle

Fix one denominator `m>=1` and one exact same-denominator physical profile cycle with numerator values

\[
 h_0,h_1,\ldots,h_P=h_0.
\]

Write

\[
 \Delta_t=h_{t+1}-h_t,
 \qquad 0\le t<P.
\]

Then

\[
 \sum_{t=0}^{P-1}\Delta_t=0.
\]

Let `e_-` be the canonical downward wall-restoration edge supplied by BDA5br, and put

\[
 J=-\Delta(e_-)>0.
\]

The edge retains its full denominator, role, owner, operation, support and occurrence-lineage address.

## BDA5bv -- exact positive compensation identity -- PROVED

The positive and negative jump masses satisfy

\[
 \boxed{
 \sum_{\Delta_t>0}\Delta_t
 =
 \sum_{\Delta_t<0}(-\Delta_t).
 }
\]

In particular the total positive jump mass is at least `J`.

### Proof

Separate the zero-sum identity into its positive and negative parts. Since `e_-` contributes `J` to the negative mass, the common total is at least `J`. QED.

## BDA5bw -- one comparable positive source edge -- PROVED

Among the other at most `P-1` edges, one positive edge `e_+` satisfies

\[
 \boxed{
 \Delta(e_+)
 \ge
 \left\lceil\frac{J}{P-1}\right\rceil.
 }
\]

Choose the least such edge in the canonical cyclic order. The pair

\[
 (e_-,e_+)
\]

is the **large-jump compensation pair**.

### Proof

The positive increments sum to at least `J` by BDA5bv and occur on at most `P-1` edges distinct from the negative restoration edge. Their maximum is therefore at least their average, giving the displayed ceiling bound. The fixed edge order makes the selected source canonical. QED.

## Dyadic localization

For a positive integer `x`, write

\[
 \lambda(x)=\lfloor\log_2 x\rfloor.
\]

## BDA5bx -- bounded dyadic scale gap -- PROVED

The canonical compensation pair obeys

\[
 \boxed{
 \lambda(J)-\lambda(\Delta(e_+))
 \le
 \lceil\log_2(P-1)\rceil.
 }
\]

Thus a restoration jump in dyadic class `s` forces a positive source edge in one of only

\[
 \lceil\log_2(P-1)\rceil+1
\]

nearby lower dyadic classes.

### Proof

BDA5bw gives `J<= (P-1) Delta(e_+)`. Taking base-two logarithms and using integer floors yields the claim. QED.

## BDA5by -- bounded-length large-jump router -- PROVED UNDER THE COMPLETE-EDGE CONTRACT

For a fixed maximum cycle length `P`, every unbounded-jump balanced-floor recurrence has one continuation:

1. the negative restoration jump is within the bounded alphabet and uses BDA5bq--BDA5bu;
2. its canonical positive compensation edge carries current payment or a finite physical source debit;
3. the compensation pair gives strict denominator, valuation, support or arithmetic descent;
4. one edge of the pair is physically impossible under its exact address;
5. the pair consumes a capacity-one source/restoration ticket;
6. or an owner, role, operation, support, lineage, legality or context field changes, giving an outer reset.

If none of the first six routes applies, the unresolved output is one exact large-jump compensation pair with size ratio at most `P-1`; it is not a diffuse cycle word.

### Proof

Use BDA5br for the canonical downward restoration edge and BDA5bw for the canonical positive compensation edge. The declared routes are exact edge-local continuations. QED.

## BDA5bz -- updated BDA6 frontier -- PROVED AS A REDUCTION

Balanced-floor recurrence is now localized both when jump sizes are bounded and when they are unbounded:

- bounded jumps give a finite wall address;
- unbounded jumps give a negative restoration edge paired with a comparable positive physical source edge.

The remaining work is payment, descent, impossibility or finite ticketing of these exact wall/source pairs for rank-two/rank-three and unresolved ordinary-role profiles. A proof may no longer treat a large floor jump as an anonymous arithmetic event.

## Finite check

`scripts/verify_bda_large_jump_compensation.py` enumerates closed integer walks of bounded length, selects the canonical downward return to the minimum floor band, and verifies the exact positive-mass identity, comparable-source bound and dyadic scale-gap inequality.