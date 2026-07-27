# Barrier-density routing for physically matched square banks

**Branch:** `research/sparse-algebraic-spread`

SAS5fh--SAS5fl turn a matched repair/opposite-destruction ledger into a genuine two-stage operation
bank.  At a square-local minimum, a retained square family physically creates and then destroys its
matched records, but its final energy change is a nonnegative sum of square barriers.

This note expands that barrier exactly.  Because every selected matched record is absent both before
the repair stage and after the destruction stage, it contributes zero to the final energy difference.
The complete barrier is therefore final new collateral minus final destroyed collateral among the
remaining exact records.  A threshold split gives either a large physically cancelled bank with small
barrier density or a quantitatively heavy current output record.

## Square-local barrier model

Fix an interaction-independent square bank `J` supplied by SAS5fi--SAS5fj.  For each square
`a in J`, let:

- `H_a>0` be its exact transient matched weight;
- `kappa` be the common base colouring;
- `kappa^a=kappa^(sigma_a tau_a)` be its final colouring;
- `Delta_a=T(kappa^a)-T(kappa)` be its final square barrier.

Assume square-local minimality:

`Delta_a>=0`

for every `a in J`.

For each exact rank-three record `Q` not in the selected matched set of `a`, define its final positive
and negative contributions

`p_(a,Q)=w_Q*(I_Q(kappa^a)-I_Q(kappa))_+`,

`n_(a,Q)=w_Q*(I_Q(kappa)-I_Q(kappa^a))_+`.

Put

`C_a^+=sum_Q p_(a,Q)`,

`C_a^-=sum_Q n_(a,Q)`.

Every selected matched record has indicator zero in both `kappa` and `kappa^a`.

## SAS5fm -- exact final-collateral identity -- PROVED

For every selected square,

`Delta_a=C_a^+-C_a^-`.

For the whole interaction-independent bank,

`H_J=sum_(a in J) H_a`,

`B_J=sum_(a in J) Delta_a`,

`C_J^+=sum_(a in J) C_a^+`,

`C_J^-=sum_(a in J) C_a^-`

satisfy

`B_J=C_J^+-C_J^-`.

Every exact record contributing to `C_J^+` or `C_J^-` is changed by exactly one selected square.

### Proof

For one square, expand the complete exact energy ledger record by record.  A selected matched record is
absent in the base and final states, so its net contribution is zero.  Every other record contributes
its positive final difference, its negative final difference, or zero.  This proves the local
identity.

SAS5fi independence says no complete-ledger scope meets two selected square supports.  Hence one exact
record indicator changes under at most one selected square.  Summing the local identities gives the
bank identity without alias or reuse loss. QED.

The transient matched mass `H_J` is physical even though it cancels from the final energy difference.

## SAS5fn -- low-barrier cancellation or high-barrier output -- PROVED

Fix any rational threshold `lambda>0`.  Partition the selected squares into

`J_low={a:Delta_a<=lambda*H_a}`

and

`J_high={a:Delta_a>lambda*H_a}`.

Exactly one of the following quantitative alternatives holds:

1. **low-barrier cancellation:**

   `sum_(a in J_low) H_a>=H_J/2`,

   and executing `J_low` physically creates and destroys that matched weight with final energy cost at
   most

   `lambda*sum_(a in J_low) H_a`;

2. **high final collateral:**

   `sum_(a in J_high) H_a>H_J/2`,

   and the exact final positive collateral created by `J_high` has total weight strictly greater than

   `lambda*H_J/2`.

### Proof

The two matched weights sum to `H_J`.  If the low part has at least half, add
`Delta_a<=lambda H_a` over that part.  Every subset of an interaction-independent bank remains
interaction-independent, so SAS5fj executes it with exact energy additivity and physical matched
cancellation.

Otherwise the high part has more than half.  Summing its strict inequalities gives

`sum_(a in J_high) Delta_a
 >lambda*sum_(a in J_high) H_a
 >lambda*H_J/2`.

By SAS5fm,

`sum_(a in J_high) C_a^+
 =sum_(a in J_high) Delta_a+sum_(a in J_high) C_a^-
 >=sum_(a in J_high) Delta_a`.

