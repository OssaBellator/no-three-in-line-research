# An explicit Cartesian collinear-triple constant

PX333 fixes an absolute constant `A_3` satisfying

\[
W_{3,5}+W_{3,6}
\le
A_3t^4\log(2t),
\]

but does not instantiate it.  This is the first numerical witness isolated by
PX455.  A self-contained crossing-lemma calculation gives a conservative
explicit value

\[
\boxed{A_3=320.}
\]

The proof counts all collinear triples in a Cartesian point set, so it also
bounds the compatible support-five/six subfamily used by the decoder.

## 1. Explicit crossing lemma

Let a simple graph with `v` vertices and `e` edges be drawn in the plane with no
three edges crossing at one nonvertex point and no edge passing through a
nonincident vertex.  Let `cr(G)` be its crossing number.

### Theorem PX456 -- PROVED

If

\[
e\ge4v,
\]

then

\[
\boxed{
\operatorname{cr}(G)
\ge
\frac{e^3}{64v^2}.
}
\]

### Proof

For every drawing of a simple graph,

\[
\operatorname{cr}(G)
\ge
e-3v,
\]

because deleting one edge at each crossing leaves a planar simple graph with at
most `3v-6` edges.

Retain every vertex independently with probability

\[
p=\frac{4v}{e}\le1
\]

and take the induced drawing.  Its expected vertex, edge, and crossing counts
are `pv`, `p^2e`, and `p^4 cr(G)`.  Apply the preceding inequality to every
sample and take expectations:

\[
p^4\operatorname{cr}(G)
\ge
p^2e-3pv.
\]

Substitution gives

\[
p^2e-3pv
=
\frac{16v^2}{e}-\frac{12v^2}{e}
=
\frac{4v^2}{e}.
\]

Divide by `p^4=256v^4/e^4`. \(\square\)

## 2. Explicit point-line incidence bound

Let `P` be `M` points and `L` be `L` distinct lines.  Join consecutive points
of `P` on every line.  The resulting simple topological graph has `M` vertices
and

\[
e=I(P,\mathcal L)-L
\]

edges.  Two edges from different supporting lines cross at most once, so

\[
\operatorname{cr}(G)\le\binom L2<L^2/2.
\]

### Theorem PX457 -- PROVED

For every finite point set and line set,

\[
\boxed{
I(P,\mathcal L)
\le
4M^{2/3}L^{2/3}+4M+L.
}
\]

### Proof

If `e<4M`, the result follows from `I=e+L`.
Otherwise PX456 and the crossing upper bound give

\[
\frac{e^3}{64M^2}
<
\frac{L^2}{2},
\]

hence

\[
e<32^{1/3}M^{2/3}L^{2/3}<4M^{2/3}L^{2/3}.
\]

Add `L`.  The displayed form includes the first case simultaneously. \(\square\)

Coincident edges do not occur: two distinct points determine one supporting
line.  Standard infinitesimal perturbation at incidence vertices separates
crossings without increasing their number.

## 3. Rich-line count

Let `L_k` be the number of lines containing at least `k>=2` points of a fixed
`M`-point set.

### Theorem PX458 -- PROVED

For every `k>=2`,

\[
\boxed{
L_k
\le
\frac{512M^2}{(k-1)^3}
+
\frac{8M}{k-1}.
}
\]

### Proof

Apply PX457 to the `L_k` rich lines:

\[
kL_k
\le
4M^{2/3}L_k^{2/3}+4M+L_k.
\]

Thus

\[
(k-1)L_k
\le
4M^{2/3}L_k^{2/3}+4M.
\]

At least one right-hand term is at least half the left side.  In the first case,

\[
L_k^{1/3}
\le
\frac{8M^{2/3}}{k-1},
\]

and in the second,

\[
L_k\le\frac{8M}{k-1}.
\]

The sum of the two case bounds is valid uniformly. \(\square\)

## 4. Explicit Cartesian triple bound

Let `R,C` be real coordinate sets with

\[
|R|=|C|=t.
\]

The point set `R times C` has `M=t^2` points and at most `t` points on one
nonaxis or axis line.

### Theorem PX459 -- PROVED

For every `t>=2`, the total number of unordered collinear triples in
`R times C` is at most

\[
\boxed{
320t^4\log(2t).
}
\]

Consequently the compatible support-five/six rank-three weight satisfies

\[
\boxed{
W_{3,5}+W_{3,6}
\le
320t^4\log(2t),
}
\]

so PX333 may take `A_3=320`.

### Proof

For a line with `r` points,

\[
\binom r3
=
\sum_{k=3}^r\binom{k-1}{2}.
\]

Therefore the total triple count is

\[
T
=
\sum_{k=3}^t\binom{k-1}{2}L_k.
\]

Use PX458 with `M=t^2`.  The cubic rich-line term contributes at most

\[
256t^4
\sum_{j=2}^{t-1}\frac1j
\le
256t^4H_t.
\]

The linear rich-line term contributes at most

\[
4t^2\sum_{j=2}^{t-1}(j-1)
\le
2t^4.
\]

Since `H_t<=1+log t` and, for `t>=2`,

\[
256(1+\log t)+2
\le
320\log(2t),
\]

the first display follows.  Compatible support-five/six triples are a subfamily
of all collinear triples. \(\square\)

### Corollary PX460 -- PROVED

The cutoff audit PX453 no longer needs an unspecified incidence constant.  It
may set

\[
\boxed{A_3=320.}
\]

The remaining effective witnesses are:

1. an explicit divisor threshold `(rho,N_div)`;
2. an exact nested-depth envelope `d_*(N)`.

## 5. Verification

Run

```bash
python scripts/verify_product_explicit_cartesian_triples.py
```

The verifier checks the crossing-lemma algebra, the rich-line case split, the
harmonic summation, the constant `320`, and exhaustive Cartesian grids of small
order.
