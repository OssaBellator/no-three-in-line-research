# Aggregate payment scale for matched-square final outputs

**Branch:** `research/sparse-algebraic-spread`

SAS5fm--SAS5fv route a high matched-square barrier to one heavy final record and then classify that
record.  The one-record step loses the final-output stock `K_out`.  This note keeps the complete
interaction-independent high-barrier bank instead.

Every final-positive record has only a composed-only positive table or a neutral persistent repair
table.  Summing the exact mixed-energy identity over the bank then gives a three-way global payment:
neutral repair mass, a quantified positive barrier, or equally quantified negative mixed collateral.
No exact-record pigeonhole or output-stock loss remains.

## High square-bank model

Fix the interaction-independent square bank from SAS5fi--SAS5fj.  Write:

- `H_a>0` for the transient matched weight of square `a`;
- `Delta_a=T(kappa^a)-T(kappa)>=0` for its square-local barrier;
- `H_J=sum_a H_a`;
- `B_J=sum_a Delta_a`.

Fix `lambda>0` and let

`J_high={a:Delta_a>lambda*H_a}`.

Assume the high branch of SAS5fn:

`sum_(a in J_high) H_a>H_J/2`.

Assume also that both constituent swaps of every selected square are individually admissible from the
base colouring.  If one improves, it is used as direct descent.  Otherwise all corresponding
single-swap increments are nonnegative.

Interaction independence means that no complete exact record scope meets two selected square
supports.

## SAS5fw -- exact aggregate final-positive table split -- PROVED

Let `C_fin^+` be the total weight of exact records absent in the base colouring and present after their
unique selected square.  Partition them into:

- `P_comp`: composed-only positive records with table `(0,0,0,1)`;
- `N_neu`: neutral persistent records with table `(0,1,0,1)` or `(0,0,1,1)`.

Then

`C_fin^+=P_comp+N_neu`.

The two banks are alias-disjoint, and every record belongs to a unique selected square.

### Proof

The final-positive conditions are `I_0=0` and `I_(sigma tau)=1`.  SAS5fr leaves exactly the three
displayed tables.  Complete alias aggregation and interaction independence assign each exact record
to one square and one table class.  Summing weights proves the identity. QED.

## SAS5fx -- high barriers force aggregate final-positive mass -- PROVED

In the high branch,

`C_fin^+>lambda*H_J/2`.

Consequently either

`N_neu>=C_fin^+/2>lambda*H_J/4`

or

`P_comp>C_fin^+/2>lambda*H_J/4`.

### Proof

For one square, final energy change is final-positive weight minus final-negative weight, so its
final-positive weight is at least `Delta_a`.  Summing over `J_high` gives

`C_fin^+>=sum_(a in J_high) Delta_a
          >lambda*sum_(a in J_high) H_a
          >lambda*H_J/2`.

The two table classes partition `C_fin^+`; weighted halving gives the conclusion. QED.

## SAS5fy -- exact aggregate mixed-collateral inequality -- PROVED

For square `a`, let:

- `P_a` be its composed-only final-positive weight;
- `U_a^+` be all other positive mixed-curvature weight;
- `C_a^-` be its negative mixed-curvature weight;
- `Delta_sigma(a),Delta_tau(a)` be its two base single-swap increments.

Then

`Delta_a=Delta_sigma(a)+Delta_tau(a)+P_a+U_a^+-C_a^-`.

After excluding direct single-swap descent,

`C_a^->=P_a-Delta_a`.

Therefore, with

`C_J^-=sum_(a in J_high) C_a^-`

and

`P_J=sum_(a in J_high) P_a=P_comp`,

one has

`C_J^->=P_J-B_high`,

where

`B_high=sum_(a in J_high) Delta_a`.

Every exact negative record in `C_J^-` is used once.

### Proof

The displayed equality is the mixed-second-difference identity, separating the composed-only
final-positive contribution from all other positive curvature.  Nonnegative single-swap increments
and `U_a^+>=0` give the local inequality.  Sum over the high bank.  A negative mixed-curvature record
meets both constituent swap supports of its square; interaction independence prevents its scope from
meeting another selected square, so no reuse factor appears. QED.

## SAS5fz -- global neutral/barrier/collateral router -- PROVED

Fix `theta in (0,1)`.  In the high branch, after any direct single-swap descent, one of the following
holds:

1. **neutral repair mass**

   `N_neu>lambda*H_J/4`;

2. **quantified aggregate barrier**

   `B_high>theta*lambda*H_J/4`;

3. **quantified negative mixed collateral**

   `C_J^->(1-theta)*lambda*H_J/4`;

4. or one conjunction-table, base-admissibility, interaction-independence, complete-ledger or boundary
   field fails.

The neutral mass enters the existing one-swap repair ledger with no address loss.  Under the
neutral-operation and incidence contracts, SAS5ex--SAS5fb may then batch it.

### Proof

Use SAS5fx.  If the neutral half is heavy, alternative 1 holds.  Otherwise

`P_J>lambda*H_J/4`.

If `B_high>=theta*P_J`, strict heaviness of `P_J` gives alternative 2.  Otherwise SAS5fy gives

`C_J^->=P_J-B_high>(1-theta)P_J
       >(1-theta)lambda*H_J/4`.

This is alternative 3. QED.

The aggregate theorem removes the `K_out` factor from the high-output route.

## SAS5ga -- integrated matched-bank payment-scale router -- PROVED UNDER THE DECLARED CONTRACTS

Let the original exact matched bank have weight `M`, and let

`D_sq=r*(mu-1)+r*Lambda_sq*(3mu-1)`.

For every `lambda>0` and `theta in (0,1)`, at square-local minimum one has:

1. a low-barrier bank physically creates and destroys matched weight at least

   `M/[2(D_sq+1)]`

   with final energy cost at most `lambda` times that selected matched weight;

2. or neutral persistent repair mass greater than

   `lambda*M/[4(D_sq+1)]`;

3. or aggregate square barrier greater than

   `theta*lambda*M/[4(D_sq+1)]`;

4. or exact negative mixed collateral greater than

   `(1-theta)*lambda*M/[4(D_sq+1)]`;

5. or one constituent single swap gives direct descent;

6. or one realization, joint-legality, base-admissibility, incidence, complete-ledger or boundary field
   fails.

### Proof

SAS5fi gives `H_J>=M/(D_sq+1)`.  In the low branch apply SAS5fn.  In the high branch apply SAS5fz and
substitute the lower bound for `H_J`.  Direct single-swap improvements and failed hypotheses are
retained explicitly. QED.

The same substitution may be made after the neutral-matched and common-step lower bounds, without an
exact-record stock loss.

## Corrected SAS6 frontier

The high matched-square branch no longer requires selection of one exact final record.  At every
density scale, its entire final-positive mass gives a lossless aggregate choice between neutral
persistent repairs, a positive square barrier and negative mixed collateral.

The remaining sparse work is choosing a global scale whose barrier alternative can be paid or ruled
out, batching the neutral output under failed incidence caps, physically exploiting the negative
collateral bank, establishing base-state single-swap admissibility where necessary, realizing
matched-square contracts for every word family, and the positive-base-row or boundary branches.

## Finite check

`scripts/verify_sparse_aggregate_final_output_payment.py` samples exact weighted conjunction tables for
interaction-independent square banks.  It checks final-positive table partition, the high-bank mass
bound, the summed mixed-energy identity, one-use negative collateral, the
neutral/barrier/collateral trichotomy and the integrated `M/(D_sq+1)` constants.
