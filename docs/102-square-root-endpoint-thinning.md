# Square-root thinning removes the rematching logarithm universally

PX183--PX184 show that the full uniform rematching bank can have
\(\Theta(t\log t)\) expected internal collateral. PX185--PX188 remove the
logarithm on arithmetic endpoint blocks. This chapter gives a universal
alternative: retain only a square-root-sized subset of the movable endpoints.

The selected block loses size, but its complete row-column candidate grid has
only \(O(s^4)\) compatible collinear triples. Therefore the usual
\(128/(s)_3\)-spread matching bank has only \(O(s)\) expected internal
collateral.

Let

\[
A=\{(x_i,y_i):i\in[t]\}
\]

be endpoints from one permutation layer, so the \(x_i\) are distinct and the
\(y_i\) are distinct. For \(J\subseteq[t]\), put

\[
R_J=\{x_i:i\in J\},
\qquad
C_J=\{y_i:i\in J\}.
\]

Write \(T(J)\) for the number of collinear triples in

\[
R_J\times C_J
\]

having distinct rows and columns.

## 1. Full candidate-grid bound

A standard Szemerédi--Trotter consequence states that a planar point set of
size \(N\), with at most \(\ell\) points on one line, spans

\[
O(N^2\log\ell+\ell^2N)
\]

collinear triples. Apply this to

\[
R\times C,
\qquad |R|=|C|=t.
\]

There are \(N=t^2\) points and every nonaxis line contains at most \(t\) of
them. Hence

\[
\boxed{T([t])=O(t^4\log t).}
\]

The compatible triples can be classified by the number of endpoint indices
used. A candidate cell \((x_i,y_j)\) carries the index pair \((i,j)\). Three
compatible cells use between three and six distinct endpoint indices.

Let \(N_u\) be the number using exactly \(u\) indices. Then

\[
N_3=O(t^3),
\qquad
N_4=O(t^4),
\]

and

\[
N_5+N_6=O(t^4\log t).
\]

The first two estimates are purely combinatorial: choose the union of three or
four indices, then choose the two ordered three-subsets and their matching in
only constantly many ways.

## Theorem PX189 -- PROVED

For every sufficiently large \(t\), every endpoint family \(A\) contains a
subset \(J\) satisfying

\[
\boxed{|J|\ge\frac12\sqrt t}
\]

and

\[
\boxed{T(J)=O(|J|^4).}
\]

### Proof

Retain every endpoint index independently with probability

\[
q=t^{-1/2}.
\]

The expected selected size is \(\sqrt t\), and Chernoff's inequality gives

\[
\Pr\left(|J|<\frac12\sqrt t\right)=o(1).
\]

A candidate triple using \(u\) endpoint indices survives with probability
\(q^u\). Therefore

\[
\begin{aligned}
\mathbb E T(J)
&=
q^3N_3+q^4N_4+q^5N_5+q^6N_6\\
&=
O(t^{3/2})
+O(t^2)
+O(t^{3/2}\log t)
+O(t\log t)\\
&=O(t^2).
\end{aligned}
\]

Markov's inequality and the size concentration hold simultaneously with
positive probability. For such a realization,

\[
t^2=O(|J|^4),
\]

which proves the result. \(\square\)

The theorem is deliberately stated with a square-root subset. More general
sampling exponents give a continuum of size/collateral tradeoffs, but
\(q=t^{-1/2}\) is the first scale at which all four union-size sectors are
bounded by \(O(t^2)\).

## 2. Consequence for the forbidden matching bank

Let \(F\subseteq R_J\times C_J\) be the inherited forbidden-position set. Since
it comes from the original diagonal and the opposite permutation layer, it has
row and column degree at most two.

PX73 supplies a nonempty allowed matching family whose uniform distribution
satisfies

\[
\Pr(E\subseteq M)\le\frac{128}{(|J|)_{|E|}}
\]

for every compatible partial matching \(E\).

## Theorem PX190 -- PROVED

For the subset \(J\) from PX189, the uniform allowed rematching has expected
number of internal collinear triples

\[
\boxed{
\mathbb E\Phi_{\rm internal}(M)=O(|J|).
}
\]

### Proof

Every internal triple is one of the \(T(J)=O(|J|^4)\) compatible candidate
triples. Its matching probability is at most

\[
\frac{128}{(|J|)_3}.
\]

Summing gives

\[
O\left(\frac{|J|^4}{(|J|)_3}\right)
=O(|J|).
\]

\(\square\)

## 3. Application to all first-generation decoder outcomes

The square-root subset remains a valid movable endpoint family in every
neutralization bank.

- **Clean star:** each retained endpoint destroys its original star triple.
- **Loaded line:** each retained point is moved off the loaded line and destroys
  every old line triple containing it.
- **Radial core:** each retained point is moved off its original radial line and
  destroys at least one old radial triple.

Thus the guaranteed destroyed mass remains

\[
D_*\ge |J|,
\]

while the internal rank-three collateral is only \(O(|J|)\). The logarithmic
mismatch of PX184 is gone without assuming any arithmetic structure.

This does not yet prove strict improvement: the constants and the mixed
one-/two-background-point terms still matter. But the remaining obstruction is
now fixed-rank and constant-scale rather than logarithmically divergent.

## 4. Revised second-generation target

After PX190, the neutralization program has two complementary structured tools.

1. **Large arithmetic block:** PX188 gives a deterministic conic rematching and
   an explicit mixed-shadow criterion.
2. **Arbitrary endpoint set:** PX189--PX190 give a square-root block with linear
   expected internal collateral.

The next theorem only needs to control the thinned analogues of

\[
\frac{T_1}{s},
\qquad
\frac{T_2}{(s)_2},
\]

or show that their concentration produces another executable batch. The
rank-three term is no longer the asymptotic bottleneck.

A promising refinement is to include the one- and two-background-point
certificates in the same random endpoint thinning. Their survival probabilities
depend on only one to four endpoint indices, so a second moment or alteration
argument may simultaneously keep all three normalized certificate masses at
constant scale.

## External input

The collinear-triple estimate follows from the Szemerédi--Trotter rich-line
bound. One convenient formulation is the Payne--Wood lemma: a set of \(N\)
points with at most \(\ell\) collinear spans

\[
O(N^2\log\ell+\ell^2N)
\]

collinear triples.

## Verification

Run

```bash
python scripts/verify_product_square_root_thinning.py
```

The verifier classifies candidate triples by endpoint-index union size and finds
square-root subsets with bounded \(T_3/s^4\) on arithmetic and random endpoint
families through size twenty. It also checks the four sampling exponent scales
symbolically.
