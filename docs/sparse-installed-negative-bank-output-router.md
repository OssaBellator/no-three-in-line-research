# Output routing from a low-cost installed negative bank

**Branch:** `research/sparse-algebraic-spread`

SAS5gb--SAS5gf physically install a large bank of negative mixed-curvature records by choosing one
creator orientation in every independent square.  In the low creator-density branch, the installation
cost is small relative to the installed exact-record weight.  This note applies the complete two-swap
energy identity to the whole installed bank.

The result is a lossless aggregate trichotomy: a large opposite-swap barrier, a large bank of
already-current records destroyed by both swaps, or a large composed-only final-output bank.  No exact
signature pigeonhole is used.

## Low-cost installed-bank model

Fix an interaction-independent square family `J`.  For every square `a` let:

- `gamma_a` be the selected creator swap;
- `bar_gamma_a` be the opposite constituent swap;
- `R_a^->0` be the installed selected negative-record weight;
- `C_a^->=R_a^-` be the complete negative mixed-curvature weight;
- `Delta_gamma(a)>=0` and `Delta_bar(a)>=0` be the two base single-swap energy increments;
- `P_cur(a)>=0` be positive mixed-curvature weight with table `(1,0,0,0)`;
- `P_comp(a)>=0` be positive mixed-curvature weight with table `(0,0,0,1)`;
- `Delta_a>=0` be the composed-square increment.

The exact conjunction-table classification gives

`Delta_a=Delta_gamma(a)+Delta_bar(a)+P_cur(a)+P_comp(a)-C_a^-`.

Put

`R=sum_a R_a^-`,

`G=sum_a Delta_gamma(a)`,

`B_opp=sum_a Delta_bar(a)`,

`P_cur=sum_a P_cur(a)`,

`P_comp=sum_a P_comp(a)`.

Assume the creator bank is the low-cost branch of SAS5ge:

`G<=kappa_0 R`

for one `kappa_0 in (0,1)`.

All record aliases are aggregated and interaction independence assigns every exact mixed-curvature
record to one square.

## SAS5gg -- exact positive-table partition -- PROVED

For conjunction records under two disjoint swaps, every positive mixed-curvature record has exactly one
of the tables

`(1,0,0,0)`

or

`(0,0,0,1)`.

Therefore the complete positive mixed-curvature bank is the alias-disjoint union of the current-only
bank `P_cur` and the composed-only bank `P_comp`.

### Proof

The product factorization of SAS5bs writes the mixed difference as the product of two one-variable
differences.  Positive curvature requires equal nonzero signs.  Two decreasing factors give the
current-only table; two increasing factors give the composed-only table.  Alias aggregation and unique
square assignment give the disjoint aggregate partition. QED.

A current-only record is physically present in the base colouring and absent after either single swap
or the composed move.  A composed-only record is absent in the base and both single-swap states and
present only after the composed move.

## SAS5gh -- aggregate installed-bank energy inequality -- PROVED

At square-local minimum,

`G+B_opp+P_cur+P_comp>=R`.

Consequently, in the low creator-cost branch,

`B_opp+P_cur+P_comp>=(1-kappa_0)R`.

### Proof

For each square, `Delta_a>=0` and the exact energy identity give

`Delta_gamma(a)+Delta_bar(a)+P_cur(a)+P_comp(a)>=C_a^->=R_a^-`.

Sum over the independent bank.  Subtract `G<=kappa_0R` to obtain the second inequality. QED.

## SAS5gi -- opposite-barrier/current-payment/composed-output trichotomy -- PROVED

At least one of the following holds:

1. **opposite base barrier**

   `B_opp>=(1-kappa_0)R/3`;

2. **current-only payment bank**

   `P_cur>=(1-kappa_0)R/3`;

3. **composed-only output bank**

   `P_comp>=(1-kappa_0)R/3`.

Every current-only record in alternative 2 is an exact current factor destroyed by both constituent
single swaps.  Every composed-only record in alternative 3 enters the existing final-output curvature
and aggregate payment-scale routers with no address loss.

### Proof

The three nonnegative quantities sum to at least `(1-kappa_0)R` by SAS5gh.  One is at least one third
of the sum.  The physical interpretations are the two exact tables in SAS5gg. QED.

## SAS5gj -- integrated matched-bank constants -- PROVED

Suppose SAS5gf installs a low-cost negative bank from an original matched bank of weight `M`, so

`R>(1-theta)lambda M/[16(D_sq+1)]`

for `lambda>0`, `theta in (0,1)` and `kappa_0 in (0,1)`.  Then one has:

1. aggregate opposite base barrier greater than

   `(1-kappa_0)(1-theta)lambda M/[48(D_sq+1)]`;

2. exact current-only payment weight greater than the same quantity;

3. exact composed-only final-output weight greater than the same quantity;

4. or one two-swap table, base-admissibility, interaction-independence, complete-ledger, creator,
   opposite-destroyer, record, alias or boundary field fails.

### Proof

Apply SAS5gi and substitute the strict lower bound for `R`.  Failed hypotheses are retained as
alternative 4. QED.

## SAS5gk -- installed-negative-bank output router -- PROVED UNDER THE DECLARED CONTRACTS

A low-cost physically installed negative bank cannot disappear into an unstructured energy term.  Its
full scale produces one of:

1. a quantified opposite-swap barrier;
2. a quantitatively comparable exact current payment bank;
3. a quantitatively comparable composed-only output bank returning to SAS5fw--SAS5ga;
4. direct descent from an improving constituent or composed move;
5. or a named legality, ledger, incidence, record or boundary failure.

### Proof

Use SAS5gj at square-local and swap-local minimum.  Any excluded improving move is the direct descent
alternative.  The remaining failures are exactly the declared contracts. QED.

## Corrected SAS6 frontier

The low-cost installed negative-record branch now has a lossless aggregate output router.  It yields a
large current payment bank, a large composed-only bank already covered by the final-output machinery, or
a comparably large opposite single-swap barrier.

The remaining sparse work is globally paying the opposite-barrier alternative, preventing repeated
composed-only recycling, proving creator/opposite-destroyer legality in every arithmetic word family,
batching neutral outputs under failed incidence caps, and resolving positive-base-row, boundary and
high-incidence profiles.

## Finite check

`scripts/verify_sparse_installed_negative_bank_output_router.py` enumerates the exact positive and
negative conjunction tables and samples weighted independent square banks.  It checks the complete
energy identity, the low-creator-cost aggregate inequality, the three-way one-third split and the
integrated matched-bank constants.
