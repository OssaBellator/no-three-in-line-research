# Ambient divisor control of support-four collateral

PX205--PX206 isolate rank-two support four as the only rematching sector that can
remain superlinear after square-root endpoint thinning.  This chapter exploits
one feature not used in the support classification: all coordinates lie in one
bounded integer grid.

For a fixed background anchor, collinearity of two candidate cells is an equal-
product equation.  Integer divisor multiplicity bounds all such pairs at once.
After summing over the selected background, this pays the support-four sector on
endpoint blocks above the ambient `N^(2/3+epsilon)` scale.

Let the ambient grid be

\[
[0,N-1]^2.
\]

Let

\[
R=\{x_i:i\in[t]\},
\qquad
C=\{y_j:j\in[t]\},
\]

where both coordinate lists are injective, and write

\[
e_{ij}=(x_i,y_j).
\]

As in PX201--PX206, diagonal cells `e_(ii)` are forbidden.  Let `Z` be a
background point set disjoint from the complete candidate grid `R x C`.

Define the ambient divisor envelope

\[
\mathfrak d(N)
=
\max_{1\le m\le(N-1)^2}\tau(m),
\]

where `tau(m)` is the positive-divisor function.  The standard divisor bound
gives

\[
\mathfrak d(N)=N^{o(1)}.
\]

## 1. Fixed-anchor product energy

Fix an anchor

\[
z=(a,b)\in Z.
\]

Let `Q_z` be the number of unordered compatible candidate-cell pairs collinear
with `z`.  This count includes every endpoint-support sector, so it also bounds
the support-four contribution at `z`.

### Theorem PX207 -- PROVED

For every fixed background anchor,

\[
\boxed{
Q_z\le \mathfrak d(N)t^2.
}
\]

### Proof

A compatible collinear candidate pair cannot use the anchor row or anchor
column.  For example, if `x_i=a`, then the line through `z` and `e_(ij)` is
horizontal.  A second point on that line would have the same candidate row,
contradicting compatibility.  The column case is identical.

Put

\[
A_i=x_i-a,
\qquad
B_j=y_j-b.
\]

For a compatible pair `e_(ij),e_(k ell)` collinear with `z`, all four relevant
differences are nonzero and

\[
\boxed{
A_iB_\ell=A_kB_j.
}
\]

For every nonzero integer `p`, let

\[
r_z(p)
=
|\{(i,\ell):A_iB_\ell=p\}|.
\]

Because the `A_i` are distinct, a representation is determined by choosing the
signed divisor `A_i` of `p`.  Hence

\[
r_z(p)\le2\tau(|p|)\le2\mathfrak d(N).
\]

Also

\[
\sum_p r_z(p)\le t^2.
\]

Every unordered compatible collinear pair gives two ordered distinct
representations of the same product, namely

\[
((i,\ell),(k,j))
\quad\text{and}\quad
((k,j),(i,\ell)).
\]

Therefore

\[
\begin{aligned}
2Q_z
&\le
\sum_p r_z(p)(r_z(p)-1)\\
&\le
2\mathfrak d(N)\sum_p r_z(p)\\
&\le
2\mathfrak d(N)t^2.
\end{aligned}
\]

Divide by two. \(\square\)

The proof is insensitive to the forbidden-position graph and to the support
pattern.  It is a pure integer-lift bound on one anchor pencil.

## 2. Summed support-four load

Weight a compatible candidate pair by the number of anchors in `Z` completing
it to a collinear triple, as in PX203a and PX206.  Let `W_(2,4)` be the total
weight of the support-four sector before thinning.

### Theorem PX208 -- PROVED

One has

\[
\boxed{
W_{2,4}\le |Z|\mathfrak d(N)t^2.
}
\]

If `Z` is contained in a saturated selected state, then `|Z|<=2N`, and hence

\[
\boxed{
W_{2,4}\le2N\mathfrak d(N)t^2.
}
\]

Assume `t>=1024`, choose the square-root-thinned block supplied by PX201, and
write its order as `s`.  If its forbidden graph has maximum degree `Delta` and
`s>=8Delta`, then the uniform allowed rematching satisfies

\[
\boxed{
\mathbb E T_{2,4}
\le
256e^{4\Delta}\frac{|Z|\mathfrak d(N)}t.
}
\]

Consequently,

\[
\boxed{
\frac{\mathbb E T_{2,4}}s
\le
512e^{4\Delta}
\frac{|Z|\mathfrak d(N)}{t^{3/2}}.
}
\]

For a saturated background this becomes