This proves the second alternative. QED.

The theorem is valid for every chosen barrier-density scale `lambda`.

## SAS5fo -- exact record and column localization of a high barrier -- PROVED

Assume the complete final-positive output bank in the high branch has at most `K_out>=1` exact
alias-aggregated record signatures.  Then one exact current final record has weight strictly greater
than

`lambda*H_J/(2*K_out)`.

Moreover one physical board column carries final-positive record incidence strictly greater than

`3*lambda*H_J/(2N)`.

### Proof

SAS5fn gives final-positive weight greater than `lambda H_J/2`.  Weighted pigeonhole over at most
`K_out` exact records gives the first bound.

Every rank-three exact record has three distinct physical columns, so total weighted column incidence
is three times the final-positive weight.  Pigeonhole over the `N` board columns gives the second
bound. QED.

The selected record is present in the final colouring after the two-stage square batch; it is not a
prospective or accounting-only object.

## SAS5fp -- integrated matched-bank barrier bounds -- PROVED

Let the matched square interaction degree be

`D_sq=r*(mu-1)+r*Lambda_sq*(3mu-1)`.

At a square-local minimum, SAS5fi gives an interaction-independent bank with

`H_J>=M/(D_sq+1)`,

where `M` is the original exact matched repair/destruction weight.

For every `lambda>0`, either:

1. a low-barrier bank physically creates and destroys matched weight at least

   `M/[2(D_sq+1)]`

   with final energy cost at most `lambda` times that selected matched weight;

2. one exact current final record has weight strictly greater than

   `lambda*M/[2(D_sq+1)K_out]`;

3. one physical column carries final-positive incidence strictly greater than

   `3*lambda*M/[2N(D_sq+1)]`;

4. or one realization, joint-legality, incidence, complete-ledger or output-stock field fails.

### Proof

Apply SAS5fn to the bank from SAS5fi.  In the low branch use
`H_J>=M/(D_sq+1)`.  In the high branch apply SAS5fo and the same lower bound.  The remaining
alternatives are exactly the hypotheses used by the square and output-stock models. QED.

## SAS5fq -- neutral and common-step barrier router -- PROVED UNDER THE DECLARED CONTRACTS

For the neutral persistent repair branch, let

`A_neu=(2N-3)(4Lambda_rep+1)`.

Whenever the matched branch occurs, either a low-barrier square bank physically cancels weight at
least

`W_neu/[4*A_neu*(D_sq+1)]`,

or one exact final record has weight strictly greater than

`lambda*W_neu/[4*A_neu*(D_sq+1)K_out]`,

or one final-positive column incidence is strictly greater than

`3*lambda*W_neu/[4N*A_neu*(D_sq+1)]`.

For a common-step pair bank, the corresponding bounds are

`B_pair/[4(D_pair+1)(D_sq+1)]`,

`lambda*B_pair/[4(D_pair+1)(D_sq+1)K_out]`

and

`3*lambda*B_pair/[4N(D_pair+1)(D_sq+1)]`.

The improving-square and failed-contract alternatives of SAS5fk remain unchanged.

### Proof

SAS5fg gives

`M>=W_neu/[2*A_neu]`

in the neutral matched branch, while SAS5el gives

`M>=B_pair/[2(D_pair+1)]`

for common-step pairs.  Substitute these bounds into SAS5fp. QED.

## Corrected SAS6 frontier

A nonnegative matched-square barrier no longer remains an undifferentiated scalar.  At every density
threshold it gives either a large physically cancelled matched bank with controlled final energy cost,
or a heavy exact current final record and high-incidence column.

The remaining sparse work is choosing and paying a useful global barrier-density scale, routing the
heavy final current record through a descending or arithmetic classifier, realizing the local and
joint matched-square contracts for every word family, resolving composed-only positive curvature,
positive base-row realization, and the reflected-boundary or high-incidence branches.

## Finite check

`scripts/verify_sparse_matched_square_barrier_density.py` samples square-local exact indicator ledgers.
It checks the final positive-minus-negative identity, interaction-independent additivity, the
low/high barrier-density split, exact-record and column localization, and the integrated neutral and
common-step constants.
