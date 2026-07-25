# Ordinary support closure and reflected-CD correction

**Branch:** `research/alternating-core-chain`

The original AC3aq and AC3dm interfaces left a broad support-faithfulness gate.
For ordinary records this gate is stronger than necessary: once each record is
an exact current radial occurrence, same-anchor scale pairing automatically
enters the proved AC3ec collision/clean-support audit, and complete AC3v
envelopes handle every incompatibility not seen by the row-column graph.

For raw reflected `CD` roles the opposite correction is required.  Their two
local cells are not collinear with the nominal anchor, so they are not radial
occurrences and must not be passed directly to BDA5a.  They remain legitimate
collateral profiles, but become executable only after one legal state realizes
the corresponding current triples and AC3gk--AC3gj orient them to pivot
buckets.

## Exact physical ordinary occurrences

Call an ordinary BDA record **occurrence-faithful** when its paid current
certificate is exactly

\[
T_h(P)=\{P,P+hu\,d,P+hv\,d\},
\]

with one current permutation layer containing all three cells, fixed nonzero
distinct scalars `u,v`, positive scale `h`, and all arithmetic fields attached
to this physical occurrence.

A same-profile, same-anchor pair at scales `h` and `H=h+q` is then a pair of
actual current triples, not merely a pair of arithmetic slots.

## AC3hq -- ordinary co-anchor support closes automatically -- PROVED

Let two occurrence-faithful ordinary records have the same anchor `P`, the same
`q,d,u,v` and scales

\[
H=h+q.
\]

Then exactly one of the following holds.

1. **Mixed collision:**
   \[
   hu=Hv
   \qquad\hbox{or}\qquad
   hv=Hu.
   \]
   The pair is one of the finite collision profiles AC3eh--AC3ek.
2. **Actual clean pair:** neither equality holds.  The union of the two current
   triples is the clean five-cell support of AC3ec and therefore admits the
   canonical union-safe BDA menu AC3gc.

No additional support-faithfulness hypothesis is needed.

### Proof

Occurrence faithfulness says all five formal cells are actual cells of one
current permutation layer.  AC3ec proves that the only possible cross-scale
cell equalities are the two displayed mixed collisions.  If neither holds,
the five cells are distinct; in a permutation layer distinct cells have
distinct rows and columns.  AC3ec and AC3gc give the clean union-safe menu.
QED.

## AC3hr -- complete-scope replacement for conflict faithfulness -- PROVED

Let an ordinary exact-profile family first pass through AC3ap and BDA4e.

- A high row or column is already closed by BDA5ap--BDA5ar and AC3hf--AC3hh.
- In the bounded-load branch, BDA4e returns a row-column-compatible pair family
  of paid weight `V`.

Assume only occurrence faithfulness, not that the BDA4e row-column graph
contains every alternating-core incompatibility.  Split off the finite mixed
collision profiles by AC3hq.  On the remaining actual clean pairs build the
complete AC3v envelope graph, including every local union-safe state,
auxiliary blocker cell, replacement cell, protected scope, paid set and
potential factor.

For every `K>=1`, one of the following holds.

1. one pair has closed-neighbourhood paid load greater than `K` times its
   weight, and AC3fr returns an explicit finite overload label;
2. an independent executable clean-pair family carries payment at least
   \[
   \boxed{V_{\rm clean}/K}.
   \]

Every product state is legal and payment/collateral are exactly additive.

### Proof

AC3hq supplies a nonempty union-safe menu for every noncollision pair.
Occurrence-faithful pair payments are exact current certificate resources.
The complete AC3v graph contains every actual incompatibility by definition,
so AC2c gives the weighted dichotomy.  AC3w gives exact additivity. QED.

Thus the old requirement that the BDA4e row-column conflict graph itself
dominate all AC incompatibilities is unnecessary.  Row-column regularization
is only the first extraction; AC3v is the scope-complete second extraction.

## Raw reflected `CD` geometry

Translate the nominal anchor `P` to the origin.  For one reflected role
coefficient `w`, denominator step `q>0`, positive scale `h`, and nonzero
primitive direction coordinates `a,b`, the two local `CD` cells are

\[
C_w=P+w(ha,(h+q)b),
\]

\[
D_w=P+w((h+q)a,hb).
\]

## AC3hs -- raw reflected `CD` support is nonradial -- PROVED

The anchor determinant is

\[
\boxed{
\det(C_w-P,D_w-P)
=
-w^2abq(2h+q).
}
\]

Under the BDA role hypotheses

\[
w,a,b,q\ne0,
\qquad h>0,
\qquad q>0,
\]

this determinant is nonzero.  Therefore

\[
\boxed{P,C_w,D_w\text{ are not collinear}.}
\]

In particular, the raw reflected `CD` occurrence is not a radial triple
`T_h(P)` and a scalar pair of such records is not, by itself, a BDA5a radial
pair.

### Proof

Expand

\[
\det\bigl(w(ha,(h+q)b),w((h+q)a,hb)\bigr)
\]

and factor:

\[
w^2ab\bigl(h^2-(h+q)^2\bigr)
=
-w^2abq(2h+q).
\]

Every factor is nonzero under the stated hypotheses. QED.

## AC3ht -- corrected reflected-profile execution route -- PROVED

A raw reflected `CD` profile remains a valid finite arithmetic and collateral
label through AC3dj--AC3dm, but its scale-pair output has the following exact
router.

1. If the role supplies an additional, separately proved occurrence-faithful
   radial triple at each scale, apply AC3hq--AC3hr to that radial support.
2. Otherwise do **not** invoke BDA5a on the raw cells `P,C_w,D_w`.  Retain the
   reflected scalar, effective denominator, reduced unit, anchor, scale,
   channel and context-line labels.  Once a legal product state realizes the
   corresponding current collateral triples, apply AC3gk:
   - one state carries at least the exact expected reflected-profile weight;
   - AC3gg orients those current triples to private pivot buckets without
     loss;
   - for every `K>=1`, AC3gi gives an explicit overload or pivot payment at
     least
     \[
     \boxed{T_{\rm ref}/K};
     \]
   - a failed pivot product returns a next created-cell rank at least
     \[
     \boxed{T_{\rm ref}/(3K)}.
     \]

This route preserves every reflected determinant and denominator decoration.

### Proof

The first case is AC3hq--AC3hr.  AC3hs excludes direct radial decoding in the
second case.  AC3dm supplies a finite weighted reflected profile, while AC3gk
requires only a finite legal state bank and a nonnegative expected physical
certificate weight.  After realization, AC3gg--AC3gj supply the pivot
partition, payment and failed-rank return. QED.

## Consequence

The broad ordinary/reflected support-faithfulness frontier is replaced by two
literal obligations.

- **Ordinary:** prove physical occurrence faithfulness of each arithmetic
  record.  Same-anchor pairing, clean support and complete conflict handling
  are then automatic through AC3hq--AC3hr.
- **Reflected `CD`:** either exhibit a separate actual radial occurrence or
  keep the role as nonradial determinant-address collateral and execute it
  only after state realization through AC3ht.

This prevents an arithmetic scalar pair from being silently promoted to a
radial decoder input.

## Finite check

`scripts/verify_ac_bda_support_correction.py` exhausts signed ordinary role
scalars, adjacent scales and collision equations; verifies the clean five-cell
criterion for occurrence-faithful pairs; exhausts reflected `CD` parameters
and the nonzero determinant identity; and checks every `1/K`, `1/(3K)`
composition constant in AC3hr and AC3ht.
