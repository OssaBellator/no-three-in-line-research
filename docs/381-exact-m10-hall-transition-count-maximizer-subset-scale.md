# Exact Hall-subset scale profile of the `m=10` transition count maxima

`docs/373` resolves the intermittent inverse-support transition by compatible
source count, while `docs/378` shows that most individual violations are created
by proper Hall subsets. This chapter asks a narrower structural question:

> At each nonempty source count, how large is the Hall subset witnessing that
> count's exact worst charge?

The audit uses the deterministic count-level maximizers already recorded in
`experiments/m10-hall-support-count-profile-106-399-audit.json`. It is finite.
It does not classify all 284 flaws by subset size and does not prove an
asymptotic small-subset theorem.

## 1. Exact count-maximizer subset-size census

For each nonempty compatible-source count `s` in `209--287`, let `f_s` be the
deterministically selected flaw attaining the exact maximum

```text
A_s = max_{f:s(f)=s} s gamma(f),
```

and let `k_s` be the size of the maximizing source subset returned by the exact
Dinkelbach/min-cut computation for `f_s`.

### Theorem PP3buf -- VERIFIED FINITELY / EXACT SUBSET-SIZE PROFILE

There are 43 nonempty source counts and 13 count-level constant-one violations.
The exact subset-size histogram is

| `k_s` | count maxima | violating count maxima | largest `A_s` at this size | maximizing `s` |
|---:|---:|---:|---:|---:|
| 1 | 11 | 1 | `4544/4315` | 284 |
| 2 | 7 | 3 | `1984/1563` | 248 |
| 3 | 5 | 3 | `564/445` | 282 |
| 4 | 3 | 1 | `2288/1957` | 286 |
| 5 | 1 | 0 | `3136/4689` | 224 |
| 6 | 2 | 1 | `6744/6383` | 281 |
| 7 | 1 | 0 | `6600/7361` | 275 |
| 8 | 1 | 0 | `8352/10567` | 261 |
| 11 | 1 | 0 | `46464/52597` | 264 |
| 13 | 2 | 0 | `12350/13743` | 247 |
| 14 | 1 | 0 | `3159/3677` | 243 |
| 17 | 1 | 0 | `393/508` | 262 |
| 27 | 2 | 1 | `41768/39613` | 227 |
| 29 | 1 | 1 | `45980/45691` | 209 |
| 40 | 1 | 0 | `50932/66553` | 214 |
| 49 | 1 | 0 | `41220/59507` | 229 |
| 85 | 1 | 1 | `14076/11845` | 276 |
| 124 | 1 | 1 | `51152/38383` | 278 |

The thirteen violating count maxima are exactly

| `s` | `k_s` | `A_s` | subset supply | reached capacity |
|---:|---:|---:|---:|---:|
| 209 | 29 | `45980/45691` | 3,520 | 731,056 |
| 215 | 3 | `3440/3321` | 384 | 79,704 |
| 227 | 27 | `41768/39613` | 2,944 | 633,808 |
| 234 | 2 | `234/193` | 256 | 49,408 |
| 248 | 2 | `1984/1563` | 256 | 50,016 |
| 272 | 3 | `3264/2893` | 384 | 92,576 |
| 276 | 85 | `14076/11845` | 9,792 | 2,274,240 |
| 278 | 124 | `51152/38383` | 13,248 | 2,763,576 |
| 280 | 2 | `4480/3781` | 256 | 60,496 |
| 281 | 6 | `6744/6383` | 384 | 102,128 |
| 282 | 3 | `564/445` | 384 | 85,440 |
| 284 | 1 | `4544/4315` | 128 | 34,520 |
| 286 | 4 | `2288/1957` | 512 | 125,248 |

#### Verification

The verifier reads the already committed exact source-count ledger, filters the
43 rows in `209--287`, recomputes the constant-one comparison by exact rational
arithmetic, and checks every subset size, supply, capacity, and histogram entry
against the compact machine ledger added with this chapter. ∎

## 2. Microscopic dominance with two mesoscopic islands

### Corollary PP3bug -- PROVED / VERIFIED FINITELY / TWO-SCALE OBSTRUCTION

Among the thirteen violating count maxima,

```text
7 have k_s <= 3,
9 have k_s <= 6.
```

The remaining four have subset sizes

```text
27, 29, 85, 124.
```

In particular there is no violating count maximum with

```text
7 <= k_s <= 26
```

and none with

```text
30 <= k_s <= 84.
```

The coarse profile is

| subset-size band | count maxima | violations | violation fraction |
|---|---:|---:|---:|
| `1` | 11 | 1 | `1/11` |
| `2--3` | 12 | 6 | `1/2` |
| `4--6` | 6 | 2 | `1/3` |
| `7--26` | 7 | 0 | `0` |
| `27--29` | 3 | 2 | `2/3` |
| `30--84` | 2 | 0 | `0` |
| `85+` | 2 | 2 | `1` |

Thus the finite transition is not governed by a monotone subset-size threshold.
It has a microscopic family, a gap, a narrow `27--29` island, another gap, and
two large-subset witnesses.

## 3. Proper-subset scale and the revised Hall split

### Corollary PP3buh -- PROVED / VERIFIED FINITELY / STRICTLY SUBHALF WITNESSES

Every violating count maximum is witnessed by fewer than half of its compatible
sources. The largest observed fraction is

```text
124/278 = 62/139 < 1/2.
```

The maximum occurs at the global transition-window count maximizer `s=278`.
The inequality is the exact cross multiplication

```text
2 * 124 = 248 < 278.
```

Subset size alone is nevertheless insufficient. Sizes `1`, `2`, `3`, `4`, `6`,
and `27` each occur for both violating and nonviolating count maxima. The
one-source deficit and the pair/triple overlap mechanisms from `docs/380` are
therefore necessary but not sufficient statistics.

The finite evidence suggests a proof split:

1. control singleton through six-source subsets by one-source capacity,
   pairwise overlap, and a bounded amount of higher-order inclusion-exclusion;
2. treat the separated mesoscopic scales by expansion or heat-kernel estimates.

This is a structural target only. The chapter does not show that all individual
violating flaws have small maximizing subsets, nor that the two observed gaps
persist for larger `m`.

Verify with

```bash
python scripts/verify_m10_hall_transition_count_maximizer_subset_scale.py .
```

The next theorem identifier after this chapter is `PP3bui`.
