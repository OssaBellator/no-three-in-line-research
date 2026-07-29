# Exact-core capacity bank for iterated heavy legality atoms

**Branch:** `research/sparse-algebraic-spread`

SAS5hx--SAS5ib reduce weighted legality conflicts to a nested common core `C` of size at most the candidate support rank. This note supplies the finite execution bank once the exact core is physically shareable.

## Core capacity

Let `C` be a nonempty exact set of physical atoms shared by every candidate in one terminal fan. Each atom `a in C` has an initial nonnegative integer capacity `kappa_a`. A legal execution through the fan consumes one unit from every atom of `C`.

Optional replenishment deposits are recorded exactly as `r_a>=0`; write `R_a` for their cumulative totals.

## SAS5ic -- exact common-core debit -- PROVED

After `N` executions,

\[
N\le kappa_a+R_a
\qquad\text{for every }a\in C.
\]

Hence

\[
\boxed{N\le\min_{a\in C}(kappa_a+R_a).}
\]

### Proof

Every execution debits one unit from every core atom, and no capacity account may become negative. QED.

## SAS5id -- nonreplenishing terminal bound -- PROVED

If `R_a=0` for all `a`, at most

\[
\boxed{\min_{a\in C}\kappa_a}
\]

terminal-fan executions occur. One least-capacity atom is exhausted and becomes the canonical stopping witness.

## SAS5ie -- weighted execution variant -- PROVED

If an execution of weight `u>=0` consumes `u` units from every core account, then the total executed weight is at most

\[
\min_{a\in C}(\kappa_a+R_a).
\]

The conclusion is unchanged for rational weights after clearing one common denominator.

## SAS5if -- core overload alternative -- PROVED UNDER EXACT SHAREABILITY

For every terminal heavy core:

1. if all core accounts have remaining capacity, execute the residual-independent fan and debit the common core once per selected candidate;
2. if some account lacks capacity, return the least exhausted exact atom as a physical overload;
3. if the common use cannot be represented by the declared capacity account, return a shareability or legality reset.

Thus a bounded heavy core is either an executable finite resource or one exact overload, not an unstructured high-incidence output.

## SAS5ig -- SAS6 interface -- PROVED UNDER COMPLETE CORE LINEAGE

Combining SAS5hx--SAS5ib with SAS5ic--SAS5if gives a terminating local router:

- extend the nested heavy core at most `r` times;
- stop at a light residual fan or depth `r`;
- execute while exact core capacity remains;
- then return one least exhausted core atom, paid replenishment, or reset.

Remaining work is arithmetic verification of shareability and payment for the finite exact core atoms, plus the global barrier, neutral and compression ledgers.

## Finite check

`scripts/verify_sas_exact_core_capacity_bank.py` generates nested core accounts with exact replenishment, execution and overload attempts and verifies that all core debits remain equal and bounded by the least total capacity.