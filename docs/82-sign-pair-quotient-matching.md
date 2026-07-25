# Sign-pair quotient matchings for odd strong-complete maps

The affine-orbit route asks for one strong-complete seed with low secant and
affine-triangle multiplicities.  This chapter introduces a symmetric subfamily
whose existence problem is itself a regular perfect-matching problem with
bounded codegrees.

Let \(p\) be an odd prime and put

\[
\mathcal Q_p=\mathbb F_p^*/\{\pm1\},
\qquad
m=|\mathcal Q_p|=\frac{p-1}{2}.
\]

Write \([x]\) for the sign class of a nonzero field element \(x\).

## 1. The quotient hypergraph

Take four labelled copies

\[
X,Y,D,S
\]

of \(\mathcal Q_p\).  For nonzero \(x,y\) with \(y\ne\pm x\), define

\[
e(x,y)=([x],[y],[x-y],[x+y])\in X\times Y\times D\times S.
\]

The pairs \((x,y)\) and \((-x,-y)\) define the same edge.  No other pair does:
if only one sign is reversed, the last two sign classes are interchanged, and
\([x-y]\ne[x+y]\) because \(x,y\ne0\).

Call the resulting four-partite four-graph \(\mathcal H_p^{\pm}\).

## Theorem PX138 -- PROVED

Perfect matchings of \(\mathcal H_p^{\pm}\) are in bijection with permutations

\[
f:\mathbb F_p\longrightarrow\mathbb F_p
\]

satisfying

\[
f(0)=0,
\qquad
f(-x)=-f(x),
\]

and such that

\[
f,
\qquad x\mapsto x-f(x),
\qquad x\mapsto x+f(x)
\]

are all permutations.  In other words, they are exactly the odd
strong-complete mappings.

### Proof

Let \(M\) be a perfect matching.  The unique edge of \(M\) covering an input
class \([x]\) has a representative \(e(x,y)\).  Define

\[
f(x)=y,
\qquad
f(-x)=-y,
\qquad
f(0)=0.
\]

Changing the representative to \((-x,-y)\) gives the same definition.  Since
\(M\) covers every \(Y\)-vertex once, the nonzero values of \(f\) occupy every
sign class once, with both signs supplied by oddness; hence \(f\) is a
permutation.  Covering every \(D\)-vertex once gives the same conclusion for
\(x-f(x)\), and covering every \(S\)-vertex once gives it for \(x+f(x)\).

Conversely, an odd strong-complete map contributes one edge

\[
([x],[f(x)],[x-f(x)],[x+f(x)])
\]

for every input sign class.  The three permutation conditions imply that these
edges cover every vertex in all four parts exactly once.  Thus they form a
perfect matching. \(\square\)

## 2. Exact regularity

## Theorem PX139 -- PROVED

The quotient hypergraph has

\[
|E(\mathcal H_p^{\pm})|
=
\frac{(p-1)(p-3)}2
=
m(p-3)
\]

edges and is exactly \((p-3)\)-regular.  Its maximum pair and triple codegrees
are

\[
\boxed{\Delta_2=2,\qquad\Delta_3=1.}
\]

### Proof

Fixing \([x]\in X\), there are \(p-3\) signed output choices

\[
y\in\mathbb F_p^*\setminus\{x,-x\}.
\]

They give distinct edges, so the \(X\)-degree is \(p-3\).  The same argument
works for \(Y\).

Fix a difference class and orient it as \(x-y=d\ne0\).  Then \(y=x-d\), and
\(x\) may be any field element except

\[
0,
\qquad d,
\qquad d/2.
\]

These exclusions respectively prevent \(x=0\), \(y=0\), and \(x+y=0\).
Therefore the \(D\)-degree is again \(p-3\).  The sum part is identical.
Multiplying the degree by \(|X|=m\) gives the edge count.

Any two of the four linear forms

\[
x,
\qquad y,
\qquad x-y,
\qquad x+y
\]

are linearly independent in odd characteristic.  After fixing two sign
classes, there are at most four choices of their signs, paired by simultaneous
negation, so at most two edges.  Generic pairs attain two.

For three parts, the third sign class distinguishes the two possible relative
sign choices.  For example, after fixing \([x]\) and \([y]\), the two candidates
have difference classes \([x-y]\) and \([x+y]\), which are distinct.  The other
three choices of parts reduce to this calculation by solving the corresponding
pair of linear equations.  Thus every triple lies in at most one edge, and
examples attaining one are immediate. \(\square\)

The base matching problem is therefore unusually clean: its degree tends to
infinity linearly while every nontrivial codegree is bounded absolutely.

## 3. Exact finite odd seeds

Randomized exact-cover search in \(\mathcal H_p^{\pm}\), followed by exact
multiplicity scoring, produced the following odd strong-complete seeds.  The
full row-order permutations are stored in the verifier.

## Theorem PX140 -- PROVED FINITE

There are explicit odd strong-complete maps with the following affine-orbit
parameters.

