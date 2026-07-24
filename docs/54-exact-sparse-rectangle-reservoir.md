# Exact sparse rectangle reservoirs from universal product seeds

PX63--PX64 produce, for every saturated no-three side-`n` factor, a
factor-compatible saturated side-`2n` rectangle state with only `O(n log n)`
bad triples.  This chapter extracts an exact no-three subconfiguration from that
state.  The extraction keeps whole rectangles, so it preserves degree two on
every scalar row and column that remains in use.

The result is not yet a saturated configuration on all `2n` rows and columns.
It is an exact all-side reservoir of size

\[
\Omega\!\left(\frac{n}{\sqrt{\log n}}\right)
\]

rectangles, and therefore of the same order of used rows and columns.  It gives
a structured exact starting set for absorption or extension arguments.

Throughout, let

\[
H_k=\sum_{d=1}^k\frac1d
\]

be the harmonic number.

## 1. Rank-two and rank-three defect separation

In the PX43 rectangle normal form, every bad triple is of one of two kinds.

- A **diagonal defect** uses two opposite corners of one rectangle and one
  corner of a second rectangle.  It therefore involves exactly two rectangle
  indices.
- A **transversal defect** uses one corner from each of three rectangles.  It
  therefore involves exactly three rectangle indices.

Write `D_2` and `D_3` for the numbers of these defects.

PX63 proves the separate expectation bounds

\[
\mathbb E D_2\le \frac{8n^2}{n-1}
\]

and

\[
\mathbb E D_3
\le
12288\,\frac{n^3}{(n-1)(n-2)}H_{2n-1}.
\]

### Lemma PX65 -- PROVED

For every `n>=3`, every saturated no-three side-`n` factor has a
factor-compatible rectangle state satisfying simultaneously

\[
D_2\le 48n
\]

and

\[
D_3\le 221184\,nH_{2n-1}.
\]

### Proof

Choose the random rectangle state from PX63.  By Markov's inequality,

\[
\Pr(D_2>4\mathbb E D_2)<\frac14,
\qquad
\Pr(D_3>4\mathbb E D_3)<\frac14.
\]

Hence with positive probability both displayed four-times-expectation bounds
hold.

For `n>=3`,

\[
\frac{n}{n-1}\le\frac32,
\qquad
\frac{n^2}{(n-1)(n-2)}\le\frac92.
\]

Therefore

\[
4\frac{8n^2}{n-1}\le48n
\]

and

\[
4\cdot12288\frac{n^3}{(n-1)(n-2)}H_{2n-1}
\le
221184\,nH_{2n-1}.
\]

Full-symmetric gauge transport makes the resulting scalar state available to
every factor layer. \(\square\)

## 2. Rank-sensitive alteration

The following elementary form is recorded separately because it is reusable for
other product-state syndrome hypergraphs.

### Lemma PX66 -- PROVED

Let a hypergraph on `n` vertices have `e_2` edges of size two and `e_3` edges of
size three.  For every `q in [0,1]`, it has an independent set of size at least

\[
nq-e_2q^2-e_3q^3.
\]

### Proof

Select every vertex independently with probability `q`.  The expected number
of selected vertices is `nq`; the expected numbers of surviving two- and
three-edges are `e_2q^2` and `e_3q^3`.

From the selected set, delete one vertex from each surviving edge.  The result
is independent, and its size is at least the number selected minus the number
of surviving edges.  Averaging proves the claim. \(\square\)

## 3. Universal exact reservoir

Put

\[
K=221184
\]

and

\[
q=\frac{1}{4\sqrt{K H_{2n-1}}}.
\]

### Theorem PX67 -- PROVED

For every `n>=3` and every saturated no-three side-`n` factor, there is a
factor-compatible collection of at least

\[
\boxed{
 m\ge
 \frac{n}{8\sqrt{221184\,H_{2n-1}}}
}
\]

whole product rectangles whose union is no-three.

The union has exactly `4m` points.  It uses exactly `2m` scalar rows and `2m`
scalar columns, with exactly two selected points in every used row and every
used column.

In particular,

\[
m=\Omega\!\left(\frac{n}{\sqrt{\log n}}\right).
\]

### Proof

Take the rectangle state from PX65 and form a defect hypergraph on its `n`
rectangle indices.  Insert one size-two edge for each diagonal defect and one
size-three edge for each transversal defect.  Multiple defects may produce the
same hyperedge; retaining multiplicity only weakens the alteration bound.

Apply PX66 with the displayed value of `q`.  The transversal deletion term is

\[
D_3q^3
\le
KnH_{2n-1}\,
\frac{1}{64(KH_{2n-1})^{3/2}}
=
\frac{n}{64\sqrt{KH_{2n-1}}}
=
\frac1{16}nq.
\]

The diagonal deletion term satisfies

\[
D_2q^2
\le
48n\frac{1}{16KH_{2n-1}}
=
\frac{3n}{KH_{2n-1}}.
\]

Since `n>=3`, we have `H_{2n-1}>=H_5>3/2`, and hence

\[
\sqrt{KH_{2n-1}}>576.
\]

Consequently

\[
D_2q^2
\le
\frac1{48}nq.
\]

Thus PX66 gives an independent rectangle set of size at least

\[
nq\left(1-\frac1{16}-\frac1{48}\right)
=\frac{11}{12}nq
>\frac12nq
=
\frac{n}{8\sqrt{KH_{2n-1}}}.
\]

A triple among the retained points cannot lie within one rectangle, since three
corners of a nondegenerate axis-parallel rectangle are not collinear.  If it
uses two rectangles it would be a retained diagonal defect, and if it uses
three rectangles it would be a retained transversal defect.  Independence of
the rectangle set excludes both possibilities, so the union is no-three.

The permutations controlling the rectangle state give distinct scalar row
labels in each of the two row blocks and distinct scalar column labels in each
of the two column blocks.  Hence `m` retained rectangles use `2m` distinct rows
and `2m` distinct columns, and each used row and column contains exactly the two
corners supplied by its rectangle. \(\square\)

## 4. Structural interpretation

PX67 gives an exact object rather than only a low-defect state:

- a no-three set of `4m` points;
- degree two on every used row and column;
- a decomposition into `m` disjoint four-corner product rectangles;
- compatibility with every saturated side-`n` factor after block-map transport;
- `m=Omega(n/sqrt(log n))` uniformly in the factor.

The missing step is now an **extension theorem**: enlarge such a sparse exact
rectangle reservoir until all `2n` rows and columns are covered, while keeping
its existing points protected.  The branch already contains clone-host and
superregular completion criteria, so the concrete next target is to prove that
the unused product-host cells retain sufficient regularity after conditioning
on the PX67 reservoir.

A successful protected-extension theorem would upgrade the universal sparse
reservoir into exact product doubling.

## Verification

Run

```bash
python scripts/verify_product_sparse_rectangle_reservoir.py
```

The verifier checks the alteration inequality exhaustively over small rank-two
and rank-three hypergraphs, verifies the numerical constants for a range of
sides, and extracts exact independent rectangle reservoirs from every
normalized rectangle state through base side four.