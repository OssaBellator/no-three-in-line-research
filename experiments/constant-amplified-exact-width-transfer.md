# Constant-amplified exact-width prime-transfer diagnostic

Run

```text
python scripts/check_constant_amplified_exact_width_transfer.py \
  experiments/constant-amplified-exact-width-transfer-example.json
```

The stored constants use controller-domain density `gamma=0.2` and request leading
patch coefficient three.  The explicit choice from PP3awq is

```text
a=115200,
b=4.340277777777778e-06,
ab=0.5.
```

It recovers

```text
a gamma sqrt(b)/16=3.
```

For the exact-width check, twenty macros of maximum width 10,000 must realize total
width 175,000.  The balanced decomposition uses eighteen macros:

```text
[9723, 9723, 9723, 9723,
 9722, 9722, 9722, 9722, 9722, 9722, 9722,
 9722, 9722, 9722, 9722, 9722, 9722, 9722].
```

Every local width remains between one third of the maximum and the maximum.  The
heterogeneous Ore slack is approximately

```text
14352.864576995198,
```

only `0.08201636901140114` of the target width.

At `x=10^12`, the shifted backward-prime construction uses the exact patch band

```text
1995262.3149688807
<=t<=
3990522.5398741257,
```

whose endpoint ratio is `1.9999989524867883`.  Thus a coefficient larger than two
covers the whole shifted band without requiring small-width patches.

The expected output is

```text
gamma 0.2
target leading coefficient 3.0
slab constants a b [115200.0, 4.340277777777778e-06]
slab density ab 0.5
recovered coefficient 3.0
available macros 20
active macros 18
maximum macro width 10000
target exact width 175000
heterogeneous widths [9723, 9723, 9723, 9723, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722, 9722]
minimum and maximum widths [9722, 9723]
heterogeneous Ore slack 14352.864576995198
slack to target ratio 0.08201636901140114
prime shift x 1000000000000.0
shift lower width 1995262.3149688807
shift upper width 3990522.5398741257
upper to lower ratio 1.9999989524867883
outcome constant_amplified_exact_width_prime_transfer
```

This verifies the numerical identities in PP3awq--PP3awu and the shifted full-scale
band in PP3awx.
