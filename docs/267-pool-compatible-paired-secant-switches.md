# Pool-compatible paired secant switches

The direct secant switch PP3ayx preserves the total row and column degree vector, but a
restart repair must preserve every permanent controller block separately.  If the
tentative pivot cell and the witness-host pivot cell lie in different permanent pools,
the direct cross diagonal pairs `X_i` with `Y_j` and is not pool-compatible.

The correction pairs two secant records.  Cross the two tentative pivots inside their
own permanent block, and independently cross the two witness pivots inside their own
block.  The product has four local states.  Its all-cross state omits every designated
pivot, clears both secant certificates, preserves both permanent matching rectangles,
and moves all credited source endpoints.

## 1. Two internal rectangle switches

Let two secant records be

```text
(a_r,b_r,z_r),  r=1,2,
```

where

```text
a_r=(x_r,y_r)
```

are distinct cells of one tentative endpoint matching in permanent block `E_i`, and

```text
z_r=(u_r,v_r)
```

are distinct cells of one witness-clearing endpoint matching in permanent block `E_j`.
The blocks may be equal or different, but all eight typed endpoint resources are
distinct when the blocks coincide.  Assume

```text
a_r,b_r,z_r are collinear.
```

Define the tentative-block states

```text
A^0={a_1,a_2},
A^1={(x_1,y_2),(x_2,y_1)},
```

and witness-block states

```text
Z^0={z_1,z_2},
Z^1={(u_1,v_2),(u_2,v_1)}.
```

For `(epsilon,eta) in {0,1}^2`, put

```text
T^(epsilon,eta)=A^epsilon union Z^eta.
```

### Proposition PP3azk -- PROVED

Every state `T^(epsilon,eta)` preserves the row and column degree vector separately
inside `E_i` and `E_j`.  In particular, it preserves every permanent coordinate pair
`X_h,Y_h` and the movement/refill candidate-cell universe.

The state `T^(1,1)` contains none of

```text
a_1,a_2,z_1,z_2,
```

and therefore contains neither designated triple

```text
{a_r,b_r,z_r},  r=1,2.
```

#### Proof

`A^0,A^1` are the two perfect matchings of the two-by-two rectangle on columns
`x_1,x_2` and rows `y_1,y_2`.  Thus the tentative block is preserved internally.
The same statement holds for `Z^0,Z^1` inside the witness block.  Taking their union
preserves both blocks independently.  The two cross states omit their diagonal cells,
so the all-cross product omits all four designated pivots. ∎

This product switch, not the cross-pool diagonal of PP3ayx, is the restart-compatible
state when `i!=j`.

## 2. Avoiding accidental fixed source edges

The tentative and witness cells arise as arcs of endpoint permutations.  Crossing two
arcs can recreate a current diagonal edge only when one arc endpoint immediately
precedes or succeeds the other in the corresponding permutation cycle.

### Proposition PP3azl -- PROVED

Let a family of `h` secant records have pairwise distinct tentative arcs in one
directed single cycle and pairwise distinct witness arcs in another directed single
cycle.  Form a conflict graph on the records by joining two records when their
tentative arcs are adjacent in the first cycle or their witness arcs are adjacent in
the second cycle.

The conflict graph has maximum degree at most four.  It therefore contains a matching
of nonconflicting record pairs covering all but at most five records.

For every paired block, both internal cross states move all four corresponding current
source endpoints.

#### Proof

One directed cycle arc is adjacent to at most two other arcs.  The two cycle layers
therefore contribute at most four conflicting partners.  A maximal matching in the
complement leaves an independent set in the complement, hence a clique in the conflict
graph, of size at most `Delta+1<=5`.  Thus all but at most five vertices are paired.

For nonadjacent arcs `r->pi(r)` and `s->pi(s)`, neither crossed arc
`r->pi(s)` nor `s->pi(r)` is diagonal.  Apply this separately in the two cycles. ∎

The same argument applies when the endpoint states are unions of boundedly many path
components: finite component-end conflicts increase the maximum degree by only an
absolute constant.

## 3. Target bank survives pairing

### Corollary PP3azm -- PROVED

A resource-disjoint secant bank of size `h=Omega(s)` yields

```text
floor((h-5)/2)=Omega(s)
```

pairwise resource-disjoint four-state product switches.  Every product switch carries
at least two units of the original allocation-failure credit and has one preferred
state `T^(1,1)` clearing both designated source certificates.

#### Proof

Apply PP3azl and use resource disjointness of the original records.  Each paired record
contributes one distinct marked source endpoint and one designated credit unit.  The
all-cross state moves both marked endpoints by PP3azl. ∎

Thus the constant loss from pairing is harmless at every active marked scale.

## 4. Exact finite-state normal form

One paired switch has alphabet

```text
Omega_4={(0,0),(0,1),(1,0),(1,1)}.
```

### Proposition PP3azn -- PROVED

For a bank of resource-disjoint paired switches:

