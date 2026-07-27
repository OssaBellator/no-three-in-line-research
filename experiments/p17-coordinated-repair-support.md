# Exact p=17 coordinated-repair support census

Compile and run:

```bash
g++ -O3 -std=c++17 \
  scripts/check_p17_coordinated_repair_support.cpp \
  -o /tmp/check_p17_repair
/tmp/check_p17_repair \
  experiments/p17-coordinated-repair-support-example.json
```

The input is the one-defect state of PP3bdw.  Both layers are individually
no-three and their union has the unique bad triple

```text
(1,11), (3,10), (13,5).
```

For every total two-sided assignment support through seven, the checker
enumerates every support subset and every derangement of the old values on that
support.  After the logically necessary filter that at least one point of the
bad triple moves, the exact candidate counts are:

```text
support 4:      4,845
support 5:    109,550
support 6:  2,459,240
support 7: 44,402,358
             ----------
total:     46,975,993
```

No candidate is a saturated no-three seed.  Combined with the exact one-layer
nonextension result PP3bdw, this proves that every repair of this labelled
near-state changes at least eight assignment positions.

The stored valid `p=17` certificate differs in 29 assignment positions, giving

```text
8 <= minimum labelled repair support <= 29.
```

This is a finite repair-radius result for one audited state.  It is not a
uniform repair theorem and does not prove the asymptotic seed conjecture.