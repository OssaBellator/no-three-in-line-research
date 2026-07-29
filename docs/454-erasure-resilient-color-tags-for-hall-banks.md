# Erasure-resilient color tags for Hall banks

`docs/448` makes every residual Hall action private by retaining its proper edge color. This chapter quantifies what survives when a short color tag is partly erased by later clean-up operations.

Let a residual bipartite action graph have a proper edge coloring `c(e)`. Each color is encoded by a word

```text
kappa(c) in A^m.
```

The final target retains its geometric endpoint and some subset of the code coordinates.

## 1. Exact partially observed column load

### Theorem PP3ccw -- PROVED / PARTIAL-TAG COLUMN FORMULA

Let source `x` choose uniformly among its `d_x` residual actions. For an observed coordinate set `J` and observed word `a`, the reverse load at terminal `(y,a)` is exactly

```text
sum_(e=(x,y): kappa(c(e))|_J=a) 1/d_x.
```

#### Proof

Every retained action contributes its source probability `1/d_x`. Proper edge coloring ensures that a color occurs at most once at a fixed endpoint, but no further relaxation is needed for the displayed identity. ∎

## 2. List ambiguity after erasures

For `e>=0`, define `L_e` as the largest number of colors incident with one target that become identical after deleting at most `e` code coordinates.

### Theorem PP3ccx -- PROVED / ERASURE-LIST LOAD

If every source has residual degree at least `d`, then after at most `e` erased coordinates,

```text
lambda<=L_e/d.
```

#### Proof

At one observed terminal there are at most `L_e` compatible incident colors. Each comes from at most one edge at that target and contributes at most `1/d`. Apply `PP3ccw`. ∎

The theorem also applies when the erased coordinate set depends on the final geometric target.

## 3. Distance gives exact privacy

### Theorem PP3ccy -- PROVED / DISTANCE-PROTECTED COLOR RECOVERY

If the color code has minimum Hamming distance `delta`, then every pattern of at most `delta-1` erasures leaves each color uniquely recoverable. Consequently

```text
L_e=1 and lambda<=1/d       for e<delta.
```

#### Proof

Two distinct codewords differ in at least `delta` coordinates. Erasing fewer than `delta` coordinates cannot remove every disagreement. Proper edge coloring then leaves at most one compatible edge at each target. ∎

This turns color retention into a standard finite coding problem: geometric work need only realize a few robust marker coordinates, not one indivisible color label.

## 4. Exact audit

Run

```bash
python scripts/check_erasure_resilient_hall_colors.py
```

The audit uses the degree-three graph `K_(4,4)` minus a perfect matching and a binary length-three color code of distance two. It verifies exact load `1/3` after any one erasure and exact worst-case load `2/3` after two erasures.
