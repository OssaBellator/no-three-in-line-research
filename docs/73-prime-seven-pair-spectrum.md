# Pair-spectrum sharpening for the prime-seven bank

CMR116--CMR119 give a balanced recursive bank at every power of seven. A second
seven-map factorization has a stronger pair-difference spectrum and therefore
pays an extra separation-node factor on every binary same-layer cluster.

Define

```text
H0 = (0,2,6,5,3,4,1)
H1 = (1,0,4,6,2,3,5)
H2 = (2,3,5,4,1,6,0)
H3 = (3,5,0,2,6,1,4)
H4 = (4,1,3,0,5,2,6)
H5 = (5,6,2,1,4,0,3)
H6 = (6,4,1,3,0,5,2)
```

and put

\[
\mathcal H_7=\{H_0,\ldots,H_6\}.
\]

## 1. Exact factorization and pair spectrum

### Theorem CMR120 — PROVED BY EXHAUSTIVE FINITE CHECK

Every member of `H_7` is an integer no-three permutation, and the seven graphs
partition the complete `7` by `7` grid.

For every two distinct child inputs `u,v` and every nonzero residue `d`,

\[
\#\{H\in\mathcal H_7:H(u)-H(v)=d\pmod7\}
\le3.
\]

Thus a uniform local map has exact one-cell atom `1/7`, while every prescribed
pair difference has probability at most `3/7`.

### Proof

All assertions are finite. The checker verifies the seven permutation and grid
partition conditions, all `245` within-map triples, and all

\[
\binom72\cdot6=126
\]

input-pair/difference cells. ∎

## 2. Binary-cluster separation factor

Use the ordered-distinct root law and independent uniform `H_7` maps at every
nonroot node, exactly as in CMR117--CMR118.

Fix a nontransverse binary cluster whose closest same-layer pair separates at
depth `s>=1`. The two closest columns enter one local map through distinct child
digits `xi_1,xi_2`.

### Theorem CMR121 — PROVED

For every fixed binary same-layer cluster,

\[
\Pr(\Delta\equiv0\pmod{7^k})
\le
\frac37\,7^{-(k-s-1)}.
\]

The same bound holds for real collinearity.

### Proof

After division by the common minimum power of seven in the determinant
coefficients, the two closest endpoints have opposite unit coefficients and the
third coefficient vanishes modulo seven. At the separation digit the next
congruence fixes one value of

\[
H(\xi_1)-H(\xi_2)\pmod7.
\]

CMR120 permits at most three of the seven local maps. At every depth above `s`,
the three node keys are distinct and the usual one-cell exposure contributes an
independent factor `1/7`. ∎

## 3. Sharpened recursive syndrome

The layer-transverse argument of CMR70 applies to the ordered-distinct root
law. At the root, after the repeated layer map is exposed, the singleton layer
is uniform among the six remaining maps. Hence every layer-transverse triple
has probability at most

\[
\frac1{6\,7^{k-1}}
=
\frac7{6N}.
\]

Equilateral nontransverse clusters retain the CMR68 above-separation bound.
Binary clusters use CMR121.

### Corollary CMR122 — PROVED

For `N=7^k`, the sharpened balanced bank satisfies

\[
\boxed{
\mathbb E T_k
<
\frac{36}{7}(k-1)N^2
+
\frac{29}{9}N^2.
}
\]

The same estimate holds for determinant-zero-modulo-`N` triples with three
distinct columns.

### Proof

Layer-transverse triples contribute less than

\[
8\binom N3\frac7{6N}
<
\frac{14}{9}N^2.
\]

For equilateral nontransverse clusters, insert `p=7` into the exact clustering
sum from CMR74. Their contribution is below

\[
\frac{7-2}{3}N^2
=
\frac53N^2.
\]

At binary valuation level `s`, the number of exact closest column pairs is

\[
P_s
=
\frac{3N^2}{7^{s+1}}.
\]

There are fewer than `P_s N` column triples and four layer assignments in which
the closest pair is same-layer. CMR121 gives

\[
4P_sN\frac37\,7^{-(k-s-1)}
=
\frac{36}{7}N^2.
\]

Sum the at most `k-1` binary levels and add the two quadratic terms:

\[
\frac{14}{9}+\frac53=\frac{29}{9}.
\]

Every argument imposes determinant congruences, so the modular version follows
as well. ∎

The exact local spectrum and recursive structural checks are in
[`scripts/verify_prime_seven_pair_spectrum.py`](../scripts/verify_prime_seven_pair_spectrum.py).
