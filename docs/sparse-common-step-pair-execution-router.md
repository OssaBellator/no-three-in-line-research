# Compatibility and energy routing for weighted common-step parameter pairs

**Branch:** `research/sparse-algebraic-spread`

SAS5dw--SAS5eb extract weighted disjoint adjacent-parameter pairs from every localized primitive
line, singleton dilation or positive fixed-third-column chain.  Disjoint parameter endpoints prevent
reuse of one parameter fibre, but they do not automatically prevent two pair operations from
touching one geometric constraint.

This note separates the exact movable-coordinate reuse from the remaining operational contract.  A
bounded column-incidence hypothesis then yields a large constraint-independent pair subbank with
exact additive energy.  At a local minimum that subbank returns distinct repaired collateral rather
than another diffuse interaction term.

## Adjacent-pair notation

Let `P` be one path matching of adjacent parameter edges `(s,s+1)` supplied by SAS5dx.  Give edge
`e` bottleneck weight

`b_e=min{w_s,w_(s+1)}`

and put

`B_pair=sum_(e in P) b_e`.

The parameter edges are endpoint-disjoint, so every parameter fibre is used by at most one pair.

There are three geometric models.

1. **Double-scope line.**  The varying third cell is

   `(r(s),c(s))=(r_0,c_0)+s(A_0,D_0)`.

2. **Singleton dilation.**  The two varying columns are

   `c_j(s)=x+A_0*s`,
   `c_k(s)=x+B_0*s`.

3. **Positive fixed-third-column base-row chain.**  The three rows are

   `(r_1(s),r_2(s),r_3(s))=(u_1+s,u_2+s,u_3+s)`.

Common fixed swapped columns are treated once as common support and are not counted as movable
coordinates of every pair.

## SAS5ec -- exact paired-mass ledger -- PROVED

The selected adjacent edges admit two occurrence-faithful endpoint ledgers, each of total weight
`B_pair`, one on the lower parameters and one on the upper parameters.

No exact parameter fibre contributes weight to two selected edges.

### Proof

For edge `(s,s+1)`, take a subweight `b_e` from each endpoint fibre.  Since the path edges have
pairwise disjoint endpoints, the chosen subweights for different edges lie in disjoint parameter
fibres.  Summing the lower and upper allocations gives `B_pair` on each side. QED.

Thus an adjacent-pair batch is an exact weighted transport bank, not merely a count of occupied
edges.

## SAS5ed -- movable-coordinate reuse bounds -- PROVED

Across one endpoint-disjoint adjacent-pair batch:

1. in a double-scope primitive line, one physical varying row or varying column occurs in the movable
   support of at most one pair;
2. in a singleton dilation, one physical varying column occurs in the movable support of at most two
   pairs;
3. in a positive base-row chain, one physical row occurs in the movable support of at most three
   pairs.

### Proof

For the double-scope model, both maps

`s -> r_0+A_0*s`,
`s -> c_0+D_0*s`

are injective because `A_0,D_0` are nonzero.  A parameter belongs to one selected edge, so each
varying row or column belongs to one pair.

For the singleton model, each arm `x+A_0*s` and `x+B_0*s` is injective.  A physical column can occur
once on each arm, hence in at most two parameter fibres and therefore at most two selected pairs.

For the base-row model, each of the three maps `s -> u_i+s` is injective.  A physical row can occur
once in each row position, hence in at most three parameter fibres and selected pairs. QED.

Cross-arm or cross-position coincidences are allowed; the constants two and three account for them.

## Local pair-operation contract

For the line and dilation models, suppose every adjacent parameter pair `e` has a declared balanced
local operation `sigma_e` with movable column support `S_e`, after one common fixed swap or common
base operation has been applied once.

Assume:

1. `|S_e|<=r`;
2. every physical movable column lies in at most `mu` pair supports;
3. every exact rank-three geometric record scope contains three columns;
4. every physical column occurs in at most `Lambda` record scopes;
5. two pair operations are declared incompatible whenever some record scope meets both movable
   supports;
6. a record meeting only the common fixed support is charged to the common base operation, not to
   every pair separately.

For double-scope pairs one may take

`r=2`, `mu=1`.

For singleton pairs one may take

`r=4`, `mu=2`.

Failure to realize an adjacent arithmetic pair by such an operation returns its exact word,
primitive address and parameter edge.

## SAS5ee -- pair interaction degree -- PROVED

The pair-operation interaction graph has maximum degree at most

`D_pair=r*Lambda*(3*mu-1)`.

In particular:

- double-scope: `D_pair<=4*Lambda`;
- singleton: `D_pair<=20*Lambda`.

### Proof

