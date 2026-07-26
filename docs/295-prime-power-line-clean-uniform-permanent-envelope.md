# Line-clean response graphs contain a spanning regular core

CMR1526--CMR1533 make every extension-free line-clean response row an exact
rook-class dot product.  The denominator still depends on the deleted line
trace.  This chapter gives one host-uniform lower bound.

The forbidden board is the union of the fixed opposite matching, one deleted
partial matching, and the target edge.  Every cut rectangle therefore loses at
most two matching-widths plus one edge.  The remaining allowed graph satisfies
the exact capacitated Hall inequalities for a spanning `(d-3)`-factor.  Van der
Waerden then gives a uniform permanent denominator, rank-one through rank-three
prescription bounds, and one explicit target-versus-collateral criterion.

Fix `d>=4`, a perfect matching `O` of `K_{d,d}`, a target edge `e notin O`, and a
partial matching

\[
X\subseteq E(H_e),
\qquad
H_e=K_{d,d}\setminus(O\cup\{e\}).
\]

Put

\[
F=O\cup X\cup\{e\},
\qquad
G=K_{d,d}\setminus F,
\qquad
q=d-3.
\]

For the geometric application, `X` is the complete allowed trace of one
nonaxis real line.

## 1. Forbidden rectangles lose at most two matching widths and one edge

Let `A` be a source set and `C` a target set.  Write

\[
x=|A|,
\qquad
z=|C|,
\qquad
m=\min\{x,z\}.
\]

### Theorem CMR1534 -- PROVED

\[
\boxed{
|F\cap(A\times C)|\le 2m+1.
}
\]

Consequently

\[
\boxed{
|E(G)\cap(A\times C)|
\ge xz-2m-1.
}
\]

### Proof

The perfect matching `O` contributes at most `m` edges to the rectangle.  The
partial matching `X` contributes at most another `m`.  The single target edge
contributes at most one.  Subtract from the `xz` cells of the rectangle. ∎

The estimate deliberately ignores overlaps between the three forbidden parts;
such overlaps can only improve it.

## 2. Capacitated Hall inequality

Let `B` be a target set and put

\[
C=R\setminus B,
\qquad
z=d-|B|.
\]

### Theorem CMR1535 -- PROVED

For every source set `A` and target set `B`,

\[
\boxed{
|E(G)\cap(A\times(R\setminus B))|
\ge
q\bigl(|A|-|B|\bigr)
}
\]

whenever `|A|>|B|`.  When `|A|<=|B|` the right side is nonpositive and the
inequality is automatic.

### Proof

Write `x=|A|`, `z=d-|B|`, `m=min{x,z}` and `M=max{x,z}`.  The hypothesis
`x>|B|` is equivalent to

\[
m+M>d.
\]

CMR1534 gives the lower bound

\[
m(M-2)-1.
\]

Set

\[
\alpha=d-M,
\qquad
\beta=d-m.
\]

Then `0<=alpha<=beta` and `alpha+beta<d`.  Subtracting the required quantity
`(d-3)(m+M-d)` from the displayed lower bound gives

\[
d-1+\alpha\beta-3\alpha-\beta.
\]

If `beta>=2`, use `d>=alpha+beta+1` to bound this from below by

\[
\alpha(\beta-2)\ge0.
\]

If `beta=0`, then `alpha=0` and the expression is `d-1`.  If `beta=1`, then
`alpha` is zero or one, giving `d-2` or `d-4`; both are nonnegative because
`d>=4`. ∎

## 3. A spanning `(d-3)`-factor

### Theorem CMR1536 -- PROVED

The line-clean allowed graph `G` contains a spanning `q`-regular bipartite
subgraph with

\[
\boxed{q=d-3.}
\]

### Proof

Use the standard integral flow network:

- source to every left vertex, capacity `q`;
- every allowed edge of `G`, capacity one;
- every right vertex to the sink, capacity `q`.

A cut determined by source-side vertex sets `A` on the left and `B` on the
right has capacity

\[
q(d-|A|)
+
|E(G)\cap(A\times(R\setminus B))|
+
q|B|.
\]

CMR1535 says this is at least `qd`.  Hence the maximum flow has value `qd`.
Integral capacities give an integral flow, whose unit-flow allowed edges form
a spanning `q`-factor. ∎

The degree `d-3` is optimal at vertices incident with all three forbidden
parts.

## 4. Uniform permanent denominator

Define

\[
\kappa_d^{\rm line}
=
\left(\frac d{d-3}\right)^d.
\]

### Theorem CMR1537 -- PROVED

The line-clean response family obeys

\[
\boxed{
|\operatorname{PM}(G)|
\ge
 d!\left(\frac{d-3}{d}\right)^d.
}
\]

### Proof

Let `J` be the spanning `(d-3)`-regular subgraph from CMR1536 and let `A_J` be
its adjacency matrix.  Then `A_J/(d-3)` is doubly stochastic.  Van der Waerden
gives

