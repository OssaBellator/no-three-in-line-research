# Reference-state normalization and blocker-exchange Hall cores

**Branch:** `research/alternating-core-chain`

AC3it leaves a state-derived host-drift profile at fixed arithmetic/context,
envelope epoch and unavailable-resource mask.  The profile was stated as a
possible change of reference matching, opposite-layer exclusion or derived
allowed host.  This note separates those effects exactly.

Reference-matching drift is removable: every historical target matching can be
projected to the unique alternating component through the paid pivot relative
to one current reference matching.  Opposite-layer feasibility is then one
ordinary perfect-matching problem in a blocker exchange digraph.  On the
unrestricted board that problem is always solvable for `n>=3`.  In a restricted
host, failure has a canonical minimal Hall core, not a generic host-change
label.

The result does not claim that every restricted-host Hall core is already paid.
It reduces the remaining temporal obstruction to a zero-mobility blocker row,
a low-mobility repair column, or the same role-pure collision outputs already
handled by AC3i--AC3j.

## Current base-host model

Fix one current ordered state

\[
S=(M,O)
\]

of disjoint permutation matchings on an `n x n` board.  Fix a current pivot
cell

\[
e\in M
\]

carrying one private current pivot bucket of certified weight `W_e`.  Let `A`
be the fixed base host for the changed layer and `B` the fixed base host for
the blocker layer.  Thus

\[
M\subseteq A,\qquad O\subseteq B.
\]

The current opposite layer is not deleted from `B`; disjointness from a proposed
active matching will be enforced by choosing a new blocker matching.

Let `N` be any historical or candidate active permutation matching satisfying

\[
N\subseteq A,\qquad e\notin N.
\]

No assumption is made that different targets `N` have one common historical
reference state.

## AC3iu -- current-reference component projection -- PROVED

Let `Gamma_e(M,N)` be the unique component of the matching symmetric difference

\[
M\triangle N
\]

which contains `e`.  Switch only this component in `M`, leaving every other
component unchanged, and call the resulting matching `P_N`.

Then:

1. `P_N` is a permutation matching;
2. `P_N subseteq M union N subseteq A`;
3. `e notin P_N`;
4. `M triangle P_N` is exactly one alternating cycle containing `e`;
5. if `M triangle N` already has one nontrivial component, then `P_N=N`.

Consequently variation of the historical reference matching is not itself an
execution obstruction.  Every historical target in one fixed active base host
produces a one-cycle candidate relative to the current matching `M`.

### Proof

The symmetric difference of two perfect matchings is a disjoint union of even
alternating cycles.  Since `e` belongs to `M` and not to `N`, exactly one such
cycle contains `e`.  Replacing the `M` edges of that cycle by its `N` edges
preserves every row and column exactly once.  All retained and inserted cells
belong to `M union N`, and the edge `e` is removed.  The final two statements
are immediate from the construction. QED.

Different historical targets may project to the same `P_N`.  Such repetition
is retained as one exact projected-state ancestry class rather than counted as
distinct menu states.

## Blocker exchange digraph

Fix one projected matching `P=P_N`.  Write the current blocker as

\[
O=\{(c,\rho_c):c\in[n]\}.
\]

Identify the blocker row `rho_c` with a source vertex `c`.  Define the directed
exchange graph `D_P` on `[n]` by putting an arc

\[
a\longrightarrow b
\]

exactly when the blocker cell

\[
(b,\rho_a)
\]

belongs to

\[
B\setminus(P\cup\{e\}).
\]

A directed cycle cover means a permutation `sigma` of `[n]` with
`a -> sigma(a)` for every `a`.

## AC3iv -- exact blocker-exchange equivalence -- PROVED

The following objects are in bijection:

1. directed cycle covers `sigma` of `D_P`;
2. blocker permutation matchings
   \[
   O_\sigma=\{(\sigma(a),\rho_a):a\in[n]\}
   \]
   contained in `B`, disjoint from `P`, and avoiding `e`.

