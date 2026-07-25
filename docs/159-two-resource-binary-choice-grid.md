# Two-resource binary choice grids

PP3xh--PP3xi leave a repeated secondary resource supporting many linear partner
fibres. A perfect matching chooses only one cell at each fixed endpoint resource.
The whole pencil is therefore a two-choice forbidden matrix: choose one local
cell at the first resource and one compatible local cell at the second.

In a superregular host, every compatible pair of allowed cells extends to a full
perfect matching after deleting its four endpoint resources. Hence one allowed
nonconflict pair avoids the entire two-resource pencil. Failure forces the binary
conflict relation to contain every compatible pair in two linear local choice
sets, producing a quadratic complete choice grid.

## 1. Choice sets at two resources

Let `G=(L,R;E)` be a balanced endpoint host of order `q`. Fix two distinct typed
endpoint resources `v,w`.

There are three cases.

1. `v,w` are both left resources. Let `A` and `B` be the allowed cells incident
   with `v` and `w`.
2. `v,w` are both right resources. Use the transposed definition.
3. `v` is left and `w` is right. If the common cell `(v,w)` is allowed and extends
   to a perfect matching, it already bypasses every two-cell conflict touching
   both resources. Otherwise remove the common cell and let

   ```text
   A={cells incident with v but not w},
   B={cells incident with w but not v}.
   ```

Let `A ~ B` denote compatible pairs: the two cells use distinct left and right
resources. Let

```text
F subseteq {(a,b) in A x B : a ~ b}
```

be the binary-conflict relation supported by the repeated two-resource pencil.

## 2. Exact two-choice conditioning

Every perfect matching that does not use the common cell in case 3 contains one
unique cell `a in A` and one unique cell `b in B`, with `a~b`.

For a compatible pair `(a,b)`, let `G_ab` be the host obtained by deleting the
left and right endpoints used by `a` and `b`.

### Proposition PP3xj -- PROVED

A perfect matching containing `a,b` avoids every conflict in `F` if and only if

```text
(a,b) notin F.
```

#### Proof

The matching chooses no other cell incident with either fixed resource. Every
conflict in the pencil contains one choice from `A` and one from `B`, so the only
pencil conflict that can occur is the selected pair itself. ∎

### Theorem PP3xk -- PROVED

The host has a perfect matching avoiding the entire two-resource pencil if and
only if at least one compatible nonconflict pair `(a,b)` has a perfect matching in
`G_ab`.

#### Proof

Adjoin `a,b` to a perfect matching of `G_ab` and apply PP3xj. Conversely, delete
the two selected cells from any pencil-avoiding perfect matching. ∎

This is the two-resource analogue of PP3ww.

## 3. Superregular extension of every local pair

### Proposition PP3xl -- PROVED FROM STANDARD SUPERREGULAR SLICING

Fix `delta>0` and sufficiently small `epsilon>0`. If `G` is
`(epsilon,delta)`-superregular, then for every compatible pair of allowed cells
`a,b`, the residual host `G_ab` is

```text
(epsilon',delta-o(1))-superregular
```

for every fixed `epsilon'>epsilon` and all sufficiently large `q`. In particular,
`G_ab` has a perfect matching.

#### Proof

The pair uses two left and two right resources. Deleting those four vertices
changes degrees and densities by `O(1/q)`. Apply the standard slicing estimate and
Hall's theorem for superregular graphs. ∎

### Corollary PP3xm -- PROVED

In a superregular host, the two-resource pencil obstructs perfect matching only if

```text
F = {(a,b) in A x B : a~b};
```

that is, every compatible local pair is a binary conflict.

The opposite-side case has the additional immediate escape through the common
cell `(v,w)` whenever that cell is allowed and completable.

#### Proof

Any compatible pair outside `F` extends by PP3xl and avoids the pencil by PP3xk.
∎

## 4. Size of a complete choice grid

Assume each fixed resource has host degree at least `delta q`.

### Proposition PP3xn -- PROVED

If both fixed resources lie on the same bipartition side, then the number of
compatible local pairs satisfies

```text
|{(a,b) in A x B : a~b}|
>= |A||B|-q
>= delta^2 q^2-q.
```

If the resources lie on opposite sides and the common cell is excluded, every
pair in `A x B` is compatible, so

```text
|A x B| >= (delta q-1)^2.
```

#### Proof

For two same-side resources, incompatibility means that the two cells share their
opposite resource. There are at most `q` such pairs, one for each opposite
resource. In the opposite-side case, removing the common cell ensures distinct
left and right endpoints automatically. ∎

Thus a failed superregular two-resource pencil contains `Omega(q^2)` binary
conflicts in one complete local choice grid.

## 5. Candidate incidence inside the complete grid

For every conflict pair `(a,b)`, choose one controller candidate point `z_ab`
blocked by that pair. Then `a,b,z_ab` are collinear.

### Proposition PP3xo -- PROVED

For every threshold `D>=1`, a complete choice grid of `H` conflicts has one of:

1. one controller candidate assigned to at least `D` conflict pairs;
2. at least `H/D` distinct controller candidates.

When `H=Omega(q^2)` and `D=q`, this gives either a candidate incident with
`Omega(q)` grid secants or `Omega(q)` distinct controller candidates.

#### Proof

Pigeonhole the assigned conflicts by their chosen candidate. ∎

For two fixed same-side resources, the pairs assigned to one candidate form a
projective correspondence between the two resource lines. For opposite-side
resources, they form a pencil of secants joining one fixed row and one fixed
column.

## 6. Revised two-resource endpoint

A repeated secondary-resource pencil in the superregular branch reduces to:

1. one compatible nonconflict pair and immediate conditional completion;
2. an allowed common-cell bypass in the opposite-side case;
3. a complete quadratic binary choice grid;
4. a candidate-rich secant pencil or linearly many distinct controller candidates;
5. source-invalid or paid collateral after the local pair is fixed.

A mere repeated secondary resource with linear partner traces is no longer the
terminal obstruction.
