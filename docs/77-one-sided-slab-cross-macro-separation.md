# One-sided slab separation for cross-macro same-edge pairs

The movement and refill points controlled by one source edge determine a
negative-slope line.  By ordering source column slabs and movement-row label
blocks in the same direction, one can exclude every movement point of another
macro from that line.  The transposed construction gives the analogous refill
separation.

## 1. Universal slab pools

Let `P` be a perfect matching on `[m]`.  Fix positive integers `M,R` with

\[
 MR\le m.
\]

Choose pairwise disjoint consecutive old-column intervals

\[
 C_1< C_2<\cdots<C_M,
 \qquad |C_i|=R,
\]

where `C_i<C_j` means every coordinate in `C_i` is smaller than every coordinate
in `C_j`.  Let

\[
 E_i=\{(x,y)\in P:x\in C_i\}.
\]

### Proposition PP3ga -- PROVED

The sets `E_1,...,E_M` are pairwise disjoint matching pools of size `R`.

#### Proof

A perfect matching has exactly one edge in each old column.  Therefore the `R`
columns of `C_i` support exactly `R` edges, and disjoint column intervals give
disjoint edge sets.  Every subset of a perfect matching is a matching. ∎

At the balanced exponents of PP3dg,

\[
 M=m^{23/80+o(1)},
 \qquad
 R=m^{19/40+o(1)},
\]

one has `MR=m^(61/80+o(1))=o(m)`, so these slab pools exist with ample unused
source coordinates.  Unlike the monotone-pool extraction, no endpoint order
inside one pool is required by the product-LLL macro construction.

## 2. Ordered movement labels

Put `T=MW` and partition the actual final new-row set

\[
 \mathcal A=\{m+1,\ldots,m+T\}
\]

into consecutive intervals

\[
 A_1<A_2<\cdots<A_M,
 \qquad |A_i|=W.
\]

Macro `i` uses movement rows from `A_i`.  Its refill columns may be assigned by
the global matching PP3fw and need not be ordered for the theorem below.

For one slot of macro `i`, controlled by `e=(x,y) in E_i`, write

\[
 M_e=(x,A),
 \qquad
 F_e=(B,y),
\]

where `A in A_i` and `B>m`.  The line `M_eF_e` has negative slope.

### Theorem PP3gb -- PROVED

No movement point of any other macro lies on the same-slot line `M_eF_e`.
Equivalently, every grouped forbidden relation consisting of

- the movement/refill pair controlled by one slot of macro `i`, and
- one movement point controlled by a slot of macro `j!=i`

is empty.

#### Proof

Take `j>i`.  Every source column in `C_j` is larger than `x`, and every movement
row in `A_j` is larger than `A`.  Hence every movement point `(x',A')` of macro
`j` is strictly northeast of `M_e`:

\[
 x'>x,
 \qquad
 A'>A.
\]

But the line through `M_e` and `F_e` has negative slope.  To the right of
`M_e`, every point of that line has second coordinate strictly smaller than
`A`.  Thus `(x',A')` is not on it.

If `j<i`, every movement point of macro `j` is strictly southwest of `M_e`.
To the left of `M_e`, a negative-slope line has second coordinate strictly
larger than `A`, so the southwest point is again excluded. ∎

This removes one entire high-probability cross-macro class without using any
state entropy or local-lemma budget.

## 3. Transposed refill version

Choose instead pairwise disjoint consecutive old-row intervals

\[
 Y_1<\cdots<Y_M,
 \qquad |Y_i|=R,
\]

and let `E_i` contain the matching edges whose old row lies in `Y_i`.  Partition
the actual final new columns into ordered intervals

\[
 B_1<\cdots<B_M,
 \qquad |B_i|=W.
\]

### Corollary PP3gc -- PROVED

With the row-slab pools and ordered refill-column intervals, no refill point of
one macro lies on the same-slot movement/refill line of another macro.

#### Proof

Transpose the proof of PP3gb.  A later refill point is strictly northeast of the
refill endpoint `F_e`, while the same-slot line has negative slope; an earlier
refill point is strictly southwest. ∎

Thus every saturated source offers two one-sided architectures:

1. column slabs eliminate cross-macro movement completions of same-edge pairs;
2. row slabs eliminate cross-macro refill completions of same-edge pairs.

## 4. Weighted-energy consequence

Split the grouped cross-macro pair relation of PP3fm for a same-slot
movement/refill pair into

\[
 \Gamma^{hM}_{s,t}
\]

when the third point is a movement point of slot `t`, and

\[
 \Gamma^{hF}_{s,t}
\]

when it is a refill point.

### Corollary PP3gd -- PROVED

In the column-slab architecture,

\[
 \Gamma^{hM}_{s,t}=\varnothing
 \quad\text{for all cross-macro slot pairs }s,t.
\]

In the row-slab architecture,

\[
 \Gamma^{hF}_{s,t}=\varnothing.
\]

Therefore the corresponding contribution to every grouped pair completion
energy `bar d_{s,t}` and every external slot mass `Lambda_ext(s)` is exactly
zero.

#### Proof

The relations record precisely the geometric configurations excluded by PP3gb
and PP3gc. ∎

## 5. Remaining cross-macro geometry

One-sided slab ordering does not remove:

- the opposite third-point type for a same-slot pair;
- ordinary cross-macro pairs controlled by two source edges;
- triples using one point from each of three slots.

Those remain in the grouped completion energies PP3fp.  The theorem nevertheless
removes the rank-one source-edge spike from one whole movement/refill direction
and is universal at the balanced prime-gap exponents.