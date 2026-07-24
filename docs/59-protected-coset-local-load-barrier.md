# Protected coset local-load criterion and finite barrier

PX89 installs an exponential factor-compatible state space while preserving all
chosen low-height line capacities.  This chapter asks whether the independent
coset shifts can already be selected by a direct Lovasz local lemma.

The answer has two parts.

1. There is a clean exact local-load criterion, because every bad-triple event
   depends on at most three coset variables.
2. The first nontrivial protected bank misses that criterion by several orders
   of magnitude.  Thus plain coset translations do not provide enough spread;
   a richer protected distribution or a preliminary cleaning step is required.

Failure of the criterion is not an impossibility theorem for the entire state
space.

## 1. Event system

Use the protected coset bank PX89 with additive subgroup `K` of order `h` and
coset variables

\[
X_C\in K.
\]

Choose all variables independently and uniformly.  For every unordered triple
`E` of abstract selected corner labels, let the bad event `B_E` be that its
three scalar realizations are collinear.

A corner indexed by `u` depends only on the shift variable of the coset
containing `u`.  Therefore

\[
|\operatorname{supp}(B_E)|\le3.
\]

Write

\[
p_E=\Pr(B_E)
\]

and define the normalized load at one coset variable by

\[
\Lambda_C
=
\sum_{E:C\in\operatorname{supp}(B_E)}p_E.
\]

Events with disjoint supports are mutually independent.

## Theorem PX90 -- PROVED

If

\[
\boxed{
\max_C\Lambda_C\le\frac1{12},
}
\]

then some protected coset-shift state is no-three.

Consequently, under the hypotheses of PX89, this state is saturated,
factor-compatible, and preserves every protected line capacity.

### Proof

Use the dependency graph in which two bad events are adjacent when their
supports intersect.  Set

\[
x_E=2p_E.
\]

For any event `E`,

\[
\sum_{F\sim E}x_F
\le
2\sum_{C\in\operatorname{supp}(B_E)}\Lambda_C
\le
2\cdot3\cdot\frac1{12}
=\frac12.
\]

Also `p_E<=1/12`, hence `0<=x_E<=1/6`.  For numbers in `[0,1]`,

\[
\prod_i(1-z_i)\ge1-\sum_i z_i.
\]

Therefore

\[
x_E\prod_{F\sim E}(1-x_F)
\ge
2p_E\left(1-\sum_{F\sim E}x_F\right)
\ge p_E.
\]

The asymmetric Lovasz local lemma gives positive probability that no bad event
occurs. \(\square\)

The constant `1/12` is not optimized.  The point is that the criterion is
expressed entirely by exact one-, two-, and three-coset certificate masses.

## 2. Integer form of the loads

For a bad event supported on `k` cosets, let `N_E` be the number of assignments
to those `k` variables which realize the collinearity.  Then

\[
p_E=\frac{N_E}{h^k}.
\]

Multiplying all loads by `h^3` gives the exact integer quantity

\[
W_C
=
\sum_{E:C\in\operatorname{supp}(B_E)}
N_Eh^{3-|\operatorname{supp}(B_E)|},
\qquad
\Lambda_C=\frac{W_C}{h^3}.
\]

Thus PX90 is algorithmically checkable without floating-point arithmetic.

## 3. Exact order-five census in `Z_25`

Take

\[
n=25,
\qquad
K=5\mathbb Z_{25},
\qquad
h=5,
\]

and the protected affine rectangle parameters

\[
m=2,
\qquad
c=s=0.
\]

The directions `(1,1)` and `(1,-1)` are protected because

\[
\gcd(1-2,25)=1,
\qquad
\gcd(-1-2,25)=1.
\]

There are five independent coset variables and 100 abstract corner labels.
Enumerating every unordered label triple and every assignment on its support
gives:

| Support size | Nonzero bad events | Total probability mass | Integer mass times `125` |
|---:|---:|---:|---:|
| 1 | 1,150 | 388 | 48,500 |
| 2 | 20,614 | 2,026.4 | 253,300 |
| 3 | 25,484 | 754.144 | 94,268 |

The exact variable load numerators are

\[
(W_0,W_1,W_2,W_3,W_4)
=
(167688,167429,167462,167670,167655).
\]

Hence

\[
(\Lambda_0,\ldots,\Lambda_4)
=
\frac1{125}
(167688,167429,167462,167670,167655),
\]

and

\[
\max_C\Lambda_C
=
\frac{167688}{125}
=1341.504.
\]

### Theorem PX91 -- PROVED FINITE

The direct local-load hypothesis PX90 fails for this protected `Z_25`
order-five coset bank by a factor greater than sixteen thousand.

### Proof

The exact enumeration above gives

\[
\frac{\max_C\Lambda_C}{1/12}
=
12\cdot\frac{167688}{125}
>16000.
\]

All counts use exact integer determinants and integer event weights. \(\square\)

No individual event is certain in this census.  The failure is accumulated
local mass, not one frozen collinearity.

## 4. Consequence for the general proof

The protected coset construction solves the low-direction geometry and supplies
local variables, but its plain translation measure is far from sufficiently
spread.  The next entropy source must reduce normalized certificate loads while
retaining the protected line-coordinate injections.

A suitable target is a **two-coordinate protected spread theorem**: construct a
distribution on the three labelings `(R,A,B)` from PX61 such that

1. every protected low-height line has capacity at most two;
2. fixed-rank cylinders have probability `O((n)_k^{-1})` in each independently
   exposed coordinate family;
3. the resulting one-, two-, and three-variable certificate loads satisfy a
   constant local bound such as PX90.

The universal low-syndrome seed PX63 shows that unrestricted independent
permutations have enough global spread.  PX86--PX89 show that low directions can
be protected deterministically.  The unresolved task is to achieve both
properties in one distribution.

## 5. Verification

Run

```bash
python scripts/verify_product_protected_coset_local_load.py
```

The verifier computes every event probability exactly, checks the support-rank
bound, reproduces all three certificate populations and the five load
numerators, and verifies the stated failure ratio.