# Multiplicity-four completion for the radius-three support-twenty cache

PX792--PX795 close global multiplicity-four cases `2280` through `2379`. This chapter closes the final twelve cases, `2380` through `2391`, and completes the entire multiplicity-four tier.

## 1. Final exact tail

### Theorem PX796 -- PROVED FINITE

The final tail contains twelve multiplicity-four signatures and therefore 48 selectors. Every selector is infeasible in all four radix orientations.

## 2. Final clean-top census

### Theorem PX797 -- PROVED FINITE

| Column order | Clean top orders | Top-search nodes |
|---|---:|---:|
| Concatenated | 333,578 | 5,829,983 |
| Interleaved | 347,478 | 8,718,578 |
| **Total** | **681,056** | **14,548,561** |

The complete ordered final-tail transcript has deterministic digest

`5163944326560678257` (`0x47aa0401588b0171`).

## 3. Final shared bottom CSP

### Theorem PX798 -- PROVED FINITE

| Orientation | Bottom-CSP nodes |
|---:|---:|
| 0 | 479,309 |
| 1 | 579,006 |
| 2 | 599,385 |
| 3 | 423,526 |
| **Total** | **2,081,226** |

All 48 selectors terminate with an empty active mask.

## 4. Complete multiplicity-four classification

### Corollary PX799 -- PROVED CLASSIFICATION

All `2,392` multiplicity-four signatures and all

\[
2{,}392\cdot4=9{,}568
\]

selectors are now classified:

- `9,567` selectors are certified infeasible in every orientation;
- one selector—global case `1392`, selector zero—has the constructive no-three witness of PX754.

The multiplicity-four tier used exactly `748,192,356` shared rejection-CSP nodes. Across every completed higher-multiplicity tier and multiplicity four, the support-twenty cache now contains:

- `4,590` completed top-signature classes;
- `26,968` certified-infeasible selectors;
- `1` constructively witnessed selector;
- `1,486,167,944` cumulative rejection-CSP nodes;
- `44,891` selectors still unclassified.

The next exact frontier is multiplicity three, containing `3,544` signatures and `10,632` selectors.

## 5. Verification

```bash
g++ -O3 -std=c++17 \
  scripts/verify_product_side_seven_cycle52_radius_three_support_twenty_multiplicity4_final12.cpp \
  -o /tmp/m4-final12

/tmp/m4-final12
/tmp/m4-final12 2380 0
/tmp/m4-final12 2391 3
```

The complete multiplicity-four classification combines the ordinary shard verifiers, the mixed witness verifier for cases `1380` through `1479`, and this final tail verifier.
