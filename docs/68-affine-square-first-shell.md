# Affine-square design and the exact first nonlinear shell

PX98 gives a support-minimal four-row trade for strong complete mappings.  PX103
counts the trades available at an affine root.  This chapter identifies the
complete incidence geometry of those supports and then determines every trade
available after one affine-root move.

Throughout, let

\[
p\equiv1\pmod4
\]

be prime, let \(p\ge13\), choose \(i\in\mathbb F_p\) with \(i^2=-1\), and use the
affine strong complete mapping

\[
F(x)=ix+b.
\]

Put

\[
V=\{0,1,-i,1-i\}.
\]

The support of every PX98 trade at \(F\) is

\[
B(a,r)=a+rV,
\qquad
a\in\mathbb F_p,\quad r\in\mathbb F_p^\ast.
\]

Different parameter pairs may describe the same support.

## 1. The affine-square design

Let \(\mathcal B_i\) be the set of distinct supports \(B(a,r)\).

### Theorem PX104 -- PROVED

The incidence structure

\[
(\mathbb F_p,\mathcal B_i)
\]

is a super-simple

\[
\boxed{2-(p,4,3)}
\]

design.  More explicitly:

1. \(|\mathcal B_i|=p(p-1)/4\);
2. every point lies in exactly \(p-1\) blocks;
3. every pair of distinct points lies in exactly three blocks;
4. two distinct blocks meet in at most two points.

### Proof

PX103 shows that every block has exactly four ordered representations by the
distinguished corner of the same affine square.  Hence

\[
|\mathcal B_i|=\frac{p(p-1)}4.
\]

The affine group

\[
x\longmapsto \alpha x+\beta,
\qquad
\alpha\ne0,
\]

acts transitively on ordered pairs of distinct points and preserves
\(\mathcal B_i\).  Thus the number \(\lambda\) of blocks through a pair is
constant.  Counting point pairs inside blocks gives

\[
\lambda\binom p2
=
\frac{p(p-1)}4\binom42,
\]

so \(\lambda=3\).  Counting point incidences then gives replication number

\[
\frac{4|\mathcal B_i|}{p}=p-1.
\]

It remains to exclude a three-point intersection.  Translate and scale the
first block to \(V\).  Any second block meeting it in three points is obtained
from an affine map sending three distinct elements of \(V\) to three distinct
elements of \(V\).  The affine map is determined by the first two assignments.
Substitution of the third assignment gives either the identity map, hence the
same block, or a nonzero Gaussian-integer obstruction whose norm is \(1\),
\(2\), or \(5\).  In characteristic \(p\ge13\) none can vanish.  Therefore a
distinct block cannot share three points with \(V\), and affine invariance
proves the claim for all block pairs. \(\square\)

The prime \(p=5\) is exceptional: the five blocks are complements of one point
and distinct blocks meet in three points.  This is why the first-shell theorem
below begins at \(p=13\).

## 2. Exact intersection profile

Fix one affine square \(S\in\mathcal B_i\).  Let \(N_j\) be the number of blocks
\(B\in\mathcal B_i\) with

\[
|B\cap S|=j.
\]

### Theorem PX105 -- PROVED

For every fixed affine square,

\[
\boxed{
N_4=1,\qquad
N_2=12,\qquad
N_1=4(p-8),\qquad
N_0=\frac{p^2-17p+76}{4}.
}
\]

### Proof

The block itself gives \(N_4=1\).  Each of the six pairs in \(S\) lies in three
design blocks.  Besides \(S\), this gives two blocks per pair.  Super-simplicity
prevents double counting, so

\[
N_2=6\cdot2=12.
\]

Fix a vertex \(x\in S\).  There are \(p-1\) blocks through \(x\).  One is \(S\).
For each of the other three vertices of \(S\), exactly two further blocks
contain that pair, giving six blocks whose intersection with \(S\) has size
two.  Hence exactly

\[
p-1-1-6=p-8
\]

blocks through \(x\) meet \(S\) only at \(x\).  Summing over the four vertices
gives \(N_1=4(p-8)\).  Subtracting from the total block count gives

