# Upper-guard localization for recurrent exact macro words

**Branch:** `research/alternating-core-chain`

The AC4 ledger still lists upper-guard legality as an unresolved source of recurrence.  A finite upper
guard is not harmless if its resource coordinate is omitted from the exact state: a word may leave the
guarded region, wander through large values and later return.  However, once the recurrent macro word
has bounded length, every coordinate whose upper guard is actually used is anchored in a finite interval.

This note turns that observation into a finite-ticket or strict resource-dimension reduction.  It applies
to the bounded simple macro cycles already extracted by AC3kz--AC3lc and AC3tn--AC3tr.

## Guard-complete cycle model

Fix one exact recurrent macro word

`w=e_1 ... e_l`,  `1<=l<=P`,

which starts and ends at the same complete finite boundary state and resource vector

`m(0)=m(l) in Z_(>=0)^q`.

Edge `e_j` changes resources by one fixed vector `v_j in Z^q`.  Put

`B_i=max_j |v_(j,i)|`.

An upper-guard occurrence `(j,i,u)` means that immediately before `e_j` the complete legality test
includes

`m_i(j-1)<=u`.

Let `G(w)` be the set of resource coordinates with at least one upper-guard occurrence in `w`, and for
`i in G(w)` let

`u_i(w)=min{u:(j,i,u) is an upper-guard occurrence in w}`.

Assume the **upper-guard-complete macro contract**:

1. `w`, every increment vector, every upper-guard threshold and every guard occurrence are present in
   the exact cycle address;
2. all lower guards, gross consumptions, ownership, payment, occurrence and context fields are present
   in the complete boundary state;
3. resource updates are additive and coordinatewise integral;
4. the word length is at most the declared bound `P`;
5. a changed word, threshold, increment, guard interpretation, boundary field or resource law is an
   outer reset.

## AC3vg -- one used upper guard bounds its whole cycle coordinate -- PROVED

For every `i in G(w)` and every cycle position `0<=r<=l`,

`0<=m_i(r)<=u_i(w)+P B_i`.

### Proof

Choose an occurrence `(j_i,i,u_i(w))` attaining the least threshold.  At its pre-edge state,
`m_i(j_i-1)<=u_i(w)`.  Every other cycle position is reached from that state by at most `l<=P` cyclic
edge steps.  Each step increases coordinate `i` by at most `B_i`, so

`m_i(r)<=u_i(w)+P B_i`.

Nonnegativity is part of the resource state. QED.

The estimate is cyclic: it also bounds positions lying before the chosen guard in the displayed linear
word by traversing through the exact return.

## AC3vh -- finite guarded-coordinate decoration stock -- PROVED

Choose the canonical rotation of `w` by the existing total order on exact edge occurrences.  The vector
of guarded resource values at that root has at most

`K_guard(w)=prod_(i in G(w)) (u_i(w)+P B_i+1)`

possible values.

For a finite cycle-word dictionary `W`, the total guarded decoration stock is at most

`K_guard=sum_(w in W) K_guard(w)`.

### Proof

AC3vg places each guarded root coordinate in the integer interval
`[0,u_i(w)+P B_i]`.  Multiply the interval sizes, then sum over the finite word dictionary. QED.

This counts exact values, not only threshold bits, so every future upper-guard decision on a guarded
coordinate is reconstructed.

## AC3vi -- fully upper-guarded cycles have capacity-one tickets -- PROVED UNDER THE TICKET CONTRACT

If `G(w)={1,...,q}`, then the canonical root resource vector of `w` belongs to the finite stock counted
by `K_guard(w)`.  Consequently every recurrent fully guarded decorated word has one continuation:

1. exact erasure or bounded descent;
2. current/source payment;
3. one capacity-one ticket indexed by its exact word and guarded root vector;
4. or an outer reset named by the complete macro contract.

Across the finite word dictionary, at most `K_guard` distinct capacity-one tickets are required.

### Proof

All unbounded resource coordinates are bounded by AC3vg, while every nonresource field is already in the
finite boundary address.  Thus the exact recurrent state and word have a finite address.  Assign one
ticket to each address not already erased, descending or paid.  Capacity one forbids a second unpaid use
of the same exact address in the epoch. QED.

No claim is made that the ticket is free or recreatable; recreation must enter AC3vb--AC3vf or reset.

## AC3vj -- partial upper guarding strictly lowers unbounded dimension -- PROVED

If `G(w)` is a nonempty proper subset of `{1,...,q}`, retain the exact guarded-coordinate decoration and
project the resource walk to the complementary coordinates

`H(w)={1,...,q}\G(w)`.

The projected word is an exact recurrent additive macro word in dimension

`|H(w)|=q-|G(w)|<q`.

Every legality test involving a guarded coordinate is now a finite boundary predicate.  The only
remaining unbounded resource recurrence lies in the projected coordinates.

### Proof

AC3vg and AC3vh place all guarded coordinates in a finite exact decoration.  Deleting those coordinates
from every increment vector preserves additivity and the zero total increment of the recurrent word.
The start and end projected vectors agree because the original vectors agree.  Since `G(w)` is nonempty,
the projected unbounded dimension is strictly smaller.  Complete-boundary legality ensures that no
omitted cross-coordinate predicate survives the projection. QED.

## AC3vk -- upper-guard recurrent-cycle router -- PROVED UNDER THE DECLARED CONTRACTS

Every bounded simple recurrent macro word containing at least one finite upper-guard occurrence has one
continuation:

1. if every unbounded resource coordinate is guarded, it enters the finite erasure, payment, descent or
   `K_guard` capacity-one ticket stock of AC3vi;
2. if only some coordinates are guarded, it enters a strictly lower-dimensional additive recurrence
   with the guarded values retained as finite boundary data;
3. a repeated ticket enters the finite recreation-cycle router AC3vb--AC3vf;
4. any changed threshold, increment, word, legality, occurrence, ownership, payment or context field is
   an explicit outer reset.

Thus finite upper guards are no longer an independent AC4 obstruction for bounded exact macro cycles.
The remaining guard problem is genuinely unbounded thresholds, hidden/nonadditive cross-coordinate
legality, dynamic word dictionaries or upper-guard-sensitive fields omitted from the complete state.

### Proof

Apply AC3vg--AC3vj.  Full guarding gives a finite exact state stock; partial guarding reduces the number
of unbounded additive coordinates.  Ticket recreation and contract failure use the stated existing
routers. QED.

## Finite check

`scripts/verify_ac_upper_guard_cycles.py` generates and exhausts small closed integral resource walks,
places upper guards at exact cycle positions and checks the global `u_i+PB_i` bound, finite decoration
stock and strict dimension reduction for every partially guarded example.
