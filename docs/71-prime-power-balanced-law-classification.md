# Classification of balanced completed-reciprocal laws

The balanced recursive construction CMR67 works for primes
`p=1 mod 4`. The remaining question was whether a different probability law on
completed-reciprocal maps could give exact one-cell balance when
`p=3 mod 4`. The answer is no: balance itself forces uniformity in the shift
parameter, while the two endpoint shifts require incompatible quadratic
characters.

Let `p` be an odd prime and define

\[
\tau(0)=0,
\qquad
\tau(x)=x^{-1}\quad(x\ne0).
\]

For `b in F_p` and `c in F_p^*`, write

\[
F_{b,c}(x)=b+c\tau(x)\pmod p.
\]

All residues are represented by the standard integers `0,...,p-1` when real
collinearity is discussed.

## 1. Fourier rigidity of exact cell balance

Let `mu(b,c)` be any probability distribution on the parameter pairs. Say that
it is **cell-balanced** when

\[
\Pr(F_{B,C}(x)=y)=\frac1p
\]

for every column `x` and row `y`.

### Theorem CMR113 — PROVED

Every cell-balanced parameter law has the form

\[
\boxed{
\mu(b,c)=\frac{\alpha_c}{p}
}
\]

for some probability distribution `(alpha_c)_{c in F_p^*}`.
Equivalently, conditional on every coefficient `c` of positive mass, the shift
`b` is exactly uniform on `F_p`.

### Proof

The completed inverse `tau` is a permutation of `F_p`. Thus cell balance says
that

\[
B+uC
\]

is uniform on `F_p` for every `u in F_p`.

Fix a nontrivial additive character

\[
\chi_a(z)=\exp(2\pi i az/p),
\qquad a\ne0.
\]

Uniformity gives

\[
0
=
\mathbb E\chi_a(B+uC)
=
\widehat\mu(a,au)
\]

for every `u`. Since multiplication by `a` permutes `F_p`, this says

\[
\widehat\mu(a,d)=0
\]

for every frequency `d` whenever `a ne 0`.
Fourier inversion in the first coordinate therefore makes
`b -> mu(b,c)` constant for each fixed `c`. Write that constant as
`alpha_c/p`. Total mass one gives `sum_c alpha_c=1`. ∎

This rigidity uses only exact cell marginals; it does not use the no-three
condition.

## 2. The two endpoint shifts

### Theorem CMR114 — PROVED

The standard integer graph of `F_{0,c}` is no-three exactly when `c` is a
quadratic nonsquare modulo `p`.

The graph of `F_{p-1,c}` is no-three exactly when `-c` is a quadratic
nonsquare.

### Proof

CMR35 with shift `b=0` proves that every nonsquare `c` is no-three.
If `c=x^2` is a square, then the three distinct standard grid points

\[
(0,0),
\qquad
(x,x),
\qquad
(p-x,p-x)
\]

belong to the graph and lie on the real diagonal `y=x`. Hence every square is
invalid.

Reflect the integer square in its horizontal midline,

\[
(x,y)\longmapsto(x,p-1-y).
\]

This real affine reflection sends the graph of `F_{p-1,c}` to the graph of
`F_{0,-c}`. The second assertion follows from the first. ∎

## 3. Exact classification

### Theorem CMR115 — PROVED

A cell-balanced probability law supported entirely on integer no-three maps
`F_{b,c}` exists if and only if

\[
p\equiv1\pmod4.
\]

When `p=1 mod 4`, every such law is obtained by choosing an arbitrary
probability distribution on the quadratic nonsquares `c`, then choosing `b`
uniformly and independently. In particular, the uniform law from CMR67 is the
canonical finite balanced family.

When `p=3 mod 4`, no cell-balanced completed-reciprocal no-three law exists,
even with arbitrary nonuniform weights and even before asking for a disjoint
second layer.

### Proof

By CMR113, a coefficient `c` of positive mass forces positive and equal mass on
all shifts `b`.

At `b=0`, CMR114 requires `c` to be a nonsquare. At `b=p-1`, it requires `-c`
to be a nonsquare.

If `p=3 mod 4`, then `-1` is a nonsquare, so multiplication by `-1` swaps
squares and nonsquares. The two endpoint requirements are incompatible.
Therefore every `alpha_c` must be zero, contradicting total mass one.

If `p=1 mod 4`, multiplication by `-1` preserves quadratic character. CMR67
proves that every nonsquare coefficient works for every shift. Choosing `b`
uniformly makes `b+u c` uniform for every fixed `u` and `c`; mixtures over
nonsquare coefficients remain balanced. Conversely `b=0` excludes every square
coefficient by CMR114. ∎

## 4. Consequence for the recursive program

The balanced-law bottleneck is now completely classified within the
completed-reciprocal family:

- primes `p=1 mod 4` have exactly the uniform-shift, nonsquare-coefficient laws;
- primes `p=3 mod 4` require a genuinely different local permutation family,
  not a different weighting of the existing reciprocal maps.

Thus future work at `p=3 mod 4` should search outside the completed-reciprocal
parameter space or use an unbalanced law with a different global summation
argument. Linear programming over the same maps cannot solve the problem.

The Fourier-rigidity dimensions and endpoint classification are checked in
[`scripts/verify_prime_power_balanced_law_classification.py`](../scripts/verify_prime_power_balanced_law_classification.py).
