# Anchored transition factorization and divisor regularization

The only potentially large low-support term in PP3jb is the family of anchored
two-step transitions

\[
i\to j\to k.
\]

This chapter gives an exact product factorization for that class. Summing the
result over anchors bounds the total transition population, and deleting only
`o(q)` endpoint indices makes every remaining transition resource degree
`o(q^2)` at the prime-gap endpoint scale.

## 1. Exact transition factorization

Use endpoint cells

\[
c_{ij}=(x_i,y_j),
\qquad
c_{jk}=(x_j,y_k),
\]

and a retained source anchor

\[
p=(u,v).
\]

### Proposition PP3jc -- PROVED

The points `c_ij,c_jk,p` are collinear if and only if

\[
\boxed{
(u-x_i)(v-y_k)
=
(u-x_j)(v-y_j).
}
\]

#### Proof

The determinant equation is

\[
(x_j-x_i)(v-y_j)
=
(y_k-y_j)(u-x_i).
\]

Write

\[
a=x_j-x_i,
\qquad
b=y_k-y_j,
\qquad
U=u-x_j,
\qquad
V=v-y_j.
\]

Then the equation is `a(V-b)=bU`. Adding the missing product term gives

\[
(a+U)(V-b)=UV.
\]

Since `a+U=u-x_i` and `V-b=v-y_k`, this is the displayed identity. ∎

The right side depends only on the middle endpoint `j` and the anchor `p`.

## 2. Divisor bound for one middle index

Let

\[
D_m
=
\max_{1\le n\le m^2}\tau(n).
\]

The standard maximal-divisor estimate gives

\[
D_m=m^{o(1)}.
\]

### Proposition PP3jd -- PROVED

Fix a middle endpoint `j` and an anchor `p=(u,v)`.

1. If

   \[
   (u-x_j)(v-y_j)\ne0,
   \]

   then at most `2D_m` ordered pairs `(i,k)` satisfy the transition equation.

2. If

   \[
   (u-x_j)(v-y_j)=0,
   \]

   then at most `q` ordered pairs `(i,k)` satisfy it.

For fixed `j`, at most two anchors are in the second case.

#### Proof

In the nonzero case, the two nonzero integers

\[
u-x_i,
\qquad
v-y_k
\]

form a signed divisor pair of the fixed nonzero integer

\[
(u-x_j)(v-y_j).
\]

There are at most `2tau(|(u-x_j)(v-y_j)|)` signed ordered factor pairs. The
endpoint layer has distinct old columns and distinct old rows, so each factor
pair determines at most one `(i,k)`.

If the fixed product is zero, the anchor shares the old column `x_j` or the old
row `y_j`. These two possibilities contribute at most one anchor each because
the retained source is saturated. In the shared-column case the equation forces
one value of `k` and leaves at most `q` choices of `i`; the shared-row case is
transposed. ∎

## 3. Total transition population

Let `N_tr` be the number of distinct support-rank-three anchored pair events on a
`q`-endpoint rectangle, counted once regardless of anchor multiplicity.

### Corollary PP3je -- PROVED

One has

\[
\boxed{
N_{\rm tr}
\le
2qmD_m+2q^2.
}
\]

#### Proof

For each of the `q` choices of middle index `j`, sum PP3jd over at most `2m`
retained source anchors. The nonaxis anchors contribute at most `2mD_m`, while
the at most two axis anchors contribute at most `2q`. Counting distinct events
instead of anchored witnesses can only decrease the total. ∎

At the resource-bank scale

\[
q=\Omega(m^{21/40}),
\]

this is

\[
N_{\rm tr}
=
O(qm^{1+o(1)}+q^2)
=
o(q^3).
\]

Thus the transition system is globally sparse even though its maximum endpoint
degree need not initially be small.

## 4. Endpoint-degree regularization

For an endpoint index `s`, let `d_tr(s)` be the number of transition events in
which `s` appears as predecessor, middle, or successor.

### Theorem PP3jf -- PROVED

