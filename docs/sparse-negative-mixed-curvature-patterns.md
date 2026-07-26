# Exact negative mixed-curvature patterns for two disjoint swaps

**Branch:** `research/sparse-algebraic-spread`

SAS5bn--SAS5br reduce the safe-donor divisor-scale branch to a positive scale
contribution and a possible negative mixed-curvature endpoint-pair fibre.  A generic
Boolean four-state function has five negative second-difference patterns and can even
have curvature `-2`.  A geometric constraint record is not a generic Boolean function:
it is a conjunction of exact required-label literals, and the two disjoint swaps act on
disjoint column sets.

This product structure eliminates curvature `-2` and leaves exactly two negative
patterns.  Every negative record is satisfied by exactly one single swap, but not by
the original colouring or by the composed move.  The cross fibre therefore has a
finite orientation and scope-type dictionary.

## Two-swap record factorization

Fix disjoint transpositions

`omega={x,y}`,

`tau={z,r}`.

Let `Q` be one rank-three constraint record with distinct scope columns and one required
label at each scope column.  For `epsilon,eta in {0,1}`, write

`I_(epsilon,eta)=I_Q(kappa^(omega^epsilon union tau^eta))`.

Partition the literals of `Q` into those whose columns lie in `{x,y}`, those whose
columns lie in `{z,r}`, and the remaining fixed literals.  Let

`A_epsilon in {0,1}`

be the conjunction of the first group after state `epsilon`, let `B_eta` be the
conjunction of the second group after state `eta`, and let `C` be the conjunction of
the fixed group.  Empty conjunctions are one.

## SAS5bs -- exact product factorization -- PROVED

For all `epsilon,eta in {0,1}`,

`I_(epsilon,eta)=A_epsilon*B_eta*C`.

Consequently

`partial_(omega,tau)I_Q
 = C*(A_1-A_0)*(B_1-B_0)`.

### Proof

The satisfaction indicator of `Q` is the product of its required-label indicators.
The disjoint swap `omega` changes only columns in its own endpoint set, and `tau`
changes only columns in its endpoint set.  Grouping the literal products gives the
first identity.  Expanding the four-state mixed difference gives the second. QED.

This factorization remains valid when the scope contains both endpoints of one swap and
one endpoint of the other.

## SAS5bt -- curvature `-2` is impossible -- PROVED

Every exact constraint record satisfies

`partial_(omega,tau)I_Q in {-1,0,1}`.

In particular, the generic Boolean pattern

`(I_00,I_10,I_01,I_11)=(0,1,1,0)`,

which has curvature `-2`, cannot occur for one conjunction record under two disjoint
swaps.

### Proof

Each difference `A_1-A_0` and `B_1-B_0` belongs to `{-1,0,1}`, while `C` belongs to
`{0,1}`.  Apply SAS5bs. QED.

## SAS5bu -- the two exact negative patterns -- PROVED

A record has negative mixed curvature if and only if its four indicators are exactly
one of

`(0,1,0,0)`

or

`(0,0,1,0)`.

Equivalently:

1. **omega-only orientation:** `Q` is satisfied after `omega` alone and in none of the
   other three states;
2. **tau-only orientation:** `Q` is satisfied after `tau` alone and in none of the
   other three states.

Every negative record has curvature exactly `-1`.

### Proof

By SAS5bs, negativity requires `C=1` and the two one-variable differences to have
opposite signs.

If `A_1-A_0=1` and `B_1-B_0=-1`, then

`(A_0,A_1)=(0,1)`, `(B_0,B_1)=(1,0)`,

so the product table is `(0,1,0,0)`.  Reversing the signs gives `(0,0,1,0)`.
Conversely each displayed table has mixed difference `-1`. QED.

Thus negative mixed collateral is not a record repaired by both single swaps and lost
under composition.  Exactly one single swap repairs it; the other swap destroys that
single-swap repair in the composed state.

## Scope type inside a fixed endpoint-pair fibre

Fix one endpoint pair

`(a,b) in {x,y} x {z,r}`

contained in the scope, as in the canonical assignment of SAS5bq.  Since the record has
rank three, its third scope column has exactly one of three types:

1. outside all four swap endpoints;
2. the mate of `a` in `omega`;
3. the mate of `b` in `tau`.

The third column cannot be both mates because the two swaps are disjoint.

## SAS5bv -- orientation and scope-type localization -- PROVED

Let one fixed endpoint-pair fibre carry total negative mixed-curvature weight `V`.
Then one of the two orientations from SAS5bu carries at least `V/2`, and within that
orientation one of the three third-column scope types carries at least

`V/6`.

Every record in the selected subfibre has the same:

- original endpoint `a`;
- donor endpoint `b`;
- single-swap-only orientation;
- and third-column endpoint-incidence type.

### Proof

Negative curvature equals `-1` on every record by SAS5bu, so negative-curvature weight
is ordinary record weight.  Partition first into two orientations and then into at most
three scope types.  Two applications of weighted pigeonhole give the bound. QED.

This is an incidence classification only; the third column itself and its affine
address may still vary.

## SAS5bw -- quantitative cross-fibre router -- PROVED

Use the endpoint-pair fibre supplied by SAS5bq.

1. If `C_minus>=eta*L_g`, for `0<eta<1`, one exact endpoint-pair/orientation/scope-type
   fibre carries negative mixed-curvature weight at least

   `eta*L_g/24`.
2. If the composed move improves, one such exact fibre carries weight strictly greater
   than

   `L_g/24`.

### Proof

SAS5bq supplies one endpoint-pair fibre of weight at least `C_minus/4`; apply SAS5bv to
retain one sixth.  This gives `C_minus/24`.  Substitute the two bounds from SAS5bp:
`C_minus>=eta L_g` in the first branch and `C_minus>L_g` for an improving composed
move. QED.

The selected fibre is now a one-sided cancellation witness: either `omega` alone
satisfies every record and `tau` destroys that satisfaction under composition, or the
roles are reversed.

## Corrected SAS6 frontier

The negative mixed-curvature branch is no longer an arbitrary four-state Boolean
interaction.  It has two orientations and three endpoint-incidence types, with explicit
retention `1/24` from the full negative collateral.  The remaining work is to classify
the varying third column arithmetically, exploit repeated required-label patterns, and
handle high-incidence or board-boundary profiles.  The coprime donor-saturated
progression remains the other exact-scale obstruction.

## Finite check

`scripts/verify_sparse_negative_mixed_curvature_patterns.py` exhausts small label
alphabets, rank-three scopes, required-label vectors and two disjoint swaps.  It checks
the product factorization, impossibility of curvature `-2`, the two negative patterns,
orientation/scope-type localization and the quantitative `1/24` router.