# Bounded marked sets admit separated zero-cost cancellation hosts

PP3aqa--PP3aqg cancel one selected local insertion atom by moving one of its
inserted endpoints.  A conditioned path has at most four inserted local cells and
at most ten atoms.  It is more efficient to move the entire bounded local cell set
in one second trade.

Choose a single-cycle state in which no two distinguished local indices are
adjacent.  Every selected arc then uses at least one ordinary helper.  Consequently
every nonzero canonical source or insertion event has nonempty ordinary-helper
support.  An independent helper block makes the second trade source-valid with
zero insertion cost.

The complete local `A_2/B_3/B_4` table created by the first trade is then destroyed
and cancelled at once.  The composite change is exactly the negative of the
first trade's original removal credit, apart from any genuinely nonlocal first-step
cost.

## 1. Separated single cycles through a bounded marked set

Let

```text
D={d_1,...,d_r}
```

be distinguished endpoint indices, where `1<=r<=4`, and let `H` be an ordinary
helper set disjoint from `D`, with

```text
|H|>=r.
```

Call a directed single cycle on `D union H` **D-separated** when no selected arc
has both endpoints in `D`.

### Proposition PP3aqh -- PROVED

A `D`-separated directed single cycle exists.  Every distinguished index is moved.

#### Proof

Choose distinct helpers `h_1,...,h_r` and start the cyclic order

```text
d_1,h_1,d_2,h_2,...,d_r,h_r.
```

Insert every remaining helper anywhere between two existing objects.  Consecutive
distinguished indices never occur.  The resulting order is one directed cycle,
so every index, including every member of `D`, is moved. ∎

The construction permits any additional ordering or pool constraints that can be
imposed while inserting the remaining helpers.

## 2. Complete support after several marked indices are fixed

Fix one `D`-separated cycle law.  For every canonical source-invalid or positive
insertion signature `G`, define its ordinary-helper support

```text
supp_H(G)=supp(G) cap H.
```

Let

```text
H_D
```

be the simple hypergraph of all nonempty supports `supp_H(G)` arising from
positive signatures compatible with a `D`-separated single cycle.

### Proposition PP3aqi -- PROVED

Every nonzero selected canonical source or insertion event has nonempty ordinary-
helper support.

#### Proof

Every nonzero insertion atom contains at least one selected arc.  By
`D`-separation, each selected arc has an ordinary helper endpoint.  Thus every
`A_2`, `B_3`, or `B_4` event contains a helper index.

Every canonical source-invalid event also contains at least one selected inserted
arc.  The marked source classes of PP3aod may additionally use retained anchors or
several inserted arcs, but each selected arc still contains a helper.  Hence its
ordinary-helper support is nonempty.

The only formal insertion classes with no selected off-diagonal arc are the
diagonal unary class and a transposition; both are absent from a single cycle by
PP3aof. ∎

This is the bounded-multimarked analogue of PP3aod--PP3aoh.

## 3. Independent helpers give a zero-cost second trade

### Theorem PP3aqj -- PROVED

If `H_0 subseteq H` is independent in `H_D` and `|H_0|>=r`, then some
`D`-separated single-cycle state on `D union H_0` satisfies

```text
source-invalid count=0,
insertion cost=0.
```

It moves every distinguished local cell.

#### Proof

Choose any `D`-separated cycle supplied by PP3aqh.  By PP3aqi every nonzero
canonical event has a helper support belonging to `H_D`.  Selection of that event
would place its support inside `H_0`, contradicting independence.  Therefore no
source-invalid or positive insertion event is selected. ∎

The theorem is deterministic after the independent helper set is chosen; no
residual first moment remains.

## 4. Independent set or another terminal pencil

Suppose the ambient ordinary-helper reservoir has size `N_D`, and the maximum
ordinary-helper support rank is at most five.

### Theorem PP3aqk -- PROVED

