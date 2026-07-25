# Historical back-edge reset and antichain child extraction

PX291--PX293 reduce a genuinely immobile terminal block to an acyclic allowed
label digraph whose forbidden positions are a bounded base together with one
historical partial matching per ancestor level.  This chapter separates two
possibilities.

A historical position which points backwards across an allowed reachability
path is an immediate reset edge: releasing its unique ancestor constraint
closes a principal directed cycle.  If no such reset edge exists, every reverse
comparability is already paid by the bounded base graph.  The reachability
poset then has few comparable pairs and therefore a large antichain.  Inside
that antichain every off-diagonal position is forbidden, so the remaining
obstruction is a smaller, quantitatively dense trajectory child.

## 1. Terminal historical decomposition

Let `V=[m]`.  Write

\[
F=D\cup F_0\cup H_1\cup\cdots\cup H_d,
\]

where `D={(i,i):i in V}` is the current diagonal, `F_0` has maximum row and
column degree at most `Delta_0`, and each `H_j` is a partial matching of
historical endpoint positions.  Along a causal branch the `H_j` are pairwise
edge-disjoint: every later rematching avoids every earlier historical cell.

Let `A` be the loopless allowed digraph, with arc `x to y` when `(x,y) notin F`.
Assume that `A` is acyclic, as in the trajectory-saturated side of PX293.

Call `(y,x) in H_j` a **historical back edge** when `A` contains a directed path
from `x` to `y`.

### Theorem PX294 -- PROVED

If `(y,x)` is a historical back edge in `H_j`, then deleting the single
ancestor constraint `H_j` makes a principal directed cycle executable.
Explicitly, if

\[
x=v_0\to v_1\to\cdots\to v_r=y
\]

is an allowed path, then after releasing `H_j` the cycle

\[
\boxed{v_0\to v_1\to\cdots\to v_r\to v_0}
\]

is allowed and moves `r+1` endpoints.

### Proof

The path edges are already allowed.  Pairwise edge-disjointness of the
historical matchings and `(y,x) notin F_0\cup D` imply that removing `H_j`
releases the closing edge `y to x`.  The resulting directed cycle is a
principal cyclic rematching by PX287. \(\square\)

This is a one-history reset: no family of ancestor constraints has to be
removed simultaneously.

## 2. No reset forces a sparse reachability poset

Let

\[
R(A)=\{(x,y):x\ne y\text{ and }A\text{ has a directed path }x\leadsto y\}.
\]

### Theorem PX295 -- PROVED

If `A` has no historical back edge, then

\[
\boxed{(y,x)\in F_0\quad\text{for every }(x,y)\in R(A).}
\]

Consequently

\[
\boxed{|R(A)|\le |F_0|\le m\Delta_0.}
\]

### Proof

For `(x,y) in R(A)`, the reverse cell `(y,x)` cannot be allowed, because it
would close a directed cycle in `A`.  It is not diagonal.  If it belonged to a
historical matching, it would be a historical back edge, contrary to the
hypothesis.  Hence it belongs to `F_0`.  Reversal is injective, and the row
sum of `F_0` is at most `m Delta_0`. \(\square\)

The estimate counts the full transitive closure, not merely the arcs of `A`.

## 3. Quantitative antichain child

Let `h(A)` be the maximum number of vertices in a directed chain of the
reachability order.

### Theorem PX296 -- PROVED

Under the no-reset hypothesis,

\[
\binom{h(A)}2\le m\Delta_0.
\]

Thus, with

\[
H_0=
\left\lfloor
\frac{1+\sqrt{1+8m\Delta_0}}2
\right\rfloor,
\]

there is an antichain `Q subseteq V` of exact order

\[
\boxed{
 s\ge
 \left\lceil\frac{m}{\max(1,H_0)}\right\rceil.
}
\]

No two distinct vertices of `Q` are joined by an allowed arc in either
direction.

### Proof

A chain of order `h` contributes all `binom(h,2)` ordered comparable pairs to
`R(A)`, so PX295 gives the first inequality.  Assign to each vertex the maximum
number of vertices in a directed path ending there.  There are at most `h(A)`
values, and vertices with the same value are incomparable.  One level therefore
has at least `ceil(m/h(A))` vertices.  Thin that level to exact order `s` if
needed. \(\square\)

For fixed `Delta_0`, this gives `s=Omega(sqrt(m/Delta_0))` whenever `m Delta_0`
is large.

## 4. Historical density inside the child

Write `H=H_1 union ... union H_d` and let `E_H(Q)` be the set of historical
cells in `Q times Q`.

### Theorem PX297 -- PROVED

For the antichain `Q` of order `s`,

\[
\boxed{
 |E_H(Q)|\ge s(s-1-\Delta_0).
}
\]

The right side is interpreted as zero when negative.

### Proof

There are `s(s-1)` off-diagonal cells in `Q times Q`.  None is allowed, by
antichainhood.  At most `s Delta_0` belong to the base graph, by the row-degree
bound.  Every remaining cell is historical. \(\square\)

Thus the no-reset outcome does not produce an arbitrary smaller block: it
produces an internally trajectory-dense child.

### Corollary PX298 -- PROVED

Some ancestor level satisfies

\[
\boxed{
 |H_j\cap(Q\times Q)|
 \ge
 \left\lceil
 \frac{s(s-1-\Delta_0)}{d}
 \right\rceil.
}
\]

The cells in this intersection are pairwise row- and column-disjoint.

### Proof

The historical matchings are edge-disjoint, so their intersection sizes sum to
`|E_H(Q)|`.  Average PX297 over the `d` levels.  Each intersection is a partial
matching because `H_j` is. \(\square\)

### Corollary PX299 -- PROVED

If one level has

\[
|H_j\cap(Q\times Q)|=s,
\]

then releasing `H_j` gives a fixed-point-free perfect matching on `Q`, hence a
principal directed-cycle cover and an executable reset moving every endpoint
of `Q`.

### Proof

A size-`s` partial matching from the `s` rows of `Q` to the `s` columns of `Q`
is a permutation.  Historical avoidance prevents a current diagonal cell from
appearing in `H_j`, so it has no fixed point.  Its permutation digraph is a
union of directed cycles of length at least two. \(\square\)

## 5. Consequence for the frontier

Every trajectory-saturated terminal core now has one of three explicit forms.

1. A historical back edge gives an immediate one-level reset by PX294.
2. A full ancestor layer on the extracted antichain gives a cycle-cover reset by
   PX299.
3. Otherwise PX296--PX298 produce a smaller antichain child with a certified
   number of disjoint positions from one ancestor level.

The third case is the remaining reset interface.  It is substantially narrower
than the PX293 obstruction: the allowed internal digraph is empty, the child
order is controlled by the reachability height, and its historical load is
explicit.

## 6. Verification

Run

```bash
python scripts/verify_product_historical_backedge_antichain.py
```

The verifier exhausts every DAG compatible with a fixed topological order
through order six.  It checks the back-edge cycle criterion, the transitive-
closure bound, the chain-height inequality, the longest-path antichain
extraction, and the historical-density estimate.
