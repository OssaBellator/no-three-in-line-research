# Spare-resource conditional Hall lemma

`docs/604` embeds the twelve quotient choices into a five-resource lift of the
stored binary-resource-star fixture.  This chapter isolates the exact structural
reason the lift is robust: after the local pair consumes two resources, the
remaining `3 x 3` host is complete and the restricted partner fibre is a partial
matching.

## 1. Matching-shaped partner fibres

### Theorem PP3cuw -- PROVED / PARTIAL-MATCHING RESIDUAL COMPLETION

Let the residual conditional host be `K_(3,3)`, and delete any partial matching
`F` from its cells.  The residual host has a perfect matching.  More precisely,
for `|F|=0,1,2,3`, the perfect-matching counts are respectively

```text
6, 4, 3, 2.
```

#### Proof

There are exactly thirty-four partial matchings in `K_(3,3)`:

```text
1 + 9 + 18 + 6 = 34.
```

The checker enumerates all of them and all six ambient perfect matchings.  The
count histogram is

```text
(0,6):1, (1,4):9, (2,3):18, (3,2):6.
```

Every residual family is nonempty. ∎

## 2. One further exclusion

### Theorem PP3cux -- PROVED / UNIFORM SINGLE-EXCLUSION ROBUSTNESS

Under the hypotheses of `PP3cuw`, deleting any one additional residual cell
still leaves a perfect matching.  Equivalently, the perfect-matching family has
cell blocker number at least two.

#### Proof

For each of the thirty-four partial matchings `F`, the checker deletes every
remaining cell in turn and re-enumerates the perfect matchings.  Every resulting
host is matchable.  The exact blocker-number histogram is

```text
|F|=0: blocker 3,
|F|=1,2,3: blocker 2.
```

Thus no single residual cell meets all completions. ∎

## 3. Source-typed fixture application

### Theorem PP3cuy -- PROVED / TWELVE-CHOICE SPARE-RESOURCE CERTIFICATE

In the best five-resource lift from `docs/604`, every one of the twelve decoded
local pairs leaves a restricted partner fibre that is a partial matching in its
residual `K_(3,3)`.  Consequently every choice survives one further residual-cell
exclusion.

The twelve choices have sixty-four conditional perfect matchings in total.  Nine
choices have six completions, one has four, and two have three.  Their blocker
numbers are nine threes and three twos.

#### Proof

The checker uses the actual six partner-fibre conflicts from
`experiments/binary-resource-star-conditioning-example.json`, the second left
resource `1`, and quotient columns `(1,2,3,4)`.  It restricts each centre fibre
after the two selected rows and columns are removed.  Every restriction has
distinct left and right coordinates, hence is a partial matching.  Apply
`PP3cuw--PP3cux` and audit the exact completion counts. ∎

## 4. Missing asymptotic condition

The finite Hall decoder now has a clean source-typed sufficient condition:

```text
one spare left resource + one spare right resource
+ matching-shaped restricted partner fibre.
```

The open step is to derive that condition from the asymptotic conditional
resource-star or superregular host, including all source and partner-fibre
exclusions.  This chapter does not assert that the spare resources are available
in every prime-patching instance.
