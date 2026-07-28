# Exact blocker-profile recurrence and physical lineage gates

**Branch:** `research/rational-inverse-expansion`

RI5au--RI5ax reduce every rank-at-most-three blocker prescription to one of nine
path/cycle types.  RI5af--RI5aj reconstruct the prime-field quotient, scale and
physical occurrence labels.  This note combines those results to remove free
recurrence of one exact labelled blocker profile.

It does not classify the remaining affine or hyperbola arithmetic.  It proves
that recurrence of a fully labelled profile must expose a physical occurrence
gate, a finite arithmetic-label gate, payment, descent or a ticket.

## Complete blocker address

Let `N=p-1` and let

\[
K_{\rm occ}\le L_{\rm RI}N^6
\]

be the physical RI occurrence stock from RI5ai.  A complete blocker profile
retains:

1. one of the nine types from RI5au;
2. rank `s<=3`, overlap `q` and occupancy `t`;
3. at most three exact physical RI occurrence addresses;
4. quotient, root, image, scale, carry, direction/offset and secant labels;
5. every owner, coherence and blocker-repair field used by the transition.

Let `L_B` bound the remaining finite role word.

## RI5ay -- polynomial complete blocker-profile stock -- PROVED UNDER THE
PRIME-FIELD PHYSICAL CONTRACT

The number of complete rank-at-most-three blocker profiles is at most

\[
\boxed{
K_B\le 9L_B(1+K_{\rm occ})^3
\le 72L_B\max(1,L_{\rm RI}^3N^{18}).
}
\]

### Proof

Choose one of nine types and one finite role word.  Encode a profile by three
slots, each empty or occupied by one exact occurrence address.  This safely
contains ranks zero through three and gives `9L_B(1+K_occ)^3`.  Use
`(1+x)^3<=8max(1,x^3)`. QED.

The bound is deliberately ambient.  Injectivity, overlap and arithmetic
compatibility only reduce the stock.

## RI5az -- canonical least-changing profile field -- PROVED

Let

\[
P_0\to P_1\to\cdots\to P_\ell=P_0
\]

be a nonconstant exact recurrence of complete blocker profiles.  Exactly one of
the following canonical gates exists:

1. the least physical occurrence destroyed on the cycle and its first later
   restoration;
2. if physical support is fixed, the least finite address field that changes
   and its first return.

### Proof

If support changes, exact return restores every destroyed occurrence.  Choose
the least occurrence, rotate to its first destruction and then its first
restoration.  If support does not change, the ordered finite profile tuple is
nonconstant, so it has a least changing coordinate.  Rotating to its first
change gives a first return because the word is closed. QED.

## RI5ba -- occurrence-restoration router -- PROVED UNDER THE OWNER-LINEAGE
CONTRACT

Assume every created RI occurrence has a complete owner/coherence lineage.
For the occurrence gate in RI5az, the first restoration is one of:

1. current physical payment from a faithfully destroyed factor;
2. strict scale, denominator, margin or rank descent;
3. exact restoration of the same occurrence with one capacity-one ticket;
4. changed owner, coherence, blocker host, quotient interpretation or context,
   hence reset.

### Proof

The complete lineage contract makes these alternatives exhaustive and
disjoint.  Exact physical equality is required for route 3; equality of a
symbolic alias is insufficient. QED.

## RI5bb -- finite recurrence-ticket stock -- PROVED

Let `L_op` be the decorated operation stock per ordered profile pair.  The
complete directed-edge stock is at most

\[
\boxed{L_{\rm op}K_B^2}.
\]

A capacity-one occurrence-restoration ticket has stock at most

\[
\boxed{3L_{\rm op}K_B^2},
\]

and a least-field return ticket has stock at most

\[
\boxed{d_BL_{\rm op}K_B^2},
\]

where `d_B` is the number of retained finite address coordinates.

### Proof

Choose the ordered profile pair and operation decoration.  A blocker profile
uses at most three occurrence slots.  A finite-label ticket additionally chooses
one tuple coordinate. QED.

## RI5bc -- exact blocker-profile recurrence router -- PROVED UNDER THE
DECLARED CONTRACTS

Every recurrent singleton, small-derangement or large exact blocker profile has
one continuation:

1. current physical payment;
2. scale/denominator/margin/rank descent;
3. a capacity-one physical occurrence ticket;
4. a capacity-one finite-label return ticket;
5. or an explicit owner/coherence/host/context reset.

Therefore physical owner/coherence recurrence is no longer an unlabelled
infinite branch once the RI5af--RI5ax complete address is present.  RI6 remains
open because one selected exact profile still requires arithmetic payment or
absorption, and because genuinely recreated ticket sources or omitted legality
fields are outside this contract.

## Finite check

`scripts/verify_ri_profile_recurrence.py` exhausts closed words of support and
finite labels, checks the canonical occurrence or least-field gate and records
the finite gate-address stocks.