| Prime \(p\) | \(\mu(f)\) | \(	au(f)\) | \(K_2=\mu/p\) | \(K_3=(p-2)	au/p\) |
|---:|---:|---:|---:|---:|
| 43 | 72 | 10 | \(<1.68\) | \(<9.54\) |
| 47 | 84 | 12 | \(<1.79\) | \(<11.49\) |
| 53 | 76 | 10 | \(<1.44\) | \(<9.63\) |
| 59 | 94 | 10 | \(<1.60\) | \(<9.67\) |
| 61 | 90 | 12 | \(<1.48\) | \(<11.61\) |
| 67 | 96 | 12 | \(<1.44\) | \(<11.65\) |

Thus forcing the sign symmetry does not create a linear triangle-multiplicity
obstruction.  It costs only a modest constant in the tested affine-orbit
parameters while replacing an unrestricted exact-cover problem by the regular
bounded-codegree hypergraph of PX139.

## 4. What a spread matching measure already gives

Let \(d=p-3\).  A probability distribution on perfect matchings of
\(\mathcal H_p^{\pm}\) is called rank-three \(K/d\)-spread when every compatible
set \(F\) of at most three hyperedges satisfies

\[
\Pr(F\subseteq M)
\le
\left(\frac Kd\right)^{|F|}.
\]

Assume \(1\le K\le d\), and let \(f_M\) be the odd strong-complete map obtained
from PX138.

## Theorem PX141 -- PROVED CONDITIONALLY

For every scalar secant slope \(r\),

\[
\boxed{
\mathbb E\,\mu_{f_M}(r)
\le
\frac{3K(p-1)}{p-3}
+
\frac{K^2p(p-1)}{p-3}.
}
\]

In particular,

\[
\mathbb E\,\mu_{f_M}(r)
=O(K^2p).
\]

For every affine-triangle shape \((r,t,s)\), with \(t,s\ne0,1\),

\[
\boxed{
\mathbb E\,\tau_{f_M}(r,t,s)
\le
\frac{6Kp}{p-3}
+
\frac{K^3p^2(p-1)}{(p-3)^3}.
}
\]

Hence

\[
\mathbb E\,\tau_{f_M}(r,t,s)
=O(K^3)
\]

uniformly in the shape and the prime.

### Proof: secants

Consider an ordered row pair \((u,v)\).

There are exactly \(3(p-1)\) degenerate pairs of the following forms:

\[
u=0,
\qquad
v=0,
\qquad
v=-u\ne0.
\]

For a fixed slope \(r\), each such condition fixes at most one quotient
hyperedge.  Its probability is at most \(K/d\).

The remaining

\[
(p-1)(p-3)
\]

ordered pairs use two distinct nonzero sign classes.  After choosing the scalar
value \(f(u)\), of which there are at most \(p\) possibilities, the equation

\[
f(v)-f(u)=r(v-u)
\]

fixes \(f(v)\).  Every valid assignment prescribes two compatible quotient
edges and therefore has probability at most \((K/d)^2\).  Summing gives the
first displayed bound.

### Proof: affine triangles

Put

\[
w=u+t(v-u).
\]

The three scalar rows are distinct.  Their sign classes fail to be three
distinct nonzero classes only when at least one of

\[
u=0,
\quad v=0,
\quad w=0,
\quad v=-u,
\quad w=-u,
\quad w=-v
\]

holds.  For fixed \(t\), these six linear equations account for at most \(6p\)
ordered pairs.  Oddness, together with the prescribed shape \((r,t,s)\), then
fixes every nonzero image involved, if the shape is consistent at all.  The
probability is at most \(K/d\).

For every other ordered pair, choose \(f(u)\) in at most \(p\) ways.  The slope
\(r\) fixes \(f(v)\), and the output ratio \(s\) fixes \(f(w)\).  This prescribes
three distinct compatible quotient edges, with probability at most
\((K/d)^3\).  There are at most \(p(p-1)\) ordered pairs.  Summing proves the
second displayed bound. \(\square\)

## 5. The sharpened remaining theorem

PX141 shows that first moments are already at the desired scales in the
sign-pair matching model.  The missing statement is now a tail theorem:
construct a perfect-matching distribution in \(\mathcal H_p^{\pm}\) which is
spread through logarithmic rank, or prove comparable concentration for the
random-greedy-plus-absorption process.

Such a result should yield one matching with

\[
\mu(f)=O(p\operatorname{polylog}p),
\qquad
\tau(f)=\operatorname{polylog}p,
\]

and potentially the constant bounds suggested by PX132--PX140.  The exact
regularity and bounded codegrees in PX139 match the hypotheses of modern
nibble, absorption, and spread methods much more closely than the original
unrestricted permutation formulation.

The asymptotic enumeration of toroidal queens proves that strong-complete maps
are exponentially abundant, but its currently stated error term does not by
itself give the fixed-rank completion ratios required here.  The next proof
must extract robust conditional counting or direct cylinder bounds from that
machinery.

## 6. Verification

Run

```bash
python scripts/verify_product_sign_pair_quotient.py
```

The verifier constructs the quotient hypergraph through prime order nineteen,
checks its edge count, regularity and exact codegrees, and verifies every
listed odd seed and multiplicity through order sixty-seven.
