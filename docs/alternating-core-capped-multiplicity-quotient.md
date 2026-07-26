# Threshold-capped multiplicity quotients and monotone supply

**Branch:** `research/alternating-core-chain`

AC3oz--AC3pd quotient arbitrarily many symbolic aliases through one finite
payment-complete physical signature.  A remaining source of apparent infinitude is
an exact integer multiplicity attached to that signature.  The raw multiplicity need
not be inserted into the recurrence alphabet when all structural decisions depend
only on finitely many thresholds and the remaining units form additive supply.

This note separates those two roles.  Threshold-capped multiplicity belongs to the
finite owner signature.  Raw multiplicity above the thresholds is a monotone integer
resource counter.  Replenishment is not free: it is an outer reset or must receive a
separate ticket/payment theorem.

## Capped multiplicity signatures

Let `Sigma_0` be a finite reconstructed physical-signature set.  Fix `q>=1`
multiplicity coordinates and thresholds

`H=(H_1,...,H_q) in Z_(>=0)^q`.

For a raw multiplicity vector `m in Z_(>=0)^q`, define

`cap_H(m)_i=min(m_i,H_i)`.

The capped structural signature is

`Sigma_H=Sigma_0 x product_(i=1)^q {0,1,...,H_i}`.

Assume owner identity, currentness and the set of certified continuation kinds depend
on raw multiplicity only through `cap_H(m)`.  Exact units above the thresholds may
still be consumed as additive private supply, but do not distinguish structural
owner identities.

## AC3pe -- finite threshold quotient -- PROVED

The capped signature stock satisfies

`|Sigma_H|=|Sigma_0|*product_i(H_i+1)`.

Consequently every currentness predicate and certified continuation graph which
factor through `Sigma_H` have a finite exact state and edge alphabet.  If `q` is
constant and `|Sigma_0|` and all `H_i` are polynomially bounded, the capped signature
stock is polynomial.

### Proof

Choose one base signature and one capped value in each coordinate.  The choices are
independent, giving the product.  Every factored predicate or continuation relation
is a function or relation on this finite set. QED.

The constant-`q` qualification is necessary: a product of polynomially many
nontrivial coordinate ranges may be exponential.

## AC3pf -- multiplicity identity wall -- PROVED UNDER THE CAPPED-MULTIPLICITY CONTRACT

Two raw owner states `(sigma_0,m)` and `(sigma_0',m')` may be treated as the same
structural owner state exactly when their declared payment-complete capped signatures
agree and the continuation witness projects to the same registered capped edge and
kind.

Equality of physical support alone is insufficient.  Conversely, distinct raw
values above the thresholds do not create distinct owner identities merely by being
numerically different.

If currentness, eligibility, phase, capacity type or any other payment-relevant
semantic can distinguish two raw values with the same cap, the capped-multiplicity
contract fails and that datum must be added to the signature.

### Proof

The contract declares the capped signature to contain every structural datum.
Registered capped continuation therefore suffices.  Any omitted semantic distinction
would make the quotient nonfaithful, while numerical differences which affect only
how many additive units remain are resource amounts rather than owner identities.
QED.

## AC3pg -- canonical capped recreation gate -- PROVED

Let a certified raw lineage path begin in a noncurrent state and end in a current
state.  Project every state to `Sigma_H`.  There is a unique first path edge whose
projected currentness changes from zero to one.  The projected source signature,
target signature and continuation kind form the canonical capped-multiplicity
recreation gate.

Writing `S_H=|Sigma_H|` and letting `K_H` be the number of continuation kinds, the
safe false-to-true gate stock satisfies

`E_H<=K_H*floor(S_H^2/4)`.

### Proof

The projected truth word begins with zero and ends with one because currentness
factors through the cap.  Choose the least index where it becomes one.  The complete
false/true directed-pair stock is at most the balanced product, with one decoration
for each continuation kind. QED.

Raw multiplicity changes which leave the cap unchanged cannot themselves be a
currentness recreation gate.

## AC3ph -- monotone raw supply has an integer potential -- PROVED

Inside one multiplicity epoch, suppose the raw vectors form a coordinatewise
nonincreasing history

`m^(0)>=m^(1)>=m^(2)>=...>=0`,

and every accepted multiplicity-consuming transition decreases

`M(m)=sum_i m_i`

by at least one.  Then the number of accepted consuming transitions is at most

`M(m^(0))`.

This remains true when long stretches occur above every threshold and therefore leave
the capped signature unchanged.

### Proof

`M` is a nonnegative integer, begins at `M(m^(0))`, and strictly decreases on every
accepted consuming transition. QED.

Any coordinate increase replenishes raw supply.  It must be recorded as a higher
outer reset or charged to an independently bounded source; otherwise fresh
multiplicity can recreate an unbounded ticket stock.

## AC3pi -- closure under capped signatures and monotone multiplicity -- PROVED UNDER THE CAPPED-SUPPLY CONTRACT

Inside one reconstructed multiplicity epoch assume:

1. every owner state has a finite payment-complete capped signature in `Sigma_H`;
2. currentness and certified continuation factor through the capped signature;
3. all raw multiplicity not represented structurally by the cap is additive private
   supply;
4. raw multiplicity is coordinatewise nonincreasing inside the epoch, and every
   accepted supply-consuming step decreases its total by at least one;
5. every capped false-to-true gate is impossible, terminal/improving, strictly
   descending, or consumes finite unrestorable shared gate capacity;
6. every replenishment or departure from the reconstructed cap contract is a higher
   outer reset.

Then unbounded initial raw multiplicity cannot sustain an infinite nonterminal owner
recreation history inside the epoch.

### Proof

AC3pg sends every structural recreation to one gate in a finite stock.  The declared
gate routes bound or eliminate those returns.  Steps which consume multiplicity while
leaving the cap unchanged are bounded by AC3ph.  Replenishment exits the epoch.
Recreation-free common-owner segments are bounded by AC3nz. QED.

## Corrected AC4 owner frontier

Payment-relevant multiplicity is no longer automatically a state-space obstruction.
It closes when:

- structural semantics factor through finitely many capped coordinates; and
- the uncapped remainder is monotone additive supply.

The remaining owner cases are genuinely unbounded structural thresholds or support,
semantics which distinguish arbitrarily large raw values, replenishable multiplicity
without a source ledger, nonadditive/shared resources not covered by an exact capacity
model, and the unresolved availability, conflict, reverse and arithmetic macro-cycle
interfaces.

## Finite check

`scripts/verify_ac_capped_multiplicity_quotient.py` exhausts small threshold vectors,
base signatures, raw aliases and projected truth paths.  It checks the product stock,
identity wall, first capped boundary, gate bound, shared alias capacities and monotone
raw-supply potential.