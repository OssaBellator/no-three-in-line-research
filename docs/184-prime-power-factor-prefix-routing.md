# Reduced matching factors decompose over canonical prime-power prefix-routing skeletons

CMR649--CMR655 reduce the remaining candidate-conflict problem to a strictly
smaller pure matching factor after complete essential-core contraction and
anchored deletion.  The factor host may use scattered source and target
vertices inside its inherited prime-power parent.  This chapter gives the exact
prefix recursion for such a factor.

Take the deepest full prefix cell containing every residual source and target
vertex.  Unless the factor side is one, the next base-`p` digit splits at least
one projection.  Every perfect matching then has a `p`-by-`p` child transport
table.  The transport table alone does not factor the state space, because it
does not record which vertices cross between child blocks.  The correct object
is the **vertex-routing skeleton**: for every source vertex, record the target
child it enters, and for every target vertex, record the source child from which
it is supplied.

After fixing that routing skeleton, matching choices in distinct child cells
are independent.  The complete factor family is therefore a disjoint union of
at most `p^{2d}` exact products of strict child-prefix matching hosts, where `d`
is the factor side.  Long histories either change routing skeleton a bounded
number of times or recur inside one fixed lower-dimensional child product.

Fix an inherited parent coordinate interval of side

\[
t=p^h.
\]

Let `H` be a balanced bipartite factor host with nonempty source set `X`, target
set `Y`, and

\[
|X|=|Y|=d.
\]

The source and target labels are their original parent-grid coordinates.

## 1. Canonical full-prefix envelope of a factor

For a nonempty coordinate set `A`, let

\[
\delta(A)
=
\max\{s: x\equiv x'\pmod{p^s}\text{ for all }x,x'\in A\}.
\]

Put

\[
\beta
=
\min\{\delta(X),\delta(Y)\}.
\]

### Theorem CMR656 — PROVED

There is one unique depth-`\beta` full prefix cell

\[
\boxed{
B_\beta(X,Y)
=
C_{\beta,a}\times C_{\beta,c}
}
\]

containing `X\times Y`, where `a` and `c` are the common source and target
residues modulo `p^\beta`.

It is the deepest full prefix cell containing the factor.  Its side length is

\[
\boxed{q_\beta=t/p^\beta.}
\]

If `d\ge2`, then

\[
\boxed{\beta<h.}
\]

### Proof

The definitions of `\delta(X)` and `\delta(Y)` give unique common residues at
every depth up to their respective values.  Their minimum is therefore the
deepest depth at which both projections lie in one prefix block.  A depth-`s`
prefix block has side `t/p^s`.

If `\beta=h`, both `X` and `Y` lie in singleton depth-`h` blocks, forcing
`d=1`. ∎

The cell `B_\beta(X,Y)` is the canonical matching-factor envelope.

## 2. First child split and projection support

Assume `d\ge2`, so `\beta<h`.  For `r,s\in\{0,\ldots,p-1\}`, define the next
digit classes

\[
X_r
=
\left\{x\in X:
\left\lfloor\frac{x}{p^\beta}\right\rfloor
\equiv r\pmod p
\right\},
\]

\[
Y_s
=
\left\{y\in Y:
\left\lfloor\frac{y}{p^\beta}\right\rfloor
\equiv s\pmod p
\right\}.
\]

Let

\[
r_X=|\{r:X_r\ne\varnothing\}|,
\qquad
r_Y=|\{s:Y_s\ne\varnothing\}|.
\]

### Theorem CMR657 — PROVED

At least one projection splits at the next digit:

\[
\boxed{\max\{r_X,r_Y\}\ge2.}
\]

Every child full prefix cell

\[
X_r\times Y_s
\]

lies inside one strict depth-`\beta+1` descendant of
`B_\beta(X,Y)` of side

\[
\boxed{q=t/p^{\beta+1}.}
\]

### Proof

If both projections occupied only one next-digit class, then all source and
target coordinates would have a common prefix of length `\beta+1`, contradicting
the maximality of `\beta`.  Appending one digit to each common prefix gives the
strict child cells and their side length. ∎

