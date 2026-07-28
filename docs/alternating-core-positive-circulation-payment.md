# Physical payment for positive-output circulation words

**Branch:** `research/alternating-core-chain`

AC3um--AC3uq give every buffer-rich primitive nondecreasing circulation a legal chronological word.
The zero-output case is an exact return.  This note closes the positive-output case whenever boundary
resource growth is paid either by finite physical headroom or by a finite nonreplenishing source
ledger.

## Positive circulation-word model

Fix one root-boundary epoch.  Every realized positive circulation word `w`:

- returns to the same complete finite root-boundary state;
- has net resource output `z_w in Z_(>=0)^q`, `z_w!=0`;
- contains at most
  `L_circ=(q+1)D_q L_macro`
  completed root-return gates and at most `L_circ L_gate` control edges;
- has exact gross created and consumed occurrence counts `R_w,C_w` satisfying
  `M(m')-M(m)=R_w-C_w=sum_i z_(w,i)`.

A word is **cap charged** when its net new output occurrences are assigned to exact residual physical
headroom slots.  Let the finite cap-address set be `P`, with integer residual stocks `h_p>=0`.  It is
**source paid** when there are exact source addresses `u in A`, residual stocks `s_u`, integer rates
`rho_u>=1` and debits `d_(w,u)>=0` such that every gross created occurrence is assigned to those debits
and

`R_w<=sum_u rho_u d_(w,u)`.

Every positive word is assigned canonically to one available route.  Cap slots and source debits are
occurrence-faithful and spent at most once.  New cap addresses, replenished slots or sources, changed
rates, changed occurrence semantics or omitted payment fields are outer resets.

## AC3ur -- strict boundary-stock increase -- PROVED

For every positive circulation word,

`sum_i m_i'-sum_i m_i=sum_i z_(w,i)>=1`.

In particular `R_w>0`.

### Proof

The net output is a nonzero nonnegative integer vector, so its coordinate sum is at least one.  The
gross identity gives `R_w-C_w=sum_i z_(w,i)>0`, hence `R_w>0`. QED.

## AC3us -- physical-headroom budget -- PROVED

Put

`H_cap=sum_(p in P) h_p^(0)`.

Then at most `H_cap` cap-charged positive circulation words occur in the epoch.  Their total net output
is at most `H_cap`.

### Proof

AC3ur gives at least one net new output occurrence on every positive word.  The cap contract assigns
all such output occurrences to distinct residual physical headroom slots.  Summing spent slots gives
both claims. QED.

## AC3ut -- finite-source payment budget -- PROVED UNDER THE SOURCE CONTRACT

Along all source-paid positive circulation words,

`sum_w R_w<=sum_u rho_u s_u^(0)`.

The number of source-paid words is at most

`S_src=sum_u s_u^(0)`.

### Proof

Sum the source-payment inequality.  Every source debit telescopes and is bounded by its initial
nonnegative stock.  AC3ur gives `R_w>0`, so at least one integer source debit is positive on every
source-paid word.  Therefore the word count is at most the total initial source stock. QED.

## AC3uu -- explicit positive-word gate and edge budget -- PROVED

If every positive circulation word is canonically cap charged or source paid, their total number is at
most

`K_pos=H_cap+S_src`.

Their total contribution is at most

`K_pos L_circ`

completed root-return gates and at most

`K_pos L_circ L_gate`

underlying control edges.

### Proof

Apply AC3us and AC3ut to the two disjoint route classes and add their word counts.  Expand each word by
the AC3uo length bound. QED.

If a word satisfies both payment mechanisms, the canonical least-route rule counts it only once.

## AC3uv -- positive-circulation closure router -- PROVED UNDER THE DECLARED CONTRACTS

Every buffer-rich positive primitive circulation has one continuation:

1. exact physical-headroom-slot charge, with total epoch budget `H_cap`;
2. exact finite-source payment, with word budget `S_src` and gross-creation budget
   `sum_u rho_u s_u^(0)`;
3. an existing monotone-output rank, finite ticket, independent descent or outer reset;
4. or one cap, source, gross-occurrence, rate, address, root-boundary, payment or context field fails.

Under finite budgets for the declared alternatives, positive-output circulation words cannot recur
infinitely in one fixed epoch.

### Proof

AC3uq supplies the chronological positive word and its exact output field.  AC3us--AC3uu close the cap
and source routes.  Every other declared route already spends a finite budget or exits the epoch.
An infinite fixed history would force infinitely many headroom units, source debits, tickets, rank
decreases or resets. QED.

## Corrected AC4 numerical frontier

Positive-output primitive circulations are no longer open when their new output occurrences spend
finite physical headroom slots or are occurrence-faithfully paid from finite nonreplenishing sources.
The resulting word, gate and control-edge budgets are explicit.

The remaining numerical work is low-buffer recurrence, free or cyclically replenished circulation
resources, upper-guard or hidden-balance legality, nonlinear or nonadditive balances, unbounded
zero-sum-free lift residuals, dynamic dictionaries and omitted payment fields.

## Finite check

`scripts/verify_ac_positive_circulation_payment.py` samples nondecreasing circulation histories split
between cap and source routes.  It checks strict boundary-stock increase, telescoping headroom and
source budgets, gross creation accounting and the expanded gate/control-edge bounds.
