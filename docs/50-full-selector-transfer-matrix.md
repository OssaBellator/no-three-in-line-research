# Transfer matrix for abstract full-selector states

PX50 shows that the complete four-layer host for the side-two outer factor
depends combinatorially only on the relative permutation `H` of the inner
factor.  This chapter counts every spanning degree-two selector state before
geometry is imposed.

The count separates exactly over the cycles of `H` and has a closed form.

## 1. One relative cycle

Let one cycle of `H` have length `L>=2`, written cyclically as

\[
x\mapsto x+1\pmod L.
\]

The corresponding abstract host component has:

- two row vertices at each position `x`;
- two column vertices at each position `x`;
- every row vertex at `x` adjacent to both column vertices at `x` and both
  column vertices at `x+1`.

A selector state chooses degree two at every row and every column vertex.

Process the row positions cyclically.  Before processing position `x`, record
the degrees already contributed to the two column vertices at `x` by the rows at
`x-1`.  The boundary state is therefore

\[
(d_0,d_1)\in\{0,1,2\}^2.
\]

Each of the two row vertices at `x` chooses two of its four incident targets.
The choices must complete the current two column degrees to two; their
contributions to position `x+1` form the outgoing boundary state.

In the state order

```text
(0,0) (0,1) (0,2) (1,0) (1,1) (1,2) (2,0) (2,1) (2,2)
```

the transition matrix is

\[
M=
\begin{pmatrix}
1&0&0&0&0&0&0&0&0\\
0&2&0&2&0&0&0&0&0\\
0&0&1&0&2&0&1&0&0\\
0&2&0&2&0&0&0&0&0\\
0&0&2&0&6&0&2&0&0\\
0&0&0&0&0&2&0&2&0\\
0&0&1&0&2&0&1&0&0\\
0&0&0&0&0&2&0&2&0\\
0&0&0&0&0&0&0&0&1
\end{pmatrix}.
\]

Cyclic closure requires the outgoing state after `L` positions to equal the
incoming state, so the selector count is

\[
A_L=\operatorname{tr}(M^L).
\]

## Theorem PX54 -- PROVED

For every `L>=2`, the number of spanning degree-two selector states supported on
one relative `L`-cycle is

\[
\boxed{
A_L
=
2+2\cdot4^L
+(4+2\sqrt3)^L
+(4-2\sqrt3)^L.
}
\]

If the relative permutation has cycle lengths

\[
L_1,\ldots,L_k,
\]

then the complete abstract host is the disjoint union of the corresponding
components, and the total selector-state count is

\[
\boxed{
\prod_{q=1}^k A_{L_q}.
}
\]

### Proof

The transfer construction above proves `A_L=tr(M^L)`.  The matrix decomposes
into:

- two one-dimensional blocks with eigenvalue `1`;
- two copies of
  \(
  \begin{pmatrix}2&2\\2&2\end{pmatrix}
  \), with eigenvalues `4,0`;
- one three-dimensional block
  \(
  \begin{pmatrix}1&2&1\\2&6&2\\1&2&1\end{pmatrix}
  \), with eigenvalues `0,4+2sqrt(3),4-2sqrt(3)`;
- one additional zero eigenvalue.

Taking the trace of the `L`th power gives the displayed formula.  Distinct
cycles of `H` use disjoint row and column vertices and have no common host
edges, so selector choices multiply. \(\square\)

The radical terms sum to an integer.  If

\[
B_L=(4+2\sqrt3)^L+(4-2\sqrt3)^L,
\]

then

\[
B_0=2,
\qquad
B_1=8,
\qquad
B_L=8B_{L-1}-4B_{L-2}.
\]

## 2. Exact component counts

The first relevant values are:

| Relative cycle length `L` | `A_L` |
|---:|---:|
| 2 | 90 |
| 3 | 546 |
| 4 | 3,618 |
| 5 | 25,218 |
| 6 | 181,122 |
| 7 | 1,323,522 |
| 8 | 9,765,378 |

The exponential growth rate for one long cycle is

\[
4+2\sqrt3\approx7.4641.
\]

Thus the abstract selector space is large even though its count is exactly
controlled.

## Corollary PX55 -- PROVED

For the three relative cycle types occurring among saturated side-six factors,
the exact numbers of abstract spanning degree-two states are:

| Relative cycle type | Selector states |
|---|---:|
| `(6)` | 181,122 |
| `(4,2)` | `3,618 * 90 = 325,620` |
| `(3,3)` | `546^2 = 298,116` |

These counts are independent of the geometric permutations `T,P,Q` from PX50.
The latter determine where the abstract selector cells land in the scalar grid
and therefore which of these states are no-three.

## 3. Verification

Run

```bash
python scripts/verify_product_selector_transfer.py
```

The verifier constructs the transition matrix directly from the two row choices,
checks the displayed matrix, compares `tr(M^L)` with the integer recurrence
formula for `2<=L<=8`, and verifies the three side-six products.

## 4. Consequence for the remaining bottleneck

PX54 removes raw selector enumeration as a conceptual mystery.  For each
relative cycle type, the complete selector space is an explicit product of
cyclic transfer systems.  The unresolved difficulty is geometric:

- `T,P,Q` couple the otherwise independent relative cycles in the scalar grid;
- collinear triples can use cells from different selector components;
- the exact no-three condition is not visible in the nine-state degree transfer
  alone.

The next useful refinement would enrich the boundary state with a bounded
geometric signature, or derive a resampling theorem over the transfer-generated
selector measure.  No such theorem is currently proved.
