# Active and latent dependencies of saturated hard literals

**Branch:** `research/alternating-core-chain`

AC3ld--AC3lh complete a target whenever a residual transversal has globally
unused hard phases.  The remaining obstruction contains one or more blocks for
which every noncurrent phase is named by an active hard check somewhere in the
fixed registry.  Such global saturation does not mean that every phase is
forbidden in the current context: many named checks may still require other
noncurrent literals.

This note separates those two cases exactly.  Current-context literals return to
the cross-centre hard router.  Every latent literal receives one canonical
noncurrent dependency.  In a fixed hard registry these dependencies form a
functional directed graph, so every chain reaches a current-context blocker or
one simple dependency cycle.

## Canonical saturated-literal records

Let `omega` be the current hard-feasible phase assignment.  For a mutable block
`x`, write

\[
B_x=\mathcal A_x\setminus\{\omega_x\}.
\]

Assume `x` is hard-literal saturated:

\[
B_x\subseteq L_x^{\rm hard}.
\]

For each `b in B_x`, choose the least exact hard check `C_{x,b}` whose literal at
`x` is `b`.  Define the residual mismatch set

\[
D_{x,b}
=
\{(y,f_{C_{x,b}}(y)):
  y\in S_{C_{x,b}}\setminus\{x\},
  f_{C_{x,b}}(y)\ne\omega_y\}.
\]

Since hard rank is at most three,

\[
0\le |D_{x,b}|\le2.
\]

Call `(x,b)` **active** when `D_{x,b}` is empty and **latent** otherwise.
For a latent literal, choose the least member of `D_{x,b}` as its canonical
dependency.

## AC3li -- exact active/latent saturation split -- PROVED

For every saturated block and every `b in B_x`:

1. if `(x,b)` is active, changing only `x` from `omega_x` to `b` violates
   `C_{x,b}` in the current context;
2. if `(x,b)` is latent, `C_{x,b}` is not activated by that one-block change and
   names one or two explicit noncurrent residual literals;
3. distinct phases `b` select distinct exact hard checks.

Thus a saturated block of noncurrent size `h_x` contains exactly `h_x` canonical
literal records, partitioned into current-context blockers and latent dependency
records.

### Proof

When `D_{x,b}` is empty, every residual literal of `C_{x,b}` equals its current
phase, so installing `x=b` creates the forbidden assignment.  When the set is
nonempty, at least one residual literal remains mismatched under the one-block
change, so the selected check is not yet violated.  One exact check has a unique
forbidden literal at block `x`, hence cannot be selected for two different
values of `b`. QED.

This theorem corrects the coarse interpretation of global literal saturation.
Only the active part is an immediate hard target fan.

## AC3lj -- weighted active or latent-role concentration -- PROVED

Give the canonical saturated-literal records nonnegative weights `w(x,b)` and
let their total be `W`.  Split the records into active and latent parts.  One
part has weight at least `W/2`.

Assume the canonical record role alphabet has size at most `R_sat`; a role may
include hard-check kind, rank, target position, mismatch depth and the selected
residual position.  One role-pure class inside the heavier part has weight at
least

\[
\boxed{W/(2R_{\rm sat}).}
\]

If the heavier class is active, it is a role-pure current-context hard phase
family at its block.

If it is latent, push each record weight to its selected noncurrent dependency
literal.  For every threshold `Delta>0`, either:

1. one exact dependency literal receives load greater than `Delta`; or
2. at least
   \[
   \boxed{
   \left\lceil
   \frac{W}{2R_{\rm sat}\Delta}
   \right\rceil
   }
   \]
   distinct dependency literals receive positive load.

### Proof

The active/latent split and role split are ordinary weighted pigeonhole.  In the
latent class, if every dependency load is at most `Delta`, carrying total weight
at least `W/(2R_sat)` requires at least the displayed number of distinct
literals. QED.

