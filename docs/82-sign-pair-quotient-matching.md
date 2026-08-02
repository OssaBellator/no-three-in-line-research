# Sign-pair quotient matchings for odd strong-complete maps

The affine-orbit route asks for one strong-complete seed with low secant and
affine-triangle multiplicities. This chapter introduces a symmetric subfamily
whose existence problem is a regular perfect-matching problem with bounded
codegrees.

Let \(p\) be an odd prime and put

\[
\mathcal Q_p=\mathbb F_p^*/\{\pm1\},
\qquad
m=|\mathcal Q_p|=\frac{p-1}{2}.
\]

Write \([x]\) for the sign class of a nonzero field element \(x\).

## 1. The quotient hypergraph

Take four labelled copies \(X,Y,D,S\) of \(\mathcal Q_p\). For nonzero \(x,y\)
with \(y\ne\pm x\), define

\[
e(x,y)=([x],[y],[x-y],[x+y]).
\]

The pairs \((x,y)\) and \((-x,-y)\) define the same edge. No other pair does:
reversing only one sign interchanges the final two sign classes, and
\([x-y]\ne[x+y]\) because \(x,y\ne0\).

Call the resulting four-partite four-graph \(\mathcal H_p^{\pm}\).

## Theorem PX148 -- PROVED

Perfect matchings of \(\mathcal H_p^{\pm}\) are in bijection with permutations

\[
f:\mathbb F_p\to\mathbb F_p
\]

such that

\[
f(0)=0,
\qquad
f(-x)=-f(x),
\]

and all three maps

\[
f,
\qquad x\mapsto x-f(x),
\qquad x\mapsto x+f(x)
\]

are permutations. Thus the matchings are exactly the odd strong-complete maps.

### Proof

Let \(M\) be a perfect matching. The unique edge covering an input class
\([x]\) has a representative \(e(x,y)\). Define

\[
f(x)=y,
\qquad
f(-x)=-y,
\qquad
f(0)=0.
\]

Changing the representative to \((-x,-y)\) gives the same definition. Covering
every \(Y\)-vertex once makes \(f\) a permutation; covering \(D\) and \(S\)
makes \(x-f(x)\) and \(x+f(x)\) permutations. Conversely, an odd
strong-complete map contributes one edge

\[
([x],[f(x)],[x-f(x)],[x+f(x)])
\]

for each input sign class, and the three permutation conditions make these
edges a perfect matching. \(\square\)

This is the sign-quotient subhypergraph of the full exact-cover host from
PX138--PX139.

## 2. Exact regularity

## Theorem PX149 -- PROVED

The quotient hypergraph has

\[
|E(\mathcal H_p^{\pm})|
=
\frac{(p-1)(p-3)}2
=
m(p-3)
\]

edges and is exactly \((p-3)\)-regular. Its maximum pair and triple codegrees
are

\[
\boxed{\Delta_2=2,\qquad\Delta_3=1.}
\]

### Proof

Fixing \([x]\in X\), there are \(p-3\) signed output choices

\[
y\in\mathbb F_p^*\setminus\{x,-x\}.
\]

They give distinct edges. The same argument works for \(Y\).

Fix a difference class and orient it as \(x-y=d\ne0\). Then \(y=x-d\), and
\(x\) can be any field element except

\[
0,
\qquad d,
\qquad d/2,
\]

which respectively prevent \(x=0\), \(y=0\), and \(x+y=0\). Thus the \(D\)
degree is \(p-3\); the sum part is identical.

Any two of the linear forms

\[
x,
\qquad y,
\qquad x-y,
\qquad x+y
\]

are independent in odd characteristic. After fixing two sign classes, there
are at most four sign choices, paired by simultaneous negation, so the pair
codegree is at most two. Generic pairs attain two.

For three parts, the third sign class distinguishes the two possible relative
signs. For instance, after fixing \([x]\) and \([y]\), the two candidates have
difference classes \([x-y]\) and \([x+y]\), which are distinct. The remaining
triples of parts follow by solving the corresponding two linear equations.
Thus the triple codegree is one. \(\square\)

## 3. Exact finite odd seeds

Randomized exact-cover search in \(\mathcal H_p^{\pm}\), followed by exact
multiplicity scoring, gives the following odd strong-complete seeds. Their full
row-order permutations are stored in the verifier.

## Theorem PX150 -- PROVED FINITE

