# Deterministic non-affine side-ten recursion sample

PX970 rules out every affine column pair for the side-ten all-transposition
relative class, even with arbitrary row labeling and arbitrary spanning
degree-two selector. The remaining fixed-template space is genuinely non-affine
and too large for direct exhaustion. This chapter records a deterministic exact
sample to calibrate that frontier.

This is an experiment, not an obstruction theorem.

## 1. Sampling rule

Use `SplitMix64` with a fixed seed and an explicit descending Fisher--Yates
shuffle. Reject a draw whenever either sampled column permutation belongs to the
40-element affine group `A_10`. Every accepted geometry therefore has both
column maps genuinely non-affine.

For each accepted pair `(T,Q)`, run the exact PX972 row-pattern solver. The solver
still includes:

- every second-row labeling `P in S_10`;
- every spanning degree-two selector;
- every scalar integer-determinant constraint.

Thus each sampled geometry is decided exactly; only the selection of geometries
is nonexhaustive.

## 2. Replayed sample

The committed sample contains 250 geometries in each orientation:

| Orientation | Seed | Accepted geometries | Search nodes | Maximum nodes |
|---|---:|---:|---:|---:|
| `cc` | 101 | 250 | 6,379,764 | 162,281 |
| `cf` | 202 | 250 | 4,982,669 | 116,189 |
| `fc` | 303 | 250 | 13,423,505 | 1,314,865 |
| `ff` | 404 | 250 | 6,961,172 | 474,867 |
| **Total** | -- | **1,000** | **31,747,110** | **1,314,865** |

No sampled geometry contains a no-three degree-two state.

An additional exploratory local batch tested another 1,000 exact non-affine
geometries without a witness. Those extra runs are not part of the committed
replay object and are not used for any formal claim.

## 3. Interpretation

The experiment gives two useful pieces of evidence.

1. Random non-affine column pairs do not appear to make the recursive template
   easy: no witness occurs in the first 1,000 committed geometries.
2. Exact row-pattern search remains practical on typical non-affine inputs. The
   difficult `fc` orientation has a heavier tail, but the mean tree is still
   small compared with factorial enumeration of `P`.

The result does **not** justify a probability estimate, an obstruction claim, or
an inference that no non-affine template exists. A successful template may lie
in a highly structured and sparse double coset.

## 4. Revised search target

Rather than increasing unstructured random sampling indefinitely, the next
recursive search should classify structured non-affine map families:

1. one-transposition perturbations of the affine group;
2. explicit affine double cosets under left and right multiplication;
3. low-complexity polynomial or piecewise-affine permutations;
4. cycle-structure classes suggested by successful side-five and side-six
   templates.

Each family should use the generic exact solver and either emit a scalar witness
or a complete interval census.

## 5. Verification

```bash
python scripts/verify_product_transposition_nonaffine_sample_ten.py
```

The verifier compiles the deterministic sampler, runs all four orientations in
parallel, rejects any `FOUND` output, and asserts every node total and maximum in
the table.
