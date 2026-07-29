# Frontier pass: mixed-radix decoration descent

## Added

- OP4bf: mixed-radix injection and lexicographic order.
- OP4bg: no strict-descent closed decoration cycle.
- OP4bh: finite strict-descent stock.
- OP4bi: monotone-decoration continuation.

## Corrected frontier

Monotone physical decoration fields terminate by finite integer descent and need no nontrivial balanced-cycle ticket. Genuinely circulating fields retain the existing finite cycle-sum audit. Remaining work is to define the actual field orders, prove monotonicity and resolve exact physical stutters.

## Verification

`scripts/verify_phase_mixed_radix_descent.py` checks product-alphabet rank injection, ordering and closed-walk descent behavior.