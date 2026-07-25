# Actual PX64 line occupancy still gives bounded terminal return

PX391 assumes both the layer--channel count and selected-line occupancy are
subpower.  The recovered PX63 entry audit shows that the original low-syndrome
seed supplies a weaker but explicit line cap:

\[
K_0=O((n\log n)^{1/3}).
\]

This chapter recalculates the weighted terminal-return exponents with that
actual input.  The subpower occupancy assumption is unnecessary.  Three
one-variable high-point amplifications, rather than two, raise the designated
weight to `n^(7/8-o(1))`; rank-one averaging then gives a clean star of order
`n^(13/24-o(1))`, which is above the square-root ambient threshold.  A
two-variable return still reaches a large star in one further generation.

The only remaining asymptotic parameter hypothesis in the terminal return is
the subpower layer--channel count.

## 1. The line cap supplied by PX63--PX64

Let `D_0` be the bad-triple count of the PX63 seed and let `K_0` be its maximum
selected-line occupancy.

### Theorem PX404 -- PROVED

The seed may be chosen so that

\[
D_0
\le
\frac{8n^2}{n-1}
+
12288\frac{n^3}{(n-1)(n-2)}H_{2n-1},
\]

and

\[
\boxed{
K_0
\le
2+(6D_0)^{1/3}
=
O((n\log n)^{1/3}).
}
\]

Equivalently,

\[
\boxed{K_0=n^{1/3+o(1)}.}
\]

### Proof

The first display is PX63 and the second is PX64.  Since
`H_(2n-1)=O(log n)`, the bad-triple bound is `O(n log n)`, giving the exponent
form. \(\square\)

During later return steps fix the threshold

\[
K_*=n^{1/3+o(1)}.
\]

If a selected line exceeds `K_*`, it is sent directly to the loaded-line
interface PX240--PX244.  Otherwise all rank-one star extractions may use
`K=K_*`.

## 2. Amplification from arbitrary initial weight

Put

\[
A=\frac{n}{384q_{\rm ch}}.
\]

PX361 gives the one-variable recurrence

\[
D_{j+1}\ge\sqrt{A D_j}
\]

unless an endpoint block of the same scale appears earlier.

### Theorem PX405 -- PROVED

Starting from any designated weight `D_0>=1`, a chain of `j` high-point
one-variable returns satisfies

\[
\boxed{
D_j
\ge
A^{1-2^{-j}}D_0^{2^{-j}}.
}
\]

If `q_ch=n^(o(1))` and `D_0=n^(delta+o(1))`, then

\[
\boxed{
D_j
=
n^{1-2^{-j}(1-\delta)-o(1)}.
}
\]

### Proof

Iterating `D_(j+1)>=A^(1/2)D_j^(1/2)` gives

\[
D_j
\ge
A^{1/2+1/4+\cdots+1/2^j}D_0^{1/2^j}
=
A^{1-2^{-j}}D_0^{2^{-j}}.
\]

The exponent form uses `A=n^(1-o(1))`. \(\square\)

## 3. Polynomial line caps and the return threshold

Assume no loaded line above

\[
K=n^{\kappa+o(1)},
\qquad 0\le\kappa<\frac12.
\]

PX386--PX387 turn designated rank-one weight `D_j` into a clean star of order
`Omega(D_j/K)`.

### Theorem PX406 -- PROVED REDUCTION

From an original terminal core `D_0>=1`, after `j` high-point one-variable
returns, every coordinate or generic rank-one outcome gives a clean star of
order

\[
\boxed{
n^{1-2^{-j}-\kappa-o(1)}.
}
\]

This star is above the square-root ambient threshold whenever

\[
\boxed{2^{-j}<\frac12-\kappa.}
\]

### Proof

Use PX405 with `delta=0`, then divide the resulting weight by the line cap in
PX386 or PX387.  The exponent exceeds one half exactly under the displayed
inequality. \(\square\)

## 4. The actual one-variable return depth

For the PX64 exponent `kappa=1/3`, three high-point generations give

