# Pseudorandom almost-strong-complete seeds

PX138 identifies strong-complete mappings with perfect matchings of the linear
four-partite hypergraph

\[
e(x,y)=(x,y,x-y,x+y).
\]

The exact seed conjecture remains a perfect-matching problem. This chapter shows
that its pseudorandomness part can already be achieved asymptotically before the
last absorption step.

The external input is Theorem 1.3 of Ehard, Glock and Joos,
*Pseudorandom hypergraph matchings* (2019, arXiv:1907.09946). In the form used
here, an \(r\)-uniform hypergraph of maximum degree \(\Delta\), polynomially
smaller codegree, and not too many edges has a matching which simultaneously
tracks every prescribed clean tuple weight of bounded rank, provided the total
weight dominates each lower-rank concentration norm by the stated power of
\(\Delta\).

## 1. Partial secant and triangle multiplicities

Let \(M\) be a matching of \(\mathcal H_p\). Its selected edges are grid points.
For an allowed slope

\[
r\notin\{0,1,-1\},
\]

let \(\mu_M(r)\) be the number of ordered pairs of distinct selected points with
secant slope \(r\).

For a compatible affine-triangle shape

\[
\sigma=(r,t,s),
\qquad t,s\notin\{0,1\},
\]

let \(\tau_M(\sigma)\) be the number of ordered selected triples satisfying the
PX129 row and image ratio equations.

Compatibility means that the three formal points have distinct row, column,
difference and sum coordinates. Equivalently, besides the displayed exclusions,

\[
t\ne rs,
\quad t-1\ne r(s-1),
\quad t\ne-rs,
\quad t-1\ne-r(s-1).
\]

## Theorem PX141 -- PROVED USING AN EXTERNAL MATCHING THEOREM

For every fixed \(\eta\in(0,1)\), there is \(p_0(\eta)\) such that every prime
\(p\ge p_0(\eta)\) has a matching \(M\subseteq\mathcal H_p\) satisfying

\[
|M|=(1\pm p^{-\eta/28800})p,
\]

and, simultaneously for every allowed slope and every compatible affine shape,

\[
\boxed{
\mu_M(r)=(1\pm p^{-\eta/28800})(p-1)
}
\]

and

\[
\boxed{
\tau_M(\sigma)\le p^\eta.
}
\]

Thus \(M\) is an almost-full partial strong-complete mapping with asymptotically
optimal secant multiplicities and subpower affine-triangle multiplicities.

### Proof

Set

\[
\delta=\eta/4,
\qquad
\varepsilon=\frac{\delta}{50\cdot3^2\cdot4^2}
=\frac{\eta}{28800}.
\]

PX139 gives

\[
\Delta(\mathcal H_p)=p,
\qquad
\Delta^c(\mathcal H_p)=1\le p^{1-\delta},
\qquad
|E(\mathcal H_p)|=p^2.
\]

Hence the host satisfies the structural hypotheses of the Ehard--Glock--Joos
theorem for all sufficiently large \(p\).

### Matching size

Use the constant edge weight. Its total mass is \(p^2\), so the matching theorem
gives

\[
|M|=(1\pm p^{-\varepsilon})\frac{p^2}{p}
=(1\pm p^{-\varepsilon})p.
\]

### Secant weights

For one allowed slope \(r\), put weight one on every unordered compatible pair
of host edges with slope \(r\). There are exactly

\[
\frac{p^2(p-1)}2
\]

such pairs. A fixed host edge belongs to exactly \(p-1\) of them, and a fixed
pair has weight at most one. The tuple-weight hypotheses therefore hold. The
matching theorem gives

\[
\frac12\mu_M(r)
=(1\pm p^{-\varepsilon})
\frac{p^2(p-1)/2}{p^2},
\]

which is the stated secant estimate. There are only \(p\) slope weights, so they
may all be included simultaneously.

### Padded triangle weights

Fix a compatible shape \(\sigma\). Let \(\theta_\sigma\) be the clean
three-tuple weight whose value on an unordered triple is the number of its
orderings which realize \(\sigma\). Its total mass is exactly

\[
p^2(p-1),
\]

but this is only order \(p^3\), the same scale as \(\Delta^3\), so the direct
rank-three concentration hypothesis has no power margin.

Let \(J\) be the clean weight which is one on every unordered triple of pairwise
compatible host edges. Then

\[
J(E(\mathcal H_p))=\Theta(p^6),
\]

with concentration norms

\[
\|J\|_1=O(p^4),
\qquad
\|J\|_2=O(p^2),
\qquad
\|J\|_3=1.
\]

Put

\[
\alpha=p^{-3+\eta/2}
\]

and use the padded weight

\[
W_\sigma=\theta_\sigma+\alpha J.
\]

Its total mass is \(\Theta(p^{3+\eta/2})\). For ranks one, two and three, this
exceeds the corresponding concentration norm times
\(p^{k+\delta}\), because \(\eta/2>\delta\). Thus every padded shape weight is
admissible. There are only \(O(p^3)\) shapes, far below the theorem's allowed
number of simultaneous weights.

The matching theorem yields

\[
W_\sigma(M)
=(1\pm p^{-\varepsilon})
\frac{W_\sigma(E(\mathcal H_p))}{p^3}.
\]

Since \(M\) is a matching,

\[
J(M)=\binom{|M|}{3}.
\]

Subtracting the known padding contribution and using the matching-size estimate
gives

\[
\theta_\sigma(M)=O(p^{\eta/2})+O(p^{\eta/2-\varepsilon}).
\]

For sufficiently large \(p\), this is at most \(p^\eta\). By definition,
\(\theta_\sigma(M)=\tau_M(\sigma)\). \(\square\)

## 2. What remains

PX141 proves that the exact-cover host itself has enough pseudorandom matching
entropy. The remaining issue is completion.

The matching leaves at most

\[
O(p^{1-\eta/28800})
\]

vertices uncovered in each part. An arbitrary completion can destroy the
secant and triangle bounds, so the missing theorem is not merely the existence
of some perfect matching. It is one of the following stronger statements.

1. A spread absorber which completes the pseudorandom matching while adding only
   controlled secant and triangle load.
2. An iterative pseudorandom nibble whose final leftover has bounded size and a
   bounded-support exact completion.
3. A direct perfect-matching version of the Ehard--Glock--Joos theorem for the
   algebraic host \(\mathcal H_p\).

This separates the asymptotic seed conjecture into a solved almost-matching part
and an exact absorption part.

## 3. Verification

The finite host and tuple-weight counts used above are checked by

```bash
python scripts/verify_product_pseudorandom_almost_seed.py
```

The asymptotic concentration conclusion uses the cited external theorem.
