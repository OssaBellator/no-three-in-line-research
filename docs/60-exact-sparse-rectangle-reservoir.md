# Exact sparse rectangle reservoirs

PX63 gives, for every saturated no-three side-`n` factor, a factor-compatible
side-`2n` rectangle state with separate expected defect bounds

\[
\mathbb E D_2\le \frac{8n^2}{n-1},
\qquad
\mathbb E D_3\le
12288\frac{n^3}{(n-1)(n-2)}H_{2n-1},
\]

where `D_2` counts diagonal defects involving two rectangles and `D_3` counts
transversal defects involving three rectangles.

This chapter extracts an exact no-three subconfiguration while retaining whole
rectangles.  To avoid collisions with the concurrently advancing PX index, the
results use the stable local prefix `PR` (product reservoir).

## Theorem PR1 -- PROVED

For every `n>=3`, every saturated no-three side-`n` factor has a
factor-compatible rectangle state satisfying simultaneously

\[
D_2\le48n,
\qquad
D_3\le221184\,nH_{2n-1}.
\]

### Proof

Markov's inequality gives

\[
\Pr(D_i>4\mathbb ED_i)<1/4
\]

for `i=2,3`, so one state satisfies both four-times-expectation bounds. For
`n>=3`,

\[
\frac n{n-1}\le\frac32,
\qquad
\frac{n^2}{(n-1)(n-2)}\le\frac92,
\]

which gives the displayed constants. PX39 transports the normalized state to
every factor layer. \(\square\)

## Lemma PR2 -- PROVED

Let a hypergraph on `n` vertices have `e_2` edges of size two and `e_3` edges of
size three. For every `q in [0,1]`, it has an independent set of size at least

\[
nq-e_2q^2-e_3q^3.
\]

### Proof

Select every vertex independently with probability `q`. The expected number of
selected vertices is `nq`, while the expected numbers of surviving rank-two and
rank-three edges are `e_2q^2` and `e_3q^3`. Delete one vertex from each
surviving edge and average. \(\square\)

## Theorem PR3 -- PROVED

For every `n>=3` and every saturated no-three side-`n` factor, there is a
factor-compatible family of at least

\[
\boxed{
 m\ge
 \frac{n}{8\sqrt{221184\,H_{2n-1}}}
}
\]

whole product rectangles whose union is no-three.

The union has `4m` points and uses exactly `2m` scalar rows and `2m` scalar
columns, with exactly two points in every used row and column. Thus

\[
m=\Omega\!\left(\frac{n}{\sqrt{\log n}}\right).
\]

### Proof

Take the state from PR1 and form a defect hypergraph on its rectangle indices.
Use

\[
K=221184,
\qquad
q=\frac1{4\sqrt{KH_{2n-1}}}.
\]

PR2 gives an independent set of size at least

\[
nq-D_2q^2-D_3q^3.
\]

The rank-three term satisfies

\[
D_3q^3\le\frac1{16}nq.
\]

The rank-two term satisfies

\[
D_2q^2\le\frac{3n}{KH_{2n-1}}\le\frac1{48}nq,
\]

because `H_{2n-1}>=H_5>3/2` and therefore
`sqrt(KH_{2n-1})>576`. Hence the independent set has size greater than
`nq/2`, which is the displayed bound.

Three corners of one rectangle are never collinear. A bad triple using two
rectangles would be a retained rank-two defect, and a bad triple using three
rectangles would be a retained rank-three defect. Independence excludes both.
Since the rectangle maps are permutations, retained rectangles use distinct
row and column labels in both coarse blocks, giving degree two on every used
scalar row and column. \(\square\)

## Consequence and next target

PR3 is an exact all-side output of the product program: a protected no-three
reservoir occupying `Omega(n/sqrt(log n))` rectangle components.

The remaining general-proof target is a protected extension theorem. One must
show that the unused product host retains enough regularity to complete the
remaining rows and columns without creating a triple with the PR3 reservoir.
The transposition decoder PX67--PX71, neutralization banks PX72--PX80,
direction protection PX81--PX88, and protected matching reductions PX89 onward
supply the relevant local and structured mechanisms.

A successful completion theorem can therefore be attacked in two equivalent
forms:

1. prove superregularity and bounded certificate load in the unused host after
   conditioning on the sparse reservoir; or
2. prove the simultaneous-rainbow rank-three spread hypothesis PX97 for the
   protected nonlinear coset completion, using the strong-complete four-trade
   PX98, the order-thirteen spread evidence PX99, and the switching-flow
   criterion PX100.

## Verification

Run

```bash
python scripts/verify_product_sparse_rectangle_reservoir.py
```

The verifier checks PR2 exhaustively on all simple rank-two/rank-three
hypergraphs through four vertices, checks the PR3 numerical inequalities through
side 10000, and verifies exact rectangle-reservoir extraction on small
normalized states.