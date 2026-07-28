# Robust common relative terminal-normalizer cuts through `m=10`

`docs/377` shows that the single relative threshold `q=16/5` contracts at
`m=8,9,10`. This chapter proves that the certificate is not tied to that one
rational value: an exact common interval of relative thresholds selects the same
normalizer cut and retains a uniform positive contraction margin.

The result is finite. It does not prove that this interval or any fixed relative
threshold persists for larger `m`.

## 1. Stability interval for the selected observed cut

For one audited size, let `z_min` be the minimum observed normalizer, let `z_-`
be the observed normalizer immediately below the selected cut, and let `z_+` be
the selected observed normalizer. The first observed normalizer at least
`q z_min` is exactly `z_+` whenever

```text
z_-/z_min < q <= z_+/z_min.
```

### Proposition PP3btz -- PROVED / EXACT COMMON CUT-STABILITY INTERVAL

For the three exact terminal censuses, the cut-stability intervals are

| `m` | `z_min` | `z_-` | `z_+` | stability interval |
|---:|---:|---:|---:|---:|
| 8 | 1096 | 3488 | 3524 | `(436/137, 881/274]` |
| 9 | 2976 | 9520 | 9536 | `(595/186, 298/93]` |
| 10 | 9872 | 31520 | 31648 | `(1970/617, 1978/617]` |

Their exact intersection is

```text
I = (595/186, 298/93]
  = (3.19892473118..., 3.20430107527...].
```

In particular `16/5` lies strictly inside `I`. For every `q in I`, all three
sizes retain exactly the same low/high split as in `docs/377`.

#### Proof

The first-observed-threshold rule selects `z_+` precisely after `q z_min` has
passed `z_-` and before it passes `z_+`. Intersecting the three displayed
intervals gives the maximum lower endpoint `595/186` and the minimum upper
endpoint `298/93`. Direct cross multiplication gives

```text
595/186 < 16/5 < 298/93.
```

∎

## 2. Uniform contraction throughout the interval

For the fixed split at size `m`, write its low and high populations as `L_m` and
`H_m`. The dimensionless relaxed envelope at relative threshold `q` is

```text
E_m(q) = [L_m + H_m/q]/z_min(m).
```

It is strictly decreasing in `q`.

### Theorem PP3bua -- PROVED / VERIFIED FINITELY / ROBUST COMMON INTERVAL

For every `q in I`, the exact split populations remain

```text
m=8:  L=432,  H=1152;
m=9:  L=1024, H=6144;
m=10: L=896,  H=7168.
```

Consequently

```text
E_8(q)  < 58914/81515  = 0.72273814635...,
E_9(q)  < 54752/55335  = 0.98946417277...,
E_10(q) < 16664/52445  = 0.31774239680....
```

The strict inequalities use the open lower endpoint of `I`. Uniformly over all
three sizes and all `q in I`,

```text
E_m(q) < 54752/55335 < 1,
```

with common margin

```text
1 - 54752/55335 = 583/55335.
```

#### Proof

The split is constant on `I` by `PP3btz`. Since each `E_m(q)` decreases in `q`,
its supremum on the interval is the limit as `q` decreases to `595/186`. Exact
substitution gives the three displayed fractions. The `m=9` value is the
largest, and its difference from one is `583/55335`. ∎

## 3. Structural consequence

### Corollary PP3bub -- PROVED / VERIFIED FINITELY / THRESHOLD ROBUSTNESS

The common-scale terminal certificate is robust under a nonzero interval of
threshold perturbations. The finite contraction is therefore not an arithmetic
coincidence at exactly `q=16/5`.

A useful asymptotic target is now stronger and cleaner than existence of one
finely tuned threshold: prove that some fixed interval `(q_-,q_+]`, independent
of `m`, preserves a low/high split satisfying

```text
[L_eta(q) + H_eta(q)/q]/z_min < 1
```

uniformly over terminal targets. The present audit proves this only for
`m=8,9,10` and the interval `I` above.

Verify the exact arithmetic with

```bash
python scripts/verify_terminal_normalizer_relative_cut_robustness.py .
```

The next theorem identifier after this chapter is `PP3buc`.
