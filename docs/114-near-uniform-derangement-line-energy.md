# Near-uniform derangements and line-energy extremality

The rich-line first moment PP3lh used the coarse one-cell spread constant
\(K=O(1)\). The permutation local lemma actually gives a sharper bound in terms
of its local bad-event mass \(\lambda\). When fixed points are forbidden, every
current line incidence is removed deterministically, so only off-diagonal energy
must be paid.

This chapter shows that line-energy failure is nearly extremal: almost every
target cell must lie on exactly one current owner line and must be reachable by
almost every owner through some replacement.

## 1. Mass-sensitive conditioned spread

Use the canonical bad-event family of PP3ix, with local resource mass
\(\lambda\le1/24\), and activities

\[
x_E=2\Pr(E).
\]

### Proposition PP3nk -- PROVED FROM THE PUBLISHED LLL-DISTRIBUTION THEOREM

For every prescribed matching \(F\) of rank \(r\le3\),

\[
\boxed{
\Pr(F\subseteq\pi\mid\text{avoid }\mathcal L)
\le
\frac{\exp(8r\lambda)}{(q)_r}.
}
\]

#### Proof

A rank-\(r\) cylinder uses \(r\) left and \(r\) right resources. The total
probability mass of bad events conflicting with it is at most \(2r\lambda\), so
the total activity is at most \(4r\lambda\). The LLL-distribution theorem
multiplies the unconditioned cylinder probability by

\[
\prod_{E\sim F}(1-x_E)^{-1}.
\]

Since \(x_E\le1/2\) and \(-\log(1-x)\le2x\), this product is at most
\(\exp(8r\lambda)\). ∎

For \(\lambda=o(1)\), the conditioned fixed-rank law is
\((1+o(1))/(q)_r\), rather than merely \((3/q)^r\).

## 2. Diagonal-free line-energy estimate

Use the owner-line matrix of PP3lg:

\[
h_{ij}
=
|\{a\in\mathcal A:
a,z_i,(x_i,y_j)\text{ are collinear}\}|.
\]

Put

\[
H_0=\sum_i h_{ii},
\qquad
\mathcal W=\sum_{i,j}h_{ij}.
\]

Assume every fixed point \(\pi(i)=i\) is included as a unary bad event, so the
conditioned permutation is a derangement.

### Theorem PP3nl -- PROVED

Under the conditioned distribution of PP3nk,

\[
\boxed{
\mathbb E H(\pi)
\le
\frac{e^{8\lambda}}q
\bigl(\mathcal W-H_0\bigr).
}
\]

Consequently an improving source-admissible endpoint permutation exists whenever

\[
\boxed{
e^{8\lambda}(\mathcal W-H_0)<qH_0.
}
\]

#### Proof

Every diagonal assignment has conditional probability zero. Every off-diagonal
assignment has conditional probability at most \(e^{8\lambda}/q\) by PP3nk with
rank one. Sum the off-diagonal matrix entries. If the expectation is below the
current integer load, some supported source-admissible derangement decreases the
load. ∎

This replaces the earlier bound \(K\mathcal W/q\) by a near-uniform factor and
subtracts the complete current diagonal credit before averaging.

## 3. Geometric assignment-energy cap

### Proposition PP3nm -- PROVED

For a fixed owner \(i\) and target cell \(a\), at most one replacement index
\(j\) satisfies

\[
a,z_i,(x_i,y_j)\text{ collinear}.
\]

Hence

\[
\boxed{
\mathcal W\le q|\mathcal A|.
}
\]

If every target cell lies on at least one current owner line, then

\[
\boxed{H_0\ge|\mathcal A|.}
\]

#### Proof

The line through \(z_i\) and \(a\) meets the fixed old column \(x_i\) in at
most one point. The selected old rows \(y_j\) are distinct, proving the first
claim. Sum over owners and target cells. The final inequality is the stated
current-incidence assumption. ∎

The Hall-derived recapture target set has the final property by definition: each
of its cells is witnessed by at least one current designated line.

## 4. Near-extremal failure structure

Put

\[
\varepsilon=e^{8\lambda}-1.
\]

### Theorem PP3nn -- PROVED

Assume the hypotheses of PP3nm and suppose the improvement inequality PP3nl
fails. Then

\[
\boxed{
1
\le
\frac{H_0}{|\mathcal A|}
\le
\frac{q(1+\varepsilon)}{q+1+\varepsilon}
}
\]

and

\[
\boxed{
\frac{\mathcal W}{q|\mathcal A|}
\ge
\frac{q+1+\varepsilon}{q(1+\varepsilon)}.
}
\]

#### Proof

Failure gives

\[
(1+\varepsilon)(\mathcal W-H_0)
\ge
qH_0.
\]

Using \(\mathcal W\le q|\mathcal A|\),

\[
(1+\varepsilon)
(q|\mathcal A|-H_0)
\ge qH_0,
\]

which rearranges to the upper bound on \(H_0/|\mathcal A|\). The lower bound is
PP3nm.

The same failure inequality gives

\[
\mathcal W
\ge
H_0\left(1+\frac q{1+\varepsilon}\right).
\]

Use \(H_0\ge|\mathcal A|\) and divide by \(q|\mathcal A|\). ∎

If \(\varepsilon<1/(q-1)\), the first displayed interval is empty, so an
improving trade is automatic.

For the natural scale \(\lambda=O(1/q)\), failure forces

\[
H_0=(1+O(1/q))|\mathcal A|
\]

and

\[
\mathcal W=(1-O(1/q))q|\mathcal A|.
\]

Thus almost every target cell lies on only one current owner line, yet for almost
every owner it is reachable through some off-diagonal replacement.

## 5. Cellwise interpretation

For \(a\in\mathcal A\), let

\[
c(a)=|\{i:a\text{ lies on the current owner line }i\}|
\]

and

\[
n(a)=|\{i:\exists j\text{ with }a,z_i,(x_i,y_j)	ext{ collinear}\}|.
\]

Then

\[
H_0=\sum_a c(a),
\qquad
\mathcal W=\sum_a n(a),
\]

with

\[
1\le c(a)\le n(a)\le q.
\]

### Corollary PP3no -- PROVED

Under PP3nn,

\[
\frac1{|\mathcal A|}
\sum_a(c(a)-1)
\le
\frac{q(1+\varepsilon)}{q+1+\varepsilon}-1,
\]

and

\[
\frac1{|\mathcal A|}
\sum_a(q-n(a))
\le
q-
\frac{q+1+\varepsilon}{1+\varepsilon}.
\]

Hence failure produces simultaneously:

1. negligible excess current-line multiplicity; and
2. negligible missing owner reachability.

#### Proof

Rewrite the two inequalities of PP3nn using the displayed sums. ∎

## 6. Revised rich-line endpoint

### Corollary PP3np -- PROVED

For a Hall-derived target set and a source-valid low-event family with local mass
\(\lambda\), at least one of the following holds.

1. The near-uniform derangement criterion PP3nl gives a strict owner-line
   improvement.
2. The target incidence system is near extremal in the precise sense PP3nn--PP3no.

The remaining line obstruction is therefore not merely a grid-rich pencil. It is
a near-complete owner-reachability design in which almost every target cell has a
unique current witness but is attainable from almost every owner after
reassignment.