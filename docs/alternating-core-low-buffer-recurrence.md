# Low-buffer recurrence and capacity-one threshold tickets

**Branch:** `research/alternating-core-chain`

AC3um--AC3uq realize every primitive nondecreasing coupled-resource circulation once all resource
coordinates exceed the explicit Steinitz buffers

`beta_i=C_i+q max(B,1)`.

The remaining chronological obstruction is a recurrent exact macro cycle that repeatedly visits a
state with some `m_i<beta_i`. This note gives that obstruction a canonical finite address. A
low-buffer return either lies on a lower-dimensional resource face, crosses one exact threshold and
spends a capacity-one lineage ticket, or exposes a source-recreation gate.

No free payment is asserted. The ticket conclusion uses an explicit occurrence-faithful threshold
contract, and a changed macro dictionary, boundary state, consumption row, lineage rule or omitted
legality field remains an outer reset.

## Exact low-buffer cycle model

Retain the common-boundary resource-only macro model of AC3um--AC3uq. A **closed macro word** is a
chronological sequence

`w=lambda_1 ... lambda_L`

whose macro-endpoint states are

`(x,m^0),(x,m^1),...,(x,m^L)`,

with the same complete finite boundary state `x`, the same fixed macro dictionary, and

`m^L=m^0`.

Thus

`m^t=m^(t-1)+v_(lambda_t)`

and every endpoint resource vector is nonnegative. The word is **low-buffer** when some endpoint has
`m_i^t<beta_i`.

Fix the total order on coordinates, integer levels, macro addresses and cyclic positions. For a
low-buffer word choose the lexicographically least pair

`(i,h)`

for which

`h=min_t m_i^t<beta_i`,

and rotate the cyclic word to the least position with `m_i^0=h`. This is the **canonical low-buffer
rotation**.

Assume the **threshold-lineage contract** for coordinate `i` and level `h`:

1. every macro endpoint increment and every internal legality field is recorded in the augmented state;
2. every first crossing from level `h` to a level greater than `h` designates the least physical unit whose creation makes the coordinate exceed `h`;
3. that unit carries a source and lineage address from a finite stock `U_(i,h)`;
4. until the coordinate next returns to `h`, the designated unit either survives, is first-destroyed, or is replaced only through a recorded recreation edge;
5. one nonrecreated lineage address can be designated by at most one completed `h`-excursion in the epoch;
6. a changed source interpretation, hidden balance, upper guard, dictionary, context or lineage rule is a named reset.

The fifth item is exactly the capacity-one ticket hypothesis. It is not inferred from additive
arithmetic alone.

## AC3uw -- canonical minimum-face rotation -- PROVED

Every exact low-buffer closed macro word has a unique canonical low-buffer rotation and exactly one of
these two forms for its selected coordinate `i` and level `h`:

1. `m_i^t=h` for every macro endpoint `t`; or
2. the word contains an edge leaving level `h` upward and a later edge returning to level `h`.

### Proof

The finite set of endpoint coordinate-level pairs has a least low-buffer minimum `(i,h)`. The fixed
total order on cyclic positions selects a unique occurrence of that minimum and hence a unique
rotation. Since `h` is the minimum endpoint level in coordinate `i`, an edge leaving `h` cannot end
below `h`. If the coordinate is not constant, the first changing edge therefore ends above `h`.
Because the word closes at level `h`, a later edge returns to `h`. QED.

## AC3ux -- constant minimum face gives resource-dimension descent -- PROVED

In the first branch of AC3uw every macro occurrence in the word has

`v_(lambda_t,i)=0`.

Consequently the exact level `m_i=h` may be moved from the unbounded resource vector into the finite
boundary state. The projected word is an exact recurrent macro cycle on at most `q-1` unbounded
resource coordinates, with the same chronological order and the same payment fields.

### Proof

At consecutive macro endpoints the selected coordinate is always `h`, so

`v_(lambda_t,i)=m_i^t-m_i^(t-1)=0`

