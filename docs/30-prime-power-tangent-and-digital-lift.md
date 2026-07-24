# Exact-real tangent cells and binary digital lifting

This chapter advances two remaining targets from
[`tracks/all-n-composite-modulus.md`](../tracks/all-n-composite-modulus.md):
turning the completed-reciprocal Hensel count into an exact real-grid bound,
and extending the binary digit-linear construction beyond side length `32`.

Throughout the first part, let

\[
N=p^k
\]

with `p` odd, and use the valuation-completed reciprocal channel
\(R_{\mathbf c}\) from
[`docs/28-prime-power-completed-reciprocals.md`](28-prime-power-completed-reciprocals.md).

## 1. Exact spacing inside the top tangent cell

Let a primitive real line be

\[
L:Ax+By=C,
\]

and suppose

\[
h=v_p(C)<k,
\qquad p\nmid AB.
\]

Put

\[
m=k-h,
\qquad M=p^m,
\qquad C_h=C/p^h,
\qquad \Delta=C_h^2-4ABc_h.
\]

A top-stratum point has

\[
x=p^hu,
\qquad y=p^hw,
\]

where `u,w` are units modulo `M`, and it satisfies both

\[
Au+Bw=C_h
\]

as an exact integer equation and

\[
uw\equiv c_h\pmod M.
\]

Write

\[
H=\max(|A|,|B|),
\qquad L_0=\min(|A|,|B|).
\]

### Theorem CMR11 — PROVED

The top-stratum real points on `L` satisfy the following sharper bounds.

1. If \(v_p(\Delta)<m\) is odd, or its residual unit is a quadratic
   nonsquare modulo `p`, there are no top-stratum points.
2. Suppose

   \[
   v_p(\Delta)=2t<m
   \]

   and the residual unit is a square modulo `p`. Then the possible `u`
   coordinates lie in two residue classes modulo

   \[
   p^{m-t}.
   \]

   The same statement holds for the `w` coordinates. Consequently the number
   of exact real top-stratum points is at most

   \[
   2\left(
   1+
   \left\lfloor
   \frac{(M-1)L_0}{H p^{m-t}}
   \right\rfloor
   \right).
   \]
3. If

   \[
   \Delta\equiv0\pmod M,
   \]

   then the possible `u` coordinates lie in one residue class modulo

   \[
   p^{\lceil m/2\rceil},
   \]

   and likewise for `w`. The number of exact real top-stratum points is at
   most

   \[
   1+
   \left\lfloor
   \frac{(M-1)L_0}{H p^{\lceil m/2\rceil}}
   \right\rfloor.
   \]

Adding the lower-stratum contribution from CMR3 gives the same displayed
bounds plus `2h` for the full line intersection.

### Proof

The top-stratum congruence is

\[
Au^2-C_hu+Bc_h\equiv0\pmod M.
\]

Because `2A` is a unit modulo `M`, completing the square gives

\[
(2Au-C_h)^2\equiv\Delta\pmod M.
\]

If \(v_p(\Delta)=2t<m\), the standard odd-prime square-root classification
shows that the roots of the last congruence form two classes modulo
\(p^{m-t}\). Since multiplication by `2A` is invertible, the same is true of
`u`. If \(\Delta\equiv0\pmod M\), the square root is divisible by
\(p^{\lceil m/2\rceil}\), giving one class at that modulus. The nonsquare and
odd-valuation cases have no roots.

It remains to use the exact line rather than count every modular root. As `w`
ranges through the real interval `[0,M-1]`, the exact equation

\[
Au+Bw=C_h
\]

confines the feasible `u` coordinates to an interval of diameter at most

\[
(M-1)|B|/|A|.
\]

The symmetric quadratic in `w` gives a feasible `w` interval of diameter at
most

\[
(M-1)|A|/|B|.
\]

Choose the shorter coordinate interval. Its diameter is at most

\[
(M-1)L_0/H.
\]

A residue class modulo `q` meets a real interval of diameter `W` in at most
\(1+\lfloor W/q\rfloor\) integers. Applying this to the one or two root
classes proves the bounds. ∎

### Consequence

The raw Hensel count can only be approached by slope-balanced lines. For
example, in the two-root case, a top population of `s` forces

\[
\frac{L_0}{H}
\ge
\frac{(s/2-1)p^{m-t}}{M-1}.
\]

Thus large tangent cells are simultaneously singular in the `p`-adic sense
and balanced in their exact Euclidean slope. This narrows the remaining
line-cap problem to one explicit two-parameter regime.

## 2. A 64-point binary digit-linear no-three channel

For a binary matrix `M`, retain the notation

\[
F_M(x)=\sum_i y_i2^i,
\qquad y=Mx\quad\text{over }\mathbb F_2.
\]

### Theorem CMR12 — PROVED BY EXHAUSTIVE FINITE CHECK

At side length

\[
N=64,
\]

the matrix with row masks

```text
25, 8, 2, 11, 52, 28
```

is invertible over \(\mathbb F_2\), and the permutation graph of `F_M`
contains no real collinear triple.

The first five rows reduced modulo `32` give the additional exact
`32`-point matrix

```text
25, 8, 2, 11, 20
```

so the `64`-point example is a genuine one-bit block extension of a
`32`-point digit-linear no-three channel.

### Verification

Binary elimination proves invertibility. The verifier then checks all

\[
\binom{64}{3}=41664
\]

triples with the exact integer determinant and finds no zero.

This extends the positive digital sizes from

\[
8,16,32
\]

to

\[
8,16,32,64.
\]

It remains a one-channel theorem and does not by itself give `128` selected
points on the `64` by `64` grid.

## 3. The simplest lift to 128 is obstructed

Call a `7` by `7` binary matrix a **direct one-bit block extension** of the
CMR12 matrix if its upper-left `6` by `6` block is fixed and the new input
column, new output row, and lower-right bit are arbitrary.

### Theorem CMR13 — PROVED BY EXHAUSTIVE FINITE CHECK

There are

\[
2^{13}=8192
\]

direct one-bit block extensions of the CMR12 matrix. Exactly `4096` are
invertible. Every invertible extension has a real collinear triple in its
`128`-point permutation graph.

### Verification

The verifier enumerates all new-column vectors, all new-row vectors, and both
lower-right bits. It performs exact binary elimination and, for each
invertible extension, stops at the first exact zero determinant. No extension
survives.

This does not rule out a different `7` by `7` digit-linear matrix. It proves
that the most literal recursive continuation of the new `32` to `64` chain
fails, so any `128` construction must alter the existing six-bit block or use
a more general nonlinear digit rule.

## 4. Updated bottleneck

The two branches now have sharper endpoints.

- For completed reciprocals, the unresolved large-line regime is a
  `p`-adically singular, Euclidean-slope-balanced top cell. Unbalanced lines
  already satisfy the coefficient-sensitive CMR11 bound.
- For digital channels, side length `64` is solved for one permutation layer,
  while the direct block recursion to `128` is refuted. The next search should
  allow modifications throughout the old block, or use triangular nonlinear
  Boolean terms.

The exact checks are implemented in
[`scripts/verify_prime_power_tangent_digital.py`](../scripts/verify_prime_power_tangent_digital.py).
