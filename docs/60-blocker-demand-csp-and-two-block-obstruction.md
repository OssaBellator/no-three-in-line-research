# Blocker-demand CSP and the two-block finite obstruction

Unary blocker-cover domains are too strong: a source blocker endpoint may be
deleted by another block.  This chapter writes the exact cross-block demand and
identifies when retained-pair clauses have rank three.  It also exhausts the
first nontrivial two-block architecture on the stored larger seeds.

## 1. Exact blocker-demand bad boxes

Fix a matching-layer partition into blocks `E_1,...,E_K`.  A state `a in Omega_i`
selects a patch set `Q_i(a)` and deletes a source set `D_i(a) subseteq E_i`.
For a candidate cell `z` in block `i`, define

\[
 \Sigma_i(z)=\{a\in\Omega_i:z\in Q_i(a)\}.
\]

For a source edge `e in E_j`, define its retention set

\[
 R_j(e)=\{a\in\Omega_j:e\notin D_j(a)\}.
\]

Source points in the other matching layer or outside all chosen blocks are fixed
retained points.

### Proposition PP3cz -- PROVED

Let `z` be a candidate cell of block `i` and let `{p,q}` be a source blocker pair
through `z`.  The exact bad box selecting the retained-pair triple `{p,q,z}` is
obtained by intersecting:

1. `Sigma_i(z)` in the controller block;
2. `R_j(p)` if `p` is a deletable source edge in block `j`;
3. `R_k(q)` if `q` is a deletable source edge in block `k`;
4. no condition for a fixed retained endpoint.

Conditions belonging to the same block variable are intersected.  An empty
intersection makes the triple impossible.  Otherwise the resulting bad box has
rank at most three, and avoiding every such box is equivalent to clearing every
retained-pair blocker.

#### Proof

The triple is present exactly when the controller state selects `z` and neither
source endpoint is deleted.  These are precisely the displayed state-subset
conditions.  At most the controller block and the two endpoint blocks occur. ∎

This is the PP3bi bad-box construction specialized to the matching structure of
external-point blocker pairs.

## 2. Rank-three localization by endpoint blocks

### Corollary PP3da -- PROVED

A retained-pair blocker box has rank three only if its two deletable endpoints
lie outside the controller block and lie in two distinct endpoint blocks.

Consequently:

1. if every blocker pair of every supported cell has a deletable endpoint in the
   controller block, all `N_1` boxes have rank at most two;
2. if every deletable endpoint of those blocker pairs lies in the controller
   block, all `N_1` boxes are unary and can be removed by local state pruning;
3. if the endpoint blocks of each controller block lie in one designated partner
   block, the retained-pair CSP is binary on the controller-partner graph.

#### Proof

Conditions from one block variable are intersected before rank is counted.  A
third variable is needed exactly when the controller and the two retained
endpoint conditions belong to three distinct blocks. ∎

This gives a concrete correlated-partition target: cluster blocker endpoints
with their controller blocks or with a bounded-degree partner graph.

## 3. Exact two-block search

Take two disjoint four-edge blocks from one matching layer and reserve two
width-two intervals.  Since each block has size four, its state deletes all four
of its source edges and chooses one of the 36 degree geometries.

For a fixed pair of blocks, first delete all eight source edges.  A patch domain
for block `i` is **source-clean** if its eight patch points create no triple with
the resulting retained source, before the other patch is added.  This is a
necessary condition for any complete two-block extension.

### Proposition PP3db -- PROVED BY EXHAUSTIVE FINITE CHECK

For every stored source side `n=8,9,10`, for both matching layers, and for every
choice of two disjoint four-edge blocks, at least one of the two source-clean
patch domains is empty.  Therefore no choice of the two 36-state geometries gives
a raw saturated no-three extension from `n` to `n+4`.

The exact numbers of unordered block partitions checked per layer are:

| Source side | Partitions |
|---:|---:|
| 8 | 35 |
| 9 | 315 |
| 10 | 1575 |

For every partition the program enumerates both 36-state patch domains.  If both
were nonempty it would test every surviving state pair and independently verify
the final `2(n+4)`-point configuration by integer determinants.  No partition
reaches that second stage.

The search is implemented in

```bash
python scripts/search_two_block_width_two_extensions.py \
  certificates/prime-patching-small.json
```

## 4. Interpretation

Cross-block deletion is strictly stronger than unary blocker covering, but the
first two-block test still fails before patch-patch interactions are considered.
The retained source already empties one block domain in every partition.

This finite result does not refute asymptotic block preparation.  It shows that a
successful block partition must be chosen from a source with much stronger
blocker-endpoint clustering than the stored certificates, or must include
protected trades that alter the retained source before the width-two domains are
formed.

The exact remaining retained-pair target is now:

1. partition a matching layer so most blocker pairs meet their controller or a
   bounded-degree partner block;
2. preserve polynomially many source-clean local states;
3. solve the resulting unary/binary demand system before paying anchored-pair and
   all-patch cross-block clauses.