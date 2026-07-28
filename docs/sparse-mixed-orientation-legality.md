# Mixed-orientation operation-square legality

**Branch:** `research/sparse-algebraic-spread`

SAS5gb--SAS5hc pay aggregate negative collateral and changed-signature cycles
under creator-stage and opposite-destroyer legality contracts.  This note gives
a sufficient local criterion for those contracts.  Two disjoint swaps form a
commuting operation square; legality of every orientation follows from two
base-state checks when each guard is reversal-closed and invariant under the
other disjoint swap.

## Operation square and guards

Let `sigma` and `tau` be involutive swaps on disjoint column pairs.  For a base
state `x`, the operation square is

\[
x,\quad \sigma x,\quad \tau x,\quad \sigma\tau x.
\]

Let `L_sigma(y)` and `L_tau(y)` be the complete single-swap legality predicates,
including required cells, forbidden collisions, boundary conditions, active
word roles and payment-sensitive state.

Assume the **transported local-guard contract**:

1. `sigma tau=tau sigma`;
2. reversal closure:
   `L_sigma(y)=L_sigma(sigma y)` and
   `L_tau(y)=L_tau(tau y)`;
3. disjoint transport:
   `L_sigma(y)=L_sigma(tau y)` and
   `L_tau(y)=L_tau(sigma y)`;
4. every failed equality returns the least changed physical guard atom.

## SAS5hd -- disjoint swaps form one exact commuting square -- PROVED

For every state `x`,

\[
\boxed{\sigma\tau x=\tau\sigma x}
\]

and each of the four square edges is paired with its reverse by the same
involution.

### Proof

The swaps act on disjoint column coordinates, so their coordinate
permutations commute.  Each swap is an involution, giving the reverse edge.
QED.

## SAS5he -- legality transports across the opposite side -- PROVED UNDER THE
LOCAL-GUARD CONTRACT

If `L_sigma(x)` holds, then the two `sigma`-edges

\[
x\leftrightarrow\sigma x,
\qquad
\tau x\leftrightarrow\sigma\tau x
\]

are legal.  The analogous statement holds for `tau`.

### Proof

Reversal closure certifies both orientations of the base edge.  Disjoint
transport moves the same legality value to the opposite side of the square,
and reversal closure certifies its reverse. QED.

## SAS5hf -- two base checks certify the full mixed-orientation square --
PROVED UNDER THE LOCAL-GUARD CONTRACT

If

\[
L_\sigma(x)=L_\tau(x)=1,
\]

then every creator, donor, composed and opposite-destroyer edge of the
operation square is legal, in both orientations.

### Proof

Apply SAS5he once to `sigma` and once to `tau`.  Their certified edge pairs are
exactly the four sides of the commuting square. QED.

Thus a localized arithmetic word family does not require four unrelated
legality proofs.  It requires two base-state checks plus the transport and
reversal identities.

## SAS5hg -- failed transport has an exact physical obstruction -- PROVED

If one transport or reversal identity fails, the least changed guard field is
one of:

1. a moved or required cell;
2. a collision or line constraint;
3. a boundary admissibility field;
4. a word-role or orientation label;
5. an owner/payment/context field.

Fixing that atom and the ordered operation square gives a finite exact
mixed-orientation obstruction address.

### Proof

The complete legality predicate is an ordered finite conjunction of the listed
physical fields.  Unequal truth values have a least conjunct on which they
differ.  Retaining the square and field address makes the obstruction exact.
QED.

## SAS5hh -- mixed-orientation legality router -- PROVED UNDER THE DECLARED
CONTRACTS

Every creator/opposite-destroyer operation square now has one continuation:

1. two base checks certify all four square edges by SAS5hf;
2. a failed check returns its ordinary single-swap blocker;
3. failed transport returns one exact mixed-orientation guard atom by SAS5hg;
4. changed guard interpretation or context is an outer reset.

This discharges mixed-orientation legality for every word family whose
single-swap guards are support-local, reversal-closed and invariant under the
disjoint companion swap.  SAS6 remains open for overlapping supports,
base-state single-swap failures, global aggregate barriers, high-incidence
neutral outputs, boundary profiles and exact standard-grid compression.

## Finite check

`scripts/verify_sas_mixed_orientation_legality.py` exhausts Boolean local guard
predicates on a two-swap cube.  It verifies commutation, reversal/transport
invariance and full-square legality from the two base-state checks.
