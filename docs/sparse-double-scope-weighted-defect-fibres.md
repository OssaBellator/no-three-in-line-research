# Weighted fibre repair for double-scope reflected-label defects

**Branch:** `research/sparse-algebraic-spread`

SAS5ao--SAS5as select one designated mirror record per defect column.  In a
double-scope word that loses unnecessary weight: once the fixed swapped columns
`x,y` and the unique non-swapped defect column `z` are known, every mirror record
in that column fibre has the same three scope columns `{x,y,z}`.

A donor outside those three columns fixes the whole fibre after the original
swap is applied.  This note gives a weighted matching and global compatibility
extraction for the combined move consisting of the fixed original swap and a
donor subbank.

## Double-scope defect fibres

Fix one physical swap `omega={x,y}`, one double-scope destruction word, its
mirror repair word and its unique reflected-label defect role.  Fix the required
defect label `ell`.

Let `Z` be the set of distinct defect columns.  For `z in Z`, let `F_z` be the
multiset of reflected mirror records whose unique non-swapped column is `z`, and
let

`L(z)=sum_(Q in F_z) w(Q)`.

Write

`W_ell=sum_(z in Z)L(z)`.

Every record in `F_z` has column scope exactly `{x,y,z}`.  The records may have
different row triples, but the column scope and required labels are fixed by the
word and defect role.  After applying `omega`, the labels at `x,y` are correct
for every mirror record; only the label at `z` is wrong.

Let

`D_ell={q:kappa(q)=ell}`

be the donor columns, with `|D_ell|=d`.  Since `z` currently has the wrong label,
`z notin D_ell`.

## SAS5at -- one safe donor repairs an entire double-scope fibre after the original swap -- PROVED WITH ORIGINAL-SWAP COMPOSITION

If

`q in D_ell\{x,y}`,

then the combined move `omega union {z,q}` repairs every record in `F_z`
simultaneously.  Equivalently, applying `{z,q}` to the post-`omega` coloring
repairs the whole fibre.  The designated repaired weight is at least `L(z)`.

### Proof

The original swap puts the required opposite labels at `x,y`.  Every record in
`F_z` uses the same columns `{x,y,z}`.  The donor `q` is outside that scope: it
is not `x` or `y`, and it is not `z` because `z` has the wrong label while `q`
has label `ell`.  The donor transposition puts `ell` at `z` without changing
`x,y`.  Thus every record in the fibre is satisfied after the combined move.
QED.

A donor transposition alone need not repair the fibre because it does not swap
`x,y`.  This statement is special to the composed move.

## SAS5au -- any `d-2` defect columns have distinct safe donors -- PROVED

Every defect column has at least `d-2` safe donors.  Moreover, every subset
`Z_0 subseteq Z` with

`|Z_0|<=d-2`

admits an injective assignment `z->q_z` of safe donors.  The resulting donor
transpositions `{z,q_z}` are pairwise endpoint-disjoint and disjoint from
`omega`.

### Proof

A defect column excludes from `D_ell` only the two original swap columns `x,y`.
Hence each left vertex in the defect--donor bipartite graph has at least `d-2`
neighbours.  For any `S subseteq Z_0`, its union of neighbours has size at least
`d-2>=|Z_0|>=|S|`.  Hall's condition holds, so `Z_0` has a matching into the
donors.  Defect columns lie outside `D_ell`, and all chosen donors avoid `x,y`,
so all endpoints are distinct. QED.

## SAS5av -- weighted top-fibre composed donor bank -- PROVED

Let `k=|Z|` and

`m=min(k,(d-2)_+)`.

Choose the `m` defect columns of largest fibre load.  They admit an
endpoint-disjoint donor bank `B` satisfying

`sum_(z in B)L(z) >= (m/k)*W_ell`.

If the board has at most `N` columns, then also

`sum_(z in B)L(z) >= (m/N)*W_ell`.