| Prime \(p\) | \(\mu(f)\) | \(	au(f)\) | \(K_2=\mu/p\) | \(K_3=(p-2)	au/p\) |
|---:|---:|---:|---:|---:|
| 43 | 72 | 10 | \(<1.68\) | \(<9.54\) |
| 47 | 84 | 12 | \(<1.79\) | \(<11.49\) |
| 53 | 76 | 10 | \(<1.44\) | \(<9.63\) |
| 59 | 94 | 10 | \(<1.60\) | \(<9.67\) |
| 61 | 90 | 12 | \(<1.48\) | \(<11.61\) |
| 67 | 96 | 12 | \(<1.44\) | \(<11.65\) |

Thus sign symmetry does not create a linear triangle-multiplicity obstruction.
It costs only a modest constant in the tested affine-orbit parameters while
replacing the unrestricted exact-cover problem by the regular bounded-codegree
host of PX149.

## 4. Fixed-bin consequences of spread

Let \(d=p-3\). A probability distribution on perfect matchings of
\(\mathcal H_p^{\pm}\) is rank-three \(K/d\)-spread if every compatible set \(F\)
of at most three hyperedges satisfies

\[
\Pr(F\subseteq M)
\le
\left(\frac Kd\right)^{|F|}.
\]

Assume \(1\le K\le d\), and let \(f_M\) be the odd strong-complete map obtained
from PX148.

## Theorem PX151 -- PROVED CONDITIONALLY

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

Hence

\[
\mathbb E\,\mu_{f_M}(r)=O(K^2p).
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

Thus

\[
\mathbb E\,\tau_{f_M}(r,t,s)=O(K^3)
\]

uniformly in the shape and prime.

### Proof: secants

There are exactly \(3(p-1)\) ordered row pairs of the forms

\[
u=0,
\qquad v=0,
\qquad v=-u\ne0.
\]

For a fixed slope, each fixes at most one quotient edge and therefore has
probability at most \(K/d\).

The remaining \((p-1)(p-3)\) ordered pairs use two distinct nonzero sign
classes. After choosing \(f(u)\) in at most \(p\) ways, the equation

\[
f(v)-f(u)=r(v-u)
\]

fixes \(f(v)\). Each valid assignment prescribes two compatible quotient edges
and has probability at most \((K/d)^2\). Summing gives the first bound.

### Proof: affine triangles

Put \(w=u+t(v-u)\). The three scalar rows are distinct. Their sign classes fail
to be three distinct nonzero classes only when one of

\[
u=0,
\quad v=0,
\quad w=0,
\quad v=-u,
\quad w=-u,
\quad w=-v
\]

holds. For fixed \(t\), these equations account for at most \(6p\) ordered
pairs. Oddness and the prescribed shape then fix every nonzero image involved,
if the shape is consistent, so the probability is at most \(K/d\).

For every other ordered pair, choose \(f(u)\) in at most \(p\) ways. The slope
fixes \(f(v)\), and the output ratio fixes \(f(w)\). This prescribes three
distinct compatible quotient edges, with probability at most \((K/d)^3\).
There are at most \(p(p-1)\) ordered pairs. Summing proves the result.
\(\square\)

## 5. Relation to the current completion program

PX141 already gives an almost-perfect pseudorandom matching in the full host
\(\mathcal H_p\). PX148--PX151 provide a complementary quotient model:

1. the degree remains linear;
2. pair and triple codegrees stay absolutely bounded;
3. exact odd seeds with constant triangle multiplicity exist through order 67;
4. rank-three spread already forces the correct first-moment scales.

The remaining quotient theorem is tail control: construct a perfect-matching
measure spread through logarithmic rank, or prove comparable concentration for
a random-greedy-plus-absorption process. Such a theorem should yield

\[
\mu(f)=O(p\operatorname{polylog}p),
\qquad
\tau(f)=\operatorname{polylog}p.
\]

The full-host route is currently further advanced because PX142--PX147 compute
its exact lattice and finite absorbers. The quotient route remains useful as a
smaller symmetric testbed for a spread perfect-matching theorem.

## 6. Verification

Run

```bash
python scripts/verify_product_sign_pair_quotient.py
```

The verifier constructs the quotient hypergraph through prime order nineteen,
checks its edge count, regularity and exact codegrees, and verifies every listed
odd seed and multiplicity through order sixty-seven.
