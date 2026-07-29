# Rational-inverse collateral-deposit source conservation

This note records RI5du--RI5dy. It traces named deposits in the cumulative joint owner/charge bank back to occurrence-faithful physical source mass.

## Contract

Let `P` be exact physical source classes and `C` exact collateral-source classes. Every live physical occurrence carries nonnegative integer mass. Initial physical mass and explicitly named exogenous physical deposits are the only new mass. A legal physical transition is one-for-one and output mass is at most input mass. Issuing `x` units into collateral class `c` consumes exactly `x` units from one compatible physical source occurrence. Owner-cost and perturbation-charge payment consumes collateral balance.

## Theorem block

### RI5du — physical source conservation

Across every legal transition, remaining live physical mass plus terminally consumed mass does not exceed initial physical mass plus named exogenous deposits.

### RI5dv — collateral issuance is transfer

Every named collateral deposit is a transfer from the physical account. Issuance decreases live physical mass by the same amount that it increases one exact collateral class.

### RI5dw — joint epoch law

At every time,

`live physical mass + live collateral balance + terminal paid/expired mass <= initial physical mass + exogenous deposits`.

Thus cumulative owner/charge payment cannot exceed the physical source account.

### RI5dx — exact amplification witness

Splitting, output-mass increase, source-less collateral issuance, missing predecessor lineage or an unrecorded physical deposit is detected at the first step where the joint mass exceeds its account.

### RI5dy — reset boundary

Changed owner/coherence/host/context/arithmetic fields, relabelled source classes, omitted compatibility or nonadditive collateral semantics return reset rather than conservation.

## Proof

Each legal operation preserves or decreases the joint mass: transitions are nonamplifying, issuance moves mass between accounts, and payment moves collateral into terminal consumption. Summation over the history gives RI5dw. The first violated inequality is the canonical amplification witness.

## Finite audit

Run `python scripts/verify_ri_collateral_deposit_source_conservation.py`.

## Scope

This theorem does not construct the arithmetic source classes or prove their exogenous deposits. It does not prove RI6 or the no-three-in-line conjecture.