for every occurrence. The exact level satisfies `0<=h<beta_i`, so it has only `beta_i` possible
values. Recording `h` together with the fixed internal consumption/prefix row in the finite boundary
state preserves every declared legality test. Deleting coordinate `i` from the unbounded vector then
preserves the complete word and its return. QED.

This is a strict dimension descent, not an erasure of the finite level field.

## AC3uy -- canonical threshold excursion -- PROVED

In the second branch of AC3uw there is a unique canonical interval

`[a,b]`

of cyclic macro positions such that

- `m_i^(a-1)=h` and `m_i^a>h`;
- `m_i^t>h` for `a<=t<b`;
- `m_i^b=h`.

It is the first upward departure from the canonical minimum followed by the first return. The
interval is a positive-length exact `h`-excursion and has the finite address

`(i,h,lambda_a,lambda_b,x)`.

### Proof

Take the first changing edge after the canonical rotation. AC3uw makes it an upward departure. The
closed word eventually returns to `h`; choose the first such endpoint. Minimality of that return gives
strict inequality at all intervening endpoints. Every field in the displayed address belongs to a
finite dictionary or to one of the `K_buf=sum_i beta_i` low-buffer coordinate-level slots. QED.

## AC3uz -- capacity-one threshold ticket or recreation gate -- PROVED UNDER THE THRESHOLD-LINEAGE CONTRACT

For the canonical `h`-excursion of AC3uy, let `u` be the designated least crossing unit.
Exactly one of the following occurs:

1. `u` survives until the return edge and the excursion spends the capacity-one ticket `(i,h,u)`;
2. `u` is first-destroyed during the excursion, giving current destruction payment or a lower source debit;
3. the stock above `h` is restored through a recorded recreation edge for `u` or its source, giving a canonical recreation-gate address;
4. one threshold-lineage field changes, giving a named reset.

For fixed `(i,h)`, at most `U_(i,h)` completed excursions can take the first branch in one epoch.

### Proof

The threshold-lineage contract designates one physical unit at the first upward crossing and records
its complete lineage until the first return. The survival, first-destruction, recreation and reset
cases are exhaustive by item 4 of the contract. In the survival case item 5 makes the lineage address
capacity one. There are only `U_(i,h)` such addresses. QED.

## AC3va -- low-buffer exact-cycle router -- PROVED UNDER THE DECLARED CONTRACTS

Let

`K_low=sum_i beta_i`,

`T_low=sum_i sum_(h=0)^(beta_i-1) U_(i,h)`.

Every recurrent exact low-buffer macro cycle has one canonical continuation:

1. strict descent from `q` to at most `q-1` unbounded resource coordinates;
2. a current first-destruction or lower-source payment edge;
3. one of at most `T_low` capacity-one threshold tickets per epoch;
4. a finite source-recreation gate with address `(i,h,u,source,edge)`;
5. one of at most `K_low` low-buffer coordinate-level fields together with a changed boundary, dictionary, consumption, guard, context, lineage or hidden-balance reset.

Thus a recurrent exact macro word cannot remain an unclassified low-buffer cycle under the
threshold-lineage contract. The only recurrent branch not already paid or ticketed is an explicit
recreation gate, which enters AC3nx--AC3qt and AC3tx--AC3ub.

### Proof

Apply AC3uw. The constant-face branch is AC3ux. Otherwise AC3uy selects one canonical excursion and
AC3uz classifies it. Summing the coordinate-level and lineage stocks gives the displayed bounds. QED.

## Corrected AC4 frontier

Low-buffer recurrence is now reduced to finite coordinate-level faces, strict resource-dimension
descent, capacity-one crossing lineages, first-destruction payment or explicit recreation gates.
What remains outside this result is precisely where the threshold-lineage contract fails: freely
recreatable units, cyclic source recreation without a paid debit, upper guards, hidden balances,
nonadditive resources, dynamic dictionaries or payment-sensitive fields omitted from the augmented
state.

## Finite check

`scripts/verify_ac_low_buffer_recurrence.py` exhausts small closed integer walks, constructs the
canonical low-buffer rotation, verifies the face/excursion dichotomy, checks the first-departure and
first-return interval, and audits capacity-one versus recreated lineage accounting.
