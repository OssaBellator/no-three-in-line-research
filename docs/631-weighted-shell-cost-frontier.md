# Weighted all-cycle shell cost frontier

The preferred missing shell action is `D=(1,1,1)`. The earlier active-control
frontier assumes that one use of `D` costs one ordinary active-control unit. This
chapter removes that assumption.

## Theorem PP3cxh — weighted cost envelope

Let `w` be the active-control-equivalent cost of one geometric `D` macro. The
three nondominated exact-service solutions have weighted costs

```text
12 + 2w,
9  + 4w,
6  + 6w,
```

while the recorded even-column baseline costs `15`.

## Theorem PP3cxi — sharp cost threshold

All three affine costs meet the baseline at

```text
w = 3/2.
```

For `0 <= w < 3/2`, the unique optimum uses six copies of `D` and has cost
`6+6w`. At `w=3/2`, all three frontier points and the baseline tie. For
`w>3/2`, the recorded baseline is strictly cheaper than every solution using
`D`.

## Theorem PP3cxj — geometric shell obligation

At unit cost, the all-cycle action saves three active controls and admits the
zero-buffer word from `docs/625`. A geometric realization preserves a strict
throughput gain exactly when its active-equivalent cost is below `3/2`.

Thus the missing clean macro must satisfy three simultaneous requirements:
incidence `(1,1,1)`, exposed-state legality with controlled collateral effects,
and active-equivalent cost strictly below `3/2`.
