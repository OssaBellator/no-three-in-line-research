# Direction-stratified conflict barrier for rectangle matchings

The universal low-syndrome theorem PX63 turns every saturated side-`n` factor
into a factor-compatible rectangle state with only `O(n log n)` defects.  A
natural next step is to apply a conflict-free perfect-matching theorem directly
to the complete four-partite rectangle hypergraph.  This chapter identifies the
exact obstruction to that black-box approach.

The obstruction is not the degree or ordinary codegree of the matching
hypergraph.  It is a family of compatible rectangle pairs whose connecting
corner line has very small primitive height.  Such a pair can have order
`n^3`, rather than power-saving, many transversal completions.

Throughout, let

\[
\mathcal K_n=U\times P\times T\times R
\]

be the complete four-partite 4-graph from PX43.  An edge

\[
e=(u,p,t,r)
\]

represents one four-corner rectangle.  The degree of every vertex of
`\mathcal K_n` is

\[
d=n^3,
\]

and the ordinary maximum codegree is `n^2`.

## 1. Primitive height of a rectangle pair

For distinct scalar grid points `x,y`, write

\[
y-x=k(a,b),
\]

where `(a,b)` is primitive and `k` is a nonzero integer.  Define

\[
\operatorname{ht}(x,y)=\max(|a|,|b|).
\]

Fix one of the four radix orientations.  For compatible rectangle edges `e,f`,
define

\[
h(e,f)=
\min\{\operatorname{ht}(x,y):
 x\text{ is a corner of }e,
 y\text{ is a corner of }f\}.
\]

Compatibility means that the four abstract coordinates of `e` and `f` are
coordinatewise distinct, as required for two edges to coexist in a matching.

### Lemma PX81 -- PROVED

Let `L` be a scalar line of primitive height `h`.  Its intersection with any one
of the four scalar corner blocks contains at most

\[
1+\frac{2n}{h}
\]

points.

### Proof

Any two scalar grid points on `L` differ by a nonzero integer multiple of its
primitive direction.  Consecutive such points are separated by at least `h` in
one coordinate.  Every corner block lies inside a box of side less than `2n`,
so at most `1+2n/h` multiples can occur.  Fine-major parity restrictions only
remove points and therefore cannot increase the bound. \(\square\)

## 2. Transversal completion codegree

A transversal conflict consists of three compatible rectangle edges and one
chosen corner from each edge lying on one real scalar line.

### Theorem PX82 -- PROVED

For every compatible pair `e,f`, the number of rectangle edges `g` which are
compatible with both and form at least one transversal conflict satisfies

\[
\boxed{
\operatorname{codeg}_{\rm trans}(e,f)
\le
64n^2\left(1+\frac{2n}{h(e,f)}\right).
}
\]

In particular, if

\[
h(e,f)\ge n^\delta,
\qquad 0<\delta\le1,
\]

then

\[
\operatorname{codeg}_{\rm trans}(e,f)
\le 192n^{3-\delta}
=192d^{1-\delta/3}.
\]

### Proof

There are sixteen choices of a corner of `e` and a corner of `f`, hence at most
sixteen connecting scalar lines.  For each such line there are four possible
corner types for `g`.

Fix one connecting line and one corner type of `g`.  By PX81, at most
`1+2n/h(e,f)` scalar points of that corner block lie on the line.  Fixing one
such scalar corner fixes two of the four abstract coordinates of `g`; the other
two have at most `n^2` choices.  Compatibility can only reduce this number.
Multiplying the sixteen connecting lines, four third-corner types, scalar
intersection bound, and `n^2` free-coordinate bound gives the result. \(\square\)

Thus every high-height pair has the polynomial transversal-codegree saving
needed by modern conflict-free matching processes.

## 3. The low-height obstruction is full order

The preceding bound cannot be replaced by a uniform power saving.

### Theorem PX83 -- PROVED

For every `n>=3` and every radix orientation, there are compatible rectangle
edges `e,f` with at least

\[
\boxed{(n-2)^3}
\]

compatible transversal completions.  Consequently the complete rectangle
conflict system has

