# Bounded marked sets embed in one controller-disjoint permutation layer

PP3aqh--PP3aqn use a separated cycle through at most four distinguished local
cells and ordinary helpers.  The remaining formulation listed the possibility that
those cells could not be moved together while preserving controller and pool
coordinates.

In the endpoint architecture, the distinguished cells are produced by a trade
inside one permutation layer.  They therefore remain tied indices of one
permutation graph.  Active controllers occupy only a fixed proper fraction of that
layer, while every extra exceptional set used by the marked construction is
`o(m)`.  A linear controller-disjoint helper reservoir remains.

After puncturing the bounded subset of distinguished cells that are themselves
active controllers, alternate the marked indices with ordinary helpers in one
cycle.  This preserves the permutation layer and saturation, moves every marked
cell, and fixes every active controller.  Hence bounded marked coordinate placement
is deterministic; the only remaining failures are source/support or external Hall
and alternating constraints on the chosen helper block.

## 1. One-layer tied endpoint representation

Let

```text
M={(x_i,y_i): i in [m]}
```

be one permutation layer.  A tied endpoint state on an index set `J subseteq [m]`
replaces the cells of `M` indexed by `J` according to a permutation `pi` of `J`:

```text
(x_i,y_i) -> (x_i,y_(pi(i))).
```

### Proposition PP3ari -- PROVED

Every tied endpoint permutation on `J` preserves saturation and leaves every cell
of `M` outside `J` unchanged.  The resulting cells on the selected old columns and
rows again form a perfect matching.

#### Proof

The selected old columns are used once, and `pi` uses every selected old row once.
All unselected columns and rows retain their original matching cells. ∎

Thus controller preservation is guaranteed whenever `J` is disjoint from the
active controller indices.

## 2. Linear controller-disjoint helper reservoir

Let `E subseteq [m]` be the active controller indices in the layer.  Let `D` be a
distinguished set of size `r<=4`, and let `B` be any additional forbidden helper
set containing already used endpoints, punctured values outside `D`, or externally
reserved indices.

### Proposition PP3arj -- PROVED

Assume

```text
|E|<=rho m,
r<=4,
|B|=o(m)
```

for one fixed `rho<1`.  After removing the marked controller indices `D cap E`
from the active controller set, the ordinary helper reservoir

```text
H=[m]\(E union D union B)
```

has size

```text
|H| >= (1-rho-o(1))m-r = Theta(m).
```

#### Proof

Delete the displayed sets and use the union bound.  The bounded marked set changes
the estimate by `O(1)`. ∎

The same conclusion holds in the original-reference cascade with the untouched-
original reservoir of PP3aiw.

## 3. Bounded batch puncturing costs only bounded domain margin

Some members of `D` may be active controllers before the second trade.

### Proposition PP3ark -- PROVED

Puncturing all indices in `D cap E` removes at most `r<=4` controller values from
any macro domain.  Every original balanced ownership and global matching
certificate with fixed positive margin survives for sufficiently large `R`.

Moreover, any candidate entries controlled by a punctured marked cell are deleted
from the potential, which can only improve the chronological change.

#### Proof

Apply the one-controller domain monotonicity PP3ake successively at most four times.
The cumulative domain loss is at most four, hence `o(R)`.  Candidate-universe
deletion is monotone by PP3apm. ∎

No designated local-table incidence needs to survive such a puncture: an incidence
whose controlling entry is deleted is already removed favourably from the active
potential.

## 4. Separated cycle preserving every active controller

Fix any helper count `h>=r` with `h<=|H|`, and choose distinct helpers
`h_1,...,h_h` from `H`.

### Theorem PP3arl -- PROVED

There is a single-cycle endpoint state on

```text
J=D union {h_1,...,h_h}
```

such that:

1. every member of `D` is moved;
2. no selected arc has both endpoints in `D`;
3. every active controller in `E\D` is fixed;
4. the resulting layer is again a permutation graph;
5. saturation is preserved.

#### Proof

Begin the cyclic order

```text
d_1,h_1,d_2,h_2,...,d_r,h_r
```

and insert the remaining helpers between existing cyclic objects.  This is the
separated-cycle construction PP3aqh.  The selected index set is disjoint from
`E\D` by Proposition PP3arj, so all active controllers are outside `J` and remain
fixed.  Apply PP3ari for the matching and saturation statements. ∎

Any desired state size

```text
2r<=|J|<=r+|H|
```

is available.

## 5. Coordinate-complete bounded marked host

### Theorem PP3arm -- PROVED / CONDITIONAL SOURCE-SUPPORT INTERFACE

Suppose a bounded marked set `D`, `|D|<=4`, lies in one permutation layer whose
active controller density is at most `rho<1`.  Suppose every additional reserved
or forbidden index set has size `o(m)`.  Then the coordinate, pool, saturation, and
controller-preservation requirements for PP3aqh--PP3aqn are automatically
satisfied after bounded batch puncturing.

Exactly one of the following remains.

1. A complete-support independent helper subset exists, giving the zero-cost
   separated trade.
2. A canonical terminal source or insertion pencil is converted by PP3aqo--PP3aqt.
3. Source-clean, transition, anchor, Hall, alternating, matching, or distinguished-
   endpoint constraints exclude the available layer reservoir.
4. The marked cells do not belong to one common permutation layer, or the active
   controller set occupies `1-o(1)` of every eligible layer.

#### Proof

Propositions PP3arj--PP3ark prepare a linear controller-disjoint reservoir and
preserve every robust allocation certificate.  Theorem PP3arl supplies the required
separated single cycle.  Apply the complete-support dichotomy PP3aqj--PP3aqr.
Only the listed source/support or genuinely external alternatives remain. ∎

## 6. Application to conditioned local tables and punctured stars

### Corollary PP3arn -- PROVED / CONDITIONAL COMMON-LAYER HYPOTHESIS

For every local table produced by a one-layer endpoint trade and every captive-star
centre belonging to that same layer:

1. all bounded marked cells can be punctured if necessary at `O(1)` domain cost;
2. a linear controller-disjoint ordinary-helper reservoir remains;
3. all marked cells can be moved together in a separated single cycle;
4. the complete local table or punctured-star insertion table is zero-cost or
   converts to an already closed pencil;
5. inability to preserve the permutation layer, saturation, active controllers, or
   pool disjointness is impossible.

The only live marked-host failures are source/support constraints imposed on the
available helpers or absence of the common-layer hypothesis itself.

## 7. Revised bounded-marked frontier

### Corollary PP3aro -- PROVED

The phrase "inability to move the bounded local cell set while preserving
controller and pool coordinates" is no longer an independent frontier in the
standard one-layer architecture.  It reduces to:

1. the marked cells are not co-layered;
2. no eligible layer has a linear controller-disjoint reservoir;
3. a source-clean, transition, anchor, Hall, alternating, matching, or distinguished-
   endpoint condition deletes almost all of that reservoir.

Under co-layering and controller density bounded away from one, coordinate
placement is deterministic and the complete-support conversion applies.

The no-three-in-line conjecture remains unproved.
