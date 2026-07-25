# Exact internal rank-three support-four count and hybrid thinning

PX324--PX329 reduce the general frozen-switch sign to the case where internal
rank-three creation is at least the guaranteed old destruction.  PX227 bounded
that internal creation only by `O(s)`, using the coarse estimate
`W_(3,4)=O(t^4)`.  The support-four sector is actually constant-scale.

A rank-three partial matching on four endpoint labels has only two shapes: a
directed path of length three, or a transposition plus one disjoint arc.  In
either shape, after fixing the first two cells and the row of the third cell,
collinearity determines its target column uniquely.  Hence the number of
collinear support-four patterns is `O((s)_3)`, not `O(s^4)`.

Combining this exact count with a hybrid thinning probability

\[
q=\min\left\{t^{-1/2},\frac{t}{C_\Delta N\mathfrak d(N)}\right\}
\]

makes support five and six `o(s)` uniformly throughout the ambient range where
PX226 applies.  Thus some replacement matching has internal rank-three load
strictly below the linear old destruction, and the external blocker forest can
finish the strict-sign-or-child conversion.

## 1. Classification of rank-three support four

Use the endpoint-index notation `e_(ij)` of PX201.  Diagonal cells are forbidden.

### Theorem PX330 -- PROVED

Every compatible rank-three partial matching with endpoint support exactly four
has exactly one of the following directed-graph shapes.

1. A directed path of length three:

   \[
   a\to b,\quad b\to c,\quad c\to d,
   \]

   on four distinct labels.
2. A directed two-cycle plus a disjoint arc:

   \[
   a\to b,\quad b\to a,\quad c\to d,
   \]

   on four distinct labels.

### Proof

The three arcs have indegree and outdegree at most one at every endpoint label.
Therefore every component is a directed path or directed cycle.  Three arcs on
four used vertices can either form one path with three arcs, or one two-cycle
and one one-arc path.  A three-cycle uses only three labels, and every other
component pattern uses at least five. \(\square\)

## 2. Row uniqueness removes one endpoint factor

Let `R={x_i}` and `C={y_i}` have distinct coordinates as before.  Let
`W_(3,4)` be the number of collinear compatible rank-three candidate triples
with support four.

### Theorem PX331 -- PROVED

For every endpoint family of order `t`,

\[
\boxed{
W_{3,4}\le \frac32(t)_3.
}
\]

More precisely, the path sector contributes at most `(t)_3`, and the
two-cycle-plus-arc sector contributes at most `(t)_3/2`.

### Proof

For a path, choose the ordered distinct labels `(a,b,c)`.  The first two cells
`e_(ab),e_(bc)` determine a nonvertical line.  That line meets the row `x_c` in
one point, so at most one target coordinate `y_d` makes `e_(cd)` collinear with
them.  Hence there are at most `(t)_3` collinear path triples.

For a two-cycle plus arc, choose the unordered pair `{a,b}` and then choose
`c` outside it.  The line through `e_(ab),e_(ba)` meets row `x_c` once, so at
most one `d` works.  The count is at most

\[
\binom t2(t-2)=\frac12(t)_3.
\]

Add the two sectors. \(\square\)

The same bound holds on every retained endpoint subset `J`, with `s=|J|` in
place of `t`.

## 3. Constant expected support three and four

Let

\[
\mathcal C(s,\Delta)
=
\left(1-\frac1{s-4\Delta}\right)^{-\Delta s}
\]

be the optimized cylinder factor of PX232, and assume `s>=8Delta+2`.

### Corollary PX332 -- PROVED

For a uniform allowed replacement matching on the retained block,

\[
\boxed{
\mathbb E T_{3,3}
\le
\frac13\mathcal C(s,\Delta)
}
\]

and

\[
\boxed{
\mathbb E T_{3,4}
\le
\frac32\mathcal C(s,\Delta).
}
\]

Consequently

\[
\boxed{
\mathbb E(T_{3,3}+T_{3,4})
\le
\frac{11}{6}e^{2\Delta}.
}
\]

### Proof

PX203 gives at most `(s)_3/3` directed three-cycles.  PX331 gives at most
`3(s)_3/2` support-four triples.  Apply the optimized rank-three cylinder bound
`mathcal C(s,Delta)/(s)_3` and use PX234. \(\square\)

## 4. Hybrid thinning makes support five and six sublinear

