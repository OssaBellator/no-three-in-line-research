# Rank-one heavy-cell avoidance and coordinate concentration

PX228--PX229 give a cellwise decoder: a candidate cell of large rank-one weight
centres a large endpoint-disjoint secant star.  Their expectation bound still
pays every positive cell through the matching cylinder constant.

There is a sharper alternative.  Put all high-weight cells directly into the
forbidden graph.  If they have bounded row and column degree, the optimized
matching bank avoids them deterministically.  If they do not, the rank-one
obstruction is concentrated along one coordinate.

Let the retained block have order `s`.  Let `F` be the inherited forbidden graph
of maximum row and column degree `Delta`.  For every candidate cell `f`, let

\[
\mu(f)
=
|\{\{z,z'\}\subseteq Z:f,z,z'\text{ are collinear}\}|
\]

be its rank-one/two-background weight.

For a threshold `m>0`, define the heavy-cell graph

\[
H_m=\{f:\mu(f)\ge m\}
\]

and let

\[
\lambda_m
=
\max\{\Delta_{\rm row}(H_m),\Delta_{\rm col}(H_m)\}.
\]

## 1. Deterministic rank-one truncation

### Theorem PX245 -- PROVED

If

\[
\boxed{s\ge8(\Delta+\lambda_m),}
\]

then there is a nonempty perfect-matching bank avoiding both `F` and `H_m`.
Every matching `M` in this bank satisfies

\[
\boxed{
T_{1,2}(M)=\sum_{f\in M}\mu(f)<ms.
}
\]

The uniform bank has fixed-rank cylinder bound

\[
\boxed{
\Pr(E\subseteq M)
\le
\frac{\mathcal C(s,\Delta+\lambda_m)}{(s)_{|E|}}.
}
\]

If `s>=8(Delta+lambda_m)+2`, the cylinder factor is at most
`e^(2(Delta+lambda_m))`.

### Proof

The union `F union H_m` has maximum row and column degree at most
`Delta+lambda_m`.  Apply PX232.  Every selected cell outside `H_m` has weight
strictly less than `m`, and a perfect matching contains exactly `s` cells.
\(\square\)

Thus bounded-degree heavy rank-one cells can be removed from the probabilistic
creation ledger entirely.  Only their degree, not their total number, enters the
spread constant.

## 2. Sharp executability version

### Corollary PX246 -- PROVED

If

\[
\boxed{s\ge2(\Delta+\lambda_m),}
\]

then at least one perfect matching avoids `F union H_m` and has rank-one cost
less than `ms`.

The factor two is sharp for general forbidden graphs, by PX200.

### Proof

Apply the sharp Hall threshold PX200 to the union of the inherited and heavy-cell
forbidden graphs. \(\square\)

## 3. Failure forces coordinate concentration

### Theorem PX247 -- PROVED

At least one of the following holds.

1. there is an allowed perfect matching using only cells of rank-one weight less
   than `m`;
2. some candidate row or column contains more than
   
   \[
   \boxed{\frac s2-\Delta}
   \]
   
   cells of weight at least `m`.

### Proof

If every row and column of `H_m` has degree at most `s/2-Delta`, then
`F union H_m` has maximum degree at most `s/2`.  PX200 supplies a perfect
matching avoiding the union.  Take the contrapositive. \(\square\)

This is an exact Hall-type concentration statement.  It is stronger than a
large total rank-one weight: the heavy cells must occupy one common coordinate
unless a low-cost transversal exists.

## 4. Coordinate fields of star centres

Assume every line contains at most `K` background points, as in PX228.

### Corollary PX248 -- PROVED

For every threshold `m`, either:

1. an allowed matching has total rank-one cost less than `ms`; or
2. one candidate row or column contains more than `s/2-Delta` distinct cells,
   each of which centres an endpoint-disjoint secant star of order at least
   
   \[
   \boxed{\frac mK.}
   \]

With the quantitative slack `s>=8(Delta+lambda_m)`, alternative 1 holds for a
complete fixed-rank-spread bank, not merely for one matching.

### Proof

Apply PX247.  Every heavy cell in the concentrated coordinate has
`mu(f)>=m`, so PX228 extracts a star of order at least `mu(f)/K>=m/K` from that
cell. \(\square\)

The second alternative is a new composite decoder object: a row or column field
of many candidate star centres.  The stars need not yet be endpoint-disjoint
across different centres; controlling that overlap is the next geometric task.

## 5. Consequence for the linear sign problem

The rank-one sector now has a three-way interface.

1. **Sparse heavy cells:** forbid them and make rank-one cost deterministically
   less than `ms`, retaining optimized spread with degree `Delta+lambda_m`.
2. **One very heavy cell:** PX228 extracts one large clean star.
3. **Many heavy cells:** PX248 forces a coordinate field of star centres.

For loaded-line states, whose destruction coefficient is at least
`s ell^2/32` by PX242, one may choose any threshold

\[
m<\frac{\ell^2}{32}
\]

and still leave positive destruction margin after deterministic rank-one
truncation, provided `lambda_m` is bounded enough for the other sector constants.
This converts the loaded-line sign problem into a degree bound for the heavy-cell
field.

For clean stars and radial cores, where guaranteed destruction is only linear,
the useful threshold is `m<1`; since `mu` is integral, this asks for a matching
using only zero-rank-one cells.  PX247 says failure of that strongest truncation
forces more than `s/2-Delta` positive-weight cells in one coordinate.

## 6. Updated frontier

Rank one no longer has to be paid solely by a first-moment average.  It can be
eliminated deterministically whenever high-weight cells are coordinate-sparse.
The unresolved rank-one geometry is now precise:

> decode a row or column containing linearly many candidate centres of
> endpoint-disjoint background secant stars.

A bounded-overlap extraction from such a coordinate field would either produce
a large simultaneous neutralization batch or a loaded background point/line,
and would complete the rank-one side of the strict-sign theorem.

## 7. Verification

Run

```bash
python scripts/verify_product_rank_one_heavy_avoidance.py
```

The verifier enumerates weighted small matching grids, checks the Hall threshold,
checks the quantitative augmented-forbidden bank conditions, and verifies the
coordinate-concentration alternative.