\[
D_3
\ge
\left(\frac{n}{384q_{\rm ch}}\right)^{7/8}
=
n^{7/8-o(1)}.
\]

### Theorem PX407 -- PROVED REDUCTION

Assume `q_ch=n^(o(1))`.  On a branch with no loaded line above
`n^(1/3+o(1))`, after three one-variable high-point returns:

1. a directed-path return is impossible by PX366;
2. a coordinate rank-one return gives a clean star of order at least
   
   \[
   \boxed{
   n^{7/8-1/3-o(1)}
   =
   n^{13/24-o(1)};
   }
   \]
3. a generic rank-one return satisfies the same exponent with the stronger
   PX387 constant;
4. an endpoint-block outcome has order `n^(7/8-o(1))` and is already large.

Since

\[
\frac{13}{24}>rac12,
\]

a purely one-variable terminal-return chain reaches the established
large-block interface after at most three high-point amplifications and one
rank-one conversion.

### Proof

PX366 permits directed paths only while `D=O(n^(1/3))`, whereas
`D_3=n^(7/8-o(1))`.  PX386--PX387 divide `D_3` by
`K_*=n^(1/3+o(1))`, giving exponent `13/24`.  PX361 gives an endpoint block on
the same `D_3` scale when the high-point alternative fails. \(\square\)

## 5. The actual two-variable return depth

### Theorem PX408 -- PROVED REDUCTION

Assume `q_ch=n^(o(1))` and use the PX64 line threshold.  A first weighted
two-variable return from an original terminal core gives one-point destruction

\[
D_1\ge\frac n{64}.
\]

At the next exact-type return:

1. directed path is excluded by PX366;
2. mixed shadow is excluded by PX368;
3. coordinate or generic rank one gives a clean star of order at least
   
   \[
   \boxed{n^{2/3-o(1)};}
   \]
4. a larger selected line enters PX244 directly.

Thus a two-variable branch reaches the large-block star/line interface in at
most one additional return generation.

### Proof

The first two exclusions are unchanged from PX390.  Rank-one averaging gives
star order at least `D_1/(48K_*)` or `D_1/(32K_*)`, whose exponent is
`1-1/3=2/3`. \(\square\)

## 6. Revised actual terminal-return theorem

### Theorem PX409 -- PROVED REDUCTION

Assume

\[
q_{\rm ch}=n^{o(1)}
\]

and the ambient order is above the explicit buffer/divisor thresholds.  No
subpower selected-line hypothesis is required.

Starting from the actual PX63--PX64 seed, every order-one or order-two
trajectory-terminal core has one of the following outcomes:

1. direct buffer-cycle improvement;
2. a compatible endpoint block above the square-root ambient threshold;
3. a loaded line handled by cubic destruction;
4. a clean star above the square-root ambient threshold after at most three
   one-variable high-point amplifications and one rank-one conversion;
5. a two-variable return reaching a large star or loaded line after at most one
   additional generation.

### Proof

Use the line-or-cap dichotomy with `K_*=n^(1/3+o(1))`.  A line above the cap is
sent to PX244.  Under the cap, PX407 handles one-variable chains and PX408
handles the first two-variable occurrence.  The endpoint-block and direct
improvement alternatives are PX361 and PX350. \(\square\)

### Corollary PX410 -- PROVED REDUCTION

The selected-line component of PX396's asymptotic terminal hypothesis is now
verified from the actual PX63 seed.  The remaining asymptotic hypothesis is the
subpower layer--channel count

\[
q_{\rm ch}=n^{o(1)}.
\]

The remaining global work is therefore:

1. prove or enforce that channel bound along every descendant;
2. verify finite ambient orders below the buffer/divisor thresholds;
3. audit factor-host membership for non-rectangle endpoint and packet moves;
4. complete the final splice into exact doubling.

PX410 does not assert exact infinite closure.

## 7. Verification

Run

```bash
python scripts/verify_product_px64_return_depth.py
```

The verifier checks the generalized amplification recurrence, the polynomial
line-cap threshold inequality, the actual exponents `7/8`, `13/24`, and `2/3`,
and the directed-path/mixed-shadow exclusion comparisons.