1. every local state preserves saturation and all permanent pool rectangles;
2. every collinear-triple bad box meets at most three switch variables;
3. every candidate-shadow, old-grid endpoint-shadow, or active-anchor insertion event
   meets at most two switch variables;
4. selected-controller puncturing and role-domain restrictions remain bounded local
   conditions; and
5. the preferred state `(1,1)` has zero direct recreation cost for its two designated
   secant certificates.

#### Proof

Item 1 is PP3azk.  The variable supports are pairwise resource-disjoint, so a source
triple meets at most three supports and a blocker pair at most two.  Controller and role
conditions depend on boundedly many selected cells exactly as in the complete endpoint
normal form.  The last item is the all-cross conclusion of PP3azk. ∎

This is the same four-state rank-at-most-three finite CSP used by the multistate
rectangle chain.

## 5. Current potential and source-mass accounting

Let the current potential be

```text
Theta_E^+=Xi_cell+Lambda_E+Xi_old.
```

### Theorem PP3azo -- PROVED / CONDITIONAL EXISTING CURRENT RECTANGLE INTERFACES

For a paired secant-switch bank at the adaptive secondary scale, exactly one of the
following occurs.

1. A source-valid selection of product states moves all designated marked endpoints,
   clears their assigned secant certificates, and has `Theta_E^+` insertion cost below
   the original removal credit.
2. Unary candidate-shadow, active-anchor, or old-grid endpoint-shadow support produces
   a current paid structure.
3. Binary current-potential weight produces an `A_2/B_3/B_4`, fixed-cell fan, path,
   partner, or current endpoint-bank structure.
4. A conditional Hall, alternating, non-superregular, or locally impossible product
   state is produced explicitly.

Anchored-pair and inserted-triple source mass do not remain terminal after chromatic
amplification.

#### Proof

Use PP3azn as the four-state input to the cross-block and equitable-colour selection
chain.  The normalized anchored-pair and inserted-triple terms vanish by PP3tb--PP3td;
the proof is unchanged by replacing one rectangle variable with a four-cell product
switch because the local alphabet and support ranks remain bounded.  Hard unary old-grid
support is current `Xi_old` credit by PP3aze.  The residual unary and binary terms are
current potential weights and enter the stated current conversion interfaces. ∎

The original allocation credit is spent only in item 1 or by an earlier favourable
entry deletion.

## 6. Fixed-centre fan with fillers

Suppose a secant cover has one fixed tentative pivot `a` and many witness pivots `z_r`.
One cannot pair two records directly because their tentative resources coincide.
Choose one witness record and add:

```text
one tentative-block filler arc a',
one witness-block filler arc z'.
```

### Proposition PP3azp -- PROVED / CONDITIONAL BOUNDED ROLE-HOST INTERFACE

For every conditioned centre record `(a,b,z_r)`, the bounded complete-support host
supplies either:

1. fillers `a',z'` such that the paired internal cross state omits `a,z_r`, moves the
   centre and witness endpoints, preserves both permanent blocks, and has no positive
   current insertion event; or
2. a bounded terminal current support pencil, conditional Hall obstruction, or
   locally impossible state.

#### Proof

Each filler belongs to one specified permanent block and must avoid only a bounded list
of endpoint resources, diagonal adjacencies, source events, and current potential
events.  This is the bounded marked role-host theorem with selected-controller
puncturing.  Given the fillers, apply PP3azk to the pairs `(a,a')` and `(z_r,z')`. ∎

Thus the fixed-centre cover is a conditional paired-switch star, rather than a
cross-pool rectangle star.

## 7. Correction to the direct secant switch

### Corollary PP3azq -- PROVED

The direct switch PP3ayx--PP3ayy is restart-compatible when the tentative and witness
pivots lie in one common permanent matching block, or when fixed infrastructure is not
being preserved.

For pivots in different permanent blocks, PP3azk--PP3azp replace it without loss of
asymptotic bank size or designated credit.

#### Proof

A direct cross-pool state uses cells in `X_i x Y_j` and `X_j x Y_i`, which need not be
controller edges of either permanent macro.  The paired internal product uses only
`X_i x Y_i` and `X_j x Y_j`.  Apply the preceding results. ∎

## 8. Revised secant rectangle endpoint

### Corollary PP3azr -- PROVED / CONDITIONAL NAMED CURRENT RECTANGLE INTERFACES

Every complete secant-shadow cover now has a pool-compatible realization:

1. the resource-disjoint branch gives a target bank of paired four-state switches;
2. the fixed-centre branch gives a conditional paired-switch star with bounded fillers;
3. the same-block special case may use the direct two-by-two switch;
4. every terminal weighted branch is a current `Theta_E^+` branch or an explicit
   current endpoint-host obstruction.

The cross-pool fixed-infrastructure mismatch in PP3ayz--PP3azb is therefore repaired.

The no-three-in-line conjecture remains unproved.