Hence `P` extends to a legal two-layer state with the paid pivot absent from the
full union if and only if `D_P` has a directed cycle cover.

Moreover the loop `a -> a` is present exactly when the current blocker cell
`(a,rho_a)` does not belong to `P`.  Thus the missing loops are precisely the
current blocker intersections `O cap P`.

### Proof

Because the rows `rho_a` are all distinct, assigning them to the destination
columns `sigma(a)` gives one blocker cell in every row and every column exactly
when `sigma` is a permutation.  The arc condition is exactly containment in
`B` together with avoidance of `P` and `e`.  The converse reads the source row
of every cell of a blocker matching.  Finally `e notin O` because `e in M` and
`M,O` are disjoint, so a current loop is deleted exactly by membership in `P`.
QED.

### Complete-host corollary

If `B=[n] x [n]` and `n>=3`, every projected `P` has a blocker repair.

After relabelling rows so that `P` is the identity matching, use the two cyclic
permutations

\[
c\mapsto c+1,\qquad c\mapsto c+2\pmod n.
\]

Both avoid `P`.  Since `e notin P`, the cell `e` lies in at most one of these
two cyclic matchings.  The other is a blocker repair avoiding `P` and `e`.

Therefore opposite-layer occupancy by itself is never a terminal AC4
obstruction on the unrestricted board.  A failed blocker repair certifies a
genuine missing-edge defect of the restricted base host `B`.

## AC3iw -- repaired common-base-host cycle menu -- PROVED

Let `mathcal P` be any nonempty finite set of distinct current-reference
projections.  For every `P in mathcal P` whose exchange graph has a cycle cover,
choose one canonical cover `sigma_P` and form

\[
S_P=(P,O_{\sigma_P}).
\]

If at least one projection is repairable, the states `S_P` form one legal
finite menu.  Every menu state:

1. consists of two disjoint permutation layers;
2. uses only the fixed base hosts `A,B`;
3. removes `e` from the full union;
4. destroys the complete private pivot bucket of weight `W_e`.

No disjointness between different menu states is required.

Let `E_r` be the expected created union-collateral of created-cell rank
`r=1,2,3` under any probability law on the menu.  Then

\[
E[\text{created collateral}]=E_1+E_2+E_3,
\qquad
E[\text{destroyed payment}]=W_e.
\]

If

\[
W_e>E_1+E_2+E_3,
\]

one repaired state improves.  If no state improves, one rank satisfies

\[
\boxed{E_r\ge W_e/3}.
\]

The AC3gk--AC3gj realization/pivot interface therefore returns, for every
`K_0>=1`, an explicit complete-envelope overload, a pivot payment at least

\[
\boxed{W_e/(3K_0)},
\]

or a next-rank return at least

\[
\boxed{W_e/(9K_0)}.
\]

### Proof

AC3iu and AC3iv give legality, host containment and removal of `e`.  Every
certificate in the private bucket contains `e`, so all are destroyed.  Average
the exact created-minus-destroyed identity and split a failed average among the
three created-cell ranks, exactly as in AC3in. QED.

## AC3ix -- canonical minimal blocker Hall core -- PROVED

Suppose `D_P` has no directed cycle cover.  In its bipartite
source--destination representation choose an inclusion-minimal nonempty source
set `X` with

\[
|N(X)|<|X|.
\]

Put `m=|X|`.

Exactly one of the following holds.

### 1. Dead blocker row

If `m=1`, write `X={a}`.  Then

\[
N(X)=emptyset.
\]

The current blocker cell `(a,rho_a)` belongs to `P`, and the blocker row
`rho_a` has no admissible placement anywhere in
`B setminus (P union {e})`.

### 2. Reused-target Hall core

If `m>=2`, then

\[
\boxed{|N(X)|=m-1}
\]

and, for every `a in X`,

\[
\boxed{N(X setminus {a})=N(X)}.
\]

Consequently:

