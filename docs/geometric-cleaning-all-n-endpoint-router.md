# All-`n` completion endpoints after geometric cleaning

**Branch:** `research/geometric-cleaning`

The all-`n` work has two proved exact endpoints which can terminate geometric
cleaning before the unresolved local-resampling theorem is needed.

1. The complete clone-space local lemma closes a near-complete host with small
   row/column triple load.
2. The superregular-resampling switching theorem gives fixed-rank spread for the
   uniform two-layer measure of a dense host; a global first-moment bound then
   closes any instance with sufficiently small total candidate-triple mass.

This note records both criteria in one GC5 router.  Neither criterion proves that
GC1--GC4 reach its hypotheses.

## Complete-clone endpoint

Let `G subseteq [n]x[n]` be a candidate-cell host.  Write `m_*` for the maximum
number of unavailable cells in one row or column and `tau_*` for the maximum
number of candidate collinear triples with distinct rows and columns incident
to one row or column.

## GC5a -- near-complete local-load endpoint -- PROVED

If

\[
\boxed{
\frac{m_*}{n}
+
\frac1{2n-1}
+
\frac{32\tau_*}{(2n)(2n-1)(2n-2)}
\le
\frac1{24},
}
\]

then `G` contains exactly `2n` distinct cells, two in every row and column, with
no three collinear.

### Proof

Create two clones of every row and column and choose a perfect matching of the
`2n` by `2n` complete clone graph.  Forbid unavailable clone edges, the two
disjoint-lift pairs projecting to one repeated cell, and all clone lifts of
candidate collinear triples.  A fixed clone vertex receives probability load at
most the displayed left side: unavailable cells contribute `m_*/n`, duplicate
pairs contribute `1/(2n-1)`, and the `32` lifts containing that clone contribute
the last term.  If the load is at most `1/24`, the matching-space lopsided local
lemma with event parameter twice the event probability avoids every bad event.
Projection gives the required configuration. QED.

For `n>=100`, the sufficient bounds

\[
m_*\le n/100,
\qquad
\tau_*\le n^3/200
\]

follow immediately.

## Dense two-layer endpoint

Let `H` be a bipartite host on two copies of `[n]`.  A state consists of two
edge-disjoint perfect matchings of `H`, interpreted as two permutation layers.
Assume this state space is nonempty and put

\[
d_{\min}=\min_v d_H(v),
\qquad
L=2d_{\min}-n-3.
\]

Let `T(H)` be the number of real nonaxis collinear triples of host cells with
three distinct rows and columns.

## GC5b -- dense-host global triple-mass endpoint -- PROVED

If `L>=3` and

\[
\boxed{
8T(H)<(L+1)_3,
}
\]

then `H` contains two edge-disjoint perfect matchings whose union has no three
collinear.

### Proof

For each real candidate triple and each assignment of its three cells to one of
the two layers, form the corresponding labelled rank-three cylinder whenever it
is globally compatible.  There are at most `2^3=8` such cylinders per real
triple.  By the dense-host switching bound, every compatible labelled
rank-three cylinder has probability at most `1/(L+1)_3` under the uniform
two-layer measure.  The expected number of occurring labelled bad cylinders is
therefore at most

\[
\frac{8T(H)}{(L+1)_3}<1.
\]

Some state contains none.  Any real collinear triple in its union would realize
one of the labelled cylinders, a contradiction. QED.

When every row and column loses at most `delta n` host cells,

\[
d_{\min}\ge(1-\delta)n,
\qquad
L\ge(1-2\delta)n-3.
\]

Thus it is sufficient that

\[
8T(H)
<
\bigl((1-2\delta)n-2\bigr)_3
\]

whenever the falling-factorial argument is positive and the two-layer state
space is nonempty.

## GC5c -- exact endpoint router -- PROVED

A geometric-cleaning history may terminate successfully as soon as either:

1. its candidate-cell host satisfies GC5a; or
2. its dense two-layer host satisfies GC5b.

Failure of both tests has an explicit witness:

- the clone route has either excessive row/column holes or one row/column with
  excessive candidate-triple load;
- the dense route has either insufficient minimum degree, an empty two-layer
  matching space, or global candidate-triple mass at least `(L+1)_3/8`.

These witnesses must be retained by GC4 rather than replaced by a generic
"endpoint failure" label.

### Proof

The two success statements are GC5a and GC5b.  Negating their hypotheses gives
the displayed alternatives. QED.

## Relation to the superregular frontier

GC5b uses only cylinder rarity and global first moment.  It can handle
`Theta(n^3)` candidate triples with an explicit constant, but cannot exploit a
large global family whose local conflict neighbourhoods are sparse.  That
remaining regime is exactly the open superregular lopsided-resampling endpoint.

GC5a instead exploits local load but requires the complete clone matching space
and a near-complete original host.  The two criteria are complementary:

- use GC5a after strong row/column cleaning;
- use GC5b after dense-host regularization with small total triple mass;
- invoke the open superregular local-load theorem only when neither proved
  endpoint applies.

## Finite check

`scripts/verify_geometric_all_n_endpoints.py` enumerates small grid hosts and all
ordered pairs of edge-disjoint perfect matchings.  It checks the dense-host
rank-three cylinder bound and verifies that every state selected by the
first-moment criterion is free of real collinear triples.