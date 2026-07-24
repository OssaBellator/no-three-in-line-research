# Essential-edge factorization at the half-degree endpoint

CMR208 preserves a parent matching host until its minimum degree reaches
`ceil(t/2)`. Further certificate deletion may fail only when the chosen cell is
contained in every perfect matching of the residual host. Hall's theorem gives
an exact factorization of that obstruction.

Let `H=(L,R;E)` be a balanced bipartite graph with `|L|=|R|=t` and at least one
perfect matching. An edge is **essential** if it belongs to every perfect
matching of `H`.

## 1. Exact Hall characterization

### Theorem CMR210 — PROVED

An edge `e=uv`, with `u in L` and `v in R`, is essential if and only if there
are sets

\[
u\in A\subseteq L,
\qquad
v\in B\subseteq R
\]

such that

\[
|A|=|B|,
\qquad
N_H(A)=B,
\qquad
N_H(v)\cap A=\{u\}.
\]

For every such pair `(A,B)`, perfect matchings factor canonically:

\[
\boxed{
\operatorname{PM}(H)
\cong
\{e\}
\times
\operatorname{PM}\bigl(H[A\setminus\{u\},B\setminus\{v\}]\bigr)
\times
\operatorname{PM}\bigl(H[L\setminus A,R\setminus B]\bigr).
}
\]

### Proof

Suppose first that `e` is essential. Then `H-e` has no perfect matching. Hall's
theorem supplies `A subseteq L` with

\[
|N_{H-e}(A)|<|A|.
\]

Since `H` itself has a perfect matching,

\[
|N_H(A)|\ge|A|.
\]

The two neighbourhoods differ by at most the endpoint `v`, so equality is
forced throughout:

\[
|N_{H-e}(A)|=|A|-1,
\qquad
N_H(A)=N_{H-e}(A)\cup\{v\},
\qquad
|N_H(A)|=|A|.
\]

In particular `u in A`, the edge `uv` is the only edge from `A` to `v`, and
with `B=N_H(A)` all three displayed conditions hold.

Conversely, suppose such `A,B` exist. Every perfect matching must match the
`|A|` vertices of `A` bijectively onto the `|B|=|A|` vertices of `B`, because
there are no edges from `A` to `R\setminus B`. The vertex `v` has only the
neighbour `u` inside `A`, so every perfect matching contains `uv`.

After fixing `uv`, no matching edge crosses between the two displayed vertex
pairs: all remaining vertices of `A` match inside `B`, and cardinality then
forces the complements to match internally. This gives the product
factorization. ∎

## 2. Minimum-degree constraints

### Theorem CMR211 — PROVED

Assume `H` has minimum degree at least `delta`, and let `uv` be essential with
Hall factor `(A,B)`. Put `a=|A|=|B|`. Then

\[
\boxed{
\delta\le a\le t-\delta+1.
}
\]

### Proof

Every vertex of `A` has all its neighbours in `B`, so `a>=delta`.

The right vertex `v` has only one neighbour in `A`, namely `u`. Its remaining
at least `delta-1` neighbours lie in `L\setminus A`, whose size is `t-a`.
Thus

\[
t-a\ge\delta-1,
\]

which is the upper bound. ∎

## 3. Odd half-degree hosts have no essential edge

### Corollary CMR212 — PROVED

Let

\[
t=2h+1,
\qquad
\delta(H)\ge h+1.
\]

Then `H` has no essential edge.

Consequently, for every edge `e in E(H)`, the graph `H-e` still has a perfect
matching.

### Proof

CMR211 would force

\[
h+1\le a\le(2h+1)-(h+1)+1=h+1,
\]

so `a=h+1=delta`. Every vertex of `A` has degree at least `a` and all its
neighbours lie in `B`, which also has size `a`. Hence `H[A,B]` is complete.
The vertex `v` is then adjacent to every vertex of `A`, contradicting
`N_H(v) cap A={u}` because `a>=3`. ∎

Thus the odd-size half-degree endpoint is fully deletable one edge at a time:
there is no forced parent cell.

## 4. Even half-degree hosts split off a complete factor

### Theorem CMR213 — PROVED

Let

\[
t=2h,
\qquad
h\ge3,
\qquad
\delta(H)\ge h,
\]

and suppose `uv` is essential. Then its Hall factor satisfies

\[
\boxed{|A|=|B|=h+1.}
\]

Moreover

\[
\boxed{
H[A\setminus\{u\},B\setminus\{v\}]
=K_{h,h}.
}
\]

Hence

\[
\operatorname{PM}(H)
\cong
\{uv\}
\times S_h
\times
\operatorname{PM}(H_0),
\]

where `H_0=H[L\setminus A,R\setminus B]` is a balanced host of size `h-1` and
`S_h` denotes the `h!` matchings of the complete factor.

### Proof

CMR211 gives

\[
h\le a\le h+1.
\]

If `a=h`, every vertex of `A` has degree at least `h` and all neighbours in the
`h`-set `B`; thus `H[A,B]=K_{h,h}`, again contradicting the unique neighbour
condition at `v`. Hence `a=h+1`.

Every vertex of `A\setminus\{u\}` is not adjacent to `v`, because `uv` is the
only edge from `A` to `v`. It has degree at least `h`, all inside
`B\setminus\{v\}`, which has exactly `h` vertices. Therefore it is adjacent to
all of `B\setminus\{v\}`. This proves the complete factor, and CMR210 gives the
matching product. ∎

The only essential-edge obstruction at the half-degree threshold is therefore
a rigid even-size bridge with one forced edge and one complete half-size
matching component.

## 5. Certificate deletion or factorization

### Corollary CMR214 — PROVED

Let `H` be a half-degree residual parent host from CMR208, and let `Q` be any
rank-`1/2/3` candidate certificate realized by at least one perfect matching of
`H`.

At least one of the following holds.

1. **Deletable certificate cell.** Some prescribed edge `e in Q` is not
   essential. Then `H-e` has a perfect matching and no matching of `H-e`
   realizes `Q`.
2. **Forced factor certificate.** Every prescribed edge of `Q` is essential.
   Each is present in every perfect matching and has the exact Hall
   factorization of CMR210. If `t` is odd, this alternative is impossible. If
   `t` is even, every prescribed edge splits off the rigid complete factor from
   CMR213.

### Proof

Deleting any prescribed edge destroys the entire cylinder `Q`. If one such
edge is not essential, the first alternative follows by definition.
Otherwise every prescribed edge is essential and the structural theorems
apply. ∎

## 6. Revised internal endpoint

CMR209 reduces internal no-return to repeated replacement of a linear
rank-three family. CMR214 now gives the next deterministic step for every
replacement certificate:

- at odd residual size, one of its cells can always be deleted while retaining
  a parent matching;
- at even residual size, failure of deletion exposes a forced bridge and a
  complete half-size matching factor.

The remaining theorem is to iterate this delete-or-factor process while
retaining enough candidate-cover information. A natural induction parameter is

\[
(\text{host size},\ \text{number of essential factors},\ \text{remaining envelope depth}).
\]

One must show that recursive forced factors cannot support a balanced cycle of
new candidate-only triples without either producing a deletable certificate,
forcing an envelope expansion, or exhausting the quotient/carry signature
budget.

No all-`n` theorem is claimed here. Essential-edge equivalence, factor sizes,
and small half-degree hosts are checked in
[`scripts/verify_prime_power_essential_edges.py`](../scripts/verify_prime_power_essential_edges.py).
