# Peeling majority Hall-wall certificates

CMR202 isolates a source-row or target-column wall containing `W(t)` cells
assigned certificates of one common rank. Those certificates are easier to
remove than a general cylinder family: a parent permutation uses exactly one
cell of the wall coordinate, so their cylinders are pairwise disjoint.

Retain

\[
W(t)=
\left\lceil
\frac{\lfloor t/2\rfloor}{3}
\right\rceil,
\qquad t\ge5.
\]

Let `G_r` be the `W(t)` assigned rank-`r` certificates supplied by CMR200.

## 1. Exact disjointness and mass bounds

### Theorem CMR203 — PROVED

The parent derangement cylinders belonging to `G_r` are pairwise disjoint.
Their union measure is at most

\[
\boxed{
\beta_1=\frac27,
\qquad
\beta_2=\frac3{22},
\qquad
\beta_3=\frac1{22}
}
\]

for ranks one, two, and three, respectively.

### Proof

Every assigned certificate contains its distinct designated wall cell. A
parent derangement selects exactly one cell in one fixed source row and exactly
one cell in one fixed target column. Therefore two certificates assigned to
different wall cells cannot occur in the same parent state, regardless of
their other prescribed cells. Their cylinders are pairwise disjoint.

For rank one, CMR176 gives exact cylinder probability `1/(t-1)`, so the union
has measure

\[
\frac{W(t)}{t-1}\le\frac27.
\]

For ranks two and three, CMR176 gives

\[
\frac{30W(t)}{11(t)_2}\le\frac3{22},
\qquad
\frac{30W(t)}{11(t)_3}\le\frac1{22}.
\]

The three elementary maxima occur at `t=8,5,5`, respectively, and are checked
in the companion script. ∎

Thus even the rank-one majority wall explains less than one third of the full
parent bank. A rank-three candidate-only wall explains at most one state in
twenty-two in parent-law measure.

## 2. Dense residual parent banks

Let

\[
\Omega_t^{(r)}
=
\Omega_t\setminus\bigcup_{Q\in G_r}Q
\]

be the derangements avoiding every assigned majority-wall certificate.

### Theorem CMR204 — PROVED

The residual bank has density at least

\[
\boxed{
1-\beta_r
}
\]

inside `Omega_t`. Every rank-`s` candidate cylinder has conditional probability
at most

\[
\frac{1}{1-\beta_r}
\]

times its original parent-law probability.

If the original state is globally frozen, the candidate certificates outside
`G_r` cover all of `Omega_t^{(r)}`.

### Proof

CMR203 gives the density statement. For any event `E`,

\[
\Pr(E\mid\Omega_t^{(r)})
\le
\frac{\Pr(E)}{\Pr(\Omega_t^{(r)})}
\le
\frac{\Pr(E)}{1-\beta_r}.
\]

Every state in the residual bank avoids all certificates of `G_r`. Since every
parent state remains nonimproving and must create a new triple after the old
target is destroyed, some certificate outside `G_r` occurs in each residual
state. ∎

## 3. Quantitative residual expansion

### Corollary CMR205 — PROVED

The candidate family outside the peeled wall contains at least

\[
\boxed{
\left\lceil(1-\beta_r)(t-1)\right\rceil
}
\]

distinct cylinders. Explicitly, the lower bounds are

\[
\boxed{
\left\lceil\frac57(t-1)\right\rceil,
\qquad
\left\lceil\frac{19}{22}(t-1)\right\rceil,
\qquad
\left\lceil\frac{21}{22}(t-1)\right\rceil
}
\]

for majority ranks one, two, and three.

### Proof

Under the original parent law, no rank-`1/2/3` cylinder has probability larger
than the rank-one maximum `1/(t-1)`. By CMR204, its conditional probability in
the residual bank is at most

\[
\frac1{(1-\beta_r)(t-1)}.
\]

A union of fewer than `(1-beta_r)(t-1)` such cylinders cannot cover the complete
residual probability space. Take ceilings and substitute the three values from
CMR203. ∎

This is strongest in the formerly problematic rank-three case: after removing
the entire candidate-only wall, at least `21/22` of a minimum linear parent
cover must still be supplied by other certificates.

## 4. Revised fixed-envelope obstruction

A Hall wall is now a peeling step rather than a stopping structure.

- Rank-one and rank-two walls already expose executable endpoint banks by
  CMR201.
- Rank-three walls occupy at most `1/22` of the parent law and leave an almost
  full residual bank requiring linearly many different cylinders.

The remaining no-return theorem should iterate wall extraction on the dense
residual bank while controlling how its forbidden-coordinate sets accumulate.
A sufficient endpoint would show that after a bounded number of peels, either

1. the residual matching host still has minimum degree at least half and yields
   another Hall wall;
2. the accumulated peeled cells themselves force a strict envelope expansion;
3. or the residual certificate mass exceeds the joint-parent quotient/carry
   budget.

No all-`n` theorem is claimed here. The exact wall masses and residual cover
bounds are checked in
[`scripts/verify_prime_power_parent_wall_peeling.py`](../scripts/verify_prime_power_parent_wall_peeling.py).
