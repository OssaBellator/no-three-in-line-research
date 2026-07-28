# Protected simultaneous-rainbow cylinder census

PX85--PX86 reduce the protected-spread input to rank-three cylinder estimates for
simultaneous-rainbow perfect matchings, uniformly before and after conditioning
on the first matching. This chapter computes the complete families at prime
orders five and seven and isolates the exact entropy requirement behind the
missing theorem.

The protected colourings are

\[
\chi_{a,b}(x,y)=bx-2ay
\]

for directions `(1,1)` and `(1,-1)`. After fixing a first-stage matching `Phi`,
the conditional colourings are

\[
\psi_{a,b}^{\Phi}(x,w)=bw-2a\Phi(x).
\]

This is a finite census and a route barrier, not an asymptotic spread theorem.

## 1. Exact family sizes

### Theorem PX1033 -- PROVED FINITE

At order five, the common-rainbow first-stage family contains exactly `10`
permutations. Every admissible first-stage permutation has exactly `10`
conditional second-stage permutations.

At order seven, the common-rainbow first-stage family contains exactly `28`
permutations. Every admissible first-stage permutation has exactly `28`
conditional second-stage permutations.

Thus the conditional family size is uniform over every admissible first-stage
matching in both complete censuses.

## 2. Exact cylinder constants

For a permutation family `F`, define the rank-`k` normalized cylinder constant

\[
K_k(F)=\max_{|S|=k}
\frac{|\{\pi\in F:\pi\supseteq S\}|}{|F|}(\ell)_k.
\]

### Theorem PX1034 -- PROVED FINITE

The exact constants for both the first-stage family and every conditional
second-stage family are:

| Order | `K_1` | `K_2` | `K_3` |
|---:|---:|---:|---:|
| 5 | `1` | `2` | `6` |
| 7 | `1` | `3/2` | `15/2` |

Every compatible rank-two cylinder and every compatible rank-three cylinder
that occurs is contained in exactly one family member. The rank-three constants
therefore equal

\[
\frac{(5)_3}{10}=6,
\qquad
\frac{(7)_3}{28}=\frac{15}{2}.
\]

The same values hold uniformly after conditioning on any admissible first-stage
matching.

## 3. Cubic entropy requirement

### Corollary PX1035 -- PROVED REDUCTION

Let `F` be any nonempty family of permutations of order `ell`. Some rank-three
cylinder is contained in at least one member of `F`, so

\[
K_3(F)\ge\frac{(\ell)_3}{|F|}.
\]

Consequently a rank-three bound with an absolute constant `K` requires

\[
|F|\ge\frac{(\ell)_3}{K}=\Omega(\ell^3).
\]

Existence alone, or even a merely quadratic number of simultaneous-rainbow
matchings, cannot supply the PX86 cylinder input. The finite order-five and
order-seven families attain this counting lower bound because every occurring
rank-three cylinder is unique.

This redirects the protected-spread frontier toward an abundance theorem,
switching distribution, or entropy-completion result producing at least cubic
family size with controlled cylinder multiplicities.

## 4. Verification

```bash
python scripts/verify_product_protected_rainbow_cylinder_census.py
```

The verifier enumerates all permutations at orders five and seven, checks both
rainbow stages, computes every rank-one, rank-two, and rank-three cylinder
histogram, and verifies uniform conditional family sizes and constants.
