# Closure envelopes and persistent parent ancestry

Arbitrary alternating endpoint trades may mix rows between finer child blocks,
so the complete recursive fibre partition is not preserved at every depth.
Nevertheless each closure branch retains one canonical safe ancestor: the least
prefix block containing every column moved on that branch. Its two layer row
sets are invariant under all subsequent trades inside the envelope.

This supplies the inherited parent block required by the joint-escape programme
and gives a monotone scale coordinate.

## 1. Prefix envelopes

Columns are written in lower-first base-`p` digits. A depth-`s` column-prefix
block is

\[
C_{s,a}=\{x:x\equiv a\pmod{p^s}\}.
\]

For a nonempty set of columns `Y`, let `Env(Y)` be the smallest prefix block
containing `Y`. Equivalently, its depth is the length of the common lower-digit
prefix of all columns in `Y`. The root block has depth zero.

For a sequence of repair moves, let `Y_j` be the union of every column moved up
to time `j`, and put

\[
E_j=\operatorname{Env}(Y_j).
\]

## 2. Envelope row-set invariance

### Theorem CMR172 — PROVED

Fix one permutation layer. Suppose every repair move rematches selected columns
to the rows currently occupied by the selected points, as in the endpoint,
prefix, node, and joint banks of this notebook.

For every time `j`, the set of rows occupied by that layer over the envelope
`E_j` is exactly the row set which the initial state occupied over `E_j`.

The statement holds simultaneously for both layers, including ordered
one-layer-at-a-time joint repairs.

### Proof

Consider one move and any prefix block `E` containing all its moved columns.
Every selected row comes from a point whose column lies in `E`, hence from the
current layer row set over `E`. The move merely permutes those selected rows
among selected columns of `E`. Unselected columns of `E` are unchanged.
Therefore the complete row set over `E` is unchanged.

Every earlier move also has its columns inside the later envelope `E_j`, by the
definition of the union `Y_j`. Applying the preceding observation inductively
shows that no move up to time `j` changes the row set over `E_j`. The two layer
arguments are independent. ∎

The theorem does not assert that row sets of strict descendants remain
unchanged. Only the canonical envelope and its ancestors are protected.

## 3. Persistent disjointness and inherited parent banks

### Theorem CMR173 — PROVED

Start from either balanced recursive construction of CMR162. At every time in
an alternating closure branch:

1. if the current envelope `E_j` is nonroot, its two layer row sets are disjoint;
2. the disjoint-fibre joint bank CMR164 is executable over `E_j`;
3. if `E_j` is the root and its size is at least thirteen, the general
   old-cell-clean ordered bank CMR155 is executable;
4. at root size five or seven, the exact base parent escapes CMR147 and CMR151
   remain the finite reference models.

Every terminal four-core target produced on the branch touches the current
envelope, so every state of the appropriate envelope joint bank destroys that
target whenever its old-cell-clean hypothesis is used.

### Proof

For a nonroot envelope, CMR162 says the initial two layer row sets are disjoint.
CMR172 says both current row sets equal those initial sets, so they remain
disjoint and CMR164 applies.

At the root, both row sets are the complete grid row set; CMR155 applies at size
at least thirteen. The finite base statements are the cited exact theorems.

Every moved endpoint column belongs to `Y_j` and hence to `E_j`. A target triple
selected during the closure has at least one designated moved endpoint in that
set. An old-cell-clean envelope state removes its old cell. ∎

The last sentence tracks the designated target endpoint, not merely the
unlabeled triple.

## 4. Monotone envelope depth

### Theorem CMR174 — PROVED

The envelope depths form a nonincreasing integer sequence

\[
0\le d(E_{j+1})\le d(E_j)\le k.
\]

Whenever a new move uses a column outside the current envelope, the depth
strictly decreases. Hence a closure branch can expand to a strictly larger
prefix ancestor at most `k` times.

### Proof

Adding columns to `Y_j` can only shorten their common lower-digit prefix. If the
new column lies outside `E_j`, it disagrees with the common prefix at some digit
before depth `d(E_j)`, giving a strict decrease. There are only `k+1` possible
depths. ∎

This is a genuine reverse-scale coordinate. A branch may perform many local
trades inside one envelope, but it cannot alternate indefinitely between finer
and coarser inherited parents.

## 5. Envelope-compatible packing

### Corollary CMR175 — PROVED

Every alternating closure branch admits a canonical parent assignment:
associate all terminal cores created before the next strict envelope expansion
to the current envelope block.

These assigned parent blocks form a nested chain of length at most `k+1`.
Within each nonroot member of the chain, the constants and scale charges of
CMR165--CMR170 remain valid because its row sets are unchanged. At the root use
CMR156 or the exact finite base model.

### Proof

CMR174 gives the nested chain. CMR172--CMR173 give the invariant row sets and
available bank at each member. CMR169 controls the multiplicity of triple
charges at its scale. ∎

## 6. Revised remaining theorem

The terminal core does retain usable ancestry despite arbitrary finer trades:

- one canonical envelope block;
- invariant layer row sets over that block;
- an executable joint parent bank;
- a depth coordinate with at most `k` strict coarsenings;
- an exact one-to-three charge ledger at every envelope scale.

The remaining gap is now local within one fixed envelope epoch. One must prove
that before the envelope expands again, either

1. one joint parent state improves the fixed baseline; or
2. the terminal targets accumulated in the envelope exceed its expected
   collateral; or
3. a carry or quotient signature forces a strict envelope expansion.

No all-`n` theorem is claimed here. The prefix-envelope identities and depth
monotonicity are checked in
[`scripts/verify_prime_power_closure_envelope.py`](../scripts/verify_prime_power_closure_envelope.py).
