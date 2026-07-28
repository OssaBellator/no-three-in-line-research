# Clean-height routing for compatible same-token Hall fans

**Branch:** `research/geometric-cleaning`

GC4q--GC4t turn a compatible same-token fan into union-safe current payment or an exact weighted Hall core. The remaining execution issue is clean height: a selected operation may create a protected high-level certificate even when its current-factor accounting is correct. This note separates a clean-height-safe subfan before applying the same-token payment theorem.

## Complete protected-event inventory

Let `I` be an installably compatible same-token, same-role fan. Operation `y in I` has demand weight `lambda_y>0`, all operations share the exact current token `pi`, and

`W=sum_(y in I)lambda_y`.

Assume the **height-separable same-token contract**:

1. every operation has a complete exact inventory of protected-height events created by its installation;
2. an operation is **height-safe** when that inventory is empty;
3. every unsafe operation has one least protected-event address from a finite dictionary `P_H`, with `K_H=|P_H|`;
4. for every compatible subfamily, protected events are the union of the member inventories; no new cross-operation protected event appears;
5. restricting to a subfamily preserves the common token, role, destruction-faithful eligibility and installable compatibility;
6. aliases, lineages, labels and contexts are fixed before choosing the least protected-event address;
7. a missing inventory field or cross-operation protected event is returned explicitly.

Write `I_safe` and `I_bad` for the safe and unsafe operations and put

`W_safe=sum_(y in I_safe)lambda_y`,

`W_bad=sum_(y in I_bad)lambda_y`.

For `p in P_H`, let `H_p` be the total demand weight of unsafe operations whose least protected-event address is `p`.

## GC4u -- exact clean-height partition -- PROVED

One has

`W=W_safe+W_bad`

and

`W_bad=sum_(p in P_H)H_p`.

Every compatible subfamily of `I_safe` preserves clean height.

### Proof

Safe and unsafe operations partition `I`; least protected-event addresses partition the unsafe part. Height separability makes the product inventory of a safe subfamily empty. QED.

## GC4v -- safe half or one exact protected-event cause -- PROVED

Exactly one of the following weighted alternatives holds:

1. `W_safe>=W/2`;
2. one exact protected-event address satisfies

   `H_p>W/(2K_H)`.

### Proof

If the safe weight is below half, then `W_bad>W/2`. Pigeonhole the exact address partition from GC4u. QED.

The second output is occurrence-addressed protected-event demand, not automatically distinct certificate weight.

## GC4w -- clean-height-safe same-token payment/deficiency -- PROVED

Assume the safe-half branch. Fix the noncommon reuse bound `r` and payment normalization `kappa>=1` from GC4q. Applying GC4r to the safe subfan gives either:

1. a clean-height-preserving joint installation with current payment at least

   `omega_pi+W/(4r kappa)`;

2. a clean-height-safe weighted Hall deficiency greater than

   `W/(4kappa)`.

### Proof

GC4r applied to `I_safe` gives payment

`omega_pi+W_safe/(2r kappa)`

or deficiency greater than `W_safe/(2kappa)`. Use `W_safe>=W/2`. The installation and every compatible Hall-core subfamily preserve clean height by GC4u. QED.

## GC4x -- composition with labelled-fan extraction -- PROVED

Let a same-token, same-role fibre have weight `W_0` and conflict degree at most `Gamma`. GC4l supplies a compatible family of weight at least

`W_0/(Gamma+1)`.

Under the height-separable contract, one obtains:

1. clean-height-preserving current payment at least

   `omega_pi+W_0/[4r kappa(Gamma+1)]`;

2. a clean-height-safe weighted Hall deficiency greater than

   `W_0/[4kappa(Gamma+1)]`;

3. one exact protected-event address of demand greater than

   `W_0/[2K_H(Gamma+1)]`;

4. or one conflict-degree, height-inventory, separability, lineage, context or execution field fails.

### Proof

Apply GC4v--GC4w to the compatible family of weight at least `W_0/(Gamma+1)` and substitute. QED.

## GC4y -- clean-height same-token router -- PROVED UNDER THE DECLARED CONTRACTS

A compatible same-token Hall fan no longer requires clean-height preservation as an unstructured extra hypothesis. It yields clean-height-safe payment, a clean-height-safe exact Hall core, or one concentrated protected-event cause. The Hall-core branch enters GC2al--GC2ap and GC4t without losing the displayed deficiency scale.

## Corrected GC5 frontier

Same-token union accounting and clean-height filtering now compose quantitatively. A selected transition either preserves clean height through payment/Hall-core extraction or returns one exact protected-event address with explicit demand.

The remaining geometry is payment or removal of that protected-event cause, neutralization or delegation of the clean-height-safe minimal Hall core, capacity-overloaded target-common/global blockers, bounded small donor reservoirs, repeated non-tagged feedback, roles outside the singleton-rectangle host, pool depletion and local superregular resampling.

## Finite check

`scripts/verify_gc_clean_height_same_token_router.py` samples weighted compatible fans, protected-event addresses and bounded-reuse noncommon pools. It checks the safe/unsafe partition, protected-cause concentration, clean-height-safe payment/deficiency constants and the labelled-fan composition bounds.
