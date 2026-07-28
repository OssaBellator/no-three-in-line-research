# Minimal terminal normalizer scale resolution through `m=10`

`docs/371` keeps all dyadic normalizer-bin populations attached to the same
target and thereby restores terminal contraction at `m=9`. This chapter asks how
many of those scales are actually necessary.

No asymptotic bounded-scale theorem is claimed.

## 1. Contiguous coarsening

Let the fine normalizer bins be

```text
I_j=[L_j,U_j],  1<=j<=r,
```

and let `b_j(eta)` be the incoming-label population of target `eta` in fine bin
`j`. A contiguous coarsening partitions `1,...,r` into consecutive segments.
For a segment beginning at fine bin `a`, all labels in that segment are bounded
using the lower edge `L_a`.

### Proposition PP3btk -- PROVED / COARSENING AND REFINEMENT

For a contiguous partition `P`, define

```text
E_P(eta)
 = sum_{segments S in P} (sum_{j in S} b_j(eta))/L_{min S}.
```

Then

```text
kappa_F(eta) <= E_P(eta).
```

Moreover, refining a partition weakly decreases `E_P(eta)` for every target.
Consequently the optimal worst-target envelope among partitions with `k`
segments is nonincreasing in `k`.

#### Proof

Every label in a segment beginning at `a` has normalizer at least `L_a`, giving
the displayed bound. If a segment is split, the new upper subsegment is divided
by a lower edge at least as large as the old one, while all other terms are
unchanged. Thus refinement cannot increase the envelope. ∎

## 2. Exact best coarsenings

### Theorem PP3btl -- VERIFIED FINITELY / COMPLETE CONTIGUOUS-COARSENING AUDIT

The checker enumerates every contiguous coarsening of the dyadic bins from
`docs/371`, maximizes its envelope over target cycles exactly, and then chooses
the best partition at each segment count.

### `m=8`

| segments | best worst-target envelope | decimal | contractive |
|---:|---:|---:|---:|
| 1 | `218/137` | `1.591240876...` | no |
| 2 | `390310/561289` | `0.695381524...` | yes |
| 3 | `203200918/383360387` | `0.530051943...` | yes |

The best two-segment partition merges the first two fine bins and keeps the
highest bin separate:

```text
[1096,4096], [4097,8192].
```

### `m=9`

| segments | best worst-target envelope | decimal | contractive |
|---:|---:|---:|---:|
| 1 | `1429/496` | `2.881048387...` | no |
| 2 | `279706/253983` | `1.101278432...` | no |
| 3 | `3478755928/4161511455` | `0.835935685...` | yes |
| 4 | `148937290752/183330241195` | `0.812398924...` | yes |

The best three-segment partition is

```text
[2976,8192], [8193,16384], [16385,32768].
```

Thus two scales are still insufficient at `m=9`, but the two lowest dyadic bins
may be merged without losing contraction.

### `m=10`

| segments | best worst-target envelope | decimal | contractive |
|---:|---:|---:|---:|
| 1 | `560/617` | `0.907617504...` | yes |
| 2 | `6257720/20218473` | `0.309505075...` | yes |
| 3 | `348002942008/1325058065001` | `0.262632221...` | yes |
| 4 | `7972033929088/35188130299905` | `0.226554633...` | yes |

The one-segment certificate is simply

```text
maximum raw incoming labels / minimum normalizer
 = 8960/9872
 = 560/617
 < 1.
```

#### Verification

The regeneration harness instruments the already committed exact correlated-bin
checker in a temporary directory. For each contiguous partition, it changes only
the bin boundaries, recompiles warning-clean, runs the complete terminal shell
census, and records the exact worst-target correlated envelope. The default mode
checks the committed ledger arithmetic and monotonicity. ∎

## 3. Minimum scale resolution

### Corollary PP3btm -- PROVED / VERIFIED FINITELY / SCALE-RESOLUTION PROFILE

The minimum numbers of contiguous normalizer segments needed to certify terminal
contraction are

```text
m=8:  2,
m=9:  3,
m=10: 1.
```

The profile is not monotone in `m`. At `m=9`, cross-scale structure remains
essential; at `m=10`, the growth of the minimum normalizer alone dominates the
complete reverse multiplicity.

This gives a sharper asymptotic target than preserving every dyadic scale. It is
enough to prove that some bounded or summably weighted contiguous coarsening has
worst-target envelope below one. The finite data also warn that a universal
one-scale argument cannot simply be extrapolated backward through the first
nonforest sizes.

Verify the committed ledger, or regenerate it from the existing exact
correlated-bin implementation, with

```bash
python scripts/check_terminal_normalizer_coarsening_profile.py .

python scripts/check_terminal_normalizer_coarsening_profile.py . \
  --regenerate --threads 8 \
  --output /tmp/terminal-normalizer-coarsening.json
```

The next theorem identifier after this chapter is `PP3btn`.
