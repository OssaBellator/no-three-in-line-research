# Global mass versus proper-subset localization in the `m=10` Hall transition

`docs/373` locates the constant-one transition by compatible-source count, and
`docs/376` shows that prescribed-arc connectivity does not determine it.  This
chapter separates the transition into full-neighbourhood overload and genuinely
localized Hall-cut overload.

The audit covers the complete intermittent source-count window `209--287`.  It
is finite and does not prove a uniform Hall-localization theorem.

## 1. Exact multiplicative decomposition

For a supported flaw `f`, let

```text
s(f)     = compatible clean source-cycle count,
W_f      = total source supply over all compatible sources,
V_f      = total clean-fibre capacity of the full reached target neighbourhood,
gamma(f) = exact optimal weighted-Hall charge.
```

Define

```text
A(f)      = s(f) gamma(f),
G(f)      = s(f) W_f/V_f,
Lambda(f) = gamma(f)/(W_f/V_f).
```

### Proposition PP3btw -- PROVED / GLOBAL-LOCAL HALL FACTORIZATION

For every supported flaw,

```text
A(f) = G(f) Lambda(f).
```

Moreover `Lambda(f)>=1`, with strict inequality exactly when a proper source
subset improves on the full-source ratio.

#### Proof

The displayed identity is algebraic.  The full compatible source family is an
admissible Hall subset, so `gamma(f)>=W_f/V_f`.  Equality holds precisely when
the full family is optimal. ∎

This yields two distinct kinds of constant-one violation:

```text
global-mass violation:        G(f)>1;
proper-subset-only violation: G(f)<=1 but A(f)>1.
```

## 2. Complete transition-window decomposition

### Theorem PP3btx -- VERIFIED FINITELY / LOCALIZATION DOMINATES THE TRANSITION

The source-count window `209--287` contains 284 supported signed flaws.  All 284
have proper Hall bottlenecks.  Their constant-one classification is exactly:

| class | signed flaws | fraction of all 284 | fraction of the 68 violations |
|---|---:|---:|---:|
| global-mass violations | 8 | `2/71` | `2/17` |
| proper-subset-only violations | 60 | `15/71` | `15/17` |
| nonviolations | 216 | `54/71` | -- |

Thus 60 of the 68 constant-one failures are invisible at the full-neighbourhood
ratio and are created only by a proper Hall subset.

The decomposition by prescribed-arc type is:

| prescribed-arc type | signed flaws | all violations | global-mass violations | proper-subset-only violations |
|---|---:|---:|---:|---:|
| directed three-edge path | 40 | 8 | 4 | 4 |
| two-edge path plus one arc | 124 | 20 | 4 | 16 |
| three disjoint arcs | 120 | 40 | 0 | 40 |

In particular, every constant-one violation among the three-disjoint-arc flaws
is a localization phenomenon: their full reached target capacity is sufficient,
but a small source subset sees too little of it.

The exact largest full-neighbourhood normalized ratio is

```text
max G(f) = 713904/596453 = 1.1969157670...,
```

at source count 278.  Its optimal charge gives

```text
A(f) = 51152/38383 = 1.3326733189...,
Lambda(f) = 13718419/12320943 = 1.1134228119... .
```

The strongest proper-subset-only violation is instead

```text
A(f) = 1984/1563 = 1.2693538068...
```

at source count 248 with three disjoint prescribed arcs.  Its full-neighbourhood
ratio remains below one,

```text
G(f) = 556264/786391,
```

but a two-source Hall subset has supply 256 and capacity 50,016.

#### Verification

The warning-clean checker reconstructs every `m=10` Hamilton cycle, parity-clean
fibre, compatible source family, owner-intersecting clean target neighbourhood,
and exact Dinkelbach/min-cut optimum for all flaws in `209--287`.  For each flaw
it records full source supply, full reached capacity, optimal Hall ratio, source
subset witness, target count, and neighbourhood degree data.  Complement partners
are counted separately.  The displayed totals and extrema are hard-coded
regressions. ∎

## 3. Neither global mass nor localization factor alone suffices

### Corollary PP3bty -- PROVED / VERIFIED FINITELY / TWO-FACTOR OBSTRUCTION

The largest localization factor among proper-subset-only violations is

```text
Lambda(f) = 46304896/23735187 = 1.9508966161...
```

at source count 215.  Here

```text
G(f) = 1536605/2894056,
A(f) = 3440/3321 > 1,
```

and the maximizing Hall subset has three sources.

However the largest localization factor in the entire transition window is even
larger,

```text
Lambda(f) = 1500597/656230 = 2.2866936897...,
```

at source count 222, while

```text
A(f) = 111/137 < 1.
```

Therefore neither `G(f)` nor `Lambda(f)` alone classifies the transition.  Their
product is decisive, and controlling that product requires information about how
source weight is distributed across proper subsets of the weighted clean-target
neighbourhood.

This sharpens the structural Hall frontier: source support and prescribed-arc
connectivity must be supplemented by a localized weighted-expansion estimate,
not merely a full-neighbourhood capacity lower bound.

Reproduce or verify with

```bash
python scripts/check_m10_hall_transition_localization.py .

python scripts/check_m10_hall_transition_localization.py . \
  --regenerate --threads 8 \
  --output /tmp/m10-hall-transition-localization.json
```

The next theorem identifier after this chapter is `PP3btz`.
