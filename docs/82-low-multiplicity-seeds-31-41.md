# Low-multiplicity affine-orbit seeds at orders 31, 37, and 41

PX129 converts one strong-complete mapping into a three-parameter affine-orbit
distribution. Its rank-two and rank-three cylinder constants are controlled by

\[
K_2=\frac{\mu(f)}p,
\qquad
K_3=\frac{p-2}{p}\tau(f).
\]

PX132 and PX134 verify bounded triangle multiplicity through order 29. This
chapter records the next three exact seeds.

## Theorem PX135 -- PROVED FINITE

At order 31, the permutation

\[
\begin{aligned}
f_{31}={}&(0,10,22,5,14,16,9,29,6,26,17,1,18,27,19,23,\\
&3,12,2,4,8,13,15,24,20,7,30,21,25,28,11)
\end{aligned}
\]

is strong complete and satisfies

\[
\boxed{\mu(f_{31})=44,\qquad \tau(f_{31})=6.}
\]

Hence

\[
K_2=\frac{44}{31}<1.42,
\qquad
K_3=\frac{174}{31}<5.62.
\]

Since \(31\equiv3\pmod4\), this seed is not generated from the affine
square-root-of-\(-1\) switching shell PX103. Thus the low-multiplicity orbit
phenomenon is not restricted to primes congruent to one modulo four.

## Theorem PX136 -- PROVED FINITE

At order 37, the permutation

\[
\begin{aligned}
f_{37}={}&(0,10,17,25,21,19,8,32,35,12,36,22,33,31,24,2,7,14,11,\\
&15,6,28,20,27,16,30,1,9,4,23,29,26,3,34,13,18,5)
\end{aligned}
\]

is strong complete and satisfies

\[
\boxed{\mu(f_{37})=54,\qquad \tau(f_{37})=7.}
\]

Consequently

\[
K_2=\frac{54}{37}<1.46,
\qquad
K_3=\frac{245}{37}<6.63.
\]

## Theorem PX137 -- PROVED FINITE

At order 41, the permutation

\[
\begin{aligned}
f_{41}={}&(0,14,28,5,22,39,18,29,11,37,27,7,1,19,38,10,13,16,25,34,2,\\
&30,33,17,40,23,31,15,6,9,20,4,36,12,35,26,3,21,24,8,32)
\end{aligned}
\]

is strong complete and satisfies

\[
\boxed{\mu(f_{41})=64,\qquad \tau(f_{41})=8.}
\]

Thus

\[
K_2=\frac{64}{41}<1.57,
\qquad
K_3=\frac{312}{41}<7.61.
\]

## Proof of PX135--PX137

For every displayed map, exact enumeration verifies that

\[
f,
\qquad x-f(x),
\qquad x+f(x)
\]

are permutations. The verifier then enumerates every ordered secant and every
ordered affine-triangle shape from PX129 and reproduces the displayed maxima.
\(\square\)

## Consequence

The exact seed table now covers

\[
p=13,17,19,23,29,31,37,41.
\]

In every case

\[
\mu(f_p)<2p,
\qquad
\tau(f_p)\le9.
\]

The data therefore support a slightly relaxed uniform target

\[
\mu(f_p)\le2p,
\qquad
\tau(f_p)\le9,
\]

while the sharper conjecture from PX134 asks for \(\tau\le8\). Either constant
bound is sufficient for constant rank-three affine-orbit spread.

## Verification

Run

```bash
python scripts/verify_product_low_multiplicity_seeds.py
```

The same verifier checks all eight committed seeds exactly.
