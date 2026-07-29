# Exact source-mass and capacity-deficit profile of the `m=10` Hall transition maxima

`docs/381` classifies the exact count-level Hall maximizers by maximizing-subset
cardinality. This chapter resolves the second scalar carried by those subsets:
their total source supply and the reached-capacity deficit responsible for the
constant-one failure.

The audit is finite and concerns only the thirteen violating count maxima, not all
68 violating flaws.

## 1. Capacity-deficit identity

For a violating count maximizer at compatible-source count `s`, let

```text
k = maximizing Hall-subset size,
W = total source supply on that subset,
V = capacity of its reached target neighbourhood,
A_s = s W/V.
```

Define

```text
Delta = sW-V.
```

### Proposition PP3bvm -- PROVED / EXACT DEFICIT FORM

For every violating count maximizer,

```text
A_s = 1 + Delta/V,
```

and constant-one failure is equivalent to `Delta>0`.

#### Proof

This is the identity `sW/V=(V+Delta)/V`. ∎

Thus the amount by which the inverse-support constant one fails is exactly the
relative reached-capacity deficit `Delta/V`.

## 2. Exact thirteen-row profile

### Theorem PP3bvn -- VERIFIED FINITELY / SOURCE-MASS DEFICIT CENSUS

The thirteen violating count maxima have the following exact data:

| `s` | `k` | mean source mass `W/k` | capacity deficit `Delta=sW-V` | normalized deficit `Delta/V=A_s-1` |
|---:|---:|---:|---:|---:|
| 209 | 29 | `3520/29` | 4,624 | `289/45691` |
| 215 | 3 | `128` | 2,856 | `119/3321` |
| 227 | 27 | `2944/27` | 34,480 | `2155/39613` |
| 234 | 2 | `128` | 10,496 | `41/193` |
| 248 | 2 | `128` | 13,472 | `421/1563` |
| 272 | 3 | `128` | 11,872 | `371/2893` |
| 276 | 85 | `576/5` | 428,352 | `97/515` |
| 278 | 124 | `3312/31` | 919,368 | `12769/38383` |
| 280 | 2 | `128` | 11,184 | `699/3781` |
| 281 | 6 | `64` | 5,776 | `361/6383` |
| 282 | 3 | `128` | 22,848 | `119/445` |
| 284 | 1 | `128` | 1,832 | `229/4315` |
| 286 | 4 | `128` | 21,184 | `331/1957` |

Every displayed fraction and integer is derived by exact arithmetic from the
committed count-maximizer ledger.

Among the nine microscopic witnesses with `k<=6`, eight have mean source mass
exactly `128` and one has mean source mass exactly `64`. The strongest microscopic
failure is

```text
s=248, k=2, Delta/V=421/1563.
```

The strongest overall failure is the large-subset witness

```text
s=278, k=124, Delta/V=12769/38383.
```

All thirteen mean source masses lie in the narrow interval `[64,128]`, despite
subset cardinalities ranging from one to 124.

#### Verification

The verifier reads the compact ledger, checks `W/k`, recomputes `Delta=sW-V`, and
checks `Delta/V` and both extrema using exact `Fraction` arithmetic. ∎

## 3. Structural consequence

### Corollary PP3bvo -- PROVED / VERIFIED FINITELY / CAPACITY-REUSE FRONTIER

For the count-level transition maxima, source-mass scale varies by at most a
factor two, while Hall-subset size varies by a factor 124 and normalized deficits
vary from `289/45691` to `12769/38383`.

Therefore the finite transition cannot be attributed to an unbounded source-mass
scale. At microscopic subset sizes the concrete task is to prove enough reached
capacity per unit source mass; for pairs this is exactly the overlap inequality of
`PP3bud`. At the separated mesoscopic scales, the relevant quantity is capacity
reuse or scaled overlap congestion, as in `docs/389`.

This does not prove that individual source weights inside each maximizing subset
are equal, nor that the mean-mass interval persists beyond `m=10`.

Verify with

```bash
python scripts/verify_m10_hall_transition_count_maximizer_source_mass.py .
```

The next theorem identifier after this chapter is `PP3bvp`.
