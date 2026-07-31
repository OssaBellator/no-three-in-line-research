# Nonprecancelled shell incidence benchmark

`docs/559` showed that the shell fixture in `docs/553` cancels before the
incidence map is applied.  This chapter uses the independently stored service
multiset from `docs/529` and applies a full-rank incidence map to a genuinely
nonzero residual word.

The component service multiset is

```text
A,A,B,B,C
```

with target rate `(2/5,2/5,1/5)`.  Define three physical reserve coordinates:

```text
R_0 = A+C service,
R_1 = B+C service,
R_2 = A+B service.
```

The incidence matrix is therefore

```text
I=((1,0,1),
   (0,1,1),
   (1,1,0)).
```

## 1. Full-rank nonprecancelled image

### Theorem PP3cpr -- PROVED / NONZERO PHYSICAL SHELL TRAJECTORY

The matrix `I` has determinant `-2`, hence rank three.  Every individual service
residual has a nonzero physical image, and the selected period contains nonzero
physical increments before its total returns to zero.

#### Proof

The determinant is direct.  Applying `I` to each of

```text
e_A-r, e_B-r, e_C-r
```

gives a nonzero vector.  Their multiset sum is zero because the period has the
target multiplicities. ∎

## 2. Exact physical order optimization

### Theorem PP3cps -- PROVED / FULL-RANK SHELL ORDER CENSUS

Among all thirty distinct orders of `A,A,B,B,C`, the minimum physical `l_1`
startup reserve is `6/5`.  Exactly ten words attain it.  The lexicographically
first optimum is

```text
ABABC
```

with physical startup buffer

```text
(2/5,4/5,0).
```

Repeating this period preserves nonnegative reserve for every truncation.

#### Proof

For each word, accumulate its physical centered increments and take the negative
coordinatewise prefix minima.  Exact enumeration of the thirty multiset words
gives the optimum and multiplicity.  A complete period has zero net residual, so
the same prefix table certifies every repetition. ∎

## 3. Benchmark completeness and geometric gap

### Theorem PP3cpt -- PROVED / IDENTIFIABLE SHELL BENCHMARK

For the displayed benchmark, the physical resources, incidence entries,
component residuals, prefix trajectory, startup reserve, rank, and nullspace are
all independently reconstructible.  Nevertheless this does not identify the
true prime-patching shell system because no repository map equates these three
resources with the geometric shell incidences.

#### Proof

The first statement follows from `PP3cpr--PP3cps` and the exact checker.  The
second is a provenance statement: the benchmark resource definitions are new
and no source path to the geometric shell construction is supplied. ∎

## 4. Stored exact audit

Run

```bash
python scripts/check_nonprecancelled_shell_incidence.py
```

The checker verifies rank, nonzero slot images, all thirty orders, the ten
optima, and five hundred repeated physical prefixes.

## 5. Prime-patching consequence

The shell adapter is now tested on a nondegenerate, identifiable finite model.
The remaining work is not another phase optimizer; it is extracting the actual
component-to-resource incidence map and feeding it through the same exact
reserve computation.