- every source in `X` has at least one admissible repair destination;
- every destination in `N(X)` is reached from at least two sources of `X`;
- at least one source in `X` has its current loop missing, equivalently its
  current blocker cell belongs to `P`.

### Proof

Hall's theorem gives a deficient set.  Inclusion minimality gives the singleton
case immediately.  In the non-singleton case every proper nonempty subset
satisfies Hall.  Thus `N(X\{a})` has size at least `m-1`, is contained in
`N(X)`, and deficiency gives `|N(X)|<=m-1`; all are equalities.  A destination
used by only one source would disappear after deleting that source, contrary
to the equality.  Every singleton source has a neighbour.  If every current
loop in `X` were present, the distinct vertices of `X` themselves would lie in
`N(X)`, contradicting deficiency. QED.

### Role-pure collision interface

Suppose the admissible repair arcs in the core carry one of at most `R` finite
host/arithmetic role labels.  Let

\[
d=\min_{a\in X}|N(a)|.
\]

For `m>=2`, AC3i applies verbatim with reopening set `X`, token set `N(X)`,
minimum eligibility `d` and role alphabet `R`.  In particular, if

\[
B_0=R(m-1),\qquad E_0=dm=qB_0+r,\qquad 0\le r<B_0,
\]

the role-pure shared-target collision mass is at least

\[
\boxed{
B_0\binom q2+rq.
}
\]

AC3j then routes that mass to either:

- one destination token reused in one role by many source columns; or
- one source column incident in one role with many distinct reused repair
  destinations.

If `d` is small, the core is instead an explicit low-mobility blocker source.
Thus a failed blocker completion is never left as an unlabelled host defect.

## AC3iy -- fixed-mask host-drift normalization -- PROVED

Retain one fixed arithmetic/context label, envelope epoch, unavailable mask,
active base host `A`, blocker base host `B`, current state `(M,O)`, pivot `e`
and private pivot payment.

Every recurrent target family from AC3it has the following exact continuation.

1. Project every historical target to the current reference matching by AC3iu.
2. If a projected state has a blocker cycle cover, all distinct repairable
   projections enter the executable menu AC3iw.
3. If a projected state is not repairable, it returns:
   - one dead blocker row;
   - one low-mobility minimal Hall core;
   - or the role-pure shared-target/resource-star output of AC3ix.
4. If `A`, `B`, the arithmetic/context label, mask or envelope epoch is not
   fixed across the selected occurrences, that changed field is retained as
   the genuine outer transition.

Therefore **reference-matching drift and raw opposite-layer exclusion are
removed from the residual AC4 dictionary**.  At fixed base hosts, the only
state-derived host obstruction is a canonical blocker-exchange Hall
certificate.  On the complete blocker host even that obstruction is absent.

For a weighted family of nonrepairable distinct projections of total weight
`V`, choose in every canonical Hall core the least source whose current loop is
missing.  Its current blocker cell belongs to the projection.  Since `O`
contains exactly `n` cells, one exact current blocker cell carries canonical
witness weight at least

\[
\boxed{V/n}.
\]

This is an explicit fixed-blocker concentration, not generic temporal drift.

## Consequence

After AC3it and AC3iu--AC3iy, a long fixed-mask history cannot remain obstructed
merely because its historical reference matchings or opposite layers differ.
It either:

- executes as a current-reference repaired cycle menu;
- returns a dead or low-mobility blocker repair core;
- returns a role-pure reused-target/resource star;
- concentrates on one exact current blocker cell;
- or changes one genuinely external base-host, arithmetic/context, mask or
  envelope field.

The next AC4 target is payment and finite ancestry for these blocker-exchange
Hall outputs together with physical occurrence realization of the attached
carry/BDA/RI role.

## Finite check

`scripts/verify_ac_host_drift_normalization.py` exhausts permutation projections
through side six, every directed exchange graph through four sources, all
minimal Hall cores, exhaustive small role assignments, complete-host repairs,
fixed-blocker concentration, failed-menu rank ledgers and every displayed
constant.
