# Bounded-denominator occurrence-slot repair transversal

## Contract

Fix one finite primitive-potential use/slot graph `G=(U,S,E)` with complete physical occurrence, source, numerator weight, rational gain, damping, restoration and slot addresses. Let `C` be the canonical least maximum-deficit restoration core from BDA5gb--BDA5gf and set

`delta = |C| - |N_G(C)| > 0`.

A repair extension `G+=(U,S+,E+)` retains `S subseteq S+` and `E subseteq E+` and admits an injective restoration assignment `P:U -> S+`. Every new potential slot or compatibility edge has a complete arithmetic lineage record.

## Theorem block BDA5gg--BDA5gk

### BDA5gg — missing-neighbour repair count

For

`R_P(C) = {(u,P(u)) : u in C and P(u) notin N_G(C)}`,

one has `|R_P(C)| >= delta`. Only `|N_G(C)|` core uses can occupy old neighbouring slots, whereas all `|C|` uses receive distinct assigned slots.

### BDA5gh — genuinely new arithmetic incidence

Every pair in `R_P(C)` belongs to `E+ \ E`. Its primitive weight, gain, damping and predecessor address therefore describe a genuinely new compatible potential occurrence, not a relabelling of an old slot.

### BDA5gi — canonical repair transversal

The first `delta` pairs of `R_P(C)` in complete arithmetic address order form a canonical transversal of distinct restoration uses and distinct outside potential slots.

### BDA5gj — arithmetic-class concentration

If the transversal incidences are partitioned into `L` exact source/gain/damping creation classes, one class contains at least `ceil(delta/L)` pairs. All primitive-potential values and restoration addresses remain explicit.

### BDA5gk — failure and resets

Fewer than `delta` distinct outside compatible slots cannot repair the core. Changed gains or damping, omitted predecessor fields, hidden potential issuance, occurrence splitting, reuse or relabelling return the first exact reset witness rather than counting as payment.

## Consequence

Every successful arithmetic repair must exhibit `delta` distinct faithful potential slots or compatibility restorations outside the old core neighbourhood. Construct them, pay them through named potential deposits, or rule the repair out.

This theorem is conditional on the complete arithmetic use/slot and repair-extension contracts. It does not prove BDA6 or the no-three-in-line conjecture.
