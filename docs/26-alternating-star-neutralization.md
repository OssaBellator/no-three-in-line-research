# Alternating star neutralization

This chapter constructs an exact two-colour repair bank for a secant-star obstruction. A fixed switch in one permutation layer is coupled to a row-column-preserving permutation of selected star endpoints in the opposite active layer. The original star triples are neutralized, while the replacement anchor matching has a constant-spread distribution.

## 1. Permutations avoiding two forbidden matchings

Let `F subseteq [t] times [t]` be a forbidden-position set with at most two cells in every row and every column. Let

\[
\Omega(F)
=
\{\pi\in S_t:(i,\pi(i))\notin F\text{ for every }i\}.
\]

### Theorem AN1 — PROVED

For `t>=7`,

\[
\boxed{|\Omega(F)|\ge\frac{t!}{128}.}
\]

If `Q` is any compatible partial matching of `r` nonforbidden cells, and `pi` is uniform on `Omega(F)`, then

\[
\boxed{
\Pr(Q\subseteq\pi)
\le
\frac{128}{(t)_r}.
}
\]

### Proof

Choose a uniformly random permutation of `[t]`. For every forbidden cell `(i,j)`, let `A_{ij}` be the canonical event `pi(i)=j`. Each event has probability `1/t`.

The canonical-event conflict graph is a negative dependency graph. Because every row and column of `F` has size at most two, each event conflicts with at most two other forbidden events.

Set

\[
x=\frac2t.
\]

For `t>=7`,

\[
\frac1t
\le
\frac2t\left(1-\frac2t\right)^2.
\]

The lopsided local lemma therefore gives

\[
\Pr(\pi\in\Omega(F))
\ge
\left(1-\frac2t\right)^{|F|}
\ge
\left(1-\frac2t\right)^{2t}
>
\frac1{128}.
\]

This proves the count. At most `(t-r)!` permutations contain a prescribed compatible partial matching `Q`, so conditioning on `Omega(F)` gives

\[
\Pr(Q\subseteq\pi)
\le
\frac{(t-r)!}{t!/128}
=
\frac{128}{(t)_r}.
\]

\(\square\)

## 2. Extracting a movable endpoint layer

Consider an endpoint-disjoint secant star of `M` pairs through one candidate point. Assume the current configuration is decomposed into two permutation layers and is contained in `q` modular-hyperbola channels.

Label every endpoint by its permutation layer and hyperbola channel. There are at most `2q` endpoint types.

### Lemma AN2 — PROVED

One may choose one endpoint from each of at least

\[
\boxed{t\ge\frac{M}{2q}}
\]

star pairs so that all chosen endpoints belong to one fixed permutation layer and one fixed hyperbola channel.

The chosen endpoints occupy distinct rows and distinct columns.

### Proof

The `2M` endpoint incidences are distributed among at most `2q` types. Some type occurs at least `M/q` times. A pair contributes at most two incidences of one type, so that type occurs in at least `M/(2q)` distinct pairs. Choose one such endpoint from every represented pair.

Points in one permutation layer have distinct rows and columns. \(\square\)

## 3. The alternating neutralization bank

Fix one admissible rectangle switch in the first permutation layer. Let `z` be one of its inserted candidate points, and let

\[
\{P_j,Q_j\},
\qquad 1\le j\le t,
\]

be endpoint-disjoint outside pairs whose lines pass through `z`. Choose the endpoints `Q_j` using AN2, all in one permutation layer. Let their columns and rows be

\[
C=\{c_1,\ldots,c_t\},
\qquad
R=\{r_1,\ldots,r_t\}.
\]

Remove the selected points `(c_j,r_j)`. A replacement state is a perfect matching between `C` and `R`.

There are two forbidden positions in each source row or target column at most:

1. the original diagonal cell `(c_j,r_j)`, because the endpoint must move;
2. the cell occupied by the other permutation layer after the fixed rectangle switch, because the two layers must remain disjoint.

Thus these forbidden cells form a set `F` with row and column degree at most two.

### Theorem AN3 — PROVED

For `t>=7`, the family `Omega(F)` is nonempty. Every state in this family:

1. preserves the selected anchor columns and rows;
2. remains disjoint from the other permutation layer;
3. moves every chosen star endpoint;
4. destroys every original prospective triple
   \[
   \{z,P_j,Q_j\}.
   \]

Moreover, the uniform state is `128/t`-spread in the sense of AN1.

### Proof

The first two assertions follow from the definition of an allowed perfect matching. The forbidden diagonal ensures that no `Q_j` remains in its original cell, so the exact old pair `{P_j,Q_j}` is no longer present. Therefore its prospective triple with `z` is destroyed. AN1 supplies nonemptiness and spread. \(\square\)

New triples involving moved endpoints may still appear. The point is that they are no longer the concentrated original star and can be bounded by a spread matching calculation.

## 4. Average collateral of the joint bank

Let `A` be the set of chosen anchor endpoints and let `C_0` be the two current points removed by the fixed rectangle switch. Put

\[
X=S\setminus(A\cup C_0).
\]

Let `W` be the two inserted points of the fixed rectangle switch and define

\[
Z=X\cup W.
\]

The current configuration is

\[
S=X\cup A\cup C_0,
\]

while a joint alternating state is

\[
S_\pi=Z\cup M_\pi,
\qquad \pi\in\Omega(F),
\]

where `M_pi` is the replacement anchor matching.

Define

\[
D_\star=\Phi(S)-\Phi(X)
\]

and

\[
F_\star=\Phi(Z)-\Phi(X).
\]

For `r=1,2,3`, let `T_r` be the number of real collinear triple certificates consisting of exactly `r` mutually compatible nonforbidden anchor-block cells and `3-r` points of `Z`.

### Theorem AN4 — PROVED

For a uniformly random `pi in Omega(F)`,

\[
\boxed{
\mathbb E\bigl[\Phi(S_\pi)-\Phi(Z)\bigr]
\le
128\left(
\frac{T_1}{t}
+
\frac{T_2}{t(t-1)}
+
\frac{T_3}{t(t-1)(t-2)}
\right).
}
\]

Consequently, if

\[
\boxed{
D_\star
>
F_\star
+
128\left(
\frac{T_1}{t}
+
\frac{T_2}{t(t-1)}
+
\frac{T_3}{t(t-1)(t-2)}
\right),
}
\]

then some alternating state strictly lowers the triple potential.

### Proof

A new triple containing `r` anchor-block cells appears only if its prescribed compatible partial matching is contained in `M_pi`. AN1 bounds this probability by `128/(t)_r`. Sum over all potential certificates and use linearity of expectation.

Finally,

\[
\Phi(S_\pi)-\Phi(S)
=
F_\star-D_\star
+
\bigl(\Phi(S_\pi)-\Phi(Z)\bigr).
\]

If the displayed strict inequality holds, the expected potential change is negative, so one state improves. \(\square\)

## 5. Consequence for the closure program

A large secant star is no longer merely added to the active core. It supplies an explicit opposite-layer state bank which neutralizes a linear substar before paying new collateral.

The remaining theorem is now a second-order concentration statement:

> If every alternating neutralization state fails, prove that the normalized counts `T_1/t`, `T_2/(t)_2`, or `T_3/(t)_3` force either a new paid common-ratio bank in the moved layer, growth of carry-signature complexity, or a bounded-denominator perfect chamber.

This is a smaller target than the original alternating carry-core termination lemma because the dominant first-generation star has already been removed exactly.
