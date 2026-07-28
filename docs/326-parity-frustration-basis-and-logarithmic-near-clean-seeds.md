# Parity frustration bases and logarithmic near-clean seeds

`docs/322` removes owner pairs that forbid both relative orientation parities, and
`docs/323` supplies a pair-safe Hamilton cycle with only `O(log m)` one-XOR
constraints.  The remaining obstruction is signed-cycle frustration.  This
chapter compresses that obstruction to a minimum edge-deletion core and obtains
an `O(log m)` near-clean signed state.

No clean asymptotic seed or no-three-in-line theorem is claimed.

## 1. Signed parity graph and frustration index

For a pair-safe Hamilton cycle `rho`, let `G_rho=(V,E,sigma)` be its signed parity
graph.  An edge `uv` with label `sigma(uv)` requires

```text
e_u xor e_v = sigma(uv).
```

Write

```text
q=|E|,
c=number of connected components of the underlying graph,
beta=q-|V|+c.
```

Thus `beta` is the cyclomatic rank, including isolated vertices in `c`.
Define the frustration index

```text
lambda(G_rho)
 = min_e |{uv in E : e_u xor e_v != sigma(uv)}|.
```

### Proposition PP3bnd -- PROVED / FUNDAMENTAL-CYCLE LOCALIZATION

Fix any spanning forest `F` of the underlying graph.  There is an orientation
vector satisfying every edge of `F`.  For this vector, a chord `f in E\F` is
violated exactly when the signed parity around its fundamental cycle is odd.
Consequently all parity inconsistency is supported on the set of inconsistent
fundamental chords.

#### Proof

Choose one root bit in each tree component and propagate across every tree edge
using its required XOR label.  A forest has no cycle, so this produces a
well-defined orientation satisfying every edge of `F`.

For a chord `f=uv`, the forest path from `u` to `v` fixes `e_u xor e_v` as the
XOR sum of the path labels.  Hence `f` is satisfied exactly when its own label
agrees with that path sum, equivalently when the XOR sum around the fundamental
cycle is zero.  There are no other possible violations because all forest edges
were satisfied. ∎

This replaces an arbitrary family of frustrated cycles by one explicit set of
chords relative to a forest basis.

## 2. Cyclomatic-rank bound and exact deletion interpretation

### Theorem PP3bne -- PROVED / FRUSTRATION CORE BOUND

For every signed parity graph,

```text
lambda(G_rho) <= beta.
```

Moreover `lambda(G_rho)` is exactly the minimum number of parity edges whose
deletion makes the signed graph satisfiable.

#### Proof

A spanning forest has `|V|-c` edges, so it has exactly

```text
q-(|V|-c)=beta
```

chords.  The forest orientation from PP3bnd violates only inconsistent chords,
which proves `lambda<=beta`.

For the exact deletion statement, any orientation becomes a satisfying
orientation after deleting its violated edges.  Thus the minimum deletion
number is at most `lambda`.  Conversely, if deleting a set `D` makes the graph
satisfiable, choose an orientation satisfying every edge outside `D`.  It
violates at most `|D|` original edges, so `lambda<=|D|`.  Minimize over `D`. ∎

The theorem is a structural reduction, not a repair operation on the Hamilton
cycle.  It identifies the smallest owner-pair constraint set that must be
changed or bypassed.

## 3. Logarithmic near-clean asymptotic seed

Call an orientation **`L`-near-clean** when at most `L` one-XOR owner pairs use
their forbidden relative parity.

### Corollary PP3bnf -- PROVED / LOGARITHMIC NEAR-CLEAN SEED

For every sufficiently large `m`, there is a pair-safe Hamilton cycle and an
orientation vector that is `O(log m)`-near-clean.

#### Proof

PP3bmu supplies a pair-safe Hamilton cycle with

```text
q=O(log m)
```

parity edges.  Since `beta<=q`, PP3bne gives an orientation violating at most
`O(log m)` parity edges. ∎

Thus the reduced parity frontier is no longer the construction of a sparse
instance: one may start from a state with only logarithmically many bad
owner-pair constraints.  A violated owner-pair constraint can still represent
more than one atomic collinear triple, so this is not yet an atomic flaw bound.

## 4. Exact frustration audit through `m=9`

### Theorem PP3bng -- VERIFIED FINITELY / EXACT MINIMUM VIOLATIONS

Every pair-safe Hamilton cycle was reconstructed for `4<=m<=9`, and the
frustration index was minimized over all `2^m` orientation vectors.  The exact
distributions are:

| `m` | pair-safe cycles | `lambda=0` | `lambda=1` | `lambda=2` | `lambda=3` | maximum `beta` |
|---:|---:|---:|---:|---:|---:|---:|
| 4 | 6 | 6 | 0 | 0 | 0 | 0 |
| 5 | 24 | 22 | 2 | 0 | 0 | 1 |
| 6 | 120 | 112 | 8 | 0 | 0 | 1 |
| 7 | 720 | 664 | 56 | 0 | 0 | 2 |
| 8 | 4,560 | 3,542 | 940 | 78 | 0 | 4 |
| 9 | 37,440 | 31,688 | 5,478 | 272 | 2 | 4 |

In particular, every pair-safe cycle through `m=9` has an orientation violating
at most three parity edges.  The bound `lambda<=beta` holds for every audited
cycle.

#### Verification

Compile and run

```bash
g++ -O3 -std=c++17 \
  scripts/check_hamilton_parity_frustration_index.cpp \
  -o /tmp/check_hamilton_parity_frustration_index
/tmp/check_hamilton_parity_frustration_index
```

The checker reconstructs the exact geometric pair predicates, discards cycles
with a locally impossible owner pair, computes connected components and
cyclomatic rank, exhausts every orientation vector, and compares all
constraint, rank, and frustration distributions with hard-coded regression
values.  Its JSON output is stored in
`experiments/hamilton-parity-frustration-index-audit.json`. ∎

The two `m=9` cycles at frustration index three show that one- or two-edge
repair is not a universal finite statement even before asymptotic issues.

## 5. Revised signed-cycle frontier

### Corollary PP3bnh -- PROVED / FRONTIER SHARPENED

For a pair-safe sparse Hamilton cycle, signed-cycle inconsistency is equivalent
to a minimum parity-edge deletion core of size at most `O(log m)`.  The next
steps may therefore work with a logarithmic marked owner-pair set rather than an
unstructured family of frustrated cycles:

1. find clean successor rotations that hit or replace one marked violated edge
   without creating a larger marked core;
2. prove bounded or logarithmic descent of the frustration index under a
   parity-aware rotation kernel;
3. combine the marked core with the trajectory-local causal window of
   `docs/317`;
4. compare frustration-index descent with the weighted Hall transport of
   `docs/324`;
5. determine whether a biased pair-safe Hamilton measure makes `beta` bounded
   or makes `lambda=0` with positive probability.

The logarithmic near-clean state does not prove that these repairs preserve
pair safety, Hamilton mobility, or the three-owner charge scale.