\[
\Delta_2(\mathcal C^{(3)})=\Theta(n^3)=\Theta(d).
\]

### Proof

Take

\[
e=(0,0,0,0),
\qquad
f=(1,1,1,1).
\]

Their corner of type `(0,0)` lies at a scalar point of the form

\[
(c_x u,c_y t),
\qquad c_x,c_y\in\{1,2\},
\]

where the constants depend only on the two radix modes.  Hence the corresponding
corners of `e` and `f` are `(0,0)` and `(c_x,c_y)`.

For every

\[
w,p,r\in\{2,\ldots,n-1\},
\]

put

\[
g=(w,p,w,r).
\]

The three `(0,0)` corners are

\[
(0,0),
\quad(c_x,c_y),
\quad(wc_x,wc_y),
\]

and are collinear.  The edge `g` is coordinatewise disjoint from both `e` and
`f`.  There are exactly `(n-2)^3` such choices.  The upper bound
`O(n^3)` follows from PX82 with `h(e,f)>=1`. \(\square\)

This is the precise reason that the published conflict-free hypergraph matching
theorems cannot be applied directly to the unfiltered rectangle conflict
system: their bounded-conflict hypotheses require a polynomial saving in the
codegree of rank-three conflicts, while PX83 gives codegree of the same order as
the base degree.

## 4. Low-direction filtering tradeoff

For a height cutoff `H>=2`, call a compatible pair `H`-low if

\[
h(e,f)<H.
\]

### Theorem PX84 -- PROVED

For every rectangle edge `e`, the number of `H`-low compatible partners is at
most

\[
\boxed{256Hn^3}.
\]

After declaring every `H`-low pair to be a rank-two conflict, every remaining
compatible pair has transversal completion codegree at most

\[
\boxed{64n^2\left(1+rac{2n}{H}\right)}.
\]

### Proof

Fix one corner `x` of `e` and one corner type for a possible partner.  For every
primitive height `q<H`, there are at most `8q` oriented primitive directions of
height `q`, and at most `2n/q` nonzero multiples remaining inside the scalar
grid.  Hence fewer than

\[
\sum_{q=1}^{H-1}8q\frac{2n}{q}
<16nH
\]

candidate scalar corners have height below `H` from `x`.

Each candidate scalar corner fixes two coordinates of the partner rectangle and
leaves at most `n^2` choices.  There are four choices for `x` and four partner
corner types.  This gives at most

\[
4\cdot4\cdot16nH\cdot n^2
=256Hn^3
\]

partners.  The second assertion is PX82 with `h(e,f)>=H`. \(\square\)

## 5. Why a simple cutoff is still insufficient

The cutoff theorem exposes a quantitative tension.

- The base degree is `d=n^3`.
- Taking `H=n^delta` gives the desired rank-three codegree bound
  `O(d^(1-delta/3))`.
- But the available rank-two degree bound becomes
  `O(Hd)=O(d^(1+delta/3))`, rather than `O(d)`.
- Keeping `H` bounded preserves rank-two boundedness but leaves rank-three
  codegree `Theta(d)` by PX83.

Therefore a one-parameter operation which simply converts every low-height
triple interaction into a forbidden pair does not verify the standard
bounded-conflict hypotheses.  A general proof needs one additional ingredient:

1. a direction-aware process which can tolerate many low-height pair labels;
2. a structured construction avoiding all low-height pair directions;
3. an absorber which handles the low-height part after a high-height
   conflict-free matching; or
4. a repair theorem applied to the PX63 low-syndrome state.

The first three options now connect directly to the finite-direction affine
machinery A1--A3.  The remaining bottleneck is no longer an undifferentiated
large conflict codegree: it is the low-primitive-height sector alone.

## 6. Verification

Run

```bash
python scripts/verify_product_direction_stratification.py
```

The verifier checks the line-intersection estimate on small grids, verifies the
canonical `(n-2)^3` completion family in all four orientations, computes its
exact completion count through base seven, and checks PX82 on deterministic
samples of compatible pairs.