Fix an absolute constant `A_3` such that the PX189 rich-line estimate gives

\[
W_{3,5}+W_{3,6}
\le
A_3t^4\log(2t).
\]

Put

\[
X=C_\Delta N\mathfrak d(N),
\qquad
q_\diamond
=
\min\left\{t^{-1/2},\frac tX\right\},
\]

where `C_Delta=1024e^(4Delta)` is the PX226 constant.  Let PX201 choose a
simultaneous retained set `J` of order `s>=q_diamond t/2`.

### Theorem PX333 -- PROVED

Assume `q_diamond t>=32` and `s>=8Delta+2`.  Then

\[
\boxed{
\frac{\mathbb E(T_{3,5}+T_{3,6})}{s}
\le
512A_3e^{2\Delta}
\left(q_\diamond\log(2t)+q_\diamond^2\log(2t)\right).
}
\]

Moreover, uniformly for `1<=t<=N`,

\[
\boxed{
q_\diamond\log(2t)
\le
X^{-1/3}\log(2X)
}
\]

for all sufficiently large `X`.  Hence the displayed expected-load ratio is
`o(1)` for fixed `Delta`.

### Proof

PX201 retains at most `16q^uW_(3,u)` weight in sector `u`.  Since `s>=16`,

\[
(s)_3\ge\frac{s^3}{2}\ge\frac{q^3t^3}{16}.
\]

Apply the optimized rank-three cylinder bound.  For support five this gives at
most

\[
256A_3e^{2\Delta}q^2t\log(2t),
\]

and support six gives at most the same expression with `q^3`.  Divide by
`s>=qt/2`.

For the uniform bound, the two terms defining `q_diamond` cross at
`t=X^(2/3)`.  Below the crossover, `q=t/X`; above it, `q=t^(-1/2)`.  The maximum
of `q log(2t)` is therefore at the crossover up to the harmless eventual
monotonicity of `log(2t)/sqrt(t)`, giving the stated bound. \(\square\)

## 5. Internal rank three is strictly below destruction

Put

\[
B_\Delta
=
\max\left\{
32,
16\Delta+4,
16e^{2\Delta}
\right\}.
\]

### Corollary PX334 -- PROVED

Suppose

\[
\sqrt t\ge B_\Delta,
\qquad
\frac{t^2}{C_\Delta N\mathfrak d(N)}\ge B_\Delta.
\]

Then `q_diamond t>=B_Delta`.  For all sufficiently large `N` depending on
`Delta` and `A_3`, the simultaneous retained block has an allowed replacement
matching `M` satisfying

\[
\boxed{
T_{3,3}(M)+T_{3,4}(M)+T_{3,5}(M)+T_{3,6}(M)<s.
}
\]

The same retained block still satisfies the PX226 support-four rank-two bound

\[
\mathbb E T_{2,4}\le s/2.
\]

### Proof

The two size hypotheses imply `q_diamond t>=B_Delta`, hence
`s>=B_Delta/2`.  PX332 contributes at most `11e^(2Delta)/6<s/4` by the chosen
constant.  PX333 is `o(s)`, and is below `s/4` for large `N`.  Thus the expected
total internal rank-three load is below `s/2`, so some allowed matching has
load below `s`.  The rank-two support-four estimate follows because
`q_diamond<=t/(C_Delta N d(N))`, exactly the inequality used in PX226. \(\square\)

### Corollary PX335 -- PROVED REDUCTION

In every clean-star, radial, coordinate-field, or loaded-line retained block
where every allowed matching destroys at least `s` old certificates, choose the
matching supplied by PX334.  Its internal support-three creation `c_3` satisfies

\[
\boxed{c_3<s\le d_\sigma.}
\]

Therefore PX326--PX327 discharge every support-one and support-two blocker by a
finite causal child forest and then execute the switch strictly.

Hence, above the square-root ambient threshold and for sufficiently large `N`,
internal rank three is no longer a sign obstruction.  The remaining exact
frontier is confined to the below-threshold packet/terminal range and the
constant trajectory residuals of PX315--PX318.

## 6. Verification

Run

```bash
python scripts/verify_product_rank_three_support_four.py
```

The verifier classifies all rank-three support-four partial permutations,
checks their exact populations, tests the row-uniqueness bound on finite integer
endpoint sets, and verifies the hybrid-thinning inequalities numerically and
symbolically over representative ranges.