\[
\boxed{
\frac{\mathbb E T_{2,4}}s
\le
1024e^{4\Delta}
\frac{N\mathfrak d(N)}{t^{3/2}}.
}
\]

### Proof

Count the weighted pair-anchor incidences by anchors rather than by candidate
pairs.  PX207 gives at most `mathfrak d(N)t^2` compatible pairs through each
anchor, proving the first display.  A saturated `N x N` state contains at most
`2N` selected points, proving the second.

PX203a bounds the support-four expectation by

\[
256e^{4\Delta}\frac{W_{2,4}}{t^3}.
\]

Substitute the first bound.  Finally PX201 gives

\[
s\ge\frac12\sqrt t,
\]

which gives the two normalized estimates. \(\square\)

### Corollary PX208a -- PROVED

Fix a recursion depth, so `Delta=O(1)`, and fix `epsilon>0`.  If

\[
\boxed{
t\ge N^{2/3+\epsilon},
}
\]

then

\[
\boxed{
\mathbb E T_{2,4}=o(s).
}
\]

More explicitly, the support-four sector is at most the destroyed-mass scale
whenever

\[
\boxed{
t^{3/2}
\ge
1024e^{4\Delta}N\mathfrak d(N).
}
\]

### Proof

The standard divisor estimate gives `mathfrak d(N)=N^(o(1))`, while

\[
\frac{N}{t^{3/2}}
\le
N^{-3\epsilon/2}.
\]

Apply PX208. \(\square\)

Thus the allegedly unique superlinear rank-two sector is not an obstruction on
large endpoint blocks.  The unresolved range is now

\[
t\le N^{2/3+o(1)}.
\]

## 3. Divisor loss is genuinely necessary

The fixed-anchor theorem cannot be improved to an absolute `O(t^2)` estimate
for arbitrary integer endpoint sets.

### Theorem PX209 -- PROVED

For every `t`, take

\[
x_i=y_i=2^i
\qquad(0\le i<t)
\]

inside a grid of side `N=2^(t-1)+1`, and take the single anchor `z=(0,0)`.
Then the number of support-four candidate pairs through `z` is

\[
\boxed{
2\sum_{d=1}^{t-1}
\left[
\binom{t-d}{2}-\max(t-2d,0)
\right]
=
\Theta(t^3).
}
\]

### Proof

For every nonzero difference `d`, the line of slope `2^d` contains exactly the
candidate cells

\[
e_{i,i+d}
\qquad
(0\le i<t-d)
\]

when `d>0`, with the analogous family for negative `d`.  There are `t-d` cells
on the positive-slope class.

Two distinct cells in this class fail support four exactly when their directed
arcs share an endpoint.  Apart from equality, this occurs precisely when their
starting indices differ by `d`, giving `max(t-2d,0)` overlapping pairs.  Hence
the positive and negative classes together contribute the displayed sum.

The first summand totals

\[
2\sum_{d=1}^{t-1}\binom{t-d}{2}
=
2\binom t3,
\]

while the overlap correction is `O(t^2)`.  Therefore the total is
`Theta(t^3)`. \(\square\)

In this example the equal-product multiplicity is itself of order `t`, exactly
matching the growth permitted by the divisor envelope.  Any stronger theorem
must use either the bounded ambient side, the size and structure of the
background set, or decoder-specific information beyond arbitrary endpoint
coordinates.

## 4. Updated support-four frontier

PX207--PX209 split the former support-four problem into two ranges.

1. **Large blocks:** if `t>=N^(2/3+epsilon)`, ambient divisor energy makes the
   entire support-four contribution `o(s)` after square-root thinning.
2. **Small and medium blocks:** if `t<=N^(2/3+o(1))`, the divisor estimate alone
   does not pay the destroyed-mass scale.  This is the remaining decoder range.
3. **Sharp arithmetic obstruction:** one anchor may already support
   `Theta(t^3)` pairs, so a uniform fixed-anchor `O(t^2)` theorem is false.

The next useful statement should therefore be scale-sensitive.  It may either:

- extract additional structure when a decoder endpoint has
  `t<=N^(2/3+o(1))` and large support-four load;
- combine several medium endpoint blocks into one batch whose total destroyed
  mass exceeds the divisor-controlled collateral; or
- prove that repeated PX195 extraction necessarily reaches the large-block
  regime in bounded depth.

## 5. Verification

Run

```bash
python scripts/verify_product_support_four_divisor.py
```

The verifier checks the equal-product upper bound on random integer endpoint
sets and anchors, computes the ambient divisor envelope exactly at small sides,
verifies the geometric-progression formula and its cubic growth, and checks the
`N^(2/3+epsilon)` exponent saving.