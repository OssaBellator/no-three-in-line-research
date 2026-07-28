# Occurrence-lineage gates on recurrent non-scalar BDA cycles

**Branch:** `research/bounded-denominator-absorbers`

BDA5az--BDA5bf reduce every long fixed-denominator history to one explicit
simple profile cycle and give decorated-edge and cycle-space ticket stocks.  The
remaining local question is whether a physically realized cycle can recreate
the support it destroyed without payment.  This note gives the canonical gate
for that question.

## Fixed-level physical cycle contract

Fix one effective denominator, one complete non-scalar profile alphabet and one
simple directed cycle

\[
P_0\xrightarrow{e_0}P_1\xrightarrow{}\cdots
\xrightarrow{e_{\ell-1}}P_\ell=P_0.
\]

Every profile retains its exact finite role word and a set `S(P)` of physical
occurrence atoms.  Assume:

1. every nonstutter edge changes `S(P)` or a declared arithmetic label;
2. every created occurrence has an exact lineage;
3. a lineage is current-factor payment, strict denominator/arithmetic descent,
   restoration of one previously destroyed occurrence, or a named reset;
4. exact restoration uses a capacity-one ticket carrying the complete
   denominator, profile, occurrence and edge address;
5. raw reflected `CD` roles remain on the nonradial route.

## BDA5bg -- canonical support excursion on a simple profile cycle -- PROVED

If the cycle changes physical support, choose the least occurrence atom `a`
destroyed on the cycle, rotate to its first destruction edge, and let `e_j` be
its first later restoration edge.  The resulting destruction--restoration
interval is canonical, and `a` is absent at every internal profile boundary.

### Proof

Exact return restores every destroyed support atom.  The fixed order on physical
addresses chooses `a`, the first destruction fixes the rotation, and finiteness
of the cycle gives a first restoration.  No earlier internal state contains `a`
by definition. QED.

## BDA5bh -- arithmetic-only cycles expose a least changed label -- PROVED

If every edge preserves physical support but the cycle is nonconstant, there is
a least arithmetic field that changes: denominator realization, primitive
direction, board anchor, role, scalar/carry label, or external decoration.
Rotating to its first change gives either strict arithmetic descent, a first
return gate for that label, or an outer reset.

### Proof

The complete profile address from BDA5av--BDA5ay is a finite ordered tuple.
A nonconstant support-preserving cycle changes at least one tuple coordinate.
Choose the least coordinate and its first change.  If its ordered value
decreases, use descent.  If it returns, the first return edge is a canonical
gate.  A changed interpretation or omitted coordinate is a reset. QED.

## BDA5bi -- physical restoration trichotomy -- PROVED UNDER THE LINEAGE
CONTRACT

For the support excursion of BDA5bg, the first restoration edge has exactly one
route:

1. current-factor payment from a faithfully destroyed factor;
2. strict denominator or lower arithmetic-profile descent;
3. restoration of `a` with one capacity-one decorated restoration ticket;
4. changed occurrence, role, owner or context, hence reset.

### Proof

These are the exhaustive creation lineages declared by the contract.  They are
disjoint because the complete physical occurrence and arithmetic address is
retained. QED.

## BDA5bj -- explicit recurrent-cycle ticket stock -- PROVED

Let `A_q` be the physical occurrence stock on the fixed denominator level and
let `E_q` be the decorated operation-edge stock.  The restoration-ticket stock
is at most

\[
\boxed{|A_q|\,|E_q|}.
\]

Using the ambient address bounds from BDA5av--BDA5ay gives a polynomial stock.
If the complete non-scalar profile stock is `K_q` and every operation has at
most `L_op` decorations, the safe bound is

\[
\boxed{|A_q|L_{\rm op}K_q^2}.
\]

### Proof

A restoration ticket is determined by the destroyed occurrence and the
decorated restoration edge.  The second display substitutes the ambient
directed-edge bound. QED.

## BDA5bk -- cycle-local payment/descent/ticket router -- PROVED UNDER THE
DECLARED CONTRACTS

Every simple same-denominator non-scalar cycle from BDA5bb now has one of the
following continuations:

1. current physical payment;
2. strict denominator or arithmetic-profile descent;
3. one capacity-one physical restoration ticket;
4. one capacity-one arithmetic return gate;
5. or an explicit occurrence/role/context reset.

Thus a fixed-level physical BDA cycle cannot recur freely when its complete
support and arithmetic lineage are occurrence-faithful.  The remaining BDA6
frontier consists of roles lacking physical realization, balanced-floor or
higher-rank profiles not yet connected to this cycle contract, and sources that
are genuinely replenishable.

## Finite check

`scripts/verify_bda_cycle_lineage.py` exhausts closed support words on three
physical atoms, verifies the least-atom destruction/restoration gate and checks
the exact atom-by-restoration-edge address bound.
