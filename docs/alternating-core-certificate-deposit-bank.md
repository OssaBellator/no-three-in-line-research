# Alternating-core certificate deposit bank

This note records AC5ci--AC5cm. It extends the exact layer-defect certificate transport across repeated restricted-menu epochs without reusing certificate capacity.

## Contract

Fix a finite set of exact layer-defect classes `L`, a finite set of certificate classes `C`, and a complete compatibility graph `E subseteq L x C`. At epoch `t`, layer `l` has integral defect demand `d_t(l)`. Certificate `c` has current integral balance `b_t(c)`. Exact named deposits are added before the epoch. Every paid defect unit is assigned to one compatible certificate and debits one unit of its current balance.

## Theorem block

### AC5ci — current integral certificate flow

For fixed current balances, all layer defects are paid exactly if and only if every layer subset `X` satisfies

`sum_{l in X} d_t(l) <= sum_{c in N(X)} b_t(c)`.

### AC5cj — canonical current failure cut

If payment fails, the maximum unpaid defect equals the maximum capacitated Hall deficit. The least maximizing layer subset and its exact certificate neighborhood form the canonical current failure cut.

### AC5ck — cumulative balance conservation

Across every sequence of fully paid epochs, cumulative debit from certificate `c` is at most its initial balance plus all named deposits into `c`.

### AC5cl — first-unpaid-epoch alternative

Either every epoch is paid by the evolving balances, or the first unpaid epoch returns its current canonical layer/certificate Hall cut. Earlier paid epochs remain valid and are not retrospectively reallocated.

### AC5cm — reset boundary

An omitted layer or certificate class, changed compatibility arc, unrecorded deposit, relabelled obstruction class, fractional splitting outside the integral expansion, or certificate reuse without debit is outside the theorem and returns reset.

## Proof

AC5ci and AC5cj are integral max-flow/min-cut. AC5ck follows by summing the exact debits of each certificate. Applying the current theorem after every named deposit proves AC5cl.

## Finite audit

Run `python scripts/verify_ac_certificate_deposit_bank.py`.

The deterministic audit checks 6,000 finite systems, 9,230 epochs, 40,301 compatibility arcs, 59,134 defect-demand units, 21,728 paid units, 15,986 deposit units, 4,378 deficient epochs carrying 18,590 unpaid units, and 167,070 exact Hall-subset checks.

## Scope

This theorem does not construct the physical certificate graph or prove its capacities and deposits. Those remain the concrete AC5 target. AC4, AC5, AC6 and the no-three-in-line conjecture are not proved.