Applying `omega` once together with every donor transposition in `B` repairs all
selected fibres simultaneously.

### Proof

The sum of the `m` largest among `k` nonnegative numbers is at least `m/k` of
the total.  SAS5au matches those columns to distinct safe donors.  SAS5at says
the original swap composed with each donor repairs its whole fibre.  Endpoint
disjointness and avoidance of `x,y` imply that no other donor changes a column
in `{x,y,z}` for a selected fibre `z`; hence all selected fibres survive the
combined move.  Finally `k<=N` gives the second bound. QED.

No global constraint-incidence hypothesis is needed for survival of the
selected mirror fibres.  Such a hypothesis is needed only to make donor energy
changes additive relative to the post-`omega` coloring.

## SAS5aw -- compatible weighted fibre bank under global incidence -- PROVED

Assume every column lies in at most `Lambda` complete geometric constraint
records.  Then the donor bank from SAS5av has an independent subbank `I` in the
global donor interaction graph satisfying

`sum_(z in I)L(z) >= [1/(4*Lambda+1)]*sum_(z in B)L(z)`.

Thus

`sum_(z in I)L(z) >= W_ell*m/[k*(4*Lambda+1)]`

and, using `k<=N`,

`sum_(z in I)L(z) >= W_ell*m/[N*(4*Lambda+1)]`.

Applying `omega` and the donor subbank repairs every reflected record in every
selected fibre.  The donor energy increments are exactly additive relative to
the post-`omega` coloring.

### Proof

SAS5aj gives maximum donor-interaction degree at most `4*Lambda`, so the graph
has a proper colouring with at most `4*Lambda+1` colours.  Give a donor
transposition weight `L(z)`.  One colour class carries at least the average
total fibre weight.  It is independent.  Apply SAS5ak using `kappa^omega` as the
baseline for energy additivity, and apply SAS5at to every selected fibre. QED.

## SAS5ax -- weighted double-scope composed-move router -- PROVED

Suppose the original double-scope reflected-label defect family has total
weight `W` and there are `b` labels.  After retaining one required-label class,
`W_ell>=W/b`.

Let `k` be the number of defect columns in that class and

`m=min(k,(d-2)_+)`.

Then:

1. the original swap composed with an endpoint-disjoint donor bank repairs
   reflected records of total weight at least

   `W*m/(b*k)`;

2. under global column incidence `Lambda`, a compatible composed subbatch
   repairs reflected records of total weight at least

   `W*m/[b*k*(4*Lambda+1)]`,

   and donor energy increments are additive relative to the post-original-swap
   coloring;

3. using only the board bound `k<=N`, the corresponding uniform lower bounds are

   `W*m/(b*N)` and `W*m/[b*N*(4*Lambda+1)]`.

### Proof

SAS5ae gives `W_ell>=W/b`.  Apply SAS5av and SAS5aw and substitute this lower
bound. QED.

The combined move either lowers the original energy or realizes the displayed
weighted mirror-repair bank without lowering it.  A swap-local minimum does not
choose between these branches because the move uses several transpositions.

## Corrected SAS6 frontier

For double-scope reflected-label defects:

- the original swap plus donor matching repairs whole weighted column fibres;
- the top `min(k,d-2)` fibres retain an `m/k` fraction of the defect weight;
- global donor compatibility costs only `4*Lambda+1`;
- energy additivity is exact relative to the post-original-swap coloring.

The remaining weighted issue is the singleton word, where the second
non-swapped column varies inside a defect-column fibre.  Arithmetic
classification, high-incidence hosts and reflected-board boundary profiles also
remain.

## Finite check

`scripts/verify_sparse_double_scope_weighted_fibres.py` exhausts small weighted
defect fibres, donor sets and interaction graphs.  It checks the combined
original-plus-donor repair, Hall matching for every subset of at most `d-2`
defects, top-fibre weight retention, simultaneous survival and weighted
post-swap compatibility extraction.