No weight in the latent branch is payment.  It is incidence weight attached to
an exact hard dependency.

## Canonical literal-dependency graph

Let `L` be the set of all noncurrent hard literal addresses `(x,b)` appearing in
the fixed registry.  Give every active node no outgoing edge.  Give every latent
node the directed edge

\[
(x,b)\longrightarrow(y,c),
\]

where `(y,c)` is its selected dependency.  The target is again in `L`, because
it is a literal of the selected hard check.  The edge never points to the same
block as its source, since a canonical check contains each block at most once.

## AC3lk -- latent chains reach activity or a simple cycle -- PROVED

Let `U=|L|`.  Starting from any literal node and repeatedly following the
canonical dependency edge:

1. an active node is reached after at most `U-1` latent edges; or
2. a directed simple cycle of latent literals is reached, with length between
   two and `U`.

### Proof

A latent node has exactly one successor and an active node has none.  If a walk
does not reach an active node, after `U+1` visited nodes one node repeats.
Deleting the preperiod leaves a directed simple cycle.  Self-loops are excluded
because source and dependency blocks differ. QED.

The selected hard check on a cycle edge may have a second noncurrent residual
literal.  The cycle is therefore a dependency witness, not a claim that
installing all cycle phases simultaneously violates every selected check.

## AC3ll -- fixed-registry dependency stock -- PROVED

In one fixed hard registry:

1. the canonical dependency graph has at most `U` directed edges;
2. its directed cycles are vertex-disjoint;
3. it has at most `floor(U/2)` directed cycles;
4. every literal node belongs to the in-tree of one active node or one directed
   cycle.

For a two-layer O1 registry, `U<=2n^2`, so the canonical dependency edge stock is
at most `2n^2` and the fixed-registry cycle stock is at most `n^2`.

### Proof

There is at most one edge from each literal node.  A functional directed graph
has at most one cycle in each weak component, and different cycles cannot share
a vertex.  Every cycle has length at least two, giving the cycle-count bound.
The component decomposition gives the final statement.  The O1 physical bound
is the phase-address bound used in AC3lh. QED.

This is a polynomial cycle inventory **inside one fixed canonical hard
registry**.  A change of registry, least-check order, physical occurrence chart
or role interpretation is an AC3ka outer reset and is not silently identified
with the old graph.

## AC3lm -- saturated-literal recurrence interface -- PROVED

Within one fixed outer profile and hard registry, recurrent saturated-block
output returns one of:

1. a role-pure active current-context hard phase family, routed by
   AC3aj--AC3ak and AC3ld--AC3lh;
2. one exact latent dependency literal of high incidence;
3. many distinct latent dependency literals;
4. one exact canonical latent dependency cycle from AC3lk--AC3ll; or
5. a hard-registry, physical, arithmetic, owner, protected-contract or envelope
   reset, recorded as a decorated macro edge.

The dependency-cycle branch is not declared progressive.  It enters AC3lc only
after an arithmetic theorem supplies current payment, strict bounded descent,
physical impossibility or a capacity-one cycle ticket.

### Proof

Apply AC3lj to recurrent saturated records.  Active mass gives conclusion 1.
Latent mass gives conclusions 2 or 3.  Following selected dependencies from any
retained literal gives an active node or a cycle by AC3lk; if the registry
changes before that fixed-graph conclusion is used, retain conclusion 5.
AC3ll bounds the fixed-registry cycle stock. QED.

## Consequence

The local AC4 frontier no longer contains an undifferentiated
"hard-literal-saturated block" label.  It contains only:

- current-context hard target families;
- exact high-incidence latent literals;
- role-pure latent dispersion;
- one of at most `floor(U/2)` canonical dependency cycles in the fixed registry;
- or an exact outer reset.

The next arithmetic task is to classify those active and latent literal roles
by their phase, carry, BDA, RI and protected-resource interpretations, while
preserving the rule that prospective hard geometry carries no destroyed
payment.
