# Steinitz-buffer realization of primitive coupled-resource circulations

**Branch:** `research/alternating-core-chain`

AC3uc--AC3ug apply a finite-dimensional cone alternative to a coupled additive macro dictionary.
AC3uh--AC3ul already realize every primitive circulation by a fixed canonical order with a buffer growing
linearly in its bounded word length.  This note sharpens that chronological result under the stronger
gross-consumption legality contract: the required prefix buffer depends only on the resource dimension
and one-macro increment size, not on the circulation length.

Append `z_i` virtual unit drains in coordinate `i`, apply the Steinitz rearrangement lemma to the
resulting zero-sum vector family, and then delete the virtual drains.  The remaining real macro order has
coordinatewise prefix deficit at most `q max(B,1)`.  Gross-consumption headroom then makes the entire
primitive circulation chronologically legal.

## Buffered primitive-circulation model

Retain the coupled additive macro model of AC3uc--AC3ug.  Fix one primitive circulation address

`x in Z_(>=0)^k`,  `x!=0`,  `z=Vx in Z_(>=0)^q`.

Write

`L=|x|_1`

for its real macro multiplicity and put

`B_0=max(B,1)`.

For coordinate `i`, let

`C_i=max_(lambda in Lambda)c_(i,lambda)`

be the largest gross consumption of one live macro and define the **Steinitz buffer**

`beta_i=C_i+qB_0`.

Assume the **common-boundary resource-only legality contract**:

1. every macro in the circulation begins and ends at the same complete finite root-boundary state;
2. inside that state its only changing legality field is the displayed resource test `m>=c_lambda`;
3. executing one macro changes resources exactly by `v_lambda` and preserves the circulation dictionary;
4. exact gross occurrence identities and every payment-sensitive field are present in the macro address;
5. a changed boundary state, dictionary, vector, consumption row or omitted legality field is an outer reset;
6. failure returns the least macro, coordinate, gross-consumption, boundary, occurrence or context field.

## AC3um -- Steinitz ordering with one-sided resource deficit -- PROVED

The multiset containing `x_lambda` copies of every real vector `v_lambda` admits an ordering

`v_(lambda_1),...,v_(lambda_L)`

such that every real prefix satisfies

`sum_(j=1)^t v_(lambda_j)>=-qB_0*1`

coordinatewise for `0<=t<=L`.

The final sum is `z>=0`.

### Proof

Append `z_i` copies of the virtual vector `-e_i`.  The complete family has sum zero and every vector has
infinity norm at most `B_0`.  The Steinitz rearrangement lemma in dimension `q` gives an ordering whose
full partial sums have infinity norm at most `qB_0`.

Delete the virtual drain symbols while preserving the order of the real macros.  At a real prefix, let
`d>=0` be the coordinatewise number of virtual drains which occurred before the corresponding point in
the full ordering.  The real prefix sum equals the bounded full partial sum plus `d`, so it is at least
`-qB_0` in every coordinate.  Its final value is the sum of the real vectors, namely `z`. QED.

The virtual drains are a proof device only; they are never executed.

## AC3un -- uniform buffer makes the circulation chronological -- PROVED UNDER THE LEGALITY CONTRACT

If the current resource state satisfies

`m_i>=beta_i`

for every coordinate, the order from AC3um is a legal chronological execution of all `L` real macros.
Every intermediate state is nonnegative and has enough stock for the next gross consumption.  The final
resource state is

`m'=m+z>=m`.

### Proof

Before macro `lambda_(t+1)`, AC3um gives current stock at least

`m-qB_0*1>=C`

coordinatewise.  Since `c_(i,lambda)<=C_i`, the next gross-consumption test is legal.  The same inequality
also gives a nonnegative post-prefix resource vector.  Induct through all macros.  The final identity is
the definition of `z=Vx`.  The nonresource legality fields are unchanged by the common-boundary contract.
QED.

## AC3uo -- explicit chronological word and buffer-address stocks -- PROVED

For the primitive circulation supplied by AC3ue,

`L<=(q+1)D_q`.

Hence a buffer-rich realization uses at most

`(q+1)D_q L_macro`

completed root-return gates and at most

`(q+1)D_q L_macro L_gate`

underlying control edges.

If the state is not buffer rich, return the least deficient pair

`(i,m_i)`,  `0<=m_i<beta_i`.

The safe stock of exact deficient-coordinate addresses is

`K_buf=sum_(i=1)^q beta_i`.

### Proof

The length bound is AC3ue.  Expand each macro by its declared gate and control-edge bounds.  A failed
buffer test has one least coordinate and one integer level below its threshold; summing the threshold
stocks gives `K_buf`. QED.

The deficient address is not itself a termination proof.  It is a finite exact boundary field for the
existing boundary-gate, ticket, payment or reset routers.

## AC3up -- exact-return and positive-output circulation routes -- PROVED

For a buffer-rich primitive circulation:

1. if `z=0`, its chronological word is an exact return to the same finite boundary state and resource
   vector;
2. if `z!=0`, its word is a chronological nondecreasing resource return and one least coordinate has
   positive output `z_i>=1`.

In the first case the complete word is an exact recurrence address.  In the second case the least
positive coordinate is an exact net-output field.  The gross macro ledger retains the occurrence
identities of the created units which realize that net output, and those units must enter an existing cap,
source-payment, ticket, monotone-output or outer-reset route.

### Proof

AC3un gives final state `m+z` with the same finite root-boundary state.  If `z=0`, every field returns
exactly.  Otherwise nonnegativity and integrality of `z` give a least positive coordinate with value at
least one. QED.

No free quotient is claimed for a positive-output circulation.

## AC3uq -- buffered circulation realization router -- PROVED UNDER THE DECLARED CONTRACTS

Every primitive nondecreasing circulation address from AC3ue now has one continuation:

1. a buffer-rich legal chronological word of at most `(q+1)D_q` macros;
2. an exact zero-output return entering erasure, descent, finite ticket or reset closure;
3. a positive-output return entering physical cap, source-payment, monotone-output or ticket accounting;
4. one of at most `K_buf` exact deficient-coordinate addresses;
5. or one common-boundary, gross-consumption, occurrence, legality, dictionary or context failure.

Consequently AC3uh--AC3ul are sharpened in buffer-rich states whenever gross consumption is the
complete resource-legality test.  What remains is payment of positive-output circulations and control of
histories trapped below one or more buffer thresholds.

### Proof

Apply AC3um--AC3uo.  AC3up classifies the realized final output.  Every excluded hypothesis is retained as
a named failure or outer reset. QED.

## Corrected AC4 numerical frontier

Primitive nondecreasing circulation addresses now have canonical chronological realizations whenever
every resource coordinate has gross-consumption headroom `C_i+q max(B,1)`.  The ordering loss is linear
in the resource dimension and independent of the circulation length.

The remaining numerical work is payment of positive-output circulation words, low-buffer recurrence,
free or cyclically replenished resources, genuinely nonlinear or nonadditive balances, unbounded
zero-sum-free lift residuals, dynamic dictionaries and omitted payment fields.

## Finite check

`scripts/verify_ac_steinitz_circulation_realization.py` enumerates and samples small primitive
nondecreasing vector multisets.  It finds a real macro ordering with the asserted one-sided prefix bound,
checks gross-consumption legality from the Steinitz buffer, exact final output, deficient-address counts
and the inherited macro/gate/control-edge bounds.
