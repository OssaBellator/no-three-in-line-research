# Orbit phase: zero-drift physical residual transportation

## Scope

This note records OP4bm--OP4bq. Once prime valuations, finite unit classes, and holonomy all return, the remaining payment problem is finite provided every physical residual and every payment source is retained.

Let `R` be the finite set of exact zero-drift physical residual classes and `S` the finite set of payment-source classes. Residual `r` has demand `c_r>=0`; source `s` has capacity `d_s>=0`. A compatibility edge `r~s` means source `s` can absorb residual `r` without changing any retained blocker, action, boundary, unit, valuation, or holonomy field.

## OP4bm: integral transport network

The maximum payable residual mass is the maximum integral flow in the network with source-to-residual capacity `c_r`, infinite compatibility edges, and payment-source-to-sink capacity `d_s`.

## OP4bn: capacitated Hall criterion

All zero-drift physical residuals are payable if and only if every subset `X subseteq R` satisfies

`sum_{r in X} c_r <= sum_{s in N(X)} d_s`.

## OP4bo: exact unpaid residual mass

The unpaid mass is exactly

`max_X (sum_{r in X} c_r - sum_{s in N(X)} d_s)_+`.

This retains a complete residual subset and all physically compatible source classes.

## OP4bp: canonical residual cut

Choose the least maximizing subset in a fixed residual ordering. The resulting cut is a finite exact obstruction address after the valuation, unit, and holonomy clocks have returned.

## OP4bq: omitted-field reset

If compatibility depends on an omitted action variable, blocker atom, boundary field, unit-sensitive legality datum, or a dynamically created source class, the event is returned as a residual-transport reset rather than counted as payment.

## Remaining frontier

The theorem reduces the zero-drift physical endpoint to concrete residual/source capacities and compatibility. Proving those estimates, the multiplicative-deposit inequality, and bounded width for the actual action CSP remains open. OP5 and the no-three-in-line conjecture are not proved.