# Prime-support growth from a multiplicative height bank

**Branch:** `research/orbit-phase-expansion`

OP4as--OP4bb close finite-prime-support valuation and unit recurrence. This note handles growth of the prime dictionary when every first appearance is witnessed by a paid numerator or denominator factor.

## First-introduction witnesses

Fix one scale epoch. Whenever a prime `p` appears for the first time in any physical or relative scale, retain an exact source factor whose numerator or denominator is divisible by `p`. Choose one first-introduction witness for each new prime.

Assume the product of the distinct prime parts of all accepted first-introduction witnesses is bounded by a multiplicative height bank

\[
H_{\rm src}\ge1.
\]

This contract is satisfied, for example, when the source operation supplies a nonreplenishing product budget and each new prime is charged once.

## OP4bc -- new primes consume height -- PROVED

If `P_new` is the set of newly introduced primes, then

\[
\prod_{p\in P_{\rm new}}p\le H_{\rm src}.
\]

### Proof

Each new prime divides its selected first-introduction witness. Removing repeated and old prime factors can only lower the product. Multiply the retained distinct prime parts. QED.

## OP4bd -- logarithmic support bound -- PROVED

The number of new primes satisfies

\[
\boxed{|P_{\rm new}|\le\lfloor\log_2 H_{\rm src}\rfloor.}
\]

### Proof

Every prime is at least two, so `2^{|P_new|}` is at most their product and hence at most `H_src`. QED.

## OP4be -- finite expanded valuation/unit quotient -- PROVED

After adjoining all primes permitted by OP4bd, the valuation vector has finite dimension and every residue-unit factor lies in the corresponding fixed finite unit dictionary. The valuation-drift and unit-clock routers OP4as--OP4bb therefore apply without further prime-support growth.

## OP4bf -- replenished height bank -- PROVED UNDER THE PAID-FACTOR CONTRACT

If additional height deposits of total multiplicative budget `R` are admitted, replace `H_src` by `H_src R`. Every new support prime is still charged once, and

\[
|P_{\rm new}|\le\lfloor\log_2(H_{\rm src}R)\rfloor.
\]

A free, cyclically replenished or unrecorded factor source is returned as an explicit reset.

## OP4bg -- OP5 interface -- PROVED UNDER COMPLETE SCALE LINEAGE

Dynamic prime support has one continuation:

1. finite logarithmic expansion of the valuation/unit dictionary;
2. debit from a paid multiplicative source bank;
3. strict source-height or denominator descent;
4. physical impossibility of the selected first-introduction factor;
5. or an explicit reset in factor source, unit dictionary, scale lineage or legality interpretation.

After the finite expansion, the existing valuation, unit, holonomy and physical restoration clocks close recurrence. The remaining obstruction is genuinely unbounded unpaid factor creation.

## Finite check

`scripts/verify_op_prime_support_height_bank.py` factors deterministic random source witnesses, charges each fresh prime once and verifies the product and logarithmic support bounds.