# Fixed-secant orientation and order-two recurrence

**Branch:** `research/rational-inverse-expansion`

RI5ad reduces every two-target terminal interaction to the secant through

\[
(x,a/x),\qquad(y,a/y),\qquad x\ne y,
\]

and RI5bd--RI5bg place that secant inside a complete polynomial terminal address.  This note removes the remaining lift ambiguity over one fixed secant.  The unordered target pair is uniquely reconstructed, while the ordered lift has only the transposition involution.

## Normalized secant address

The exact secant equation is

\[
xyR+aX=a(x+y).
\]

Assume `a` is nonzero and define

\[
s=x+y,
\qquad
p=xy.
\]

Equivalently, after division by `a`, the line is

\[
X+(p/a)R=s.
\]

## RI5bh -- sum/product is the complete normalized secant address -- PROVED

The physical secant determines the pair `(s,p)`, and conversely `(a,s,p)` determines its line.  The target parameters on that line are exactly the roots of

\[
T^2-sT+p=0.
\]

### Proof

The displayed line has constant term `s` and `R`-coefficient `p/a`, so `a` and the line determine `s,p`.  Conversely those values determine the line.  Substituting a target point `(X,R)=(t,a/t)` gives

\[
p(a/t)+at=as,
\]

which is equivalent to `t^2-st+p=0`. QED.

## RI5bi -- the unordered two-target lift is unique -- PROVED

For a nondegenerate two-target secant, the normalized address `(a,s,p)` determines the unordered pair

\[
\boxed{\{x,y\}}
\]

uniquely.

### Proof

The monic quadratic `T^2-sT+p` has its multiset of roots uniquely determined by its coefficients.  The interaction is nondegenerate, so `x!=y` and the root multiset is the unordered two-element set `{x,y}`. QED.

No quotient, scale or carry decoration can create a second physical target pair on the same exact secant without changing the complete terminal address.

## RI5bj -- the ordered lift is one transposition fibre -- PROVED

If the terminal word distinguishes two ordered target roles, the complete ordered lift over one fixed secant has exactly the two states

\[
(x,y),
\qquad
(y,x).
\]

The nontrivial lift symmetry is the involution

\[
\tau(x,y)=(y,x),
\qquad
\tau^2=1.
\]

### Proof

RI5bi fixes the unordered pair.  Since its elements are distinct, there are exactly two bijections from that pair to two ordered roles, exchanged by the transposition. QED.

## RI5bk -- fixed-secant recurrence has period at most two -- PROVED

Consider a terminal history in which the complete normalized secant address and every non-orientation field remain fixed.

- If the physical role order is part of the complete occurrence address, the ordered lift is constant.
- If only the unordered secant is retained, every nonconstant recurrence alternates between the two states of RI5bj and has exact period two.

Thus no longer orientation cycle exists over a fixed exact secant.

### Proof

The fibre has one state when role order is fixed and two states otherwise.  The only nonidentity permutation of the two-state fibre is `tau`, whose order is two. QED.

A capacity-one orientation ticket therefore needs only the exact secant address and the transposition bit.

## RI5bl -- two-target terminal router -- PROVED UNDER THE COMPLETE-SECANT CONTRACT

Every recurrent two-target terminal interaction has one continuation:

1. the normalized secant changes, exposing the canonical least coefficient/physical-field restoration gate of RI5bg;
2. the secant is fixed and the ordered physical roles are fixed, so the lift is constant;
3. the secant is fixed but role order is forgotten, giving the exact order-two transposition of RI5bk;
4. the fixed pair is paid or absorbed by its selected owner, fixed-edge bank or blocker repair;
5. the orientation transposition consumes one capacity-one exact secant ticket;
6. or the field, target hyperbola, physical occurrence, role order, scale, owner or legality interpretation changes, giving an explicit reset.

Consequently the two-target branch of RI6 has no hidden long secant-lift recurrence.  Remaining work is payment or arithmetic classification of the fixed exact secant and its owner/coherence data.

### Proof

Use RI5bh--RI5bi to reconstruct the unordered pair and RI5bj--RI5bk to classify its ordered lift.  Changed complete fields route through RI5bg or an outer reset; fixed fields leave only the declared payment, bank and ticket alternatives. QED.

## Finite check

`scripts/verify_ri_fixed_secant_orientation.py` enumerates nondegenerate target pairs over small prime fields, groups them by normalized secant address, verifies the secant equation and checks that every fibre consists exactly of one unordered pair and its two ordered lifts.