# Threshold replacement price frontier

`docs/587` found eight geometrically legal four-layer matrices at minimum entrywise distance six from the stored conservative source matrix. This chapter classifies the exact quotient-observable cost of those nearest replacements.

Let the aligned observables be total fixed-point occupancy and total cyclic-forward occupancy. The source matrix has observable vector

```text
(8,4).
```

## 1. Two exact replacement branches

### Theorem PP3csx -- PROVED / NEAREST-REPLACEMENT LOSS DICHOTOMY

The eight nearest legal matrices split into two classes of four:

```text
4 replacements have observable loss (2,1),
4 replacements have observable loss (3,0).
```

Every nearest replacement moves exactly three units of source-cell mass. No nearest legal matrix preserves both aligned observables.

#### Proof

Enumerate all `5985` multisets of four legal permutation layers, retain the eight matrices at distance six, and evaluate the two observable sums. The resulting loss histogram is exactly `{(2,1):4,(3,0):4}`. Distance six with conserved row and column totals consists of three unit removals and three unit insertions. ∎

## 2. Symbolic price frontier

### Theorem PP3csy -- PROVED / TWO-BRANCH NONNEGATIVE PRICE ENVELOPE

Assign a nonnegative price `alpha` to each lost unit of fixed occupancy and `beta` to each lost unit of forward occupancy. The exact minimum price among nearest legal replacements is

```text
min(2 alpha + beta, 3 alpha).
```

The two branches exchange optimality on the wall

```text
beta = alpha.
```

#### Proof

The only loss vectors are those of `PP3csx`. Taking the lower of their two linear prices gives the stated envelope. ∎

## 3. No price-free promotion

### Theorem PP3csz -- PROVED / SOURCE CHARGE STILL REQUIRED

The geometric replacement search does not by itself justify a threshold ledger row. Every nearest legal replacement loses at least two fixed units, and one branch also loses a forward unit. Promotion therefore requires a source-derived inequality or dual price assigning an admissible charge to one of the two branches.

#### Proof

The zero loss vector is absent from the exact histogram. Without source prices, the replacement changes the controlled threshold resources by an uncharged amount. ∎

## 4. Exact audit

Run

```bash
python scripts/check_threshold_replacement_price_frontier.py
```

The checker reconstructs the legal-layer search, the eight nearest matrices, all three-unit mass transports, and the symbolic two-branch price envelope.

## 5. Prime-patching consequence

Geometric legality and quotient preservation cannot both be obtained for free in the current four-layer model. The remaining threshold task is no longer to find a legal matrix, but to derive an actual residual inequality whose prices select and pay for one of the two exact branches.
