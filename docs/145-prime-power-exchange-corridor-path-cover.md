# Exchange corridors compress essential-edge ancestry to linear cycle covers

CMR429--CMR432 reduce one deletion pass to a final essential matching core of
size at most `t`, but the resulting edge-set ancestry ledger can still contain
cubicly many certificate links.  The matching structure gives a sharper
representation.  Relative to one fixed perfect matching, alternating exchange
cycles are ordinary directed cycles in a contracted digraph.  Deleting one
edge turns the newly essential matching edges into acyclic vertices lying on
one directed source-to-sink corridor.

Reachability in that corridor is a partial order.  A chain can be exchanged in
one alternating cycle, while an antichain consists of edges which no single
exchange cycle through the deleted edge can address together.  Dilworth's
theorem therefore identifies the exact number of historical exchange cycles
needed to cover one first-essentiality layer.

Let

\[
G=(L,R;E),
\qquad
L=\{\ell_1,\ldots,\ell_t\},
\qquad
R=\{r_1,\ldots,r_t\},
\]

and fix a perfect matching

\[
M=\{m_j=\ell_jr_j:1\le j\le t\}.
\]

Define the **matching contraction digraph** `D_M(G)` on `[t]` by placing an arc

\[
j\longrightarrow k
\]

for every nonmatching edge `\ell_jr_k\in E\setminus M`.

## 1. Essential matching edges are directed-cycle vertices

### Theorem CMR433 — PROVED

For `x\in[t]`, the matching edge `m_x` is nonessential in `G` if and only if
`x` lies on a directed cycle of `D_M(G)`.

### Proof

A directed cycle

\[
x_1\to x_2\to\cdots\to x_s\to x_1
\]

encodes the `M`-alternating cycle using the nonmatching edges
`\ell_{x_j}r_{x_{j+1}}` and the matching edges `m_{x_{j+1}}`.  Flipping this
cycle gives a perfect matching avoiding every matching edge on the cycle.

Conversely, if a perfect matching `M'` avoids `m_x`, then the component of
`M\triangle M'` containing `m_x` is an `M`-alternating cycle.  Contracting its
matching edges gives a directed cycle of `D_M(G)` containing `x`. ∎

## 2. Exact one-edge exchange corridor

Let

\[
f=\ell_ur_v\notin M,
\qquad
\alpha=(u\to v),
\]

and assume `M` is a perfect matching of `G-f`.  Put

\[
D=D_M(G),
\qquad
D^-=D-\alpha.
\]

A matching edge is **newly essential at `f`** when it is nonessential in `G`
but essential in `G-f`.

### Theorem CMR434 — PROVED

A matching edge `m_x` is newly essential at `f` if and only if both of the
following hold in `D^-`:

1. `x` lies on no directed cycle;
2. some directed path from `v` to `u` passes through `x`.

Equivalently, `x` is a singleton acyclic strongly connected component of
`D^-` lying in the directed `v`-to-`u` corridor.

### Proof

By CMR433, newly essential means that `x` lies on a directed cycle of `D`, but
on no directed cycle of `D^-`.  Every directed cycle of `D` containing `x`
must therefore use `\alpha`.  Removing `\alpha=u\to v` from such a cycle leaves
a directed path from `v` to `u` through `x`.

Conversely, suppose `x` lies on no directed cycle of `D^-` and on a directed
`v`-to-`u` path `P`.  Then `P\cup\{\alpha\}` is a directed cycle of `D`
containing `x`, so `m_x` is nonessential in `G` by CMR433.  It is essential in
`G-f` because `x` lies on no directed cycle of `D^-`. ∎

## 3. Reachability chains give simultaneous exchange cycles

Let `S_f` be the set of vertices corresponding to matching edges newly
essential at `f`.  Define

\[
x\preceq_f y
\]

when `x=y` or `D^-` contains a directed path from `x` to `y`.

### Theorem CMR435 — PROVED

The relation `\preceq_f` is a partial order on `S_f`.  If

\[
x_1\prec_f x_2\prec_f\cdots\prec_f x_k
\]

is a chain, then `D^-` contains a directed path from `v` to `u` passing through
`x_1,\ldots,x_k` in that order.  Consequently `G` contains one
`M`-alternating cycle through `f` and all matching edges

\[
m_{x_1},\ldots,m_{x_k}.
\]

Flipping that cycle produces a perfect matching of `G` which contains `f` and
simultaneously avoids all `k` matching edges.

### Proof

Reflexivity and transitivity are immediate.  If distinct `x,y\in S_f`
satisfied both `x\preceq_f y` and `y\preceq_f x`, then they would lie in one
nontrivial strongly connected component of `D^-`, contradicting CMR434.
Hence the relation is antisymmetric.

