# Exact `m^3` weighted-Hall scale through `m=10`

The complete exact transport ledgers now cover every supported atomic signed
assignment flaw for `4 <= m <= 10`. This chapter places their optimal charges on
the proposed cubic scale.

The result is finite. It does not prove a uniform asymptotic `O(m^-3)` theorem.

## 1. Exact scaled ledger

Let `gamma_m` be the largest exact weighted-Hall charge over all supported
atomic signed-assignment flaws at size `m`.

### Theorem PP3bss -- VERIFIED FINITELY / COMPLETE SCALED LEDGER

For `4 <= m <= 10`, the exact values are

| `m` | `gamma_m` | `m^3 gamma_m` | decimal scaled value |
|---:|---:|---:|---:|
| 4 | `1/24` | `8/3` | `2.666666666667...` |
| 5 | `1/37` | `125/37` | `3.378378378378...` |
| 6 | `4/215` | `864/215` | `4.018604651163...` |
| 7 | `12/931` | `84/19` | `4.421052631579...` |
| 8 | `1/93` | `512/93` | `5.505376344086...` |
| 9 | `223/29271` | `54189/9757` | `5.553858768064...` |
| 10 | `2397/349898` | `1198500/174949` | `6.850567879782...` |

#### Verification

The verifier reads the complete compressed `m<=9` ledger and the complete
`m=10` summary. It reconstructs every displayed rational exactly and checks the
source files' completion flags. ∎

## 2. Finite monotonicity of the scaled extrema

### Corollary PP3bst -- VERIFIED FINITELY / STRICTLY INCREASING SCALED SEQUENCE

The seven exact scaled extrema satisfy

```text
4^3 gamma_4 < 5^3 gamma_5 < ... < 10^3 gamma_10.
```

#### Verification

The verifier compares each adjacent pair by exact rational cross
multiplication. ∎

This strengthens the earlier observation that the scaled data do not decrease
from `m=9` to `m=10`: over the complete audited interval they increase at every
size. This is finite evidence only and is not a claim about later sizes.

## 3. A clean finite cubic envelope

### Corollary PP3bsu -- PROVED / VERIFIED FINITELY / SEVEN-OVER-CUBIC ENVELOPE

For every audited size `4 <= m <= 10`,

```text
gamma_m < 7/m^3.
```

The smallest margin occurs at `m=10`, where

```text
7 - 10^3 gamma_10
 = 7 - 1198500/174949
 = 26143/174949
 > 0.
```

#### Proof

The scaled sequence is strictly increasing, so its maximum is the `m=10`
entry. The displayed positive margin proves that entry is below seven, hence
all earlier entries are also below seven. ∎

Thus the complete finite data through `m=10` are consistent with a cubic scale
and admit the simple constant seven. They also show that any constant inferred
only from these finite extrema must be at least
`1198500/174949 = 6.850567...`. The remaining task is structural weighted
expansion or a heat-kernel substitute, not additional `m=10` computation.

Verify the ledger with

```bash
python scripts/verify_weighted_hall_m_cubed_scale_through_m10.py .
```

The next theorem identifier after this chapter is `PP3bsv`.