For every required helper count `b-r`, exactly one of the following occurs.

1. `H_D` has an independent set of size `b-r`, giving a zero-cost separated host.
2. There is a fixed ordinary-helper core of size at most four with at least

   ```text
   (N_D-b) / [sum_(j=0)^4 binom(b-1,j)]
   ```

   distinct variable extensions.

For adaptive `b=N_D^(o(1))`, the extension family has size `N_D^(1-o(1))`.

#### Proof

Apply the maximal-independent-set localization PP3ann--PP3aoo to `H_D`.  The
bounded distinguished set changes the required independent-set size by only
`O(1)` and does not change the support-rank bound. ∎

Thus failure of the multimarked zero-cost host is another explicit terminal
source or insertion pencil, not diffuse collateral.

## 5. Cancellation of the complete local table

Let a source-admissible first trade `T_1` have exact removal credit `R_1` and,
after independent nonlocal completion, insertion cost

```text
J_loc,
```

where `J_loc` is the complete local `A_2/B_3/B_4` table on a set `D` of at most
four inserted cells.  Let `J_nonloc` denote any first-step cost not removed by the
independent completion, so generally

```text
I_1=J_loc+J_nonloc.
```

Perform a source-admissible second trade `T_2` that moves every point of `D`.

### Theorem PP3aql -- PROVED / CONDITIONAL BOUNDED-MARKED HOST INTERFACE

The two-step potential change satisfies

```text
Xi(S_2)-Xi(S_0)
<=
J_nonloc+I_2-R_1,
```

where `I_2` is the complete second-step insertion cost.

If the separated independent host PP3aqj is available, then `I_2=0`, and

```text
Xi(S_2)-Xi(S_0)
<=
J_nonloc-R_1.
```

In particular, when the first independent completion has `J_nonloc=0`, the
composite change is at most `-R_1`.

#### Proof

Every local unary atom contains one point of `D`, and every local binary atom
contains two points of `D`.  Moving all of `D` destroys every one of the
`J_loc` incidences, with multiplicity.  Hence

```text
Xi(S_1)-Xi(S_0)=J_loc+J_nonloc-R_1
```

and

```text
Xi(S_2)-Xi(S_1)<=I_2-J_loc.
```

Add.  Under PP3aqj, `I_2=0`. ∎

This cancels all ten possible local atoms simultaneously.

## 6. Application to conditioned petals

### Corollary PP3aqm -- PROVED / CONDITIONAL EXISTING SUPPORT-HOST INTERFACES

For every source-clean conditioned arc, path, or partner petal from
PP3aok--PP3aox, one of the following holds.

1. Robust final allocation absorbs the complete local table.
2. A bounded-multimarked independent second trade cancels the complete local table
   and strictly decreases `Xi` using the original first-step removal credit.
3. Failure of the independent second host produces a near-linear fixed-core source
   or insertion pencil.
4. Controller-pool, distinguished-endpoint, Hall, alternating, transition, or
   source-clean host preparation fails explicitly.
5. Genuine first-step nonlocal collateral remains despite the complete-support
   selection.

Thus a second-step foreign-cost estimate is unnecessary in the ideal independent
host branch: the complete second insertion cost is exactly zero.

## 7. Revised composite frontier

### Corollary PP3aqn -- PROVED

After complete helper-support selection, neither an individual local atom nor the
sum of the finite local atom table is a paid obstruction.  The entire table can be
removed by one bounded-multimarked zero-cost trade.

The remaining composite paid frontier is therefore narrowed to:

1. failure to find the required independent helper set, producing another
   near-linear terminal pencil;
2. external bounded-multimarked source/transition/pool/Hall/alternating host
   failure;
3. genuinely nonlocal first-step cost not captured by the complete-support
   hypergraph;
4. branches in which the distinguished local cells cannot be moved together in
   one controller-preserving endpoint state.

The no-three-in-line conjecture remains unproved.