Fix pair `e`.  Its support contains at most `r` columns, each lying in at most `Lambda` record scopes.
Choose canonically one column of `S_e` in every incident record.  One rank-three scope has three
columns, and each column belongs to at most `mu` pair supports.  Thus the scope meets at most
`3mu-1` other pair supports besides `e`.

Multiplying the safe incident-record count `rLambda` by `3mu-1` gives the displayed degree bound.
Repeated counting of one neighbour only weakens the estimate.  Substitution gives

`2*Lambda*(3*1-1)=4Lambda`

and

`4*Lambda*(3*2-1)=20Lambda`. QED.

## SAS5ef -- weighted compatible pair extraction -- PROVED

The interaction graph has a constraint-independent pair subbank `I` satisfying

`sum_(e in I) b_e>=B_pair/(D_pair+1)`.

Hence the retained bottleneck mass is at least:

- `B_pair/(4Lambda+1)` in the double-scope case;
- `B_pair/(20Lambda+1)` in the singleton case.

### Proof

Greedy colouring uses at most `D_pair+1` colours.  Each colour class is independent, and the colour
weights sum to `B_pair`.  A heaviest class gives the bound. QED.

Every record scope meets the movable support of at most one selected operation.

## SAS5eg -- exact common-base energy additivity -- PROVED

Let `kappa_0` be the colouring after applying the common fixed swap or common base operation once.
For pair operation `e`, write

`Delta_e=T(kappa_0^(sigma_e))-T(kappa_0)=R_e-D_e`.

If `I` is independent in the pair interaction graph, then simultaneous execution satisfies

`T(kappa_0^I)-T(kappa_0)=sum_(e in I) Delta_e`.

The exact repaired and destroyed record sets are disjoint across the selected pair operations.

### Proof

A record scope meeting no selected movable support is unchanged.  By independence, every other
record meets exactly one selected support and changes exactly as under that operation alone.
Therefore indicator changes add record by record.  The same argument shows that no repaired or
destroyed exact record belongs to two selected operations. QED.

This is the same exact additivity principle as SAS5ak, with the common fixed operation separated
before the local pair bank is evaluated.

## SAS5eh -- common-step execution/collateral router -- PROVED UNDER THE PAIR-REALIZATION CONTRACT

Assume each realized pair operation destroys designated endpoint-record mass at least `b_e`.

For a line or dilation pair bank, at least one of the following holds:

1. one exact adjacent arithmetic pair fails the local pair-operation contract;
2. an independent subbank has total positive gain at least

   `G_pair/(D_pair+1)`,

   where `G_pair=sum_e (D_e-R_e)_+`, and therefore gives an executable energy descent of that size;
3. the bank is pair-local-minimal, and an independent subbank has bottleneck mass at least

   `B_pair/(D_pair+1)`

   together with a **distinct exact repaired-record union** of at least the same weight;
4. the column-incidence cap `Lambda` fails, yielding one high-incidence physical column.

For a positive base-row chain, SAS5ec and SAS5ed still give a no-reuse paired-record bank of mass
`B_pair` and row reuse at most three.  Realizing those pairs as balanced operations remains a
separate row-translation contract; failure returns the exact base-row pair address.

### Proof

For alternative 2, colour the interaction graph using positive gains as vertex weights.  SAS5ee and
the heaviest colour class retain at least `G_pair/(D_pair+1)`, and SAS5eg makes the gain additive.

If every pair is nonimproving, use bottleneck weights instead.  SAS5ef retains at least
`B_pair/(D_pair+1)`.  For every selected pair,

`R_e>=D_e>=b_e`.

SAS5eg makes the repaired exact-record sets disjoint, so their union weight is the sum of the
`R_e` values and is at least the retained bottleneck mass.  The other alternatives are the explicit
failures of the hypotheses used in SAS5ee--SAS5eg. QED.

## Corrected SAS6 frontier

The weighted common-step branch now reaches an exact global router:

- a realized constraint-compatible batch with additive energy;
- a quantified improving batch;
- a distinct repaired-record collateral bank of comparable bottleneck mass;
- one high-incidence column;
- or one exact unrealized adjacent-pair address.

The remaining work is to construct the declared local pair operations for every primitive word type,
compare the returned repaired union with the opposite destruction family, realize the positive
base-row translations, and handle reflected-board boundary profiles.  Weighted density and
cross-pair additivity are no longer separate open steps.

## Finite check

`scripts/verify_sparse_common_step_pair_execution.py` exhausts and samples primitive parameter
chains.  It checks endpoint no-reuse, the `1,2,3` movable-coordinate reuse bounds, the
`r Lambda(3mu-1)` interaction degree, weighted `1/(D_pair+1)` extraction and exact indicator-energy
additivity on independent pair banks.