Fix any constant

\[
0<\varepsilon<\dfrac1{20}.
\]

Delete every endpoint index satisfying

\[
d_{\rm tr}(s)>m^{1+\varepsilon}.
\]

At the scale `q=Omega(m^(21/40))`, the number of deleted indices is `o(q)`. Every
remaining left or right permutation resource is incident to at most
`m^(1+epsilon)` transition events, so its transition-event probability mass is

\[
\boxed{
O\left(
\dfrac{m^{1+\varepsilon}}{q^2}
\right)
=
o(1).
}
\]

#### Proof

Every transition event uses three endpoint indices. Hence

\[
\sum_s d_{\rm tr}(s)
\le
3N_{\rm tr}
=
O(qmD_m+q^2).
\]

The number removed is therefore at most

\[
O\left(
\dfrac{qmD_m+q^2}{m^{1+\varepsilon}}
\right)
=
O(qm^{o(1)-\varepsilon})
+
O\left(\dfrac{q^2}{m^{1+\varepsilon}}\right).
\]

The first term is `o(q)`. For the second, `q=m^(21/40+o(1))` gives

\[
\dfrac{q^2}{m^{1+\varepsilon}}
=
m^{1/20-\varepsilon+o(1)}
=
o(q).
\]

After pruning, a typed left or right resource is incident to no more transition
events than its underlying endpoint index. Each transition event has canonical
probability `1/(q')_2`, where `q'=(1-o(1))q`. Thus its incident mass is at most

\[
\dfrac{m^{1+\varepsilon}}{(q')_2}
=
m^{-1/20+\varepsilon+o(1)}
=o(1).
\]

∎

## 5. Combined low-support closure

### Theorem PP3jg -- PROVED

Let a resource endpoint bank have size

\[
q=\Omega(m^{21/40}).
\]

Assume its unary forbidden endpoint graph has density

\[
\theta=o(1).
\]

Then one may delete `o(q)` endpoint indices so that on the remaining bank:

1. every unary forbidden left or right degree is `o(q)`;
2. every anchored transition resource mass is `o(1)`;
3. the transposition and directed-triangle resource masses are `O(1/q)`;
4. the complete low-support mass `lambda` of PP3ix is `o(1)`.

Consequently PP3ix and PP3iy apply for all sufficiently large `m`.

#### Proof

First apply PP3is to the unary forbidden graph. Since `theta=o(1)`, it removes
`o(q)` indices and leaves maximum forbidden degree `o(q)`. Then apply PP3jf to
the remaining transition system, removing another `o(q)` indices. The unary
mass is maximum forbidden degree divided by the remaining size and is therefore
`o(1)`. The transition mass is `o(1)` by PP3jf. The universal transposition and
directed-triangle estimates in PP3jb contribute `O(1/q)`. Sum. ∎

### Corollary PP3jh -- PROVED

Under the unary-density hypothesis `theta=o(1)`, all source-validity patterns of
endpoint support rank at most three are closed. A paid endpoint trade now follows
from PP3ja once

\[
9\dfrac{P_4}{q^2}
+
27\dfrac{Q_{\ge4}}{q^3}
+
\dfrac1{\mathcal C(R_0)}
\left(
3\dfrac{A_G}{q}
+
9\dfrac{B_G}{q^2}
\right)
<1
\]

on the regularized bank.

The remaining source-validity terms are therefore only the support-rank-four
anchored pairs and support-rank-at-least-four inserted triples. The anchored
transition core is no longer an independent bottleneck.

## 6. Remaining alternatives

The resource-bank conversion now has the following exact split.

1. **Dense unary endpoint shadow:** the forbidden endpoint graph has positive
   density.
2. **Sparse unary shadow:** PP3jg removes all low-support source-validity cores,
   leaving only the PP3jh high-support and weighted-collateral expression.

The first branch is a new endpoint-level shadow concentration suitable for a
second protected trade. The second branch is a pure high-support first-moment
problem.