\[
\operatorname{per}\left(\frac{A_J}{d-3}\right)
\ge
\frac{d!}{d^d}.
\]

Thus

\[
|\operatorname{PM}(J)|
=
\operatorname{per}(A_J)
\ge
 d!\left(\frac{d-3}{d}\right)^d.
\]

Every perfect matching of `J` is a line-clean response in `G`. ∎

This denominator is weaker than the exact component rook denominator of
CMR1530 but is independent of the line trace and its path/cycle type.

## 5. Host-uniform prescription probabilities

Let `P` be any compatible allowed rank-`r` prescription, with `1<=r<=3`.
Let `R` be uniform on `PM(G)`.

### Theorem CMR1538 -- PROVED

\[
\boxed{
\Pr(P\subseteq R)
\le
\frac{\kappa_d^{\rm line}}{(d)_r}.
}
\]

Equivalently one may take the smaller bound

\[
\min\left\{1,
\frac{\kappa_d^{\rm line}}{(d)_r}
\right\}.
\]

### Proof

At most `(d-r)!` perfect matchings of the complete residual board contain `P`.
Divide by the CMR1537 denominator:

\[
\Pr(P\subseteq R)
\le
\frac{(d-r)!}
{d!((d-3)/d)^d}
=
\frac{(d/(d-3))^d}{(d)_r}.
\]

∎

## 6. Uniform line-clean collateral envelope

Let `V_r^{\rm off}` count genuinely new off-line candidate triples whose
residual response prescription has rank `r`, with old response-layer subsets
removed as in CMR1222--CMR1224.  Put

\[
\mathcal C_{\rm off}^{\rm line}
=
\frac{V_1^{\rm off}}d
+
\frac{V_2^{\rm off}}{(d)_2}
+
\frac{V_3^{\rm off}}{(d)_3}.
\]

### Theorem CMR1539 -- PROVED

For the uniform line-clean response,

\[
\boxed{
\mathbb E N_{\rm off}(R)
\le
\kappa_d^{\rm line}
\mathcal C_{\rm off}^{\rm line}.
}
\]

### Proof

Apply CMR1538 to every corrected candidate prescription and sum by residual
rank.  Candidate prescriptions using a deleted line cell have probability zero
and are not included. ∎

This is the requested host-uniform upper bound for the exact CMR1533 rook dot
product.  The exact component expression may still be used whenever it is
smaller.

## 7. Restricted-host and strict-improvement criterion

Let `U` be the set of line-clean allowed edges unavailable in the current
response host, put `b=|U|`, and let the current potential be `m`.  Let
`D_S(e)` be the old target load destroyed by omitting `e`.

### Theorem CMR1540 -- PROVED

If

\[
\boxed{
\kappa_d^{\rm line}
\left[
\mathcal C_{\rm off}^{\rm line}
+
\frac{(m+1)b}{d}
\right]
<
D_S(e),
}
\]

then some line-clean response is feasible in the restricted host and has
strictly smaller potential.

### Proof

By CMR1538 with `r=1`,

\[
\mathbb E|R\cap U|
\le
\kappa_d^{\rm line}\frac bd.
\]

Together with CMR1539, the hypothesis makes the expectation of

\[
N_{\rm off}(R)+(m+1)|R\cap U|
\]

strictly smaller than `D_S(e)`.  Choose a response below that expectation.  If
it used an unavailable edge, the displayed integer quantity would be at least
`m+1`, while `D_S(e)<=m`; hence the chosen response is feasible.  It omits `e`,
destroys at least `D_S(e)` old credits, creates no line-local collateral by
CMR1515, and creates fewer than `D_S(e)` off-line credits.  Its potential is
strictly smaller. ∎

## 8. Uniform line-clean endpoint

### Corollary CMR1541 -- PROVED

For every response side `d>=4`, every target edge outside the opposite
matching, and every deleted allowed partial matching:

1. the allowed graph contains a spanning `(d-3)`-factor;
2. its response count is at least
   \[
   d!((d-3)/d)^d;
   \]
3. every rank-one through rank-three prescription has the uniform probability
   bound of CMR1538;
4. the exact CMR1533 off-line rook row is dominated by the explicit envelope
   CMR1539;
5. CMR1540 is a host-uniform strict-improvement test after complete line
   cleaning.

Thus the first numerical recurrent-row frontier now has a closed coefficient

\[
\boxed{\kappa_d^{\rm line}=(d/(d-3))^d.}
\]

What remains is to compare this envelope, or the sharper exact component row,
with the available destroyed-credit load in every geometric class, and to
calibrate the return, persistent-selector, trace and root/fixed-interface rows.
No all-`n` theorem is claimed.

Capacitated Hall cuts, integral factors, permanent lower bounds, exact
prescription ratios and synthetic collateral envelopes are checked in
[`scripts/verify_prime_power_line_clean_uniform_permanent.py`](../scripts/verify_prime_power_line_clean_uniform_permanent.py).
