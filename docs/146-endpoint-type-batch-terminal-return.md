# Endpoint-type batching closes actual terminal blocker return

PX341--PX355 replace every actual trajectory terminal core by a valid one- or
two-core buffer cycle.  Such a cycle destroys at least one designated old
certificate, has no internal three-inserted-cell collateral, and may create only
external triples using one or two inserted cells.

The earlier blocker forest processes those external triples one at a time.  In
the actual two-layer construction this is unnecessarily expensive.  Every
external blocker contains at least one unchanged selected point, and the
unchanged selected points have only finitely many layer--channel types.  Assign
each blocker to one of its unchanged points and move all assigned points of one
type together.  At most `2q` endpoint blocks suppress the complete original
blocker list of a fixed buffer cycle.

The statement is causal: child rematching may create new obligations, but those
are assigned to deeper levels.  The original terminal blocker coordinate only
decreases and never receives new entries.

## 1. External blockers have a fixed endpoint anchor

Fix one valid buffer cycle `sigma` from PX342 or PX343.  Let `W_sigma` be its
inserted cells and let `B_sigma^ext` be the prospective created triples using
one or two cells of `W_sigma`.

### Theorem PX356 -- PROVED

Every `T in B_sigma^ext` contains at least one selected point outside the
buffer-cycle support.  Moreover, the line of `T` is nonvertical.

Consequently one may choose an **endpoint anchor**

\[
\boxed{p(T)\in T\setminus W_\sigma}
\]

for every external blocker.

### Proof

An external blocker uses either one or two inserted cells.  Since a triple has
three points, it has respectively two or one unchanged selected points.

For two inserted cells, the cells lie in distinct source rows of the cycle, so
their line is not vertical.  For one inserted cell, a vertical blocker would
place that cell and two unchanged selected points in one grid row.  The
two-layer saturated state contains exactly two selected points in each row, so
such a triple cannot occur.  \(\square\)

## 2. Endpoint-type batching

Every selected point has a permutation-layer and hyperbola-channel type.  There
are at most `2q` such types.  For a type `theta`, put

\[
X_\theta
=
\{p(T):T\in B_\sigma^{ext},\ \operatorname{type}(p(T))=\theta\}.
\]

Repeated anchors are retained only once.

### Theorem PX357 -- PROVED

Each nonempty `X_theta` is a row-column matching block: its points occupy
distinct rows and distinct columns.  The sets `X_theta` partition the assigned
external blocker list into at most

\[
\boxed{2q}
\]

batches.

### Proof

All points in `X_theta` lie in one permutation layer.  A permutation layer has
one point in every used row and every used column, hence distinct points have
distinct rows and columns.  Every blocker was assigned one endpoint anchor and
there are at most `2q` possible anchor types.  \(\square\)

## 3. One endpoint block suppresses one complete batch

Fix `theta`.  Rematch the points of `X_theta` inside their row and column sets,
requiring every point to leave its original position.  Reserve all core and
buffer-cycle cells and retain the inherited historical-position constraints.

### Theorem PX358 -- PROVED

Every blocker assigned to `X_theta` is absent after any such compatible
rematching.

### Proof

Let `T` be assigned to `p=p(T) in X_theta`, and let `ell_T` be its line.  By
PX356, `ell_T` is nonvertical.  Therefore `ell_T` meets the fixed row of `p` in
exactly one cell, namely the original position of `p`.  The endpoint rematching
forbids that position, so the moved endpoint cannot remain on `ell_T`.  Hence
`T` is suppressed.

The same argument is ancestor safe: every later return to the blocker would
require returning `p` to its recorded historical cell.  \(\square\)

## 4. Coupled executability is an existing endpoint problem

The endpoint rematching is coupled to the already chosen buffer cycle: cells
occupied by the buffer cycle in the opposite layer are added to the ordinary
forbidden graph.

### Theorem PX359 -- PROVED REDUCTION

For every type batch `X_theta`, the coupled suppression problem is exactly a
bounded-forbidden endpoint-rematching instance of the form already handled by
PX196--PX200, PX263--PX276, and PX341--PX345.

In particular:

1. `X_theta` is a compatible matching block;
2. reserving the fixed buffer cycle adds only a bounded partial matching to the
   forbidden graph;
3. current, opposite-layer, and historical positions remain partial matchings;
4. large batches enter the established large/nested decoder;
5. bounded terminal batches enter the exact terminal optimizer or the
   two-buffer escape.

No new geometric compatibility condition is introduced.

### Proof

Row-column compatibility is PX357.  Every excluded family listed above contains
at most one cell in each source row and target column, so it contributes one
partial matching to the inherited forbidden graph.  PX358 shows that avoiding
the original positions is exactly the condition needed to suppress the assigned
blockers.  The resulting object is therefore the same endpoint matching problem
used throughout the nested neutralization chain.  \(\square\)

## 5. Finite causal return to the terminal cycle

Resolve the nonempty type batches sequentially.  During one child resolution,
keep the terminal core and chosen buffer-cycle cells reserved.  Assign every new
prospective obligation created by the child to a deeper causal level.

### Theorem PX360 -- PROVED REDUCTION

After resolving at most `2q` endpoint-type children, every blocker in the
original list `B_sigma^ext` is permanently absent.  The fixed buffer cycle then
executes with strict decrease at least equal to its surviving designated core
destruction.

More precisely, if the cycle initially destroys `D>=1` designated old
certificates, then either a child transition improves earlier, or after the type
batches are resolved,

\[
\boxed{\Delta_\sigma\Phi\le-D<0.}
\]

### Proof

PX357 gives at most `2q` batches.  PX358 suppresses the complete assigned batch
at each step, and historical-position constraints prevent recurrence.  New
obligations created during child resolution are deeper coordinates and do not
repopulate the original terminal blocker coordinate.

The buffer cycle remains executable because its cells are reserved throughout.
It has no internal three-inserted-cell creation by PX342--PX343.  Once all
original external blockers are absent, its only shallow contribution is the
destruction of the designated core certificates.  Any core certificate already
destroyed by a child is an earlier improvement; otherwise the cycle destroys
the survivors.  \(\square\)

### Corollary PX361 -- PROVED REDUCTION

Under the established recursive child-resolution interface, the actual
trajectory-terminal return sign is closed:

- coordinate rank-one blockers,
- directed-path blockers,
- generic two-buffer rank-one blockers, and
- mixed two-buffer shadows

need not be handled by four separate terminal sign arguments.  They are all
batched by unchanged endpoint type and returned to the same endpoint decoder in
at most `2q` immediate child blocks.

PX351--PX355 remain useful as quantitative diagnostics, but they are no longer
required for terminal sign.

The remaining work is the formal insertion of this bounded-type return into the
global PX63 induction and the finite verification of ambient orders below the
buffer divisor threshold.

## 6. Verification

Run

```bash
python scripts/verify_product_endpoint_type_batch_return.py
```

The verifier exhausts the one- and two-core inserted-cell dependency patterns,
checks that every external pattern has one or two fixed endpoint anchors,
randomly assigns blocker lists to layer--channel types, and confirms that at
most `2q` complete type batches remove the original blocker list.