\[
N_0
=
\frac{p(p-1)}4-1-12-4(p-8)
=
\frac{p^2-17p+76}{4}.
\]

\(\square\)

## 3. Every trade after one root move

Let \(G\) be obtained from \(F\) by the PX98 trade on \(S\).

### Lemma PX105a -- PROVED

Every PX98 trade support available at \(G\) is either:

1. exactly \(S\), in which case the trade reverses \(G\) back to \(F\); or
2. disjoint from \(S\), in which case it is one of the original affine-square
   trades of \(F\).

No available trade support meets \(S\) in one, two, or three rows.

### Proof

Normalize the first trade by affine changes of row and image coordinates to

\[
F(x)=ix,
\qquad
S=\{0,1,-i,1-i\}.
\]

On these four rows the descendant \(G=F+\delta\) has deviations

\[
\begin{array}{c|c}
x&\delta(x)\\
\hline
0&1+i\\
1&1-i\\
-i&i-1\\
1-i&-1-i.
\end{array}
\]

Write a prospective PX98 support in ordered parallelogram form

\[
x_0,\quad x_1,\quad x_2,\quad x_3=x_1+x_2-x_0.
\]

The trade identities are equivalent to the three linear equations

\[
G(x_1)-G(x_0)=x_0-x_2,
\]

\[
G(x_2)-G(x_0)=x_1-x_0,
\]

\[
G(x_3)-G(x_0)=x_1-x_2.
\]

For an exact intersection of size \(k=1,2,3\), choose which \(k\) roles lie in
\(S\), assign distinct vertices of \(S\) to those roles, and use \(G(x)=ix\) on
the remaining roles.  Gaussian linear elimination gives the following complete
certificate table.

| Exact intersection size | Role/vertex assignments | Contradiction norms |
|---:|---:|---|
| 1 | 16 | \(2\) in all 16 cases |
| 2 | 72 | \(2\) in all 72 cases |
| 3 | 96 | \(1\) in 20 cases, \(2\) in 32 cases, \(5\) in 44 cases |

Thus a partial overlap could occur only in characteristics \(2\) or \(5\).
For \(p\ge13\) it is impossible.

If the support is disjoint from \(S\), then \(G=F\) on all four rows, so the
trade is an affine-root trade.  If the support is \(S\), direct substitution
gives the four parameter representations of the unique reverse trade. \(\square\)

### Corollary PX105b -- PROVED

Every one-trade descendant of an affine root has exact PX98 degree

\[
\boxed{
1+N_0
=
\frac{p^2-17p+80}{4}.
}
\]

One edge returns to the affine root.  The remaining

\[
\boxed{
\frac{p^2-17p+76}{4}
}
\]

edges apply root trades on supports disjoint from the first square and enter
the two-trade layer.

In particular, the first nonlinear shell has quadratic outward degree.

### Proof

Apply PX105a and the value of \(N_0\) from PX105.  Distinct disjoint supports
produce distinct descendants because each changes a different four-row set.
\(\square\)

The formula gives degrees \(7,20,107,205\) at primes \(13,17,29,37\),
respectively.

## 4. Consequence for switching flow

PX100 requires \(\Omega(p)\) ways to remove a prescribed edge with constant
reverse congestion.  PX105b shows that a shell vertex has far more total
outward choices, namely \(\Theta(p^2)\), but the choices are highly structured:
they are precisely affine squares disjoint from the first support.

For a row outside the first support, at most twelve affine squares through that
row meet the first support, because each of the four support vertices forms a
pair lying in three design blocks.  Hence at least

\[
p-13
\]

disjoint outward squares contain the row and remove its current affine-root
edge.  This already has the correct \(\Omega(p)\) source scale for every edge
outside the first four rows.  The remaining flow problem is to remove edges on
the original support without routing all mass through the single reverse edge.

## 5. Verification

Run

```bash
python scripts/verify_product_affine_square_first_shell.py
```

The verifier constructs the complete affine-square designs at primes
\(13,17,29,37\), checks the \(2-(p,4,3)\) parameters, reproduces every
intersection number, exhausts all descendant trades, and verifies the exact
first-shell degree formula.