CMR434 gives a path from `v` to `x_1`, the chain gives paths from `x_j` to
`x_{j+1}`, and CMR434 gives a path from `x_k` to `u`.  Work in the condensation
DAG of `D^-`.  Concatenating these paths and removing repeated subwalks gives a
directed `v`-to-`u` path through all chain vertices in order.  Adjoining
`\alpha` gives a directed cycle of `D`, hence an `M`-alternating cycle in `G`.
The usual alternating-cycle flip has the stated effect. ∎

This is a genuine batch exchange: one historical deletion edge can be traded
against every newly essential matching edge lying in one reachability chain.

## 4. Exact exchange-cycle cover number

Call an **`f`-exchange cycle** an `M`-alternating cycle in `G` containing `f`.
Such a cycle **covers** a newly essential edge when it contains that matching
edge.  Let

\[
w_f=\operatorname{width}(S_f,\preceq_f)
\]

be the maximum size of a reachability antichain.

### Theorem CMR436 — PROVED

The minimum number of `f`-exchange cycles whose union covers every newly
essential matching edge is exactly

\[
\boxed{w_f}.
\]

### Proof

Every `f`-exchange cycle becomes, after deleting `f` and contracting `M`, one
directed `v`-to-`u` path in `D^-`.  The vertices of `S_f` lying on one such path
are linearly ordered by reachability.  Therefore every exchange-cycle cover
induces a chain cover of the poset, so it uses at least `w_f` cycles by
Dilworth's theorem.

Conversely, Dilworth partitions `S_f` into `w_f` chains.  Apply CMR435 to each
chain.  The resulting `w_f` exchange cycles cover every newly essential edge.
∎

Thus the obstruction at one deletion is not the number of ancestry links.  It
is the width of one explicit reachability poset.

## 5. Batch-or-branch dichotomy

### Corollary CMR437 — PROVED

Let

\[
n_f=|S_f|.
\]

If `n_f>0`, then at least one of the following holds.

1. **Batch exchange.** One `f`-exchange cycle simultaneously avoids at least
   `\lceil\sqrt{n_f}\rceil` newly essential matching edges.
2. **Branch certificate.** There is an antichain of at least
   `\lceil\sqrt{n_f}\rceil` newly essential matching edges, and no single
   `f`-exchange cycle contains two of those edges.

### Proof

Let `q=\lceil\sqrt{n_f}\rceil`.  If the width is at least `q`, choose an
antichain of size `q`.  Every exchange cycle meets it in at most one vertex,
because the vertices on one cycle form a chain.

Otherwise the width is at most `q-1`.  Dilworth gives a partition into at most
`q-1` chains, so one chain has size at least

\[
\left\lceil\frac{n_f}{q-1}\right\rceil\ge q.
\]

Apply CMR435 to that chain. ∎

The first outcome gives simultaneous historical resampling.  The second gives
a precise branching obstruction suitable for p-adic, carry, Hall-separator, or
envelope analysis.

## 6. Linear temporal cycle compression

Return to one certificate-directed deletion pass

\[
G_0\supset G_1\supset\cdots\supset G_d,
\qquad
G_i=G_{i-1}-f_i,
\]

and choose any perfect matching `M_i` of `G_i`.  Let `S_i` be the matching edges
of `M_i` which first become essential when `f_i` is deleted, and let `w_i` be
the width of their CMR435 reachability poset.

### Corollary CMR438 — PROVED

The final essential core can be covered, at its respective first-essentiality
times, by at most

\[
\boxed{
\sum_{i=1}^d w_i
\le
\sum_{i=1}^d|S_i|
\le t
}
\]

historical alternating exchange cycles.

More precisely, for each `i`, exactly `w_i` cycles through `f_i` cover every
matching edge first becoming essential at step `i`.

### Proof

CMR436 gives the exact cover number `w_i` at step `i`.  Trivially
`w_i\le|S_i|`.  By CMR430 the first-essentiality layers are disjoint and their
union is the final essential core, which has size at most `t` by CMR429.  Sum
over `i`. ∎

CMR438 compresses the cubic edge-set ancestry ledger of CMR431--CMR432 to a
linear family of **batch exchange cycles**, while retaining the time at which
each cycle is valid.  These cycles need not coexist in one residual host, so a
global simultaneous flip is not yet proved.

The revised frontier is one of the following.

1. Lift a large low-overlap subfamily of the at most `t` historical cycles to a
   common host epoch and flip them together.
2. Show that failure of such lifting forces a large CMR437 antichain, then
   convert that branch width into a Hall separator, strict host decomposition,
   p-adic/carry concentration, or envelope expansion.
3. Extend the same corridor representation to repeated compatible local
   ancestor resets outside the packet-loss deletion pass.

No all-`n` theorem is claimed here.  Directed-cycle equivalence, the exact
corridor characterization, chain batching, path-cover width, and finite
small-digraph cases are checked in
[`scripts/verify_prime_power_exchange_corridor.py`](../scripts/verify_prime_power_exchange_corridor.py).