Thus every nontrivial factor has a canonical first recursive split.

## 3. Exact child transport table

Let `M\in\operatorname{PM}(H)`.  Define

\[
m_{rs}(M)
=
|M\cap(X_r\times Y_s)|.
\]

Put

\[
x_r=|X_r|,
\qquad
y_s=|Y_s|.
\]

### Theorem CMR658 — PROVED

The matrix

\[
\boxed{\mathbf m(M)=(m_{rs}(M))_{r,s\in\mathbb F_p}}
\]

has nonnegative integer entries and exact margins

\[
\boxed{
\sum_s m_{rs}=x_r,
\qquad
\sum_r m_{rs}=y_s,
\qquad
\sum_{r,s}m_{rs}=d.
}
\]

If `z(M)` is the number of positive entries, then

\[
\boxed{
z(M)\ge\max\{r_X,r_Y\}}
\]

and

\[
\boxed{
z(M)\ge\left\lceil\frac d q\right\rceil.}
\]

### Proof

Every source vertex is matched once, giving the row sums; every target vertex
is used once, giving the column sums.  Summing either set of margins gives `d`.

Every nonempty source class contributes to a positive matrix row and hence to
at least one positive entry; the target argument is symmetric.  A depth-
`\beta+1` child cell contains only `q` source coordinates and `q` target
coordinates, so a matching uses at most `q` edges in one cell.  Therefore at
least `\lceil d/q\rceil` cells are occupied. ∎

The transport table records exact child-cell loads but not vertex routing.

## 4. Vertex-routing skeletons

For one matching `M`, define

\[
X_{rs}(M)
=
\{x\in X_r:M(x)\in Y_s\},
\]

\[
Y_{rs}(M)
=
\{y\in Y_s:M^{-1}(y)\in X_r\}.
\]

The **routing skeleton** is

\[
\Gamma(M)
=
\bigl((X_{rs}(M),Y_{rs}(M))\bigr)_{r,s}.
\]

### Theorem CMR659 — PROVED

For every routing skeleton `\Gamma`:

1. the sets `X_{rs}` partition `X`, and for each `r` the sets over `s` partition
   `X_r`;
2. the sets `Y_{rs}` partition `Y`, and for each `s` the sets over `r` partition
   `Y_s`;
3. one has
   \[
   \boxed{|X_{rs}|=|Y_{rs}|=m_{rs};}
   \]
4. the matching family with routing skeleton `\Gamma` factors exactly as
   \[
   \boxed{
   \operatorname{PM}(H;\Gamma)
   \cong
   \prod_{r,s}
   \operatorname{PM}\bigl(H[X_{rs},Y_{rs}]\bigr).
   }
   \]

Empty child factors contribute one empty matching.

### Proof

Every source and target vertex has one matching partner, so the routing sets
form the stated partitions and corresponding source/target sets have equal
size.

After the routing sets are fixed, an edge incident with `X_{rs}` must terminate
in `Y_{rs}` and every vertex of those two sets must be matched internally.
Different child pairs use disjoint source and target sets, so their perfect
matchings may be chosen independently and united.  Conversely every state with
skeleton `\Gamma` restricts to one perfect matching in each induced child host.
These operations are inverse. ∎

This is the exact multi-child analogue of the two-block product CMR618.

## 5. Finite routing-skeleton stock

### Theorem CMR660 — PROVED

The number of routing skeletons realised by perfect matchings of `H` is at most

\[
\boxed{N_\Gamma(H)\le p^{2d}.}
\]

More precisely, for a fixed transport matrix `\mathbf m`, the number of
possible routing skeletons is at most

\[
\boxed{
\prod_r
\frac{x_r!}{\prod_s m_{rs}!}
\cdot
\prod_s
\frac{y_s!}{\prod_r m_{rs}!}.
}
\]

### Proof

For each source vertex, record one of `p` target-child labels, giving at most
`p^d` source assignments.  Independently, each target vertex records one of `p`
source-child labels, giving at most `p^d` target assignments.  Valid routing
skeletons are a subset of these assignments.

For fixed margins and entries, the source routing subsets are counted by the
row multinomials and the target routing subsets by the column multinomials.
Multiply. ∎

