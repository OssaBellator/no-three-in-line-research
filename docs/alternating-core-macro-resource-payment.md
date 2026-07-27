# Resource-ledger payment for auxiliary macro cycles

**Branch:** `research/alternating-core-chain`

AC3tn--AC3tw reduce finite-field and one-counter root-boundary recurrence to exact chronological
macro cycles.  The remaining case is a macro which returns to the same finite auxiliary state and
primitive lift but changes an unbounded physical resource inventory.  This note gives that cycle a
finite occurrence-faithful payment ledger.  Resource creation is allowed, but only against exact
debits from a finite nonreplenishing source stock.

The result is a direct macro-level analogue of AC3pj--AC3pn.  It supplies an explicit bound on both
completed root-return gates and their underlying control edges.

## Resource-charged macro model

Fix one root-boundary epoch.  Let:

- `Y` be the finite auxiliary boundary-state set, with `a=|Y|>=1`;
- every canonical simple auxiliary cycle contain at most `L_cyc` completed root-return gates;
- every completed root-return gate contain at most `L_gate` underlying control edges;
- `m=(m_1,...,m_q)` be a vector of nonnegative integer physical resource units;
- `A` be a finite set of exact source addresses;
- source `u in A` have residual integer stock `s_u>=0` and fixed conversion rate `rho_u>=1`.

A completed canonical auxiliary cycle is **resource accepted** when it returns to the same finite
boundary state and primitive lift and its resource/source update satisfies the contract below.
For one execution let `r_i,c_i` be the gross numbers of newly created and consumed occurrence
units of resource type `i`, with

`0<=c_i<=m_i`

and

`m_i'=m_i-c_i+r_i`.

Created units receive new occurrence identities even when their type equals a consumed unit.  Put

`R=sum_i r_i`,

`C=sum_i c_i`

and

`d_u=s_u-s_u'`.

Assume the **macro resource-payment contract**:

1. `d_u>=0` for every exact source address;
2. every created resource unit is assigned occurrence-faithfully to exact source debits;
3. aggregate creation satisfies

   `R<=sum_(u in A) rho_u*d_u`;

4. every accepted nonstuttering macro consumes at least one resource unit or has a positive source
   debit;
5. source addresses, rates, resource semantics and macro words are fixed inside the epoch;
6. source replenishment, a new source address, a rate change, omitted payment data or a change of
   macro law is an outer reset.

A cycle which is quotient-stuttering, independently descending, impossible or already ticketed may
use its existing route instead of this resource route.

## AC3tx -- exact macro resource inequality -- PROVED UNDER THE PAYMENT CONTRACT

For every resource-accepted macro,

`M(m')-M(m)=R-C`,

where

`M(m)=sum_i m_i`.

Moreover

`R<=sum_u rho_u*d_u`.

If `R>0`, at least one exact source debit is positive.  Thus no physical resource recreation is
hidden inside a finite auxiliary-state return.

### Proof

Summing `m_i'=m_i-c_i+r_i` over the resource types gives the first identity.  The second statement
is item 3 of the contract.  If `R>0` and every `d_u=0`, the right side vanishes, contradicting the
strict positivity of `R`. QED.

The source address includes every field affecting conversion or payment status; equal geometric
support alone is not a valid debit.

## AC3ty -- total macro recreation is source bounded -- PROVED

Along any resource-accepted history,

`sum_t R_t<=sum_u rho_u*s_u^(0)`.

The number of macro executions with positive resource creation is at most

`sum_u s_u^(0)`.

### Proof

Sum AC3tx over the history.  Each source debit telescopes and is at most its initial nonnegative
stock.  A positive-creation macro has at least one positive integer debit, so the number of such
macros is at most the total initial source stock. QED.

## AC3tz -- explicit accepted-cycle count -- PROVED

Assume every accepted nonstuttering macro has `C>=1` or a positive source debit.  Then the number
`K_acc` of resource-accepted macro executions satisfies

`K_acc<=M(m^(0))+sum_u (rho_u+1)*s_u^(0)`.

### Proof

Nonnegativity of the final resource inventory gives

`sum_t C_t<=M(m^(0))+sum_t R_t`.

Apply AC3ty to bound the right side by

`M(m^(0))+sum_u rho_u*s_u^(0)`.

Each accepted macro is counted by at least one consumed resource unit or one source debit.  Therefore

`K_acc<=sum_t C_t+sum_(t,u)d_(t,u)`,

and the final debit sum is at most `sum_u s_u^(0)`. QED.

Mixed consume/recreate macros are only overcounted.

## AC3ua -- lexicographic physical payment potential -- PROVED

Define

`Phi_res=M(m)+sum_u rho_u*s_u`

and

`S_res=sum_u s_u`.

On every resource-accepted nonstuttering macro:

- if `C>=1`, then `Phi_res` strictly decreases;
- if `C=0`, then `Phi_res` does not increase and `S_res` strictly decreases.

Hence `(Phi_res,S_res)` decreases lexicographically on every accepted macro.

### Proof

By AC3tx,

`Delta Phi_res=R-C-sum_u rho_u*d_u<=-C`.

This is strictly negative when `C>=1`.  When `C=0`, item 4 forces a positive source debit, so
`S_res` decreases by at least one while `Phi_res` does not increase. QED.

## AC3ub -- resource-paid auxiliary-cycle closure -- PROVED UNDER THE DECLARED CONTRACTS

Put

`K_res=M(m^(0))+sum_u (rho_u+1)*s_u^(0)`.

Inside one fixed epoch, suppose every canonical simple auxiliary cycle is one of:

1. quotient-stuttering and erasable;
2. strictly descending in an existing well-founded rank;
3. charged to an existing finite exact ticket;
4. resource accepted under the macro resource-payment contract;
5. impossible;
6. or an outer reset.

Then at most `K_res` resource-accepted cycles occur.  After erasing stutters and using the independent
descent/ticket budgets, the contribution of resource-accepted cycles plus one final cycle-free
auxiliary tail is at most

`K_res*L_cyc+(a-1)`

completed root-return gates and at most

`[K_res*L_cyc+(a-1)]*L_gate`

underlying control edges.

### Proof

AC3tz bounds the number of resource-accepted cycle executions.  Each contains at most `L_cyc`
completed gates.  Once all extracted cycles have been removed or discharged, an auxiliary path with
no repeated state has at most `a-1` gates.  Multiply the completed-gate count by `L_gate`.  The other
cycle classes use their stated finite closure mechanisms or leave the epoch. QED.

## Corrected AC4 numerical frontier

Unticketed auxiliary macro cycles are no longer open when every nonstuttering return consumes an
occurrence-faithful physical resource unit or recreates units from a finite nonreplenishing source
ledger.  The entire resource-paid part has an explicit gate and control-edge budget.

The remaining numerical work is free or cyclically replenished macro resources, multiple coupled
nonadditive balances, unbounded zero-sum-free lift residuals, dynamic control graphs, omitted
payment/ownership fields, and changes of law not declared as outer resets.

## Finite check

`scripts/verify_ac_macro_resource_payment.py` samples integer resource/source systems and accepted
macro histories.  It checks exact gross occurrence accounting, source-faithful recreation,
telescoping creation bounds, the accepted-cycle bound, lexicographic descent and the expanded
root-return/control-edge budget.