The coarse `p^{2d}` bound is uniform over all factor hosts and transport tables.

## 6. Routing recurrence or finite history

Consider a simple history of `T` distinct perfect matchings of the fixed factor
host `H`.

### Theorem CMR661 — PROVED

For every integer `\lambda\ge2`, at least one of the following holds.

1. **Exact routing-skeleton recurrence.**  One skeleton `\Gamma` occurs in at
   least `\lambda` factor states.
2. **Finite routing history.**
   \[
   \boxed{
   T\le(\lambda-1)p^{2d}.
   }
   \]

In the recurrent branch, all varying matching choices lie in the exact child
product of CMR659.

### Proof

Assign every factor matching its unique routing skeleton.  If no skeleton has
multiplicity `\lambda`, every one of the at most `p^{2d}` skeletons occurs at most
`\lambda-1` times. ∎

Thus long pure-factor history recurs inside one strict child-prefix product.

## 7. Heavy or dispersed child cells

For one transport table, fix an integer threshold `H_0\ge2`.

### Theorem CMR662 — PROVED

At least one of the following holds.

1. **Heavy child cell.**  Some depth-`\beta+1` full prefix cell contains at least
   \[
   \boxed{H_0}
   \]
   matching edges.
2. **Dispersed child support.**  At least
   \[
   \boxed{
   \left\lceil\frac d{H_0-1}\right\rceil
   }
   \]
   child cells are occupied.

With

\[
H_0=\max\{2,\lceil\sqrt d\rceil\},
\]

one obtains a child cell of load at least `\lceil\sqrt d\rceil` or at least
`\lfloor\sqrt d\rfloor` occupied child cells.

### Proof

The positive entries of the transport table sum to `d`.  If none reaches
`H_0`, each is at most `H_0-1`, requiring the displayed number of positive
entries.  The square-root form is the usual threshold substitution. ∎

Every occupied cell is a strict descendant with absolute prefix coordinates.

## 8. Factor-prefix recursion endpoint

### Corollary CMR663 — PROVED

Every nontrivial pure residual factor of side `d\ge2` from CMR655 reaches at
least one of the following endpoints.

1. **Strict contained descendant.**  Its canonical factor envelope has
   `\beta\ge1`, so the complete factor lies inside a strict inherited full prefix
   cell of side `t/p^\beta`.
2. **Finite routing history.**  The CMR661 bound holds.
3. **Recurrent child product.**  One routing skeleton recurs and the factor
   family is the exact product of strict child hosts
   \[
   \prod_{r,s}\operatorname{PM}(H[X_{rs},Y_{rs}]).
   \]
4. **Heavy child block.**  One strict child full-prefix cell carries the CMR662
   load.
5. **Dispersed absolute child cells.**  Many strict child cells are occupied and
   enter the existing full-token/carry ledger.

The routing skeleton, child coordinates, factor owner, and inherited envelope
are all fixed labels.  No child factor or token can migrate anonymously between
recursive calls.

### Proof

Use CMR656--CMR657 for the canonical envelope and first split.  Apply CMR661 to
factor histories, CMR659 in the recurrent branch, and CMR662 to each transport
table. ∎

## 9. Revised frontier

The pure-factor recursion now lands inside the prime-power prefix hierarchy.

- Every reduced factor has one canonical full-prefix envelope.
- Its first nontrivial digit split has an exact transport table.
- Fixing vertex routing gives an exact product of strict child-prefix factors.
- Routing history has finite stock.
- Child loads give heavy-block or dispersed-carry alternatives.

The remaining prime-power frontier is payment across the recurrent child
product: either one child factor recursively supplies a clean matching, or
cross-child candidate conflicts produce another sparse low-rank rectangle,
while repeated routing changes pay full-token return or strict closure-envelope
expansion.

No all-`n` theorem is claimed.  Envelope depth, transport margins, child-cell
capacity, routing-skeleton factorisation, and skeleton stock are checked in
[`scripts/verify_prime_power_factor_prefix_routing.py`](../scripts/verify_prime_power_factor_prefix_routing.py).
